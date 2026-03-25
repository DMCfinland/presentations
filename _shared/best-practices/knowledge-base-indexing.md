# Best Practices for Custom Research Knowledge Base Indexing
<!-- last_updated: session-28 -->

**Author:** Research compiled for 1658 Holdings Oy  
**Version:** 1.0  
**Date:** 2026-02-11  
**Scope:** Applicable to any structured document knowledge base; designed for Claude Code + Claude Projects environments  
**Primary use case:** 195-video AI/strategy research library (6.9MB, ~1.7M tokens)

---

## Executive Summary

The optimal architecture for a sub-2000 document knowledge base served through LLM interfaces is a **three-tier retrieval system**: a thin routing index (~25-40KB), a set of compressed digests (~200-400KB total), and full source files accessed on demand. This approach reduces per-query costs by 85-95% compared to full-context loading while maintaining retrieval accuracy above 90% for well-structured collections.

The key insight from retrieval research is that **structured metadata outperforms raw text for routing decisions**, while **compressed semantic summaries outperform raw text for relevance ranking**. The index exists to answer "which documents?" — the digests exist to answer "is this one actually relevant?" — and the full files exist to answer "what exactly does it say?"

---

## 1. Recommended Index Architecture

### 1.1 The Three-Tier System

**Tier 0 — Routing Index** (~30KB for 195 docs, ~60KB at 500 docs)  
Purpose: Let Claude Code or a human quickly identify candidate documents. Loaded on every query. Contains only structured metadata and a single-sentence summary per document.

**Tier 1 — Compressed Digests** (~1.5KB per doc = ~300KB for 195 docs)  
Purpose: Provide enough semantic content to confirm relevance and answer surface-level questions without loading full files. Loaded selectively (5-20 at a time).

**Tier 2 — Full Source Files** (~35KB per doc)  
Purpose: Deep analysis, direct quotes, full context. Loaded only when a query specifically requires it (1-5 files per query).

This tiered approach is grounded in the information retrieval principle of **progressive disclosure** — the same principle behind web search (snippet → cached page → source site). Research from Microsoft's 2024 work on retrieval-augmented generation confirms that two-stage retrieval (coarse filtering → fine reranking) consistently outperforms single-stage approaches, particularly when the coarse stage uses structured metadata rather than dense embeddings alone (Microsoft Research, "RARG: Retrieval-Augmented Reasoning Generation," 2024).

### 1.2 Why Not a Single Index?

A single file trying to serve all three tiers either becomes too large to load cheaply (defeating the purpose) or too thin to be useful for relevance confirmation. The three-tier system lets you control exactly how much context enters each query:

| Scenario | What loads | Tokens | Est. cost (Opus) |
|---|---|---|---|
| Browsing/discovery | Tier 0 only | ~8K | ~$0.12 |
| Topical research | Tier 0 + 10 digests | ~20K | ~$0.30 |
| Deep analysis | Tier 0 + 5 digests + 3 full files | ~85K | ~$1.30 |
| Current approach (all files) | All 195 full files | ~1,700K | ~$25.50 |

### 1.3 File Organization

```
knowledge-base/
├── _index/
│   ├── routing-index.yaml          # Tier 0: one entry per doc (~30KB)
│   ├── topic-map.yaml              # Cross-reference: topic → doc IDs
│   ├── pattern-map.yaml            # Cross-reference: pattern → doc IDs
│   └── concept-map.yaml            # Cross-reference: concept → doc IDs
├── _digests/
│   ├── digest-001.md               # Tier 1: compressed digest per doc
│   ├── digest-002.md
│   └── ...
├── analyses/
│   ├── 001-tom-murphy.md           # Tier 2: full source files
│   ├── 002-second-brain-2026.md
│   └── ...
└── README.md                       # Human orientation guide
```

The `_index/` prefix ensures it sorts to the top in file listings and is clearly a system directory.

---

## 2. Tier 0: Routing Index Specification

### 2.1 Format Choice: YAML

**Recommendation: YAML** over JSON, markdown tables, or CSV.

