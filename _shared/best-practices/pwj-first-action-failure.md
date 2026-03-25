---
name: pwj-first-action-failure
description: Sessions receiving PWJ bridge prompts skip /pwj invocation and read files directly. Happens in >50% of executions. Fix is structural — "FIRST ACTION" line must be first in bridge prompt.
type: feedback
confidence: 0.7
source: sessions-97-99 (meta session + session 1 both failed this way)
---

# PWJ First-Action Failure

When a Claude Code session receives a bridge prompt containing "Run /pwj with this intake,"
it frequently skips the /pwj invocation and starts reading source files directly.
The session then operates as a plain Worker without the PWJ quality loop running.

**Observed in:**
- Session 1 (Validator Spec): went straight to writing spec without /pwj
- Meta session (Skill Improvement): went straight to file reads without /pwj

**Why it happens:**
The /pwj instruction competes with visible source files and task descriptions.
The "helpful assistant" default behavior is to start the task, not invoke a skill first.
When a file is open in the IDE, the session sees "work to do" and starts doing it.

**Consequence:**
- PWJ quality loop never starts (no Planner intake confirmation, no Judge rounds)
- Worker produces output and self-declares done (Checklist Theater)
- External Judge never runs
- Same failure as having no PWJ at all, despite the bridge prompt containing full intake

**Fix — structural, not advisory:**
The FIRST LINE of every PWJ bridge prompt must be:

```
⚠️ FIRST ACTION: invoke /pwj skill NOW. Do NOT read any files until /pwj is running.
Say "PWJ running — confirming intake" before doing anything else.
```

This forces the session to acknowledge the /pwj invocation explicitly before proceeding.
The "FIRST ACTION" + ⚠️ makes it harder to skip than buried instructions.

**How to apply:**
- Add the ⚠️ FIRST ACTION block as the first non-comment line of every bridge prompt
- Place it BEFORE the DMC Context block, BEFORE source files, BEFORE everything
- Session start check: if session says anything other than "PWJ running" as first words → it skipped invocation. Stop and invoke before continuing.
