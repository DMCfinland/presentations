# Phase 0 Research: YouTube Transcript Extraction & Anthropic Batch API

**Research Date:** February 10, 2026
**Purpose:** Evaluate technical feasibility and cost optimization for bulk YouTube video analysis

---

## 1. Executive Summary

This research evaluates two critical components for a YouTube video analysis workflow:

**YouTube Transcript Extraction:**
- Multiple reliable tools available (youtube-transcript-api, yt-dlp)
- Auto-generated transcripts: 60-70% accuracy; Manual transcripts: 99% accuracy
- Rate limits: 5 requests per 10 seconds, max 50 videos per batch
- For 50-200 videos: expect 10-40 minutes processing time with proper rate limiting
- Can be called directly from Claude Code via Python scripts

**Anthropic Batch API:**
- 50% discount on both input and output tokens (currently confirmed for 2026)
- Stacks with prompt caching for up to 95% total savings
- 24-hour turnaround, up to 10,000 requests or 32 MB per batch
- Requires separate Python scripts but integrates well with Claude Code workflows
- Best for non-time-sensitive analysis where cost optimization is priority

**Key Recommendation:** Use youtube-transcript-api for transcript extraction (no API key needed) + Anthropic Batch API for analysis. For 100 videos, expect ~$5-10 in transcript extraction costs (if using paid services) and 50% API savings via batching.

---

## 2. YouTube Transcript Extraction

### 2.1 Tools Overview

#### youtube-transcript-api (Recommended)
- **Type:** Python library
- **Key Features:**
  - No YouTube API key required
  - Retrieves both auto-generated and manual captions
  - Supports multiple languages
  - Works with Python, JavaScript, Ruby, PHP implementations
- **Installation:** `pip install youtube-transcript-api`
- **Use Case:** Best for programmatic batch extraction without API costs
- **Active Status:** Well-maintained as of February 2026

#### yt-dlp
- **Type:** Command-line tool and Python library
- **Key Features:**
  - Fork of youtube-dl with better maintenance
  - Downloads video metadata, subtitles, and transcripts
  - More comprehensive but heavier than youtube-transcript-api
  - Can extract transcripts in various formats
- **Use Case:** Best when you need video metadata + transcripts together
- **Active Status:** Actively maintained, preferred over youtube-dl

#### yt-dlp Wrapper Tools
Several specialized wrappers combine yt-dlp with additional features:
- **yt-dlp-transcript:** Handy wrapper specifically for transcript downloads
- **yt_dlp_transcript:** Extracts transcripts and converts to Markdown format
  - Optional AI-powered summarization with Gemini API
  - Built on top of both yt-dlp and youtube-transcript-api

#### YouTube API v3
- **Type:** Official Google API
- **Key Features:**
  - Programmatic access to captions via Captions resource
  - Requires API credentials and OAuth 2.0
  - More complex setup than unofficial tools
- **Costs:** Free tier available with quota limits
- **Use Case:** When official API access is required or for commercial applications requiring compliance

#### Browser Extensions & Web Services
Multiple services offer GUI-based extraction:
- YouTube Transcript Generator (youtube-transcript.io)
- Supadata API
- Various browser extensions

### 2.2 Quality Considerations

#### Auto-Generated Transcripts
**Accuracy:**
- Average: 60-70%
- Best case (clear audio, standard accents): 80-85%
- Research studies indicate 61.92% accuracy at best

**Limitations:**
- Technical vocabulary often misinterpreted
- Accents and dialects cause errors
- Background noise degrades accuracy
- No punctuation or proper capitalization
- Poor handling of:
  - Industry-specific terminology
  - Multiple speakers
  - Fast speech or overlapping audio

**When to Use:**
- Budget-constrained projects
- Content screening before manual review
- Large-scale analysis where perfect accuracy isn't critical

#### Manual/Professional Transcripts
**Accuracy:**
- Professional human transcription: 99%+
- Includes proper punctuation, speaker identification
- Contextual understanding of homonyms and technical terms

**Advantages:**
- Precision and reliability
- Proper formatting and structure
- SEO-optimized when published
- Better for legal, medical, or technical content

**When to Use:**
- High-stakes content (legal, medical)
- Professional publications
- Customer-facing materials
- When accuracy is critical for analysis

#### Hybrid Approach (Recommended)
- Use auto-generated for initial extraction (fast + free)
- Apply AI post-processing (Claude) to clean and improve quality
- Manual review only for critical sections
- Balance: efficiency + acceptable accuracy for analysis use cases

### 2.3 Rate Limits & Costs

