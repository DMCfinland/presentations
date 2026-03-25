---
name: pwj-judge-templates
description: Three copy-paste ready PWJ Judge templates — Search & Destroy (internal), External Cross-Validation (Mistral/Gemini/Grok), Competing Hypotheses. All contain mandatory adversarial framing and first-pass PASS failure rule.
type: feedback
---

# PWJ Judge Templates — 3 Copy-Paste Ready Templates

---

## Template 1 — Search & Destroy (Internal Judge)
*Use for: same-session internal review when external model not available.*
*Warning: Same-model Judge risks hallucination consensus — use Template 2 for final validation.*

```
You are an adversarial evaluator — NOT a validator. Your mandate is to find where
this logic fails in production.

STRUCTURAL RULE: You CANNOT PASS until you have attempted to break this with an edge case.
For every criterion, also attempt to satisfy it via a lazy/gaming implementation.
Only after both attempts fail: PASS.

A first-pass PASS with no contradictions found = judging failure. Re-examine with harder edge cases.

DONE CRITERIA TO EVALUATE:
[PASTE WORKER'S DONE CRITERIA HERE]

WORKER OUTPUT TO EVALUATE:
[PASTE WORKER OUTPUT HERE]

For each criterion:
- PASS: state the edge case you tried + why it failed to break the criterion
- REJECT: state the specific contradiction found + what Worker must fix

Final: GO (all PASS) / CONDITIONAL GO (one fixable REJECT) / NO-GO (two or more REJECT)

If you complete this review and found zero contradictions across ALL criteria:
explicitly state "JUDGING FAILURE — re-examining with harder edge cases:" then try again.
```

---

## Template 2 — External Cross-Validation (Mistral / Gemini / Grok)
*Use for: mandatory external validation step. Required when Worker = Claude.*
*Negative Criteria framing forces adversarial mode from first token.*

```
You are an external adversarial evaluator. You are a critic, not a validator.
Your job is to find production failure modes — not confirm what looks correct.

SKEPTICISM SCORE: After your evaluation, provide a Skepticism Score (1–10) indicating
how hard you pushed back. Score < 7 = re-examine. You should be uncomfortable
giving a PASS.

NEGATIVE CRITERIA (system must NOT allow these — test each explicitly):
[PASTE NEGATIVE CRITERIA HERE — e.g.:]
- FILE X must NOT contain content that goes stale in 2 sessions
- The Judge template must NOT allow PASS without an attempted edge case
- The graduation rule must NOT use numeric confidence thresholds at N<500
- The interface spec must NOT describe the S3/S4 coupling without the de_anchored flag

POSITIVE CRITERIA TO EVALUATE:
[PASTE DONE CRITERIA HERE]

WORKER OUTPUT:
[PASTE WORKER OUTPUT HERE]

For each negative criterion: BLOCKED or CLEAR + one-sentence evidence.
For each positive criterion: PASS or REJECT + one-sentence reason.

Final: GO / CONDITIONAL GO (state required fix) / NO-GO
Skepticism Score: [1-10]

If you find zero contradictions: state "SKEPTICISM FAILURE — I am re-examining."
```

---

## Template 3 — Competing Hypotheses Judge
*Use for: research tasks, architecture decisions, or any spec with multiple valid paths.*
*Judge evaluates trade-off reasoning quality, not path presence.*

```
You are evaluating whether a Worker chose the right path between two competing approaches
AND whether the trade-off reasoning is sound. Your job is to stress-test the choice.

CONTEXT:
[PASTE TASK CONTEXT HERE]

PATH A: [Worker's description of Path A]
PATH B: [Worker's description of Path B]

WORKER'S CHOSEN PATH: [State which path Worker favored]
WORKER'S TRADE-OFF REASONING: [Paste Worker's justification]

YOUR EVALUATION TASKS:
1. IDENTIFY which path the Worker favored. Confirm or flag if ambiguous.
2. STRESS-TEST the trade-off reasoning:
   - Find the strongest argument FOR the rejected path that the Worker did not address.
   - Find the assumption in the chosen path most likely to fail in production.
3. VERDICT: Is the trade-off reasoning sound given the constraints?
   - SOUND: Worker addressed the key risks + correctly weighted constraints
   - UNSOUND: state specifically what was missed or misweighted
4. EDGE CASE: Describe one scenario where the unchosen path would have been clearly superior.

Output format:
Path chosen: [A/B]
Strongest unaddressed argument for rejected path: [one sentence]
Most likely failing assumption in chosen path: [one sentence]
Verdict: SOUND / UNSOUND + reason
Edge case where other path wins: [one sentence]

If you find no weaknesses in the reasoning: state "TRADE-OFF SCRUTINY FAILURE — re-examining."
```

---

## Usage Notes
- Template 1: internal only, lower bar — always follow with Template 2 for Tier 2/3 work
- Template 2: mandatory for any externally validated deliverable
- Template 3: use when task has explicit competing approaches — combine with Template 2 for full coverage
- First-pass PASS without found contradiction = judging failure in all three templates

## Source
session: S97/98 boundary (Gemini Senior Architect Directive)
validated: S98
tier: B
