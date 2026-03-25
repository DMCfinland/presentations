# Workflow Decision Framework
## When to Use Which Approach (START HERE)

**Purpose:** Master decision tree for routing any task to the optimal approach
**Owner:** 1658 Holdings Oy
**Date:** 2026-02-12
**Updates:** After discovering new patterns or when costs/capabilities change

---

## Quick Answer for Your Current Task

**You have:** 2-4 items, 300 words each (~1-2KB each, ~2-8KB total)

**Decision:** ❌ **Do NOT index.** ✅ **Process directly with Sonnet.**

**Why:** Way below 50-item indexing threshold. Loading 2-8KB is trivial ($0.03). Building index would cost more than processing.

**Recommended approach:**
```
1. Load all 2-4 items into one Sonnet session ($0.03-0.05)
2. Ask your question
3. Get answer
Done. Total time: 2 minutes, total cost: $0.05
```

---

## Master Decision Tree

```
┌─────────────────────────────────────────────────────────────┐
│                    NEW TASK ARRIVES                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   HOW MANY SOURCE ITEMS?     │
        └──────┬───────────────────────┘
               │
    ───────────┼────────────────────────────────
    │          │            │                  │
    │          │            │                  │
   <10      10-50       50-500            >500
    │          │            │                  │
    ▼          ▼            ▼                  ▼
┌──────┐  ┌────────┐  ┌──────────┐     ┌──────────┐
│DIRECT│  │PROCESS │  │BUILD     │     │VECTOR DB │
│LOAD  │  │BATCH   │  │3-TIER    │     │OR SPLIT  │
│      │  │        │  │INDEX     │     │          │
└──────┘  └────────┘  └──────────┘     └──────────┘
   │          │            │                  │
   ▼          ▼            ▼                  ▼
See §1     See §2       See §3            See §4
```

---

## §1: Direct Loading (<10 Items)

### When to Use
- ✅ 1-10 source items
- ✅ Total size <50KB (~200K tokens)
- ✅ One-time or few queries
- ✅ Items are already structured

### Approach Selection

| Scenario | Model | Tool | Cost |
|----------|-------|------|------|
| **Strategic analysis** | Opus | Claude Code or claude.ai | $0.60-2.00 |
| **General analysis** | Sonnet | Claude Code | $0.10-0.30 |
| **Quick extraction** | Haiku | Claude Code or Batch API | $0.02-0.05 |

### Example Workflows

**Example 1: Your Current Task (2-4 items)**
```bash
# In Claude Code
1. Ask: "Analyze these 2 documents for [your question]"
2. Claude Code reads files with Read tool
3. Sonnet processes (2-8KB = trivial)
4. Get answer

Cost: $0.03-0.05
Time: 2 minutes
```

**Example 2: Strategic Decision (5 items)**
```bash
# In claude.ai with Opus
1. Upload 5 documents to Projects
2. Ask strategic question
3. Opus analyzes with full context
4. Get high-quality recommendation

Cost: $0.60-1.20
Time: 5 minutes
```

**Example 3: Simple Extraction (8 items)**
```bash
# Batch API with Haiku
1. Build JSONL with 8 requests
2. Submit to Batch API
3. Wait 6-12h
4. Download results

Cost: $0.02 × 8 = $0.16 (50% discount)
Time: 10 min setup + wait
```

### Decision Factors

**Use claude.ai Projects if:**
- Need RAG (conversational queries across documents)
- Want follow-up questions
- Sharing with team

**Use Claude Code if:**
- Local files
- Quick one-shot analysis
- Want to save conversation history

**Use Batch API if:**
- Same question for each item
- Can wait 6-24h
- Want 50% cost savings

---

## §2: Batch Processing (10-50 Items)

### When to Use
- ✅ 10-50 source items
- ✅ Similar structure across items
- ✅ Same analysis needed for each
- ✅ Can wait 6-24h for results

### Batch API Decision Tree

```
Does each item need SAME analysis?
    │
    ├─ YES → Batch API (50% discount)
    │   │
    │   ├─ Simple task? → Haiku batch
    │   ├─ Good analysis? → Sonnet batch
    │   └─ Strategic depth? → Opus batch
    │
    └─ NO → Process individually
        └─ Different questions per item → Claude Code
```