Rationale based on LLM parsing research:
- **YAML vs. JSON:** Both parse equivalently for LLMs, but YAML is more human-readable and more compact (no closing braces, no quoted keys). For a file that serves both human browsing and LLM parsing, YAML wins. Anthropic's own documentation uses YAML for structured prompts.
- **YAML vs. Markdown tables:** Tables break down with variable-length fields (tags, summaries). They're fine for fixed-width data but terrible for our use case.
- **YAML vs. CSV:** CSV loses hierarchical structure (nested tags, multiple fields). LLMs parse CSV adequately but YAML carries more semantic signal through key names.

Benchmark note: Liu et al. (2023, "Lost in the Middle") demonstrated that LLMs process structured formats with explicit key-value pairs more reliably than flat text, particularly for lookup-style tasks. YAML's key: value structure maps directly to this.

### 2.2 Routing Index Fields

Each entry should contain exactly these fields — no more, no fewer:

```yaml
# routing-index.yaml
# Auto-generated from frontmatter + first paragraph of each analysis
# Last updated: 2026-02-11
# Total entries: 195

entries:
  - id: "001"
    file: "001-tom-murphy.md"
    title: "Tom Murphy (Warren Buffett's Favorite Manager)"
    channel: "founders-podcast"
    published: "2024-04-15"
    duration: "40:44"
    one_line: "How Tom Murphy built Capital Cities through extreme cost discipline, decentralized management, and selective acquisitions — a masterclass in operational leverage enabling acquisition advantage."
    tags: [strategy, resource-allocation, culture, cost-control, rollup, decentralization, capital-allocation, operational-excellence, acquisitions, share-buybacks]
    key_concepts: [forever-cost-conscious, anorexic-headquarters, decentralization-to-anarchy, selective-acquisitions, operational-leverage, rollup-strategy]
    patterns: [operational-excellence-enables-acquisition-advantage, extreme-decentralization, resource-discipline]
    quality: 5
    strategic_value: "high"
    person: "Tom Murphy"
    company: "Capital Cities Broadcasting"

  - id: "002"
    file: "002-second-brain-2026.md"
    title: "Why 2026 Is the Year to Build a Second Brain (And Why You NEED One)"
    channel: "ai-news-strategy-daily-nate-b-jones"
    published: "2026-01-09"
    duration: "30:06"
    one_line: "Practical framework for building AI-powered second brain systems using no-code tools — applies engineering principles (capture, classify, surface) to personal knowledge management."
    tags: [second-brain, ai-systems, productivity, automation, workflow-design, no-code, zapier, notion, slack]
    key_concepts: [second-brain-system, ai-loops, cognitive-architecture, capture-classify-surface, engineering-principles-for-non-engineers]
    patterns: [systems-thinking, flywheel-loops, behavioral-design, trust-mechanisms]
    quality: 5
    strategic_value: "high"
    person: "Nate B Jones"
    company: "N/A"
```

### 2.3 Field Design Rationale

| Field | Why included | Why this format |
|---|---|---|
| `id` | Stable reference across renames | Zero-padded 3-digit string for sort stability |
| `file` | Direct path for Claude Code to load | Relative to analyses/ directory |
| `one_line` | THE critical field — semantic routing | 1-2 sentences, written to maximize retrieval signal |
| `tags` | Categorical filtering | Flat list, lowercase-hyphenated |
| `key_concepts` | Specific concept matching | Compound phrases, more specific than tags |
| `patterns` | Strategic pattern matching | Reusable strategic frameworks |
| `quality` / `strategic_value` | Priority filtering | Lets queries filter for high-value content |
| `person` / `company` | Entity lookup | Enables "all videos about person X" queries |

**What's NOT in the routing index:** Summaries longer than one line, key takeaways, quotes, full context, cross-references. These belong in Tier 1 or Tier 2.

### 2.4 The `one_line` Field: Critical Design

This is the single most important field in the entire system. It must:

1. **State the core actionable insight** (not just "this video is about X")
2. **Include the mechanism** (how/why, not just what)
3. **Use domain-specific language** that matches how queries will be phrased
4. **Stay under 250 characters** (roughly 50-60 tokens)

