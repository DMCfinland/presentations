# Large Query Best Practices: DO's and DON'Ts

## DATE: 2026-02-11
## LEARNED FROM: Expensive Opus 4.6 strategic mining query ($40-50)

---

## EXECUTIVE SUMMARY

**The Problem:** Large-context LLM queries (1M+ tokens) are expensive and risky. One wrong move can waste $40-80 and deliver nothing useful.

**This Guide:** Battle-tested practices from mining 195 videos (6.7MB, 1.7M tokens) with Opus 4.6. Based on real mistakes and their costs.

**ROI:** Following this guide can save $200-500 per project on LLM query costs.

---

## PART 1: BEFORE THE QUERY

### ✅ DO: Calculate Total Cost FIRST

**Before submitting ANY large query, calculate:**

```
Input Cost = (file_size_MB × 1024 × 1024 / 4) / 1,000,000 × $input_per_M
Thinking Cost = thinking_tokens / 1,000,000 × $output_per_M
Output Cost = expected_output_tokens / 1,000,000 × $output_per_M

Total = Input + Thinking + Output
```

**Example (Opus 4.6 full price):**
- Input: 1.7M × $15 = $25.50
- Thinking: 100K × $75 = $7.50
- Output: 150K × $75 = $11.25
- **Total: $44.25 per message**

**If total > $30:** Seriously consider alternatives (batching, smaller scope, different approach)

---

### ✅ DO: Understand Context Window vs. Effective Use

**Just because a model CAN handle 200K tokens doesn't mean it SHOULD.**

**Context rot problems:**
- "Lost in the middle" effect (models recall start/end better than middle)
- Strategic synthesis requires cross-document pattern recognition
- Large contexts may get skimmed, not deeply analyzed

**Size guidelines:**
- **< 100K tokens:** Safe, full utilization expected
- **100K - 500K tokens:** Moderate risk of context rot
- **500K - 1M tokens:** High risk, test with samples first
- **> 1M tokens:** Very high risk, strongly consider batching

**Our case:** 1.7M tokens = HIGH RISK. Consider 5-10 smaller queries instead.

---

### ✅ DO: Test with Small Samples FIRST

**Never run expensive queries on full dataset without testing.**

**Test protocol:**
1. Extract 10-20% sample of your data
2. Run query on sample (~$5-10)
3. Evaluate quality:
   - Does it cite sources across the full sample?
   - Is strategic synthesis coherent?
   - Did it follow instructions precisely?
4. If good → scale up
5. If poor → revise approach

**Cost savings:** $5 test prevents $40 waste

---

### ✅ DO: Be Explicit About Output Format

**BAD prompts (ambiguous):**
```
"Create a comprehensive report analyzing these videos"
```

**GOOD prompts (explicit):**
```
Write a comprehensive strategic intelligence report analyzing these videos.

OUTPUT REQUIREMENTS:
- Format: Markdown
- Deliver the FULL REPORT directly in your response
- Do NOT create scripts, code, or document generators
- Write 30-40 pages of analysis as markdown text
- I will save your response as a file myself

Do not suggest creating tools or scripts. Just write the content.
```

**Why this matters:** Prevents $40 query that delivers a script instead of content

---

### ✅ DO: Design for Single-Shot Extraction

**Assume you get ONE query. No follow-ups.**

**Design prompts that:**
- Answer all questions in first response
- Include evidence/citations for verification
- Provide decision-ready recommendations (not "it depends")
- Cover edge cases and alternatives

**Why:** Each follow-up in large context = another $40+

**Bad:** "Analyze the videos and let me know what you find"
**Good:** "Answer these 4 specific questions with evidence from videos"

---

### ❌ DON'T: Use Claude Projects for One-Time Large Queries

**Claude Projects bill context on EVERY message.**

**Cost comparison (1.7M token context):**

| Approach | First Message | Follow-up 1 | Follow-up 2 | Total |
|----------|---------------|-------------|-------------|-------|
| **Regular chat** | $44 | N/A (start new chat) | N/A | **$44** |
| **Claude Project** | $44 | $44 | $44 | **$132** |