### Cost Comparison (50 items)

| Approach | Model | Cost | Time | When to Use |
|----------|-------|------|------|-------------|
| **Batch API** | Haiku | $1 | 6-24h | Simple extraction |
| **Batch API** | Sonnet | $5 | 6-24h | Good analysis |
| **Batch API** | Opus | $25 | 6-24h | Strategic depth |
| **Direct API** | Sonnet | $10 | 2h | Need results now |
| **Claude Code** | Sonnet | $10 | 2h | Different Q per item |

### When NOT to Use Batch API

❌ **Don't batch if:**
- Need results in <6 hours
- Each item needs different analysis
- Items >334KB each (size limit)
- Iterating on prompt (test with 5-10 first)

### Batch Workflow Template

```python
# 1. PILOT TEST (5-10 items first)
test_batch = create_batch(items[:10], prompt)
results = wait_and_retrieve(test_batch)
validate_quality(results)

# 2. REFINE PROMPT if needed
if quality < 80%:
    adjust_prompt()
    retest()

# 3. SCALE TO FULL BATCH
full_batch = create_batch(all_items, final_prompt)
submit_batch(full_batch)

# 4. WAIT & RETRIEVE (6-24h)
results = retrieve_when_ready(full_batch)

# 5. POST-PROCESS
organize_results()
build_index_if_needed()
```

**Critical:** Always pilot with 5-10 items first. Batch API is not interactive—you can't fix prompts mid-flight.

---

## §3: Three-Tier Indexing (50-500 Items)

### When to Use
- ✅ 50-500 source items
- ✅ Expect 20+ queries over time
- ✅ Items are structured/consistent
- ✅ Budget <$50 for build

### Build Decision Matrix

| Collection Size | Expected Queries | Build? | Break-Even |
|----------------|------------------|--------|------------|
| 50 items | <5 queries | ❌ No | N/A |
| 50 items | 20+ queries | ✅ Yes | Query 1-2 |
| 200 items | 10+ queries | ✅ Yes | Query 1 |
| 500 items | 5+ queries | ✅ Yes | Query 1 |

### Three-Tier Architecture

```
Tier 0: Routing Index (~30KB)
├─ Loaded: Every query
├─ Contains: Metadata + one-line summaries
├─ Cost: $0.12-0.20 per query
└─ Build: $2-4 (one-time)

Tier 1: Compressed Digests (~1.5KB each)
├─ Loaded: Selective (5-20 at a time)
├─ Contains: Core insights, mechanisms, patterns
├─ Cost: +$0.30 per 10 digests
└─ Build: $5-8 (one-time, Sonnet batch)

Tier 2: Full Source Files (~35KB each)
├─ Loaded: On demand (1-5 at a time)
├─ Contains: Complete original content
├─ Cost: +$1.00 per 3 files
└─ Build: $0 (already exist)

TOTAL BUILD COST: $8-15 (one-time)
QUERY COST: $0.50-2.00 (vs $25+ full context)
```

### Build Workflow (4 Phases)

**Phase 1: Routing Index (Week 1, $2-4)**
```python
for item in all_items:
    metadata = extract_frontmatter(item)
    summary = extract_summary_section(item)
    one_line = compress_to_one_sentence(summary)  # Sonnet
    append_to_routing_index(metadata, one_line)
```

**Phase 2: Cross-References (Week 1, $0)**
```python
# Pure computation, no LLM needed
build_topic_map(routing_index)      # tag → item IDs
build_pattern_map(routing_index)    # pattern → item IDs
build_concept_map(routing_index)    # concept → item IDs
compute_related_items(jaccard_similarity, threshold=0.3)
```

**Phase 3: Compressed Digests (Week 2, $5-8)**
```python
# Sonnet batch (not Opus—compression doesn't need top tier)
for item in all_items:
    digest = sonnet.compress(item, template=DIGEST_TEMPLATE)
    save_digest(item.id, digest)
```

