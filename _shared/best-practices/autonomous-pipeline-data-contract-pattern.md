---
name: autonomous-pipeline-data-contract-pattern
description: Before launching ANY multi-wave subagent pipeline, write a shared data contract (PRICING-MASTER.json + PRODUCT-BRIEF.md) that all subagents read. Prevents pricing hallucination and cross-document contradictions.
type: feedback
tier: A
source: patrick + Grok + Gemini unanimous (S231)
created: 2026-04-15
---

# Autonomous Pipeline: Data Contract Pattern

## Rule
Before launching ANY multi-wave subagent build pipeline, the orchestrator MUST write a shared data contract. All subagents read from it. No subagent infers facts from prose.

**Why:** Sequential subagents in a pipeline compound errors multiplicatively. At 85% quality per wave, a 4-wave pipeline has P(final correct) ≈ 0.52. A shared data contract breaks the error chain at the source.

**How to apply:**
1. Orchestrator writes `PRICING-MASTER.json` (all numbers, dates, rates) before Wave 1
2. Orchestrator writes `PRODUCT-BRIEF.md` (≤500 words, injected into EVERY subagent prompt verbatim)
3. All subagents prohibited from inventing facts — "read from PRICING-MASTER.json only"
4. If conflict found during gate check: PRICING-MASTER.json is the tiebreaker

## Structural Gate Checks (not self-reported manifests)
Replace `MANIFEST.json` written by the subagent with orchestrator-side validation:
- File exists AND size > minimum threshold
- Required strings present (pricing figures, contact email, key dates)
- Seal language violation check (domain-specific but generalizable: prohibited phrases)

Self-reported completion is always theater. The subagent writes "complete" when it runs out of turns, not when the output is correct.

## Progressive Commits
Never wait for the full pipeline before first git commit. Commit after EACH wave gate passes. If Wave 4 fails completely, Waves 1-3 are already committed and recoverable.

## Wave Isolation
Parallel wave agents must write to separate output dirs (wave-1a/, wave-1b/) — never shared write targets. Aggregation happens at the orchestrator level after both complete.

## Source
- Grok+Gemini spar: 2026-04-15, unanimous on all 4 fixes
- Applied in: SESSION-BRIDGE-S237-ARCTIC-ORCHESTRATOR-V2.md
- Spar results: _external_intel/validation/GEMINI-arctic-pipeline-orchestrator-spar-20260415.md
