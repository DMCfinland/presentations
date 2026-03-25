# Three-Tier Knowledge Base Build Plan

**Date:** 2026-02-11
**Status:** Step 1 DONE, Step 3 DONE — Tier 0 operational, Tier 1 (digests) deferred
**Architecture:** Based on `_shared/best-practices/knowledge-base-indexing.md` (Opus research)

---

## Architecture: Three-Tier Retrieval System

```
Tier 0: Routing Index    (~30KB YAML)  → loaded on every query
Tier 1: Compressed Digests (~300KB)    → loaded selectively (5-20 at a time)
Tier 2: Full Source Files  (6.9MB)     → loaded on demand (1-5 at a time)
```

| Scenario | What loads | Tokens | Cost (Opus) |
|---|---|---|---|
| Browsing/discovery | Tier 0 only | ~22K | ~$0.33 |
| Topical research | Tier 0 + 10 digests | ~20K | ~$0.30 |
| Deep analysis | Tier 0 + 5 digests + 3 full files | ~85K | ~$1.30 |
| Current (broken) | All 195 full files | ~1,700K | ~$25.50 |

**Target: 96% cost reduction per query ($25.50 → ~$1.00 average)**

---

## Build Steps (Sonnet Direct, not Batch)

### Step 1: Build Routing Index — DONE ✅ ($0)

Extracted YAML frontmatter from all 196 files via bash, generated `one_line` summaries via smart extraction from summary paragraphs. Done entirely in Claude Code (no API cost).

**Output:** `knowledge-base/_index/routing-index.yaml` (87KB, 196 entries)
- 96% one_line quality rate (189/196 good, 7 slightly long)
- Fields: file, title, one_line, tags (top 4), quality, person (if any)
- Full metadata (key_concepts, patterns, strategic_value) stays in source files
- 87KB vs 30KB target — acceptable: still 99% reduction from 1.7M tokens

**Method:** bash frontmatter extraction → Python data transformation → LLM-quality one_line via insight-marker detection in summaries. Zero API cost.

### Step 2: Generate Compressed Digests (~$5-8)

Process each of 195 files through Sonnet. Each digest: ~1.5KB.

**Output:** `knowledge-base/_digests/digest-{id}.md` (195 files, ~300KB total)

**Compression prompt (Opus-designed, from Q10):**

```
You are compressing a video analysis document into a ~1.5KB digest. Preserve ONLY:

MUST KEEP:
- Named frameworks and coined terms (exact vocabulary, e.g., "Ferrari failure mode")
- Quantified claims (specific numbers, percentages, dollar amounts)
- Contrarian/counterintuitive insights (anything that challenges conventional wisdom)
- Anti-patterns and specific warnings ("don't do X because Y")
- The ONE core strategic insight the video offers
- Temporal markers (when capabilities crossed thresholds)
- Specific tool/model recommendations with use cases

SAFE TO CUT:
- Section headers and framework labels
- "How to Apply to 1658 Holdings" sections (keep only if uniquely insightful)
- Quality Assessment sections
- Generic ethical considerations
- Repeated qualification language ("This represents a fundamental shift...")
- Detailed metric formulas unless they contain a named metric
- "When to Use / When NOT to Use" unless conditions are specific and surprising

FORMAT: YAML front matter (title, date, tags, key_concepts) + prose digest.
Start with the one-sentence core insight. Then frameworks/vocabulary.
Then anti-patterns. Then quantified claims. End with the single most
memorable quote.

CRITICAL: If unsure whether to keep something, keep named terms and cut
generic analysis.
```

**Known compression risks (from Opus Q10 analysis):**
1. Reasoning chains behind conclusions get lost — consider adding "include one sentence of WHY for each framework"
2. Cross-video connections impossible in file-by-file processing — handled by Step 3 cross-reference maps
3. Nuanced conditions ("use X, BUT NOT when Y") get flattened — prompt says keep "specific and surprising" conditions
4. Temporal evolution flattened — handled by date field in YAML front matter

**QA process:** After generation, manually review digests for the 10 Greatest Hits videos (see `_index/greatest-hits-10.md`). If key frameworks are missing, tune the prompt.