#### youtube-transcript-api (Unofficial, Free)
**Rate Limits:**
- No official published limits (uses undocumented YouTube endpoints)
- Community reports suggest reasonable use is tolerated
- Recommended: Implement 2-5 second delays between requests
- For 50-200 videos: Plan for 3-17 minutes processing time

**Costs:**
- Free (no API key needed)
- Risk: Could break if YouTube changes their internal APIs

**Best Practices:**
- Implement exponential backoff on errors
- Cache results to avoid re-fetching
- Add random jitter to avoid detection patterns

#### YouTube API v3 (Official)
**Rate Limits:**
- Default quota: 10,000 units per day
- Caption download: 200 units per request
- 50 caption downloads per day with default quota
- Can request quota increases from Google

**Costs:**
- Free tier available
- Exceeding quota requires billing account
- Large-scale usage: Contact Google for pricing

**For 50-200 Videos:**
- 50 videos: 10,000 units (1 day with default quota)
- 100 videos: 20,000 units (2 days or quota increase needed)
- 200 videos: 40,000 units (4 days or quota increase needed)

#### youtube-transcript.io API (Commercial Service)
**Rate Limits:**
- 50 videos maximum per request
- 5 requests per 10 seconds
- 429 error with Retry-After header on violations

**Costs:**
- Free tier available (limited)
- Paid plans for bulk access (pricing not specified in search results)

**For 50-200 Videos:**
- 50 videos: 1-2 batches (10-20 seconds minimum)
- 100 videos: 2-4 batches (20-40 seconds minimum)
- 200 videos: 4-8 batches (40-80 seconds minimum)

#### Bulk Processing Services
**Apify Actors:**
- YouTube Transcript Scraper
- YouTube Transcript & Metadata Extractor
- Pricing based on compute units consumed
- Handles rate limiting automatically
- 1000 videos: ~1-2 minutes processing time

**Cost Estimate (Commercial Services):**
- Small scale (50-100 videos): $5-20/month subscription
- Medium scale (200+ videos): $20-100/month
- Large scale (1000+ videos): Custom pricing

### 2.4 Claude Code Integration

#### Direct Integration (Recommended)
Claude Code can directly execute Python scripts that use youtube-transcript-api:

```python
from youtube_transcript_api import YouTubeTranscriptApi

def extract_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        return f"Error: {str(e)}"
```

**Capabilities:**
- Claude Code can write and execute these scripts directly
- Can process video lists, implement rate limiting
- Can save outputs to structured formats (JSON, CSV, Markdown)
- Can handle error recovery and retry logic

#### Custom Skills
Create a reusable skill for transcript extraction:
- Bundle Python script with instructions
- Include rate limiting and error handling
- Add output formatting options
- Make it available across projects

#### Workflow Integration
**Typical Flow:**
1. Claude Code reads video URL list
2. Executes Python script to extract transcripts
3. Saves raw transcripts to local files
4. Prepares batch for Anthropic API analysis
5. Processes results and generates reports

**Automation Options:**
- Can be fully automated via Claude Code
- Progress tracking via todo lists
- Error logging and retry mechanisms
- Output formatting customizable

---

## 3. Anthropic Batch API

### 3.1 Pricing

#### Current Rates (2026)
**Batch API Discount:**
- 50% discount on both input and output tokens
- Applies to all supported Claude models:
  - Claude 3.5 Sonnet
  - Claude 3 Opus
  - Claude 3 Haiku
  - Claude Opus 4.6 (latest as of 2026)

#### Stackable Discounts
**Prompt Caching + Batch API:**
- Prompt caching: Up to 90% savings on cached input tokens
- Batch API: 50% discount on all tokens
- Combined savings: Up to 95% on cached input tokens
- Example: Base $5/MTok → $0.25/MTok with both optimizations

**Example Cost Calculation:**
For 100 YouTube video transcripts (avg 5,000 tokens each):
- Input: 500,000 tokens
- Without optimization: ~$5-10 (depending on model)
- With Batch API: ~$2.50-5 (50% savings)
- With Batch + Caching: ~$0.25-2.50 (95% savings on repeated content)

#### Long Context Pricing
- Batch API discount applies to long context pricing
- No separate charge for extended context windows
- 200K token context fully supported with batch discount

### 3.2 Job Submission Process

#### API Format
**Creating a Batch:**
```json
{
  "requests": [
    {
      "custom_id": "video_001",
      "params": {
        "model": "claude-opus-4-6",
        "max_tokens": 1024,
        "messages": [
          {
            "role": "user",
            "content": "Analyze this transcript..."
          }
        ]
      }
    }
  ]
}
```

