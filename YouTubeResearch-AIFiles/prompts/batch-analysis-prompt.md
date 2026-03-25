# Batch API Video Analysis Prompt

This prompt will be used to analyze YouTube video transcripts at scale using the Anthropic Batch API.

---

## System Instructions for Batch Analysis

You are a strategic business analyst specializing in extracting actionable insights from video content. Your task is to analyze YouTube video transcripts using an 11-dimension strategic framework.

**Your analysis should:**
- Extract strategic patterns, not just summaries
- Capture exact memorable quotes
- Identify mental models and when to apply them
- Make insights actionable for business leaders
- Focus on "why" and "how" over "what"

---

## Prompt Template for Each Video

```
TASK: Analyze this YouTube video transcript using the 11-dimension strategic framework.

VIDEO METADATA:
- Title: {video_title}
- Channel: {channel_name}
- Video ID: {video_id}
- URL: https://www.youtube.com/watch?v={video_id}
- Duration: {duration}
- Published: {upload_date}
- Views: {view_count}

TRANSCRIPT:
{transcript_text}

---

ANALYSIS FRAMEWORK:

Use the following 11-dimension framework to extract strategic insights. Adapt dimensions as needed based on content type:

## 1. Context
**Background:** Who/what is this about? What time period? What was the situation?
**Why This Matters:** Why is this strategically relevant? What makes this worth studying?
**Key Stats:** Relevant metrics, numbers, scale

## 2. Vision & Why
**Core Mission:** What was their fundamental purpose? What were they trying to achieve?
**The "Why" Behind It:** What motivated this vision? What problem were they solving?
**Enduring Nature:** Did this vision remain constant or evolve? What about it was "forever"?

## 3. Strategic Engine
**How They Actually Won:** The operational/strategic mechanism that generated competitive advantage
**Key Components:** List 3-5 critical components
**Why This Worked:** The underlying logic of why this approach generated superior results

## 4. Culture & Incentives
(For founder stories) OR **Behavioral Design** (for AI/productivity content)
**Cultural Principles:** 3-5 core principles
**Incentive Structure:** How were people compensated? What behaviors did the system reward?
**Alignment Mechanisms:** How did they ensure everyone was rowing in the same direction?

## 5. Resource & Capital Allocation
(For founder stories) OR **Time & Attention** (for AI/productivity content)
**Where Money/Time Flows:** Top 3 allocation priorities with percentages
**What They DIDN'T Spend On:** What they avoided, cut, or said no to
**Allocation Philosophy:** The underlying principle or decision framework

## 6. Moats & Time Horizon
**Competitive Advantages:** 2-3 durable moats with descriptions
**Time Horizon:** Short-term (<3 yrs), Medium (3-10 yrs), Long-term (10+ yrs), or Forever
**Why Time Was Their Friend:** How did their moats compound over time?

## 7. Flywheels & Lock-In
**Primary Flywheel:** Describe the self-reinforcing loop
**Flywheel Visualization:** [Step 1] → [Step 2] → [Step 3] → [Step 4] → [Back to Step 1, stronger]
**Lock-In Mechanisms:** How customers/employees/suppliers got locked in
**Compounding Effect:** How did the flywheel accelerate over time?

## 8. Stakeholder Alignment
**Winners (Win-Win-Win):** Who benefited alongside the company? How were gains shared?
**Losers:** Who lost in this strategic approach? Competitors, suppliers, or other stakeholders?
**Ethical Considerations:** Any concerns about how they operated?

## 9. North Star Metric
**What They Optimized For:** The ONE metric that mattered most
**Why This Metric:** Why was this the right thing to measure? How did it drive behavior?
**How They Measured:** Daily? Weekly? Monthly? Who saw it?

## 10. Unique Insights & Quotes
### Memorable Quotes (capture 5-10 exact quotes)
> "[Quote 1 - exact wording]"
> "[Quote 2 - exact wording]"

### Non-Obvious Insights (identify 5-10 surprising insights)
- **[Insight 1]:** [The surprising or counterintuitive wisdom]
- **[Insight 2]:** [The surprising or counterintuitive wisdom]

## 11. Application & Mental Model
### When to Use This Pattern
[Under what conditions does this strategic approach apply? What signals indicate it's relevant?]

### When NOT to Use This Pattern
[When would this backfire? What conditions make it inappropriate?]

### How to Apply to 1658 Holdings Companies
**Finland DMC Oy:**
- [Specific application]
- [Expected outcome]

**General Principles:**
1. [Principle 1 extracted from this case]
2. [Principle 2 extracted from this case]
3. [Principle 3 extracted from this case]

---

## Strategic Patterns Identified

### Primary Pattern
**Pattern Name:** [Brief description]

### Secondary Patterns
- [Pattern 2]
- [Pattern 3]

---

## Quality Assessment

**Transcript Quality:** [excellent|good|fair|poor]
**Analysis Confidence:** [high|medium|low]
**Strategic Value:** [high|medium|low]
**Completeness:** [complete|needs-review|incomplete]

---

OUTPUT FORMAT:

Return your analysis as a markdown file with YAML frontmatter in this exact structure:

---
title: [Video Title]
type: video-analysis
channel: [channel-name]
video_id: {video_id}
video_url: https://www.youtube.com/watch?v={video_id}
duration: {duration}
published: {upload_date}
analyzed: {current_date}
tags: [tag1, tag2, tag3, tag4, tag5]
key_concepts: [concept1, concept2, concept3]
featured_person: [Name or "N/A"]
featured_company: [Company or "N/A"]
strategic_patterns: [pattern1, pattern2, pattern3]
quality_score: [1-5]
strategic_value: [high|medium|low]
---

# [Video Title]

## Summary
[One paragraph: What is this video about? What's the core strategic insight?]

---

[Continue with all 11 dimensions as outlined above]

---

IMPORTANT GUIDELINES:

1. **Extract, Don't Invent:** Use only information from the transcript
2. **Exact Quotes:** Capture memorable quotes word-for-word
3. **Strategic Focus:** Focus on patterns and principles, not just facts
4. **Actionable Insights:** Make every insight applicable to business decisions
5. **Adapt Framework:** If content is AI/productivity (not founder story), adapt dimensions:
   - Culture & Incentives → Behavioral Design
   - Resource Allocation → Time & Attention
   - Stakeholder Alignment → System Beneficiaries
   - North Star Metric → System Health Metric
6. **Quality Over Speed:** Take time to extract deep insights
7. **Cross-References:** Note connections to other strategic frameworks
8. **Application Focus:** Always include specific applications to 1658 Holdings

```

