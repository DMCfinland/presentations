# Model Strategy: Right Model for the Right Task
<!-- last_updated: session-40 | Opus review contradiction fix. Body rewritten to match CLAUDE.md Tier A. -->

**Philosophy:** Sonnet 4.6 is the default for everything. Opus only for GPQA-level expert reasoning where it uniquely wins (91.3% vs 74.1%). The old "Opus for strategy, Sonnet for execution" framing is obsolete.

---

## Pricing (Corrected — session-39)

| Model | Input | Output | Batch | Context |
|-------|-------|--------|-------|---------|
| **Opus 4.6** | $5/MTok | $25/MTok | $2.50/$12.50 | 1M |
| **Sonnet 4.6** | $3/MTok | $15/MTok | $1.50/$7.50 | 200K (1M beta) |
| **Haiku 4.5** | $1/MTok | $5/MTok | $0.50/$2.50 | 200K |

**Ratio: Opus = 1.67× Sonnet.** (Was 5×. Obsolete "Opus is 5× more expensive" rule is DEAD.)

---

## Benchmark Reality (2026-02-21)

| Benchmark | Sonnet 4.6 | Opus 4.6 | Winner |
|-----------|-----------|---------|--------|
| Coding (SWE-bench) | 79.6% | 80.8% | **Tie** |
| Computer use (OSWorld) | 72.5% | 72.7% | **Tie** |
| Office productivity (GDPval-AA) | **1633 Elo** | 1606 Elo | **Sonnet** |
| Financial analysis | **63.3%** | 60.1% | **Sonnet** |
| Expert reasoning (GPQA) | 74.1% | **91.3%** | **Opus** |

**Key implication:** Opus uniquely wins on GPQA (expert reasoning chains). Everything else — Sonnet matches or beats it.

**Sonnet 4.6 advantages:** Adaptive thinking (built-in automatic reasoning depth), 1M context (beta), better at financial analysis and office work.

---

## Decision Framework

### Use OPUS when:
- ✅ **GPQA-level reasoning required:** Multi-hop deductive chains, cross-source legal synthesis, scientific analysis
- ✅ **Opus reviews themselves** — every 10-session system health audit
- ✅ **Governance synthesis** — Finnish corporate law compliance, board-level legal accuracy (liability risk if wrong)
- ✅ **True needle-in-haystack WITH reasoning** — finding and synthesizing across disparate sources simultaneously

### Do NOT use Opus for:
- ❌ Strategic planning → Sonnet
- ❌ Architecture decisions → Sonnet
- ❌ Quality review → Sonnet
- ❌ Financial analysis → Sonnet (actually beats Opus: 63.3% vs 60.1%)
- ❌ Coding/scripting → Sonnet
- ❌ "Important" or "high-stakes" work (unless it also requires GPQA reasoning)
- ❌ Large corpus retrieval (Sonnet has 1M context beta — same window as Opus)
- ❌ **Long-horizon agentic execution** → Sonnet. Cursor Jan 2026 finding: "Opus 4.5 tends to stop earlier and take shortcuts when convenient, yielding control quickly." GPT-5.2 and Sonnet both outperform Opus 4.5 on extended autonomous runs. Opus conserves tokens by stopping — exactly wrong for long-running tasks.
  - ⚠️ **DD2 CONTESTED (Grok spar 2026-03-12, unverified):** Cursor finding was Opus **4.5**-specific. Grok spar surfaced unresolved conflict: Harper cites 2026 agentic reviews favoring Sonnet; Lucas cites Opus 4.6 Terminal-Bench and Elo gains as evidence behavior changed. Specific benchmarks (Terminal-Bench 65.4%, 190 Elo gains) NOT independently verified. **Rule stays: Sonnet default.** Revisit at session 80 Opus review with verified Opus 4.6 long-horizon benchmarks.

