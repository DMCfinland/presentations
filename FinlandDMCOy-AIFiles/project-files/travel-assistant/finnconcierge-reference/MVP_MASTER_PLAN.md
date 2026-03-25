# MVP MASTER PLAN

## Universal Agentic Protocol v0.1 — Single Agent Core

**Target:** Build One Perfect Agent Before Building an Army  
**Audience:** Beginners (Zero Terminal Experience)  
**Time Estimate:** 2-4 Hours

---

## THE GOAL

Before we build Leagues, Tournaments, or Bazaars, we must build **ONE agent that doesn't hallucinate**.

This MVP implements two critical laws:
1. **MEM1 (Amnesia):** The agent forgets everything except files on disk
2. **AST-Only:** The agent never uses regex/sed on code files

If we can't make ONE agent reliable, scaling to many is pointless.

---

## WHAT YOU'LL BUILD

```
┌─────────────────────────────────────────────────────────────────┐
│                    UAP MVP v0.1 ARCHITECTURE                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   [USER TASK] ──► [GATEKEEPER] ──► [AGENT LOOP] ──► [OUTPUT]   │
│                        │               │                        │
│                        ▼               ▼                        │
│                   spec.md         memory.json                   │
│                   todo.md         (MEM1)                        │
│                                                                 │
│   SAFETY RAILS:                                                 │
│   ├── Regex Ban (pre-commit hook)                              │
│   ├── Cheap Gate (pytest + pylint)                             │
│   └── Hard Reset (context wipe on commit)                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## PHASE OVERVIEW

| Phase | Name | Goal | Blueprints |
|-------|------|------|------------|
| **1** | SETUP | Create folder structure | BP1, BP2, BP3 |
| **2** | BRAIN | Implement MEM1 memory | BP4, BP8, BP9 |
| **3** | MUSCLE | Add AST tooling + safety | BP5, BP6, BP7 |
| **4** | VERIFY | Run Hello World task | BP10 |

---

## PHASE 1: SETUP (The Foundation)

**Goal:** Create a workspace that enforces discipline.

### What You'll Create
- Project folder with correct structure
- `.clinerules` file (tells AI assistants what's allowed)
- Memory system files (`memory.json`)
- Living plan files (`spec.md`, `todo.md`)

### Why This Matters
Without structure, AI agents wander. The folder layout IS the discipline.

### Blueprints
- **BP1:** Project Scaffolding
- **BP2:** Memory System
- **BP3:** Living Plan

### Success Criteria
```
✓ Folder structure matches MVP_MAP.md exactly
✓ All template files exist
✓ .clinerules file prevents bad patterns
```

---

## PHASE 2: BRAIN (The Memory System)

**Goal:** Make the agent forget everything except what's on disk.

### The Problem We're Solving
AI agents in long conversations start hallucinating. They "remember" things that didn't happen. They drift from the original task.

### The Solution: MEM1 Architecture
The agent NEVER reads chat history. It reads ONLY:
- `spec.md` (the task)
- `todo.md` (the progress)
- `memory.json` (the state)

After every `git commit`, we wipe the context. The agent is "reborn" with only file state.

### Blueprints
- **BP4:** Gatekeeper Lite
- **BP8:** Agent Loop
- **BP9:** Hard Reset

### Success Criteria
```
✓ Agent reads only from files (not chat)
✓ Gatekeeper rejects empty specs
✓ Hard reset wipes context on commit
```

---

## PHASE 3: MUSCLE (The Safety Rails)

**Goal:** Prevent the agent from writing bad code.

### The Problem We're Solving
AI agents love to use `sed`, `awk`, and regex to modify code. This ALWAYS breaks things because:
- They miss whitespace
- They hallucinate bracket counts
- They corrupt imports

### The Solution: AST-Only
We BAN all text manipulation on code. Instead, we use Abstract Syntax Tree (AST) tools that understand code structure.

### Blueprints
- **BP5:** AST Tooling
- **BP6:** Regex Ban
- **BP7:** Cheap Gate

### Success Criteria
```
✓ Pre-commit hook blocks sed/awk/regex on .py files
✓ AST tools installed and working
✓ Pytest + pylint run on every change
```

---

## PHASE 4: VERIFY (The Hello World)

**Goal:** Run ONE complete task through the entire system.

### The Test Task
```
Task: Create a Python function that adds two numbers
```

This trivial task proves the entire pipeline works:
1. Spec gets validated
2. Agent reads from files only
3. Code passes tests
4. No regex used
5. Memory persists correctly

### Blueprints
- **BP10:** Hello World Run

### Success Criteria
```
✓ Task completes without errors
✓ All tests pass
✓ Memory.json updated correctly
✓ No regex/sed in git log
✓ Context wipe simulated
```

---

## DEPENDENCY CHAIN

```
BP1 (Scaffolding)
 │
 ├──► BP2 (Memory) ──► BP8 (Agent Loop)
 │                          │
 └──► BP3 (Living Plan) ────┤
                            │
                            ▼
                      BP4 (Gatekeeper)
                            │
                            ▼
      BP5 (AST) ──► BP6 (Regex Ban) ──► BP7 (Cheap Gate)
                                              │
                                              ▼
                                    BP9 (Hard Reset)
                                              │
                                              ▼
                                    BP10 (Hello World)
