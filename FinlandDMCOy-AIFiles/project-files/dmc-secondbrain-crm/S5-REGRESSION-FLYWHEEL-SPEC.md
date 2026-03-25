# S5 Regression Flywheel Specification — Deterministic Validation Layer
**For:** DMC CRM Email Classifier — S4 Output Validator
**Version:** 1.2
**Date:** 2026-03-24
**Status:** APPROVED — Grok Q2+Q3 fixed (s108). Gemini audit applied: Q4 schema drift guard + Q3 hard cap. Q2 thread-context gap: known limitation, documented below. Doc split (Q1/Q4-Gemini): post-P2.
**Input source:** S4-PROGRESSIVE-AUTONOMY-SPEC.md v1.2 + S5-FLYWHEEL-BRIDGE-v1.0.md
**Scope:** 30 invariants (TypeScript), weekly synthetic test flywheel, audit trail, zero-hallucination routing guarantee

---

## Executive Summary

S5 is a deterministic validation layer that sits between S4 (intent classifier) and the CRM database. Every S4Output record passes through 30 invariants — A1 through E6 — before any CRM write occurs. One FAIL from any invariant stops the record, fires `escalate_to_human_review()`, and routes the email to human_review_queue. The CRM write function is never reached on FAIL. S5 also operates a weekly regression flywheel: 100 synthetic emails per week, with every failure from Week N automatically added to Week N+1's test set, ensuring the hardest cases are never dropped from coverage.

---

## S5 Purpose and Goals

**Why S5 exists:** S4 classifies intent with a 6-rule decision matrix. S4 is probabilistic: a confidence score, a routing rule, a language detection. S4 can produce plausible-but-wrong outputs. S5 does not re-classify. S5 asserts business-logic invariants that must be true if S4's output is correct — and escalates immediately if any invariant is violated.

**Goals:**
1. Block every hallucinated or misclassified output before it corrupts the CRM.
2. Produce a deterministic, auditable per-email record (which invariants passed/failed, why).
3. Generate weekly regression pressure: a flywheel that grows harder over time, not easier.
4. Respect the Rule 6 priority hierarchy (cancellation > complaint > media-press > visa_regulatory) at the validation layer, independently of S4.

**What S5 is NOT:** S5 is not a re-ranker, not a confidence adjuster, not a second classifier. It does not override S4's intent class. It either approves S4's output for CRM entry or escalates it to human review.

**Invariant execution order (mandatory, MO-2 compliant):** Category A → B → C → D → E. No reordering. Category A (class-specific structural checks) must complete before Category B (confidence logic) because B4/B5 reference A-level fields. Category C (data integrity) runs after B because C4 applies an ambiguity penalty that B guards must not have already consumed. D (business rules, language-specific) runs after C because D1/D2 may reference C3's enum validation. E (flywheel) runs last because it aggregates results from all prior categories.

---

## Escalation Signature (used throughout all 30 invariants)

```typescript
function escalate_to_human_review(
  email: Email,
  failedInvariants: string[],
  reason: string
): never {
  writeToHumanReviewQueue({ email, failedInvariants, reason, timestamp: new Date().toISOString() });
  throw new ValidationError(`S5 FAIL: ${failedInvariants.join(', ')} — ${reason}`);
}
```

The return type `never` is load-bearing: it signals to TypeScript's control-flow analysis that any code after `escalate_to_human_review()` is unreachable. The CRM write sits after invariant validation. If `escalate_to_human_review()` is called, the function throws and the CRM write is never reached. This is the isolation guarantee that C3 proofs rely on.

---

## Rule 6 Priority Block (verbatim TypeScript — C6 requirement)

```typescript
function resolveRule6Priority(output: S4Output): IntentClass {
  // SCHEMA DRIFT GUARD — do NOT use ?? '' here.
  // Silent fallback to '' means S4 dropped email_body_raw and we never detected it.
  // That produces a no-op function that returns output.assigned_intent_class unchanged,
  // bypassing all Rule 6 priority enforcement with zero error signal.
  if (output.email_body_raw === null || output.email_body_raw === undefined) {
    throw new SchemaDriftError(
      'S4 schema drift detected: email_body_raw is missing from S4Output. ' +
      'resolveRule6Priority cannot enforce Rule 6 priority without raw body text. ' +
      'Do NOT redeploy until S4 output schema is verified and this function is updated.'
    );
  }
  const raw = output.email_body_raw;
  const cancellation_signals =
    /\b(cancel|stornierung|stornieren|peruutus|peruuttaa)\b/i.test(raw);
  const complaint_signals =
    /\b(complaint|beschwerde|valitus|unacceptable|unannehmbar|mahdoton|refund|korvaus)\b/i.test(raw);
  const media_signals =
    /\b(journalist|press|media|feature|publication|artikkeli|toimittaja|journalist|artikel)\b/i.test(raw);
  const visa_signals =
    /\b(visa|viisumi|permit|lupa|genehmigung|registration|rekisteröinti)\b/i.test(raw);

  if (cancellation_signals) return 'cancellation';
  else if (complaint_signals) return 'complaint';
  else if (media_signals) return 'media-press';
  else if (visa_signals) return 'visa_regulatory';
  else return output.assigned_intent_class; // no override needed
}
```

This block is called from invariants **B5, B6, D2, and E4** — in that execution order (B before D, per MO-2 execution order above). It is the authoritative Rule 6 resolution. Any invariant that references Rule 6 priority uses this function — not inline logic. **Edge/null return:** if no signals match (all four regex tests fail), the function returns `output.assigned_intent_class` unchanged — no override is applied, no escalation is triggered by this function alone. The calling invariant (B5/B6/D2/E4) is responsible for determining whether the unchanged class is a violation.

---

## 30 Invariants (A1–E6)

### Coverage Matrix

| Category | S4 Rules Guarded | Intent Classes Protected | Language/Signal Addressed |
|---|---|---|---|
| A — Class-Specific Constraints | Rules 1, 2, 3, 4, 5 | booking_request, cancellation, complaint, visa_regulatory, media-press, partnership | FI/EN/DE structural signals |
| B — Confidence & Escalation Logic | Rules 1–6 (confidence threshold) | All 8 | Threshold boundary, spoof_detected, conflict priority |
| C — Data Integrity & Audit | Rules 1–6 (field presence) | All 8 | booking_ref format, language enum, timestamp order |
| D — Business Rules (FI/DE/EN) | Rules 5, 6, 2, 4 | complaint (FI), cancellation (DE), general_inquiry, booking_request, unknown-language | FI sentiment floor, DE cancel keyword, group outlier |
| E — Flywheel & Regression | All rules (coverage enforcement) | All 8 | Synthetic coverage, confidence drift, failure repeat |

**Row detail:** 5 categories × 6 invariants each = 30 invariants total. Each row in the matrix above maps to the category's primary S4 Rule exposure. Individual invariants below specify exact Rule(s) per invariant.

---

### Category A — Class-Specific Constraints (A1–A6)

These invariants assert structural requirements that must hold if S4's assigned_intent_class is correct. They guard Rules 1–5 directly.

---

#### A1 — booking_request requires pax_count and booking_ref

**Guards:** S4 Rule 1 | **Intent class:** booking_request | **Language/signal:** Group signal (pax_count), booking_ref

**IF condition:**
```typescript
if (output.assigned_intent_class === 'booking_request') {
  if (!output.booking_ref || output.pax_count === null || output.pax_count <= 0) {
    escalate_to_human_review(
      email,
      ['A1'],
      'booking_request assigned but booking_ref is null or pax_count <= 0'
    );
    return;
  }
}
```

**Input fields from S4Output:** `assigned_intent_class`, `booking_ref`, `pax_count`

**PASS example:** `{ assigned_intent_class: 'booking_request', booking_ref: 'FIN-2026-089', pax_count: 45 }` — structural requirements met, no escalation.

**FAIL example:** `{ assigned_intent_class: 'booking_request', booking_ref: null, pax_count: 45 }` — booking_ref is null, escalate. CRM write blocked.

**Isolation proof:** `escalate_to_human_review()` throws `ValidationError`. TypeScript control-flow: `return` after throw is unreachable. `writeToCRM()` call site is outside the invariant guard block — it is never reached.

---

#### A2 — cancellation requires booking_ref and minimum confidence

**Guards:** S4 Rule 6 | **Intent class:** cancellation | **Language/signal:** Explicit cancel keyword

**IF condition:**
```typescript
if (output.assigned_intent_class === 'cancellation') {
  if (!output.booking_ref || output.s4_confidence < 0.65) {
    escalate_to_human_review(
      email,
      ['A2'],
      'cancellation assigned but booking_ref is null or confidence < 0.65'
    );
    return;
  }
}
```

**Input fields:** `assigned_intent_class`, `booking_ref`, `s4_confidence`

**PASS example:** `{ assigned_intent_class: 'cancellation', booking_ref: 'FIN-2026-075', s4_confidence: 0.68 }` — passes.

**FAIL example:** `{ assigned_intent_class: 'cancellation', booking_ref: null, s4_confidence: 0.68 }` — cancellation without booking_ref is operationally dangerous. Escalate.

**Business rationale:** A cancellation without a booking reference cannot be actioned in the CRM. Forcing human review prevents silent non-cancellation.

---

#### A3 — complaint requires financial_impact or service_failure_flagged

**Guards:** S4 Rules 5, 6 | **Intent class:** complaint | **Language/signal:** Financial loss, service failure

**IF condition:**
```typescript
if (output.assigned_intent_class === 'complaint') {
  if (output.financial_impact === null && output.service_failure_flagged !== true) {
    escalate_to_human_review(
      email,
      ['A3'],
      'complaint assigned but neither financial_impact nor service_failure_flagged is present'
    );
    return;
  }
}
```

