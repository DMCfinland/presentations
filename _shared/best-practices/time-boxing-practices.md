---
name: time-boxing-practices
description: Rules for time-boxing workflow steps — separating one-time setup from per-session steps, and accurately calculating per-session overhead for integration specs.
type: feedback
source: session-102 + Gemini/Grok peer review
---

# Time-Boxing Practices

## Rule 1 — Separate PREREQUISITE from per-session steps (source: S102 C6 fix)

When writing an integration spec with a time constraint (e.g., "total ≤5 minutes"):

**Always separate one-time setup costs from per-session costs.**

Use a `PREREQUISITE (one-time setup)` block BEFORE the numbered steps. This block is not counted in the per-session total.

Example: Locale setup (`export LANG=fi_FI.UTF-8 >> ~/.zshrc`) is one-time, not per session. Including it in the per-session step inflated S3 integration time from 4:00 to 5:30 — a false criterion failure.

**Why:** One-time setup costs are amortized across all sessions. Counting them per-session double-penalizes the spec and obscures the real recurring cost. Saves ~1.5 min/session in reported overhead.

**How to apply:** When a step has "maximum time: X if Y required," check whether Y is a one-time condition. If yes, move it to PREREQUISITE. The per-session step then shows only the steady-state cost.

## Rule 2 — Use maximum estimates for variable-time steps

When a step has variable time (e.g., "30 seconds to 2 minutes"), always use the maximum for total calculation. Do not use averages or typical-case times.

**Exception:** If the variance is caused by a one-time condition (see Rule 1), apply Rule 1 first — then the step has a fixed steady-state time.

## Rule 3 — Flag threshold violations explicitly (criteria gaming prevention)

If an honest maximum-estimate total exceeds the time constraint:
1. Do NOT reduce step times to game the constraint
2. Write the honest total AND the fix ("after one-time setup, total drops to X")
3. Flag it as CRITERIA GAMING RISK in the spec
4. The Judge resolves it by applying Rule 1 (move one-time cost to PREREQUISITE)

Source: S102 PWJ loop — S3 Anti-Anchoring Spec C6 fix. Confirmed by Gemini/Grok peer review.
