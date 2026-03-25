# Agentic Coding Patterns — Best Practices

**Source:** 13 research files from December 2025 (Grok, Gemini, Claude conversations). Mined February 2026 with 6 parallel Sonnet extractors + Opus synthesis.
**Status:** Tier B (load on demand). Promote individual patterns to Tier A after 3+ uses.
**Use when:** Planning autonomous coding projects, evaluating agent architectures, designing multi-agent workflows for any 1658 portfolio company.

---

## 1. Timeless Principles (Model-Agnostic, Survive Any Generation)

**Minimalism wins.** 2025+ reasoning models internalize CoT via RL training. Explicit step-by-step instructions, large few-shot banks, and over-specified prompts actively *degrade* performance. OpenAI ablations: removing explicit CoT from o-series improved both latency and accuracy. Rule: less is measurably better.

**Trust the model more than yourself.** Give a clear goal, relevant context, and native tools — then step aside. Micro-control is the enemy of autonomous reasoning.

**Single responsibility per agent.** One concern per agent. Scaling, debugging, and error isolation require it. Never build "mega-agents" that do everything — errors propagate uncontrollably. 20-30% improvement in task success rates on complex tasks (arXiv papers).

**External memory beats prompt memory — always.** Files outlast any context window. Store everything outside the LLM. Each agent session loads only what's relevant for that task.

**Context quality beats context volume.** Curated 10K tokens outperforms unsorted 1M. Context rot is real: performance degrades before hitting the limit. Golden rule: find the *smallest* context set that enables the task.

**Structure beats narrative at scale.** Structured formats (XML for Claude, Markdown headings for Gemini/Grok, minimal JSON for GPT) reduce hallucinations ~10-15% in RAG tasks versus narrative prose.

**Architecture quality determines build quality.** The planning pass is where the project succeeds or fails. Garbage-in, garbage-out even with perfect execution agents.

**Mine first, build after.** Never start coding without locked architecture docs and a features manifest. This principle applies identically to AI agent projects and human ones.

---

## 2. The External Memory Harness (Core Architecture)

The only pattern that reliably completes production-grade autonomous builds:

### The 4-6 Brain Files (stored in Git)

| File | Purpose | Max Size |
|------|---------|----------|
| `architecture.md` | Global rules — What + Why, not How | 3-4 pages max |
| `features.yaml` | Single source of truth — 50-600 atomic testable rows | Each row = one coder session |
| `progress.json` | Machine-readable state for orchestrator | Auto-updated |
| `changelog.md` | Human-readable audit trail, auto-appended after every commit | Append-only |
| `init.sh` / `Dockerfile` | One-click environment reproducibility | As needed |
| `known-issues.md` | Optional — tracked bugs and workarounds | As needed |

Everything else (code, tests) lives in Git. This discipline keeps token usage sane across months-long projects.

### features.yaml Row Format

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
  status: TODO  # TODO → IN_PROGRESS → DONE
  output: null  # commit hash + file path, appended by coder
```

Zero hallucinated requirements — PM-Init writes everything the coder needs directly into the row.

---

## 3. Two-Phase Architecture: Plan First, Build After

**Never reverse the order.**

### Pass 1: Vision & Architecture Crew (multi-agent debate)

- 5 specialist personas debating: Architect, PM, Security, Data/AI, Full-Stack
- Input: founder's messy documents / requirements
- Output: clean 5-7 files (architecture.md, features.yaml, etc.)
- Cost: ~$30-90. Duration: 4-12 hours (run overnight)
- **Human approves before coding starts** — this is THE critical quality gate

### Pass 2: Coding Harness

- PM-Initializer validates artifacts, spawns first 10-15 dependency-free modules in parallel
- Sub-Boss loops per module (typically 2-5 iterations)
- Cost: ~$200-450 for 500 modules (Sonnet). ~$600-1200 with Opus
- Duration: 8-18 hours wall-clock for 200-module app

**Total for enterprise MVP:** Under $600 (Sonnet), 7-21 calendar days.

---

## 4. Team Compositions (Benchmarked)

### Decision Tree: How Many Agents?

```
Simple task (<200 LOC, 1-2 files)
  → 1 agent. Multi-agent adds 3-10x cost here.

