---
name: Verify AI Competitive Claims with Web Research
description: When Gemini/Grok says "competitor X is already in market Y" — always web-verify before accepting. AI models confabulate competitive threats that don't exist.
type: feedback
tier: B
source: patrick, S238
confirmed: 1
---

## Rule

When an external AI model claims a competitor is "already in" a niche market — treat it as a hypothesis, not a fact. Launch a web research subagent to verify before updating strategy.

**Why:** S238 — Gemini named Kontiki Reisen (Switzerland) and Voigt Travel (Netherlands) as DACH operators "already in the Saimaa market." This was used to attack the first-mover narrative: "The destination isn't undiscovered, respected Swiss competitors are already there." Patrick pushed back. Web research found:
- Kontiki Reisen sells a Finland *land tour* with day-boat segments (tied to dock overnight, not a sailing cruise)
- Voigt Travel sells Fly & Drive + 1-3 hour seal tours
- No DACH/Benelux operator currently sells a multi-night onboard sleeping Saimaa cruise

The multi-night cruise segment is genuinely unoccupied. Acting on Gemini's confabulated threat would have caused a wrong strategic pivot.

**How to apply:**
- Trigger: any time Grok/Gemini names a specific competitor in a niche market
- Action: launch web research subagent → verify what that operator *specifically* sells in that segment
- Key question: "Is what they sell actually comparable to what we build?" Day-boat ≠ 7-night cruise
- Accept the competitive threat only if the research confirms a comparable product exists

**Anti-pattern:** "Gemini says competitor X is there, so we can't claim first-mover." This is theater without verification. Gemini does not have real-time catalogue data.

**Template verification subagent prompt:**
```
Verify: does [OPERATOR] sell [SPECIFIC PRODUCT TYPE] in [MARKET]?
Is what they sell comparable to [OUR PRODUCT DESCRIPTION]?
Search: "[OPERATOR] [DESTINATION]" + their website product pages.
Report: what specific product they sell, price, and whether it is comparable.
```
