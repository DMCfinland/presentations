---
name: research-done-when-gold-stops
description: When to stop external AI validation rounds — stop when marginal value drops, not at a round limit
type: feedback
source: patrick, session 79, 2026-03-16
---

# Research Is Done When Gold Stops Coming

**Rule:** Continue external AI validation rounds (Grok, Gemini, research) until the marginal value of the next round is clearly lower than the last. Stop at a fixed round count only if rounds start repeating findings.

**Why:** Session 79 — ran 2 Grok rounds + 2 Gemini rounds + 1 background research agent on CRM security. Each round produced genuinely new findings (CVEs, attack vectors, new principles). Stopping after round 1 would have missed the BUILD-STATE.md poisoned intent attack, the Credential Isolation principle, and the CoSAI CodeGuard framework. Stopping after round 2 missed the n8n supply chain npm vector and the Multi-Message Assembly Guard. Gold kept coming until round 4-5.

**How to apply:**
- After each Grok/Gemini round: count NEW findings vs. restatements of prior findings
- If >2 new actionable findings: run another round
- If ≤1 new finding or findings are restatements: stop
- Apply to: security validation, architecture validation, strategy sparring, any multi-round external AI research
- Exception: if cost cap is reached, stop regardless

**Corollary:** When Grok or Gemini starts repeating principles or findings from prior rounds in different wording — that is the signal to stop.
