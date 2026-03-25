# Second Opinion Before Deploying System Changes

**What:** Before deploying any change that modifies core config files (CLAUDE.md, settings.json, warm-packs.md), write a second-opinion prompt and paste it into a fresh Claude session with no prior context.

**Why:** The session that designed the change is biased toward its own reasoning. A fresh-context Claude asks the questions the designing session skipped. In this case, Grok's v1 design had 3 components rejected outright (CLAUDE.md override block, keyword detection, AOU/HT metric) — none of which the designing session flagged as problematic.

**When to apply:** Any system architecture change that:
- Modifies CLAUDE.md (especially Tier A rules or session protocol)
- Touches settings.json (hooks, permissions)
- Redesigns warm packs or session-end protocol
- Was designed by an external AI (Grok, GPT-4) without Claude Code context

**Format:** Write a `second-opinion-prompt-[name].md` with:
1. What the system does today (3-5 bullets)
2. The proposed change (full description)
3. 5-6 specific questions targeting the riskiest parts
4. "Be direct. If parts of this are over-engineered or risky, say so."

**Source:** Session 52 (2026-02-23). Grok v1 upgrade validated by fresh Claude session — 3/8 components rejected.
