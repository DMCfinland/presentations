# Opus 4.6 Upgrade Workflow

Complete workflow for upgrading priority videos from Sonnet 4.5 to Opus 4.6 analysis.

## Strategy: Hybrid Approach (Option C)

**Phase 1:** Sonnet 4.5 for breadth (~$30)
**Phase 2:** Opus 4.6 for strategic depth (~$50-100)
**Total:** ~$80-130 for 189 videos with selective deep analysis

## Prerequisites

✅ Sonnet batch jobs completed
✅ Sonnet results processed into knowledge base
✅ Raw transcripts available in `reference/transcripts/`

## Step-by-Step Workflow

### Step 1: Prioritize Videos for Opus Upgrade

**Command:**
```bash
python scripts/prioritize-for-opus.py --top 30 --export
```

**What it does:**
- Analyzes all Sonnet-processed videos
- Scores based on priority topics:
  - Second brain / knowledge management (weight: 10)
  - Lead generation / sales (weight: 10)
  - Productivity / execution (weight: 9)
  - High ROI frameworks (weight: 10)
  - AI agents (weight: 8)
  - Business strategy (weight: 9)
- Considers strategic value and quality scores
- Exports top 30 to `opus-upgrade/opus-priority-list-[timestamp].json`

**Output:**
- Priority list JSON
- Detailed report with scores
- Cost estimates

**Customize:**
```bash
# Get top 20 instead
python scripts/prioritize-for-opus.py --top 20 --export

# Require minimum score of 25
python scripts/prioritize-for-opus.py --top 30 --min-score 25 --export
```

### Step 2: Create Opus Batch Job

**Command:**
```bash
python scripts/create-opus-batch.py
```

**What it does:**
- Loads the most recent priority list
- Fetches transcripts for each video
- Creates batch JSONL file with `model: "claude-opus-4-6"`
- Saves to `batch-jobs/batch-job-opus-upgrade-[timestamp].jsonl`
- Creates tracking file

**Options:**
```bash
# Limit to first 10 videos (test run)
python scripts/create-opus-batch.py --limit 10

# Use specific priority file
python scripts/create-opus-batch.py --priority-file opus-upgrade/opus-priority-list-20260210.json
```

### Step 3: Upload Batch Job

**You'll need to update upload-batch-jobs.py first to handle "opus" tier:**

```bash
python scripts/upload-batch-jobs.py opus
```

**Manual alternative:**
```python
import anthropic
client = anthropic.Anthropic()

with open('batch-jobs/batch-job-opus-upgrade-[timestamp].jsonl', 'rb') as f:
    batch = client.messages.batches.create(
        requests=f
    )
print(f"Batch ID: {batch.id}")
```

### Step 4: Monitor Progress

**Command:**
```bash
python scripts/check-batch-status.py
```

**Timeline:**
- Opus batches typically complete in 12-24 hours
- Check periodically or set a reminder

### Step 5: Download Results

**When status shows "ended":**
```bash
python scripts/download-batch-results.py opus
```

**Note:** You'll need to update the download script to handle the "opus" tier.

### Step 6: Process Opus Results

**Command:**
```bash
python scripts/process-batch-results.py opus
```

**What it does:**
- Reads `batch-jobs/results/opus-results.jsonl`
- Extracts Opus analyses
- Saves to `knowledge-base/videos/`
- **Overwrites** Sonnet versions with Opus versions

**Result:**
- Top 20-30 videos now have deep Opus analysis
- Remaining 160+ videos have good Sonnet analysis
- Total knowledge base: ~189 videos

## Priority Topic Matching

The prioritization script looks for these topics:

### Second Brain / Knowledge Management (Weight: 10)
Keywords: second brain, knowledge management, notion, obsidian, pkm, zettelkasten, note-taking, digital garden, knowledge graph

### Lead Generation / Sales (Weight: 10)
Keywords: lead generation, sales, outreach, prospecting, cold email, crm, pipeline, customer acquisition

### Productivity / Execution (Weight: 9)
Keywords: productivity, workflow, automation, get shit done, gsd, execution, task management, efficiency, delegation

### High ROI Frameworks (Weight: 10)
Keywords: framework, mental model, strategic pattern, flywheel, moat, leverage, compounding, system thinking

### AI Agents (Weight: 8)
Keywords: ai agents, autonomous, delegation, agent workflow, multi-agent, orchestration, tool use

### Business Strategy (Weight: 9)
Keywords: business model, strategy, competitive, market, revenue, growth, scaling, economics

## Cost Breakdown

### Sonnet 4.5 (Already Done)
- 189 videos
- ~$20-30 total
- Good quality (7/10)

### Opus 4.6 (Priority Upgrade)
- Top 20-30 videos
- ~$2-4 per video
- Total: ~$50-100
- Excellent quality (10/10)

### Total Investment
- **$80-130** for 189 analyzed videos
- Best videos get best analysis
- Smart resource allocation

## Troubleshooting

### No priority list found
```bash
# Run prioritization first
python scripts/prioritize-for-opus.py --export
```

### Missing transcripts
- Check `reference/transcripts/` directory
- Transcripts should be named: `tier1-[video_id].txt`

### Upload/download scripts need updates
- Scripts currently handle tier1/tier2/tier3
- Need to add "opus" handling
- See example code in create-opus-batch.py

## Tips

1. **Start small:** Test with `--limit 10` first
2. **Review scores:** Check if prioritization matches your expectations
3. **Adjust weights:** Edit PRIORITY_TOPICS in prioritize-for-opus.py
4. **Add keywords:** Customize topic keywords for your specific interests
5. **Multiple passes:** Can run Opus upgrade multiple times for different topics

## File Locations

```
YouTubeResearch-AIFiles/
├── batch-jobs/
│   ├── batch-job-opus-upgrade-[timestamp].jsonl  # Created in Step 2
│   ├── batch-job-opus-upgrade-[timestamp]-tracking.json
│   └── results/
│       └── opus-results.jsonl  # Downloaded in Step 5
├── opus-upgrade/
│   ├── opus-priority-list-[timestamp].json  # Created in Step 1
│   └── opus-upgrade-report-[timestamp].md
├── knowledge-base/
│   └── videos/
│       └── *.md  # Final Opus analyses here
└── scripts/
    ├── prioritize-for-opus.py  # Step 1
    ├── create-opus-batch.py    # Step 2
    ├── upload-batch-jobs.py    # Step 3 (needs update)
    ├── check-batch-status.py   # Step 4
    ├── download-batch-results.py  # Step 5 (needs update)
    └── process-batch-results.py   # Step 6
```

## Next Enhancements

- [ ] Update upload-batch-jobs.py to handle "opus" tier
- [ ] Update download-batch-results.py to handle "opus" tier
- [ ] Update check-batch-status.py to show all batches including opus
- [ ] Add comparison report (Sonnet vs Opus analysis quality)
- [ ] Create "re-prioritization" script (after reading Sonnet analyses)