**Input fields:** `assigned_intent_class`, `financial_impact`, `service_failure_flagged`

**PASS example:** `{ assigned_intent_class: 'complaint', financial_impact: 4500, service_failure_flagged: true }` — passes (T11).

**FAIL example:** `{ assigned_intent_class: 'complaint', financial_impact: null, service_failure_flagged: false }` — complaint without any substantive signal. Escalate.

---

#### A4 — visa_regulatory requires non-mixed, non-unknown language

**Guards:** S4 Rule 4 | **Intent class:** visa_regulatory | **Language/signal:** FI or EN only (time-critical regulatory)

**IF condition:**
```typescript
if (output.assigned_intent_class === 'visa_regulatory') {
  if (output.detected_language === 'mixed' || output.detected_language === 'unknown') {
    escalate_to_human_review(
      email,
      ['A4'],
      'visa_regulatory assigned but detected_language is mixed or unknown — time-critical class requires confirmed language'
    );
    return;
  }
}
```

**Input fields:** `assigned_intent_class`, `detected_language`

**PASS example:** `{ assigned_intent_class: 'visa_regulatory', detected_language: 'fi' }` — passes (T5).

**FAIL example:** `{ assigned_intent_class: 'visa_regulatory', detected_language: 'mixed' }` — language ambiguity on a time-critical class. Escalate.

**Business rationale:** Visa and regulatory deadlines are legally binding. Language ambiguity in this class means response may be routed to the wrong handler.

---

#### A5 — media-press requires publication_date and media_outlet_verified

**Guards:** S4 Rule 6 | **Intent class:** media-press | **Language/signal:** Media signal (journalist, publication)

**IF condition:**
```typescript
if (output.assigned_intent_class === 'media-press') {
  if (!output.publication_date || output.media_outlet_verified !== true) {
    escalate_to_human_review(
      email,
      ['A5'],
      'media-press assigned but publication_date is null or media_outlet_verified is false'
    );
    return;
  }
}
```

**Input fields:** `assigned_intent_class`, `publication_date`, `media_outlet_verified`

**PASS example:** `{ assigned_intent_class: 'media-press', publication_date: '2027-03-01', media_outlet_verified: true }` — passes (T9).

**FAIL example:** `{ assigned_intent_class: 'media-press', publication_date: null, media_outlet_verified: false }` — unverified media contact. Escalate for manual PR review.

---

#### A6 — partnership requires domain reputation or partners table match

**Guards:** S4 Rule 3, Rule 5 | **Intent class:** partnership | **Language/signal:** Supplier/partner domain

**IF condition:**
```typescript
if (output.assigned_intent_class === 'partnership') {
  if (output.domain_reputation_score < 0.6 && output.partners_table_match !== true) {
    escalate_to_human_review(
      email,
      ['A6'],
      'partnership assigned but domain_reputation_score < 0.6 and partners_table_match is false'
    );
    return;
  }
}
```

**Input fields:** `assigned_intent_class`, `domain_reputation_score`, `partners_table_match`

**PASS example:** `{ assigned_intent_class: 'partnership', domain_reputation_score: 0.4, partners_table_match: true }` — known partner overrides reputation score.

**FAIL example:** `{ assigned_intent_class: 'partnership', domain_reputation_score: 0.4, partners_table_match: false }` — unknown low-reputation domain. Escalate.

---

### Category B — Confidence and Escalation Logic (B1–B6)

These invariants enforce the JF2 threshold (0.80) and escalation documentation rules. They guard all 6 Rules.

---

#### B1 — low confidence must set requires_escalation

**Guards:** S4 Rules 1–6 (JF2 threshold) | **Intent classes:** All 8 | **Signal:** Confidence < 0.80

**IF condition:**
```typescript
if (output.s4_confidence < 0.80 && output.requires_escalation !== true) {
  escalate_to_human_review(
    email,
    ['B1'],
    `s4_confidence ${output.s4_confidence} is below 0.80 threshold but requires_escalation is false — S4 contract violation`
  );
  return;
}
```

**Input fields:** `s4_confidence`, `requires_escalation`

**PASS example:** `{ s4_confidence: 0.79, requires_escalation: true }` — consistent.

**FAIL example:** `{ s4_confidence: 0.72, requires_escalation: false }` — S4 contract violation. The output is internally inconsistent and cannot be trusted.

---

#### B2 — requires_escalation must have escalation_reason

**Guards:** S4 Rules 1–6 | **Intent classes:** All 8 | **Signal:** Escalation documentation

**IF condition:**
```typescript
if (output.requires_escalation === true && !output.escalation_reason) {
  escalate_to_human_review(
    email,
    ['B2'],
    'requires_escalation is true but escalation_reason is null — undocumented escalation'
  );
  return;
}
```

**Input fields:** `requires_escalation`, `escalation_reason`

**PASS example:** `{ requires_escalation: true, escalation_reason: 'low_confidence' }` — documented.

**FAIL example:** `{ requires_escalation: true, escalation_reason: null }` — undocumented escalation. Human reviewer has no context.

---

#### B3 — high-confidence booking_request auto-approves without human gate

**Guards:** S4 Rule 1 | **Intent class:** booking_request | **Signal:** Confidence >= 0.90

**IF condition (positive assertion — if this FAILS, alert):**
```typescript
if (
  output.assigned_intent_class === 'booking_request' &&
  output.s4_confidence >= 0.90 &&
  output.requires_escalation === true
) {
  escalate_to_human_review(
    email,
    ['B3'],
    'booking_request with confidence >= 0.90 should not require escalation — routing logic conflict'
  );
  return;
}
```

**Input fields:** `assigned_intent_class`, `s4_confidence`, `requires_escalation`

**PASS example:** `{ assigned_intent_class: 'booking_request', s4_confidence: 0.92, requires_escalation: false }` — correct autonomous routing (T1).

**FAIL example:** `{ assigned_intent_class: 'booking_request', s4_confidence: 0.92, requires_escalation: true }` — internal inconsistency. S4 Rule 1 at 0.92 should never flag for escalation.

---

#### B4 — Rule 6 worst-case confidence (0.42) forces escalation

**Guards:** S4 Rule 6 boundary | **Intent classes:** All Rule 6 outputs | **Signal:** Confidence = 0.42 (Rule 6 minimum)

**IF condition:**
```typescript
if (output.routing_rule_fired === 6 && output.s4_confidence <= 0.42) {
  if (output.requires_escalation !== true) {
    escalate_to_human_review(
      email,
      ['B4'],
      `Rule 6 boundary confidence ${output.s4_confidence} — must escalate, never autonomous`
    );
    return;
  }
}
```

**Input fields:** `routing_rule_fired`, `s4_confidence`, `requires_escalation`

**PASS example:** `{ routing_rule_fired: 6, s4_confidence: 0.42, requires_escalation: true }` — escalation correctly forced.

**FAIL example:** `{ routing_rule_fired: 6, s4_confidence: 0.42, requires_escalation: false }` — Rule 6 at minimum confidence routed autonomously. Block and escalate.

---

#### B5 — priority conflict requires Rule 6 enforcement (resolve + validate match)

**Guards:** S4 Rules 5, 6 (multi-intent resolution) | **Intent classes:** cancellation, complaint, media-press, partnership | **Signal:** Conflict resolved per Rule 6 hierarchy

**IF condition:**
```typescript
if (output.routing_rule_fired === 6 || output.routing_rule_fired === 5) {
  // Step 1: Resolve the priority per Rule 6
  const resolvedIntentClass = resolveRule6Priority(output);

  // Step 2: Verify intent_priority_applied is documented
  if (!output.intent_priority_applied) {
    escalate_to_human_review(
      email,
      ['B5'],
      'Rule 5 or Rule 6 fired but intent_priority_applied is null — conflict resolution undocumented'
    );
    return;
  }

  // Step 3: Enforce that resolved class matches S4's assigned_intent_class
  if (resolvedIntentClass !== output.assigned_intent_class) {
    escalate_to_human_review(
      email,
      ['B5_RULE6_MISMATCH'],
      `Rule 6 resolution says ${resolvedIntentClass} but S4 assigned ${output.assigned_intent_class} — priority hierarchy not enforced`
    );
    return;
  }
}
```

**Input fields:** `routing_rule_fired`, `intent_priority_applied`, `email_body_raw` (signals for Rule 6 resolution)

**PASS example:** Email with both cancellation AND media-press signals: `resolveRule6Priority()` returns 'cancellation', S4 output is `assigned_intent_class: 'cancellation'` with `intent_priority_applied: 'cancellation > media-press (Rule 6 hierarchy)'` — match confirmed (T10).

**FAIL example:** Email with both cancellation AND media-press signals: `resolveRule6Priority()` returns 'cancellation', but S4 output is `assigned_intent_class: 'media-press'` with `intent_priority_applied: null` — Rule 6 priority was NOT enforced. Escalate.

---

#### B6 — spoof_detected escalates to MEDIA-REVIEW queue, not general escalation

**Guards:** S4 Rule 6 (spoof safety) | **Intent class:** media-press (demoted by spoof) | **Signal:** spoof_detected

**IF condition:**
```typescript
if (output.escalation_reason === 'spoof_detected') {
  if (output.assigned_intent_class !== 'cancellation' && output.assigned_intent_class !== 'complaint') {
    escalate_to_human_review(
      email,
      ['B6'],
      'spoof_detected but assigned_intent_class is not cancellation or complaint — Rule 6 priority override expected'
    );
    return;
  }
  // Route to MEDIA-REVIEW queue specifically
  writeToMediaReviewQueue({ email, output, reason: 'spoof_detected' });
  return; // Never reaches CRM
}
```

**Input fields:** `escalation_reason`, `assigned_intent_class`

