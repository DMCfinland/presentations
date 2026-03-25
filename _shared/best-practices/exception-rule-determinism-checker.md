---
name: Exception Rule Determinism Checker
description: How to write exception rules that are deterministic (IF/AND/THEN) not judgment-based
type: feedback
source: session 104 S3 Anti-Anchoring (C2 acceptance criterion improvement)
---

# Exception Rule Determinism Checker

## Rule

When a spec requires an "exception rule" — a condition under which normal behavior is overridden — the rule MUST be **deterministic**: testable by a machine or junior developer without requiring judgment.

**Deterministic:** IF [pattern matches X] AND [context condition Y] THEN [action Z]

**Non-deterministic:** "Evaluate whether the authority adds information" / "Use judgment to determine if this is a real signal"

## Why

Judgment-based rules hide ambiguity. They produce inconsistent outputs (different people apply them differently), silent failures (someone applies it wrong, nobody catches it), and maintenance debt (next person tries to guess what "judgment" means).

Deterministic rules are:
- Testable (can write a unit test)
- Consistent (same input → same output always)
- Auditable (can explain why a decision was made)
- Machine-checkable (regex, lookup table, or boolean logic)

## The Pattern — 5 Anti-Patterns vs 5 Deterministic Replacements

### Anti-Pattern 1 — Vague authority evaluation

**❌ Non-deterministic:**
```
Exception Rule: "Preserve authority markers when they add information to the classification"
```

Why this fails: "Adds information" is subjective. When does "toimitusjohtaja" (CEO) add classification signal? When does it add bias? Developer has to guess.

**✅ Deterministic:**
```
Exception Rule:
  IF [pattern matches media role: Päätoimittaja | Editor | Toimittaja | Journaliste]
  AND [email class == media-press]
  THEN preserve role marker AND set exception_triggered=true
  ELSE strip the marker AND set exception_triggered=false
```

Now it's testable: "Does this email's sender title match the media role list? If yes AND the classification output includes media-press, preserve it."

---

### Anti-Pattern 2 — Context-dependent judgment

**❌ Non-deterministic:**
```
Exception Rule: "Keep tone markers if they're part of normal business communication style"
```

Why this fails: What counts as "normal"? For Finnish emails, exclamation marks are rarer than in German. Who decides what's normal?

**✅ Deterministic:**
```
Exception Rule:
  IF [email class == existing-partner]
  AND [sender domain matches known-partner-list]
  THEN apply debiasing but preserve 1 exclamation mark (do not strip all of them)
  ELSE strip all exclamation marks
```

Now: look up the sender domain against a list. If found, apply a specific rule. No judgment.

---

### Anti-Pattern 3 — "Evaluate relevance" clauses

**❌ Non-deterministic:**
```
Exception Rule: "Keep organization names that are relevant to the request"
```

Why this fails: Is "Germany Logistics GmbH" relevant when they mention "our subsidiary in Munich"? The rule doesn't say.

**✅ Deterministic:**
```
Exception Rule:
  IF [organization name appears in email body (not just From line)]
  AND [sentence structure is "[Company] does X" or "[Company]'s Y"]
  THEN preserve that company mention (do not strip from body)
  ELSE strip all company names from From/Von line only
```

Scope is now explicit: Only strip From lines. Body mentions are preserved. Test case: "our subsidiary GmbH" in body → preserved. "Klaus Weber, GmbH" in From → stripped.

---

### Anti-Pattern 4 — Open-ended "use judgment"

**❌ Non-deterministic:**
```
Exception Rule: "Use your judgment to decide if a title should be preserved based on context"
```

Why this fails: This isn't a rule; it's a delegation of work to the evaluator. Next person will apply it differently.

**✅ Deterministic:**
```
Exception Rule:
  IF [title is in Class A media roles: {Päätoimittaja, Editor, Viranomainen, ...}]
  THEN preserve AND set exception_triggered=true
  ELSE IF [title is in Class B authority roles: {toimitusjohtaja, hallitus, ...}]
  THEN strip AND set exception_triggered=false
  ELSE IF [title is unknown]
  THEN log as ambiguous AND route to human
```

