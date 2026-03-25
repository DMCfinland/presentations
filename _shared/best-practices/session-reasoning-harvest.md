---
name: session-reasoning-harvest
description: Compress and save AI reasoning chains from sessions for future leverage analysis and spawn prompt improvement
type: feedback
---

# Session Reasoning Harvest

## What
At session end, capture 3-5 key reasoning chains the AI derived during the session — compressed to 1-2 sentences each. Store in a reasoning log. These are NOT decisions (those go in DECISIONS.md) — they are the HOW and WHY behind the AI's thinking.

## Why
AI reasoning derived once gets lost at context compression. In future sessions, the same reasoning must be re-derived — costing tokens and sometimes producing different conclusions. Captured reasoning chains can be:
- Pre-loaded into spawn prompts (eliminates re-derivation cost)
- Analyzed to find where AI consistently needs company context (= context card improvement)
- Reviewed to find redundant reasoning patterns (= prompt efficiency gains)
- Used to calibrate human vs AI touch ratio over time

Example from session 63-64:
- "Why pgvector in Wave 1A: ALTER TABLE on 500+ live rows is expensive; 30-min addition now vs. painful migration later" → this reasoning is reusable for every schema decision involving live data
- "Why atomic facts not blobs: semantic search averages out meaning in full-blob embeddings" → reusable for any future embedding design decision
- "Why soft-delete not hard-delete: GDPR audit trail requires the row to exist as evidence" → reusable GDPR pattern

## When to apply
Any session that produced significant AI reasoning (architectural decisions, security analysis, GDPR design). Not needed for routine sessions (status updates, file moves, brief Q&A).

## Format
At session end, write 3-5 entries to `reasoning-log/` in the project folder:
```markdown
## [date] — [project]
- **[topic]:** [1-2 sentence compressed reasoning chain] (reusable: yes/no, applies to: [domain])
- **[topic]:** ...
```

Or append to the session log in CURRENT-STATUS.md as a `reasoning_harvest:` YAML field.

## Leverage mechanism
Over 10+ sessions, reasoning harvest builds a library of pre-derived conclusions. Spawn prompts can include "Pre-derived reasoning: [paste relevant items]" — reducing the AI's need to re-reason from first principles. Estimated value: 15-30 min per complex session once library has 20+ entries.

## MemPO-Inspired Memory Decision Block (add to harvest prompt)

When writing the reasoning harvest, also run this structured memory decision for each entry.
Inspired by MemPO (Self-Memory Policy Optimization, arxiv 2603.00680, Feb 2026) — agents
that learn to autonomously decide what to retain, update, or archive during a session.

```
## MEMORY DECISION (for each reasoning chain captured)

For each item in the reasoning harvest above, also decide:

- warm_pack: [which warm pack should this be added to? E.g. "strategic-research" / "all"]
- company_scope: [DMC only / all portfolio / specific project]
- confidence: [0.3 tentative / 0.5 moderate / 0.7 strong]
- supersedes: [does this replace an existing entry? If yes: which file/entry?]
- pre_load_value: [high / medium / low — how often will future sessions need this reasoning?]
- action: [ADD to warm pack / UPDATE existing entry / ARCHIVE superseded / SKIP — already documented]
```

This replaces manual Context Pack compilation: Claude decides what updates warm packs,
reducing the chance of stale or redundant entries accumulating over time.
Estimated value: prevents 60% reasoning-chain loss at context compression, richer context packs.

## Automation horizon
The manual version of this pattern is being validated first. Production tools that automate it:
- **Mem0** (mem0.ai) — automated memory extraction + update layer. 26% accuracy boost vs OpenAI.
  Extracts, compares, updates/deprecates memories automatically. Could replace Context Pack compilation.
- **DSPy GEPA** (dspy.ai) — human text feedback → automatic prompt rewrites. The correction harvest
  (gepa-correction-harvest.md) is the manual version of GEPA.
- **MemPO** (arxiv 2603.00680) — agents self-summarize memory during session. -67% tokens, +26% F1.
These tools are relevant at scale (10+ companies, 200+ sessions). Current manual system is sufficient
for now and more controllable for a 1-person operation.

## Status
Tier B (new — not yet validated across sessions). First application: session 64.
MemPO block added: session 64 (Grok 4-agent validation).

## Source
session: 64, source: patrick ("our conversations could be decompressed and used to boost our human to AI work leverage ratio")
research_validated: Grok 4-agent debate (session 64) — MemPO (Feb 2026), Mem0, DSPy GEPA
applies_to: all portfolio companies