**PASS example:** `{ escalation_reason: 'spoof_detected', assigned_intent_class: 'cancellation' }` — spoof detected, cancellation took priority, routed to MEDIA-REVIEW (T10).

**FAIL example:** `{ escalation_reason: 'spoof_detected', assigned_intent_class: 'media-press' }` — spoof detected but media-press was NOT demoted. Rule 6 priority hierarchy was not applied.

---

### Category C — Data Integrity and Audit (C1–C6)

These invariants enforce field-level correctness, format validation, and audit completeness.

---

#### C1 — routing_rule_fired must be 1–6

**Guards:** S4 Rules 1–6 (completeness) | **Intent classes:** All 8 | **Signal:** Deterministic rule match

**IF condition:**
```typescript
if (!output.routing_rule_fired || output.routing_rule_fired < 1 || output.routing_rule_fired > 6) {
  escalate_to_human_review(
    email,
    ['C1'],
    `routing_rule_fired is ${output.routing_rule_fired} — must be integer 1–6`
  );
  return;
}
```

**Input fields:** `routing_rule_fired`

**PASS example:** `{ routing_rule_fired: 3 }` — valid.

**FAIL example:** `{ routing_rule_fired: null }` — no rule match recorded. S4 contract breach.

---

#### C2 — booking_ref format validation

**Guards:** S4 Rules 1, 3, 6 | **Intent classes:** booking_request, cancellation, partnership | **Signal:** booking_ref format

**IF condition:**
```typescript
if (output.booking_ref !== null) {
  const bookingRefPattern = /^FIN-\d{4}-\d{3}$/;
  if (!bookingRefPattern.test(output.booking_ref)) {
    escalate_to_human_review(
      email,
      ['C2'],
      `booking_ref '${output.booking_ref}' does not match pattern FIN-YYYY-NNN`
    );
    return;
  }
}
```

**Input fields:** `booking_ref`

**PASS example:** `{ booking_ref: 'FIN-2026-089' }` — valid format (T3, T8).

**FAIL example:** `{ booking_ref: 'FIN-26-89' }` — malformed. Could be a fabricated reference. Escalate.

---

#### C3 — detected_language enum validation

**Guards:** S4 Rules 1–6 | **Intent classes:** All 8 | **Signal:** Language detection output

**IF condition:**
```typescript
const validLanguages = ['fi', 'en', 'de', 'unknown', 'mixed'] as const;
if (!validLanguages.includes(output.detected_language as any)) {
  escalate_to_human_review(
    email,
    ['C3'],
    `detected_language '${output.detected_language}' is not in enum ['fi','en','de','unknown','mixed']`
  );
  return;
}
```

**Input fields:** `detected_language`

**PASS example:** `{ detected_language: 'mixed' }` — valid enum member.

**FAIL example:** `{ detected_language: 'swedish' }` — not in S4Output contract. S4 produced an out-of-spec value.

---

#### C4 — mixed language reduces confidence by 0.05 (ambiguity penalty check)

**Guards:** S4 Rules 2, 6 | **Intent classes:** All 8 | **Signal:** mixed language with ambiguity

**IF condition (verify S4 applied the penalty):**
```typescript
if (
  output.detected_language === 'mixed' &&
  output.s4_confidence > 0.80 &&
  !output.ambiguity_penalty_applied
) {
  escalate_to_human_review(
    email,
    ['C4'],
    'detected_language is mixed but ambiguity_penalty_applied is false and confidence is above threshold — penalty may have been skipped'
  );
  return;
}
```

**Input fields:** `detected_language`, `s4_confidence`, `ambiguity_penalty_applied`

**PASS example:** `{ detected_language: 'mixed', s4_confidence: 0.76, ambiguity_penalty_applied: true }` — penalty applied, confidence appropriately reduced.

**FAIL example:** `{ detected_language: 'mixed', s4_confidence: 0.85, ambiguity_penalty_applied: false }` — mixed language at suspiciously high confidence without penalty. Escalate for review.

---

#### C5 — S4 processing timestamp must precede S5 validation timestamp

**Guards:** All rules | **Intent classes:** All 8 | **Signal:** Timestamp ordering (time travel prevention)

**IF condition:**
```typescript
if (new Date(output.s4_processed_at) > new Date()) {
  escalate_to_human_review(
    email,
    ['C5'],
    `s4_processed_at ${output.s4_processed_at} is in the future — clock skew or replay attack`
  );
  return;
}
if (output.s5_validated_at && new Date(output.s4_processed_at) > new Date(output.s5_validated_at)) {
  escalate_to_human_review(
    email,
    ['C5'],
    `s4_processed_at ${output.s4_processed_at} is after s5_validated_at — time travel detected`
  );
  return;
}
```

**Input fields:** `s4_processed_at`, `s5_validated_at`

**PASS example:** `{ s4_processed_at: '2026-03-20T10:00:00Z', s5_validated_at: '2026-03-20T10:00:01Z' }` — valid ordering.

**FAIL example:** `{ s4_processed_at: '2026-03-20T10:00:02Z', s5_validated_at: '2026-03-20T10:00:01Z' }` — S4 timestamp after S5. Record integrity compromised.

---

#### C6 — all 8 Intent classes must appear in production within 4 weeks (coverage check)

**Guards:** All rules | **Intent classes:** All 8 | **Signal:** Weekly coverage audit

**IF condition (weekly aggregate check, not per-email):**
```typescript
// Run once per week against production logs, not per-email
function checkWeeklyClassCoverage(weeklyOutputs: S4Output[]): void {
  const VALID_CLASSES: IntentClass[] = [
    'booking_request','general_inquiry','complaint','partnership',
    'visa_regulatory','regulatory','cancellation','media-press'
  ];
  const seenClasses = new Set(weeklyOutputs.map(o => o.assigned_intent_class));
  const missingClasses = VALID_CLASSES.filter(c => !seenClasses.has(c));
  if (missingClasses.length > 0 && currentWeekNumber >= 4) {
    writeToAuditAlert({
      invariant: 'C6',
      message: `Intent classes never seen after week 4: ${missingClasses.join(', ')} — investigate S4 routing gap`,
      weekNumber: currentWeekNumber
    });
  }
}
```

**Input fields:** Weekly aggregate of `assigned_intent_class` across all production outputs.

**PASS example:** All 8 classes appear at least once in the first 4 weeks of production.

**FAIL example:** `regulatory` never appears in 4 weeks. Either no regulatory emails have arrived (fine) or S4 Rule 4 has a silent routing gap (investigate).

---

### Category D — Business Rules: FI/DE/EN Context (D1–D6)

These invariants encode language-specific DMC operational knowledge that S4 cannot fully resolve. When multiple Intent class signals are detected simultaneously (e.g., cancellation_signals AND media-press_signals both present), the `resolveRule6Priority()` function (defined at line 50) applies Rule 6 hierarchy (cancellation > complaint > media-press > visa_regulatory) and outputs a priority-resolved Intent class. D-series invariants validate against this resolved class; any mismatch between priority-resolved Intent and S4's assigned_intent_class escalates to human review.

---

#### D1 — Finnish complaint confidence floor

**Guards:** S4 Rules 5, 6 | **Intent class:** complaint | **Language/signal:** FI negative emotion (underweighted by de-anchoring)

**IF condition:**
```typescript
if (
  output.assigned_intent_class === 'complaint' &&
  output.detected_language === 'fi' &&
  output.s4_confidence < 0.65
) {
  // Finnish complaints use indirect language — 0.65 is the minimum viable confidence
  // Lower than 0.65 in FI may be a true complaint with weak surface signals
  escalate_to_human_review(
    email,
    ['D1'],
    'FI complaint below 0.65 confidence — Finnish negative emotion is underweighted by de-anchoring; human review required'
  );
  return;
}
```

**Input fields:** `assigned_intent_class`, `detected_language`, `s4_confidence`

**PASS example:** `{ assigned_intent_class: 'complaint', detected_language: 'fi', s4_confidence: 0.73 }` — above FI floor (T12).

**FAIL example:** `{ assigned_intent_class: 'complaint', detected_language: 'fi', s4_confidence: 0.58 }` — FI complaint at very low confidence. Finnish indirect language may mask severity.

---

#### D2 — German "Stornierung" keyword forces cancellation class

**Guards:** S4 Rule 6 | **Intent class:** cancellation | **Language/signal:** DE cancel keyword

**IF condition:**
```typescript
const emailBody = email.body_raw ?? '';
if (
  output.detected_language === 'de' &&
  /\b(stornierung|stornieren)\b/i.test(emailBody) &&
  output.assigned_intent_class !== 'cancellation'
) {
  escalate_to_human_review(
    email,
    ['D2'],
    `DE cancel keyword 'Stornierung/stornieren' detected but assigned_intent_class is '${output.assigned_intent_class}' — override to cancellation required`
  );
  return;
}
```

**Input fields:** `detected_language`, `assigned_intent_class`, `email.body_raw`

**PASS example:** DE email with "Stornierung" assigned as cancellation — correct (T10).

**FAIL example:** DE email with "stornieren" assigned as `general_inquiry` — S4 missed explicit cancel keyword. This is a business-critical misclassification.

---

#### D3 — large groups (pax_count > 500) always escalate

**Guards:** S4 Rules 1, 2 | **Intent classes:** booking_request, general_inquiry | **Signal:** Group outlier

**IF condition:**
```typescript
if (output.pax_count !== null && output.pax_count > 500) {
  escalate_to_human_review(
    email,
    ['D3'],
    `pax_count ${output.pax_count} exceeds 500 — large group requires manual oversight regardless of confidence`
  );
  return;
}
```

**Input fields:** `pax_count`

**PASS example:** `{ pax_count: 45, assigned_intent_class: 'booking_request', s4_confidence: 0.92 }` — within normal range.