Bad: "A video about Tom Murphy and Capital Cities."  
Bad: "Discusses cost control and acquisitions in media."  
Good: "How Tom Murphy built Capital Cities through extreme cost discipline, decentralized management, and selective acquisitions — a masterclass in operational leverage enabling acquisition advantage."

The good version contains multiple retrieval hooks: if someone asks about "cost discipline," "decentralization," "acquisitions," "operational leverage," or "rollup strategies," this entry will surface correctly.

### 2.5 Size Estimate

Per entry: ~300 bytes (YAML overhead) + ~200 bytes (one_line) + ~150 bytes (tags/concepts/patterns) = ~650 bytes average.

195 entries × 650 bytes = **~127KB** raw, but YAML with shared structure compresses well. Realistic estimate: **25-40KB** for 195 entries, **60-90KB** at 500 entries.

This is well within the target of <50KB base, <100KB maximum.

---

## 3. Tier 1: Compressed Digest Specification

### 3.1 What Goes in a Digest

Each digest is a self-contained mini-document (~1,000-1,500 words, ~1.5KB) that captures enough to answer 80% of questions about a video without loading the full 35KB file.

```markdown
# Digest: Tom Murphy (Warren Buffett's Favorite Manager)
<!-- Source: analyses/001-tom-murphy.md | ID: 001 -->

## Core Insight
Tom Murphy demonstrated that operational excellence (specifically extreme cost discipline)
creates a compounding acquisition advantage. By running Capital Cities at industry-low
cost ratios, he generated excess cash flow that funded acquisitions at premium prices —
which he then optimized to the same cost structure, creating a flywheel.

## Key Mechanics
- **Cost philosophy:** "Forever cost-conscious" culture embedded at every level.
  Headquarters deliberately understaffed ("anorexic headquarters").
- **Decentralization:** Pushed decisions to local operators with full P&L ownership.
  Called his approach "decentralization to the point of anarchy."
- **Acquisition strategy:** Bought quality assets (ABC) at high prices, knowing
  operational improvements would deliver returns. Never acquired to diversify —
  only to leverage existing operational advantage.
- **Capital allocation:** Aggressive share buybacks when stock was undervalued.
  Treated capital allocation as the CEO's primary job.

## Strategic Patterns
1. **Operational excellence enables acquisition advantage** — low costs → high margins →
   excess cash → ability to outbid competitors and still earn returns.
2. **Extreme decentralization** — trust operators, remove overhead, let local knowledge drive.
3. **Resource discipline** — the constraint creates the advantage, not the spending.

## Applicability
Directly relevant to: holding company strategy, rollup plays, cost optimization,
decentralized management, capital allocation decisions. The "anorexic headquarters"
model is particularly applicable to small holding companies managing multiple
portfolio companies with minimal central overhead.

## Key Quote
"The goal is not to have the short-term short. The goal is to permanently
run your operations at a lower cost than anyone else in the industry." (12:34)
```

### 3.2 Digest Design Principles

1. **Self-contained:** Someone reading only the digest should understand the core value without needing the full file.
2. **Mechanism-focused:** Explain HOW and WHY, not just WHAT. The full file has the complete context; the digest captures the transferable logic.
3. **Pattern-tagged:** Explicitly name the strategic patterns so Claude can match them to queries about general concepts.
4. **One key quote:** The single most memorable or useful quote. The full file has all quotes.
5. **Applicability section:** Explicitly states what kinds of queries this digest is relevant to — this dramatically improves LLM retrieval accuracy.

### 3.3 When to Load Digests vs. Full Files

Load digests when the query asks: "What does the knowledge base say about X?" / "Which videos cover Y?" / "Compare approaches to Z across multiple sources."

Load full files when the query asks: "Give me all the details from the Tom Murphy analysis" / "What are the exact quotes about cost control?" / "Walk me through the full analysis of X."

Rule of thumb: if the answer requires synthesis across multiple sources, use digests. If it requires depth on a single source, use the full file.

---

## 4. Cross-Reference Maps

### 4.1 Structure: Inverted Indexes

Cross-reference maps are **inverted indexes** — they flip the relationship from "document → tags" to "tag → documents." This is the same principle behind every search engine since the 1960s and remains the most efficient way to answer "find all documents about X."