Medium (2-5 files, testing needed)
  → 2-3 agents: Planner + Coder + Reviewer
  → AgentCoder pattern: 96.3% HumanEval (arXiv:2312.13010)

Complex (full system, >10 files)
  → 5-7 agents: MetaGPT/ChatDev patterns
  → MetaGPT: 85.9% HumanEval (arXiv:2308.00352)
  → ChatDev: 67% fewer hallucinations (arXiv:2307.07924)

Production multi-repo, high concurrency
  → Hierarchical with dynamic agents
  → HALO: 83.39% GAIA (arXiv:2411.15339)

> 10 agents → almost always over-engineering
  → UserJot started with 15, reduced to 6
```

### The Optimal 4-5 Roles

| Role | Purpose | Key Rule |
|------|---------|----------|
| **PM-Initializer** | One-shot: architecture + features.yaml + artifacts. Also IS the team builder. | Max 2 pages per artifact. Include human gate. |
| **Orchestrator** | Simple script (NOT AI). Polls progress, picks next row, spawns Module-Lead. | While-loop. Do not over-engineer. |
| **Module-Lead (Sub-Boss)** | Oversees one module. Spawns Coder + Tester, loops until acceptance criteria pass. | Required. Raises quality 65% → 92% (SWE-Bench). |
| **Coder Agent** | Implements one features.yaml row. Loads only: architecture.md + its row + touched files. | Incremental only — no rewrites. |
| **Tester Agent** | Runs tests, flags failures with explanations. | Separate from Coder for isolation. |

**The orchestrator is a script, not an agent.** Do not over-engineer the coordination layer.

---

## 5. Red Team & Judgment Patterns

### Judge Agent Pattern (Non-Optional in Production)

- PwC: 7x accuracy improvement (10% → 70%) with structured validation loops
- STRATUS: 1.5x improvement via independent validation
- Hallucination reduction: -40%
- **Rule: If deploying to production, a Judge Agent is not optional.**

### Multi-Model Voting (EnsLLM)

- 3 models: $0.06/task, +6.7% accuracy
- 5 models: $0.10/task, +8.0% accuracy (diminishing returns after 3)
- Method: parallel generation → CodeBLEU similarity → CrossHair differential → consensus
- When to trigger: error cost > 100x generation cost, complexity > 8/10

### Scope-Calibration-First for Reviews

Before critiquing any document or output, first ask: what is this *trying to be*? Research survey? Implementation handbook? Prototype? Then assess against that stated goal — not a different one. Prevents severity inflation and scope confusion.

### Quality Rubric

| Level | Definition | Max per document |
|-------|-----------|-----------------|
| FATAL | Fails stated purpose entirely, incorrect, or dangerously outdated | Max 2 |
| HIGH | Major omission that blocks intended use | Unlimited |
| MEDIUM | Structural gap that degrades but doesn't block | Unlimited |
| LOW | Styling, formatting, minor polish | Unlimited |

### Property-Based Testing (for Non-Deterministic Agents)

Test *properties*, not exact outputs:
- Idempotence: same input → similarity > 0.95
- Monotonicity: more context must not degrade quality
- 50 intents × 10 personas = 500 scenarios before edge cases

---

## 6. Error Recovery

### Traditional Circuit Breakers Fail for Stateful Agents

They were designed for stateless microservices. Agents hold state, reason across turns, and require different recovery semantics.

### Recovery Patterns

| Pattern | When to Use | Mechanism |
|---------|-------------|-----------|
| **Saga** | Multi-step workflows with side effects | All agents rollback together. 60% faster than local-only (Galileo AI). |
| **Circuit Breaker** | Independent parallel workers | Individual retry with exponential backoff. |
| **Adaptive Backpressure** | Downstream can't keep up | Rate-limit upstream based on queue depth. |
| **Checkpoint-Restart** | Long-running tasks | Checkpoint state BEFORE execution. Restore on failure. Interval: every 5 min. |
| **Sub-Boss Re-spawn** | One module fails | Re-run only that module's Sub-Boss (5-20 min), not the whole project. |

### Mandatory Production Rules

- **90% of AI agents fail within 30 days** in production (Substack survey, 2025). Production hardening is not optional.
- **Human escalation gates required** in regulated domains. McDonald's drive-through shutdown: no fallback. MD Anderson $62M loss: no human review gate.
- **Always maintain a manual override path.**

---

## 7. Context Management Over Long Runs

### Core Rules

- **Effective window: stay under 256K tokens** regardless of model's stated limit
- **Each coding session: <15K tokens** after PM-Init (modularity enforces this)
- **architecture.md ≤ 4 pages** or agents drift
- **Middle curse confirmed:** relevant content in the center of long contexts loses ~20-50% retrieval accuracy. Put critical data at start/end.
- **Delta updates over full rewrites** in long sessions (ACE paper: +10.6% AppWorld)
- **Never glob-read entire codebases.** Pass file paths; let agents read selectively.

### Anthropic's Four-Step Framework

**Write → Select → Compress → Isolate.** Apply in that order. JIT retrieval: fetch relevant context only when needed, not upfront.

### Memory Architecture for Long-Horizon Projects

| Layer | Scope | Implementation |
|-------|-------|---------------|
| Short-term | Current session | In-context window |
| Working memory | Cross-session state | File system (brain files) or Redis |
| Long-term | Knowledge base | Vector DB + graph links |

A-Mem (Zettelkasten for agents, NeurIPS 2025): +114% on LongMemEval vs baseline. Atomic notes → embedding links → graph expansion on retrieval.

### Session Discipline

- **6 × 3-4h modules > 1 × 20h session.** Quality collapses to ~11% of target at hour 10 of a single session.
- **Parallel creation, sequential review.** Agents create simultaneously; review happens one module at a time.
- **Lock-and-advance:** Once a module receives approval, it is not revisited unless integration conflict. Prevents endless refinement.

---

## 8. Anti-Patterns & Reality Checks

### The Benchmark vs. Reality Gap

| Benchmark | Score | Reality |
|-----------|-------|---------|
| SWE-bench Verified (public) | 77.2% (Claude Sonnet) | — |
| SWE-bench Pro (private repos) | **23%** (Scale AI 2025) | Real codebases are 3.3x harder |
| AppWorld | 86.7% failure rate | Production ≠ benchmarks |
| ChatDev correctness | 33.3% on some benchmarks | — |

**Never cite Verified scores as production reliability indicators.**

### Technology Reality Checks

**LatentMAS** (arXiv:2511.20639) — 70-84% token savings are real BUT:
- Works ONLY within Qwen model family (requires hidden state access via HuggingFace + vLLM)
- Claude/GPT APIs do NOT expose hidden states → incompatible with commercial API models
- Any claim of LatentMAS with Claude+GPT is wrong

**CodeCRDT** (arXiv:2510.18893):
- Complex tasks (>500 LOC): +21.1% speedup, 100% convergence
- Simple tasks (<200 LOC): -39.4% slowdown. Use only when complexity justifies overhead.

**Apple "Illusion of Thinking"** (2025):
- Frontier models show >80% accuracy collapse above compositional complexity threshold
- Models *reduce* thinking effort on harder tasks (counter-intuitive scaling limit)
- Implication: Always decompose highly compositional tasks. Never rely on internal reasoning alone for critical paths.

### What Kills Autonomous Projects

- **No external memory** — agents repeat errors, lose context, declare premature success
- **>10 agent types** — coordination overhead exceeds value
- **Placeholders masquerading as deliverables** — "will be covered later" means never
- **Full history in every prompt** — balloons cost 80%+, hits context limits
- **No Sub-Boss quality gate** — solo coder = 65% quality
- **Treating orchestrator as AI** — it's a while-loop script
- **No changelog** — impossible to debug at scale
- **Vague features.yaml rows** — if acceptance criteria aren't specified, the coder invents them
- **Over-promising scope** — 20,000-word document attempted in one session delivered 2,231 words (11%)

---

## 9. Cost Architecture

### Stacking Discounts

| Technique | Savings |
|-----------|---------|
| Prompt caching (system field) | 90% on cache reads |
| Batch API | 50% discount |
| Combined | ~95% off repeated content |

### Model Assignment (Cost-Optimized)

| Task | Model | Rationale |
|------|-------|-----------|
| Architecture/planning | Opus or Sonnet | Best reasoning for synthesis |
| Implementation | Sonnet (default) or local model | Sonnet = 79.6% SWE-bench, best value |
| Testing | Sonnet or Haiku | Mechanical validation |
| Review / Judge | Sonnet | Structured critique |
| Classification / sorting | Haiku | 3x cheaper, sufficient for mechanical work |

### Project Cost Estimates

- Simple prototype (50 modules): $50-100
- Medium app (200 modules): $200-400
- Enterprise MVP (500 modules): $400-600 (Sonnet), $600-1200 (Opus)
- Multi-model voting per task: $0.06 (3 models), $0.10 (5 models)

---

## 10. Prompt Engineering for Agents (2025+ Rules)

### What Changed

- **Explicit CoT hurts on reasoning models** — degrades performance, adds 20-80% latency
- **Temperature ~1.0 outperforms 0** for complex reasoning — enables multi-path hypothesis exploration. Use 0 only for structured execution.
- **Native structured outputs ~100% compliance** vs prompt-based ~70-90%. Always use API-level schemas.
- **Parallel tool calling** improves multi-step success rate ~15-20%. Use by default.
- **>20-50 tools without search mechanism** degrades selection accuracy. Use Tool Search.

### Validated Prompt Order

Context → Role → Goal/Task → Constraints → Output Format

"Anchor reasoning in data first, instructions last."

### Model-Specific Structuring

| Model | Preferred Format | Note |
|-------|-----------------|------|
| Claude | XML tags | +15-20% grounding, +20-50% recall on long context |
| GPT | Minimal JSON / schema | Direct tasks |
| Gemini | Markdown headings | Deep Think for complex |
| Grok | Bullet points | Minimal + tool hints |

Exception: Context under 10K tokens — plain text is fine for any model.

### Agent Role Incompatibility Pairs (Never Combine)

- Critic + Creative Writer (conflicting tone)
- Planner + Creative Writer (structure vs creativity)
- Data Scientist + Creative Writer (rigor vs creativity)
- Legal Advisor + Creative Writer (caution vs creativity)
- Any critical role + Customer Support (hard critique vs soft tone)

---

## 11. Quality Checklist (Non-Negotiable per Module)

Before treating any agent output as complete:

1. Every claim has a URL/DOI or source reference
2. Numbers, not "significantly" — quantify everything
3. Both benefits AND limitations shown for every pattern
4. Decision tree: when to use AND when NOT to use
5. Code examples run without modification
6. No placeholders ("will be covered later" = not done)
7. Machine-verifiable completion criteria (word counts, test pass rates, not vibes)

Self-validation gate: verify 3 random claims, run 2 code examples, count cross-references, confirm every benchmark cites source. Required: 9.8/10 minimum.

---

## 12. Future-Proofing: New Model Integration Protocol

When a new frontier model ships, evaluate within 1 week:

1. **Baseline:** Context window, reasoning API, tool use architecture, structured output support
2. **Validate (20-50 samples each):**
   - Does minimalism still win? (vs verbose prompts)
   - Preferred format? (XML vs headings vs JSON)
   - Temperature sweet spot for reasoning
   - Tool decision autonomy sufficient?
   - Reflection/error recovery strength
   - Compositional complexity ceiling (Apple "Illusion of Thinking" test)
   - Cost/latency profile
3. **Integrate:** Update capability matrix, update warm packs, version the change

---

## Quick Reference: Decision Trees

### "Should I add more agents?"
```
Can 1 agent do it?           → Yes → Don't add agents
Need quality gate?            → Add Judge Agent (always worth it)
Need parallel execution?      → Add Sub-Boss per module
Need different expertise?     → Add specialist (max 5-7 total)
Considering >10 agents?       → You're over-engineering. Stop.
```

### "How should I decompose this project?"
```
<50 features   → Single features.yaml, 1 PM-Init pass
50-200 features → Group into modules of 10-20, parallel Sub-Bosses
200-600 features → Two-phase: Architecture Crew + Coding Harness
>600 features  → Split into sub-projects with separate architecture.md each
```

### "Which recovery pattern?"
```
Side effects (DB, API calls)?     → Saga (coordinated rollback)
Independent workers?              → Circuit Breaker (local retry)
Downstream bottleneck?            → Adaptive Backpressure
Long-running (>30 min)?           → Checkpoint-Restart (every 5 min)
One module failed?                → Re-spawn Sub-Boss only
```

---

---

## 13. Production Harness Patterns (Anthropic Nov 2025 + Cursor Jan 2026)

Two primary sources validated in practice at scale. Added session 71 — mined from actual blog posts.

### Anthropic Initializer-Coder Pattern (Nov 2025)
URL: anthropic.com/engineering/effective-harnesses-for-long-running-agents

**Two-agent decomposition (same agent, different initial prompts):**
- **Initializer** — runs once. Creates: `init.sh`, `claude-progress.txt`, `feature_list.json`, initial git commit
- **Coding agent** — runs every subsequent session. Reads handoff files → picks one failing feature → implements → commits → updates progress log

**Session startup protocol (exact order matters):**
1. Run `pwd` — confirm working directory
2. Read `claude-progress.txt` + git logs — understand prior work
3. Read `feature_list.json` — identify highest-priority failing feature
4. Run `init.sh` — start development server
5. Run baseline end-to-end test — before writing any new code
6. Implement one feature only

**feature_list.json design choices:**
- JSON over Markdown — models less likely to inappropriately modify JSON
- Each feature has: category, description, step-by-step test instructions, `passes: false/true`
- Agents may ONLY edit the `passes` field — everything else is locked
- The rule given to agents verbatim: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality"

**Failure modes without this structure (documented):**
1. Over-ambition: agents one-shot the entire app, run out of context mid-implementation, leave undocumented fragments
2. Premature completion: later agents see completed features and declare job finished without addressing remaining work
3. Marking done without testing: code changes + unit tests ≠ working feature. Fix: Puppeteer MCP for browser-native end-to-end testing

**git as continuity mechanism:** `git log` tells new agents what happened. Agents revert bad changes and recover via git. "This increased efficiency by eliminating guesswork about prior work."

### Cursor Planner-Worker-Judge Architecture (Jan 2026)
URL: cursor.com/blog/scaling-agents | Author: Wilson Lin

**Why flat coordination fails (documented failure modes):**
1. Lock contention: 20 agents → throughput of 2-3. Optimistic concurrency fixes locking but not the deeper problem
2. Risk aversion: without hierarchy, agents avoided difficult tasks and made small, safe changes. No one took ownership of hard problems
3. Work churned without progress — activity without outcomes

**Planner-Worker-Judge roles:**
- **Planner:** Continuously explores codebase + creates tasks. Can spawn sub-planners recursively — planning itself is parallelized
- **Worker:** Picks up one task, focuses entirely on it. No big-picture awareness, no coordination with other workers. Grinds until done, then pushes
- **Judge:** Evaluates cycle output. Decides continue or restart. Restarts fresh with a new agent — this is THE critical property

**Judge restart = critical property:** Fresh context at each Judge cycle prevents drift and tunnel vision. Periodic clean restarts are designed-in, not a failure mode.

**Scale validated in production:**
- Web browser in Rust: ~1 week, 1M+ lines, 1,000 files
- Solid→React migration: 3 weeks, +266K/-193K edits, passed CI
- Java LSP: 7.4K commits, 550K LoC | Excel clone: 1.6M LoC

**Key principles from Cursor's experience:**
1. "Many improvements came from removing complexity rather than adding it" — they built an integrator role for conflict resolution, it created more bottlenecks than it solved, removed it
2. "A surprising amount of the system's behavior comes down to how we prompt the agents" — harness and models matter, but prompts matter more
3. Too little structure → conflicts, duplicate work, drift. Too much → fragility. Right amount = minimum viable hierarchy.

**Model choice for long-horizon tasks (Cursor's finding):**
"GPT-5.2 models excel at extended autonomous work: following instructions, maintaining focus, avoiding drift, implementing things precisely and completely. Opus 4.5 tends to stop earlier and take shortcuts when convenient, yielding control quickly."
→ For Claude-only systems: use Sonnet for long-running execution, not Opus. Aligns with model-strategy.md.

### Hybrid Handoff Pattern (DD3 resolved — Grok spar session 71)

Pure JSON fails for hybrid business outputs (strategy documents, negotiation packages, B2B presentations). Pure Markdown loses parse reliability for structured data. Resolution:

- **JSON core:** structured data that agents process programmatically (schemas, feature lists, acceptance criteria, status fields, `passes: true/false`). Models less likely to inappropriately modify. Use JSON here.
- **Markdown supplement:** narrative, strategy content, evolving context (negotiation summaries, discovery findings, B2B deck briefs). Use MD alongside the JSON core. Informational — agents read it, don't parse it.
- **Validate at handoff boundary:** auto-check that JSON fields are present and correctly typed before passing to next agent. MD supplement is advisory — not programmatically required.
- **When to deviate:** coding-only pipelines → pure JSON (Anthropic recommendation holds). Strategy/presentation pipelines → hybrid. Never pure Markdown for agent-to-agent handoffs with structured status fields.

### Cross-Source Convergence (Anthropic + Cursor + METR)

Three independent findings that reinforce each other:
1. **Structure compensates for agent cognitive limits.** Anthropic: progress files + JSON feature lists. Cursor: hierarchy eliminates risk aversion. METR 2503.14499: agents fail in "messy environments without clear feedback loops."
2. **Removing complexity is a form of improvement.** Cursor: integrator role removed. Anthropic: single agent per session vs multi-agent. METR: improvements came from greater reliability (fewer wrong things), not more features.
3. **Handoffs are the key design problem.** Anthropic: `claude-progress.txt` + git log = shift handoff. Cursor: Judge restart = planning cycle handoff. METR: measures the cost of unsolved handoff problem in task horizon time.

---

*Compiled from 13 research conversations (Dec 2025) + Anthropic harness post (Nov 2025) + Cursor scaling agents post (Jan 2026) + METR arXiv 2503.14499 (Mar 2025). Key sources: MetaGPT (arXiv:2308.00352), ChatDev (arXiv:2307.07924), HALO (arXiv:2411.15339), AgentCoder (arXiv:2312.13010), EnsLLM (arXiv:2503.15838), A-Mem (arXiv:2502.12110), ACE (arXiv:2510.04618), LatentMAS (arXiv:2511.20639), CodeCRDT (arXiv:2510.18893), Apple "Illusion of Thinking" (2025), SWE-bench Pro (Scale AI 2025), PwC Judge Agent study.*