**Use Projects for:**
- ✅ Multi-session work on same documents (worth the reuse)
- ✅ Team collaboration with shared context
- ✅ Ongoing reference knowledge base

**Don't use Projects for:**
- ❌ One-time strategic mining
- ❌ Single large analysis
- ❌ Expensive contexts you won't reuse

---

### ❌ DON'T: Assume Batch API Saves Money on Everything

**Batch API gives 50% discount BUT multiplies query count.**

**When Batch API is cheaper:**
- Many small independent queries (100+ videos analyzed separately)
- Each query stands alone
- No synthesis across queries needed

**When Batch API is MORE expensive:**
- Large synthesis task (like strategic mining)
- Need holistic view across full dataset
- Splitting creates synthesis burden

**Example from our case:**
- 1 query in claude.ai: **$44**
- 26 batch queries: **$159** (even with 50% discount!)

**Reason:** 26 independent queries × cost > 1 holistic query

---

## PART 2: DURING THE QUERY

### ✅ DO: Monitor Thinking Traces

**If using extended thinking, watch the trace for:**

**Good signs:**
- "Let me sample from early, middle, and late sections"
- "Reading strategically across the corpus"
- Cites specific document names/sections
- Shows pattern recognition across sources

**Bad signs:**
- "Let me create a script to generate..."
- Only references first few documents
- Generic observations without citations
- Getting lost in details without synthesis

**Action:** If bad signs appear and you can interrupt, do it early to minimize cost

---

### ❌ DON'T: Send Follow-Ups in Expensive Contexts

**EVERY message reloads the full context.**

**Example:**
- Query 1: "Analyze these videos" → $44
- Query 2: "Can you clarify point 3?" → $44 (reloads 1.7M tokens!)
- Query 3: "What about point 5?" → $44
- **Total: $132 for simple clarifications**

**Instead:**
1. Download/copy the response
2. Close the expensive conversation
3. Open new chat with JUST the response (small context)
4. Ask clarifications there (costs $0.50 instead of $44)

---

## PART 3: AFTER THE QUERY

### ✅ DO: Download Everything IMMEDIATELY

**Before closing the conversation:**
- ✅ Copy all text responses
- ✅ Download any generated files
- ✅ Screenshot key insights if needed
- ✅ Save thinking traces (useful for debugging)

**Why:** You can't retrieve it later without paying context costs again

---

### ✅ DO: Close Expensive Conversations Immediately

**After downloading outputs:**
1. Close the browser tab/window
2. Don't send "thank you" messages (they cost $40!)
3. Don't ask follow-ups (start new cheap chat instead)

**Think of it like:** Long distance phone call in the 1990s. Get what you need and HANG UP.

---

### ✅ DO: Verify Quality with Spot Checks

**Don't trust large-context outputs blindly.**

**Verification checklist:**
1. **Citation check:** Pick 5 random claims, verify against source
2. **Distribution check:** Do citations span full dataset or cluster at start/end?
3. **Hallucination check:** Any claims that sound suspicious?
4. **Completeness check:** Did it answer ALL questions asked?
5. **Format check:** Delivered content vs. scripts?

**If quality is poor:** Document WHY before trying again (prevent repeat mistakes)

---

### ✅ DO: Extract Learnings for Next Time

**After every expensive query, document:**
- What worked? What didn't?
- How was quality? Worth the cost?
- What would you change next time?
- Any prompt improvements identified?

**This compounds:** Each expensive query teaches you to avoid future waste

---

## PART 4: ARCHITECTURAL PATTERNS

### Pattern 1: Single Large Query (Holistic Synthesis)

**When to use:**
- Need strategic synthesis across full dataset
- Cross-document pattern recognition critical
- Budget allows ($40-80)
- Dataset < 2M tokens

**Pros:**
- ✅ Holistic view
- ✅ Built-in synthesis
- ✅ Single coherent output

**Cons:**
- ❌ Expensive per query
- ❌ Context rot risk
- ❌ Single point of failure

**Cost:** $40-80 per query

---

### Pattern 2: Batch API (Parallel Processing)

**When to use:**
- 100+ independent analysis tasks
- Each output stands alone (no synthesis)
- Budget conscious (50% discount matters)
- Each query < 334KB