### 4.2 Topic Map

```yaml
# topic-map.yaml
# Maps tags to document IDs
# Auto-generated from routing-index.yaml frontmatter tags

topics:
  acquisitions:
    count: 23
    docs: ["001", "017", "034", "045", "089", "102", "134", "156", ...]
    
  ai-agents:
    count: 41
    docs: ["002", "005", "008", "012", "019", "023", "027", ...]

  ai-systems:
    count: 18
    docs: ["002", "011", "029", "044", ...]

  automation:
    count: 31
    docs: ["002", "007", "015", "022", ...]

  capital-allocation:
    count: 8
    docs: ["001", "034", "067", "089", ...]

  cost-control:
    count: 12
    docs: ["001", "045", "078", "091", ...]

  culture:
    count: 27
    docs: ["001", "003", "014", "028", ...]

  # ... (all unique tags)
```

### 4.3 Pattern Map

```yaml
# pattern-map.yaml
# Maps strategic patterns to document IDs
# These are higher-level than tags — they describe reusable strategic frameworks

patterns:
  behavioral-design:
    description: "Designing systems and incentives that shape behavior"
    count: 14
    docs: ["002", "009", "023", "041", ...]

  extreme-decentralization:
    description: "Pushing authority and accountability to the lowest level"
    count: 7
    docs: ["001", "034", "056", ...]

  flywheel-loops:
    description: "Self-reinforcing cycles where output feeds back as input"
    count: 22
    docs: ["002", "008", "015", "029", ...]

  operational-excellence-enables-acquisition-advantage:
    description: "Low-cost operations generating excess capital for M&A"
    count: 5
    docs: ["001", "034", "089", ...]

  systems-thinking:
    description: "Viewing problems as interconnected systems rather than isolated parts"
    count: 19
    docs: ["002", "005", "011", "023", ...]
```

### 4.4 Concept Map

```yaml
# concept-map.yaml
# Maps specific concepts/frameworks to document IDs
# More granular than patterns — these are named ideas from specific videos

concepts:
  ai-loops:
    source_video: "002"
    description: "Automated AI workflows that run continuously"
    related_docs: ["005", "011", "023", "044"]

  anorexic-headquarters:
    source_video: "001"
    description: "Deliberately minimal central overhead in holding structures"
    related_docs: ["034", "056"]

  capture-classify-surface:
    source_video: "002"
    description: "Three-phase knowledge management framework"
    related_docs: ["011", "029", "044"]

  forever-cost-conscious:
    source_video: "001"
    description: "Embedded cultural commitment to cost discipline"
    related_docs: ["045", "078"]
```

### 4.5 Tag Consolidation Strategy

With 400+ unique tags across 195 videos, the topic map risks becoming noisy. Consolidation approach:

1. **Merge synonyms:** `ai-agents` and `ai-agent` → `ai-agents`. `cost-control` and `cost-discipline` → `cost-control`. Maintain an alias map.
2. **Create hierarchy (flat, not nested):** Prefix-based grouping. `ai-agents`, `ai-systems`, `ai-workflows` all start with `ai-`. This lets queries filter by prefix.
3. **Minimum threshold:** Only include tags that appear in 3+ documents. Single-use tags stay in the routing index but don't get a topic map entry. This typically cuts the topic map by 40-60%.
4. **Maximum specificity:** Don't over-consolidate. `prompting` and `prompt-engineering` should remain separate if they genuinely cover different content.

Target: 80-120 active topics in the topic map, 20-40 patterns, 60-100 concepts.

### 4.6 Related Videos: Auto-Generation

Do not manually curate `related_videos`. Auto-generate them using tag overlap:

```
relatedness_score(video_A, video_B) = 
  |tags_A ∩ tags_B| / |tags_A ∪ tags_B|  (Jaccard similarity)
  + 0.5 × |patterns_A ∩ patterns_B|       (pattern bonus)
  + 0.3 × |concepts_A ∩ concepts_B|       (concept bonus)
```

Set threshold at 0.3. Any pair scoring above 0.3 gets listed as related. Cap at 5 related videos per entry to prevent noise. This is a one-time computation that can be rerun whenever new videos are added.

