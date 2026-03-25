# How to Use This Knowledge Base

## What This Is
1,331 gold insights extracted from 172 YouTube videos (Nate B Jones AI strategy channel). Cost: $95 total ($92 analysis + $3 gold extraction).

## Four-Level Architecture

| Level | Name | What | Where | Loaded When |
|-------|------|------|-------|-------------|
| **0** | Universal Principles | 3 cross-project KB principles | CLAUDE.md Tier A | Every session, always |
| **1** | Knowledge Triggers | 3-5 one-line action triggers per project type (KB + BP) | `### Knowledge Triggers` in warm packs | Every session of that type |
| **2** | Deep Dive | Topic file + BP file paths + size + use-when condition | `### Deep Dive (load on demand)` in warm packs | On demand, when question arises |
| **3** | Archive | ai-strategy.md, full video files | This file + _topic-index.md | Never unless targeted research |

## Topic Files (Level 2 — Load on Demand)

| File | Insights | Size | Load When |
|------|----------|------|-----------|
| seo-search-geo.md | 26 | ~10KB | SEO/GEO optimization work |
| cost-infrastructure.md | 40 | ~15KB | Cost optimization or infrastructure decisions |
| security-governance.md | 44 | ~15KB | Compliance, privacy, or security governance |
| productivity-workflows.md | 53 | ~20KB | Workflow design or automation |
| knowledge-rag.md | 95 | ~100KB | Knowledge system design, RAG, retrieval |
| models-capabilities.md | 95 | ~35KB | Model selection or capability evaluation |
| career-skills.md | 97 | ~35KB | Career development or skills strategy |
| prompting-context.md | 114 | ~119KB | Prompt engineering or context optimization |
| leadership-org.md | 125 | ~40KB | Organizational design or leadership |
| software-dev.md | 147 | ~50KB | Software development practices |
| agent-architecture.md | 249 | ~80KB | Multi-agent systems or agent design |
| ai-strategy.md | 888 | ~150KB | NEVER load fully — use best-of-ai-strategy.md instead |

## Never-Load List
- `topics/ai-strategy.md` (888 insights, ~150KB) — too broad, too large. Use `best-of-ai-strategy.md` for broad coverage
- `knowledge-base/videos/*.md` (196 files, ~35KB each, 7MB total) — raw analysis files, superseded by topic clusters
- Type flat files (`gold-frameworks.md`, `gold-contrarian.md`, etc.) — redundant with topic files

## Context Budget Rules
- Total system overhead: ~49KB (6% of 200K context)
- Hard ceiling: 15% of context (30KB remaining for KB content)
- Files <50 insights: safe to load fully when relevant
- Files 50-150 insights: load selectively or use KB Triggers only
- Files >150 insights: never load fully, use curated subsets

## How Knowledge Triggers Work
Each warm pack has a `### Knowledge Triggers` section with lines like:
```
- [Compressed principle] → [What to do when triggered] (topics/[source].md or bp: [file].md)
```
These are **retrieval keys** — compressed action principles from both the YouTube KB and Best Practices files that activate during normal work. When the assistant recognizes a relevant situation, the trigger fires and the principle guides the decision. No searching required.

If deeper context is needed, the `### Deep Dive (load on demand)` section in each warm pack points to full topic files and BP files with size warnings and load conditions.

## Maintenance Schedule
- **Per session:** Nothing. Zero maintenance cost.
- **Every 5 sessions (compression cycle):** Check `last_curated` timestamps. Flag packs >30 sessions stale.
- **Quarterly (~1 hour, Patrick):** Review triggers, check for topic files >200 insights, promote/demote insights.
- **When adding new videos:** Gold extraction → topic files auto-update → triggers reviewed at next quarterly.

## File Map
```
knowledge-base/
├── HOW-TO-USE-THIS-KB.md          ← you are here
├── gold-insights/
│   ├── gold-index.md               ← extraction stats
│   ├── by-type/                     ← 5 flat files (frameworks, contrarian, etc.)
│   └── topics/                      ← 12 topic clusters + routing index
│       ├── _topic-index.md          ← routing table (load this when unsure)
│       ├── ai-strategy.md           ← 888 insights — NEVER load fully
│       ├── best-of-ai-strategy.md   ← curated ~30 insights (Patrick-selected)
│       └── [11 other topic files]
└── videos/                          ← 196 raw analysis files — NEVER glob-read
```
