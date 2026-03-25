---
name: grok-post-pass-strategy-gate
description: Run a Grok strategic challenge AFTER PWJ technical PASS on any significant spec — technical quality ≠ correct strategic priority
type: feedback
---

After a PWJ technical PASS, the spec is proven internally consistent and criteria-complete. It is NOT proven strategically correct. These are different questions.

**Why:** S106 built S4-PROGRESSIVE-AUTONOMY-SPEC.md (PWJ PASS, Round 2, all 11 criteria). Grok's 4-agent council then challenged the strategic priority — finding that S4 may be founder distraction during peak revenue season, and that email baseline measurement was missing before any custom routing dev.

**Why it matters:** PWJ validates "does this output meet the criteria we set?" Grok strategic spar validates "were the criteria for the right thing?" Two different questions. A technically perfect spec for the wrong priority is wasted effort.

**How to apply:**
- After any PWJ PASS on a significant spec (not single-file edits): run /grok-spar in Cross-Validate mode
- Frame the question as open challenge: "Is this the right priority given constraints?"
- Do NOT pre-load the conclusion — Grok must reason independently
- Lucas's adversarial case is the highest-value output; extract specifically
- If Grok returns CONDITIONAL GO or stronger NO: surface to Patrick before implementation starts

**Threshold for when to run:**
- Dev effort ≥ 10 hours OR implementation will touch production → mandatory
- Spec affects revenue-critical workflow during peak season → mandatory
- Pure reference doc (no immediate implementation) → optional

Source: Patrick, S106. Grok council (Harper/Benjamin/Lucas) returned: "NOT the right strategic priority right now" for S4 during peak revenue season. Recommendation: measure 1-week email baseline first; start Mikko practices #1/#2/#5 instead.