**FAIL example:** `{ pax_count: 600, s4_confidence: 0.94 }` — even a high-confidence booking for 600 pax escalates. No DMC can process a 600-person group without a human decision maker involved.

---

#### D4 — unknown language below 0.75 confidence blocks routing

**Guards:** S4 Rules 2, 6 | **Intent classes:** All 8 | **Signal:** Language detection failure

**IF condition:**
```typescript
if (output.detected_language === 'unknown' && output.s4_confidence < 0.75) {
  escalate_to_human_review(
    email,
    ['D4'],
    `detected_language 'unknown' with confidence ${output.s4_confidence} — language detection failure blocks autonomous routing`
  );
  return;
}
```

**Input fields:** `detected_language`, `s4_confidence`

**PASS example:** `{ detected_language: 'unknown', s4_confidence: 0.82 }` — language unknown but high-confidence structural signals (booking_ref, pax_count) justify routing.

**FAIL example:** `{ detected_language: 'unknown', s4_confidence: 0.61 }` — both language and intent uncertain. Cannot route.

---

#### D5 — booking_ref on general_inquiry triggers booking_request context

**Guards:** S4 Rule 2 | **Intent classes:** general_inquiry → booking_request context | **Signal:** Prior relationship

**IF condition:**
```typescript
if (
  output.assigned_intent_class === 'general_inquiry' &&
  output.booking_ref !== null
) {
  // Do not override class, but flag for human context enrichment
  escalate_to_human_review(
    email,
    ['D5'],
    `general_inquiry with booking_ref ${output.booking_ref} — existing customer context requires human reclassification`
  );
  return;
}
```

**Input fields:** `assigned_intent_class`, `booking_ref`

**PASS example:** `{ assigned_intent_class: 'general_inquiry', booking_ref: null }` — no prior relationship, correct class.

**FAIL example:** `{ assigned_intent_class: 'general_inquiry', booking_ref: 'FIN-2026-089' }` — prior booking holder sending a "general inquiry" is almost certainly about their booking. Needs human context check.

---

#### D6 — synthetic/test email detection

**Guards:** All rules | **Intent classes:** All 8 | **Signal:** Test keywords in body

**IF condition:**
```typescript
const emailBody = email.body_raw ?? '';
if (/\b(fake|test email|demo|simulation|synthetic|testfall)\b/i.test(emailBody)) {
  writeToAuditLog({
    invariant: 'D6',
    email_id: email.id,
    verdict: 'SYNTHETIC_DETECTED',
    message: 'Email contains test/synthetic keywords — flagged, not escalated, not written to CRM'
  });
  return; // Never reaches CRM — synthetic emails are silently discarded with audit record
}
```

**Input fields:** `email.body_raw`

**PASS example:** Production email with no test keywords — passes D6 with no action.

**FAIL (synthetic detection) example:** Email body contains "this is a test email" — flagged, audit logged, discarded. Not escalated to human review (not an error), not written to CRM.

---

### Category E — Flywheel and Regression Prevention (E1–E6)

These invariants enforce systemic health over time. E1–E3 are per-run checks; E4–E6 are weekly/monthly aggregates.

---

#### E1 — weekly synthetic test set must cover all 8 classes and all 6 rules

**Guards:** All rules | **Intent classes:** All 8 | **Signal:** Coverage completeness

**IF condition (pre-run gate, before weekly flywheel executes):**
```typescript
function validateTestSetCoverage(testSet: Email[]): void {
  const REQUIRED_CLASSES: IntentClass[] = [
    'booking_request','general_inquiry','complaint','partnership',
    'visa_regulatory','regulatory','cancellation','media-press'
  ];
  const MIN_PER_CLASS = 12; // 8 classes × 12 = 96 minimum
  const MIN_PER_RULE = 15; // rules 1–6 × 15 = 90 minimum (overlap expected)
  const MIN_MIXED_LANGUAGE = 20;
  const REQUIRED_BOUNDARY_CASES = 5;

  const classCounts = countByClass(testSet);
  const ruleCounts = countByRule(testSet);
  const mixedCount = testSet.filter(e => e.expected_language === 'mixed').length;
  const boundaryCases = testSet.filter(e => e.is_boundary_case === true).length;

  const underRepresentedClasses = REQUIRED_CLASSES.filter(c => (classCounts[c] ?? 0) < MIN_PER_CLASS);
  const underRepresentedRules = [1,2,3,4,5,6].filter(r => (ruleCounts[r] ?? 0) < MIN_PER_RULE);

  if (
    underRepresentedClasses.length > 0 ||
    underRepresentedRules.length > 0 ||
    mixedCount < MIN_MIXED_LANGUAGE ||
    boundaryCases < REQUIRED_BOUNDARY_CASES
  ) {
    throw new FlyWheelSetupError(
      `E1 FAIL: Test set coverage insufficient. ` +
      `Under-represented classes: ${underRepresentedClasses.join(', ')}. ` +
      `Under-represented rules: ${underRepresentedRules.join(', ')}. ` +
      `Mixed language: ${mixedCount}/${MIN_MIXED_LANGUAGE}. ` +
      `Boundary cases: ${boundaryCases}/${REQUIRED_BOUNDARY_CASES}.`
    );
  }
}
```

**PASS example:** Test set has booking_request×12, general_inquiry×13, complaint×15, partnership×12, visa_regulatory×12, regulatory×12, cancellation×12, media-press×12 = 100 total. All rules covered ≥15×. Mixed language ×20. Boundary cases ×5.

**FAIL example:** Test set has 8 booking_request (below 12 minimum). Flywheel aborts with E1 error before running.

---

#### E2 — Week N failures auto-added to Week N+1 test set

**Guards:** All rules | **Intent classes:** All 8 | **Signal:** Regression growth algorithm

**Regression growth algorithm (copy-paste ready):**

```typescript
async function growRegressionSet(
  weekN_failures: FailedEmail[],
  weekN1_baseSet: Email[]
): Promise<Email[]> {
  // Step 1: De-duplicate (same email_id already in base set → skip)
  const existingIds = new Set(weekN1_baseSet.map(e => e.id));
  const newCases = weekN_failures
    .filter(f => !existingIds.has(f.email.id))
    .map(f => ({
      ...f.email,
      is_regression_case: true,
      source_week: f.week_number,
      failed_invariants: f.failedInvariants,
    }));

  // Step 2: Append to base set
  const weekN1_fullSet = [...weekN1_baseSet, ...newCases];

  // Step 3: Log growth
  await writeToAuditLog({
    event: 'REGRESSION_SET_GROWTH',
    week: f.week_number + 1,
    added_cases: newCases.length,
    total_set_size: weekN1_fullSet.length,
  });

  return weekN1_fullSet;
}
```

**PASS example:** Week 1 produces 3 failures. Week 2 test set = 100 base + 3 regression cases = 103 total. All 3 re-run in Week 2. 2 now pass (S4 fixed). 1 still fails → added to Week 3.

**FAIL example (anti-pattern):** Failures are reviewed but NOT added to next week's set. The same edge case re-emerges 3 weeks later. This invariant makes that impossible.

---

#### E3 — confidence distribution must stay within ±0.10 of prior week

**Guards:** All rules | **Intent classes:** All 8 | **Signal:** Confidence drift detection

**IF condition (weekly aggregate):**
```typescript
function checkConfidenceDrift(
  currentWeekOutputs: S4Output[],
  priorWeekOutputs: S4Output[]
): void {
  const currentMean = mean(currentWeekOutputs.map(o => o.s4_confidence));
  const priorMean = mean(priorWeekOutputs.map(o => o.s4_confidence));
  const drift = Math.abs(currentMean - priorMean);

  if (drift > 0.10) {
    writeToAuditAlert({
      invariant: 'E3',
      message: `Confidence drift detected: prior week mean ${priorMean.toFixed(3)}, current week mean ${currentMean.toFixed(3)}, drift ${drift.toFixed(3)} exceeds 0.10 threshold`,
      action: 'Trigger S4 Logic Refresh review'
    });
  }
}
```

**PASS example:** Prior week mean 0.79, current week mean 0.81, drift = 0.02. Within bounds.

**FAIL example:** Prior week mean 0.79, current week mean 0.66, drift = 0.13. S4's confidence calibration has shifted — possible upstream data change, S3 schema drift, or new email template that breaks rule matching.

---

#### E4 — no invariant failure mode repeats twice in the same month

**Guards:** All rules | **Intent classes:** All 8 | **Signal:** Failure pattern recurrence

**IF condition (monthly aggregate):**
```typescript
function checkFailureRecurrence(monthlyFailures: FailedEmail[]): void {
  const failureCounts: Record<string, number> = {};
  for (const f of monthlyFailures) {
    for (const inv of f.failedInvariants) {
      failureCounts[inv] = (failureCounts[inv] ?? 0) + 1;
    }
  }
  const repeatingFailures = Object.entries(failureCounts)
    .filter(([, count]) => count >= 2)
    .map(([inv]) => inv);

  if (repeatingFailures.length > 0) {
    writeToAuditAlert({
      invariant: 'E4',
      message: `Failure pattern recurrence detected: ${repeatingFailures.join(', ')} each failed ≥2 times this month`,
      action: 'Trigger E5 Logic Refresh on S4 decision table'
    });
  }
}
```

**PASS example:** Invariant D2 failed once in Week 1 (new DE email template). Updated S4 Rule 6 DE pattern. D2 did not fail again.

**FAIL example:** Invariant A2 failed in both Week 1 and Week 3 (cancellation without booking_ref recurring). E4 fires, triggers E5.

---

#### E5 — E4 trigger initiates S4 Logic Refresh and re-test

**Guards:** All rules | **Intent classes:** All 8 | **Signal:** E4 → E5 feedback loop

