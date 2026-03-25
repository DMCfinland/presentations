# MVP MAP

## UAP v0.1 Folder Structure

**Purpose:** Visual reference for where every file goes  
**Rule:** Create this structure EXACTLY before writing any code

---

## COMPLETE FOLDER TREE

```
uap-mvp/
│
├── .clinerules                    # AI assistant rules (BP1)
├── .pre-commit-config.yaml        # Git hooks config (BP6)
├── .gitignore                     # Ignore patterns
├── README.md                      # Project documentation
│
├── config/                        # Configuration files
│   └── agent_config.yaml          # Agent settings
│
├── memory/                        # MEM1 System (BP2)
│   ├── memory.json                # Agent state (THE BRAIN)
│   └── memory_schema.json         # JSON schema for validation
│
├── plan/                          # Living Plan (BP3)
│   ├── spec.md                    # Task specification
│   └── todo.md                    # Progress tracking
│
├── src/                           # Source code
│   ├── __init__.py
│   ├── main.py                    # Entry point
│   │
│   ├── gatekeeper/                # Spec Validation (BP4)
│   │   ├── __init__.py
│   │   └── validator.py           # Gatekeeper logic
│   │
│   ├── agent/                     # Agent Loop (BP8)
│   │   ├── __init__.py
│   │   ├── loop.py                # Main agent loop
│   │   └── memory_manager.py      # MEM1 implementation
│   │
│   ├── tools/                     # AST Tools (BP5)
│   │   ├── __init__.py
│   │   ├── ast_refactor.py        # AST-based code changes
│   │   └── banned_patterns.py     # Regex detection
│   │
│   └── gates/                     # Quality Gates (BP7)
│       ├── __init__.py
│       └── cheap_gate.py          # pytest + pylint runner
│
├── tests/                         # Test suite
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixtures
│   ├── test_gatekeeper.py         # Gatekeeper tests
│   ├── test_memory.py             # MEM1 tests
│   ├── test_agent.py              # Agent loop tests
│   └── test_ast_tools.py          # AST tool tests
│
├── scripts/                       # Utility scripts
│   ├── reset_context.py           # Hard Reset (BP9)
│   └── run_hello_world.py         # Demo script (BP10)
│
└── workspace/                     # Agent working directory
    └── output/                    # Generated code goes here
```

---

## FILE PURPOSES

### Root Files

| File | Purpose | Created In |
|------|---------|------------|
| `.clinerules` | Tells Cursor/Cline what patterns are banned | BP1 |
| `.pre-commit-config.yaml` | Git hooks for regex ban | BP6 |
| `.gitignore` | Standard Python ignores | BP1 |
| `README.md` | Project docs | BP1 |

### config/

| File | Purpose | Created In |
|------|---------|------------|
| `agent_config.yaml` | Timeout, model, constraints | BP1 |

### memory/ (THE MOST IMPORTANT FOLDER)

| File | Purpose | Created In |
|------|---------|------------|
| `memory.json` | Agent's ONLY persistent state | BP2 |
| `memory_schema.json` | Validates memory.json structure | BP2 |

### plan/ (THE LIVING PLAN)

| File | Purpose | Created In |
|------|---------|------------|
| `spec.md` | What the agent must build | BP3 |
| `todo.md` | Step-by-step progress | BP3 |

### src/gatekeeper/

| File | Purpose | Created In |
|------|---------|------------|
| `validator.py` | Checks spec.md is valid | BP4 |

### src/agent/

| File | Purpose | Created In |
|------|---------|------------|
| `loop.py` | Main execution loop | BP8 |
| `memory_manager.py` | Read/write memory.json | BP2 |

### src/tools/

| File | Purpose | Created In |
|------|---------|------------|
| `ast_refactor.py` | AST-based code modification | BP5 |
| `banned_patterns.py` | Detect sed/awk/regex | BP6 |

### src/gates/

| File | Purpose | Created In |
|------|---------|------------|
| `cheap_gate.py` | Run pytest + pylint | BP7 |

### scripts/

| File | Purpose | Created In |
|------|---------|------------|
| `reset_context.py` | Simulate hard reset | BP9 |
| `run_hello_world.py` | Complete demo | BP10 |

---

## CRITICAL PATHS

### The Memory Path
```
Agent reads: memory/memory.json
Agent reads: plan/spec.md
Agent reads: plan/todo.md
Agent writes: memory/memory.json
Agent writes: plan/todo.md
Agent writes: workspace/output/*.py
```

