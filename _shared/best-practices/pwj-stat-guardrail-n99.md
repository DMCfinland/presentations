---
name: pwj-stat-guardrail-n99
description: Clopper-Pearson math for zero-override graduation trigger. N≥50 is wrong at DMC email volumes — N≥99 required for upper CI <3%. Source: Grok Heavy cross-validation, session 99.
type: feedback
source: grok-heavy-session-99
---

# PWJ Statistical Guardrail — N≥99 Correction

## Rule
For a zero-override graduation trigger, the correct N floor is **N≥99 per subclass**,
not N≥50.

## The Math (Clopper-Pearson, k=0 overrides)
```
p_upper = 1 - α^(1/n)   (exact upper bound when zero overrides observed)

α = 0.05 (95% CI):
  n=45: p_upper = 6.44%  ← actual volume at 5 emails/month × 90 days
  n=50: p_upper = 5.82%
  n=99: p_upper = 2.98%  ← first n where upper bound drops below 3%
  n=100: p_upper = 2.95%

Rule-of-three approximation (fast check): p_upper ≈ 3/n
  For p_upper < 3%: n ≥ 100
```

## Why This Matters at DMC Volume
- DMC email volume: 200–500/month total across 8 subclasses
- Rare subclass (e.g., media-press): ~5–10 emails/month
- 90-day window at 5/month = 45 examples → 6.44% upper CI
- "Upper bound of error rate < 3%" is mathematically impossible at this volume

## Implication for Session Bridge 4 (Progressive Autonomy)
The S4 spec's "N≥50 + <3% upper bound" pairing is contradictory.
Fix options:
1. Change N floor to N≥99 (requires ~20 months for rare subclasses at 5/month)
2. Change CI target to <7% (honest at N=45) — but then autonomy is on weaker evidence
3. Accept that rare subclasses may never graduate within 12 months and say so explicitly

## When to Apply
- Any spec with a statistical graduation trigger using zero-override logic
- Any "N samples + CI threshold" done criterion
- Before approving any Tier 2/3 autonomy expansion framework

## Source
Verified by: Grok Heavy Benjamin agent, session 99 (2026-03-19)
Formula: Clopper-Pearson exact method, k=0 special case
Cross-check: Rule-of-three (3/n) gives same conclusion
