# Long-Running Near-Oneshot Task Design
<!-- source: Grok 4.20 Research Debate session 71 (Run 7) | session: 71 -->
<!-- created: 2026-03-12 | confidence: 0.7 | tier: B -->
<!-- context: CEO portfolio use case, 10 companies, 2-3 sessions/week, heterogeneous task types -->

**What:** 5-layer architecture for tasks where a human specifies work once, frontloads all judgment upfront, and receives a complete result without mid-task interruption. Generalizes across coding builds, strategy documents, negotiation packages, and B2B presentations.

**Why:** CEO time is the binding constraint. Frontloaded attention + right harness structure = more valuable output per unit of Patrick's time. The goal is genuine near-oneshot completion, not theater of autonomy.

**When to apply:** Any complex task lasting >60 minutes, spanning multiple subagents, or requiring cross-session continuity. See `lead-agent-quality-gate.md` for the gate architecture that runs within this framework.

---

## The 5 Layers

### [Specification Layer]
**Best practice:** Immutable core spec artifact persisted as a structured file from structured intake (goal + exhaustive DONE criteria + constraints + output format + tier + escalation triggers). Add exactly one controlled refinement gate where Lead Agent can propose sub-criteria elaborations with logged rationale — Judge validates before accepting.

**Known failure modes:**
- Over-rigid upfront criteria on discovery-driven tasks (municipal negotiations, strategic pivots) → Judge rejects all 3 rounds against criteria that no longer fit reality → forced suboptimal output
- Spec drift without logging → original intent lost by round 3

**Frontier practice:** Treat spec as a self-updating contract — Lead can elaborate sub-parts inside guardrails. Temporal workflows embed spec checkpoints so refinement is atomic and auditable.

**Resolves:** DD5 (upfront-only acceptance criteria infeasible for Tier 3 discovery tasks)

---

### [Handoff Layer]
**Best practice:** Hybrid JSON/MD protocol.
- **JSON core:** structured data agents process programmatically — schemas, feature lists, acceptance criteria, status fields. Models less likely to inappropriately modify.
- **Markdown supplement:** narrative content — negotiation summaries, discovery findings, B2B deck briefs, strategy context.
- **Validate at handoff boundary:** auto-check JSON fields present and typed before passing to next agent. MD supplements are informational — not programmatically required.

**Known failure modes:**
- Pure JSON for hybrid business outputs → schema-evolution breaks when strategy content evolves; lost nuance in negotiation/B2B contexts
- Pure MD for structured data → parse errors, agents modify fields they shouldn't

**Frontier practice:** MCP/A2A contracts declaring exact inputs/outputs per agent. Auto-converter between JSON and MD representations.

**Resolves:** DD3 (JSON vs Markdown — neither wins alone)

---

### [Memory Layer]
**Best practice — highest ROI layer:** Hierarchical persistent memory for 2-3 sessions/week cadence:
1. **Structured rejection summaries** (between rounds): Lead writes ≤500-word file after each rejection: what was tried, exact failure reason, domain model snapshot. Fresh agents read this at spawn. No full context carry — no anchoring bias.
2. **Session checkpoints** (for tasks >60 min): atomic flat-file summary every 30-60 min. Keys: decisions made, discovered constraints, domain model state, what's left.
3. **Cross-session blackboard** (for multi-week portfolio tasks): persistent file keyed by company/project ID. Contains: stakeholder maps, negotiation constraints, schema versions, strategy branches. Survives between 2-3 session/week cadence.

**Known failure modes:**
- Full context carry across rounds → anchoring bias, same wrong approach repeated (context rot)
- Full fresh wipe in long-horizon tasks → identical dead-ends re-triggered across sessions; re-discovering same domain knowledge each time → token explosion
- No cross-session memory → every session starts cold on portfolio state that took 5 sessions to build

**Frontier practice:** Temporal durable checkpoints, LangGraph state machines with explicit undo boundaries, /memories directories.

**Resolves:** DD1 (fresh restart vs state continuity — selective carry is the compromise)

**Implementation note for our system (current):** Claude Code's `claude-progress.txt` + git log pattern (Anthropic Nov 2025) IS the session checkpoint for coding projects. For non-coding tasks (strategy, negotiation, B2B), equivalent is a `[project]-progress.md` file updated at each major decision point.

