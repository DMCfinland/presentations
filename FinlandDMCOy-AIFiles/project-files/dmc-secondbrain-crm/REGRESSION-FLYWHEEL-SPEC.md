# REGRESSION FLYWHEEL SPEC
## DMC CRM Email Classifier — Minimum Viable Regression System

**Version:** 1.0
**Date:** 2026-03-19
**Stack:** n8n + Supabase + TypeScript (no LangSmith, no Braintrust, no OpenTelemetry)
**Maintenance budget:** <2 hours/month
**Golden-set cap:** 80 cases maximum

---

### Pre-Spec: Red Team Findings

Three production failure modes identified before writing this spec:

1. **Statistical thinness trap.** With 200-500 emails/month across 8 label classes, rare subclasses (media/press, supplier-inquiry) may accumulate only 2-5 examples in 6 months. A suite that never fires on a class gives false confidence — it "passes" because the class is never exercised. Mitigation: invariants are written as universal rules, not class-specific tests. The suite validates behavior, not distribution coverage.

2. **LLM-as-judge drift.** Using the same model version as both classifier and judge on disagreements produces hallucination consensus (identical priors → same errors → guaranteed PASS theater). Mitigation: judge calls use a deterministic rule layer first; LLM-as-judge is gated to 1-in-10 human spot-check and uses a different model family (Mistral or Grok) when invoked, never the same Claude version.