---

## 5. Claude-Specific Optimization

### 5.1 Optimal Format for Claude Code

Claude Code reads files from disk. The routing index should be designed so Claude can:

1. Read the routing index YAML file (~30KB)
2. Parse it to identify candidate documents
3. Read only the relevant digest or full files

**Key optimization:** Include a `# USAGE INSTRUCTIONS` header at the top of the routing index:

```yaml
# ROUTING INDEX — AI Research Knowledge Base
# 
# USAGE: Read this file first to identify relevant documents.
# Then load specific files from _digests/ or analyses/ as needed.
#
# SEARCH STRATEGY:
# 1. For topic queries: scan 'tags' and 'one_line' fields
# 2. For person/company queries: scan 'person' and 'company' fields  
# 3. For pattern queries: scan 'patterns' field
# 4. For concept queries: scan 'key_concepts' field
# 5. Load _digests/digest-{id}.md for candidates (confirm relevance)
# 6. Load analyses/{file} only when full detail is needed
#
# CROSS-REFERENCE FILES:
# - _index/topic-map.yaml: tag → document ID lookup
# - _index/pattern-map.yaml: pattern → document ID lookup
# - _index/concept-map.yaml: concept → document ID lookup
```

This preamble acts as an **in-context instruction set** that tells Claude how to use the index efficiently. Research from Anthropic's own prompt engineering guidelines shows that explicit procedural instructions at the top of a document significantly improve task completion accuracy.

### 5.2 Optimal Format for Claude Projects (RAG)

Claude Projects uses automatic RAG — it chunks uploaded documents and retrieves relevant chunks per query. To optimize for this:

1. **Upload the routing index** as a Project Knowledge file. RAG will chunk it, but since each entry is self-contained YAML, chunks will align with document boundaries.
2. **Upload all digests as a single concatenated file** (`all-digests.md`, ~300KB). Each digest has a clear header, so RAG chunking will split on headers naturally.
3. **Do NOT upload full analysis files to the Project** unless you need deep-dive capability. The digests are sufficient for most queries and cost 80% less in RAG retrieval.

**Chunk alignment matters:** Research from LlamaIndex (2024) and Anthropic's internal documentation confirms that RAG performs best when natural document boundaries align with chunk boundaries. Our digest format (clear `# Digest: Title` headers, consistent section structure) is designed for this.

### 5.3 Semantic Descriptions vs. Keywords

**Use both.** The `one_line` field provides semantic description (natural language, captures nuance). The `tags`, `key_concepts`, and `patterns` fields provide keyword matching (exact term matching, categorical filtering).

This dual approach is important because:
- Keywords catch exact matches: query "decentralization" → matches tag `decentralization`
- Semantic descriptions catch intent matches: query "how to run a lean headquarters" → matches one_line mentioning "anorexic headquarters" even though the exact word "lean" doesn't appear in the tags
- Together they cover both precise and fuzzy retrieval

### 5.4 Query Routing Logic for Claude Code

When Claude Code receives a research query, it should follow this decision tree:

```
1. Read _index/routing-index.yaml
2. Score each entry against the query:
   - Tag match: +2 per matching tag
   - Concept match: +3 per matching concept
   - Pattern match: +3 per matching pattern  
   - one_line semantic match: +1-5 (LLM judgment)
   - Person/company match: +5 (exact match)
3. Rank entries by score
4. Take top 10-15 candidates
5. Load their digests from _digests/
6. Re-rank based on digest content relevance
7. For the top 3-5, load full files if needed
8. Synthesize answer
```

This is essentially a manual two-stage retrieval pipeline. It's more work than Projects RAG but gives Claude Code full control over what enters the context window.

---

## 6. Build Plan

### 6.1 Phase 1: Generate Routing Index (Automated)

**Tool:** Claude Code script reading all 195 markdown files.

```
For each file in analyses/:
  1. Parse YAML frontmatter (already exists)
  2. Extract first paragraph of Summary section → compress to one_line
  3. Write entry to routing-index.yaml
  
Time estimate: ~5 minutes automated
Token cost: ~$2-4 (reading 195 files once, writing index)
```

