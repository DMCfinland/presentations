---
name: dmccrm-validator-spec
description: Deterministic validation layer spec v2 for DMC CRM email classification pipeline. Fixes Rule 10 ordering bug, Rule 8 data corruption, stopping vs correction rule ambiguity, and contains-semantics.
type: project
source: session-bridge-challenge-1, Grok Heavy cross-validation (session 97/98 boundary)
version: 2.0
---

# DMC CRM Email Classifier — Deterministic Validation Layer Spec v2.0

**Version:** 2.0 (v1 cross-validated by Grok 4-agent council — 3 critical bugs fixed)
**Date:** 2026-03-19
**Scope:** TypeScript/Edge validator between LLM intent JSON and Supabase write
**Architecture:** n8n (Graph API ingestion) → LLM classification → **[THIS SPEC]** → Supabase

---

## Background

Chain-of-thought faithfulness is structurally unreliable (40-60% causal failure rate, METR 2025).
An LLM can correctly identify "hot lead with urgency" in reasoning and then call `archive`.
This validator sits outside the LLM and enforces that the LLM's stated intent is internally
consistent before any Supabase write. It does NOT re-run the LLM.

**Known limitation:** Deterministic keyword rules on LLM-extracted signals stack two imperfect
layers. The monthly drift review process is mandatory to prevent silent degradation after ~3 months.

---

## Acceptance Criterion 1 — LLM Intent JSON Schema

The LLM outputs ONLY this JSON. No prose, no markdown fences.

```json
{
  "$schema": "dmccrm-intent/v1",
  "email_id": "string (Outlook message-id, required)",
  "classification": "hot_lead | warm_lead | cold_lead | existing_client | supplier | internal | archive",
  "confidence": "number (0.0–1.0)",
  "reasoning_steps": [
    {
      "step": "number (1-indexed)",
      "observation": "string",
      "inference": "string"
    }
  ],
  "extracted_signals": {
    "urgency_markers": ["string (exact quoted phrase) or 'n/a'"],
    "authority_signals": ["string (role/title indicator) or 'n/a'"],
    "budget_signals": ["string (price/group size mention) or 'n/a'"],
    "relationship_signals": ["string (prior booking reference) or 'n/a'"],
    "negative_signals": ["string (unsubscribe/complaint/out-of-scope) or 'n/a'"]
  },
  "proposed_action": "create_deal | update_deal | archive | human_review",
  "proposed_deal_stage": "inquiry | qualified | proposal_sent | negotiation | closed_won | closed_lost | null",
  "proposed_priority": "high | medium | low",
  "requires_human": "boolean",
  "human_reason": "string (populated only if requires_human=true, else empty string)"
}
```

**Schema invariants enforced by LLM system prompt:**
- `requires_human: true` → `proposed_action` MUST be `"human_review"`
- `confidence < 0.6` → `requires_human` MUST be `true`
- `proposed_deal_stage` is `"null"` when action is `"archive"` or `"human_review"`
- Every signal array has at least one entry (`"n/a"` is valid; empty array `[]` is not)

**LLM system prompt instruction:**
```
Output ONLY valid JSON matching dmccrm-intent/v1 schema. No text before or after. No markdown code fences.
All signal arrays must have at least one entry. If uncertain on any field, set requires_human: true
and explain in human_reason.
```

---

## Acceptance Criterion 2 — Rule Execution Model

### Two Rule Categories (critical — read before implementing)

Rules are **NOT all first-match-wins**. They fall into two categories with different execution behavior:

| Category | Rules | Behavior |
|----------|-------|----------|
| **STOPPING** | 1, 2, 3, 4, 7 | Fire → immediately route to human_review → exit rule chain → no further rules run |
| **CORRECTION** | 5, 6, 8, 9 | Fire → apply correction to the intent object → continue to next rule |

A single email can trigger multiple CORRECTION rules in sequence.
A STOPPING rule always exits immediately — no subsequent rules run.
If a CORRECTION rule fires after a STOPPING rule has already routed to human_review: the STOPPING rule wins.

**Rule evaluation order:** 1, 2A, 2B, 3, 4, 5, 6, 7, 8, 9 (see Rule 2 split below)

### String Matching Semantics (applies to all keyword rules)

Unless stated otherwise:
- Match is **case-insensitive substring** (not exact, not regex)
- Applied to the signal array values as extracted by the LLM
- `"n/a"` is treated as no signal present (never matches any keyword)
- Negation caveat: explicitly exclude matches preceded by "not", "no longer", "no", "deadline passed",
  "not urgent", "was urgent" — check 3 words preceding any keyword hit

---

## Acceptance Criterion 2 — Rules