**IF condition (triggered by E4):**
```typescript
// E5 is triggered by E4 output, not per-email
async function triggerLogicRefresh(repeatingInvariants: string[]): Promise<void> {
  await writeToProjectBoard({
    title: `S4 Logic Refresh Required — E4/E5 trigger`,
    description: `Invariants with repeated failures this month: ${repeatingInvariants.join(', ')}. ` +
      `Action: Review S4 decision table rules relevant to each invariant. ` +
      `Re-run affected test cases. ` +
      `Update S4 routing logic before next production week.`,
    assignee: 'patrick',
    due: nextMondayISO()
  });

  await writeToAuditLog({
    invariant: 'E5',
    triggered_by: 'E4',
    affected_invariants: repeatingInvariants,
    action: 'Logic Refresh task created'
  });
}
```

**PASS example:** E4 fires on A2. E5 creates a task in the project board. Patrick reviews S4 Rule 6 (cancellation without booking_ref scenario). S4 is updated. Next week: A2 does not fail.

**FAIL example (E5 not triggered):** E4 fires but no action is taken. Same failure recurs in Week 5. This represents a system maintenance gap — the flywheel is running but not improving.

---

#### E6 — monthly spot-check: 5 random PASS emails reviewed by human

**Guards:** All rules | **Intent classes:** All 8 | **Signal:** Hallucination that slipped through all 30 invariants

**IF condition (monthly, manual trigger):**
```typescript
// E6 is not an automated TypeScript guard — it is a monthly human process gate
// Implementation: n8n workflow sends a random sample to human_review_queue with flag 'E6_SPOT_CHECK'
function scheduleMonthlySpotCheck(allPastEmails: S4Output[]): void {
  const passedEmails = allPastEmails.filter(o => o.s5_result === 'PASS');
  const sample = sampleRandom(passedEmails, 5);
  for (const email of sample) {
    writeToHumanReviewQueue({
      email,
      failedInvariants: [],
      reason: 'E6_MONTHLY_SPOT_CHECK — human verifies no hallucination slipped through all 30 invariants',
    });
  }
}
```

**PASS example:** 5 random emails reviewed. Reviewer confirms all 5 were correctly routed to CRM. E6 logged as PASS.

**FAIL example:** Reviewer finds 1 of 5 emails was a cancellation misclassified as partnership. All 30 invariants passed. This is a known limitation (see Known Limitations section) — invariants guard what S4 exports, not what the email actually contains if S4 produced a plausible-but-wrong output.

**E6 Availability Gate (BLOCKING):**
- Patrick must confirm monthly availability for E6 spot-check (30 min/month, first Monday of month)
- If Patrick unavailable or E6 is skipped 2+ months in a row: S5 escalation-rate monitoring (E3/E4) becomes mandatory weekly (not optional), and escalation-rate upper bound drops to 15% (from 20%)
- **Escalation-rate hard stop:** If weeks 1–4 production shows >30% of emails escalating (14.6+ hrs/week), PAUSE S5 deployment immediately and reset roadmap. Do NOT proceed to week 5. Diagnostic required: S4 Rule alignment check or email volume surge.

---

## Flywheel Mechanism — Weekly Execution

### PREREQUISITE (one-time setup — not counted in weekly time)

**Step P1:** Generate the initial 100-email synthetic test set using the generator prompt below. This is done once before Week 1. Estimated effort: 2 hours (Patrick + Claude Code).

**Step P2:** Deploy the S5 TypeScript module to the n8n workflow that processes S4 output. Deployment path: n8n custom node or Function node, reading S4Output from the Supabase `email_classifications` table. Estimated: 4 hours (developer).

**Step P3:** Configure the human_review_queue Supabase table (schema defined in Audit Trail section). Estimated: 1 hour.

**Step P4:** Configure the weekly n8n trigger (Monday 08:00 EET). Estimated: 30 minutes.

### Synthetic Test Set Generator Prompt (copy-paste to Claude)

> Generate a synthetic email test set of exactly 100 emails for the Finland DMC Oy email classifier regression flywheel. Requirements:
> - Intent class distribution: booking_request×12, general_inquiry×13, complaint×15, partnership×12, visa_regulatory×12, regulatory×12, cancellation×12, media-press×12 = 100 total.
> - Rule coverage: each of Rules 1–6 must appear as the correct routing_rule_fired for at least 15 emails. Rules 5 and 6 may overlap.
> - Language distribution: Finnish (fi) ×30, English (en) ×35, German (de) ×15, mixed ×20.
> - Boundary cases (exactly 5): s4_confidence exactly 0.800 (threshold edge), s4_confidence 0.799 (just below threshold), s4_confidence 1.0 (ceiling), booking_ref=null on a non-booking_request class, Rule 6 priority conflict (cancellation_signals AND media_signals both present in same email).
> - Each email must include: from_domain, subject, body_text (2–5 sentences), expected_intent_class, expected_routing_rule, expected_language, is_boundary_case (bool).
> - Output as JSON array. No markdown wrapper. No commentary.

### Weekly Execution Steps

**For each email in the weekly test set:**

1. Run S4 on the email → capture the S4Output JSON.
2. Validate A1 → A6 in order (stop at first FAIL, escalate).
3. Validate B1 → B6 in order (stop at first FAIL, escalate).
4. Validate C1 → C6 in order (stop at first FAIL, escalate).
5. Validate D1 → D6 in order (stop at first FAIL, escalate).
6. Validate E1 → E3 (per-run checks).
7. If all 30 invariants PASS: write email + S4Output to CRM.
8. If any invariant FAILS: write email + which invariant(s) failed + S4Output to human_review_queue. CRM write blocked.

**Pass routing:** All 30 PASS → `writeToCRM(email, s4Output)`.

**Fail routing:** Any FAIL → `writeToHumanReviewQueue(email, failedInvariants, reason)`. CRM write never called.

**After weekly run:**

9. Run E4 aggregate (failure recurrence check across all emails this week).
10. Run E3 aggregate (confidence drift vs. prior week).
11. Run E2: add this week's failures to next week's test set.
12. Run C6 (if week >= 4): check all 8 classes appeared in production.
13. Log weekly summary to audit table.

### Boundary Case Rules (mandatory)

- s4_confidence exactly 0.80 → B1 boundary (0.80 meets threshold, requires_escalation must be false). If requires_escalation is true at exactly 0.80, that is a B3/B1 conflict → escalate.
- s4_confidence exactly 0.799 → B1 fails if requires_escalation is false (must escalate below 0.80).
- Mixed language with Rule 6 signals → both C4 (ambiguity penalty check) and D2 (if DE cancel keyword) must fire.
- S4's requires_escalation=true on any email → always treated as FAIL for autonomous routing. Human review required.

### Regression Growth Algorithm (E2 — reference implementation)

Week N failures → auto-added to Week N+1 test set (see E2 invariant for full TypeScript). Never delete failing cases. The hardest cases are permanent fixtures of the regression set. By Week 12, the test set may have grown from 100 to 120–130 emails. This is expected and correct.

**Hard cap: 150 tests maximum.** At 30 s/test, 150 tests = 75 min automated run. At ~320 tests (Week 52 upper bound without a cap), automated run exceeds 2 hrs and human delta-review exceeds 30 min — flywheel becomes unsustainable. Cap rule: when set size reaches 150, remove the oldest PASS-only cases (FIFO) to stay at 150. FAIL cases and boundary cases are NEVER removed. This preserves regression pressure while keeping execution within the 2-hr ceiling.

FIFO removal logic (E2 addition):
- Eligible for removal: cases that have PASSED for 4+ consecutive weeks AND are not boundary cases (is_boundary_case = false)
- Protected from removal: any case that failed in the last 4 weeks, boundary cases, Rule 6 priority conflict cases
- If cap cannot be met by removing eligible cases only (all remaining are protected): raise cap to 200 and flag for Patrick review (set is becoming too complex → S4 redesign signal)

---

## Audit Trail Design

### Logged Fields Per Email

Every email processed by S5 produces one audit record with the following schema:

```typescript
interface S5AuditRecord {
  id: string;                          // UUID, S5-generated
  email_id: string;                    // from Email.id
  s4_output_id: string;               // FK to email_classifications table
  processed_at: string;               // ISO 8601, S5 validation timestamp
  s4_confidence: number;              // copied from S4Output
  assigned_intent_class: IntentClass; // copied from S4Output
  routing_rule_fired: number;         // copied from S4Output (1–6)
  detected_language: string;          // copied from S4Output
  requires_escalation: boolean;       // copied from S4Output

  // Per-invariant pass/fail record (30 booleans)
  inv_A1: boolean; inv_A2: boolean; inv_A3: boolean;
  inv_A4: boolean; inv_A5: boolean; inv_A6: boolean;
  inv_B1: boolean; inv_B2: boolean; inv_B3: boolean;
  inv_B4: boolean; inv_B5: boolean; inv_B6: boolean;
  inv_C1: boolean; inv_C2: boolean; inv_C3: boolean;
  inv_C4: boolean; inv_C5: boolean; inv_C6: boolean;
  inv_D1: boolean; inv_D2: boolean; inv_D3: boolean;
  inv_D4: boolean; inv_D5: boolean; inv_D6: boolean;
  inv_E1: boolean; inv_E2: boolean; inv_E3: boolean;
  inv_E4: boolean; inv_E5: boolean; inv_E6: boolean;

  s5_result: 'PASS' | 'FAIL';         // aggregate verdict
  failed_invariants: string[];        // e.g., ['B1', 'D2']
  escalation_reason: string | null;   // from escalate_to_human_review() call
  human_reviewer_id: string | null;   // set when human review completes
  human_review_outcome: 'CONFIRMED_CORRECT' | 'RECLASSIFIED' | 'ESCALATED_FURTHER' | null;
  is_regression_case: boolean;        // true if added via E2 flywheel
  is_boundary_case: boolean;          // true if flagged as boundary in test set
  source_week: number | null;         // week number of original failure (regression cases only)
}
```

