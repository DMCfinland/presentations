# Case Study: Batch API vs Single Query for Strategic Mining

## DATE: 2026-02-11
## DECISION NEEDED: How to run Opus 4.6 strategic mining on 195 videos

---

## THE SITUATION

Patrick has 195 analyzed videos (6.7MB consolidated) from Nate B Jones AI strategy content. He needs Opus 4.6 to mine these for strategic intelligence to answer 4 critical business questions:

1. **Employee Second Brain:** Should he build one for 50 employees?
2. **Document Architecture:** How to organize knowledge for 10 portfolio companies?
3. **Work Style:** GSD Protocol vs Ralph Wiggum approach?
4. **Next Project:** What to build in next 10-20 hours?

## THE CONSTRAINT

**Batch API has ~334KB per-request size limit** (not just token limits)

This forces a choice between two approaches.

---

## OPTION A: 26 BATCH API QUERIES

### What It Means
- Split 195 videos into 26 batches (~7-8 videos each, ~270KB per batch)
- Submit 1 Batch API job with 26 independent requests
- Anthropic processes all 26 in parallel
- Each request: independent Opus 4.6 query with own thinking budget
- Download 26 separate responses
- **Patrick synthesizes** the 26 responses into final strategic report

### Costs
- **Input:** 1.72M tokens × $7.50 = $12.90
- **Thinking:** 1.30M tokens (26 × 50K) × $37.50 = $48.75
- **Output:** 2.60M tokens (26 × 100K) × $37.50 = $97.50
- **TOTAL:** $159.15 (with 50% Batch API discount)

### Pros
✅ 50% cost savings ($159 vs $320)
✅ Parallel processing (all 26 run simultaneously)
✅ Each batch gets full 50K thinking + 100K output budget
✅ Proven infrastructure (already did 189 videos this way)
✅ Can re-run individual batches if needed

### Cons
❌ Opus sees each batch independently (no cross-batch synthesis during analysis)
❌ 26 separate responses need manual synthesis
❌ Risk of inconsistent insights across batches
❌ Patrick must do final integration work (10-20 hours?)
❌ More complex workflow (submit, monitor, download, synthesize)
❌ Strategic questions answered 26 times in fragments

### Key Unknowns
- How much synthesis effort is realistic?
- Will 26 fragmented responses lose strategic coherence?
- Can pattern recognition work across disconnected analyses?
- Is $161 savings worth the synthesis complexity?

---

## OPTION B: 1 CLAUDE.AI QUERY

### What It Means
- Upload 2 files to claude.ai web UI:
  - OPUS-DIRECT-MINING.md (prompt)
  - consolidated-videos-context.md (all 195 videos, 6.7MB)
- Single Opus 4.6 conversation with extended thinking
- Opus sees ALL 195 videos at once
- **Opus synthesizes** across all videos during analysis
- Delivers integrated strategic report in one response

### Costs
- **Estimated:** $320-400 (full price, no Batch API discount)
- (Exact pricing depends on actual token usage)

### Pros
✅ Opus sees complete dataset (holistic analysis)
✅ Built-in synthesis across all 195 videos
✅ Strategic questions answered with full context
✅ Pattern recognition across entire corpus
✅ Single coherent response (no manual synthesis)
✅ 5-minute setup (drag & drop 2 files)
✅ Extended thinking can synthesize deeply

### Cons
❌ 2x cost ($320 vs $159)
❌ Single point of failure (if query fails, re-do entire thing)
❌ Less control over token budgets
❌ Can't parallelize or re-run parts
❌ Manual upload (no automation)

### Key Unknowns
- Does Opus actually synthesize better with full context?
- Or does it get overwhelmed by 6.7MB at once?
- Will extended thinking be sufficient for this complexity?
- Is the holistic view worth $161 extra?

---

## THE STRATEGIC QUESTION

**This isn't just about THIS mining job.**

This decision has implications for:
- **Future mining jobs:** More YouTube research, other knowledge bases
- **Workflow design:** How to structure large-scale LLM work
- **Budget allocation:** When to optimize for cost vs quality
- **Infrastructure investment:** What tooling to build

**The real question:**
> When doing strategic synthesis work with LLMs, is it better to:
> - Let the model see everything and synthesize (expensive, holistic)
> - OR split into parallel queries and synthesize manually (cheaper, fragmented)

---

## WHAT WE NEED FROM OPUS

Patrick needs **strategic guidance** on this decision that considers:

### 1. Quality Trade-offs
- How much does synthesis quality suffer in fragmented (Batch) approach?
- Does Opus actually leverage full context in single-query approach?
- Which approach produces more actionable strategic intelligence?
- What's the expected quality difference: 10%? 50%? Negligible?

### 2. Synthesis Effort
- If we do 26 batches, how much work is the human synthesis?
- Is it 2 hours? 20 hours? Manageable or crushing?
- Can the fragmented insights even BE synthesized effectively?
- What synthesis methods work for 26 independent analyses?

### 3. Cost-Benefit Analysis
- Is $161 savings worth it given synthesis burden?
- At what cost difference does single-query become worth it? ($50? $100? $200?)
- What's the break-even point for Patrick's time value?
- When should he optimize for cost vs. convenience?

