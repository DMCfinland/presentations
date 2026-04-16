# Phase System — Grok Architecture Review (2026-04-01)
**Model:** Grok Auto (spar mode)
**Source prompt:** T2: ARCH_STRESS — Kill Vector Analysis on 5-phase protocol
**Chat URL:** https://grok.com/chat?rid=10854cca-87da-4d15-a723-9ebf934530c7

---

## Kill Vector 1: Real-usage breakdown
Sessions overrun because discovery leaks into research, research uncovers plan-breaking facts, and execution hits edge cases. Hard gates are theater — Claude cannot physically stop a session. Multi-LLM hand-off summaries degrade. After 2 projects, "LLM loop fatigue" causes copy-paste of previous output.

## Kill Vector 2: Session overrun across phase boundary
Phase N overruns → Phase N+1 starts with previous phase still "in progress". Hard gate enforcement = checking a markdown file. Claude may hallucinate "previous phase verified". Contamination compounds across 3+ consecutive phases.

## Kill Vector 3: Tier-gated review realism
Tier 1 self-critique = wishful thinking. Claude's self-critique is superficial. Tier 3 is so heavyweight nobody invokes it. Result: 80% of work gets weakest review. "Risk-avoidance theater."

## Kill Vector 4: Verify command friction
VALIDATION.md is cargo-cult for non-deterministic/creative tasks (SEO, copywriting, governance). Verify commands devolve into `wc -l` or `find | grep` that prove existence, not correctness. People mark tasks done when file appears.

## Kill Vector 5: Warm-pack template decay by project 3+
Missing: context rot detection, version audit trail of which LLM edited, drift-detection. By project 4 the warm-pack is a Frankenstein document.

## Kill Vector 6: Multi-track concurrency (JYS: SEO + photo library)
Shares same VALIDATION.md, same phase gates, same session history. No locking, no dependency graph, no inter-track sync. Claude will reference image filenames that don't exist yet.

## Kill Vector 7: Command-design anti-patterns
"Run verify command from VALIDATION.md" trains Claude to treat commands as sacred. Results in: (a) hallucinated execution, (b) wasted time on irrelevant shell commands, (c) refusal to progress on external failures.

## VERDICT
Critical flaw: religious faith in session-isolated hard gates and LLM self-policing. AI agents are stochastic, not stateful microservices.

**Proposed alternative:** Collapse 5 phases → 3 live artifacts (Intent, Blueprint, Delivery) edited in-place. Human sign-off + automated diff audit. Kill tiered self-critique; every project >$200 gets one Grok + one Gemini check. Explicit dependency graph. Delete "self-critique" from vocabulary.

---

## Response Assessment (Claude's analysis)

**Valid points to act on:**
- KV2: Phase boundary overrun is real — need explicit "carry-over" protocol
- KV3: Tier 1 self-critique weakness is real — fixed by making Expert-model Grok optional but recommended
- KV6: Multi-track was unhandled — FIXED in S146 (added Tracks section + per-track PLAN/VALIDATION files)
- KV5: Warm-pack versioning via `<!-- last_updated -->` header exists but lacks diff audit

**Overstated/wrong:**
- KV1: "LLM loop fatigue" and "people copy-paste" — this is a 1-person operation (Patrick), not a team workflow
- KV4: Verify commands for CRM (SQL queries) are genuinely useful; creative tasks already have "spar Grok if uncertain" fallback
- KV7: Claude Code runs real bash commands, doesn't hallucinate them — this is CLI, not chat
- VERDICT "collapse to 3 phases": more ceremony doesn't mean wrong; 5 phases prevent context rot (the actual problem this solves)

**Actionable changes for next session:**
1. Add phase carry-over protocol (what happens when session ends mid-phase)
2. Consider adding warm-pack diff check (compare with previous version at session start)
3. Make Grok review recommended (not just optional) for Tier 1 projects with 3+ file changes
