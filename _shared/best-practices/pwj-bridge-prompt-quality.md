---
name: pwj-bridge-prompt-quality
description: Anti-patterns + mandatory patterns for PWJ bridge prompt construction — Search & Destroy Judge, Integrated Eval Sets, Statistical Guardrails, Competing Hypotheses. Produced from Gemini Senior Architect Directive diagnosis (S97/98).
type: feedback
---

# PWJ Bridge Prompt Quality — Anti-Patterns + Mandatory Patterns

## Exact Phrase Rule (behavioral trigger — do not paraphrase)
All Judge prompts MUST contain this exact phrase:
> "You CANNOT PASS until you have attempted to break this with an edge case"

Paraphrase weakens the adversarial mandate. Exact wording is load-bearing.

## First-Pass PASS Rule (structural, not advisory)
If a Judge produces PASS on round 1 with zero contradictions found → **judging failure, not success.**
Structural enforcement — embed in every Judge prompt:
> "A first-pass PASS with no contradictions found = I failed my duty. Re-examine with harder edge cases."

## Anti-Patterns

| Anti-Pattern | Source Session | Specific Consequence |
|---|---|---|
| Context Inflation: DMC block copy-pasted into every bridge file | S3-bridge-v1 | N files need updating per company change; stale contexts persist silently |
| Checklist Theater: Judge validates section exists, not that it works | S3/S4 bridges | PASS on spec that fails at first production edge case |
| Future Testing: "humans will test this later" | S3/S4 analysis | Spec filed, never stress-tested → silent production failure |
| Parallel Isolation: S3 and S4 treated as independent sessions | S3/S4 design v1 | S3 regex changes S4 input distribution → S4 calibration runs on wrong data |
| Time-based triggers: "90 days" without N≥50 constraint | S4 initial design | 5 emails/month × 90 days = 45 examples → autonomy granted by calendar not evidence |

## Integrated Eval Sets (mandatory for Planner — NOT optional)
During the planning session — **not after** — Planner produces **10–20 cases per class minimum**
(80–160 total for an 8-class classifier). Worker MUST run spec logic against them and report
results BEFORE finalizing any file.
Done criterion must require: "Worker ran [N] synthetic cases per class. Pass/fail results shown."
"Testing is a future step" = spec is unfinished. "10–20 total" = ~1–2 per class = zero statistical power.

## Statistical Guardrails
- **Anti-pattern (flag and reject):** Time-based triggers only ("90 days", "3 months")
- **Correct pattern:** Signal-based — Clopper-Pearson / Bootstrap 95% CI, **N≥99 per subclass**,
  upper bound of zero-override error rate < 3%
- **Why N≥99:** At k=0 overrides, p_upper = 1 − 0.05^(1/n). For n=45: 6.44%. For n=50: 5.82%.
  Only at n≥99 does p_upper drop below 3.0%. (Verified: Grok Heavy, 2026-03-19)
- At N<99 per subclass, "upper bound <3%" is mathematically impossible at actual email volumes.
- Done criteria that use only time-based graduation → REJECT in Judge review.

## Competing Hypotheses (research/architecture tasks)
Bridge prompts for research tasks must require:
- Path A: [approach + trade-off logic]
- Path B: [approach + trade-off logic]

Judge evaluates: which path did Worker favor AND is the trade-off reasoning sound?
"Two paths exist" is NOT the pass bar. "Correct path chosen for documented reasons" is.

## Anti-Criteria-Gaming Warning (paste verbatim into every Worker spawn prompt)
> "Your goal is the best possible system, not passing the criteria. If you notice yourself
> writing to satisfy a criterion rather than solving the actual problem →
> CRITERIA GAMING RISK: [criterion N] → [X] but better is [Y]. Flag for human review."

## Production Failure Audit

| Failure Mode | Structural Mitigation |
|---|---|
| Checklist produced but never consulted: done criteria listed but Judge reviews presence only | Embed criteria directly into Judge prompt as the evaluation target — not as a preamble. Judge cannot skip what it's explicitly evaluating. |
| DMC-CORE-CONTEXT.md goes stale after company change (staff count, stack update, new label class) | File contains a "Last updated: [session N]" header. Any session that changes company profile must update this file. Session-end checklist item: "Did company profile change? If yes, update DMC-CORE-CONTEXT.md." |
| Search & Destroy Judge games criteria with compliant edge cases (writes edge cases that look hard but don't break anything) | Judge must explicitly state "JUDGING FAILURE — re-examining with harder edge cases:" if round 1 yields zero contradictions. This is structural in Template 1 — cannot output PASS without the re-examination step. |

## Source
session: S97/98 boundary (Gemini Senior Architect Directive, 3-session convergent diagnosis)
validated: S98 — three sessions independently diagnosed same root failure (presence vs production survival)
tier: B — promote to Tier A after 3 confirmed uses
