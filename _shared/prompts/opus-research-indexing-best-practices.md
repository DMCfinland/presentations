# Research Prompt: Best Practices for Custom Research Knowledge Base Indexing

**Target:** Claude Opus (claude.ai)
**Purpose:** Design an optimal indexing strategy for a 195-video AI research knowledge base
**Cost estimate:** ~$1-3 (moderate context, one-shot)
**Instructions:** Copy everything below the line into claude.ai as a single message.

---

# RESEARCH REQUEST: Best Practices for Custom Research Knowledge Base Indexing

## Who You Are Advising

Patrick Heiskanen, CEO of **1658 Holdings Oy** — a Finnish holding company with 10 portfolio companies. Patrick is building an AI-powered knowledge management system using Claude Code (local file orchestration) and Claude Projects (team AI assistants). He has already built a 195-video research knowledge base and needs to make it efficiently searchable without loading 6.9MB into every query context.

## What We Have

### The Knowledge Base
- **195 video analyses** in individual markdown files
- **Total size:** 6.9MB (~1.7M tokens)
- **Per file:** ~35KB average (~8,500 tokens)
- **Content:** 11-dimension strategic analysis per video (Summary, Context, Key Strategy, Culture, Operations, etc.)
- **Sources:** Nate B Jones (AI strategy, 189 videos), Founders Podcast (business strategy, 6 videos)
- **Quality:** Consistent framework, professionally analyzed by Sonnet 4.5

### YAML Frontmatter Per Video (actual example)
```yaml
---
title: Tom Murphy (Warren Buffett's Favorite Manager)
type: video-analysis
channel: founders-podcast
video_id: qScpb2DIUxY
video_url: https://www.youtube.com/watch?v=qScpb2DIUxY
duration: 40:44
published: 2024-04-15
analyzed: 2026-02-10
tags: [strategy, resource-allocation, culture, cost-control, rollup, decentralization, capital-allocation, operational-excellence, acquisitions, share-buybacks]
key_concepts: [forever-cost-conscious, anorexic-headquarters, decentralization-to-anarchy, selective-acquisitions, operational-leverage, rollup-strategy]
featured_person: Tom Murphy
featured_company: Capital Cities Broadcasting
strategic_patterns: [operational-excellence-enables-acquisition-advantage, extreme-decentralization, resource-discipline]
quality_score: 5
strategic_value: high
related_videos: []
related_insights: [focus-beats-diversification, cost-control-as-moat, decentralization-as-culture]
---
```

### Second Example (AI/Strategy content)
```yaml
---
title: Why 2026 Is the Year to Build a Second Brain (And Why You NEED One)
type: video-analysis
channel: ai-news-strategy-daily-nate-b-jones
video_id: 0TpON5T-Sw4
video_url: https://www.youtube.com/watch?v=0TpON5T-Sw4
duration: 30:06
published: 2026-01-09
analyzed: 2026-02-10
tags: [second-brain, ai-systems, productivity, automation, workflow-design, no-code, zapier, notion, slack]
key_concepts: [second-brain-system, ai-loops, cognitive-architecture, capture-classify-surface, engineering-principles-for-non-engineers]
featured_person: Nate B Jones
featured_company: N/A
strategic_patterns: [systems-thinking, flywheel-loops, behavioral-design, trust-mechanisms]
quality_score: 5
strategic_value: high
related_videos: []
related_insights: [ai-loop-design, behavior-change-systems, no-code-automation]
---
```

### Full Analysis Structure (per video, ~35KB each)
After the YAML frontmatter, each file contains:
1. **Summary** (1 paragraph, ~150 words)
2. **Video Metadata** (channel, URL, duration, published date)
3. **Context** (background, why this matters)
4. **Key Strategy / Business Model** (core insights)
5. **Culture & Incentives** (behavioral design aspects)
6. **Market/Industry Position** (competitive landscape)
7. **Resource Allocation** (how resources are deployed)
8. **Stakeholder Alignment** (who benefits, how)
9. **Innovation / Technology** (technical approaches)
10. **Risk Assessment** (challenges, vulnerabilities)
11. **Operational Execution** (implementation details)
12. **Key Takeaways** (3-5 bullet points)
13. **Memorable Quotes** (direct quotes with timestamps)
14. **Cross-References** (related videos, concepts, patterns)

## The Problem

