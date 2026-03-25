# Best Practices for Medium-Sized Custom Research Projects
<!-- last_updated: session-28 -->
## Chunking Strategy + Cost Optimization

**Author:** Compiled from YouTube Research project learnings
**Version:** 1.0
**Date:** 2026-02-12
**Source Experience:** 196-video YouTube KB ($89 spent, 99% cost reduction achieved)
**Applicable to:** Any research project with 50-500 source documents, target 200-2000 insights

---

## Executive Summary

**The Golden Rule:** Individual files + three-tier retrieval = 96% cost reduction AND better quality.

**Core Insight:** Loading everything into one file creates four failure modes: sampling bias (6.5% actually read), primacy/recency bias (middle items invisible), confident extrapolation (training data fills gaps), and RAG chunk gambling (retrieval may miss connections). The solution: never process more than one document at a time, build a routing system for selective loading.

**Conservative ROI:** First query pays for entire build. 100 queries = $2,565 saved vs full-context approach.

---

## 1. The Three-Tier Architecture (PROVEN PATTERN)

### Core Principle
Never dump everything into context. Build layers that control what loads when.

```
Tier 0: Routing Index    (~30KB)   → loaded every query, identifies candidates
Tier 1: Compressed Digests (~1.5KB each) → loaded selectively (5-20 at a time)
Tier 2: Full Source Files  (~35KB each)  → loaded on demand (1-5 at a time)
```

### Cost Comparison (Opus pricing)

| Scenario | Tokens | Cost per Query | When to Use |
|----------|--------|----------------|-------------|
| All files loaded | 1,700K | $25.50 | ❌ Never — sampling bias guaranteed |
| Tier 0 only | 8K | $0.20 | Discovery: "what do we have?" |
| Tier 0 + 10 digests | 23K | $0.50 | Synthesis: "patterns across sources" |
| Tier 0 + 3 full files | 100K | $1.73 | Deep dive: "full details on X" |
| Claude Projects RAG | 30K | $0.60 | Mixed queries, automated retrieval |

**Target achieved:** $25.50 → ~$1.00 average = **96% cost reduction**

### Break-Even Analysis
- **Build cost:** $8-15 one-time (routing index + digests generation)
- **Payback:** First query that would have loaded full context
- **100 queries:** $2,565 → $100 = **$2,465 saved**

---

## 2. Context Window Failure Modes (CRITICAL LEARNINGS)

### Failure Mode 1: Sampling Bias
**What happens:** LLMs don't read every line of large files. They sample.

**Evidence from YouTube KB:**
- Loaded: 107,340 lines (1.27M tokens)
- Actually read: ~7,000 lines (6.5%)
- Deeply engaged: 25-30 items of 195
- **Cost:** $44 spent, $1.50/item actually processed

**Prevention:**
- ✅ Process files individually (1 at a time)
- ✅ Never load >200K tokens expecting faithful processing
- ✅ Include honesty prompts: "What % did you actually read?"

### Failure Mode 2: Primacy/Recency Bias
**What happens:** Items in the middle of large contexts are invisible.

**Evidence:**
- Beginning/end items: Opus recalled specific quotes
- Middle items (80-120): Could only recall 2 where samples landed
- Asked for 5th insight: "I don't have enough to confidently offer a fifth"

**Prevention:**
- ✅ Equal-treatment processing (one file at a time = no position bias)
- ✅ Don't rely on position-dependent retrieval
- ✅ Critical content goes in Tier 0 (always loaded)

### Failure Mode 3: Confident Extrapolation
**What happens:** Model fills gaps with training data, presents as source content.

**Contamination estimate:** 10-15% of output = training knowledge masquerading as source insight

**Detection signals:**
1. Vague attribution ("Across the corpus...")
2. Generic advice ("start small and iterate")
3. Smooth narrative (no surprises or friction)
4. Confident comprehensiveness ("all 195 videos...")
5. No "I don't know" admissions
6. Uniform quality across sections

**Prevention:**
- ✅ Ask for item-level citations, not just pattern-level
- ✅ Include Q5-style honesty prompts
- ✅ Request self-assessment before trusting synthesis

### Failure Mode 4: RAG Chunk Gambling
**What happens:** RAG retrieves 10-150K tokens, not full dataset. Great for targeted queries, risky for broad synthesis.

**Prevention:**
- ✅ Use RAG for: "What does source X say about Y?"
- ✅ Use full files for: "Patterns across all sources" (but <200K tokens total)
- ✅ For >200K datasets: Build routing index first

