# Opus vs Sonnet Comparison Test

## Strategy: Scientific A/B Test Before Full Rollout

Instead of blindly upgrading all 189 videos to Opus, let's test first with your existing 6 videos.

### Why This Is Smart:

1. ✅ **Low cost** - Test with 6 videos (~$5) before committing to full batch (~$50)
2. ✅ **Real comparison** - Side-by-side analysis quality measurement
3. ✅ **Data-driven decision** - Measure if Opus is worth 6x the cost
4. ✅ **Keep Sonnet work** - All baseline analyses preserved
5. ✅ **Learn first** - Understand quality differences before scaling

## Your Current Situation

**6 videos already analyzed** (probably Sonnet, or manual):
- `2025-12-4-ai-agents-guide.md`
- `2026-01-second-brain-system.md`
- `2025-10-jensen-huang-nvidia.md`
- `2024-02-buffett-munger-berkshire.md`
- `2026-01-claude-code-meta-guide.md`
- `2024-04-tom-murphy-capital-cities.md`

**Next:** 189 videos in Sonnet batch (currently processing)

## Comparison Test Workflow

### Step 1: Create Comparison Batch

```bash
# Re-analyze your existing 6 videos with Opus
python scripts/create-comparison-batch.py --all
```

**What it does:**
- Finds all existing videos in `knowledge-base/videos/`
- Fetches their transcripts
- Creates Opus batch JSONL for comparison
- Cost: ~$5 for 6 videos

**Output:**
- `batch-jobs/batch-job-comparison-[timestamp].jsonl`
- `opus-comparison/comparison-manifest-[timestamp].json`

### Step 2: Upload Comparison Batch

**Option A: Using upload script (if updated):**
```bash
python scripts/upload-batch-jobs.py comparison
```

**Option B: Manual (if script not updated):**
```python
import anthropic
import json

client = anthropic.Anthropic()

with open('batch-jobs/batch-job-comparison-[timestamp].jsonl', 'rb') as f:
    batch = client.messages.batches.create(requests=f)

print(f"Batch ID: {batch.id}")

# Save batch ID to tracking file
with open('batch-jobs/batch-job-comparison-[timestamp]-tracking.json', 'r+') as f:
    data = json.load(f)
    data['batch_id'] = batch.id
    data['uploaded_at'] = datetime.now().isoformat()
    data['status'] = 'processing'
    f.seek(0)
    json.dump(data, f, indent=2)
```

### Step 3: Wait (12-24 hours)

Monitor with:
```bash
python scripts/check-batch-status.py
```

### Step 4: Download Comparison Results

```bash
python scripts/download-batch-results.py comparison
```

**Note:** You may need to update the download script to handle "comparison" tier.

### Step 5: Run Comparison Analysis

```bash
python scripts/compare-analyses.py
```

**What it does:**
- Loads Sonnet analyses (existing files)
- Loads Opus analyses (batch results)
- Compares:
  - Word count (depth)
  - Number of quotes
  - Number of insights
  - Strategic patterns mentioned
  - Quality scores
- Generates detailed report

**Output:**
```
📊 COMPARISON RESULTS
======================================================================

1. The 4 AI Agents Guide
   ──────────────────────────────────────────────────────────────────
   Strategic Value:  Sonnet:       high | Opus:       high
   Quality Score:    Sonnet:          5 | Opus:          5

   Depth Metrics:
   📈 Word Count:      Sonnet:   8500 | Opus:  12000 (+41.2%)
      Quotes:          Sonnet:      5 | Opus:      8 (+3)
      Insights:        Sonnet:     12 | Opus:     18 (+6)
      Patterns:        Sonnet:      3 | Opus:      7 (+4)

[... continues for all 6 videos ...]

======================================================================
📈 OVERALL STATISTICS
======================================================================

Average Differences (Opus vs Sonnet):
  Word Count:    +35.5%
  Quotes:        +2.8
  Insights:      +5.2

💡 Cost Context:
   Sonnet: ~$0.10-0.15 per video
   Opus: ~$0.60-0.90 per video (6x more)
   Is the quality improvement worth 6x the cost?
```

### Step 6: Manual Review

**Compare side-by-side:**
```
Sonnet version: knowledge-base/videos/2025-12-4-ai-agents-guide.md
Opus version:   opus-comparison/opus-analyses/opus-2025-12-4-ai-agents-guide.md
```

