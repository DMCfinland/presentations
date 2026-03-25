# Research Mining Workflow — Extract Knowledge Gold from Any Corpus

**Version:** 2.0
**Date:** 2026-02-16
**Status:** Production-ready (v3 prompt validated, batch JSONL generated)
**Validated:** 20 test runs, 15 unique documents, 3 prompt iterations
**Proven on:** YouTube KB (196 videos indexed, 164 active)

---

## Overview

Single-stage Sonnet pipeline extracts actionable insights ("gold") directly from raw research documents. Optional Opus synthesis finds cross-corpus patterns.

**Key principle:** Precision over recall. 5 genuine insights > 10 padded ones.

**What changed from v1 (3-stage):**
- Killed Stage 1 (Haiku compression) — single Sonnet pass is $0.89 cheaper AND simpler
- Reduced insight types from 8 to 5 (eliminated type blurring)
- Added NO GOLD pre-screening (news roundups correctly filtered)
- Added anti-contamination rules (analyst commentary ≠ source insight)

---

## When to Use This Workflow

**Use for:** Research corpora (50+ structured documents) where you want strategic insights
**Don't use for:** <10 docs (just read them), operational retrieval (needs full text), unstructured dumps (index first)
**Prerequisites:** Structured markdown docs, routing index exists, deprecated items flagged

---

## Architecture: Single-Stage + Optional Synthesis

```
┌─────────────────────────────────────────────────────────────────┐
│ SONNET GOLD EXTRACTION (Batch API)                              │
│ Input: Raw documents (~35KB each, 164 files)                    │
│ Output: 0-12 gold insights per document (YAML)                  │
│ Cost: ~$3 for 164 docs (batch + prompt caching)                 │
│ Time: 2-24 hours (batch processing)                             │
│                                                                 │
│ System prompt (cached): Pre-screening + 5 insight types         │
│ User message (unique): Raw document content                     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ OPTIONAL: OPUS CROSS-SYNTHESIS                                  │
│ Input: All gold nuggets from extraction (~1000 insights)        │
│ Output: Mega-patterns, contradictions, priority stack           │
│ Cost: $3-5 per synthesis run                                    │
│ Approach: Topic-cluster synthesis (not single 164K query)       │
└─────────────────────────────────────────────────────────────────┘
```

### Why Not Haiku Compression First?

Tested and rejected. Numbers:
- 2-stage (Haiku + Sonnet batch): $3.44 + complexity of managing intermediate files
- 1-stage (Sonnet batch direct): $2.97 with prompt caching
- Single pass is **cheaper**, simpler, and avoids contamination risk from Haiku adding training knowledge

### Cost by Corpus Size

| Corpus Size | Sonnet Extraction | Opus Synthesis | Total |
|-------------|-------------------|----------------|-------|
| 50 docs     | ~$1               | $2-3           | ~$3-4 |
| 164 docs    | ~$3               | $3-5           | ~$6-8 |
| 500 docs    | ~$9               | $5-8           | ~$14-17 |

All costs assume Batch API (50% discount) + prompt caching (90% off system prompt).

---

## The v3 Prompt (Validated)

### Pre-Screening (NO GOLD trigger)

Automatic gold_count: 0 if ANY apply:
- Document covers 3+ unrelated news stories
- Title contains "breakdown", "your X-minute", "this week"
- Content primarily reports WHAT happened, not analyzes WHY
- Document is a product review listing features without strategy

**Validation:** News roundup correctly triggered NO GOLD in testing (was 7 false insights in v2).

### 5 Insight Types

| Type | Definition | Quality Gate |
|------|-----------|-------------|
| FRAMEWORK | Named model/mental model from source author | Must have a name or clear structure |
| ANTI_PATTERN | "Don't do X because Y" warning | Must include mistake AND consequences |
| METRIC | Quantified claim (number, %, $) | Must be novel or surprising |
| CONTRARIAN | Contradicts conventional wisdom | Must state both views |
| TECHNIQUE | Step-by-step procedure | Must have 2+ concrete steps |

**Why 5, not 8:** Testing showed PATTERN blurred with FRAMEWORK, PREDICTION blurred with CONTRARIAN, TENSION was too rare. 5 types = clean classification.

### Extraction Rules

1. **Precision over recall** — every false positive wastes downstream Opus tokens
2. **Source content only** — if it uses academic/analytical language not in the source's quotes/frameworks, skip it
3. **Non-obvious test** — would a smart person know this from title + summary alone?
4. **Max 12 per document** — if more, keep only most non-obvious
5. **Actionability = source author's recommendation** — not AI's opinion
6. **<2 insights passing = gold_count: 0** with explanation

### Sections to Ignore

Quality Assessment, "How to Apply to 1658 Holdings", Version History, Related Content, Notes & Questions, analyst commentary from prior analysis passes.

### Full Prompt

See: `YouTubeResearch-AIFiles/scripts/prepare-gold-extraction-batch.py` → `SYSTEM_PROMPT` constant

---

## Execution

### 1. Generate Batch JSONL

