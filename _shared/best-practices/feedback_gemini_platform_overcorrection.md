---
name: feedback_gemini_platform_overcorrection
description: Gemini applies generic LLM failure modes to platform-specific architectures. Always cross-validate with Grok when Gemini critiques architectural fragility.
type: feedback
---

When Gemini critiques an architecture as "fragile" or "breaking under load," verify whether the critique is platform-specific or generic LLM assumption.

**Why:** In S111 CoS review, Gemini predicted claude.ai Projects would suffer recency bias overriding Project Files within 48h. Grok Heavy + Benjamin's logic map showed this was a generic LLM assumption incorrectly applied to claude.ai Projects, which explicitly injects Custom Instructions + Knowledge Files as persistent context at session start.

**How to apply:** Any time Gemini says "[X] will break because of [general LLM behavior]" — run a Grok cross-validation prompt with explicit tool activation asking Harper to find platform-specific documentation before applying the fix. Especially for: recency bias, context window drift, layer priority conflicts.

**The correction that must NOT be made:** Gemini recommended removing the manual "Commit" gate from memory protocol (Change A). Grok [Lucas] correctly identified this as introducing a worse failure mode: passive listing allows unverified AI state to pollute the stable knowledge layer. The manual gate is the GDPR firewall, not friction.

source: patrick-session-111 | tier: B | validated: Grok Heavy MAD 2-round
