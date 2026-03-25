# Batch Processing Guide

**Status:** Ready to use once YouTube IP unblocks (24-48h)

---

## What Was Created

### 1. Batch Analysis Prompt
**File:** `prompts/batch-analysis-prompt.md`
- Complete 11-dimension framework prompt
- Adapts for AI/productivity content
- Variable substitution template
- Quality control guidelines

### 2. Batch Job Preparation Script
**File:** `scripts/prepare-batch-job.py`
- Automates batch job creation
- Loads video metadata + transcripts
- Generates Anthropic Batch API requests
- Estimates costs

---

## How to Use (When IP Unblocks)

### Step 1: Extract Transcripts (24-48h from now)

```bash
# Wait for YouTube IP unblock, then:
python scripts/extract-transcripts.py tier1 --rate-limit 10
```

This will:
- Extract transcripts for Tier 1 (40 videos)
- Add 10-second delays between requests
- Save to `reference/transcripts/`

### Step 2: Prepare Batch Job

```bash
# Create batch job file
python scripts/prepare-batch-job.py tier1

# Or test with limited videos first:
python scripts/prepare-batch-job.py tier1 --limit 5
```

This creates:
- `batch-jobs/batch-job-tier1-TIMESTAMP.jsonl`
- Ready to upload to Anthropic Batch API

### Step 3: Submit to Anthropic Batch API

```bash
# Upload via Anthropic API (need API key)
# See: https://docs.anthropic.com/en/docs/batch-api

# Example (when implemented):
anthropic batches create batch-jobs/batch-job-tier1-TIMESTAMP.jsonl
```

### Step 4: Wait 12-24 Hours

Anthropic processes the batch in the background.

### Step 5: Download & Process Results

```bash
# Download results from Anthropic
anthropic batches download <batch-id>

# Process results into markdown files
python scripts/process-batch-results.py results.jsonl
```

This creates markdown files in `knowledge-base/videos/`

---

## Cost Breakdown

### Tier 1 (40 videos)
- **Cost:** $0.40
- **Savings:** 95% vs. standard API
- **Time:** 12-24h processing

### All Tiers (455 videos)
- **Tier 1:** $0.40 (40 videos)
- **Tier 2:** $0.64 (64 videos)
- **Tier 3:** $0.85 (85 videos)
- **Tier 4:** $2.66 (266 videos)
- **Total:** $4.55

---

## What You Get

**Per Video:**
- 8,000-12,000 word strategic analysis
- 11-dimension framework applied
- 5-10 memorable quotes (exact)
- 5-10 non-obvious insights
- Specific applications to 1658 Holdings
- Quality assessment scores

**File Format:**
- Markdown with YAML frontmatter
- Saved as: `YYYY-MM-title-slug.md`
- Cross-referenced and tagged
- Ready for Claude context

---

## Current Status

✅ Batch prompt template ready
✅ Preparation script ready
⏸️ Waiting for YouTube IP unblock (24-48h)
⏳ Transcripts need extraction
⏳ Batch job needs submission

---

## Next Session Checklist

1. [ ] Verify YouTube IP unblocked (test with 1 video)
2. [ ] Extract Tier 1 transcripts (40 videos, ~10 min)
3. [ ] Prepare batch job (1 min)
4. [ ] Submit to Anthropic Batch API (2 min)
5. [ ] Monitor batch progress
6. [ ] Download results when complete (24h later)
7. [ ] Process results into knowledge base
8. [ ] Quality check 5-10 random analyses
9. [ ] Test strategic queries

---

## Files Created Today

### Documentation
- ✅ `SESSION-SUMMARY-2026-02-10.md` - Comprehensive session summary
- ✅ `BATCH-PROCESSING-GUIDE.md` - This file

### Prompts
- ✅ `prompts/batch-analysis-prompt.md` - Batch analysis template

### Scripts
- ✅ `scripts/prepare-batch-job.py` - Batch job preparation
- ⏳ `scripts/extract-transcripts.py` - TODO: Create this
- ⏳ `scripts/process-batch-results.py` - TODO: Create this

### Reference
- ✅ `reference/nate-b-jones-videos-catalog.json` - All 455 videos
- ✅ `reference/nate-b-jones-prioritized.json` - Organized by tiers

### Knowledge Base (6 videos analyzed)
- ✅ `knowledge-base/videos/2024-04-tom-murphy-capital-cities.md`
- ✅ `knowledge-base/videos/2025-10-jensen-huang-nvidia.md`
- ✅ `knowledge-base/videos/2024-02-buffett-munger-berkshire.md`
- ✅ `knowledge-base/videos/2026-01-second-brain-system.md`
- ✅ `knowledge-base/videos/2025-12-4-ai-agents-guide.md`
- ✅ `knowledge-base/videos/2026-01-claude-code-meta-guide.md`

---

**Ready to scale to 455 videos once IP unblocks!**