**Key Fields:**
- `custom_id`: Unique identifier for tracking (required)
- `params`: Standard Messages API parameters
- Supports all Messages API features (system prompts, tools, etc.)

#### Submission Methods

**Via Python SDK:**
```python
import anthropic

client = anthropic.Anthropic(api_key="your_api_key")

batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": "video_001",
            "params": {
                "model": "claude-opus-4-6",
                "max_tokens": 1024,
                "messages": [...]
            }
        }
    ]
)
```

**Via REST API:**
- POST to `/v1/messages/batches`
- Standard authentication headers
- JSON payload with requests array

#### Monitoring & Retrieval
**Check Status:**
```python
batch = client.messages.batches.retrieve(batch_id)
print(batch.processing_status)
```

**Retrieve Results:**
- Results available once all requests processed
- Download via batch results endpoint
- Results retained for 29 days
- Each result includes `custom_id` for matching

### 3.3 Limits & Turnaround

#### Size Limits
**Per Batch:**
- Maximum: 10,000 requests per batch
- OR 32 MB total size (whichever reached first)
- Each request: Standard Messages API limits apply

**For 50-200 Videos:**
- All videos fit in single batch
- Total size consideration: ~1-5 MB for transcript text
- Plenty of headroom for analysis prompts

#### Turnaround Time
**Processing Window:**
- Maximum: 24 hours
- Typical: Often much faster (hours, not days)
- No real-time guarantees
- Not suitable for user-facing applications requiring immediate response

**For YouTube Analysis:**
- Submit batch of 100-200 video analyses
- Expect results within 12-24 hours
- Perfect for overnight processing
- Check status periodically

#### Expiration
- Batches expire after 29 days if not retrieved
- Results available for 29 days after completion
- Download results promptly for long-term storage

### 3.4 Best Practices

#### Batch Design

**Optimal Batch Size:**
- Target: 1,000-5,000 requests per batch for manageability
- Don't split unnecessarily (up to 10,000 is fine)
- For 100 videos: Single batch is optimal

**Custom ID Strategy:**
```
video_001
video_002
channel_ABC_video_001
```
- Use descriptive IDs for easy result matching
- Include metadata in ID if helpful
- Ensure uniqueness within batch

**Error Handling:**
- Each request succeeds or fails independently
- Check individual results for errors
- Re-submit failed requests in new batch
- Log custom_id for all failures

#### Prompt Optimization for Batching

**Structured Prompts:**
Use consistent prompt structure across batch:
```
Analyze this YouTube video transcript and provide:
1. Main topics (bullet list)
2. Key insights (3-5 sentences)
3. Sentiment (positive/neutral/negative)
4. Content category

Transcript:
[TRANSCRIPT_TEXT]
```

**Prompt Caching Strategy:**
- Place reusable instructions in system prompt
- Cache system prompt across all batch requests
- Only transcript varies between requests
- Achieves 90% cache hit rate on system prompt

**Token Management:**
- Set reasonable `max_tokens` (1024-4096 for analysis)
- Truncate extremely long transcripts if needed
- Monitor output token usage for cost estimation

#### Integration with Transcript Extraction

**Workflow Pattern:**
1. **Phase 1 - Extract:** Use youtube-transcript-api to download all transcripts
2. **Phase 2 - Prepare:** Format transcripts into batch JSON
3. **Phase 3 - Submit:** Send batch to Anthropic API
4. **Phase 4 - Wait:** Check status every hour
5. **Phase 5 - Process:** Download results and generate reports

**File Organization:**
```
project/
  raw-transcripts/
    video_001.txt
    video_002.txt
  batch-input/
    batch_001.json
  batch-results/
    batch_001_results.json
  analysis-output/
    final_report.md
```

### 3.5 Integration Options

#### From Claude Code (Recommended)
**Capabilities:**
- Claude Code can write and execute Python scripts
- Can use Anthropic SDK directly
- Can monitor batch status
- Can process results when complete

**Example Skill:**
Create a "batch-analyze" skill:
- Reads transcript directory
- Formats batch request
- Submits to API
- Polls for completion
- Processes results

**Workflow:**
```
User: "Analyze all transcripts in raw-transcripts/ using batch API"
Claude Code:
  1. Writes Python script
  2. Executes: Creates batch JSON
  3. Executes: Submits batch
  4. Provides batch ID for tracking
  5. (Later) Retrieves results when ready
```

#### Standalone Scripts
**When to Use:**
- Very large batches (thousands of videos)
- Scheduled/automated workflows
- Integration with existing data pipelines

