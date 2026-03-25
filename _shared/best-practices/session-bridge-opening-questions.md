---
name: session-bridge-opening-questions
description: Include 6 explicit situational questions at the top of session bridge handoff files so the next Claude asks Patrick for current state BEFORE taking any action. Critical for projects with human actions between sessions.
type: feedback
---

## Pattern: Session Bridge Opening Questions

**Rule:** When a session bridge is created for a project where Patrick will take real-world actions between sessions (meetings, calls, submissions, approvals), always include a § ALOITUSKYSYMYKSET block at the top of the bridge file with 3–6 specific questions.

**Why:** Multiple parallel sessions run in 1658 Holdings. The next Claude inherits stale context without knowing what Patrick has done since. In S99: multiple sessions (99, 100, 101) ran concurrently. Without opening questions, the next Kulusiirto Claude might produce a Rainer letter not knowing the lausunto wasn't submitted yet, or brief Aku Kärki incorrectly not knowing he'd already been called.

**Format:**
```markdown
## ALOITUSKYSYMYKSET (esitä heti session aluksi)

Ennen mitään muuta, kysy Patrickiltä:
1. [Specific yes/no or status question]
2. [Specific yes/no or status question]
...
*Vastausten perusteella navigoi oikeaan tehtävälistaan alla.*
```

**How to apply:**
1. At session end, think: "What real-world actions will Patrick take before the next session?"
2. Write one question per action (binary preferred: "jätetty kyllä/ei?")
3. Include navigation instructions: "if yes → do X, if no → do Y"
4. Place at the VERY TOP of the session bridge, before any context

**When NOT to use:**
- Pure AI work sessions with no human-action dependencies → standard bridge is fine

**Source:** S99 (2026-03-19) — Kulusiirto session bridge construction, multi-session parallel context problem