**Phase 4: Validate (Week 2, $5-10)**
```python
test_queries = [
    "What does KB say about X?",
    "Compare approaches to Y",
    "Which items cover Z?"
]

for query in test_queries:
    candidates = search_routing_index(query)
    digests = load_digests(candidates[:10])
    result = synthesize_answer(digests)
    validate_accuracy(result)
```

### Maintenance

**Adding new items (ongoing):**
```bash
# Single command (should be automated)
claude add-to-index new-document.md

# What it does:
1. Extract metadata → append to routing-index.yaml
2. Generate one_line summary
3. Generate compressed digest
4. Update cross-reference maps
5. Recompute related items

Cost: $0.02-0.05 per new item
Time: 30 seconds automated
```

---

## §4: Large Collections (>500 Items)

### When to Use
- ✅ >500 source items
- ✅ Growing collection (adds 50+/month)
- ✅ High query volume (100+/month)
- ✅ Need semantic search

### Architecture Decision

| Size | Approach | Tools | Cost |
|------|----------|-------|------|
| 500-2000 | **Split indexes** | YAML files by category | $20-40 build |
| 2000-5000 | **SQLite + YAML** | Structured queries + semantic | $50-100 build |
| >5000 | **Vector DB** | Embeddings + semantic search | $200+ build |

### Split Index Strategy (500-2000 items)

```
knowledge-base/
├── _index/
│   ├── routing-index-all.yaml       # Master (100KB)
│   ├── routing-index-category-A.yaml (30KB)
│   ├── routing-index-category-B.yaml (30KB)
│   └── routing-index-category-C.yaml (30KB)
├── _digests/
│   ├── category-A/ (150 digests)
│   ├── category-B/ (200 digests)
│   └── category-C/ (150 digests)
└── documents/
    ├── category-A/ (150 files)
    ├── category-B/ (200 files)
    └── category-C/ (150 files)
```

**Query workflow:**
1. Check category (human or LLM routing)
2. Load category-specific routing index (30KB)
3. Load relevant digests (5-20)
4. Load full files if needed (1-5)

**Cost per query:** $0.50-2.00 (same as single index)

---

## §5: Tool Selection (Claude Code Features)

### Task Tool (Subagents)

**When to use Task tool:**
- ✅ Complex multi-step tasks (3+ steps)
- ✅ Need specialized expertise (Explore, Plan, Bash, SEO, etc.)
- ✅ Want autonomous execution
- ✅ Parallel processing (multiple agents at once)

**Available subagent types:**
- `Explore` — Codebase exploration, pattern searching
- `Plan` — Implementation planning (code changes)
- `Bash` — Terminal operations, git workflows
- `general-purpose` — Multi-step research/analysis
- `seo-*` — SEO audits, sitemaps, schema, GEO
- Custom subagents — mining-organizer, file-builder, company-setup

**Example: Codebase research**
```python
# DON'T use Grep/Glob directly for exploratory questions
# User: "How are errors handled in the client?"

# DO use Task tool with Explore agent
Task(
    subagent_type="Explore",
    prompt="Find how client errors are handled",
    description="Error handling research"
)
# Agent will: Glob → Grep → Read → Synthesize
```

### When NOT to Use Task Tool

❌ **Don't use Task for:**
- Reading a specific known file (use Read tool)
- Searching for a specific class/function (use Grep)
- Single-step operations (use direct tools)
- Tasks that need YOUR context (Tool has separate context)

### Direct Tools vs Task Tool

| Task Type | Use | Not |
|-----------|-----|-----|
| "Read config.json" | Read tool | Task tool |
| "Find all TODO comments" | Grep tool | Task tool |
| "How does auth work in codebase?" | Task(Explore) | Grep |
| "Build implementation plan" | Task(Plan) | Direct prompting |
| "Audit SEO for site X" | Task(seo-audit) | Manual tools |

---

## §6: Model Selection (By Task Type)

### Strategic Work → Opus

**Use Opus 4.6 when:**
- ✅ Fundamental business decisions (M&A, pivots)
- ✅ Deep strategic analysis (market research)
- ✅ Complex planning (multi-year roadmaps)
- ✅ Pattern recognition (synthesis across sources)
- ✅ First principles thinking
- ✅ Orchestration leadership (coordinates other agents)