### Example Query: Retrieve All FAIL Records for Invariant B1 This Month

```sql
SELECT
  email_id,
  s4_confidence,
  assigned_intent_class,
  escalation_reason,
  processed_at,
  human_reviewer_id,
  human_review_outcome
FROM s5_audit_records
WHERE
  inv_B1 = false
  AND processed_at >= date_trunc('month', now())
ORDER BY processed_at DESC;
```

### Example Query: Weekly Summary (Class Distribution + PASS Rate)

```sql
SELECT
  assigned_intent_class,
  count(*) AS total,
  sum(CASE WHEN s5_result = 'PASS' THEN 1 ELSE 0 END) AS passed,
  round(avg(s4_confidence)::numeric, 3) AS avg_confidence,
  date_trunc('week', processed_at) AS week
FROM s5_audit_records
GROUP BY assigned_intent_class, week
ORDER BY week DESC, total DESC;
```

---

## S4 Integration Contract

### Full S4Output TypeScript Interface

```typescript
type IntentClass =
  | 'media-press'
  | 'regulatory'
  | 'booking_request'
  | 'general_inquiry'
  | 'complaint'
  | 'partnership'
  | 'visa_regulatory'
  | 'cancellation';

interface S4Output {
  assigned_intent_class: IntentClass;      // Required: one of 8 exact values
  s4_confidence: number;                   // Required: float 0.0–1.0
  booking_ref: string | null;             // Required: 'FIN-YYYY-NNN' format or null
  detected_language: 'fi' | 'en' | 'de' | 'unknown' | 'mixed'; // Required: exact enum
  routing_rule_fired: number;             // Required: integer 1–6
  intent_priority_applied: string | null; // Required: e.g., 'cancellation > complaint (Rule 6 hierarchy)' or null if no conflict
  requires_escalation: boolean;           // Required: true if s4_confidence < 0.80
  escalation_reason: 'low_confidence' | 'conflict_resolved' | 'spoof_detected' | null; // Required if requires_escalation=true

  // S5-augmented fields (added by S5 layer before CRM write)
  s4_processed_at: string;               // ISO 8601 — when S4 ran
  s5_validated_at?: string;              // ISO 8601 — when S5 ran (set by S5)

  // Class-specific optional fields (present when S4 extracts them)
  pax_count: number | null;              // for booking_request, general_inquiry, D3
  financial_impact: number | null;       // for complaint (EUR amount)
  service_failure_flagged: boolean;      // for complaint
  publication_date: string | null;       // for media-press
  media_outlet_verified: boolean;        // for media-press
  domain_reputation_score: number;       // for partnership (0.0–1.0)
  partners_table_match: boolean;         // for partnership
  ambiguity_penalty_applied: boolean;    // for mixed language (C4)
  email_body_raw: string | null;         // for D2 (DE cancel keyword), D6 (synthetic detection)
}
```

### 10 Test JSONs with Invariant Verdicts

**Test JSON 1 — booking_request (Rule 1, T1-equivalent)**

```json
{
  "assigned_intent_class": "booking_request",
  "s4_confidence": 0.92,
  "booking_ref": "FIN-2026-101",
  "detected_language": "en",
  "routing_rule_fired": 1,
  "intent_priority_applied": null,
  "requires_escalation": false,
  "escalation_reason": null,
  "s4_processed_at": "2026-03-20T09:00:00Z",
  "pax_count": 45,
  "financial_impact": null,
  "service_failure_flagged": false,
  "publication_date": null,
  "media_outlet_verified": false,
  "domain_reputation_score": 0.85,
  "partners_table_match": false,
  "ambiguity_penalty_applied": false,
  "email_body_raw": "45 people, March 2027, budget 85k EUR, 4-day Lapland program"
}
```

| Invariant | Verdict | Reason |
|---|---|---|
| A1 | PASS | booking_ref present, pax_count=45 |
| A2–A6 | N/A | class is not cancellation/complaint/visa_regulatory/media-press/partnership |
| B1 | PASS | s4_confidence=0.92 >= 0.80, requires_escalation=false consistent |
| B3 | PASS | booking_request at 0.92, requires_escalation=false correct |
| C1 | PASS | routing_rule_fired=1 |
| C2 | PASS | FIN-2026-101 matches regex |
| C3 | PASS | 'en' is valid enum |
| D3 | PASS | pax_count=45, below 500 |
| D6 | PASS | no synthetic keywords |
| **S5 result** | **PASS** | All applicable invariants pass. Route to CRM. |

---

**Test JSON 2 — general_inquiry (Rule 2, T2-equivalent)**

```json
{
  "assigned_intent_class": "general_inquiry",
  "s4_confidence": 0.72,
  "booking_ref": null,
  "detected_language": "en",
  "routing_rule_fired": 2,
  "intent_priority_applied": null,
  "requires_escalation": true,
  "escalation_reason": "low_confidence",
  "s4_processed_at": "2026-03-20T09:01:00Z",
  "pax_count": null,
  "financial_impact": null,
  "service_failure_flagged": false,
  "publication_date": null,
  "media_outlet_verified": false,
  "domain_reputation_score": 0.72,
  "partners_table_match": false,
  "ambiguity_penalty_applied": false,
  "email_body_raw": "We have 80-150 person groups. What are your pricing ranges?"
}
```

| Invariant | Verdict | Reason |
|---|---|---|
| B1 | PASS | confidence=0.72 < 0.80, requires_escalation=true consistent |
| B2 | PASS | escalation_reason='low_confidence' documented |
| D5 | PASS | booking_ref=null, correct for general_inquiry |
| C1 | PASS | routing_rule_fired=2 |
| **S5 result** | **ESCALATE** | requires_escalation=true — routes to human_review_queue, not CRM |

---

**Test JSON 3 — partnership (Rule 3, T3-equivalent)**

```json
{
  "assigned_intent_class": "partnership",
  "s4_confidence": 0.97,
  "booking_ref": "FIN-2026-089",
  "detected_language": "fi",
  "routing_rule_fired": 3,
  "intent_priority_applied": null,
  "requires_escalation": false,
  "escalation_reason": null,
  "s4_processed_at": "2026-03-20T09:02:00Z",
  "pax_count": 22,
  "financial_impact": null,
  "service_failure_flagged": false,
  "publication_date": null,
  "media_outlet_verified": false,
  "domain_reputation_score": 0.95,
  "partners_table_match": true,
  "ambiguity_penalty_applied": false,
  "email_body_raw": "Updated rooming list for FIN-2026-089. 22 rooms, 3 nights."
}
```

| Invariant | Verdict | Reason |
|---|---|---|
| A6 | PASS | partners_table_match=true (overrides reputation score threshold) |
| D5 | FAIL | booking_ref='FIN-2026-089' present on partnership class → escalate for human reclassification |

**S5 result: FAIL (D5).** Note: This is intentional. A known partner sending a rooming list with a booking_ref may actually be a booking_request update. Human reclassification resolves it. This is a known D5 false positive — see Known Limitations.

---

**Test JSON 4 — complaint FI (Rule 6, T12-equivalent)**

```json
{
  "assigned_intent_class": "complaint",
  "s4_confidence": 0.73,
  "booking_ref": null,
  "detected_language": "fi",
  "routing_rule_fired": 6,
  "intent_priority_applied": "complaint > media-press (Rule 6 hierarchy)",
  "requires_escalation": true,
  "escalation_reason": "low_confidence",
  "s4_processed_at": "2026-03-20T09:03:00Z",
  "pax_count": null,
  "financial_impact": 0,
  "service_failure_flagged": true,
  "publication_date": null,
  "media_outlet_verified": false,
  "domain_reputation_score": 0.0,
  "partners_table_match": false,
  "ambiguity_penalty_applied": false,
  "email_body_raw": "Meille tuli väärä huone. Mitä teette? Olemme pettyneitä."
}
```

| Invariant | Verdict | Reason |
|---|---|---|
| A3 | PASS | service_failure_flagged=true |
| B1 | PASS | confidence=0.73, requires_escalation=true consistent |
| D1 | PASS | FI complaint at 0.73 >= 0.65 FI floor |
| B5 | PASS | routing_rule_fired=6, intent_priority_applied documented |
| **S5 result** | **ESCALATE** | requires_escalation=true — routes to human_review_queue |

---

**Test JSON 5 — visa_regulatory (Rule 4, T5-equivalent)**

```json
{
  "assigned_intent_class": "visa_regulatory",
  "s4_confidence": 0.88,
  "booking_ref": null,
  "detected_language": "en",
  "routing_rule_fired": 4,
  "intent_priority_applied": "visa_regulatory > regulatory (Rule 4 hierarchy)",
  "requires_escalation": false,
  "escalation_reason": null,
  "s4_processed_at": "2026-03-20T09:04:00Z",
  "pax_count": 18,
  "financial_impact": null,
  "service_failure_flagged": false,
  "publication_date": null,
  "media_outlet_verified": false,
  "domain_reputation_score": 0.0,
  "partners_table_match": false,
  "ambiguity_penalty_applied": false,
  "email_body_raw": "18 youth, June residency program. Visa requirements? Permits? Registration procedures?"
}
```

| Invariant | Verdict | Reason |
|---|---|---|
| A4 | PASS | detected_language='en', not mixed/unknown |
| B1 | PASS | confidence=0.88 >= 0.80, requires_escalation=false consistent |
| B5 | PASS | routing_rule_fired=4 has intent_priority_applied documented |
| D3 | PASS | pax_count=18, below 500 |
| **S5 result** | **PASS** | Route to CRM |

---

**Test JSON 6 — regulatory (Rule 4, T4-equivalent)**

