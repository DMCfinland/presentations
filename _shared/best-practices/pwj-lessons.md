# PWJ Loop — LESSONS File
**Purpose:** Persistent log of Judge failure traces. Feeds back into spawn prompts via tag-based grep-filtering.
**Architecture:** Single file, tag-based (replaces tier-split design — session 83, Gemini thinking validation).
**Review:** Monthly by Patrick. Archive entries where `Fix applied: Accepted as-is` produced bad regenerations. Do not auto-inject without spot-check.

**Usage in spawn prompts:** Planner grep-filters this file for matching task tags (e.g. `grep "#crm #strategy-brief" pwj-lessons.md`). Include 3 most recent FAIL entries with matching tags as few-shot anti-examples in Judge rubric. Filters prevent context poisoning from unrelated failure patterns.

---

## Entry Format

```
## [date] Task: [one-sentence task description]
Tags: #[domain] #[task-type] #[output-type]
Criticality: [routine/standard/high-stakes/critical] | Iterations: [N] | Outcome: [PASS/FAIL/ESCALATED]
FAIL criterion: [exact criterion text that failed]
Evidence: [Judge's exact quote of what went wrong]
Root cause: [Ambiguity / Novelty / Conflict / Worker Error / Criteria drift / Silent Drift]
Fix applied: [Criteria rewrite / Human input / Logic Refresh / Accepted as-is]
---
```

**Tag taxonomy (use 2-4 tags per entry):**
- Domain: `#crm` `#dmc` `#seo` `#financial` `#legal` `#hr` `#strategy`
- Task type: `#strategy-brief` `#research-synthesis` `#sql-migration` `#consistency-check` `#market-analysis` `#email-draft`
- Output type: `#document` `#code` `#analysis` `#plan` `#proposal`

---

## Log

## 2026-03-20 Task: Build S3 Anti-Anchoring System Spec for M365 mining workflow
Tags: #dmc #anchoring #regex-order #document #m365-mining
Criticality: standard | Iterations: 1 (+ Judge edits) | Outcome: PASS
FAIL criterion: [C6] "Integration spec total must be ≤5 minutes using maximum estimates per step" — Worker's honest maximum gave 5:30 due to locale fix step.
Evidence: Step 2 (encoding check) had max=2min for first-run locale fix, pushing total to 5:30. Worker flagged it correctly as CRITERIA GAMING RISK rather than hiding it.
Root cause: Criteria ambiguity — criterion did not distinguish one-time setup costs from per-session recurring costs. Both counted in "total" produced a false violation.
Fix applied: Criteria rewrite — separate PREREQUISITE block (one-time, not counted) from per-session steps. After fix, Step 2=30s, total=4:00.
Lesson: Integration time criteria must specify "per-session recurring cost, excluding one-time setup." Add "PREREQUISITE (one-time setup)" block to any integration spec with a time constraint. See `time-boxing-practices.md` for the general rule.
---

## 2026-03-20 Task: S3 regex pattern execution order — CAPS before urgency
Tags: #dmc #anchoring #regex-order #m365-mining #document
Criticality: standard | Iterations: 0 (pattern finding, not failure) | Outcome: PATTERN CAPTURED
FAIL criterion: N/A — this was caught by Judge adversarial edge case testing before production.
Evidence: Pattern 23 (CAPS normalization) and Pattern 10 (Finnish urgency "heti") are in different categories. If urgency patterns run before CAPS normalization, "HETI" is not matched by Pattern 10 (which targets lowercase "heti"). Silent bypass — "HETI" survives as "heti" in stripped output.
Root cause: Spec documented categories but not execution order. Silent failure in production.
Fix applied: Added explicit 7-step execution order to Pattern List header. Step 3 reads: "CAPS normalization BEFORE urgency patterns — without this, 'HETI' is not caught by Pattern 10."
Lesson: Any spec with multiple regex passes on the same text must specify execution order explicitly. CAPS normalization must always precede urgency/authority strip passes. Add execution order table to all regex-heavy specs.
---

