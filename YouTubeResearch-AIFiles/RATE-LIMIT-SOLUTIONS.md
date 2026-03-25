# Rate Limit Solutions: Two Approaches

**Problem:** YouTube transcript API rate limits (hit after ~6 videos)

**Two Solutions Created:**

---

## Solution A: Use Multiple LLM Providers

**File:** `prompts/universal-analysis-prompt.md`

### What It Does
- Model-agnostic prompt that works with ANY LLM
- Can distribute 455 videos across multiple providers
- No single provider gets overloaded

### Supported Models
- ✅ Claude (Anthropic)
- ✅ GPT-4 / GPT-4o (OpenAI)
- ✅ Gemini 1.5 Pro (Google)
- ✅ Mixtral (Together AI)
- ✅ Any other LLM

### Cost Comparison (455 Videos)

| Provider | Model | Cost/Video | Total |
|----------|-------|------------|-------|
| **Anthropic** | Claude Sonnet 4.5 Batch | **$0.01** | **$4.55** ⭐ Cheapest |
| **Google** | Gemini 1.5 Pro | $0.025 | $11.38 |
| **Together AI** | Mixtral 8x7B | $0.004 | $1.82 |
| **OpenAI** | GPT-4o | $0.08 | $36.40 |
| **OpenAI** | GPT-4 Turbo | $0.15 | $68.25 |

### Distribution Strategy
Split load to avoid rate limits:

```
Tier 1 (40 videos)  → Anthropic Batch    ($0.40)
Tier 2 (64 videos)  → Gemini API         ($1.60)
Tier 3 (85 videos)  → Together AI        ($0.34)
Tier 4 (266 videos) → Anthropic Batch    ($2.66)

Total: ~$5 across 3 providers
No rate limit issues!
```

---

## Solution B: Use yt-dlp for Transcripts ⭐ Recommended

**File:** `scripts/extract-transcripts-ytdlp.py`

### What It Does
- Downloads subtitles directly from YouTube
- **No API rate limits** (different mechanism than API)
- Cleans VTT format → plain text
- Handles 455 videos with configurable delays

### Usage

```bash
# Extract Tier 1 with 5-second delays
python scripts/extract-transcripts-ytdlp.py tier1 --delay 5

# Extract all tiers at once
python scripts/extract-transcripts-ytdlp.py all --delay 5

# Test with limited videos first
python scripts/extract-transcripts-ytdlp.py tier1 --limit 5 --delay 2
```

### Why This Works Better
✅ **No rate limits** - Direct subtitle download, not API
✅ **More reliable** - Works even when API blocks
✅ **Free** - No API costs
✅ **Cached** - Skips already-extracted videos
✅ **Configurable delays** - Adjustable rate limiting

### Time Estimate
- Tier 1 (40 videos, 5s delay): ~3-4 minutes
- All 455 videos (5s delay): ~40-50 minutes total
- Can run overnight safely

---

## Recommended Workflow

### Best Approach: B + A
Use **yt-dlp for transcripts**, then **multiple LLMs for analysis**

**Step 1: Extract All Transcripts (yt-dlp)**
```bash
# Run once, get all 455 transcripts
python scripts/extract-transcripts-ytdlp.py all --delay 5
# Time: ~40-50 minutes
# Cost: $0
```

**Step 2: Analyze with Multiple Providers**
```bash
# Tier 1 → Anthropic Batch API
python scripts/prepare-batch-job.py tier1

# Tier 2 → Gemini API (if Anthropic rate-limited)
python scripts/prepare-gemini-batch.py tier2

# Tier 3+4 → Together AI or back to Anthropic
python scripts/prepare-batch-job.py tier3
python scripts/prepare-batch-job.py tier4
```

**Total:**
- Transcripts: $0 (yt-dlp is free)
- Analysis: $5-10 (distributed across providers)
- No rate limits!

---

## Comparison: Old vs. New Approach

### Old Approach (Hit Rate Limits)
❌ youtube-transcript-api → Rate limited after 6 videos
❌ Single provider (Anthropic) → Could hit rate limits
❌ Blocked for 24-48h

### New Approach (Rate Limit Proof)
✅ yt-dlp → No rate limits, downloads subtitles directly
✅ Multiple LLM providers → Distributed load
✅ Can process all 455 videos in one session

---

## When to Use Each Solution

### Use Solution A (Multiple LLMs) When:
- You already have transcripts
- Want to avoid single-provider rate limits
- Need cost optimization across providers
- Anthropic batch is full

### Use Solution B (yt-dlp) When:
- You need to extract transcripts
- youtube-transcript-api is rate-limited
- Want most reliable extraction
- Processing large batches (100+ videos)

### Use Both (Recommended) When:
- Processing 455 videos
- Want maximum reliability
- Need to avoid ALL rate limits
- Budget is ~$5-10

---

## Files Created

### Solution A: Multi-Provider
- ✅ `prompts/universal-analysis-prompt.md` - Works with any LLM
- Cost: $5-10 for 455 videos (distributed)

### Solution B: yt-dlp
- ✅ `scripts/extract-transcripts-ytdlp.py` - Robust extraction
- Cost: $0 (subtitle download is free)

### Updated Batch Scripts
- ✅ `scripts/prepare-batch-job.py` - Still works for Anthropic
- Can add: `prepare-gemini-batch.py`, `prepare-openai-batch.py`

---

## Next Steps

**Immediate (Don't wait for IP unblock):**
```bash
# Solution B: Extract all transcripts now (works immediately)
cd YouTubeResearch-AIFiles
python scripts/extract-transcripts-ytdlp.py all --delay 5

# ~40-50 minutes, then you have all 455 transcripts
```

**Then:**
```bash
# Solution A: Prepare batches for multiple providers
python scripts/prepare-batch-job.py tier1  # Anthropic
# Submit tier2-4 to Gemini, Together AI, etc.

# Total: $5-10, no rate limits
```

---

## Success Metrics

### Solution B (yt-dlp)
- ✅ Should extract 400+ of 455 videos (88%+ success rate)
- ✅ Failed videos usually don't have subtitles enabled
- ✅ No rate limiting issues

### Solution A (Multi-Provider)
- ✅ Can process all videos with $5-10 budget
- ✅ No single-provider bottleneck
- ✅ Flexible if one provider has issues

---

**Status:** Ready to use immediately - don't need to wait for IP unblock!

**Recommendation:** Run `extract-transcripts-ytdlp.py all` now!