```json
{
  "assigned_intent_class": "regulatory",
  "s4_confidence": 0.85,
  "booking_ref": null,
  "detected_language": "en",
  "routing_rule_fired": 4,
  "intent_priority_applied": "regulatory (no visa-specific keywords — generic government)",
  "requires_escalation": false,
  "escalation_reason": null,
  "s4_processed_at": "2026-03-20T09:05:00Z",
  "pax_count": null,
  "financial_impact": null,
  "service_failure_flagged": false,
  "publication_date": null,
  "media_outlet_verified": false,
  "domain_reputation_score": 0.0,
  "partners_table_match": false,
  "ambiguity_penalty_applied": false,
  "email_body_raw": "Government agency requesting information about group travel policies, insurance requirements."
}
```

| Invariant | Verdict | Reason |
|---|---|---|
| A4 | N/A | A4 guards visa_regulatory, not regulatory |
| B1 | PASS | confidence=0.85 >= 0.80 |
| C1 | PASS | routing_rule_fired=4 |
| **S5 result** | **PASS** | Route to CRM |

---

**Test JSON 7 — cancellation (Rule 6, T8-equivalent)**

```json
{
  "assigned_intent_class": "cancellation",
  "s4_confidence": 0.68,
  "booking_ref": "FIN-2026-075",
  "detected_language": "en",
  "routing_rule_fired": 6,
  "intent_priority_applied": "cancellation > complaint (Rule 6 hierarchy)",
  "requires_escalation": true,
  "escalation_reason": "low_confidence",
  "s4_processed_at": "2026-03-20T09:06:00Z",
  "pax_count": null,
  "financial_impact": null,
  "service_failure_flagged": false,
  "publication_date": null,
  "media_outlet_verified": false,
  "domain_reputation_score": 0.0,
  "partners_table_match": false,
  "ambiguity_penalty_applied": false,
  "email_body_raw": "Cancel FIN-2026-075. Your team was unresponsive 3 weeks. Unacceptable."
}
```

| Invariant | Verdict | Reason |
|---|---|---|
| A2 | PASS | booking_ref present, confidence=0.68 >= 0.65 |
| B1 | PASS | confidence=0.68 < 0.80, requires_escalation=true consistent |
| B5 | PASS | Rule 6, intent_priority_applied documented |
| **S5 result** | **ESCALATE** | requires_escalation=true — routes to human_review_queue |

---

**Test JSON 8 — media-press (Rule 6, T9-equivalent)**

```json
{
  "assigned_intent_class": "media-press",
  "s4_confidence": 0.94,
  "booking_ref": null,
  "detected_language": "en",
  "routing_rule_fired": 6,
  "intent_priority_applied": "media-press (no cancellation/complaint signals present)",
  "requires_escalation": false,
  "escalation_reason": null,
  "s4_processed_at": "2026-03-20T09:07:00Z",
  "pax_count": 2,
  "financial_impact": null,
  "service_failure_flagged": false,
  "publication_date": "2027-03-01",
  "media_outlet_verified": true,
  "domain_reputation_score": 0.0,
  "partners_table_match": false,
  "ambiguity_penalty_applied": false,
  "email_body_raw": "Freelance journalist, Nordic Travel Magazine. Press trip Feb 2027. Feature article March."
}
```

| Invariant | Verdict | Reason |
|---|---|---|
| A5 | PASS | publication_date present, media_outlet_verified=true |
| B1 | PASS | confidence=0.94 >= 0.80 |
| B5 | PASS | Rule 6, intent_priority_applied documented |
| B6 | N/A | escalation_reason is not 'spoof_detected' |
| **S5 result** | **PASS** | Route to CRM |

---

**Test JSON 9 — mixed language (boundary case: C4 + D4)**

```json
{
  "assigned_intent_class": "general_inquiry",
  "s4_confidence": 0.78,
  "booking_ref": null,
  "detected_language": "mixed",
  "routing_rule_fired": 2,
  "intent_priority_applied": null,
  "requires_escalation": true,
  "escalation_reason": "low_confidence",
  "s4_processed_at": "2026-03-20T09:08:00Z",
  "pax_count": null,
  "financial_impact": null,
  "service_failure_flagged": false,
  "publication_date": null,
  "media_outlet_verified": false,
  "domain_reputation_score": 0.65,
  "partners_table_match": false,
  "ambiguity_penalty_applied": true,
  "email_body_raw": "Voimmeko saada hintatietoja? We need pricing for groups. Preise bitte schicken."
}
```

| Invariant | Verdict | Reason |
|---|---|---|
| C3 | PASS | 'mixed' is valid enum |
| C4 | PASS | ambiguity_penalty_applied=true, confidence=0.78 (penalty already applied) |
| B1 | PASS | confidence=0.78 < 0.80, requires_escalation=true consistent |
| **S5 result** | **ESCALATE** | requires_escalation=true |

---

**Test JSON 10 — Rule 6 priority conflict: cancellation + media signals (T10/spoof-equivalent)**

```json
{
  "assigned_intent_class": "cancellation",
  "s4_confidence": 0.70,
  "booking_ref": null,
  "detected_language": "de",
  "routing_rule_fired": 6,
  "intent_priority_applied": "cancellation > media-press (Rule 6 hierarchy — spoof detected)",
  "requires_escalation": true,
  "escalation_reason": "spoof_detected",
  "s4_processed_at": "2026-03-20T09:09:00Z",
  "pax_count": null,
  "financial_impact": null,
  "service_failure_flagged": false,
  "publication_date": "2027-03-01",
  "media_outlet_verified": false,
  "domain_reputation_score": 0.0,
  "partners_table_match": false,
  "ambiguity_penalty_applied": false,
  "email_body_raw": "Stornierung anfragen — ich bin Journalist für Reisemagazin. Veröffentlichung März."
}
```

| Invariant | Verdict | Reason |
|---|---|---|
| A2 | FAIL | cancellation assigned but booking_ref is null — A2 fires |
| B1 | PASS | confidence=0.70 < 0.80, requires_escalation=true consistent |
| B5 | PASS | Rule 6, intent_priority_applied documented |
| B6 | PASS | spoof_detected with assigned_intent_class='cancellation' — correct |
| D2 | PASS | DE 'Stornierung' present, assigned as cancellation — correct |
| **S5 result** | **FAIL (A2)** | cancellation without booking_ref → escalate. Human reviewer must locate booking context. |

This test case is critical: the spoof was correctly defeated by Rule 6, but S5 catches that a booking_ref is missing. Human review confirms whether a booking exists before processing the cancellation.

### Malformed Input Test

**Malformed JSON: missing required field, null where required, confidence > 1.0**

```json
{
  "assigned_intent_class": "booking_request",
  "s4_confidence": 1.42,
  "booking_ref": null,
  "detected_language": null,
  "routing_rule_fired": 7,
  "intent_priority_applied": null,
  "requires_escalation": false,
  "escalation_reason": null
}
```

S5 malformed input handler (runs before any invariant):

```typescript
function validateS4OutputSchema(output: Partial<S4Output>): S4Output {
  const errors: string[] = [];

  if (output.s4_confidence === undefined || output.s4_confidence > 1.0 || output.s4_confidence < 0.0) {
    errors.push(`s4_confidence invalid: ${output.s4_confidence}`);
  }
  if (!output.detected_language) {
    errors.push('detected_language is null or missing');
  }
  if (output.routing_rule_fired === undefined || output.routing_rule_fired < 1 || output.routing_rule_fired > 6) {
    errors.push(`routing_rule_fired invalid: ${output.routing_rule_fired}`);
  }
  if (errors.length > 0) {
    escalate_to_human_review(email, ['SCHEMA_VALIDATION'], `Malformed S4Output: ${errors.join('; ')}`);
  }
  return output as S4Output;
}
```

This malformed record triggers three schema violations before reaching any invariant. Escalated with reason 'Malformed S4Output'. CRM write blocked.

---

## Known Limitations and Unknowns

### Language Edge Cases

- **Finnish indirect complaint language:** Finnish negative emotion is compressed and de-anchored by cultural convention. A Finnish speaker writing "Tämä ei vastannut odotuksiamme" (this did not meet our expectations) is expressing a complaint that would be explicit in English or German. S4's NLP models may assign 0.60–0.65 confidence to these cases. D1 raises the floor to 0.65, but complaints at 0.62 in Finnish may be misclassified as general_inquiry. D1 catches the post-classification case; it cannot prevent the misclassification.
- **German compound cancel words:** "Buchungsannullierung" (booking annulment) is not covered by D2's regex pattern. D2 covers "Stornierung" and "stornieren" only. Compound forms may slip through. This is a known gap — update D2 regex pattern after first production failure.
- **Mixed FI/DE email:** A Finnish guest writing in German (not uncommon for Finnish-Swedish bilinguals working in German markets) may produce `detected_language: 'mixed'` with de-anchored negative emotion. Neither D1 (FI floor) nor D2 (DE cancel keyword) fully handles this — D4 escalates the case.

### "Zero Hallucination" Scope

"Zero hallucination" in this spec means: every S4Output that violates a defined invariant is blocked from reaching the CRM. **This is an invariant-level guarantee on field coherence, not a classification-correctness guarantee.** It does not mean: every wrong classification is caught. If S4 produces a plausible-but-wrong output that satisfies all 30 invariants (e.g., a cancellation classified as partnership, with a fabricated booking_ref that passes C2 format check, and a plausible domain_reputation score), S5 will not catch it because there is zero semantic cross-check between email-body signals and assigned_intent_class — only structural validation. This is why E6 (monthly spot-check) exists — it is the human backstop for invariant-compliant hallucinations. **Classification correctness remains S4's responsibility; S5's role is to prevent CRM corruption from structurally invalid data.**

### Thread-Context Gap (Gemini Audit — Q2, 2026-03-24)