**Cost:** $0.60-2.00 per analysis (worth it for critical decisions)

**Examples:**
- "Should we acquire Company X?" → Opus
- "Design 3-year AI roadmap" → Opus
- "Analyze market trends" → Opus
- "Synthesize 50 customer interviews" → Opus

### Execution Work → Sonnet

**Use Sonnet 4.5 when:**
- ✅ Coding & scripting
- ✅ File organization
- ✅ First-pass analysis (80% quality sufficient)
- ✅ Implementation work
- ✅ Documentation
- ✅ High-volume processing

**Cost:** $0.10-0.30 per task (great ROI)

**Examples:**
- "Build Python script" → Sonnet
- "Organize mining outputs" → Sonnet
- "Analyze video transcript" → Sonnet
- "Create dashboard" → Sonnet

### Volume Work → Haiku

**Use Haiku 4.5 when:**
- ✅ Simple classifications
- ✅ Quick summaries
- ✅ Data extraction
- ✅ Format conversions
- ✅ Validation checks
- ✅ High-volume screening

**Cost:** $0.02-0.05 per task (volume efficiency)

**Examples:**
- "Tag 1000 documents" → Haiku
- "Extract dates from JSON" → Haiku
- "Check if files have required fields" → Haiku

### Progressive Filtering (Hybrid)

```
Stage 1: Haiku filters 1000 items → 200 candidates ($1)
Stage 2: Sonnet analyzes 200 → 50 high-value ($3)
Stage 3: Opus deep-dives on 50 → final insights ($5)

Total: $9 vs $150 all-Opus = 94% savings
```

---

## §7: Orchestration Patterns

### Pattern 1: Opus Plans, Sonnet Executes

**Use when:** Strategic project with clear implementation

```
1. Opus: "Design Finland DMC AI adoption strategy"
   → Strategic framework, priorities, timeline
   Cost: $5

2. Sonnet (×10): "Build tools, scripts, systems to implement"
   → Code, automation, file structures
   Cost: $1.50

3. Opus: "Review implementation, course-correct"
   → Strategic adjustments
   Cost: $2

TOTAL: $8.50 vs $55 all-Opus = 85% savings
```

### Pattern 2: Sonnet Gathers, Opus Synthesizes

**Use when:** Breadth-then-depth analysis

```
1. Sonnet batch: "Analyze 189 video transcripts"
   → Good analyses, patterns
   Cost: $20

2. Human: "Which videos deserve deep dive?"
   → Prioritization

3. Opus: "Deep analysis of top 20"
   → Extract strategic insights
   Cost: $16

TOTAL: $36 vs $170 all-Opus = 79% savings
```

### Pattern 3: Multi-Agent Orchestration

**Use when:** Parallel research with synthesis

```
1. Opus orchestrator: "Research competitor landscape"
   → Breaks into sub-tasks
   Cost: $1

2. Sonnet agents (parallel):
   ├─ Agent A: "Analyze Company X"
   ├─ Agent B: "Research Company Y reviews"
   └─ Agent C: "Extract competitor pricing"
   Cost: $0.45

3. Opus synthesizer: "Strategic opportunities"
   → High-level insights
   Cost: $1.50

TOTAL: $2.95 vs $7.50 all-Opus = 61% savings
```

---

## §8: Interface Selection

### Claude Code (VS Code Extension)

**Best for:**
- ✅ Local file operations
- ✅ Git workflows
- ✅ Building/organizing
- ✅ Quick analysis
- ✅ Orchestrated multi-agent work

**Available:**
- All models (Opus, Sonnet, Haiku)
- All tools (Read, Write, Edit, Bash, etc.)
- Task tool with subagents
- Free tier + paid Pro tier

**Limitations:**
- ❌ No M365 API access (only locally-synced OneDrive files)
- ❌ No RAG (loads files directly, not chunked retrieval)
- ❌ No persistent Projects

### Claude for Desktop (Cowork)