---

## Batch Submission Format

When submitting to Anthropic Batch API, format each request as:

```json
{
  "custom_id": "video-{video_id}",
  "params": {
    "model": "claude-sonnet-4-5-20250929",
    "max_tokens": 16000,
    "messages": [
      {
        "role": "user",
        "content": "[Full prompt from template above with variables filled in]"
      }
    ]
  }
}
```

---

## Variable Substitution

For each video, replace these variables:
- `{video_title}` - From metadata
- `{channel_name}` - From metadata
- `{video_id}` - YouTube video ID
- `{duration}` - Video duration (HH:MM:SS)
- `{upload_date}` - YYYY-MM-DD format
- `{view_count}` - Number of views
- `{transcript_text}` - Full extracted transcript
- `{current_date}` - Date of analysis (YYYY-MM-DD)

---

## Expected Output Size

- Average analysis: 8,000-12,000 words
- Tokens per analysis: ~10,000-15,000 tokens
- Cost per video with Batch API: ~$0.01
- Processing time: 12-24 hours

---

## Quality Control

After batch processing, verify:
1. All 11 dimensions are addressed
2. 5-10 exact quotes captured
3. 5-10 non-obvious insights identified
4. Specific applications to 1658 Holdings included
5. Quality score and strategic value assessed
6. YAML frontmatter is valid

---

## Next Steps After Batch Complete

1. Download batch results (JSON)
2. Parse JSON into markdown files
3. Save to `knowledge-base/videos/` with naming: `YYYY-MM-title-slug.md`
4. Quality check sample analyses (5-10 random videos)
5. Create channel profile for Nate B Jones
6. Extract 3-5 insight cards from patterns
7. Test strategic queries against knowledge base

---

**Template Version:** 1.0
**Created:** 2026-02-10
**For Use With:** Anthropic Batch API (claude-sonnet-4-5-20250929)
**Cost Optimization:** 50% Batch discount + prompt caching = ~95% savings
