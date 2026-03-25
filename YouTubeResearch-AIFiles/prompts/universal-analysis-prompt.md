# Universal Video Analysis Prompt
**Works with: Claude, GPT-4, Gemini, or any LLM**

This prompt is model-agnostic and can be used with any LLM provider for video analysis at scale.

---

## Prompt (Copy-Paste to Any LLM)

```
Analyze this YouTube video transcript using a strategic business framework.

VIDEO METADATA:
- Title: {video_title}
- Channel: {channel_name}
- Published: {upload_date}
- Duration: {duration}
- Views: {view_count}

TRANSCRIPT:
{transcript_text}

---

ANALYSIS INSTRUCTIONS:

Extract strategic insights using this 11-dimension framework. Focus on actionable patterns for business leaders.

## 1. Context & Background
- What is this video about?
- Why does this matter strategically?
- What makes this worth studying?
- Key stats or metrics mentioned

## 2. Core Vision & Purpose
- What was the fundamental goal or mission?
- What problem were they solving?
- What motivated this approach?

## 3. Strategic Mechanism (How They Won)
- What was the operational engine that generated advantage?
- List 3-5 key components
- Why did this approach work?

## 4. Culture & Behavioral Design
- What were the core principles?
- How were people incentivized?
- What behaviors did the system encourage?

## 5. Resource Allocation
- Where did money/time/attention flow?
- What did they NOT spend on?
- What was the allocation philosophy?

## 6. Competitive Advantages & Moats
- What made this defensible?
- What was the time horizon (short/long-term)?
- How did advantages compound over time?

## 7. Flywheels & Compounding
- What was the self-reinforcing loop?
- Visualize: [Step 1] → [Step 2] → [Step 3] → [Back to Step 1, stronger]
- What made it hard to replicate?

## 8. Stakeholder Value
- Who benefited (customers, employees, partners)?
- Who lost or was disadvantaged?
- Any ethical considerations?

## 9. Key Metric
- What was the ONE metric that mattered most?
- Why this metric?
- How was it measured?

## 10. Memorable Insights & Quotes
**Quotes (5-10 exact quotes from transcript):**
- "[Quote 1]"
- "[Quote 2]"
- "[Quote 3]"

**Non-Obvious Insights (5-10 surprising takeaways):**
- Insight 1: [counterintuitive wisdom]
- Insight 2: [surprising pattern]
- Insight 3: [unexpected principle]

## 11. Practical Application
**When to use this pattern:**
- [Conditions where this applies]

**When NOT to use:**
- [When this would backfire]

**How to apply:**
- [3-5 specific action items for business leaders]

---

OUTPUT FORMAT:

Structure your response as:
1. One-paragraph summary (core insight)
2. All 11 dimensions filled out
3. Quality assessment (transcript quality, confidence level, strategic value)
4. Strategic patterns identified

Focus on extracting patterns and principles, not just summarizing facts.
```

---

## How to Use with Different Providers

### OpenAI GPT-4 (API)
```python
import openai

response = openai.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": "You are a strategic business analyst."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=16000
)
```

### Google Gemini (API)
```python
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content(prompt)
```

### Claude (API - Alternative)
```python
import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=16000,
    messages=[{"role": "user", "content": prompt}]
)
```

### Any LLM (Manual)
1. Copy the prompt
2. Replace variables with actual data
3. Paste into ChatGPT, Claude.ai, Gemini, etc.
4. Copy output to markdown file

---

## Cost Comparison (455 Videos)

| Provider | Model | Cost/Video | Total (455) |
|----------|-------|------------|-------------|
| Anthropic | Claude Sonnet 4.5 Batch | $0.01 | $4.55 |
| OpenAI | GPT-4 Turbo | $0.15 | $68.25 |
| OpenAI | GPT-4o | $0.08 | $36.40 |
| Google | Gemini 1.5 Pro | $0.025 | $11.38 |
| Together AI | Mixtral 8x7B | $0.004 | $1.82 |

**Recommendation:**
- Anthropic Batch API is cheapest ($4.55)
- If rate-limited: Use Gemini 1.5 Pro ($11.38) or Together AI ($1.82)

---

## Batch Processing with Multiple Providers

### Strategy: Distribute Load
Process 455 videos across multiple providers to avoid rate limits:

**Split:**
- Tier 1 (40 videos): Anthropic Batch ($0.40)
- Tier 2 (64 videos): Gemini API ($1.60)
- Tier 3 (85 videos): GPT-4o ($6.80)
- Tier 4 (266 videos): Together AI Mixtral ($1.06)

**Total: ~$10 across all providers (no rate limits)**

---

## Template Version
**Version:** 1.0 Universal
**Compatible With:** Claude, GPT-4, Gemini, Mixtral, Llama, any LLM
**Created:** 2026-02-10