### Rule 1 — Schema Integrity Gate [STOPPING]
```
IF JSON is missing any required field
OR any enum value is outside the defined set
OR any signal array is empty
THEN → human_queue, mismatch_type: "schema_violation", exit
```
Catch-all before any logic runs. Prevents downstream null-reference crashes.

---

### Rule 2A — Overconfident Without Reasoning [STOPPING]
```
IF reasoning_steps.length < 2
AND confidence > 0.80
THEN → override confidence to 0.55
       continue to Rule 2B immediately (do not wait for sequential position)
```

### Rule 2B — Low Confidence Override [STOPPING]
```
IF confidence < 0.60
THEN → override proposed_action to "human_review"
       set requires_human = true
       mismatch_type: "low_confidence"
       exit
```

**Note:** Rule 2A is a pre-check that feeds 2B. They run as a unit at position 2.
Rule 10 in v1 was placed last (bug) — moved here and split so the chain executes correctly.

---

### Rule 3 — Urgency-Archive Contradiction [STOPPING]
```
IF urgency_markers contains (case-insensitive substring, negation-checked) any of:
  ["urgent", "asap", "immediately", "deadline", "by end of", "we need this confirmed",
   "waiting for your response", "time-sensitive", "group is ready to book",
   "deposit deadline", "can you confirm today", "last chance"]
AND proposed_action = "archive"
THEN → human_queue, mismatch_type: "urgency_archive_conflict", exit
```

**Negation exclusion:** skip match if "not", "no", "no longer", "passed", "was" precedes the keyword.

---

### Rule 4 — Authority-Archive Contradiction [STOPPING]
```
IF authority_signals contains (case-insensitive substring, negation-checked) any of:
  ["CEO", "CFO", "COO", "director", "VP", "vice president", "head of", "procurement",
   "travel manager", "event manager", "DMC coordinator", "requesting on behalf of",
   "on behalf of our company", "our procurement team"]
AND proposed_action = "archive"
THEN → human_queue, mismatch_type: "authority_archive_conflict", exit
```

**Note:** Authority signals in email signatures do not count — instruct LLM in system prompt:
"authority_signals must reflect the authority of the REQUEST, not the sender's email signature."

---

### Rule 5 — Hot Lead Cannot Be Low Priority [CORRECTION]
```
IF classification = "hot_lead"
AND proposed_priority = "low"
THEN → override proposed_priority to "high"
       log mismatch_type: "classification_priority_mismatch" (append to correction_log, do not stop)
       continue to Rule 6
```

---

### Rule 6 — Budget Signal Without Deal Stage [CORRECTION]
```
IF budget_signals contains non-"n/a" value
AND proposed_action = "create_deal"
AND (proposed_deal_stage = "null" OR proposed_deal_stage is missing)
THEN → override proposed_deal_stage to "inquiry"
       log mismatch_type: "missing_deal_stage" (append, do not stop)
       continue to Rule 7
```

---

### Rule 7 — requires_human Flag Without human_review Action [STOPPING]
```
IF requires_human = true
AND proposed_action ≠ "human_review"
THEN → override proposed_action to "human_review"
       mismatch_type: "human_flag_action_mismatch"
       exit
```

---

### Rule 8 — Existing Client Mis-staged as New Lead [CORRECTION + SAFETY CHECK]
```
IF relationship_signals contains (case-insensitive substring) any of:
  ["booking reference", "previous group", "booked with you", "invoice number",
   "your team handled our", "repeat client", "annual trip", "last year you arranged",
   "we used your services"]
AND classification is "hot_lead" OR "warm_lead" OR "cold_lead"
THEN → override classification to "existing_client"
       log mismatch_type: "client_classification_mismatch" (append, do not stop)

SAFETY CHECK (added v2 — prevents data corruption):
  IF after override: classification = "existing_client" AND proposed_action = "create_deal"
  THEN → override proposed_action to "human_review"
         append mismatch_type: "existing_client_create_deal_conflict"
         exit (STOPPING behavior for this compound case)

  ELSE → continue to Rule 9
```

**Rationale for safety check:** "your team handled" is also a cold-outreach phrase.
Reclassifying as existing_client and proceeding with create_deal silently corrupts the pipeline.
When uncertain, route to human. Cost: a few minutes of staff time. Value: no orphaned Supabase records.

---

### Rule 9 — Supplier in Lead Pipeline [CORRECTION]
```
IF negative_signals contains (case-insensitive substring) any of:
  ["we offer our services", "our company provides", "partnership opportunity with us",
   "we are a supplier", "subcontractor", "looking to work with you"]
AND proposed_action = "create_deal"
THEN → override classification to "supplier"
       override proposed_action to "archive"
       log mismatch_type: "supplier_misclassified" (append, do not stop)
       continue (no further rules apply after archive)
```

