---
name: 5-Agent Research Wave Architecture
description: Multi-domain research pattern using parallel task subagents in two waves with briefing flag handoff. Validated on transcript pipeline research (S111).
type: feedback
---

Use wave architecture for comprehensive multi-domain research (5+ topics, cross-dependencies):

**Wave 1 (parallel, no dependencies):** 3 agents covering independent domains simultaneously.
**Briefing flag:** Lead writes `BRIEFING-WAVE-1-COMPLETE.md` after Wave 1 — critical findings, conflicts, inputs for Wave 2.
**Wave 2 (parallel, depends on Wave 1):** 2 agents that need Wave 1 outputs. Read briefing flag before starting.
**Synthesis:** Lead reads all 5 outputs, resolves conflicts, writes final spec.

**Why task subagents (NOT Agent Teams):**
Non-overlapping targets per wave → no real-time debate needed → 3-4× cheaper. Agent Teams only if agents analyze THE SAME thing from different angles simultaneously.

**Cost:** 5 Sonnet agents ~$8-10 total. ~20-30 min total.

**Acceptance criteria per agent (mandatory):** 5 PASS/FAIL binary criteria, not "quality review." Same-model Judge = theater — validate criteria are binary and testable.

**Why:** S111 validated this pattern. All 5 agents PASS. Synthesis caught 4 cross-agent conflicts that individual agents missed.

**When to apply:** Any research task with 4+ independent domains that feed into one deliverable (architecture spec, strategy doc, system design).

**Source: S111 (2026-03-25)**