### The Validation Path
```
User writes: plan/spec.md
Gatekeeper checks: plan/spec.md (not empty, has requirements)
If valid: Agent starts
If invalid: Error message, agent blocked
```

### The Safety Path
```
Agent writes code: workspace/output/*.py
Pre-commit checks: no sed/awk/regex
Cheap Gate runs: pytest + pylint
If pass: git commit allowed
If fail: commit blocked
```

---

## WHAT GOES WHERE (Decision Guide)

| I need to... | Put it in... |
|--------------|--------------|
| Define a task | `plan/spec.md` |
| Track progress | `plan/todo.md` |
| Store agent state | `memory/memory.json` |
| Configure the agent | `config/agent_config.yaml` |
| Write production code | `src/**/*.py` |
| Write generated code | `workspace/output/*.py` |
| Write tests | `tests/*.py` |
| Write utility scripts | `scripts/*.py` |
| Ban AI patterns | `.clinerules` |
| Configure git hooks | `.pre-commit-config.yaml` |

---

## VISUAL: DATA FLOW

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           UAP MVP DATA FLOW                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                          ┌─────────────┐                                │
│                          │   USER      │                                │
│                          │ (writes)    │                                │
│                          └──────┬──────┘                                │
│                                 │                                       │
│                                 ▼                                       │
│                          ┌─────────────┐                                │
│                          │  spec.md    │ ◄── plan/                      │
│                          └──────┬──────┘                                │
│                                 │                                       │
│                                 ▼                                       │
│   ┌─────────────────────────────────────────────────────────┐          │
│   │                    GATEKEEPER                            │          │
│   │               (src/gatekeeper/validator.py)              │          │
│   └─────────────────────────┬───────────────────────────────┘          │
│                             │                                           │
│              ┌──────────────┴──────────────┐                           │
│              ▼                              ▼                           │
│       [VALID SPEC]                  [INVALID SPEC]                     │
│              │                              │                           │
│              │                              ▼                           │
│              │                       ┌───────────┐                      │
│              │                       │   ERROR   │                      │
│              │                       │   (stop)  │                      │
│              │                       └───────────┘                      │
│              │                                                          │
│              ▼                                                          │
│   ┌─────────────────────────────────────────────────────────┐          │
│   │                    AGENT LOOP                            │          │
│   │                (src/agent/loop.py)                       │          │
│   │                                                          │          │
│   │   READS:                    WRITES:                      │          │
│   │   ├── memory.json           ├── memory.json              │          │
│   │   ├── spec.md               ├── todo.md                  │          │
│   │   └── todo.md               └── workspace/output/*.py    │          │
│   │                                                          │          │
│   └─────────────────────────┬───────────────────────────────┘          │
│                             │                                           │
│                             ▼                                           │
│   ┌─────────────────────────────────────────────────────────┐          │
│   │                    CHEAP GATE                            │          │
│   │               (src/gates/cheap_gate.py)                  │          │
│   │                                                          │          │
│   │   CHECKS:                                                │          │
│   │   ├── pytest (tests pass?)                               │          │
│   │   └── pylint (code quality?)                             │          │
│   │                                                          │          │
│   └─────────────────────────┬───────────────────────────────┘          │
│                             │                                           │
│              ┌──────────────┴──────────────┐                           │
│              ▼                              ▼                           │
│       [TESTS PASS]                  [TESTS FAIL]                       │
│              │                              │                           │
│              ▼                              ▼                           │
│   ┌─────────────────┐            ┌─────────────────┐                   │
│   │   GIT COMMIT    │            │   RETRY LOOP    │                   │
│   │   (allowed)     │            │   (max 3x)      │                   │
│   └────────┬────────┘            └─────────────────┘                   │
│            │                                                            │
│            ▼                                                            │
│   ┌─────────────────────────────────────────────────────────┐          │
│   │                   HARD RESET                             │          │
│   │              (scripts/reset_context.py)                  │          │
│   │                                                          │          │
│   │   WIPES:                    PRESERVES:                   │          │
│   │   ├── Chat history          ├── memory.json              │          │
│   │   └── Context window        ├── spec.md                  │          │
│   │                             ├── todo.md                  │          │
│   │                             └── workspace/*              │          │
│   │                                                          │          │
│   └─────────────────────────────────────────────────────────┘          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## GOLDEN RULE

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   THE AGENT READS FROM FILES, NOT FROM MEMORY.              │
│                                                             │
│   If it's not in memory.json, spec.md, or todo.md,          │
│   the agent DOESN'T KNOW IT.                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

*UAP MVP v0.1 Map | December 2025*