**Ask yourself:**
- Is Opus significantly deeper?
- Are the insights more actionable?
- Does Opus catch patterns Sonnet missed?
- Is the 6x cost justified?

### Step 7: Decide

**Option A: Opus is worth it**
```bash
# Upgrade priority videos to Opus
python scripts/prioritize-for-opus.py --top 30 --export
python scripts/create-opus-batch.py
python scripts/upload-batch-jobs.py opus
# Cost: ~$25-50 for top 30
```

**Option B: Sonnet is good enough**
```bash
# Just process the Sonnet batch and call it done
python scripts/download-batch-results.py all
python scripts/process-batch-results.py all
# Cost: ~$15-20 for all 189
```

**Option C: Hybrid approach**
```bash
# Opus for top 10-15 most critical videos only
python scripts/prioritize-for-opus.py --top 15 --export
python scripts/create-opus-batch.py --limit 15
# Cost: ~$12-20 for top 15
```

## What Gets Preserved

**Sonnet analyses:**
- Stay in `knowledge-base/videos/` (your baseline)
- Never deleted or overwritten

**Opus comparison analyses:**
- Saved to `opus-comparison/opus-analyses/`
- Side-by-side comparison possible

**If you upgrade later:**
- Sonnet versions archived to `knowledge-base/videos-archive/sonnet/`
- Opus becomes canonical in `knowledge-base/videos/`

## Cost Summary

| Stage | Videos | Model | Cost | Total |
|-------|--------|-------|------|-------|
| **Comparison Test** | 6 | Opus 4.6 | $0.80/ea | **~$5** |
| **Sonnet Baseline** | 189 | Sonnet 4.5 | $0.10/ea | **~$20** |
| **Option A: Full Opus** | 30 | Opus 4.6 | $0.80/ea | **~$25** |
| **Option B: Sonnet Only** | 0 | - | - | **$0** |
| **Option C: Selective** | 15 | Opus 4.6 | $0.80/ea | **~$12** |

**Best approach:** Test ($5) → Baseline ($20) → Decide → Selective upgrade ($12-25)

**Total: $37-50** for smart, data-driven implementation

## Timeline

- **Now:** Create comparison batch (5 min)
- **Now + 1 min:** Upload batch (instant)
- **Now + 12-24h:** Results ready
- **Now + 24h:** Download and compare (10 min)
- **Now + 24h + 30min:** Review and decide
- **If upgrading:** Create priority batch → wait 12-24h → done

**Total: ~48 hours for complete scientific comparison**

## Files Created

```
YouTubeResearch-AIFiles/
├── batch-jobs/
│   ├── batch-job-comparison-[timestamp].jsonl
│   └── batch-job-comparison-[timestamp]-tracking.json
├── opus-comparison/
│   ├── comparison-manifest-[timestamp].json
│   ├── comparison-report-[timestamp].json
│   └── opus-analyses/
│       ├── opus-2025-12-4-ai-agents-guide.md
│       └── ... (5 more Opus analyses)
└── knowledge-base/
    └── videos/
        ├── 2025-12-4-ai-agents-guide.md  # Original Sonnet
        └── ... (5 more Sonnet baselines)
```

## Quick Commands

```bash
# 1. Create comparison batch
python scripts/create-comparison-batch.py --all

# 2. Upload (manual for now)
# See Step 2 above

# 3. Check status
python scripts/check-batch-status.py

# 4. Download results
python scripts/download-batch-results.py comparison

# 5. Run comparison
python scripts/compare-analyses.py

# 6. Review
open opus-comparison/opus-analyses/
open knowledge-base/videos/
```

## Success Criteria

After comparison, you should be able to answer:

1. **Depth:** Is Opus 30-50% deeper in analysis?
2. **Insights:** Does Opus surface non-obvious patterns?
3. **Actionability:** Are Opus recommendations more specific?
4. **ROI:** Is the quality improvement worth 6x the cost?

**If YES to 3+ questions:** Opus upgrade is worth it
**If NO to 3+ questions:** Sonnet is good enough

## Next Steps

After comparison test completes:
1. Update ROADMAP.md with test results
2. Document decision rationale
3. If upgrading: Follow OPUS-UPGRADE-WORKFLOW.md
4. If not: Process remaining Sonnet batches and ship it