### 4. Strategic Patterns
- When does Batch API make sense vs. single queries?
- What characteristics of a task favor fragmented approach?
- What characteristics demand holistic synthesis?
- How to decide BEFORE committing resources?

### 5. Future Workflow Design
- Should Patrick build synthesis tooling for batch outputs?
- Or should he just use claude.ai for strategic work?
- What infrastructure investments make sense?
- How to scale this across portfolio companies?

---

## PROMPT FOR OPUS

**Mission:** Analyze this case study and provide strategic decision guidance.

**Deliverable:** A comprehensive analysis with:

1. **RECOMMENDATION:** Option A (Batch API) or Option B (claude.ai) with reasoning
2. **QUALITY ANALYSIS:** Expected difference in strategic intelligence quality
3. **SYNTHESIS FRAMEWORK:** If Batch API, how to synthesize 26 responses effectively
4. **DECISION MATRIX:** When to use which approach in future
5. **DO'S AND DON'TS:** Best practices for large-scale LLM strategic work
6. **TOOLING RECOMMENDATIONS:** What infrastructure to build/buy
7. **PORTFOLIO IMPLICATIONS:** How to scale this across 10 companies

**Context You Need:**
- Patrick is CEO, not engineer (but technical enough to run scripts)
- Time is valuable: 10-20 hour projects are his sweet spot
- Portfolio-wide AI transformation in progress
- This decision shapes future knowledge activation strategy
- Budget exists but waste is unacceptable

**Quality Bar:**
- Decisive: Make a clear recommendation, don't hedge
- Evidence-based: Draw from your knowledge of LLM behavior
- Practical: Consider actual human synthesis burden
- Strategic: Think 2-3 moves ahead for portfolio implications
- Honest: If you don't know, say so and suggest tests

---

## RESEARCH QUESTIONS FOR OPUS

Please investigate and answer:

1. **Fragmentation Loss:** How much strategic coherence is lost when splitting analysis into 26 independent queries?

2. **Context Window Utilization:** Do large LLMs actually leverage 6.7MB contexts effectively? Or do they "lose the thread" with too much data?

3. **Synthesis Methods:** What are proven techniques for synthesizing multiple independent LLM analyses into coherent strategic intelligence?

4. **Cost-Quality Curve:** At what cost differential does quality loss become acceptable for strategic work?

5. **Batch Job Patterns:** When are batch jobs actually superior (beyond just cost)? Are there cases where fragmentation helps?

6. **Human-AI Synthesis:** Is a human synthesizing 26 AI outputs better or worse than AI synthesizing everything at once?

7. **Extended Thinking Impact:** Does extended thinking change the answer? (More budget for synthesis in single query vs. parallel deep thinking in batches)

8. **Failure Modes:** What are the likely failure modes of each approach, and how to mitigate?

---

## WHAT SUCCESS LOOKS LIKE

After Opus analyzes this case study, Patrick should:
- ✅ Know which approach to use (A or B) with confidence
- ✅ Understand the trade-offs clearly
- ✅ Have a framework for future similar decisions
- ✅ Know what infrastructure to build
- ✅ Be able to explain the decision to portfolio companies
- ✅ Have DO's and DON'Ts to avoid future mistakes

---

## META-QUESTION

**Is THIS case study itself worth the cost of an Opus query?**

The irony: We're asking Opus to help us decide how to query Opus.

But this is strategic research that applies beyond just this mining job. If the answer informs:
- Future YouTube research (more channels to analyze)
- M&A research automation workflows
- Knowledge base activation strategies
- Portfolio-wide AI infrastructure

...then the ROI on this meta-research is high.

**Cost of this meta-analysis:** ~$5-10 (single Opus query, small context)
**Potential savings from better decisions:** Hundreds of dollars + dozens of hours

**Verdict:** This case study is worth researching.

---

## NEXT STEPS

1. Submit this case study to Opus 4.6
2. Review Opus strategic guidance
3. Make final decision on mining approach
4. Execute chosen approach
5. Document learnings in BATCH-API-GUIDE.md
6. Update project DO's and DON'Ts

---

## APPENDIX: TECHNICAL DETAILS

### Batch API Characteristics
- Per-request size limit: ~334KB (not documented, discovered empirically)
- Per-request token limits: Model-dependent (Opus 4.6: large)
- Pricing: 50% discount on input/output
- Extended thinking: Supported (budget_tokens parameter per request)
- Processing: Parallel (all requests in batch run simultaneously)
- Delivery: All-or-nothing (full batch completes before download)

### Single Query Characteristics
- File upload limit: 20 files in claude.ai Projects
- No per-file size limit (tested: 6.7MB works)
- Pricing: Full price (no discount)
- Extended thinking: Supported via UI toggle
- Processing: Sequential conversation
- Delivery: Streaming response

### Previous Experience
- Successfully processed 189 videos via Batch API (Sonnet 4.5)
- Cost: ~$20 with batch discount
- Quality: Excellent, consistent framework application
- Synthesis: Not attempted (each video analyzed independently)
- This job: More complex (strategic mining, not just analysis)

---

**END CASE STUDY**