### Cost Problem
- Loading all 195 files = 1.7M tokens = $25+ per Opus query
- Most queries only need 5-15 relevant videos
- We need a way to find the right videos first, then load only those

### Context Window Problem
- Claude Code (local) processes files from disk — currently no index exists
- If Claude Code accidentally reads the 6.85MB consolidated file, it wastes the entire context window
- We need a lightweight index that Claude Code can read to identify which videos to load

### Project/RAG Problem
- Claude Projects uses RAG (retrieves relevant chunks, not full dataset)
- But 1.7M tokens is still large — may benefit from pre-compression
- An index could also serve as a navigation layer for the Project

### Cross-Referencing Problem
- 195 videos have overlapping themes (AI agents, second brain, prompting, etc.)
- No way to see "all videos about X" without scanning all files
- `related_videos` field is currently empty in all files

## What We Need You To Research

### 1. Index Architecture
- What's the optimal structure for a research knowledge base index?
- Should it be one file or multiple (by-topic, by-channel, by-date)?
- What fields should be in the index vs. left in the full files?
- How much of each video's content should the index capture?
- What's the target size for the index? (We want <50KB ideally, <100KB maximum)

### 2. Compression vs. Indexing
- Should we build a **thin index** (just metadata + 1-line summary per video, ~20KB)?
- Or a **compressed digest** (metadata + summary + key takeaways, ~100-200KB)?
- Or a **tiered system** (thin index → compressed digest → full file)?
- What does research say about optimal context size for retrieval accuracy?

### 3. Cross-Reference Maps
- How should we map topics → videos, patterns → videos, concepts → videos?
- Should these be separate index files or embedded in the main index?
- How to handle the 400+ unique tags across 195 videos without the map becoming unwieldy?
- What's the best practice for "related_videos" — manual curation vs. auto-generation?

### 4. Claude-Specific Optimization
- How should the index be formatted for Claude Code to efficiently find relevant videos?
- Is markdown table, YAML, JSON, or some other format best for LLM index parsing?
- Should we include semantic descriptions or just keywords?
- How does chunk size affect Claude Projects RAG retrieval quality?

### 5. Maintenance & Scaling
- As we add more videos (potentially 500+), how does the index scale?
- Should the index auto-generate from frontmatter, or include human curation?
- When does a flat file index break down and need a database?
- How to handle index freshness (new videos added, old ones updated)?

### 6. Multi-Use Optimization
- This index needs to serve THREE purposes simultaneously:
  1. **Claude Code local search:** Read index → identify files → read only those files
  2. **Claude Projects RAG:** Upload index + compressed digests for cheaper queries
  3. **Human browsing:** Patrick should be able to scan it and find what he needs
- Is one index format sufficient for all three, or do we need specialized views?

## Context: Our Existing RAG Research

We've already researched RAG extensively. Key findings:
- RAG retrieves relevant chunks (10K-150K tokens), not full dataset
- RAG cost per query: ~$3-12 vs. $44 for full context
- "Lost in the middle" problem is real at 1.7M tokens — RAG actually improves quality
- Break-even: 3-4 RAG queries = 1 full context query cost
- Claude Projects RAG is automatic once files are uploaded

**What we DON'T know:** Whether a well-structured index + compressed digests would further improve RAG retrieval quality vs. raw full files.

## What I Need From You

1. **Research-backed recommendations** — cite actual studies, papers, or documented best practices where possible. Don't just theorize.
2. **Concrete index specification** — show me the exact format, fields, and structure. Include a real example using the two videos above.
3. **Build plan** — step-by-step instructions for generating the index from our existing 195 files (what to extract, how to format, how to maintain)
4. **Tiered access design** — how the thin index, compressed digest, and full files work together
5. **Cost analysis** — what's the expected cost reduction per query using the index approach vs. current raw files?
6. **Template** — a reusable pattern we can apply to future knowledge bases (not just this YouTube project)

**Format:** Write your answer as a structured markdown document I can save as `_shared/best-practices/knowledge-base-indexing.md`. This should be a reference guide we use across all 10 portfolio companies, not just for the YouTube project.

**Important:** Be decisive. Give specific recommendations, not "it depends." Where multiple approaches are valid, pick the best one for our context (small team, Mac-based, Claude Code + Claude Projects, scaling to 500-2000 documents).
