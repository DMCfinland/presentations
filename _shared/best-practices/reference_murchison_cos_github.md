---
name: reference_murchison_cos_github
description: Mike Murchison (CEO, Ada) published his full Claude CoS system prompt on GitHub under MIT license. Operating Modes table is the single most reusable element.
type: reference
---

**Location:** github.com/mimurchison/claude-chief-of-staff (MIT licensed, public)
**Announced:** x.com/mimurchison/status/2022368529417224480

**Most valuable element — Operating Modes table (verbatim):**
```
Prioritize | Decide | Draft | Coach | Synthesize | Explore
```
"Explore" mode explicitly suspends the push-hard / Socratic mandate — the "release valve" when CEO needs to think out loud without being challenged. Invoke with "explore" or "just thinking out loud."

**Second most valuable: goals.yaml architecture**
Goals live in an external file (~/.claude/goals.yaml), not in the system prompt. Updated quarterly. System prompt references it by name. This means Custom Instructions never need rewriting when priorities change — only the file does.

**Third: Send guard**
"Never send any message without explicit 'Send' or 'Y' — applies to ALL channels, no exceptions."

**How to apply:** When building any CoS-style system prompt:
1. Use the Operating Modes table as the mode-detection backbone
2. Externalize quarterly goals to a Project File (not Custom Instructions)
3. Include the send guard verbatim or adapted

source: session-111 | tier: B | validated: research session (agent web search)