**Note:** Legitimate partner-discussion emails (existing supplier, renewal discussion) will have
relationship_signals that fire Rule 8 first. Rule 9 applies only to cold inbound supplier pitches.

---

### Multi-Rule Fire Logging

When multiple rules fire on one email:
- First STOPPING rule's mismatch_type → primary field in email_triage_queue.mismatch_type
- All correction logs → stored in email_triage_queue.correction_log (jsonb array)
- Format: `[{"rule": 5, "mismatch_type": "classification_priority_mismatch"}, ...]`

---

## Acceptance Criterion 3 — Human Queue: email_triage_queue

```sql
CREATE TABLE email_triage_queue (
  id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at         timestamptz NOT NULL DEFAULT now(),
  email_id           text NOT NULL,
  subject            text,
  sender_email       text,
  received_at        timestamptz,

  -- LLM original intent (before any overrides)
  llm_classification   text,
  llm_action           text,
  llm_priority         text,
  llm_confidence       numeric(4,3),
  llm_reasoning_steps  jsonb,

  -- Validator output
  mismatch_type        text NOT NULL,
  correction_log       jsonb DEFAULT '[]'::jsonb,
  validator_version    text NOT NULL DEFAULT '2.0',
  override_applied     boolean NOT NULL DEFAULT false,

  -- Signals (for human context — copied from LLM output)
  urgency_markers      text[],
  authority_signals    text[],
  budget_signals       text[],
  relationship_signals text[],
  negative_signals     text[],

  -- Human resolution
  resolved_by          text,
  resolved_at          timestamptz,
  human_classification text,
  human_action         text,
  resolution_notes     text,

  status               text NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'resolved', 'escalated'))
);

CREATE INDEX idx_triage_status    ON email_triage_queue (status, created_at DESC);
CREATE INDEX idx_triage_email_id  ON email_triage_queue (email_id);
```

**SLA and notifications:**
- All mismatch_type fires → write to email_triage_queue, status = pending
- Emails with urgency_markers (non-null, non-"n/a") → trigger immediate Teams notification via n8n Global Error Handler
- pg_cron daily: pending items > 24h → Teams digest
- pg_cron: pending items > 48h → status = escalated, notify manager

---

## Acceptance Criterion 4 — Drift Mitigation: Monthly 20-Email Sample Review

**Who:** Liisa or Sebastian
**When:** First Monday of each month, ~30 minutes
**Cadence:** Month 1-3 mandatory. After 3 months, escalate to bi-weekly if queue volume > 20/month.

### Step 1 — Pull sample

```sql
-- 10 auto-processed (no human review triggered)
SELECT email_id, llm_classification, llm_action, llm_confidence,
       urgency_markers, authority_signals
FROM email_classifications
WHERE processed_at > now() - interval '30 days'
  AND human_reviewed = false
ORDER BY RANDOM() LIMIT 10;

-- 10 human-overridden (LLM wrong, human corrected)
SELECT eq.email_id, eq.llm_classification, eq.human_classification,
       eq.mismatch_type, eq.correction_log, eq.resolution_notes
FROM email_triage_queue eq
WHERE eq.resolved_at > now() - interval '30 days'
  AND eq.human_classification IS DISTINCT FROM eq.llm_classification
ORDER BY eq.resolved_at DESC LIMIT 10;
```

### Step 2 — Pattern scan (30 min hard cap)

Look for:
- New urgency phrases (not in Rule 3 list) appearing in auto-processed emails that should have been flagged
- New authority titles (not in Rule 4 list)
- Classification errors in the auto-processed sample
- Signals the LLM extracted that are systematically wrong (affects Rule 8/9 confidence)

### Step 3 — Add rule exceptions

If a new phrase appears 3+ times in the sample → add to the relevant rule's keyword list.
Update validator_version (2.0 → 2.1).

**Cap:** Maximum 5 new phrases per rule per month. If > 5 needed → rule needs semantic redesign, escalate to Patrick.

**Retirement:** Remove phrases producing false positives 2+ consecutive months. Never grow lists without pruning.

### Step 4 — Log findings

File: `_shared/best-practices/dmccrm-validator-drift-log.md`
Format: `YYYY-MM-DD | Rule N | phrase added | count observed | reviewer initials | false positive rate this month`

### 6-Month Drift Warning

At 6 months, static keyword lists will degrade silently regardless of monthly reviews (documented
in B2B SaaS production cases). Schedule a full rule audit at month 6: review all keyword lists,
compare queue volume trend, consider whether semantic matching (embedding similarity) should
replace substring matching for Rules 3 and 4.