## 2026-03-20 Task: Build S4 Progressive Autonomy routing spec for DMC CRM email classifier
Tags: #crm #dmc #specification #code #document
Criticality: standard | Iterations: 2 | Outcome: PASS (round 2)
FAIL criterion C1: [Round 1] "Routing table: 5 rows × 8 columns with numeric thresholds per class" — Worker built a 5×4 state table with global thresholds (0.82/0.60). Per-class thresholds existed in a separate section, not in the decision table.
Evidence: Table had columns: de_anchored | exception_triggered | state description | routing action — no class columns.
Root cause: Criteria ambiguity — "5×8 columns" could be read as state table OR as a state×class matrix. Worker chose state-flow table; Judge required state×class matrix.
Fix applied: Criteria rewrite → explicitly said "5 rows × 9 columns: Column 1 = state, Columns 2–9 = one per class, each cell = per-class threshold + action."
FAIL criterion C4: [Round 1] Coverage gap — complaint and cancellation not present as routed_class in any test. Worker flagged as CRITERIA GAMING RISK but still self-reported ✓ on background scores.
Evidence: Coverage table line 800: "complaint: T2 background / cancellation: implied via T2 CALIBRATION TARGET note ✓" — background score ≠ coverage.
Root cause: Worker honestly flagged the gap but criteria did not say "must appear as routed_class output" — only "all 8 classes covered." Worker exploited ambiguity.
Fix applied: Patrick allowed 11 tests (JF3). T9 (complaint), T10 (cancellation), T11 (Row 4 regulatory) added.
FAIL criterion C6: [Round 1] FI and DE trace pairs both produced S5-human-queue regardless of de_anchored flag — same routing action in both states.
Evidence: Traces 1/2 (FI): both S5-human-queue, booking_request. Traces 5/6 (DE): same. Criterion says "each de_anchored=true trace must produce DIFFERENT class OR queue."
Root cause: Worker chose authority-marker-stripped emails for all traces. After stripping, confidence dropped below auto-approve threshold → same queue as raw. Should have chosen emails where stripped confidence exceeds threshold.
Fix applied: Replaced FI/DE traces with clean-email cases (no authority markers) where stripped confidence = raw confidence ≥ 0.82 → auto-approve. de_anchored=false (R1) → human-queue; de_anchored=true (R2) → auto-approve. Genuine divergence.
Lesson: For routing trace specs, choose examples that DEMONSTRATE the routing difference, not just show the mechanism. If all traces produce the same action, the spec does not prove the routing works differently across states.
---

## 2026-03-19 Task: Design regression flywheel spec for DMC CRM email classifier
Tags: #crm #dmc #plan #document
Criticality: standard | Iterations: 2 | Outcome: PASS (round 2)
FAIL criterion: [Round 1 — C2] "Each invariant must follow format: [source label] → [target label]: NEVER/ALWAYS + reason" — 3 of 30 invariants (17, 28, 30) missing the → [target label] component.
Evidence: Invariant 17 written as `spam: ALWAYS when...`, invariant 28 as `any-label: NEVER flip class...`, invariant 30 as `hot-lead: ALWAYS escalate...`. None contained → [target]. Criterion is binary — content was DMC-specific and valid, but format failed.
Root cause: Criteria ambiguity — the format spec covers transition rules (source → different target) but the Worker correctly identified 3 invariants that are behavioral/escalation rules without a distinct target class. Worker flagged "CRITERIA GAMING RISK" honestly. Criterion did not specify how to handle non-transition invariant types.
Fix applied: Criteria rewrite → Worker reformatted all 3 using extended target notation (e.g., `any-non-spam → spam`, `any-label → any-label (override)`, `hot-lead → human-review`). Additional schema gap also fixed (last_failed_run_date column added, undefined view removed).
Lesson: When specifying format for classification invariants, include an example for non-transition rules (self-classification, escalation). "Each must follow format X" fails when X doesn't cover all valid invariant types in the domain. Fix: add "(for escalation/behavioral rules, use [source] → [outcome-label] where outcome-label may be 'human-review' or 'self')" to the criterion.
---

## 2026-03-18 Task: Research compact vs new session strategy for Claude Code
Tags: #system #research-synthesis #document
Criticality: standard | Iterations: 2 (Logic Refresh triggered) | Outcome: PASS (round 2)
FAIL criterion: [Round 1] All 7 criteria self-reported PASS on round 1 — no genuine adversarial pressure
Evidence: Worker and Judge were the same Sonnet instance. Worker self-reported "all 7 criteria pass." Zero verbatim evidence quoted. No Mistral call made. Criterion 6 (thresholds grounded in session log data) accepted on Worker's assertion alone — logs never independently read.
Root cause: Protocol Drift — Planner skipped Step 3.5 (Grok criteria stress-test) AND Step 5 (independent Judge). Lead acted as Planner + Worker + Judge in same context = theatrical compliance guaranteed.
Fix applied: Logic Refresh → Grok stress-test on criteria → 5 real gaps found → 9 Grok-hardened criteria → Mistral Large 3 Judge → 9.9/10 skepticism score, GO verdict with verbatim quotes.
Lesson (TIER A CANDIDATE): **Same-model PWJ = theater.** PWJ is only real when at least ONE external model touches it: Grok on criteria (Step 3.5) OR Mistral on output (Step 5), or both. A Lead that plays all 3 roles produces compliance, not quality. Source: Patrick, session 89.
---

## 2026-03-17 Task: Write Autoresearch Protocol for skill self-improvement
Tags: #system #strategy #document #protocol
Criticality: standard | Iterations: 2 | Outcome: PASS
FAIL criterion: Template copy-paste ready, ≤6 fields SHOWN in document
Evidence: Worker wrote "Field count: 6. All required." — fields counted but not rendered as a copy-paste block. Grok: "operator must mentally reconstruct or hunt prior sessions for format."
Root cause: Criteria ambiguity — "copy-paste ready" not defined as "fields must be shown, not just counted"
Fix applied: Criteria rewrite — added "all fields SHOWN in the document" to criterion 3 in Round 2 spawn
Lesson: "Copy-paste ready" is ambiguous. Write: "Template must display all fields as a visible block with a filled example, not just count them."
Architecture discovery: All 3 Grok FAILs were criteria gaps, not execution failures. Worker executed correctly against underspecified criteria. Fix: Run Grok stress-test on criteria BEFORE spawning (Step 3.5) — not after output is written. Source: Patrick session 85.
---