---

## 3. The 200K Token Decision Rule

| Dataset Size | Approach | Expected Coverage | Risk Level |
|--------------|----------|-------------------|------------|
| <50K tokens | Full context | ~100% | ✅ Low |
| 50-200K tokens | Full context | ~80-95% | ⚠️ Medium |
| 200-500K tokens | Full context + honesty check | ~40-60% | ❌ High |
| 500K-1M tokens | RAG or file-by-file | Varies | ⚠️ Medium |
| **>1M tokens** | **File-by-file ONLY** | **100%** | ✅ Low |

**Rule:** Never load >200K tokens and expect faithful processing. Period.

---

## 4. File Management Best Practices

### Individual Files vs. Consolidated

| Approach | Pros | Cons | Verdict |
|----------|------|------|---------|
| One big file | Easy to upload | Sampling bias, primacy/recency, $25/query | ❌ Never |
| Individual files | No bias, process all equally, $0.01/file | More files to manage | ✅ Always |

**Critical:** 195 individual files (35KB each) >> 1 consolidated file (6.85MB)

### File Size Targets
- **Source files:** 20-50KB each (readable in one API call)
- **Digests:** 1-1.5KB each (enough for relevance confirmation)
- **Routing index:** 25-40KB total for 200 docs, 60-90KB at 500 docs

### Duplication Prevention
**Risk identified:** macOS Finder creates "folder 2" silently when copying.

**Prevention checklist:**
1. ✅ Run `diff -rq folder1/ folder2/` before uploads
2. ✅ Check for " 2", " 3" suffixes
3. ✅ Calculate cost: `file_size_MB × 250K tokens/M × $15/M = cost per query`
4. ✅ Document in MEMORY.md as permanent warning

**Real cost:** 6.9MB duplicate folder would have cost $25+ per query if uploaded to Claude Project.

---

## 5. Batch API Best Practices

### When to Use Batch API
- ✅ Processing 50+ similar items (50% discount = huge savings)
- ✅ Non-urgent work (24h turnaround acceptable)
- ✅ Each item <334KB (per-request size limit, NOT token limit)
- ✅ Want 100% coverage (processes each item individually)

**Cost example (YouTube KB):**
- 195 videos via Batch API: $1.89 (189 processed)
- Same via direct API: $3.78
- Same via claude.ai Projects: ~$44-89 RAG charges over time
- **Savings:** 50-95% depending on alternative

### Size Limit Discovery (CRITICAL)
**Batch API limit:** 334KB per request (bytes, not tokens)

**What works:**
- ✅ Individual files 26-68KB: Process fine
- ❌ Consolidated 6.85MB file: Request rejected

**Prevention:**
1. Check file size before batching: `ls -lh file.json`
2. Individual source files <200KB = safe
3. Consolidated files = split into chunks <300KB each

### Batch Workflow
```python
# 1. Build batch JSONL file
for doc in documents:
    create_jsonl_request(doc.id, doc.content, prompt_template)

# 2. Submit to Batch API
batch_id = anthropic.batches.create(requests=jsonl_file)

# 3. Check status (6-24h later)
status = anthropic.batches.retrieve(batch_id)

# 4. Download results
results = anthropic.batches.results(batch_id)
```

**Cost discipline:** Always calculate total cost before submitting: `num_requests × avg_tokens × $7.50/M input × 0.5 (batch discount)`

### Pattern: regex-over-yaml
**Source:** Sessions 23-24 | **When to apply:** Any time you parse structured output from LLM-generated batch results

When processing Batch API results, prefer regex extraction over formal YAML/JSON parsers. LLMs don't perfectly follow format specs — prose fields regularly contain colons, brackets, and quotes that silently break YAML parsers. In the gold extraction batch (164 requests), YAML parsing failed on 120/164 documents due to colons in prose strings. Regex recovered all 164.

Rule: `yaml.safe_load()` fails silently on malformed LLM output. Use regex with explicit field patterns instead. Only fall back to YAML parsing for machine-generated config files, never for LLM-generated content fields.

### Pattern: batch-api-results
**Source:** Session 23 | **When to apply:** Any Batch API job result retrieval

Result processing pipeline: (1) check status via `anthropic.batches.retrieve(batch_id)`, (2) download as JSONL once `status == "ended"`, (3) parse line-by-line (NOT as JSON array — each line is independent JSON), (4) extract `result.message.content[0].text` field, (5) handle failures individually via `result.type == "error"`. Critical gotcha: `custom_id` has a 64-character max — validate before submission or the API silently truncates/rejects. Always validate custom_id format in build step, not at retrieval time.