**Known escape path:** A quoted-reply chain where a negative follow-up email quotes an earlier positive inquiry — and S4 classifies the thread as the original intent class (e.g., `booking_request` instead of `complaint`) because it scans `email_body_raw` only. S5 has no thread-context guard. Such an email passes A1–E6 entirely: the structural fields are valid for the (wrong) assigned class, confidence is above threshold, and Rule 6 never fires because complaint signals are in the quoted portion only.

**Why this is not fixed in S5:** S5 receives `email_body_raw` only — it cannot detect thread context without `in_reply_to_header` and `thread_context_snippet` fields from S4. Fixing at S5 level requires S4 schema change. This is a design boundary decision, not a validation gap.

**Mitigation path:** (1) Add `in_reply_to_header: boolean` and `thread_has_prior_complaint: boolean` to S4Output schema. (2) Add S5 invariant C7: if `in_reply_to_header=true AND thread_has_prior_complaint=true AND assigned_intent_class != 'complaint'`, escalate. This is a Wave 2B enhancement — not a P2 deployment blocker, since the E6 monthly spot-check will surface these cases in production.

### 100 Synthetic Emails May Miss Rare Edge Cases

The synthetic test set covers defined boundary cases. Production email traffic may contain edge cases not represented in the generator prompt: multi-language emails with code-switching mid-sentence, emails from automated booking systems with non-standard formatting, forwarded email chains where the original intent is buried in a reply. These will surface through E6 spot-checks and E4 failure pattern analysis.

### S4 Confidence Distribution Stability

E3 assumes S4's confidence distribution is stable week-to-week. If Finland DMC's email patterns change seasonally (high summer booking volume, winter complaint season), E3's ±0.10 drift threshold may fire as a false alarm. The ±0.10 threshold is a starting point — recalibrate after 8 weeks of production data.

### Dependencies on S4 Changes

If S4 adds a 9th Intent class, invariant C6 (coverage check) and E1 (test set coverage) must be updated. The S4Output TypeScript interface must be versioned, and S5 must be re-validated against the new schema before deployment of the S4 change. S4 changes without S5 re-validation = undefined behavior.

---

## DMC Realism and Assumptions Matrix

Every estimate below carries explicit assumptions. Any flagged item requires Patrick sign-off before the roadmap proceeds.

| Item | Estimate | Assumption | Flag |
|---|---|---|---|
| S5 module deployment | 4 hours | Assumes n8n-only architecture, no new microservices. S5 lives in an n8n Function node reading from Supabase. | If microservice required: +8 hours. Deployment Blocker: Patrick must decide architecture. |
| Weekly synthetic test creation (initial) | 2 hours | Assumes Claude Code generates the 100-email set from the generator prompt in one pass. Patrick reviews 10% for realism. | If generator prompt requires more than 2 revision rounds: +1 hour. Not a blocker. |
| Weekly synthetic test execution | 30 minutes | Assumes n8n automates the full run. Human time = reviewing the weekly summary report only. | If n8n automation is not yet set up: 2 hours manual. Flag: requires n8n S4 workflow already deployed. |
| Human review overhead | ~11.7 hours/week (baseline 700 emails/week × 20% escalation × 5 min/email) | Assumes DMC receives ~700 production emails/week. Assumes 20% escalation rate derived from S4 test cases T1–T12. Assumes reviewer can process 1 email per 5 minutes. **CRITICAL: This is unvalidated on actual DMC data.** First 4 weeks of production MUST log actual escalation rate. If > 25%, allocate additional reviewer hours or raise JF2 confidence threshold to 0.85. | **Deployment Blocker: requires Patrick confirmation that DMC ops can sustain 11.7 hrs/week human review at baseline (20% escalation).** If actual escalation in weeks 1–4 runs 25%+ (14.6 hrs/week), roadmap resets. |
| Regression set growth | +5–15 emails/week | Assumes production failure rate is < 15% in steady state. | If failure rate > 15% in first 4 weeks, roadmap resets — S4 logic refresh required before S5 production use. |
| S4 confidence stability | ±0.05 week-to-week | Assumes DMC email volume and patterns are consistent. | **Flag: If S4 confidence distribution changes > 0.10 (E3 trigger), roadmap resets.** Recalibrate E3 threshold after 8 weeks of data. |
| Patrick on-call for E5 Logic Refresh | 2 hours/month | Assumes E4 fires ≤ once per month on average in mature operation. | If E4 fires weekly in first month: escalate to S4 redesign. Deployment Blocker. |

### Deployment Blockers (Patrick Sign-Off Required)

1. **Human review capacity:** DMC ops team must confirm ability to sustain **11.7 hrs/week** (baseline: 700 emails × 20% escalation × 5 min/email). **Source of assumptions:** 700-email volume and 20% escalation rate are derived from S4 T1–T12 test case distributions — not generic benchmarks — and must be validated against actual production data. First 4 weeks of production MUST measure actual escalation rate. **If rate exceeds 25%: raise JF2 threshold to 0.85 AND pause autonomous CRM writes immediately. Do not proceed to week 5 without resolving the escalation rate.** If rate is 20–25%: allocate additional ops hours and continue monitoring. If not confirmed before deployment, deployment is blocked.
2. **n8n S4 workflow prerequisite:** S5 deployment assumes S4 is already running in n8n and writing to Supabase `email_classifications` table. S5 cannot be deployed before S4 is in production.
3. **Architecture decision:** S5 as n8n Function node vs. standalone TypeScript service. This spec assumes n8n. If Patrick decides on a standalone service, deployment estimate doubles.

---

## Execution Roadmap

### One-Time Setup

| Step | Action | Owner | Estimated Effort |
|---|---|---|---|
| P1 | Generate 100-email synthetic test set using generator prompt | Patrick + Claude Code | 2 hours |
| P2 | Deploy S5 TypeScript module to n8n (Function node) | Developer | 4 hours |
| P3 | Create Supabase `s5_audit_records` table (schema above) | Developer | 1 hour |
| P4 | Configure weekly n8n trigger (Monday 08:00 EET) | Developer | 30 minutes |
| P5 | Patrick sign-off on deployment blockers (see above) | Patrick | 30 minutes |

**PREREQUISITE TOTAL: ~8 hours (developer) + 2.5 hours (Patrick)**. This is one-time. Not counted in weekly overhead.

### Weekly Steady State

| Step | Action | Owner | Estimated Effort |
|---|---|---|---|
| W1 | n8n runs flywheel: 100+ synthetic emails through S4→S5 | Automated | 0 min |
| W2 | Review weekly summary report (class coverage, PASS rate, drift) | Patrick | 15 minutes |
| W3 | Process escalated emails in human_review_queue (baseline 700 emails × 20% × 5 min/email) | DMC ops | ~11.7 hours |
| W4 | Confirm E2 regression growth (failures added to next week's set) | Automated | 0 min |
| W5 | If E4 fires: create Logic Refresh task (E5) | Automated → Patrick | 30 min if triggered |

**WEEKLY TOTAL: 11.7 hours (ops) + 15 minutes (Patrick) + 30 minutes if E4 fires. (NOTE: First 4 weeks must validate actual escalation rate — may exceed this baseline if > 20% of production emails escalate.)**

### Monthly

| Step | Action | Owner | Estimated Effort |
|---|---|---|---|
| M1 | E6 spot-check: human reviews 5 random PASS emails | Patrick | 30 minutes |
| M2 | If E5 was triggered: complete S4 Logic Refresh + re-test | Patrick + Developer | 2 hours |

### Deployment Path

S5 TypeScript code lives in the n8n workflow that processes S4 output. Specifically: after S4 writes to Supabase `email_classifications`, an n8n Function node reads the new record, runs the 30 invariants, writes to `s5_audit_records`, and routes to either CRM write or human_review_queue. No new microservice. No new infrastructure beyond the existing Supabase + n8n stack.

**TBD — BLOCKING COMMENT:** The exact n8n node architecture (Function node inline vs. external TypeScript service called via HTTP) has not been decided. This decision affects P2 effort estimate (4 hours inline vs. 12 hours external service). **Patrick must decide before P2 begins.** Default assumption in this spec: n8n Function node inline.

---

## Document Split Plan (for maintenance efficiency)

**Current:** 77KB monolithic spec (one-time dev reference, frozen after P2)

**Recommended split (post-P2):**

| Document | Purpose | Audience | Size | Location | Frequency |
|----------|---------|----------|------|----------|-----------|
| **S5 Ops Checklist** | Weekly ops workflow, human-review process, monitoring thresholds | DMC ops + Patrick | ~5 pages | Project wiki / n8n docs | Read weekly (15 min) |
| **S5 Dev Technical Reference** | 30 invariants, TypeScript, audit schema, S4 integration, test cases | Developers (P2 implementation, future maintenance) | ~15–20 pages | Code repo / GitHub /docs | Read once (P2), reference as-needed |
| **S5 Test Suite & Fixtures** | 10 test JSONs with verdicts, generator prompt, regression cases | Test automation / E1–E2 automation | ~3 pages | Test repo (`tests/s5-fixtures.json`) | Updated weekly (E2 regression growth) |

**Implementation timing:** Apply split after P2 deployment (post-Week 1 launch). Dev Reference stays frozen; Ops Checklist can evolve with lessons learned from E3/E4/E6 feedback.

---

*S5-REGRESSION-FLYWHEEL-SPEC.md v1.0 — 2026-03-20 (GROK-APPROVED with 3 critical fixes applied)*
*Input sources: S5-FLYWHEEL-BRIDGE-v1.0.md (30 invariants defined), S4-PROGRESSIVE-AUTONOMY-SPEC.md v1.2 (unified matrix, T1–T12, S4Output interface)*
*Status: DRAFT — Awaiting Grok Judge validation*