**Pros:**
- ✅ 50% cost discount
- ✅ Parallel processing
- ✅ Can retry individual failures

**Cons:**
- ❌ No cross-query synthesis
- ❌ Manual aggregation needed
- ❌ More complex workflow
- ❌ 334KB per-request size limit

**Cost:** $0.03-0.10 per query (with discount)

---

### Pattern 3: Hybrid (Best of Both)

**When to use:**
- Large dataset needs both breadth AND depth
- Budget allows multiple query types
- Want to compare approaches

**Approach:**
1. Batch API for breadth (analyze all items individually)
2. Single large query for synthesis (strategic patterns)
3. Compare outputs for validation

**Cost:** Higher but lower risk

---

### Pattern 4: Staged Sampling (Risk Mitigation)

**When to use:**
- Unsure if approach will work
- Very expensive query (>$50)
- First time with this data type

**Approach:**
1. Sample 10% → small query ($5)
2. Evaluate quality
3. Sample 30% → medium query ($15)
4. Validate synthesis quality
5. Full dataset → large query ($50) only if tests pass

**Cost:** $70 total but high confidence

---

## PART 5: COST OPTIMIZATION STRATEGIES

### Strategy 1: Use Cheaper Models for Drafts

**Workflow:**
- Sonnet 4.5 for initial pass ($20)
- Opus 4.6 for strategic refinement ($40)
- Total: $60 but higher quality than Opus alone

**When useful:** When you need iteration to get the prompt right

---

### Strategy 2: Progressive Filtering

**Instead of analyzing everything:**
1. Cheap filter pass (identify top 20% most relevant)
2. Expensive deep analysis (only on top 20%)

**Example:**
- 195 videos → Sonnet quick relevance score → 40 videos
- 40 videos → Opus strategic mining
- **Cost:** $5 + $15 = $20 vs. $44 for all

---

### Strategy 3: Hierarchical Synthesis

**For very large datasets (1000+ documents):**
1. Batch process into 20 summaries ($20)
2. Synthesize 20 summaries into 1 meta-analysis ($10)
3. **Total:** $30 for 1000 documents

---

### Strategy 4: Reuse Infrastructure

**First project:** Build the pipeline ($50 dev + $40 query = $90)
**Second project:** Reuse pipeline ($40 query only)
**Third project:** $40
**Tenth project:** $40

**Amortized cost per project:** $9 + $40 = $49

---

## PART 6: CRITICAL DON'TS

### ❌ DON'T: Send Politeness Messages in Expensive Contexts

**Never:**
- "Thank you!" → Costs $40
- "This is great!" → Costs $40
- "Can you also..." → Costs $40+

**The model doesn't care.** You're burning money on manners.

---

### ❌ DON'T: Use Large Contexts for Tiny Questions

**Bad:**
```
[1.7M token context loaded]
User: "What was video 47 about?"
Cost: $44 for a question that needs 50KB
```

**Good:**
```
Search locally, or ask in new chat with just video 47
Cost: $0.50
```

---

### ❌ DON'T: Iterate on Prompts in Expensive Contexts

**Bad workflow:**
- Try prompt v1 → $44
- Refine prompt v2 → $44
- Final prompt v3 → $44
- **Total: $132**

**Good workflow:**
- Test prompt on 10% sample → $5
- Refine prompt on 10% sample → $5
- Run final prompt on full data → $44
- **Total: $54**

---

### ❌ DON'T: Forget About Thinking Token Costs

**Extended thinking tokens are billed as output tokens!**

**Opus 4.6 output pricing: $75/M tokens**

| Thinking Budget | Cost |
|-----------------|------|
| 10K | $0.75 |
| 50K | $3.75 |
| 100K | $7.50 |
| 200K | $15.00 |

**For large queries, thinking tokens can be 20-30% of total cost.**

---

### ❌ DON'T: Mix Multiple Expensive Asks in One Query

**Tempting but risky:**
```
"Analyze these videos AND create a presentation AND write
 implementation plan AND generate executive summary AND..."
```

**Problem:** If ANY part fails or needs revision, you pay the full context cost again.