```bash
cd YouTubeResearch-AIFiles
python scripts/prepare-gold-extraction-batch.py           # Generate JSONL
python scripts/prepare-gold-extraction-batch.py --dry-run  # Stats only
python scripts/prepare-gold-extraction-batch.py --limit 5  # Test subset
```

Output: `batch-jobs/gold-v3-sonnet-{timestamp}.jsonl`

**Key architecture decision:** System prompt is in `system` field (not `messages`), enabling prompt caching across all 164 requests. Saves ~$0.18 on this corpus, more on larger ones.

### 2. Submit Batch

```python
import anthropic, json

client = anthropic.Anthropic()  # Needs ANTHROPIC_API_KEY
with open('batch-jobs/gold-v3-sonnet-{timestamp}.jsonl') as f:
    requests = [json.loads(l) for l in f]

batch = client.messages.batches.create(requests=requests)
print(f'Batch ID: {batch.id}')
# Save batch ID — needed for retrieval
```

### 3. Retrieve Results (2-24h later)

```python
batch = client.messages.batches.retrieve(batch_id)
if batch.processing_status == "ended":
    for result in client.messages.batches.results(batch_id):
        # Save each result to _gold/ as YAML
        save_gold(result.custom_id, result.result.message.content)
```

### 4. Validate

Check 10 "greatest hits" documents:
- [ ] Named frameworks preserved with exact vocabulary?
- [ ] Insights are standalone (make sense without document)?
- [ ] NO GOLD verdicts correct (news roundups filtered)?
- [ ] No analyst commentary contamination (source language only)?
- [ ] Actionability describes source author's recommendation?

### 5. Optional: Opus Cross-Synthesis

Use topic clusters from routing index rather than single query:
1. Group gold nuggets by topic (from `topic-map.yaml`)
2. Synthesize per cluster with Opus ($1-2 per cluster)
3. Meta-synthesize across clusters ($2-3)

This avoids context rot from loading all 1000+ nuggets in one window.

---

## Prompt Iteration History

| Version | Changes | Test Results |
|---------|---------|-------------|
| v1 (old script) | 8 insight types, 10 cap, no pre-screening | ~20% contamination, no NO GOLD filtering |
| v2 | 5 types, anti-contamination rule, actionability fix | NO GOLD still failed, ~15% contamination |
| v3 (production) | Explicit NO GOLD trigger, commentary filter, 12 cap | NO GOLD working, ~5-10% contamination, 20/20 YAML valid |

### Learnings Applied

1. **NO GOLD requires explicit format detection** — "fewer than 2 non-obvious insights" is too subjective for Sonnet. Explicit title/format patterns work.
2. **"Source content only" beats "don't add commentary"** — positive instruction (only use source language) is more effective than negative instruction (don't add your own).
3. **Cap of 12 is right** — 10 was too low for rich sources (3 docs hit cap). 12 allows full extraction. Diminishing returns above 12.
4. **Batching 3-5 files per Task tool session works** for testing — no cross-contamination, saves overhead.
5. **System prompt in `system` field** enables Batch API prompt caching — every identical prefix is cached after request #1.

---

## Folder Structure After Execution

```
knowledge-base/
├── _index/
│   ├── routing-index.yaml        # 196 entries, 32 deprecated
│   ├── topic-map.yaml            # Tag → doc IDs
│   ├── pattern-map.yaml          # Pattern → doc IDs
│   └── concept-map.yaml          # Concept → doc IDs
├── _gold/                        # Sonnet extraction output
│   ├── 2024-02-buffett-munger-berkshire.yaml
│   └── ... (164 files, YAML format, ~500KB total)
├── _synthesis/                   # Opus cross-synthesis output
│   ├── cross-video-synthesis.md
│   └── priority-stack.md
├── videos/                       # Original analyses (6.9MB)
│   └── ... (196 files)
└── _archive/
    └── consolidated-videos-context.md  # DO NOT LOAD (6.85MB)
```

---

## Reuse: Applying to Other Corpora

Same pipeline, different gold targets:

| Corpus | Gold Target | Synthesis Lens |
|--------|------------|----------------|
| YouTube KB (current) | Named frameworks, strategies, anti-patterns | Portfolio implications for 1658 Holdings |
| Business documents (planned) | Contract patterns, governance gaps, financial trends | Cross-company risk flags |
| Competitor research (future) | Positioning gaps, pricing patterns | Market opportunities |

For new corpora: adjust the IGNORE SECTIONS list and possibly the insight type definitions, but the architecture stays the same.

---

## Quality Metrics

| Metric | v1 | v3 (production) |
|--------|----|----|
| False positive rate | ~20% | ~5-10% |
| NO GOLD accuracy | 0% (never triggered) | 100% (1/1 news roundup filtered) |
| YAML validity | unknown | 20/20 (100%) |
| Avg insights/doc | ~6 | ~7.3 |
| Analyst contamination | ~20% of docs | ~5-10% of docs |
| Type blurring | frequent | rare |

---

*This is a living workflow. Update after each execution with learnings.*
*Last Updated: 2026-02-16 (v2.0 — validated single-stage architecture)*
*Next: Submit batch, retrieve results, run validation*
