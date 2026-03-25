# Context Window Failure Modes
<!-- last_updated: session-28 -->

**Date:** 2026-02-11
**Source:** Empirical evidence from Opus claude.ai Project processing 195 YouTube video analyses (1.7M tokens)
**Evidence:** `YouTubeResearch-AIFiles/opus-project-followups/q5-context-rot-assessment.md` and `q6-retrieval-quality-test.md`

---

## The Core Rule

> **Large context ≠ processed context.** Loading 1M+ tokens does not mean the model reads 1M+ tokens. It samples, extrapolates, and fills gaps from training data. You pay for the full context but get partial processing.

---

## Failure Mode 1: Sampling Bias

**What happens:** When a file exceeds the model's effective processing capacity, it reads representative samples (beginning, end, and scattered middle sections) rather than every line.

**Evidence:** Opus loaded a 107,340-line file (1.27M tokens). It read 14 samples of ~500 lines each — 7,000 lines total (6.5%). It deeply engaged with 25-30 items out of 195.

**Cost impact:** $44 spent. Per-item cost of items actually processed: ~$1.50. Per-item cost of unread items: $0 value, full cost.

**Prevention:**
- Never load >200K tokens and expect faithful line-by-line processing
- Process files individually or in small batches (5-20 at a time)
- If you must load large context, design queries that only need pattern-level answers (not item-level)

## Failure Mode 2: Primacy/Recency Bias

**What happens:** Models recall content from the beginning and end of large documents much better than the middle. This is well-documented in research and now empirically confirmed.

**Evidence:** Opus recalled specific quotes from first 20 and last 20 videos. For the middle (videos 80-120), it could only recall 2 items where its samples happened to land. Could not name a single video title from the middle range. Failed to produce a 5th insight and gave up.

**Prevention:**
- Don't rely on position-dependent processing for important content
- If loading a large file, put the most critical content at the beginning
- Better: process each item individually so position is irrelevant

## Failure Mode 3: Confident Extrapolation

**What happens:** The model fills gaps between samples using pattern recognition and training data. The output reads as comprehensive but is actually "30 data points + inference." The model may not flag this unless explicitly asked.

**Evidence:** Opus's strategic synthesis read as a faithful analysis of 195 videos. Only when directly asked "did you process all 195 equally? Be honest" did it reveal the 6.5% sampling. The extrapolated patterns were real (they appeared in the samples) but the claimed coverage was not.

**Prevention:**
- Always ask the model to self-assess its coverage honestly
- Include Q5-style honesty prompts in expensive sessions: "What percentage did you actually read?"
- Design prompts that request item-level evidence, not just pattern-level synthesis
- If the model can't cite specific items from the middle of the dataset, it didn't read them

## Failure Mode 4: RAG Chunk Gambling

**What happens:** With RAG (Project Knowledge), the system retrieves relevant chunks, not the full dataset. You get 10K-150K tokens of context, not 1.7M. This is usually better for targeted queries but means you're gambling on chunk selection for broad queries.

**Evidence:** Opus confirmed RAG would have been better for specific queries ("what does Nate say about SharePoint?") but worse for cross-corpus pattern recognition. RAG retrieves topically similar content, which can miss temporal shifts and cross-domain connections.

**Prevention:**
- Use RAG for specific, targeted queries (it excels here)
- Use full context (but <200K tokens) for pattern recognition and synthesis
- For large datasets, build a routing index first, then do targeted retrieval

---

## The Decision Framework

| Dataset Size | Approach | Expected Coverage | Cost |
|-------------|----------|-------------------|------|
| <50K tokens | Full context | ~100% | Low |
| 50-200K tokens | Full context | ~80-95% | Medium |
| 200K-500K tokens | Full context with honesty check | ~40-60% | High |
| 500K-1M tokens | RAG or file-by-file processing | Varies by approach | Medium-High |
| >1M tokens | File-by-file processing ONLY | 100% (by design) | Depends on file count |

---

## The Three-Tier Solution

Built from this failure mode analysis:

```
Tier 0: Routing Index    (~30KB)  → every item summarized individually, 100% coverage
Tier 1: Compressed Digests (~300KB) → each file processed alone, no position bias
Tier 2: Full Source Files  (6.9MB)  → loaded on demand, 1-5 at a time, full fidelity
```

This architecture makes context rot structurally impossible because no processing step loads more than one file at a time.

---

## Checklist: Before Any Large Context Session

1. [ ] Calculate total tokens (file_size_MB × 250K tokens/MB)
2. [ ] If >200K tokens: redesign as file-by-file processing
3. [ ] If using full context anyway: include honesty prompt ("what % did you actually read?")
4. [ ] Budget for the real per-item cost (total_cost / items_actually_processed)
5. [ ] Design for single-shot extraction (assume no cheap follow-ups unless files are deleted)
6. [ ] After session: ask Q5-Q6 style self-assessment questions before trusting synthesis

---

## Extrapolation Detection Signals (from Opus Q12 — first-person account)

When reading a large-context output, watch for these tells that the model is extrapolating rather than recalling:

1. **Vague attribution** — "Across the corpus..." or "The research consistently shows..." without naming specific sources. Honest version: "From the videos I reviewed..." with specific cites.
2. **Generic advice as content-specific insight** — If an insight could appear in any AI strategy article ("start small and iterate"), it's training knowledge, not source-specific.
3. **Smooth narrative without friction** — Real recall includes oddities and surprises. When every point supports the thesis perfectly, the model is constructing a story from fragments.
4. **Confident comprehensiveness** — "All 195 videos converge on..." is a fabrication signal when the model read 15%. Watch for the word "all."
5. **Absence of "I don't know"** — A model that never admits gaps in a large-context task is filling them.
6. **Consistent quality across sections** — Real recall is lumpy. Some sections rich with detail, others thin. Uniform quality = generated, not recalled.

### Content Source Breakdown (Opus's Honest Estimate)
- **60-70%** grounded in what was actually read
- **~20%** reasonable pattern extrapolation
- **10-15%** training knowledge presented as source content ("the most dangerous mode")

### The Optimal Submission Architecture
For any knowledge base >200K tokens, build three layers:
1. **Navigation index** (~5KB, always in context) — title, tags, one-sentence insight per item
2. **Compressed digests** (~1-1.5KB each) — enough for most queries + routing to full docs
3. **Full documents** (retrieved on demand) — 3-5 at a time for deep analysis

Query flow: Index → Digests → Full docs. **Never dump everything into one file.**