---

## Acceptance Criterion 5 — Path B: Parallel Reasoner + Actioner + Judge

### Trigger Conditions (use Path B when ANY of these are true)

1. Mean email confidence over last 7 days < 0.70 (signals systematic LLM drift — add to monitoring dashboard)
2. 3+ `mismatch_type: schema_violation` events in past 7 days (LLM output format breaking down)
3. Email language is not standard English or Finnish (Arabic, German, French group buyer)
4. Email contains explicit domain idioms not in any rule keyword list (reviewer flags this during monthly review)

**Note (v2 change):** Trigger 1 (confidence floor) is the most reliable automatic signal.
Implement as a pg_cron query: if mean confidence < 0.70 over last 7 days → flip Path B feature flag in Supabase config table.

### Do NOT use Path B when

- Rules 3 or 7 fire — these are definitive contradictions, no second opinion needed
- Volume > 50 emails/day — Path B doubles LLM cost per email ($0.40/mo risk)
- Existing client or supplier classification (Rule 8/9 domain) — deterministic override is safer than LLM debate

### Path B Implementation

```
Email → [parallel]
  LLM Call A (Reasoner, Sonnet):
    System: "Analyze this email. Output ONLY reasoning_steps JSON array.
             No classification. No action. Reasoning only."
    Output: { reasoning_steps: [...] }

  LLM Call B (Actioner, Sonnet):
    System: "Classify this email. Output ONLY classification, proposed_action,
             proposed_priority, proposed_deal_stage, confidence. No reasoning."
    Output: { classification, proposed_action, proposed_priority, proposed_deal_stage, confidence }

→ Merge outputs into full dmccrm-intent/v1 JSON
→ Run deterministic validator (all 9 rules) on merged JSON as normal

IF Reasoner.urgency_markers (extracted from reasoning text) is high
AND Actioner.proposed_action = "archive":
  → LLM Call C (Judge, Haiku):
    "Given these reasoning steps [paste A output] and this proposed action [paste B output],
     is archiving correct for a B2B travel DMC company? Output only: {agree: boolean, reason: string}"
  IF judge.agree = false → override to human_review

IF Actioner.confidence delta vs Step 1 mean > 0.30 → human_review regardless of judge
```

**Cost estimate:** 2 Sonnet + occasional Haiku ≈ $0.20-0.40/mo at 500 emails.

---

## Implementation Checklist (for Developer — complete without clarifying questions)

- [ ] Deploy `email_triage_queue` table (SQL in Criterion 3)
- [ ] Create `email_classifications` table (standard columns + human_reviewed boolean + processed_at)
- [ ] Build validator as Supabase Edge Function `/functions/v1/classify-email`
- [ ] Implement rule executor: STOPPING rules exit immediately; CORRECTION rules mutate intent object and continue
- [ ] Wire string matching as case-insensitive substring with 3-word negation pre-check
- [ ] Wire n8n → LLM call → POST to validator endpoint → Supabase write
- [ ] Test Rules 2A/2B chain, Rule 7, Rule 8 safety check with synthetic emails before live traffic
- [ ] Implement correction_log as jsonb append (not overwrite) on multi-rule fires
- [ ] Configure pg_cron for 24h digest and 48h escalation jobs
- [ ] Add Teams webhook for urgent mismatch notification (reuse n8n Global Error Handler)
- [ ] Add Supabase config table row: `{ key: 'path_b_enabled', value: 'false' }` for feature flag
- [ ] Add pg_cron for 7-day mean confidence check → flip path_b_enabled if < 0.70
- [ ] Create `dmccrm-validator-drift-log.md` and assign monthly review to Liisa
- [ ] Set validator_version = "2.0" in Edge Function env

---

## Non-Goals

- Validator does NOT re-run the LLM
- Validator does NOT read raw email body — operates only on LLM intent JSON
- Validator does NOT handle calendar invites or internal emails (filtered upstream by n8n)
- Validator does NOT replace the LLM — it enforces the LLM's own stated intent
- Validator does NOT handle Microsoft Graph reply-thread context (known gap — future v3 scope)

---

*v2.0 changes from v1: Rule 10 moved and split into Rule 2A/2B (ordering bug fix). Rule 8 safety check
added (data corruption fix). Stopping vs Correction categories defined explicitly (developer ambiguity fix).
String matching semantics specified. Negation caveat added. Path B trigger 1 (confidence floor) added.
6-month drift warning added. Grok 4-agent cross-validation: [Harper][Benjamin][Lucas].*
