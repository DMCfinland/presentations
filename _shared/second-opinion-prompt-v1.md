# Second Opinion Request — Claude Code v1 System Upgrade
# Paste this into a fresh Claude session (no prior context)
# Date: 2026-02-23

---

I want your honest technical assessment before we deploy a system upgrade. No prior context needed — everything is below.

## What We're Running Today

We use Claude Code as a knowledge/workflow engine for a 10-company holding company. The CEO (Patrick) and Claude work together session-by-session. The system has:

- `CLAUDE.md` — always-loaded rules (global → project → company hierarchy)
- `_shared/best-practices/` — 25 Tier B pattern files loaded on demand
- `_shared/warm-packs.md` — 7 project-type briefings loaded at session start
- `CURRENT-STATUS.md` — session log, rolling window, context pack
- Session counter: currently at 50, reviewed every 10 sessions

Current problems: KB consultation 50% of sessions (target >40% but declining), pattern harvest 44% (target >20% but declining).

## Proposed Upgrade (designed by Grok 4.2)

Three components:

### 1. Post-write Hook (shell → Python → Haiku API)
Every file write under `project-files/` or `mining-outputs/` triggers:
- `post-write-trigger.sh` (bash, path-filtered, debounced at 200 bytes)
- → calls `extract_pattern_haiku.py`
- → calls Haiku 4.5 API with last 12KB of file content
- → appends structured JSON to `PENDING-PATTERNS.md`

Cost: ~$0.001 per trigger. ~$0.01/session.

### 2. Five new Skills (markdown files in ~/.claude/skills/)
- `/load-context` — selective context load at session start (target <15KB vs current 49KB)
- `/task-complete` — self-critique after each deliverable
- `/incorporate-steering` — routes Patrick's corrections to PENDING-PATTERNS.md immediately
- `/session-close` — auto-runs at session end (replaces manual logging)
- `/harvest-cycle` — every 5-10 sessions, promotes PENDING-PATTERNS.md entries to Tier B or flags Tier A

### 3. New block added to top of global CLAUDE.md
Grok says "insert at very top, overrides all lower-tier rules where conflict exists."
Contains: session start protocol, enforcement triggers, handover gates, session end automation.

The steering detection rule specifically: "If Patrick types words like 'actually', 'instead', 'better', 'change', 'fix', 'no —', immediately call /incorporate-steering."

## The AOU/HT Metric (new success measure replacing kb_consulted: yes/no)
Autonomous Output Units per Human Turn. Target: 3.5+ AOU/HT (currently ~1.0-1.2).
Logged automatically by /session-close.

---

## Specific Questions

**1. The CLAUDE.md override block:**
Grok says to insert a new block at the "very top" of global CLAUDE.md that "overrides all lower-tier rules where conflict exists." Our current CLAUDE.md is ~200 lines of carefully tuned rules. Is inserting an override block at the top a good architectural move, or does it create fragility? What's the risk of rule conflicts?

**2. The steering-detection keyword trigger:**
Triggering `/incorporate-steering` when Patrick uses words like "actually", "instead", "better", "change", "fix", "no —" — is this approach reliable? False positive rate? Better alternatives?

**3. The session-close automation:**
"When user says 'end', 'stop', 'done', or session naturally concludes" — how does Claude Code detect natural session conclusion? Can "stop" and "done" cause unintended triggering mid-session?

**4. The hook architecture overall:**
Is "post-write hook → bash → Python → Haiku API" a sound pattern for real-time self-improvement? Any failure modes we should design for?

**5. The AOU/HT metric:**
Is "Autonomous Output Units per Human Turn" actually measurable in this architecture? What defines "1 AOU"? Who counts the human turns — the hook, the AI, manual logging?

**6. Go/no-go:**
Given our actual problem (KB consultation declining, pattern harvest declining), does this upgrade address the root cause? Or is there a simpler fix we're missing?

Be direct. If parts of this are over-engineered or risky, say so.