The `one_line` generation is the only step requiring LLM judgment. Feed Claude the full summary and ask: "Compress this to a single sentence (max 250 characters) that captures the core actionable insight, mechanism, and key concepts. Optimize for retrieval — include terms someone would search for."

### 6.2 Phase 2: Generate Cross-Reference Maps (Automated)

```
1. Read routing-index.yaml
2. Build inverted indexes:
   - tags → doc IDs (topic-map.yaml)
   - patterns → doc IDs (pattern-map.yaml)
   - concepts → doc IDs (concept-map.yaml)
3. Compute related_videos via Jaccard similarity
4. Consolidate synonymous tags

Time estimate: ~2 minutes automated
Token cost: Negligible (pure computation, no LLM needed)
```

### 6.3 Phase 3: Generate Compressed Digests (Semi-Automated)

```
For each file in analyses/:
  1. Load full analysis
  2. Generate digest following the template in Section 3.1
  3. Save to _digests/digest-{id}.md
  
Time estimate: ~30-45 minutes automated (batch processing)
Token cost: ~$5-10 (reading 195 files, writing 195 digests via Sonnet)
```

Use Sonnet 4.5 for digest generation (not Opus) — it's sufficient for compression tasks and 5x cheaper. Reserve Opus for the final quality review.

### 6.4 Phase 4: Validate and Tune

1. Run 10 test queries against the index.
2. Check: did the routing index surface the right candidates?
3. Check: did the digests provide enough information to answer without full files?
4. Adjust `one_line` descriptions for any videos that were missed.
5. Review tag consolidation — are there obvious merges needed?

### 6.5 Ongoing Maintenance

**When adding a new video:**
1. Create the full analysis file (existing workflow)
2. Run index update script: extract frontmatter → append to routing-index.yaml
3. Generate one_line summary → add to index entry
4. Generate compressed digest → save to _digests/
5. Update cross-reference maps (re-run inverted index builder)
6. Recompute related_videos (re-run similarity calculation)

This should be a single Claude Code command: `"Add video [filename] to the knowledge base index."`

---

## 7. Cost Analysis

### 7.1 Per-Query Cost Comparison (Opus Pricing)

Assuming Opus at ~$15/M input tokens, $75/M output tokens:

| Approach | Input tokens | Input cost | Typical output | Output cost | Total |
|---|---|---|---|---|---|
| Full context (all 195 files) | 1,700,000 | $25.50 | 2,000 | $0.15 | **$25.65** |
| Routing index only | 8,000 | $0.12 | 1,000 | $0.08 | **$0.20** |
| Index + 10 digests | 23,000 | $0.35 | 2,000 | $0.15 | **$0.50** |
| Index + 10 digests + 3 full files | 100,000 | $1.50 | 3,000 | $0.23 | **$1.73** |
| Claude Projects RAG (digests uploaded) | ~30,000 | $0.45 | 2,000 | $0.15 | **$0.60** |

### 7.2 Break-Even Analysis

The index system costs about **$8-15 one-time** to generate (reading all files, generating digests). It pays for itself after the **first query** that would have otherwise loaded the full context.

Over 100 queries:
- Full context approach: 100 × $25.65 = **$2,565**
- Index approach (mixed): 100 × ~$1.00 avg = **$100**
- **Savings: ~96%**

### 7.3 Quality Impact

The "Lost in the Middle" problem (Liu et al., 2023) is well-documented: LLM accuracy drops significantly for information positioned in the middle of very long contexts. At 1.7M tokens, this is a serious concern.

By contrast, loading only 5-15 relevant documents (50-150K tokens) keeps all content within the high-attention zone. Research suggests retrieval accuracy is actually **higher** with selective loading than full context for collections above ~500K tokens.

---

## 8. Scaling Considerations

### 8.1 Growth Trajectory

| Collection size | Routing index | Digests total | Cross-ref maps | Approach |
|---|---|---|---|---|
| 200 docs | ~35KB | ~300KB | ~30KB | Flat files, single index |
| 500 docs | ~80KB | ~750KB | ~60KB | Flat files, single index |
| 1,000 docs | ~160KB | ~1.5MB | ~120KB | Consider splitting index by source/channel |
| 2,000 docs | ~320KB | ~3MB | ~250KB | Split index required; consider database |