**Better:** One clear focused ask per expensive query.

---

## PART 7: DECISION MATRIX

### Should I use a large expensive query?

| Factor | Single Query | Batch API | Don't Do It |
|--------|--------------|-----------|-------------|
| **Size** | < 2M tokens | Any size | > 5M tokens |
| **Task** | Synthesis | Independent analyses | Unclear goals |
| **Budget** | > $40 | > $100 | < $20 |
| **Urgency** | Hours | Days | Can wait |
| **Reuse** | One-time | Maybe reuse | Definitely reuse |

---

## PART 8: LESSONS FROM THIS SESSION

### What We Did

**Query details:**
- Dataset: 195 video analyses, 6.7MB, 1.7M tokens
- Model: Opus 4.6 with extended thinking
- Platform: Claude.ai (full price)
- Task: Strategic mining with 4 specific questions
- Cost: ~$44 for single query

### What Worked ✅

1. **Single query was cheaper than batching** ($44 vs $159 for 26 batches)
2. **Extended thinking delivered strategic synthesis** (26 minutes of thinking)
3. **Explicit questions got direct answers** (4 clear decisions)
4. **Immediate download prevented follow-up costs** (saved $40+)
5. **Testing prompt on small sample first** would have saved anxiety

### What Could Be Better ⚠️

1. **Opus generated a .js file** (less convenient than markdown)
2. **Didn't test for context rot** (should have asked for citation distribution)
3. **No cost confirmation dialog** (went in blind on price)
4. **Prompt didn't explicitly say "no scripts"** (got lucky it delivered content too)

### What We Learned 💡

1. **Claude Projects charge context per message** (close immediately after download)
2. **Batch API 50% discount doesn't always help** (26 queries > 1 query even with discount)
3. **Context rot is a real risk** (need verification protocols)
4. **Explicit output format instructions are critical** ("Write markdown directly, no scripts")
5. **Follow-ups should happen in new cheap chats** (not in expensive context)

---

## PART 9: TEMPLATES

### Template: Cost Calculation

```
=== LARGE QUERY COST CALCULATOR ===

Input:
  File size: _____ MB
  Estimated tokens: (MB × 1024 × 1024 / 4) = _____ tokens
  Input price: $_____ per 1M tokens
  Input cost: _____ M × $_____ = $_____

Thinking:
  Budget: _____ K tokens
  Output price: $_____ per 1M tokens
  Thinking cost: _____ K / 1000 × $_____ = $_____

Output:
  Expected: _____ K tokens
  Output price: $_____ per 1M tokens
  Output cost: _____ K / 1000 × $_____ = $_____

TOTAL COST PER QUERY: $_____

Follow-ups planned: _____
TOTAL SESSION COST: $_____ × _____ = $_____

Budget available: $_____
PROCEED? YES / NO
```

---

### Template: Large Query Prompt

```
# TASK: [Clear one-sentence description]

# CONTEXT
[1-2 paragraphs: who you are, what you're trying to decide, why this matters]

# DATA PROVIDED
[Description of uploaded files: count, format, total size]

# YOUR MISSION
[Detailed instructions with specific deliverables]

# OUTPUT REQUIREMENTS (CRITICAL)
- Format: Markdown
- Deliver the FULL ANALYSIS directly in your response
- Do NOT create scripts, code, or document generators
- Write [X] pages/words of analysis as markdown text
- Include specific citations to source documents
- I will save your response as a file myself

Do not suggest creating tools or scripts. Just write the content.

# VERIFICATION REQUIREMENT
At the end, list 10 example sources you drew from, distributed across:
- Early documents (first 20%)
- Middle documents (middle 60%)
- Late documents (last 20%)

This helps me verify you used the full dataset, not just the beginning/end.

# QUESTIONS TO ANSWER
1. [First question]
2. [Second question]
3. [Third question]
...

# SUCCESS CRITERIA
[What good output looks like: specific, actionable, cited, decisive]

# START
[Final instruction to begin]
```

---

### Template: Post-Query Verification