Three clear paths: Class A (preserve), Class B (strip), Unknown (escalate). No judgment needed.

---

### Anti-Pattern 5 — Fuzzy thresholds

**❌ Non-deterministic:**
```
Exception Rule: "Remove most urgency markers, but keep those that seem important"
```

Why this fails: "Seem important" is observer-dependent. What's important to a CEO might seem trivial to a developer.

**✅ Deterministic:**
```
Exception Rule:
  Urgency markers are stripped by default.
  Exception: IF email contains regulatory language (e.g., "legal obligation", "compliance requirement")
  THEN preserve the urgency phrase in context (e.g., "urgent compliance requirement")
  AND set exception_triggered=true

  Test: "Urgent — legal obligation to report" → preserve "urgent ... legal obligation"
        "Urgent — need reply today" → strip both
```

Clear threshold: regulatory context triggers preservation. Otherwise, always strip.

---

## The Determinism Checklist

Before finalizing an exception rule, ask:

- [ ] **Can I write it as IF/AND/THEN?** If not, it's judgment-based.
- [ ] **Can a junior dev apply it consistently?** No ambiguity about what counts as matching the condition.
- [ ] **Can I test it with examples?** Write 3 test cases: one should MATCH, one should NOT match, one EDGE CASE.
- [ ] **Does it reference a list or range?** (e.g., "roles in this list", "sentences matching pattern X") Or does it say "evaluate"?
- [ ] **Is there an escalation path for unknowns?** What if the email doesn't match any rule clearly? Route to human, don't guess.

If you can't check all 5 boxes, the rule is not deterministic yet. Rewrite it.

---

## Template for Deterministic Exception Rules

```markdown
### Exception Rules (Deterministic Format)

**Class A — Authority-as-Content (PRESERVE)**
IF [pattern matches media role: Päätoimittaja, Editor, Viranomainen, Journalist, Toimittaja, Behörde, Redakteur]
AND [email classification = media-press OR regulatory]
THEN preserve role marker (don't strip)
AND set exception_triggered = true
Test cases:
  - "From: Minna Saarinen, Päätoimittaja, Matkailulehti" → PRESERVE (media-press class)
  - "From: Klaus Weber, Geschäftsführer, Bayern GmbH" → STRIP (no media/regulatory signal)

**Class B — Standard Authority (STRIP)**
IF [pattern matches business role: toimitusjohtaja, hallitus, Vorstand, Managing Director]
AND [no media/regulatory context]
THEN strip the role marker
AND set exception_triggered = false

**Class C — Unknown Title**
IF [title found in email]
AND [title NOT in Class A or Class B list]
THEN log as ambiguous for human review
AND set exception_triggered = null (escalate)
```

---

## Session 104 Example

**How S3 Anti-Anchoring Spec used this rule:**

```markdown
### Exception Rules (When NOT to Strip)

Pattern Class A — Media/Editorial Authority (PRESERVE)
IF [title matches: Päätoimittaja, Editor, Viranomainen, Journalist, Toimittaja, Behörde, Chefredakteur]
AND [email class = media-press OR regulatory]
THEN preserve role marker AND set exception_triggered = true
ELSE strip AND set exception_triggered = false

Example test case (Pair 5 from Interface Spec):
  Raw: "From: Minna Saarinen, Päätoimittaja, Matkailulehti"
  Rule check: title = "Päätoimittaja" (matches Class A) AND email content = media inquiry → PRESERVE
  Expected: de_anchored=true, exception_triggered=TRUE
  Actual output: "From: [ROLE: Päätoimittaja], [MEDIA]\nKirjoitan artikkelia..."
  ✓ PASS
```

The rule is deterministic: IF title is in the list AND class is media/regulatory, preserve it. Testable with specific examples.

---

## Source

Session 104, S3 Anti-Anchoring System, Acceptance Criterion #2. Bridge specified "deterministic exception rule" but did not provide anti-patterns or a checker. Worker produced high-quality deterministic rules by pattern (IF/AND/THEN), but future specs should include this template upfront to prevent "judgment-based rule" failures.

Confidence: HIGH (design pattern validated across 3 similar specs).