```

---

## TOOLS YOU'LL USE

| Tool | Purpose | Installation |
|------|---------|--------------|
| **Python 3.10+** | Runtime | Already installed in Cursor |
| **pytest** | Testing | `pip install pytest` |
| **pylint** | Code quality | `pip install pylint` |
| **pre-commit** | Git hooks | `pip install pre-commit` |
| **ast (stdlib)** | Code parsing | Built into Python |

---

## WHAT YOU WON'T BUILD (Yet)

This MVP deliberately excludes:
- ❌ Multiple agents (Tournaments)
- ❌ ELO scoring
- ❌ Red Team attacks
- ❌ Collaborative Repair
- ❌ Citation Economy
- ❌ Gardener Protocol

These come in v1.0+ after the single agent is bulletproof.

---

## HOW TO USE THESE DOCUMENTS

### Step 1: Read MVP_MAP.md
Understand the folder structure before building.

### Step 2: Follow Blueprints 1-10 IN ORDER
Each blueprint builds on the previous. Don't skip ahead.

### Step 3: Copy-Paste Everything
All code is ready to paste into Cursor. You don't need to type commands.

### Step 4: Verify Each Step
Each blueprint has verification steps. Don't proceed until they pass.

---

## ESTIMATED TIME

| Phase | Duration | Cumulative |
|-------|----------|------------|
| Setup (BP1-3) | 30 min | 30 min |
| Brain (BP4, 8, 9) | 45 min | 1h 15m |
| Muscle (BP5-7) | 45 min | 2h |
| Verify (BP10) | 30 min | **2h 30m** |

---

## TROUBLESHOOTING

### "I don't have Python installed"
Cursor includes Python. Open any `.py` file and it works.

### "pip command not found"
In Cursor terminal, try `python -m pip install <package>`

### "Permission denied"
On Mac/Linux: `chmod +x <filename>`

### "Git not initialized"
Run: `git init` in project root

---

## NEXT STEPS AFTER MVP

Once BP10 (Hello World) passes:

1. **Add More Tasks:** Test with 5 different coding tasks
2. **Add Complexity:** Try a task requiring 2+ files
3. **Add Tests:** Increase pytest coverage to 80%+
4. **Graduate to v1.0:** Add Tournament system (Appendix F)

---

## REFERENCE DOCUMENTS

| Document | Purpose |
|----------|---------|
| `MVP_MAP.md` | Visual folder structure |
| `BLUEPRINTS_1_TO_10.md` | Step-by-step implementation |
| `Appendix H` | Full v2.2 Bible (for later) |
| `Appendix M` | v3.0 Economy (for much later) |

---

*UAP MVP v0.1 Master Plan | December 2025*