**Tools:**
- Python script with Anthropic SDK
- Temporal workflow for reliability (see sources)
- n8n workflow automation
- Custom cron jobs

#### Hybrid Approach
**Best Practice:**
- Use Claude Code for initial setup and testing
- Create reusable scripts for production runs
- Monitor via Claude Code or external dashboards
- Post-process results with Claude Code

---

## 4. Recommendations

### For 50-200 Video Analysis Project

#### Transcript Extraction Strategy
**Recommended Tool:** youtube-transcript-api
- Free, reliable, no API key needed
- Directly callable from Claude Code
- Sufficient for this scale

**Implementation:**
1. Create Python script in Claude Code session
2. Implement rate limiting (2-3 seconds between requests)
3. Save transcripts as individual text files
4. Include error handling and retry logic
5. Expected time: 3-10 minutes for 50-100 videos

**Quality Approach:**
- Accept auto-generated transcripts (60-70% accuracy)
- Use Claude for post-processing to improve quality
- Manual review not needed for most analysis use cases
- Flag low-confidence transcripts for review

#### Batch API Integration
**Recommended Approach:** Use Batch API for analysis
- 50% immediate cost savings
- Non-time-sensitive analysis is acceptable
- Stack with prompt caching for maximum savings

**Implementation:**
1. Create batch JSON from extracted transcripts
2. Use consistent analysis prompt across all videos
3. Submit single batch (well under 10,000 limit)
4. Wait 12-24 hours for results
5. Process results with Claude Code

**Cost Estimate:**
- 100 videos × 5,000 tokens = 500K tokens input
- Analysis output: ~200K tokens
- Standard API cost: ~$7-10
- Batch API cost: ~$3.50-5 (50% savings)
- With prompt caching: ~$0.50-2 (90%+ savings)

### Workflow Architecture

#### Option A: Sequential (Simplest)
```
Day 1 Morning:   Extract transcripts (10 min)
Day 1 Morning:   Prepare & submit batch (5 min)
Day 2 Morning:   Retrieve results (2 min)
Day 2 Morning:   Generate report (5 min)
Total: 22 minutes work, 24 hours elapsed
```

#### Option B: Iterative (For Learning)
```
Week 1: Extract 10 videos, test analysis
Week 2: Refine prompts, extract 50 videos
Week 3: Full batch of 100-200 videos
Week 4: Reporting and insights
```

#### Option C: Continuous (For Ongoing)
```
Weekly: New video extraction
Weekly: Batch submission
Weekly: Results processing
Monthly: Trend analysis
```

### Integration with Claude Code

**Recommended Setup:**
1. Create project folder structure
2. Use Claude Code to write extraction script
3. Use Claude Code to write batch submission script
4. Use Claude Code to write results processor
5. Save all as reusable skills

**Skills to Create:**
- `extract-yt-transcripts`: Transcript extraction with rate limiting
- `prepare-batch`: Format transcripts for Batch API
- `submit-batch`: Submit to Anthropic Batch API
- `process-batch-results`: Download and analyze results
- `generate-report`: Create final analysis documents

### Cost Optimization Strategy

**Maximum Savings:**
1. Use free youtube-transcript-api (vs. paid services)
2. Use Batch API for 50% discount
3. Implement prompt caching for 90% input savings
4. Reuse system prompts across all requests
5. Only vary transcript content between requests

**Expected Costs for 100 Videos:**
- Transcript extraction: $0 (using free tool)
- API analysis without optimization: $10
- API analysis with Batch API: $5
- API analysis with Batch + Caching: $0.50-1
- **Total optimized cost: ~$0.50-1 for 100 video analyses**

### Risk Mitigation

**Transcript Extraction:**
- Risk: youtube-transcript-api uses undocumented endpoints
- Mitigation: Have YouTube API v3 as backup
- Mitigation: Cache all transcripts immediately

**Batch API:**
- Risk: 24-hour wait time
- Mitigation: Plan workflow with built-in delays
- Mitigation: Use standard API for urgent/test requests

**Quality:**
- Risk: Auto-generated transcripts have errors
- Mitigation: Post-process with Claude
- Mitigation: Flag low-confidence analyses for review

---

## 5. Sources

### YouTube Transcript Extraction