**Cost calculation (Sonnet direct):**
- Input: 195 × ~9K tokens = 1.76M tokens × $3/M = $5.28
- Output: 195 × ~400 tokens = 78K tokens × $15/M = $1.17
- **Total: ~$6.45**

### Step 3: Build Cross-Reference Maps — DONE ✅ ($0)

Pure computation from frontmatter — no LLM needed. Generated:

- `_index/topic-map.yaml` — tag → document IDs (inverted index)
- `_index/pattern-map.yaml` — pattern → document IDs
- `_index/concept-map.yaml` — concept → document IDs
- Auto-generate `related_videos` via Jaccard similarity (threshold 0.3, max 5)
- Consolidate synonym tags (min 3-doc threshold for topic map)

### Step 4: Validate (10 test queries)

Run 10 real queries against the index to verify retrieval accuracy.

---

## Folder Structure After Build

```
knowledge-base/
├── _index/
│   ├── routing-index.yaml        # Tier 0 (~30KB)
│   ├── topic-map.yaml            # Tag → doc IDs
│   ├── pattern-map.yaml          # Pattern → doc IDs
│   └── concept-map.yaml          # Concept → doc IDs
├── _digests/
│   ├── digest-001.md             # Tier 1 (~1.5KB each)
│   ├── digest-002.md
│   └── ... (195 files, ~300KB)
├── videos/                       # Tier 2 (full files, 6.9MB)
│   ├── 2024-02-06-5-big-ai...md
│   └── ... (195 files)
└── _archive/
    └── consolidated-videos-context.md  # DO NOT LOAD (6.85MB)
```

---

## Expensive Project Follow-Ups (Q1-Q6) — COMPLETE ✅

All 6 answers received and saved to `opus-project-followups/`. Key learnings:

| Q# | File | Key Finding | Build Impact |
|----|------|-------------|--------------|
| Q1 | q1-topic-clusters.md | 15 clusters, but only directional (~15% sample) | Validation check for topic-map, not source of truth |
| Q2 | q2-compression-priorities.md | 8 high-density, 4 compressible categories | Human review list for post-digest QA |
| Q3 | q3-holdings-applicability.md | 4-persona map (CEO/DMC/hotel/docs) | `applicability` field in routing index |
| Q4 | q4-missing-gaps.md | 8 gaps (EU/Finnish, multi-lang, B2B tourism, etc.) | Future research directions, `known_gaps` metadata |
| Q5 | q5-context-rot-assessment.md | **6.5% read, 75% unread, $44 for 30 videos** | DEFINITIVE proof for file-by-file processing |
| Q6 | q6-retrieval-quality-test.md | Primacy/recency bias confirmed, middle blank | Equal-treatment processing eliminates position bias |

**Critical Discovery:** Opus sampled 14 windows of ~500 lines from a 107K-line file. Synthesis was pattern extrapolation from ~30 videos, not faithful distillation of 195. This validates the three-tier architecture completely.

## New Follow-Ups (Q7-Q12) — READY TO SEND

See `opus-project-followups/q7-q12-ready-to-send.md` for the questions.
These extract remaining value from the still-open Opus conversation (cheap queries, ~$0.50 each).

---

## Cost Tracking

| Item | Estimated | Actual |
|------|-----------|--------|
| Opus indexing research | $1-3 | DONE (saved to best-practices) |
| Opus Project follow-ups (Q1-Q6) | $2-4 | ✅ DONE (~$2-4) |
| Opus Project follow-ups (Q7-Q12) | $2-4 | Ready to send |
| Routing index generation | $2-4 | ✅ $0 (done in Claude Code) |
| Cross-reference maps | $0 (computation) | ✅ $0 (done in Claude Code) |
| Sonnet: digest generation (196 files) | $5-8 | DEFERRED (test without first) |
| **Total** | **$10-19** | **~$4-8 spent, $5-8 deferred** |

**Break-even: 1st query that would have loaded full context**

---

## Future: Batch API Best Practices

Defer to later: research and document when to use Batch API (50% off, 24h wait)
vs. direct API for these kinds of bulk operations. Could save ~$3-4 on this job.
Build as reusable best practice for all portfolio knowledge bases.