---

## 6. Progressive Filtering Strategy

### Model Selection by Task
**Principle:** Use cheapest model that can do the job. Reserve expensive models for final quality pass.

| Task | Model | Cost | When to Use |
|------|-------|------|-------------|
| Test/validate approach | Haiku | $0.25/M | First 10-20% sample |
| Bulk processing | Sonnet | $3/M | Compression, extraction, categorization |
| Strategic synthesis | Opus | $15/M | Final quality pass, strategic decisions |

**Example workflow (YouTube KB):**
1. **Haiku test:** Process 20 videos to validate prompt ($0.05)
2. **Sonnet batch:** Process all 195 for extraction ($5-8)
3. **Opus review:** Strategic synthesis of patterns ($3-5)
4. **Total:** $8-13 vs $44 all-Opus approach = **70% savings**

### Progressive Filtering Example
```
Stage 1: Haiku filters 1000 items → 200 candidates ($1)
Stage 2: Sonnet extracts from 200 → 50 high-value ($3)
Stage 3: Opus deep-dives on 50 → final insights ($5)
Total: $9 vs $150 all-Opus = 94% savings
```

---

## 7. Routing Index Architecture

### Tier 0: Routing Index Specification

**Format:** YAML (best for human + LLM parsing)

**Required fields per entry:**
```yaml
- id: "001"
  file: "source-001.md"
  title: "Document Title"
  published: "2024-04-15"
  one_line: "Single sentence capturing core insight + mechanism + key concepts"
  tags: [tag1, tag2, tag3]
  key_concepts: [concept1, concept2]
  patterns: [pattern1, pattern2]
  quality: 5  # 1-5 scale
  strategic_value: "high"  # low/medium/high
  person: "Person Name or N/A"
  company: "Company Name or N/A"
```

**Critical field: `one_line`**
- Must state actionable insight (not just "this is about X")
- Include the mechanism (how/why)
- Use domain-specific language matching likely queries
- Stay under 250 characters (~50-60 tokens)

**Bad:** "A document about cost control"
**Good:** "How extreme cost discipline creates acquisition advantage — low costs → high margins → excess cash → ability to outbid competitors"

### Cross-Reference Maps (Automated)
Build inverted indexes from routing index:
```yaml
# topic-map.yaml (tag → doc IDs)
topics:
  ai-agents:
    count: 41
    docs: ["002", "005", "008", "012", ...]

# pattern-map.yaml (strategic patterns → doc IDs)
patterns:
  flywheel-loops:
    description: "Self-reinforcing cycles"
    count: 22
    docs: ["002", "008", "015", ...]

# concept-map.yaml (specific frameworks → doc IDs)
concepts:
  ai-loops:
    source_doc: "002"
    description: "Capture → classify → surface workflow"
    related_docs: ["005", "011", "023"]
```

### Related Documents (Auto-Generated)
```python
# Jaccard similarity with bonuses
relatedness_score(A, B) =
  |tags_A ∩ tags_B| / |tags_A ∪ tags_B|  # Base similarity
  + 0.5 × |patterns_A ∩ patterns_B|      # Pattern bonus
  + 0.3 × |concepts_A ∩ concepts_B|      # Concept bonus

# Threshold: 0.3, max 5 related docs per entry
```

**Why auto-generate:** Manual curation doesn't scale. Recompute when adding new docs.

---

## 8. Tier 1: Compressed Digests

### What Goes in a Digest (~1.5KB target)

```markdown
# Digest: Document Title
<!-- Source: analyses/001-source.md | ID: 001 -->

## Core Insight
2-3 sentences: what is the main transferable idea?

## Key Mechanics
- 4-6 bullet points explaining HOW and WHY
- Include specific mechanisms, not just outcomes

## Strategic Patterns
1. **Pattern name** — one-line description
2. **Pattern name** — one-line description

## Applicability
Explicitly states what queries should surface this document.
"Relevant to: X, Y, Z use cases"

## Key Quote
"Single most useful direct quote with timestamp/source"
```

### When to Load Digests vs Full Files

**Load digests when:**
- "What does KB say about X?"
- "Compare approaches to Y across sources"
- "Which documents cover Z?"
→ Synthesis across multiple sources

**Load full files when:**
- "Give me all details from doc X"
- "What are exact quotes about Y?"
- "Walk me through full analysis"
→ Depth on single source