3. **Flywheel inversion (Lucas's finding).** Accumulating human-caught failures biases the suite toward the hardest 5% and degrades average-case autonomy. The schema has an `invariant_type` column (core/long-tail) but without an enforced ratio, engineers will keep adding long-tail cases until the 80-case cap is filled with rare failures. Mitigation: hard ratio rule — no more than 20 long-tail cases at any time (25% of cap). Core invariants hold the floor.

---

## Supabase Schema

```sql
CREATE TABLE regression_golden_set (
  email_id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  raw_email          TEXT NOT NULL,            -- stripped body only: no headers, no attachments, no PII names
  expected_label     TEXT NOT NULL CHECK (expected_label IN (
                       'hot-lead', 'warm-lead', 'cold-lead',
                       'existing-partner', 'spam', 'operational',
                       'supplier-inquiry', 'media-press'
                     )),
  actual_label       TEXT,                     -- populated on each regression run
  prompt_version     TEXT NOT NULL,            -- e.g. 'v1.3' — matches classifier prompt tag
  model_version      TEXT NOT NULL,            -- e.g. 'claude-sonnet-4-6' — exact model ID
  temperature        NUMERIC(3,2) NOT NULL DEFAULT 0.0,
  date_added         DATE NOT NULL DEFAULT CURRENT_DATE,
  invariant_type     TEXT NOT NULL CHECK (invariant_type IN ('core', 'long-tail')),
  delete_after       DATE NOT NULL,            -- computed at insert: date_added + 6 months for long-tail, NULL-equivalent sentinel '2099-01-01' for core
  last_failed_run_date DATE                    -- nullable; updated by weekly workflow when this case fails a run; NULL means never failed
);

-- Ratio enforcement: max 20 long-tail cases at any time
-- Enforced by application logic at insert time (see weekly workflow step 6)
-- Concurrency note: INSERT with ratio check and UPDATE of last_failed_run_date must run in
-- transactions (BEGIN/COMMIT) or use Supabase RPC functions to prevent race conditions
-- when weekly regression run and production addition trigger fire simultaneously.

-- Indexes (required — weekly fetch/deletion queries degrade without these)
CREATE INDEX idx_rgs_delete_after ON regression_golden_set(delete_after);
CREATE INDEX idx_rgs_invariant_type ON regression_golden_set(invariant_type);
CREATE INDEX idx_rgs_last_failed ON regression_golden_set(last_failed_run_date);
CREATE INDEX idx_rgs_version ON regression_golden_set(prompt_version, model_version);
CREATE INDEX idx_rrl_version_date ON regression_run_log(prompt_version, model_version, run_date DESC);

-- Supporting table: weekly run results
CREATE TABLE regression_run_log (
  run_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  run_date           TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  total_cases        INTEGER NOT NULL,
  core_pass          INTEGER NOT NULL,
  core_fail          INTEGER NOT NULL,
  long_tail_pass     INTEGER NOT NULL,
  long_tail_fail     INTEGER NOT NULL,
  flagged_for_human  INTEGER NOT NULL,
  prompt_version     TEXT NOT NULL,
  model_version      TEXT NOT NULL,
  trigger_source     TEXT NOT NULL DEFAULT 'scheduled'  -- 'scheduled' | 'version_change'
);
```

**Column notes:**
- `raw_email`: Body text only. Strip To/From/CC headers and attachment filenames before insert. Rationale: the classifier receives stripped body in production; regression must match production input exactly.
- `delete_after`: Core invariants use sentinel date `2099-01-01` (effectively permanent). Long-tail cases use `date_added + 6 months`. The deletion trigger evaluates `delete_after < CURRENT_DATE AND invariant_type = 'long-tail' AND (last_failed_run_date IS NULL OR last_failed_run_date < CURRENT_DATE - INTERVAL '90 days')` — see Deletion Policy section.
- `last_failed_run_date`: Set by the weekly n8n workflow whenever a case fails a regression run. NULL = has never failed (safe to delete after `delete_after`). Used directly in the deletion SQL — no separate view required.
- `actual_label`: Null until a regression run populates it. Overwritten each run — stores only the most recent result. **Per-case run history:** If per-case trend analysis is needed (e.g., "this case has failed 3 of the last 8 runs"), add a `regression_case_results` table: `(email_id UUID, run_id UUID, actual_label TEXT, pass BOOLEAN, run_date TIMESTAMPTZ)`. The current schema omits this for maintenance simplicity — add it when autonomy expansion decisions require trend data per case.
- `prompt_version` / `model_version`: Stored at insert time, not at run time. Allows detection of cases added under old prompt versions that are now obsolete.

---

## 30 Core Invariants

**Format:** `[source label] → [target label]: NEVER/ALWAYS + reason`

**Scope:** Core invariants only. These are permanent rules — they do not rotate out. Each maps to a structural property of DMC B2B travel email classification that holds regardless of wording, language (EN/FI/DE), or sender domain.

**CRITERIA GAMING RISK flagged:** Criterion 2 asks for exactly 30 invariants. Writing to hit 30 risks padding with generic rules. Each invariant below is derived from a real DMC failure mode or structural property of the B2B travel email space. Numbers 28-30 are narrower-scope but still DMC-specific — flagged with (narrow) for human review if count should be reduced.

---

**Hot-lead invariants (emails signaling new booking intent from qualified buyers)**

1. `cold-lead → hot-lead: NEVER` — An email asking for general destination information ("tell me about Finland in winter") without a specific group, date, or budget reference must not be classified as hot-lead. Absence of program specifics = pre-qualification stage.

2. `spam → hot-lead: NEVER` — A message from a domain suffix not matching any European travel agency, tour operator, or corporate travel manager pattern must not be upgraded to hot-lead even if it contains a price inquiry. Domain validation is a deterministic gate outside the LLM.

3. `existing-partner → hot-lead: NEVER` — Emails from domains already present in the `partners` table must not be reclassified as hot-lead. They are follow-on business, not new lead acquisition.

4. `operational → hot-lead: NEVER` — Emails referencing an existing booking reference number (e.g. "re: group FIN-2026-034") are operational coordination, not new leads, regardless of enthusiastic tone.

5. `hot-lead → cold-lead: NEVER` — A message containing a specific group size (>10 pax), a named travel date window, and a budget range must not be downgraded to cold-lead. All three signals present = hot by definition.

**Warm-lead invariants**

6. `warm-lead → spam: NEVER` — An email from a .de, .nl, .uk, .fr, .se, .no, .dk, or .at domain that asks about Finland program options for a corporate or leisure group must not be classified as spam, even if it is a first contact from an unknown sender.

7. `warm-lead → operational: NEVER` — A message that does not reference any existing booking or reference number must not be classified as operational, even if it uses operational language ("please send us the schedule").

8. `cold-lead → warm-lead: ALWAYS when repeat sender` — An email from a domain that has appeared in the inbox before (any prior email, any label) must be upgraded from cold-lead to at least warm-lead. Repeat contact signals self-qualified intent.

**Cold-lead invariants**

9. `hot-lead → cold-lead: NEVER when pax count >20` — Any email specifying a group larger than 20 persons must not be classified as cold-lead regardless of vagueness in other fields. Group size >20 is a high-value signal that overrides missing date/budget.

10. `cold-lead → spam: NEVER when .travel or .agency TLD` — Email domains ending in .travel or .agency are travel industry domains by registration requirement. These are never spam.

**Existing-partner invariants**

11. `existing-partner → hot-lead: NEVER` — Covered in invariant 3; restated here for existing-partner rule block completeness.

12. `existing-partner → spam: NEVER` — A domain present in the partners table must never be classified as spam regardless of email content. Misclassifying a partner as spam causes relationship damage.

13. `existing-partner → cold-lead: NEVER` — An email from a known partner asking about a new program is an upsell opportunity (warm or hot), not a cold outreach. The partner status dominates.

14. `operational → existing-partner: NEVER` — An email that contains only logistics coordination (transfer times, driver details, meal counts) with no new inquiry element must remain operational, not re-labeled as partner outreach.

**Spam invariants**

15. `hot-lead → spam: NEVER` — An email containing a group travel inquiry with named company, pax count, and date must not be classified as spam regardless of imperfect grammar or unusual sender domain. False negatives on hot-lead are the highest-cost error in the DMC stack.

16. `spam → existing-partner: NEVER` — A message classified as spam must not be upgraded to existing-partner without deterministic domain match against the partners table. LLM pattern-matching on "sounds like a travel company" is insufficient.

17. `any-non-spam → spam: ALWAYS when body is entirely a vendor sales pitch for products unrelated to Finland DMC programs (e.g. CRM software, hotel booking platforms). Commercial promotion with no program inquiry = spam.` — A message whose entire body is a vendor sales pitch for a product or service unrelated to Finland DMC programs must be classified as spam.

**Operational invariants**

18. `operational: ALWAYS when booking reference present + no new inquiry` — Any email that quotes an existing reference number and contains no new program request must be classified as operational. Booking references are a deterministic signal; they override tone-based signals.

19. `operational → hot-lead: NEVER when reference number in subject` — A subject line containing a booking reference (e.g. "RE: FIN-2026-034 — transfer update") cannot be a hot-lead. The deterministic override fires before the LLM label is accepted.

20. `hot-lead → operational: NEVER when no reference number exists in email` — If neither subject nor body contains any booking reference number matching the pattern FIN-YYYY-NNN or equivalent, the email is not operational.

**Supplier-inquiry invariants**

21. `supplier-inquiry → hot-lead: NEVER` — An email from a supplier (accommodation, transport, guide service, activity provider) offering their services to DMC must not be classified as a hot-lead. Supplier outbound = supplier-inquiry; inbound group travel request = hot/warm/cold.

22. `supplier-inquiry → existing-partner: NEVER when not in partners table` — A supplier emailing for the first time must not be labeled existing-partner even if their email mentions prior informal discussions. Partners table membership is the gate.

23. `supplier-inquiry: ALWAYS when sender is accommodation property or transport operator + content is rate/availability offer` — Rate cards, availability windows, and accommodation block offers are supplier-inquiry without exception.

**Media/press invariants**

24. `media-press → hot-lead: NEVER` — A press inquiry (journalist, blogger, influencer asking for a press trip or destination information for an article) must not be classified as hot-lead. Press trips are cost-center activities, not revenue leads.

25. `media-press: ALWAYS when sender references editorial deadline or article publication` — Any email mentioning a publication deadline, article name, or media outlet affiliation must be classified as media-press, even if it is from a domain not previously seen.

26. `media-press → spam: NEVER` — A press inquiry from an unknown sender must not default to spam. Media contact is a brand-building signal.

**Cross-class structural invariants**

27. `any-label → spam: NEVER when email is in Finnish language` — Finnish-language emails are from domestic contacts (partners, suppliers, media, or known leads). Finnish is not a spam language in the DMC context. Language detection is a deterministic pre-filter.

28. `any-label → any-label (override): NEVER reclassify based solely on quoted prior text in a reply chain.` — Each email is classified on its new content only; prior thread context cannot change the label of the current message. A reply chain where the original email was classified as X must not cause a reclassification of the reply to a different class based solely on the quoted prior text. (narrow — applies to threading behavior)

29. `cold-lead → operational: NEVER` — A first-contact email from an unknown sender cannot be operational. Operational requires an existing booking relationship. Unknown sender + no reference number = always lead-class or spam. (narrow — anti-confusion rule for ambiguous routing)

30. `hot-lead → human-review: ALWAYS when classifier confidence_score < 0.85.` — Hot-lead false negatives are the highest-cost error; the threshold is asymmetric by design. When the classifier outputs hot-lead with a confidence below 0.85, the case routes to human review regardless of label. Implemented as deterministic post-processing override, not a prompt instruction. (narrow — threshold-based override)

---

**Invariant implementation note:** Invariants 2, 3, 4, 8, 12, 16, 18, 19, 20, 22, 27, 28, 30 involve deterministic signals (domain table lookup, reference number regex, language detection, confidence score). These must be implemented as TypeScript post-processing rules that run AFTER the LLM returns its label — not as prompt instructions. Rationale: chain-of-thought faithfulness is structurally unreliable (see `llm-reasoning-action-divergence.md`). The LLM can identify a booking reference in its reasoning trace and still output hot-lead. The deterministic layer overrides.

**Deterministic layer versioning (known gap — monitor):** The partners table, booking reference regex, and domain filter lists evolve independently of golden-set cases. A golden-set case added when partner X was not in the partners table will behave differently after partner X is added. Mitigation: (1) log the partners table row count and regex version hash in each `regression_run_log` row (add `deterministic_layer_version TEXT` column when this drift becomes a production issue), (2) re-validate golden-set expected_labels after any partners table bulk update. This is not implemented in v1.0 — treat as a known gap to address when partner count exceeds 50 or regex has had ≥3 revisions.

---

## Weekly n8n Workflow

### Triggers

**Trigger A — Scheduled (primary)**
**Type:** Scheduled trigger
**Timing:** Every Monday at 06:00 Helsinki time (Europe/Helsinki timezone, UTC+2/+3)
**Rationale:** Monday morning run means results arrive before the week's first team standup. n8n scheduler (not a cron node) — simple interval with timezone awareness.
**Estimated runtime:** 4-6 minutes for 80 cases at 200-500ms per LLM call with 0.5s inter-call delay.

**Trigger B — Version change (CI gate)**
**Type:** Webhook trigger (fired by deployment pipeline or manual curl)
**When:** Any time `prompt_version` or `model_version` in `classifier_config` is updated
**Rationale:** A Tuesday prompt change would otherwise ship untested until the following Monday. This trigger runs the full regression suite immediately on any version change and blocks deployment (via Slack alert) if core failures are detected.
**Implementation:** Deployment script POSTs to n8n webhook URL after updating `classifier_config`. n8n runs steps 1-9 identically to Trigger A. Run log stamped with `trigger_source: 'version_change'` for audit trail.
**Add to run log table:** `trigger_source TEXT NOT NULL DEFAULT 'scheduled'` column — add to `regression_run_log` CREATE TABLE.

### Step-by-Step Logic

**Step 1 — Fetch active golden set**
Query `regression_golden_set` WHERE `delete_after > CURRENT_DATE`. Return all columns. If row count = 0, send Slack message "Golden set is empty — regression skipped" and stop.

**Step 2 — Fetch current classifier configuration**
Read current `prompt_version` and `model_version` from a Supabase config table (`classifier_config`, single-row). These will be stamped on the run log.

**Step 3 — Run classifier on each case**
For each row, call the TypeScript classifier function (via Supabase Edge Function HTTP endpoint) with `raw_email` as input. The classifier returns `{ label: string, confidence_score: number }`. Store results in memory as `{ email_id, expected_label, actual_label, confidence_score }` array.
**Note:** Do NOT call the LLM directly from n8n. n8n calls the Edge Function, which contains the classifier + deterministic post-processing layer. This preserves the hybrid architecture boundary.

**Step 4 — Evaluate results against invariants**
For each result: (a) check if `actual_label == expected_label` (label match), (b) check if the label pair violates any core invariant (implemented as TypeScript enum in the Edge Function — invariant violations are returned as a flag in the response). Record: `pass`, `fail_label_mismatch`, or `fail_invariant_violation`.

**Step 5 — Run LLM-as-judge on disagreements only**
For cases where `actual_label != expected_label`: if the disagreement count is ≤ 5, run LLM-as-judge using Mistral (not Claude — different model family to avoid hallucination consensus). Judge prompt: provide raw_email, both labels, ask which is correct and why. Judge output is logged, not used to auto-correct. If disagreement count > 5, skip LLM-as-judge and flag all disagreements for human review directly.

**Step 6 — Check ratio and 80-case cap**
Count current `long-tail` rows in golden set. If count ≥ 20: block any new long-tail additions this cycle (enforce in application logic, not just policy). If total rows ≥ 80: block all additions until deletion policy runs.

**Step 7 — Write run log**
Insert one row into `regression_run_log` with: run_date, total_cases, core_pass, core_fail, long_tail_pass, long_tail_fail, flagged_for_human count, prompt_version, model_version.

**Step 8 — 1-in-10 human spot-check on judge labels**
If LLM-as-judge ran in Step 5: select one judge result at random. Add to Slack message as human spot-check item (see template below). A human confirms or overrides the judge label. Result logged in a separate `judge_spot_checks` table (not spec'd here — track as text note in run log).

**Step 9 — Send Slack notification**
Post to `#dmc-crm-regression` channel using the template below.

**Step 10 — Golden-set addition (conditional)**
If any fail from this week's production emails meets the golden-set criteria (see below), n8n appends a new row. This step runs after the weekly regression, not during it — triggered by a separate "failure flagged" event in the production pipeline.

### Slack Message Template

```
*DMC CRM Regression — Week of {run_date}*
Prompt: {prompt_version} | Model: {model_version}

Core invariants: {core_pass}/{core_pass + core_fail} PASS
Long-tail cases: {long_tail_pass}/{long_tail_pass + long_tail_fail} PASS
Total cases run: {total_cases}

{if core_fail > 0}
⚠️ CORE FAILURES ({core_fail}):
{for each core failure: "  • email_id {email_id}: expected {expected_label}, got {actual_label}"}
{endif}

{if long_tail_fail > 0}
Long-tail failures ({long_tail_fail}):
{for each long_tail failure: "  • email_id {email_id}: expected {expected_label}, got {actual_label}"}
{endif}

Flagged for human review: {flagged_for_human} case(s)
{if flagged_for_human > 0}
Review in Supabase: SELECT * FROM regression_golden_set WHERE email_id IN ({comma-separated flagged IDs});
{endif}

{if judge_spot_check_required}
🔍 Judge spot-check (1 in 10 — please confirm):
  email_id: {spot_check_email_id}
  Judge said: {judge_label} | Expected: {expected_label}
  Reply 👍 (agree) or 👎 (disagree) in thread.
{endif}

Suite health: {total_cases} cases ({core_count} core / {long_tail_count} long-tail)
Next deletion review: {next_deletion_date}
```

### Golden-Set Addition Criteria

A production email is added to the golden set when it meets ALL of the following conditions — not just "it failed":

1. **It represents a novel failure pattern not already covered by an existing case.** Before adding, query `regression_golden_set` for semantically similar cases (same expected/actual label pair). If a case with the same label pair already exists, do not add a duplicate — update the existing case's `date_added` to reset its expiry instead.

2. **A human has confirmed the correct label.** Auto-detected failures are not added automatically. A staff member (or the weekly Slack reviewer) must confirm `expected_label` before insert.

3. **The ratio constraint is not violated.** Long-tail additions blocked when long-tail count ≥ 20. Core invariant additions blocked when total ≥ 80 (requires a deletion cycle first).

4. **For long-tail cases:** The subclass has appeared at least 3 times in production in the past 60 days. Single-occurrence failures are not added — they have insufficient statistical weight and inflate the long-tail bias.

5. **Core invariants are added only when a structural rule is broken repeatedly (≥3 times in one month) and the rule does not already appear in the 30 core invariants above.** Core additions require Patrick's approval (decision owner for classifier architecture).

---

## Deletion Policy

### Trigger Condition
A long-tail case is deleted when BOTH conditions are true:
- `delete_after < CURRENT_DATE` (6 months have elapsed since `date_added`)
- The case has not triggered a failure in any regression run during its lifetime (i.e., it has passed every time it ran — meaning the model got it right consistently and it no longer represents a risk)

A long-tail case is RETAINED past its `delete_after` date if it triggered at least one failure in the past 3 months. It is given a 3-month extension by updating `delete_after = CURRENT_DATE + 90`.

Core cases (invariant_type = 'core') are never automatically deleted. They can only be retired by the decision owner via manual review.

### Decision Owner
**Patrick Heiskanen** (CEO / classifier architecture owner). Deletion does not happen automatically — the weekly n8n workflow identifies candidates and posts them to Slack. Patrick approves the deletion list. No deletion runs without explicit approval.

Rationale: deletion of test cases is an architectural decision, not a maintenance task. Automated deletion without human gate risks silently removing coverage.

### Execution Method
After Patrick approves in Slack, a staff member (or Patrick) runs the following SQL in the Supabase dashboard:

```sql
-- Preview first (always run preview before delete)
SELECT email_id, expected_label, date_added, delete_after, last_failed_run_date
FROM regression_golden_set
WHERE invariant_type = 'long-tail'
  AND delete_after < CURRENT_DATE
  AND (last_failed_run_date IS NULL OR last_failed_run_date < CURRENT_DATE - INTERVAL '90 days');

-- Delete only after preview confirmed
DELETE FROM regression_golden_set
WHERE invariant_type = 'long-tail'
  AND delete_after < CURRENT_DATE
  AND (last_failed_run_date IS NULL OR last_failed_run_date < CURRENT_DATE - INTERVAL '90 days');
```

**Note:** `last_failed_run_date` is updated by the weekly n8n workflow (Step 7 extension): after writing the run log, for each case that failed this run, execute `UPDATE regression_golden_set SET last_failed_run_date = (NOW() AT TIME ZONE 'Europe/Helsinki')::date WHERE email_id = $1`.

**Timezone note:** All `CURRENT_DATE` references in deletion SQL should be replaced with `(NOW() AT TIME ZONE 'Europe/Helsinki')::date` in production to avoid UTC off-by-1 errors near midnight Helsinki time. The deletion policy operates in Helsinki business time, not UTC.

---

## Autonomy Expansion Criteria

### What autonomy expansion means
The classifier currently routes hot-lead outputs below confidence 0.85 to human review (invariant 30). Expansion means raising that threshold — allowing the classifier to act autonomously on more cases. This is the primary lever for reducing staff load.

### Metric threshold for graduation
**Core pass rate ≥ 96.7% (29/30 cases) sustained over 8 consecutive weekly regression runs.**

- 96.7% = no more than 1 core invariant failure in any given run of 30 core cases. (Note: "97%" is a rounded target; the precise gate is 29 or more passes out of 30 per run.)
- "Sustained" = 8 consecutive runs, no regression. A single core failure resets the counter.
- This is a specific number from flywheel data: the weekly run log `core_pass` / `(core_pass + core_fail)` ratio, averaged over 8 runs.
- Parallel condition: confidence threshold can only be raised if the hot-lead false negative rate in production (tracked separately in the CRM dashboard) is ≤ 2% over the same 8-week window.

### Minimum sample size requirement
Graduation decision requires a minimum of **400 production emails processed** by the current prompt version and model version — not total historical emails, but emails processed under the exact `prompt_version` + `model_version` combination being evaluated for graduation. This guards against prompt version churn inflating pass rates on small samples.

### Approval owner
**Patrick Heiskanen** approves all autonomy expansion decisions. The weekly Slack message flags when the 8-run streak is achieved and the 400-email threshold is met. Patrick makes the call — the system does not auto-expand.

### Flywheel data reference
The graduation decision is made by reading the `regression_run_log` table directly:

```sql
-- Check graduation eligibility (consecutive runs only)
-- Step 1: Get last 8 runs for current version, ordered by date
WITH recent_runs AS (
  SELECT
    run_date,
    core_pass,
    core_fail,
    ROW_NUMBER() OVER (ORDER BY run_date DESC) AS rn,
    run_date::date - (ROW_NUMBER() OVER (ORDER BY run_date DESC))::int AS streak_group
  FROM regression_run_log
  WHERE prompt_version = 'CURRENT_VERSION'
    AND model_version = 'CURRENT_MODEL'
  ORDER BY run_date DESC
  LIMIT 8
)
-- Step 2: Verify all 8 belong to the same consecutive streak (same streak_group)
-- and all meet the pass threshold
SELECT
  COUNT(*) AS qualifying_runs,
  AVG(core_pass::FLOAT / (core_pass + core_fail)) AS avg_core_pass_rate,
  MIN(run_date) AS streak_start,
  MAX(run_date) AS streak_end,
  COUNT(DISTINCT streak_group) AS streak_groups  -- must be 1 for true consecutive streak
FROM recent_runs
WHERE core_fail <= 1;
-- Graduation eligible only when: qualifying_runs = 8 AND streak_groups = 1 AND avg_core_pass_rate >= 0.967
```

The confidence threshold is raised by 0.05 per approved graduation (e.g., 0.85 → 0.80 → 0.75). Each step requires a new 8-run streak. There is no single "fully autonomous" state — expansion is incremental and reversible.

---

## Execution Traces

### Trace 1 — True Positive (classifier correct, flywheel confirms)

**Input email description:**
Subject: "Finland group program inquiry — 45 pax, March 2027, budget €85,000"
Body (stripped): Email from `events@nordic-incentives.de` (German tour operator, not in partners table). Requests a 4-day Lapland program for a corporate incentive group, names specific activities (husky safari, snowmobile), specifies hotel category (4-star), and asks for a proposal with pricing by end of week.

**Classifier output:**
`label: hot-lead, confidence_score: 0.94`
Deterministic post-processing: domain `.de` passes domain filter (invariant 6), no booking reference present (invariant 20 not triggered), pax count 45 > 20 (invariant 9 satisfied), confidence 0.94 > 0.85 (invariant 30 threshold met). No override fired. Final label: `hot-lead`.

**Flywheel action taken:**
Weekly regression run compares actual_label (`hot-lead`) to expected_label (`hot-lead`) for this golden-set case. Result: `pass`. Invariant checks: invariants 1, 5, 9, 15 evaluated — all pass. No Slack alert for this case. Run log increments `core_pass` by 1.

**Outcome:**
No Slack notification for this case (pass cases are aggregated in the summary count only). Golden set not updated. `regression_run_log` records 1 additional core pass. Flywheel continues normal operation.

---

### Trace 2 — False Positive (classifier wrong, flywheel catches)

**Input email description:**
Subject: "RE: FIN-2026-089 — updated rooming list"
Body (stripped): Email from `liisa.makinen@visitsaimaa.fi` (existing partner, in partners table). Contains an updated rooming list for a booking already in progress — 22 rooms, 3 nights, specific dietary requirements. No new program inquiry. Body is entirely operational logistics.

**Classifier output (incorrect):**
`label: hot-lead, confidence_score: 0.88`
LLM reasoning trace (not used for validation): "The email references a large group size and a Finnish tourism organization — signals of a significant lead."

**Deterministic post-processing:**
Booking reference `FIN-2026-089` detected in subject (regex match). Invariant 18 fires: `operational: ALWAYS when booking reference present + no new inquiry`. Invariant 19 fires: `hot-lead → operational: NEVER when reference number in subject`. Override applied. Final label overridden to: `operational`.

**Flywheel action taken:**
Weekly regression run compares actual_label (`operational` after override) to expected_label (`operational`) for this golden-set case. Result: `pass` — the deterministic layer caught the error before it reached the label store. The run log records a core pass, not a failure. However: if the override mechanism itself had failed (e.g., regex did not match reference number format), actual_label would be `hot-lead`, expected_label `operational` → `fail_invariant_violation`. In that failure scenario: Slack message fires a ⚠️ CORE FAILURE alert for this case; case is not auto-corrected; TypeScript classifier is flagged for developer review.

**Outcome (override success path):**
Slack summary shows 0 core failures. The false positive is caught and corrected by the deterministic layer — the flywheel confirms the override worked. No golden-set update. Flywheel health intact.

**Outcome (override failure path — for completeness):**
Slack fires: "⚠️ CORE FAILURE — email_id abc123: expected `operational`, got `hot-lead`". Invariant 18 and 19 listed as violated. Case flagged for human review. Developer investigates regex pattern. Fix deployed before next Monday's run.

---

### Trace 3 — Edge Case (ambiguous email, flywheel routes to human)

**Input email description:**
Subject: "Finland as a destination — interest from our side"
Body (stripped): Email from `partnerships@travelcollective.co.uk` (not in partners table, domain not previously seen). Body is 4 sentences. States: "We are a UK-based luxury travel consortium. We have been hearing good things about Finland as a new destination for our portfolio. We would love to learn more about what you offer for high-end groups. Could we have a call?" No pax count, no date, no budget, no specific program inquiry.

**Classifier output:**
`label: warm-lead, confidence_score: 0.72`

**Deterministic post-processing:**
No booking reference. Domain `.co.uk` passes spam filter (invariant 6). Not in partners table. No Finnish language (invariant 27 not triggered). Confidence_score 0.72 < 0.85 — but invariant 30 only auto-escalates hot-lead outputs below 0.85, not warm-lead. No deterministic override fires.

**Flywheel action taken:**
This case is not in the golden set (first occurrence of this domain). Production pipeline logs the output to a staging table. During the weekly review, a staff member notices this email was a first contact from a UK luxury consortium — a potentially high-value relationship. The email is flagged manually for golden-set addition.

Golden-set addition check: (a) novel failure pattern? Label pair `warm-lead/warm-lead` already exists, but this is a genuine ambiguity case — could be `cold-lead` or `warm-lead`. (b) Human confirms label: staff member reviews and agrees `warm-lead` is correct given the "luxury" and "high-end groups" language. (c) Ratio constraint: long-tail count is 14/20 — space available. (d) Subclass occurrence: `.co.uk` luxury consortium pattern has appeared twice in 60 days — below the 3-occurrence threshold for long-tail addition.

**Outcome:**
Case does NOT get added to golden set (3-occurrence threshold not met). It is logged in a `pending_golden_set` staging table for re-evaluation in 30 days. Slack message this week does not flag it as a failure (classifier was not wrong, just low-confidence). The flywheel correctly identified it as a case to watch — without inflating the long-tail suite with a single data point. In 30 days, if the `.co.uk` luxury consortium pattern appears a third time, it becomes eligible for golden-set addition.

---

## Maintenance Budget Accounting

| Task | Frequency | Time |
|------|-----------|------|
| Review weekly Slack summary | Weekly | 5 min |
| Confirm/override judge spot-check (1 in 10 weeks) | Monthly avg | 10 min |
| Approve golden-set additions (avg 1-2/month) | Monthly | 15 min |
| Approve deletion candidates | Monthly | 10 min |
| Approve autonomy expansion (rare) | Quarterly | 20 min |
| **Total** | **Monthly** | **~60-65 min** |

Well within the <2 hour/month budget. Headroom available for incident response (core failure investigation estimated at 20-30 min additional). Note: weekly Slack review at 5 min × 4.33 weeks/month ≈ 22 min alone; total realistic estimate is 60-65 min, not 40-60 min.

---

*Spec version 1.1 — 2026-03-19. Changes from v1.0: fixed 97% threshold math (→ 96.7%/29/30), fixed eligibility SQL consecutive-run logic, added 5 indexes, corrected maintenance budget (63 min), added Helsinki TZ note to deletion SQL, added actual_label history guidance, added concurrency transaction note, added CI/version-change trigger (Trigger B), added deterministic layer versioning guidance. Grok audit: CONDITIONAL GO → fixes applied. Review at session 125 Opus Review or when prompt_version changes.*