**Best for:**
- ✅ M365 data mining (OneDrive, SharePoint, Outlook)
- ✅ Quick standalone queries
- ✅ MCP server integrations

**Available:**
- M365 MCP connector (OneDrive, SharePoint, Outlook)
- Desktop app (Mac, Windows, Linux)
- All Claude Code features except git

**Use when:**
- Mining emails from mailboxes
- Searching SharePoint sites
- Accessing M365 data not locally synced

### claude.ai (Browser)

**Best for:**
- ✅ Projects with RAG (conversational across uploaded docs)
- ✅ Team sharing (shared Projects)
- ✅ Long-running conversations
- ✅ Follow-up questions on same dataset

**Available:**
- Projects (upload docs, RAG retrieval)
- Team collaboration
- Extended context (200K tokens)
- Artifacts (visual outputs)

**Cost:**
- Free tier: Limited
- Pro: $20/month
- Teams: $30/user/month (has M365 connector)

**Use when:**
- Need RAG across 50+ documents
- Want conversational interface
- Sharing with team

### Batch API (Python/CLI)

**Best for:**
- ✅ Bulk processing (10+ similar tasks)
- ✅ 50% cost savings
- ✅ Can wait 6-24h

**Available:**
- All models (Opus, Sonnet, Haiku)
- Same capabilities as Direct API
- JSONL format submission

**Limitations:**
- ⏳ 6-24h turnaround
- 📄 334KB per-request size limit
- ❌ No interactive refinement

**Use when:**
- Processing 50+ items same way
- Not time-sensitive
- Budget-conscious

---

## §9: Complete Decision Flowchart

```
┌─────────────────────────────────────────────────────────┐
│                    NEW TASK ARRIVES                     │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ Is this STRATEGIC?   │
            │ (M&A, roadmap, etc.) │
            └────┬────────────┬────┘
                 │            │
              YES│            │NO
                 │            │
                 ▼            ▼
         ┌──────────┐    ┌────────────────┐
         │ USE OPUS │    │ How many items? │
         └──────────┘    └───┬────────────┘
                             │
              ───────────────┼─────────────────────
              │              │              │      │
             <10          10-50          50-500  >500
              │              │              │      │
              ▼              ▼              ▼      ▼
          DIRECT        BATCH API      3-TIER   SPLIT/
          LOAD          (50% off)      INDEX    VECTOR
            │               │             │         │
            ▼               ▼             ▼         ▼
    ┌──────────────┐  ┌──────────┐  ┌──────────┐  ┌──────┐
    │ Same Q for   │  │Build cost│  │Build cost│  │Build │
    │ each item?   │  │vs savings│  │$8-15     │  │cost  │
    │              │  │          │  │Queries>20│  │$200+ │
    │ YES: Haiku   │  │Pilot 10  │  │          │  │      │
    │ NO: Sonnet   │  │Scale all │  │4 phases  │  │Hire  │
    └──────────────┘  └──────────┘  └──────────┘  └──────┘
            │               │             │         │
            └───────────────┴─────────────┴─────────┘
                            │
                            ▼
                ┌──────────────────────┐
                │   EXECUTE & TRACK    │
                │   • Cost per query   │
                │   • Accuracy         │
                │   • Time saved       │
                └──────────────────────┘
```

---

## §10: Your Current Task (APPLIED)

### Task: 2-4 items, 300 words each

**Step 1: Count items** → 2-4 items ✅

**Step 2: Calculate size** → 300 words × 4 = 1200 words ≈ 1.5KB ✅

**Step 3: Check threshold**
- <10 items? ✅ YES
- Total <50KB? ✅ YES
- Expected queries? Probably 1-5

**Step 4: Decision → DIRECT LOAD**

**Step 5: Model selection**
- Strategic decision? → Use Opus
- General analysis? → Use Sonnet
- Quick extraction? → Use Haiku

**Step 6: Interface selection**
- Local files? → Claude Code
- Need M365 data? → Claude for Desktop
- Want RAG/conversation? → claude.ai Projects

### Recommended Workflow