### Use SONNET for (default — everything except the above):
- ✅ All coding, scripting, file operations
- ✅ Strategic planning, roadmaps, recommendations
- ✅ Research synthesis, analysis, summarization
- ✅ Building prompts, custom instructions, documents
- ✅ Excel analysis, financial modeling
- ✅ Mining output organization
- ✅ Large corpus work (1M context beta)
- ✅ Any session where "Opus" is not clearly justified

### Use HAIKU for:
- ✅ Bulk classification, tagging, categorization
- ✅ Simple field extraction at scale
- ✅ Format validation (does this meet criteria?)
- ❌ Never for extraction quality, creative, or judgment work

---

## Decision Tree

```
START: New Task
    │
    ├─ Requires GPQA-level expert reasoning?
    │  (Multi-hop deductive chains, cross-source legal synthesis)
    │  YES → OPUS 4.6
    │  NO → Continue
    │
    ├─ Is this a governance/legal synthesis task with liability risk?
    │  YES → OPUS 4.6
    │  NO → Continue
    │
    ├─ Is this a system Opus review?
    │  YES → OPUS 4.6
    │  NO → Continue
    │
    └─ Everything else (strategy, analysis, coding, planning, research)
       → SONNET 4.6 (default)
           │
           └─ Simple, high-volume classification/tagging?
              → HAIKU 4.5
```

---

## Subagent Delegation Threshold

When running AS Opus: spin up Sonnet subagents for execution work of 3+ tool calls.
- Rationale: Even at 1.67× pricing, context isolation + parallel execution > cost of Opus doing sequential tool work
- For <3 calls: Opus can execute directly (overhead not worth it)

---

## 1658 Holdings Use Cases

| Task | Model | Why |
|------|-------|-----|
| File organization, scripts | Sonnet | Execution work |
| Financial analysis | Sonnet | Actually beats Opus here |
| Strategic planning, roadmaps | Sonnet | Benchmarks show equal/better |
| Research synthesis | Sonnet | Equal to Opus; much cheaper |
| Board materials, presentations | Sonnet | Office productivity: Sonnet wins |
| Mining output organization | Sonnet | Execution work |
| Governance/legal synthesis | Opus | Liability risk + GPQA needed |
| Opus 10-session system review | Opus | Meta-task by design |
| Finnish OYL compliance audit | Opus | Multi-hop legal reasoning |
| Excel extraction, budget analysis | Sonnet | Financial analysis: Sonnet wins |
| Custom instructions build | Sonnet | Implementation work |

---

## Hybrid: When Opus Orchestrates

When running an Opus review (sessions 40, 50, 60…):
- Opus designs the analysis and makes architectural calls
- Sonnet subagents run execution work (file reads, searches, report writing)
- Opus synthesizes and makes decisions

This pattern saves ~40% vs Opus doing all tool calls.

---

## Cost Benchmarks

| Task | Model | Approx. Cost |
|------|-------|-------------|
| Single analysis/synthesis | Sonnet | $0.05–0.20 |
| 196-video batch extraction | Sonnet (Batch API) | $1.89 |
| Governance synthesis (3 Opus prompts) | Opus (Batch API) | ~$1 |
| Opus 8-step system review | Opus | $1–2 |
| Parallel 4-subagent research | Sonnet × 4 | $0.20–0.80 |

---

## What Changed (vs previous version)

**Previous model-strategy.md said:** "Use Opus for strategic decisions, deep research, planning, high-stakes, recommendations, M&A, board prep."

**Why that was wrong:** Sonnet benchmarks EQUAL Opus on strategic work, BEATS Opus on financial analysis and office productivity. The old framing was based on intuition and pre-4.6 model gaps that no longer exist.

**Patrick's updated rule:** "Sonnet for doing AND deciding. Opus only for legal synthesis or when you need GPQA-level expert chains. When in doubt, Sonnet."

source: claude.md-tier-a (session-39, confirmed session-40 review)