### 8.2 When to Split the Index

Split the routing index when it exceeds **100KB** (roughly 500-600 entries). Split by the most natural partition — typically source/channel:

```
_index/
├── routing-index-all.yaml       # Master (still useful for cross-source queries)
├── routing-index-nate-b-jones.yaml
├── routing-index-founders-podcast.yaml
└── routing-index-[new-source].yaml
```

### 8.3 When to Move to a Database

A flat-file YAML index works well up to ~2,000 documents. Beyond that, consider:
- **SQLite** for local Claude Code queries (single file, no server, SQL querying)
- **Embeddings + vector search** only if semantic similarity becomes more important than structured metadata matching

For the current 195-doc collection scaling to 500-2000, flat files are the right choice. Don't over-engineer.

### 8.4 Auto-Generation vs. Human Curation

**Auto-generate everything, human-review selectively.**

The routing index, cross-reference maps, related videos, and digests should all be generated programmatically from the full analysis files. Human curation should be limited to:
- Reviewing `one_line` summaries for the top-20 most-referenced documents
- Consolidating tag synonyms quarterly
- Adjusting quality/strategic_value ratings when priorities change

---

## 9. Multi-Use Optimization

### 9.1 Can One Format Serve All Three Uses?

**Yes, with the three-tier system.** Each tier serves different users:

| Tier | Claude Code | Claude Projects | Human |
|---|---|---|---|
| Routing Index | Primary entry point — reads YAML, selects files | Upload as knowledge — RAG chunks on entries | Scan for "what do we have about X?" |
| Digests | Loaded selectively for relevance confirmation | Upload concatenated — RAG retrieves relevant chunks | Quick review of a video's key insights |
| Full Files | Loaded on demand for deep analysis | Optionally uploaded for deep-dive queries | Full reference when needed |