```bash
# Option A: Claude Code (if local files)
1. Open Claude Code
2. Ask: "Read these 2 files and [your question]"
3. Claude reads with Read tool
4. Get answer

Cost: $0.03-0.15 (depending on model)
Time: 2 minutes

# Option B: claude.ai (if want follow-ups)
1. Create new Project
2. Upload 2-4 files
3. Ask question
4. Ask follow-ups

Cost: $0.05-0.30 (depending on model + follow-ups)
Time: 5 minutes
```

**DO NOT:**
- ❌ Build an index (overkill for 4 items)
- ❌ Use Batch API (setup > processing time)
- ❌ Create subagents (direct is faster)

---

## §11: Quick Reference Card

```
┌─────────────────────────────────────────────────────┐
│            WORKFLOW DECISION CARD                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ITEM COUNT → APPROACH                              │
│  • <10 items → Direct load ($0.05-0.30)            │
│  • 10-50 items → Batch API ($1-5 with 50% off)    │
│  • 50-500 items → 3-tier index ($8-15 build)      │
│  • >500 items → Split/vector DB ($20-200 build)   │
│                                                     │
│  TASK TYPE → MODEL                                  │
│  • Strategic → Opus ($0.60-2.00)                   │
│  • Execution → Sonnet ($0.10-0.30)                 │
│  • Volume → Haiku ($0.02-0.05)                     │
│                                                     │
│  CONTEXT → INTERFACE                                │
│  • Local files → Claude Code                        │
│  • M365 mining → Claude for Desktop                 │
│  • RAG/sharing → claude.ai Projects                 │
│  • Bulk tasks → Batch API                          │
│                                                     │
│  COMPLEXITY → ORCHESTRATION                         │
│  • Simple → Direct prompting                        │
│  • Multi-step → Task tool (subagents)              │
│  • Strategic → Opus plans, Sonnet executes         │
│  • Research → Parallel agents + synthesis          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## §12: Cost Optimization Checklist

**Before starting any task:**

- [ ] **Count items** — determines approach (§1-4)
- [ ] **Calculate size** — 1KB ≈ 4 pages ≈ 250 tokens
- [ ] **Estimate queries** — >20 queries = build index worthwhile
- [ ] **Check if strategic** — strategic = Opus, execution = Sonnet
- [ ] **Pilot first** — test with 10% before scaling
- [ ] **Calculate break-even** — when does build cost pay back?
- [ ] **Consider batch** — can you wait 6-24h for 50% savings?
- [ ] **Check for duplicates** — before uploading to Projects
- [ ] **Test honestly** — include "what % did you read?" prompt
- [ ] **Track costs** — measure actual spend vs estimate

**Red flags (STOP):**
- 🚨 Loading >200K tokens expecting faithful processing
- 🚨 Building index for <50 items or <20 queries
- 🚨 Using Opus for tasks Sonnet handles
- 🚨 Skipping pilot on batch jobs
- 🚨 Uploading duplicate folders to Projects

---

## §13: When to Update This Framework

**Update when:**
- ✅ New model capabilities (faster/cheaper/smarter)
- ✅ New tools/interfaces available
- ✅ Cost structure changes
- ✅ Discovered new failure modes
- ✅ Found better orchestration patterns
- ✅ Company workflows evolve

**Review schedule:**
- Monthly: Cost tracking, pattern adjustments
- Quarterly: Full framework review
- Annually: Strategic reassessment

**Document ownership:** 1658 Holdings Oy compounding infrastructure team

---

## Next Steps

**For your current 2-4 item task:**

1. **Identify files** — where are the 2 documents?
2. **Choose interface:**
   - Local files → Claude Code
   - OneDrive files → Claude for Desktop or Claude Code (if synced)
   - Want follow-ups → claude.ai Projects
3. **Choose model:**
   - Strategic decision → Opus
   - General analysis → Sonnet
4. **Execute:**
   - Load files (Read tool or upload)
   - Ask your question
   - Get answer
5. **Cost:** ~$0.05-0.30 total

**Do NOT build index. Just process directly.**

---

*This is a living framework. Update as you discover new patterns or when capabilities/costs change.*

**Last Updated:** 2026-02-12
**Next Review:** 2026-03-12 (monthly)