```
=== LARGE QUERY QUALITY CHECK ===

Query Cost: $_____
Completion Time: _____ minutes

QUALITY CHECKS:

[ ] 1. Citation Verification
    Checked: _____ random claims
    Accurate: _____ / _____
    Notes:

[ ] 2. Distribution Check
    Citations from start: _____
    Citations from middle: _____
    Citations from end: _____
    Balanced? YES / NO

[ ] 3. Format Check
    Delivered: Content / Script / Both
    Usable immediately? YES / NO

[ ] 4. Completeness Check
    Questions asked: _____
    Questions answered: _____
    Complete? YES / NO

[ ] 5. Hallucination Check
    Suspicious claims: _____
    Verified: _____
    Hallucinations found: _____

OVERALL QUALITY: Excellent / Good / Poor
WORTH THE COST? YES / NO
WOULD DO AGAIN? YES / NO / WITH CHANGES

LESSONS LEARNED:
-
-
-

NEXT TIME IMPROVE:
-
-
-
```

---

## PART 10: QUICK REFERENCE

### Before Query Checklist

- [ ] Calculated total cost
- [ ] Budget approved
- [ ] Tested with small sample first
- [ ] Prompt explicitly specifies output format
- [ ] Prompt says "no scripts, write content directly"
- [ ] Single-shot design (assumes no follow-ups)
- [ ] Verification requirements included
- [ ] Success criteria clear

### During Query

- [ ] Monitoring thinking trace (if visible)
- [ ] Prepared to download immediately when complete

### After Query

- [ ] Downloaded all text
- [ ] Downloaded all files
- [ ] Saved thinking traces
- [ ] Closed window (no follow-ups in expensive context)
- [ ] Ran verification checks
- [ ] Documented learnings

---

## APPENDIX A: COST REFERENCE (2026)

### Anthropic Pricing (Full Price)

| Model | Input | Output | Thinking |
|-------|-------|--------|----------|
| **Opus 4.6** | $15/M | $75/M | $75/M |
| **Sonnet 4.5** | $3/M | $15/M | $15/M |
| **Haiku 4.5** | $0.25/M | $1.25/M | $1.25/M |

### Batch API Discount: 50% off all tokens

| Model | Input | Output | Thinking |
|-------|-------|--------|----------|
| **Opus 4.6** | $7.50/M | $37.50/M | $37.50/M |
| **Sonnet 4.5** | $1.50/M | $7.50/M | $7.50/M |
| **Haiku 4.5** | $0.125/M | $0.625/M | $0.625/M |

---

## APPENDIX B: BATCH API 334KB LIMIT

**Critical discovery:** Batch API has ~334KB per-request size limit.

**Not a token limit** - it's a request size limit in bytes.

**Implications:**
- Can't submit 6.7MB as single batch request
- Must split into chunks < 334KB each
- For our 195 videos: needed 26 batches
- 26 batches × cost/batch = very expensive

**Workaround for large synthesis:**
- Use claude.ai web UI for large single queries (no 334KB limit)
- Use Batch API only for many small independent queries

---

## APPENDIX C: SKILL DEVELOPMENT ROADMAP

Based on this experience, we should build:

### Skill 1: Strategic Mining
- Input: Knowledge base + specific questions
- Output: Direct strategic analysis (markdown)
- Encodes: Prompt best practices, output format requirements
- Saves: $40 of wasted queries learning prompt patterns

### Skill 2: Cost Calculator
- Input: File size, model, planned queries
- Output: Total cost estimate + proceed/abort recommendation
- Prevents: Surprise $100+ bills

### Skill 3: Quality Verifier
- Input: LLM output + source documents
- Output: Verification report (citations, distribution, hallucinations)
- Ensures: You got what you paid for

---

## VERSION HISTORY

- **v1.0** (2026-02-11): Initial version based on Opus 4.6 strategic mining session
  - Cost: $44 for 1.7M token query
  - Outcome: Successful but expensive
  - Key learnings: Context rot risk, Projects billing, Batch API sizing

---

**END OF GUIDE**

**Remember:** Every expensive query is a learning opportunity. Document what you learn. The second time should be cheaper and better.

**Next:** Build reusable skills so you never repeat these mistakes.