---

### [Escalation Layer]
**Best practice:** LLM-as-Judge with calibrated confidence thresholds + **explicit non-technical escalation triggers** for CEO use case. Technical thresholds alone miss business judgment calls.

**Non-technical escalation triggers (add to structured intake):**
- Strategy risk score exceeds threshold (e.g., commits to irreversible positioning)
- Political/stakeholder ambiguity not in original constraints (e.g., new municipal stakeholder discovered)
- External pricing or market condition contradicts original assumptions by >20%
- Action requires Patrick's unique context, risk appetite, or creative synthesis (these sessions are Tier 3 by definition — autonomous execution there is value-destroying)

**Known failure modes:**
- Technical-only triggers → agent hallucinates optimistic assumptions to meet criteria while Judge loops restarts; CEO receives risky completed output unaware
- Over-escalation → defeats purpose of near-oneshot (every uncertainty triggers a CEO question)

**Resolves:** Partially addresses all DDs — prevents over-autonomy in heterogeneous CEO portfolio tasks

---

### [Economics Layer]
**Best practice:** Hard per-session token budgets + early-stop on diminishing returns.
- Set budget at intake: expected cost + 50% buffer
- Progressive rejection penalties: round 1 = full retry; round 2 = narrowed scope; round 3 = escalate to Patrick with reason log
- Early-termination condition: if Judge observes N tokens spent with no progress on acceptance criteria → escalate rather than exhaust budget

**Known failure modes:**
- 3 fresh restarts × high-horizon tasks with no budget cap → Cursor-scale token burn ($1M+ on incomplete output)
- No integration-test layer in Judge → coordination/integration gaps invisible until output is delivered

**Frontier practice:** Per-tier budget caps with auto-downgrade (reduce scope, not model). Integration-test layer in Judge for multi-file/cross-agent outputs.

**Resolves:** DD4 (one-feature-per-session too conservative) — dynamic chunk sizing with budget guardrails replaces rigid rule

---

## Priority Ranking (Grok consensus, unanimous)

1. **Memory Layer** — highest ROI. Cross-session continuity is the #1 production failure vector for 2-3 session/week CEO portfolio work. Without it, every session rediscovers state that took hours to build.
2. **Specification Layer** — table stakes. Without refinement gate, Tier 3 tasks fail or loop.
3. **Handoff Layer** — table stakes. Hybrid JSON/MD prevents integration failures at agent boundaries.
4. **Economics Layer** — mandatory co-implementation with Memory. Without budget caps, rejection loops burn tokens at Cursor scale.
5. **Escalation Layer** — safety net. Prevents over-autonomy but doesn't generate value directly.

---

## Resolved Design Decisions (DDs from Grok spar)

| DD | Resolution | Confidence |
|----|-----------|-----------|
| DD1: Fresh restart vs state continuity | Selective carry via structured rejection summaries. Fresh agent + summary file at spawn. | High — structurally sound |
| DD3: JSON vs Markdown | Hybrid: JSON core (structured data) + MD supplement (narrative). Validate JSON at handoff boundary. | High — structurally sound |
| DD5: Upfront criteria only | Refinement gate for Tier 3: Lead proposes sub-criteria elaborations, Judge validates. | High — structurally sound |
| DD4: One-feature-per-session | Dynamic chunk sizing. Scope = interdependency unit, not always single feature. Budget guardrails replace rigid rule. | Medium — valid logic |
| DD2: Sonnet vs Opus for long-horizon | Unresolved. Sonnet default maintained. Opus 4.6 long-horizon benchmarks contested but unverified. | Low — verify at session 80 |

---

**Source:** Grok 4.20 Heavy Research Debate (Run 7, session 71, 2026-03-12). Agents: Harper (web research), Benjamin (cost analysis), Lucas (adversarial). Verified sources: Cursor Jan 2026 blog, Anthropic Nov 2025 harness post, METR arXiv 2503.14499. Contested/unverified: Opus 4.6 Terminal-Bench 65.4%, arXiv 2503.13657, DAIR.AI 74% figure, arXiv 2512.08296 coordination degradation.
