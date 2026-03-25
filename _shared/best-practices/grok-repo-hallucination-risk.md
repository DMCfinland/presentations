---
name: grok-repo-hallucination-risk
description: Grok invents GitHub repo names and star counts. Always verify before citing or building on them.
type: feedback
---

Grok invented 3 of 5 GitHub repos in a governance-as-code research session:
- microsoft/agent-governance-toolkit → DOES NOT EXIST
- eqtylab/cupcake → DOES NOT EXIST
- deeplearning-ai/sc-agent-governance → DOES NOT EXIST

Real repos in same query: open-policy-agent/opa (✅), vorionsys/vorion (✅)

**Why:** Grok generates plausible-sounding repo names when it doesn't have confirmed results. They look real (org/name format, star counts included) but are hallucinated.

**How to apply:** After any Grok response listing GitHub repos — verify via Gemini web search or direct GitHub check BEFORE mining, building prompts around, or citing. Never build a mining session around Grok-sourced repo names without verification step first.

source: session-100, source: patrick (caught in live session)
