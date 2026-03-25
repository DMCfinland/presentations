# Coding Project Preflight Checklist

**Purpose:** One-stop checklist before starting any AI-built coding project. Covers PRD design, architecture decisions, team composition, quality gates, and tool selection. Use this BEFORE writing blueprints or spawning agents.

**Source:** Synthesized from 13 Dec 2025 research files (agentic-coding-patterns.md) + 196-video YouTube KB (agent-architecture, models-capabilities, software-dev, 7 individual video analyses). Cross-validated Feb 2026.

**Tier:** B (load on demand). Promote to Tier A after 3+ uses on real projects.

---

## PHASE 0: Define Correctness (Before Everything Else)

> "Hallucinations are not a model problem. This is an us problem. The system is optimizing what we as humans are actually rewarding." — YouTube KB, CTO advice video

You CANNOT choose architecture, model, team composition, or tools until you answer these:

- [ ] **List every specific claim the system will make.** Not "good summaries" — specific claims like "display room price" or "confirm booking availability."
- [ ] **Define evidence requirements for each claim type.** Where does the proof come from? What source of truth validates it?
- [ ] **Separate fatal errors from acceptable uncertainty.** What kinds of inaccuracy destroy trust? What uncertainty can the system express honestly? (The Travel Assistant: wrong prices = fatal. "Northern lights probability ~40% tonight" = acceptable uncertainty.)
- [ ] **Explicitly allow "I don't know."** Systems must be told that admitting uncertainty is acceptable, or they hallucinate confidently. Most prompts inadvertently punish honest uncertainty.
- [ ] **Get stakeholder sign-off on what "correct" means.** In writing. Before building. Evaluation framework is built BEFORE the system, not after.
- [ ] **Define multiple quality dimensions.** Truthfulness, completeness, tone, policy compliance, speed, cost, refusal behavior, auditability. Any single metric gets gamed (Goodhart's Law).

**Health metric:** `System Health = (Daily Active Users / Intended Users) x (Correct Outputs / Total Outputs)` — measures adoption AND reliability simultaneously.

---

## PHASE 1: PRD Design — What Makes a Good Coding PRD

### The 4-6 Brain Files (External Memory Harness)

Every project needs these files before any code is written:

| File | Purpose | Max Size | Your Equivalent |
|------|---------|----------|----------------|
| `architecture.md` | Global rules — What + Why, not How | 3-4 pages MAX | CLAUDE.md + project CLAUDE.md |
| `features.yaml` / `TASKS.json` | Single source of truth — 50-600 atomic testable rows | Each row = one coder session | MASTER_MAP.md decomposed |
| `progress.json` | Machine-readable state for orchestrator | Auto-updated | Orchestrator state file |
| `changelog.md` | Human-readable audit trail, auto-appended | Append-only | Git log + session logs |
| `init.sh` / `Dockerfile` | One-click environment reproducibility | As needed | — |
| `known-issues.md` | Tracked bugs and workarounds | As needed | — |

### features.yaml Row Format (Task Decomposition Schema)

Each row is the complete self-contained prompt for a coder agent:

```yaml
- id: F-047
  name: User login form
  description: "Email + password form with validation"
  acceptance_criteria:
    - Form renders with email and password fields
    - Invalid email shows error message
    - Successful login redirects to dashboard
  estimated_complexity: 2  # 1-5 scale
  depends_on: [F-012, F-023]
  status: TODO  # TODO > IN_PROGRESS > DONE
  output: null  # commit hash + file path, appended by coder
```

**Rule:** If acceptance criteria aren't specified, the coder invents them. Vague rows = hallucinated requirements.

### PRD Quality Gates

- [ ] **architecture.md is <= 4 pages.** Longer = agents drift. If it's longer, split into sub-architecture docs per module.
- [ ] **Every feature row has explicit acceptance criteria.** No "implement login" without specifying what login means.
- [ ] **No placeholders.** "Will be covered later" = never covered. If you can't specify it now, it's not in this build.
- [ ] **Dependencies mapped.** `depends_on` field enables parallel execution of independent tasks.
- [ ] **Complexity estimated.** 1-5 scale drives model assignment and parallel batching.
- [ ] **Human gate between planning and building.** Patrick approves architecture before coding starts. This is THE critical quality gate.

---

## PHASE 2: Architecture Decisions

### Two-Phase Architecture: Plan First, Build After

**Never reverse the order.**

| Phase | What | Who | Cost | Duration |
|-------|------|-----|------|----------|
| Pass 1: Architecture | Multi-agent debate → clean brain files | Patrick + Claude (strategic) | $30-90 | 4-12h |
| Pass 2: Coding | Harness reads features.yaml, spawns parallel coders | Orchestrator script + agents | $200-600 | 8-18h wall-clock |
| **Total enterprise MVP** | 400-600 modules | — | **$400-600 (Sonnet)** | **7-21 days** |

### Codex vs Claude Code vs Orchestrated Teams — Decision Framework

> "Planning compounds, execution depreciates. When AI can execute quickly, the bottleneck shifts to decision quality." — YouTube KB, Codex vs Claude Code

| Decision Type | Best Tool | Why |
|--------------|-----------|-----|
| **High switching-cost architecture** | Codex / strategic-mode Opus | Maintains strategic altitude, returns questions before answers |
| **Multi-stakeholder alignment** | Codex / strategic-mode Opus | Presents 3 structured options, progressive disclosure |
| **Well-understood implementation** | Claude Code / orchestrated teams | Execution is the bottleneck, not decisions |
| **Parallel bulk coding** | Orchestrated teams (harness) | 10+ workers in parallel, Sub-Boss per module |
| **Single complex module** | Claude Code (single agent) | Multi-agent adds 3-10x cost on simple tasks |

**Key insight from YouTube KB:** Codex is superior for strategic thinking (architecture, PRD design). Claude Code is optimized for tactical execution. Use Codex/Opus for Pass 1, Claude orchestrated teams for Pass 2.

### Architecture Self-Check

- [ ] **Can 1 agent do it?** If yes, don't add agents. Multi-agent overhead on <200 LOC tasks = negative ROI.
- [ ] **Is the orchestrator a script, not an agent?** The orchestrator is a while-loop. Do not over-engineer coordination.
- [ ] **Do workers know about each other?** They shouldn't. Workers are deliberately dumb and isolated. Information hiding is the core architectural principle.
- [ ] **Is context per coding session <15K tokens?** Each coder loads only: architecture.md + its features.yaml row + touched files.
- [ ] **Is memory external, not in-prompt?** Files outlast any context window. State in JSON/SQLite on disk, not in chat history.
- [ ] **Are structured outputs grammar-enforced?** Use API-level JSON schemas for all agent outputs. Anthropic's implementation compiles schemas into a grammar that physically restricts token generation — guaranteed compliance, not "~100%". Only exception: safety refusals. (Verified Feb 2026, Anthropic docs.)
- [ ] **Is the architecture vendor-neutral?** Model performance moats last 6-18 months. Design for model substitution. Markdown brain files + Git state = portable across any provider.

### Context Management Rules

- **Effective window: stay under 256K tokens** regardless of model's stated limit
- **architecture.md <= 4 pages** or agents drift
- **Middle curse:** relevant content in the center of long contexts loses ~20-50% retrieval accuracy. Put critical data at start/end.
- **Default context should contain nearly nothing.** Make retrieval an active agent decision, not passive inheritance. More tokens = more distraction, not more clarity.
- **6 x 3-4h batches > 1 x 20h session.** Quality collapses to ~11% of target at hour 10.
- **Delta updates over full rewrites** in long sessions (+10.6% quality, ACE paper).
- **Lock-and-advance:** Once a module receives approval, it is not revisited unless integration conflict. Prevents endless refinement.

---

## PHASE 3: Team Composition — How Many Agents?

### Decision Tree

```
Simple task (<200 LOC, 1-2 files)
  > 1 agent. Multi-agent adds 3-10x cost here.

Medium (2-5 files, testing needed)
  > 2-3 agents: Planner + Coder + Reviewer
  > AgentCoder pattern: 96.3% HumanEval

Complex (full system, >10 files)
  > 5-7 agents: Two-tier hierarchy (Planner/Worker/Judge)
  > MetaGPT: 85.9% HumanEval

Production multi-repo, high concurrency
  > Hierarchical with dynamic agents (HALO: 83.39% GAIA)

> 10 agents > almost always over-engineering
  > UserJot started with 15, reduced to 6
```

**Google/MIT research (Dec 2025):** When single-agent accuracy exceeds ~45%, adding more agents yields diminishing or negative returns. 79% of multi-agent failures originate from spec and coordination issues; only 16% from infrastructure. Tool selection accuracy degrades past 30-50 tools.

### The Optimal 4-5 Roles (Benchmarked)

| Role | Purpose | Key Rule |
|------|---------|----------|
| **PM-Initializer** | One-shot: architecture + features.yaml + artifacts | Max 2 pages per artifact. Include human gate. |
| **Orchestrator** | Simple script (NOT AI). Polls progress, spawns next worker. | While-loop. Do not over-engineer. |
| **Module-Lead (Sub-Boss)** | Oversees one module. Loops Coder + Tester until acceptance criteria pass. | **Required. Raises quality 65% > 92% (SWE-Bench).** |
| **Coder Agent** | Implements one features.yaml row. Loads only: arch + row + files. | Incremental only — no rewrites. |
| **Tester Agent** | Runs tests, flags failures with explanations. | Separate from Coder for isolation. |

**Sub-Boss is the single highest-ROI pattern.** Without it: 65% quality. With it: 92%. This is non-negotiable for any project >50 features.

### Anthropic's Memory-First Pattern (Validated)

- **Initializer Agent:** Transforms user prompt into persistent domain memory artifacts (feature lists, progress logs, test harnesses, rules of engagement). Initializer needs no memory itself — purely transformational.
- **Worker Agent:** Stateless. Every run: reads shared memory > picks one atomic task > executes > tests > updates memory > exits.
- **Test harness is the source of truth** — not agent self-assessment. This eliminates "confident failure."
- **Bootup ritual mandatory:** Read memory, run checks, orient, then act.

> "Memory is the system. The prompt is not the agent. The LLM is not the agent." — Anthropic ACE paper

### Worker Design Rules

- [ ] Workers are stateless and episodic (~1h cycles, then terminate with clean context)
- [ ] Workers never know other workers exist (no peer communication)
- [ ] 3-5 core tools per worker maximum (orthogonal, not overlapping)
- [ ] Communication through structured artifacts, not shared transcripts
- [ ] Functional roles (planner/executor/verifier), NOT human job titles (CEO/researcher). Anthropomorphic titles cause reasoning drift.

### Darwinian/Tournament Model: NOT Recommended

The research (Dec 2025) and YouTube KB both recommend AGAINST competitive multi-coder tournament models:
- 3x inference cost for marginal quality gain on well-decomposed tasks
- The two-tier hierarchy (Planner/Worker/Judge) achieves equivalent quality at 1/3 the cost
- Only consider tournament for truly ambiguous design decisions where multiple valid approaches exist
- **Recommendation:** Resolve TA-A4 in favor of the standard 4-5 role pattern.

---

## PHASE 4: Quality Gates — Non-Negotiable

### Red Team & Judge Agent

- [ ] **Judge Agent is mandatory for production systems.** PwC: 7x accuracy improvement (10% > 70%). STRATUS: 1.5x improvement. Hallucination reduction: -40%.
- [ ] **Scope-Calibrate first.** Before critiquing any output, ask: what is this *trying to be*? Assess against stated goal, not a different one.
- [ ] **Chain of Verification.** Force models to attack their own outputs through mandatory critique steps. Don't ask "be careful" — build self-critique into the generation process.
- [ ] **Multi-persona debate requires structural conflict.** Personas must have explicitly conflicting optimization targets (cost vs quality vs speed). Without conflict, you get agreement theater.
- [ ] **Test harness = automated judge.** Pass/fail is definitive truth, not agent self-assessment.

### Quality Rubric (per output)

| Level | Definition | Max per module |
|-------|-----------|---------------|
| FATAL | Fails stated purpose entirely, incorrect, or dangerously outdated | Max 2 |
| HIGH | Major omission that blocks intended use | Unlimited |
| MEDIUM | Structural gap that degrades but doesn't block | Unlimited |
| LOW | Styling, formatting, minor polish | Unlimited |

### 7 Non-Negotiable Checks per Module

Before treating any agent output as complete:

1. [ ] Every claim has a URL/DOI or source reference
2. [ ] Numbers, not "significantly" — quantify everything
3. [ ] Both benefits AND limitations shown for every pattern
4. [ ] Decision tree: when to use AND when NOT to use
5. [ ] Code examples run without modification
6. [ ] No placeholders ("will be covered later" = not done)
7. [ ] Machine-verifiable completion criteria (word counts, test pass rates, not vibes)

**Self-validation gate:** Verify 3 random claims, run 2 code examples, count cross-references, confirm every benchmark cites source. Required: 9.8/10 minimum.

### Multi-Model Voting (When Error Cost is High)

- 3 models: $0.06/task, +6.7% accuracy
- 5 models: $0.10/task, +8.0% accuracy (diminishing returns after 3)
- **When to trigger:** error cost > 100x generation cost, complexity > 8/10
- Travel Assistant examples: booking confirmations, price quotes, safety advisories

---

## PHASE 5: Error Recovery Architecture

### Recovery Pattern Selection

```
Side effects (DB, API calls, bookings)?     > Saga (coordinated rollback)
Independent parallel workers?                > Circuit Breaker (exponential backoff)
Downstream bottleneck?                       > Adaptive Backpressure (rate-limit upstream)
Long-running (>30 min)?                      > Checkpoint-Restart (every 5 min)
One module failed?                           > Re-spawn Sub-Boss only (5-20 min)
```

### Production Hardening Rules

- [ ] **90% of AI agents fail within 30 days** in production. Production hardening is not optional.
- [ ] **Human escalation gates required** in regulated domains.
- [ ] **Always maintain a manual override path.** (Travel Assistant: Staff Dashboard Takeover mode)
- [ ] **Intent validation before execution.** Split interpretation and execution layers. Intent is surfaced and validated before tools are touched.

---

## PHASE 6: Prompt Engineering for Agents (2025+ Rules)

### What Changed (Validated)

| Rule | Evidence |
|------|----------|
| **Explicit CoT HURTS reasoning models** | OpenAI ablations: removing CoT from o-series improved latency AND accuracy |
| **Temperature ~1.0 beats 0** for complex reasoning | Enables multi-path hypothesis exploration. Use 0 only for structured execution. |
| **Structured outputs: grammar-enforced, not "~100%"** | Anthropic compiles JSON schemas into grammar, physically restricts token generation. Guaranteed. Only exception: safety refusals. |
| **Parallel tool calling improves success ~15-20%** | Use by default |
| **>20-50 tools without search mechanism** degrades accuracy | Use Tool Search |
| **Multi-turn degradation is real** | Models perform better on 1st response than nth (RLHF training data artifact) |

### Validated Prompt Order

**Context > Role > Goal/Task > Constraints > Output Format**

"Anchor reasoning in data first, instructions last."

### Model Routing for Coding Projects

| Task | Model | Rationale |
|------|-------|-----------|
| Architecture / PRD design | Opus or Codex (strategic mode) | Best reasoning for synthesis |
| Implementation | Sonnet (default) | 79.6% SWE-bench, best value |
| Testing | Sonnet or Haiku | Mechanical validation |
| Review / Judge | Sonnet | Structured critique |
| Classification / sorting | Haiku | 3x cheaper, sufficient |

### Agent Role Incompatibility Pairs (Never Combine)

- Critic + Creative Writer
- Planner + Creative Writer
- Data Scientist + Creative Writer
- Legal Advisor + Creative Writer
- Any critical role + Customer Support

---

## PHASE 7: Cost Architecture

### Stacking Discounts

| Technique | Savings |
|-----------|---------|
| Prompt caching (system field) | 90% on cache reads |
| Batch API | 50% discount |
| Combined | ~95% off repeated content |

### Project Cost Estimates

| Project Size | Modules | Cost (Sonnet) | Duration |
|-------------|---------|---------------|----------|
| Simple prototype | 50 | $50-100 | 2-5 days |
| Medium app | 200 | $200-400 | 1-2 weeks |
| Enterprise MVP | 500 | $400-600 | 2-3 weeks |
| + Multi-model voting | per task | $0.06 (3 models) | — |

---

## PHASE 8: Anti-Patterns & Reality Checks

### The Benchmark vs. Reality Gap

| What They Claim | What's Real |
|----------------|------------|
| SWE-bench Verified: 77% | SWE-bench Pro (private repos): **23%** |
| AppWorld: high scores | 86.7% failure rate in production |
| ChatDev: multi-agent magic | 33.3% correctness on some benchmarks |

**Plan for ~25% first-pass success rate on complex real-world modules, not 77%.**

### What Kills Autonomous Projects

- No external memory (agents repeat errors, lose context, declare premature success)
- >10 agent types (coordination overhead exceeds value)
- Placeholders masquerading as deliverables
- Full history in every prompt (balloons cost 80%+)
- No Sub-Boss quality gate (solo coder = 65% quality)
- Treating orchestrator as AI (it's a while-loop script)
- No changelog (impossible to debug at scale)
- Vague features.yaml rows
- Over-promising scope (20K-word doc attempted in one session delivered 2,231 words = 11%)

### Apple "Illusion of Thinking" Warning

Frontier models show >80% accuracy collapse above compositional complexity threshold. Models reduce thinking effort on harder tasks (counter-intuitive). **Always decompose compositional tasks.** Never rely on internal reasoning alone for critical paths. The Travel Assistant's scoring formula (`Score = (Match*W1) + (Weather*W2) + ...`) is compositional — test heavily, decompose if accuracy drops.

---

## PHASE 9: Future-Proofing — New Model Integration Protocol

### When a New Frontier Model Ships (Evaluate Within 1 Week)

Run these 7 checks with 20-50 samples each:

1. **Does minimalism still win?** (vs verbose prompts)
2. **Preferred format?** (XML vs headings vs JSON)
3. **Temperature sweet spot for reasoning?**
4. **Tool decision autonomy sufficient?**
5. **Reflection/error recovery strength?**
6. **Compositional complexity ceiling?** (Apple "Illusion of Thinking" test)
7. **Cost/latency profile?**

Then: Update capability matrix, update warm packs, version the change.

### YouTube KB Additions to Future-Proofing

- **Model drift management > model selection.** "Obsessing over which model to use misses that drift over time can have greater impact than starting model quality." Build drift detection as a first-class system.
- **Architecture-first diagnosis.** If swapping in a frontier model produces no improvement, your architecture is the bottleneck, not the model.
- **Vendor-neutral memory.** Build memory in markdown/structured files with explicit export. Treat vendor memory features as convenience layers over a portable core.
- **Context files (.md) are strategic compounding assets.** CLAUDE.md files reduce first-try degradation as models change.
- **Model performance moats: 6-18 months.** Design for model substitution. Multi-model platforms are the endgame.

---

## QUICK REFERENCE: The 15 Highest-Impact Rules

1. **Define correctness before choosing technology** — Phase 0 is non-negotiable
2. **Sub-Boss pattern** — 65% > 92% quality (single biggest ROI)
3. **Orchestrator = script, not agent** — while-loop, not LLM
4. **architecture.md <= 4 pages** — longer = agents drift
5. **Workers are stateless, episodic, isolated** — no peer awareness
6. **3-5 tools per worker maximum** — orthogonal, not overlapping
7. **Grammar-enforced structured outputs** — API-level schemas, not prompt-based
8. **Judge Agent is mandatory for production** — 7x accuracy improvement
9. **Plan for 25% first-pass success** (real codebases), not 77% (benchmarks)
10. **6 x 3-4h batches > 1 x 20h session** — quality collapses at hour 10
11. **Codex/Opus for architecture, Claude teams for execution** — strategic vs tactical
12. **Test harness = source of truth** — not agent self-assessment
13. **Memory is the system** — files on disk, not in context window
14. **Lock-and-advance** — approved modules don't get revisited
15. **90% of AI agents fail in 30 days** — production hardening is not optional

---

*Compiled from: agentic-coding-patterns.md (13 research files, Dec 2025) + YouTube KB (196 videos, 1,331 gold insights, 12 topic clusters). Cross-validated against Anthropic ACE paper, Google ADK, Manus architecture docs, PwC Judge Agent study, Scale AI SWE-bench Pro, Google/MIT multi-agent study (Dec 2025). Structured outputs verified against Anthropic API docs (Feb 2026).*