- [YouTube Transcript Generator | Extract & Download Video Transcripts](https://www.youtube-transcript.io/)
- [Free API to Get the Transcript of a YouTube Video (2026)](https://supadata.ai/youtube-transcript-api)
- [youtube-transcript-api · PyPI](https://pypi.org/project/youtube-transcript-api/)
- [Using yt-dlp to download youtube transcript | by jon allen | Medium](https://medium.com/@jallenswrx2016/using-yt-dlp-to-download-youtube-transcript-3479fccad9ea)
- [YouTube Transcript Downloader | Claude Skills](https://mcpservers.org/claude-skills/michalparkola/youtube-transcript)
- [How to Get YouTube Video Transcripts](https://www.assemblyai.com/blog/how-to-get-the-transcript-of-a-youtube-video)
- [Auto-Generated vs Manual YouTube Transcripts: Which Is Better?](https://thedatascientist.com/auto-generated-vs-manual-youtube-transcripts/)
- [Best YouTube Video Transcript Generators in 2026](https://sonix.ai/ai/best-youtube-video-transcript-generators/)
- [YouTube Auto Caption Accuracy Test: How Good Is AI Transcription](https://www.cisdem.com/resource/youtube-auto-caption-accuracy.html)
- [Automatic vs. Manual YouTube Transcription: Pros and Cons - Insight7](https://insight7.io/automatic-vs-manual-youtube-transcription-pros-and-cons/)

### YouTube API & Rate Limits

- [Youtube Transcript API](https://www.youtube-transcript.io/api)
- [Bulk YouTube Transcript Downloader | Extract Channels](https://www.downloadyoutubetranscripts.com/)
- [How to Scrape Captions from YouTube](https://roundproxies.com/blog/scrape-youtube-captions/)
- [YouTube Data API for Automated Transcript Extraction](https://youtubetranscribes.com/blog/youtube-api-transcript-automation/)
- [YouTube Transcript Scraper - Extract Video Subtitles · Apify](https://apify.com/futurizerush/youtube-transcript-scraper)
- [YouTube Transcript & Metadata Extractor · Apify](https://apify.com/transcriptdl/transcript-downloader-youtube-transcript-and-metadata-scraper)

### Anthropic Batch API

- [Pricing - Claude API Docs](https://platform.claude.com/docs/en/about-claude/pricing)
- [Anthropic Claude API Pricing 2026: Complete Cost Breakdown | MetaCTO](https://www.metacto.com/blogs/anthropic-api-pricing-a-full-breakdown-of-costs-and-integration)
- [Anthropic API Pricing: The 2026 Guide](https://www.nops.io/blog/anthropic-api-pricing/)
- [Claude Opus 4.6 Pricing: Complete Guide to API Costs, Subscriptions & Savings (2026)](https://www.aifreeapi.com/en/posts/claude-opus-4-pricing)
- [Introducing the Message Batches API | Claude](https://www.anthropic.com/news/message-batches-api)
- [Using Anthropic's Message Batches API with Temporal | Steve Kinney](https://stevekinney.com/writing/anthropic-batch-api-with-temporal)
- [Anthropic Launches Message Batches API for Cost-Effective Querying with Claude AI | by AI In Transit | Medium](https://aiintransit.medium.com/anthropic-launches-message-batches-api-for-cost-effective-querying-with-claude-ai-3bd4ba3a003e)
- [Anthropic AI Introduces the Message Batches API - MarkTechPost](https://www.marktechpost.com/2024/10/09/anthropic-ai-introduces-the-message-batches-api-a-powerful-and-cost-effective-way-to-process-large-volumes-of-queries-asynchronously/)
- [Batch processing - Claude Docs](https://docs.claude.com/en/docs/build-with-claude/batch-processing)
- [Create a Message Batch - Claude API Reference](https://docs.anthropic.com/en/api/creating-message-batches)
- [Optimizing costs with Anthropic's API batching and caching](https://www.ai.moda/en/blog/anthropics-batches-with-caching)

### Claude Code Integration

- [Common workflows - Claude Code Docs](https://code.claude.com/docs/en/common-workflows)
- [How Claude Code Is Transforming AI Coding in 2026](https://apidog.com/blog/claude-code-coding/)
- [GitHub - anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python)
- [How to Integrate Claude Code into Your Development Workflow in 2 Hours](https://learn.ryzlabs.com/ai-coding-assistants/how-to-integrate-claude-code-into-your-development-workflow-in-2-hours)
- [How to train Claude Code agents with custom skills](https://www.howdoiuseai.com/blog/2026-02-08-how-to-train-claude-code-agents-with-custom-skills)
- [Claude Code: A Guide With Practical Examples | DataCamp](https://www.datacamp.com/tutorial/claude-code)

---

**Document Version:** 1.0
**Last Updated:** February 10, 2026
**Next Review:** As needed for implementation planning