**Rule:** Synthesis = digests. Depth = full files.

---

## 9. Build Workflow (Step-by-Step)

### Phase 1: Generate Routing Index
**Tool:** Claude Code reading all source files

```
For each source file:
  1. Parse YAML frontmatter (if exists)
  2. Extract summary section
  3. Compress to one_line via LLM
  4. Append to routing-index.yaml

Time: 5-10 minutes automated
Cost: $2-4 (Sonnet reading files once)
```

### Phase 2: Generate Cross-Reference Maps
```
1. Read routing-index.yaml
2. Build inverted indexes (tags, patterns, concepts → doc IDs)
3. Compute related documents via Jaccard similarity
4. Consolidate synonym tags (min 3-doc threshold)

Time: 2-5 minutes automated
Cost: $0 (pure computation)
```

### Phase 3: Generate Compressed Digests
**Model:** Sonnet 4.5 (not Opus — compression doesn't need top tier)

```
For each source file:
  1. Load full source
  2. Generate digest following template
  3. Save to _digests/digest-{id}.md

Time: 30-45 minutes for 195 files
Cost: $5-8 (Sonnet batch processing)
```

**Compression prompt (from Opus research):**
```
MUST KEEP:
- Named frameworks and coined terms
- Quantified claims (numbers, percentages)
- Contrarian/counterintuitive insights
- Anti-patterns and warnings
- ONE core strategic insight
- Specific tool/model recommendations

SAFE TO CUT:
- Section headers
- "How to Apply" sections (unless uniquely insightful)
- Generic ethical considerations
- Repeated qualification language
- Detailed formulas (unless they contain named metrics)
```

### Phase 4: Validate with Test Queries
```
1. Run 10 real queries against routing index
2. Check: Did it surface right candidates?
3. Check: Did digests answer without loading full files?
4. Adjust one_line summaries for missed items
5. Review tag consolidation needs
```

### Ongoing Maintenance
**When adding new document:**
```
1. Create full source file
2. Run index update: extract frontmatter → append to routing-index.yaml
3. Generate one_line summary → add to entry
4. Generate compressed digest
5. Update cross-reference maps (re-run inverted index builder)
6. Recompute related_docs (re-run similarity calculation)
```

**Should be single command:** "Add document [filename] to knowledge base index"

---

## 10. Quality Gates & Testing

### Before Large Query Sessions

**Pre-flight checklist:**
- [ ] Calculate total tokens: `file_size_MB × 250K tokens/MB`
- [ ] If >200K: Redesign as file-by-file processing
- [ ] If using full context: Include honesty prompt
- [ ] Budget per-item cost: `total_cost / items_actually_processed`
- [ ] Design for single-shot extraction (assume no cheap follow-ups)
- [ ] Test with 10-20% sample first

### After Query Sessions

**Post-flight assessment:**
- [ ] Ask Q5-style honesty: "What % did you actually read?"
- [ ] Check for extrapolation signals (6 tells listed in Section 2)
- [ ] Calculate actual per-item cost
- [ ] Document learnings in MEMORY.md
- [ ] Delete Project files if no more queries planned

### Quality Metrics

| Metric | Target | Bad | Good |
|--------|--------|-----|------|
| Routing index hit rate | >90% | Missed relevant docs | Found all candidates |
| Digest sufficiency | >80% | Needed full files often | Digests answered most queries |
| Cost per query | <$2 avg | $20+ per query | $0.50-1.50 per query |
| Processing coverage | 100% | Sampled 6.5% | Processed each item individually |

---

## 11. Reusable Patterns Discovered

### Pattern 1: Three-Tier Knowledge Base
**Context:** YouTube Research (196 videos, $89 spent)
**Impact:** 96% cost reduction per query
**Reusability:** Any structured document collection 50-2000 items
**Documentation:** `_shared/best-practices/knowledge-base-indexing.md`

### Pattern 2: Context Window Failure Modes
**Context:** $44 Opus Project with 1.7M tokens
**Impact:** Discovered 6.5% actual read rate, extrapolation contamination
**Reusability:** Any large context session >200K tokens
**Documentation:** `_shared/best-practices/context-window-failure-modes.md`

### Pattern 3: Batch API for Equal Treatment
**Context:** Processing 195 videos for $1.89
**Impact:** 50% cost savings + 100% coverage guarantee
**Reusability:** Any bulk processing 50+ similar items
**Documentation:** This document, Section 5

### Pattern 4: Progressive Model Filtering
**Context:** Haiku test → Sonnet bulk → Opus synthesis
**Impact:** 70-94% cost savings depending on task
**Reusability:** Any multi-stage workflow (filter → extract → synthesize)
**Documentation:** This document, Section 6

### Pattern 5: Duplication Prevention
**Context:** Nearly uploaded 6.9MB duplicate folder ($25/query cost)
**Impact:** Prevented $250+ wasted spend over 10 queries
**Reusability:** Any Claude Projects upload workflow
**Documentation:** MEMORY.md warning + this document, Section 4

### Pattern 6: Training Data Contamination Detection
**Context:** 10-15% of Opus output was training knowledge, not source content
**Impact:** Identified 6 detection signals for future quality checks
**Reusability:** Any LLM synthesis task claiming to summarize sources
**Documentation:** `context-window-failure-modes.md`, Section on Extrapolation

### Pattern 7: Quality Over Quantity
**Context:** 196 high-quality videos > 2000 random videos
**Impact:** Focused retrieval beats exhaustive documentation
**Reusability:** All knowledge base projects — curation is the advantage
**Documentation:** `CLAUDE.md` foundational principle

---

## 12. Cost Tracking Template

### Project Economics Dashboard
```markdown
| Item | Budget | Actual | ROI Notes |
|------|--------|--------|-----------|
| Research/design | $10-20 | $X | One-time |
| Routing index generation | $2-4 | $X | One-time |
| Cross-reference maps | $0 | $0 | Computation |
| Digest generation (195 docs) | $5-8 | $X | One-time |
| Validation queries | $5-10 | $X | One-time |
| **Total build cost** | **$22-42** | **$X** | |
| | | | |
| Query cost (old way) | $25/query | N/A | 100 queries = $2,565 |
| Query cost (new way) | $1/query | N/A | 100 queries = $100 |
| **Break-even** | **Query 1** | **✅** | **$2,465 saved over 100 queries** |
```

### Per-Query Cost Tracking
```markdown
| Query | Approach | Tokens | Cost | Notes |
|-------|----------|--------|------|-------|
| Q1 | Full context (baseline) | 1.7M | $25.50 | Discovery: sampling bias |
| Q2 | Tier 0 only | 8K | $0.20 | Browse: what do we have? |
| Q3 | Tier 0 + 10 digests | 23K | $0.50 | Synthesis across sources |
| Q4 | Tier 0 + 3 full files | 100K | $1.73 | Deep dive on specific topic |
```

---

## 13. Decision Framework for New Projects

### Should I Use This Architecture?

**✅ YES — use three-tier architecture if:**
- 50-2000 source documents
- Each document 10-100KB
- Expect 20+ queries over lifetime
- Need cross-source synthesis frequently
- Budget <$50 build cost

**⚠️ MAYBE — consider alternatives if:**
- <50 documents (might be overkill)
- Only need 1-5 queries total (just load directly)
- Documents change frequently (maintenance cost)
- Need real-time updates (index rebuild overhead)

**❌ NO — use simpler approach if:**
- <10 documents (just load them all)
- >5000 documents (need vector database)
- Unstructured/variable content (hard to compress)
- No budget for build phase

### Architecture Selection Matrix

| Collection Size | Structure | Query Frequency | Recommendation |
|----------------|-----------|-----------------|----------------|
| <50 docs | Any | Any | Load directly, no index |
| 50-500 docs | Structured | >20 queries | ✅ Three-tier architecture |
| 500-2000 docs | Structured | >50 queries | ✅ Three-tier + split indexes |
| >2000 docs | Structured | >100 queries | Vector DB + semantic search |
| Any size | Unstructured | Ad-hoc | Claude Projects RAG |

---

## 14. Applying to Your New Idea

### Step 1: Assess Your Project

**Answer these questions:**
1. How many source items? (aim for 50-500 sweet spot)
2. What's average item size? (target 10-50KB each)
3. How many queries expected? (>20 = build index worthwhile)
4. Is content structured? (consistent format = easier to compress)
5. What's your budget? ($50 build = $2,400 saved over 100 queries)

### Step 2: Design Your Data Model

**Define your equivalents:**
- **Routing index fields:** What metadata identifies/categorizes your items?
- **Tags/concepts/patterns:** What's your classification taxonomy?
- **one_line format:** What's the core insight structure?
- **Digest template:** What 4-6 sections capture essence?

### Step 3: Pilot Before Scaling

**10-item pilot checklist:**
- [ ] Process 10 items manually (understand patterns)
- [ ] Build routing index entries (test metadata design)
- [ ] Generate 10 digests (validate compression prompt)
- [ ] Run 5 test queries (confirm retrieval accuracy)
- [ ] Calculate actual costs (budget for full build)
- [ ] **Decision gate:** Build full system or pivot?

### Step 4: Build in Phases

**Phase order:**
1. **Week 1:** Routing index (5-10 min automated, $2-4)
2. **Week 1:** Cross-reference maps (2-5 min automated, $0)
3. **Week 2:** Compressed digests (30-45 min automated, $5-8)
4. **Week 2:** Validation with 10 test queries
5. **Week 3:** Adjust based on learnings, finalize

**Total timeline:** 2-3 weeks part-time
**Total cost:** $8-15 one-time
**Payback:** Query 1

---

## 15. Success Criteria

### You know it's working when:
- ✅ Query costs drop 85-95% vs full-context baseline
- ✅ Retrieval accuracy >90% (finds relevant docs reliably)
- ✅ Digest sufficiency >80% (most queries answered without full files)
- ✅ No sampling bias (each item processed individually)
- ✅ Build cost paid back in first 1-2 queries

### You know it's NOT working when:
- ❌ Still loading full context (defeats the purpose)
- ❌ Routing index misses relevant docs frequently
- ❌ Digests too thin (always need full files anyway)
- ❌ Maintenance burden exceeds query value
- ❌ Queries take longer than just loading directly

---

## Checklist: Applying This to New Project

**Planning phase:**
- [ ] Count source items (50-500 = sweet spot)
- [ ] Check average item size (10-50KB = ideal)
- [ ] Estimate query frequency (>20 = worthwhile)
- [ ] Calculate baseline cost (items × size × $15/M tokens)
- [ ] Design metadata taxonomy (tags, concepts, patterns)

**Build phase:**
- [ ] Process 10-item pilot first (validate approach)
- [ ] Generate routing index with one_line summaries
- [ ] Build cross-reference maps (automated)
- [ ] Generate compressed digests (Sonnet batch)
- [ ] Run 10 test queries (validate retrieval)

**Quality phase:**
- [ ] Check routing accuracy (>90% hit rate)
- [ ] Check digest sufficiency (>80% answer without full files)
- [ ] Calculate cost reduction (target 85-95%)
- [ ] Document learnings in project MEMORY.md
- [ ] Add any new patterns to _shared/best-practices/

---

## Appendix: Real Project Economics

### YouTube Research KB — Full Cost Breakdown

| Phase | Activity | Cost | Notes |
|-------|----------|------|-------|
| Phase 0 | Foundation research | $3 | Opus strategic guidance |
| Phase 1 | 6 manual analyses (pilot) | $0 | Claude Code (free) |
| Phase 2 | Batch API (189 videos) | $20 | Haiku $1.89 actual |
| Phase 3 | Routing index build | $0 | Claude Code extraction |
| Phase 3 | Cross-reference maps | $0 | Pure computation |
| Phase 3 | Opus Project Q1-Q6 | $4 | RAG retrieval (6 questions) |
| Mistakes | Full context query | $44 | Discovery: sampling bias |
| Strategic | Opus review batch | $3-5 | Week 1 utilization strategy |
| **Total** | | **~$75-89** | |

**Value delivered:**
- 196 videos analyzed and indexed
- 7 reusable patterns documented
- 4 context window failure modes discovered
- 96% cost reduction architecture proven
- Strategic framework for 50-user rollout

**Conservative ROI:** 10-50x (prevented mistakes, delivered reusable patterns for 10 companies)

### Projected Economics for Similar Project

**Assumptions:** 200 documents, 30KB average, 100 queries over 3 years

| Item | Old Way | New Way | Savings |
|------|---------|---------|---------|
| Build cost | $0 | $15 | -$15 |
| Query 1-100 | $2,565 | $100 | +$2,465 |
| **Net 3-year** | **$2,565** | **$115** | **$2,450 (95%)** |

**Break-even:** Query 1
**Per-company value:** $2,450
**×10 companies:** $24,500 savings
**Investment:** $150 (10 × $15)
**Net:** $24,350 saved

---

**Last Updated:** 2026-02-12
**Next Review:** After first new project applies this framework
**Owner:** 1658 Holdings Oy — compounding infrastructure team

---

*This is a living document. Update it when new patterns emerge or when costs/capabilities change.*