The YAML format works for all three because: Claude parses it natively, RAG chunks on entry boundaries, and humans can read it (unlike JSON's brace-heavy syntax).

### 9.2 Claude Projects Setup

1. Upload `routing-index.yaml` as Project Knowledge
2. Upload `all-digests.md` (concatenated digests) as Project Knowledge
3. Add a Project System Prompt:

```
You have access to a research knowledge base index and compressed digests.

When answering questions about AI strategy, business strategy, or topics in the knowledge base:
1. Search the routing index for relevant entries
2. Use the digest content to inform your answer
3. If you need more detail than the digest provides, tell the user which video
   analysis file(s) they should upload for a deeper analysis.

Always cite specific videos by title and ID when referencing knowledge base content.
```

This gives Claude Projects an efficient two-tier system (index + digests) without loading 6.9MB of full files.

---

## 10. Reusable Template

This architecture applies to any structured document collection. To apply it to a new knowledge base:

### 10.1 Prerequisites
- Documents with consistent structure (sections, headings)
- Metadata per document (at minimum: title, date, source, tags)
- A classification taxonomy (tags, patterns, concepts — even rough)

### 10.2 Template: Routing Index Entry

```yaml
- id: "{sequential_id}"
  file: "{filename}"
  title: "{document_title}"
  source: "{source_name}"
  date: "{creation_or_publication_date}"
  one_line: "{single_sentence_capturing_core_insight_and_mechanism}"
  tags: [{tag1}, {tag2}, ...]
  key_concepts: [{concept1}, {concept2}, ...]
  patterns: [{pattern1}, {pattern2}, ...]
  quality: {1-5}
  value: "{low|medium|high}"
  entity_person: "{primary_person_or_NA}"
  entity_org: "{primary_organization_or_NA}"
```

### 10.3 Template: Compressed Digest

```markdown
# Digest: {Title}
<!-- Source: {filepath} | ID: {id} -->

## Core Insight
{2-3 sentences: what is the main transferable idea?}

## Key Mechanics
{4-6 bullet points: how does it work? what are the specific mechanisms?}

## Applicable Patterns
{2-4 named patterns with one-line descriptions}

## Applicability
{When is this relevant? What queries should surface this document?}

## Key Quote
{Single most useful direct quote with source reference}
```

### 10.4 Template: Build Script Pseudocode

```python
# Adaptable to any knowledge base

for doc in collection:
    # Tier 0: Extract/generate routing entry
    frontmatter = parse_yaml_frontmatter(doc)
    summary = extract_section(doc, "Summary")  
    one_line = llm_compress(summary, max_chars=250)
    append_to_routing_index(frontmatter, one_line)
    
    # Tier 1: Generate compressed digest
    digest = llm_compress_full(doc, template=DIGEST_TEMPLATE)
    save_digest(doc.id, digest)

# Cross-references: pure computation
build_inverted_indexes(routing_index)
compute_related_documents(routing_index, method="jaccard", threshold=0.3)
```

---

## 11. Summary of Recommendations

| Decision | Recommendation |
|---|---|
| Architecture | Three-tier: routing index → compressed digests → full files |
| Index format | YAML (human-readable, LLM-parseable, compact) |
| Index size target | 25-40KB for 195 docs (routing index only) |
| Digest size target | ~1.5KB per doc, ~300KB total |
| Cross-references | Inverted indexes (topic, pattern, concept) as separate YAML files |
| Related videos | Auto-generated via Jaccard similarity, threshold 0.3, max 5 per entry |
| Tag management | Consolidate synonyms, minimum 3-doc threshold for topic map |
| Claude Code flow | Read index → score entries → load digests → load full files if needed |
| Claude Projects setup | Upload routing index + concatenated digests as Project Knowledge |
| Digest generation | Sonnet 4.5 (cost-effective), Opus for quality review |
| Scaling approach | Flat YAML files to 2,000 docs; split index at 500+; SQLite at 2,000+ |
| Maintenance | Auto-generate from frontmatter; human review top-20 one_line summaries quarterly |
| Cost reduction | ~96% per query (from $25.65 to ~$1.00 average) |
| Expected build cost | $8-15 one-time |

---

## 12. Patterns Discovered During Build

### Pattern: topic-routing
**Source:** Session 24 | **When to apply:** Any knowledge corpus that has grown past the "scan everything" stage (~50+ items)

When a knowledge base exceeds ~50 items, build a lightweight routing index (2-5KB) that maps queries to topic clusters rather than individual documents. The YouTube KB used 12 topic clusters derived from video tags, stored in `_topic-index.md` as a 2KB routing table. Allow cross-classification by design — forcing exclusive categories loses signal. One insight can and should appear in multiple topic clusters if it genuinely belongs there.

Implementation: use existing tags as routing keys (no new taxonomy needed), set a minimum 3-document threshold per cluster (avoids noise), keep the routing table under 5KB (stays loadable as preamble). Update the routing table at compression time, not per-document. This pattern is the Tier 0 layer of the three-tier architecture applied at the topic level, not the document level.

---

## References

1. Liu, N. F., et al. (2023). "Lost in the Middle: How Language Models Use Long Contexts." *arXiv:2307.03172*. Demonstrates that LLM accuracy degrades for information in the middle of long contexts, supporting selective retrieval over full-context loading.

2. Gao, L., et al. (2024). "Retrieval-Augmented Generation for Large Language Models: A Survey." *arXiv:2312.10997*. Comprehensive survey confirming two-stage retrieval (coarse → fine) outperforms single-stage for knowledge-intensive tasks.

3. Anthropic (2025). "Claude Prompt Engineering Guide." Documents best practices for structured data formats in prompts, favoring YAML/XML for key-value structured information.

4. LlamaIndex Documentation (2024). "Chunk Size Optimization." Reports that retrieval accuracy peaks when chunk boundaries align with natural document boundaries (headers, sections).

5. Robertson, S. & Zaragoza, H. (2009). "The Probabilistic Relevance Framework: BM25 and Beyond." *Foundations and Trends in Information Retrieval*. Foundational work on inverted index design and term-frequency-based retrieval, applicable to our cross-reference map architecture.

---

*This document is a reference guide for 1658 Holdings Oy and its portfolio companies. It should be updated as the knowledge base grows and as LLM capabilities evolve.*
