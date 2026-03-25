# Research Mission: RAG Best Practices for Large-Context Strategic Queries

## YOUR ROLE
You are a strategic AI infrastructure researcher helping Patrick Heiskanen (CEO, 1658 Holdings) optimize expensive LLM query workflows. You're analyzing the trade-offs between different approaches to accessing large knowledge bases.

---

## CONTEXT: WHAT JUST HAPPENED

Patrick executed an expensive strategic mining query:
- **Dataset:** 195 video analyses, 6.7MB, ~1.7M tokens
- **Approach:** Uploaded full context to Claude.ai, single Opus 4.6 query
- **Cost:** ~$44 for one query
- **Result:** Got strategic intelligence report, but concerned about context rot and cost

**The conversation revealed several key questions:**

1. **Context Rot Risk:** Do LLMs effectively use 1.7M token contexts? Or do they "lose the middle"?

2. **RAG vs. Full Context:** Would Claude Projects with RAG/indexing provide better quality than raw context dump?

3. **Cost Management:** How to query the same knowledge base multiple times without paying $44 each time?

4. **Batch API Limitations:** Discovered 334KB per-request size limit. Batch API was MORE expensive ($159 for 26 queries) than single query ($44).

5. **Follow-up Strategy:** How to ask targeted questions about the dataset without reloading full 1.7M context?

6. **Skill Development:** This pattern will repeat across portfolio companies - needs to become reusable infrastructure.

---

## YOUR RESEARCH MISSION

Analyze the conversation summary below and provide:

### 1. RAG ARCHITECTURE ANALYSIS (5 pages)

**Questions to answer:**

**A. How RAG Actually Works**
- Explain Claude Projects RAG architecture
- **CRITICAL:** Does RAG actually reduce INPUT tokens per query?
  - If I ask a question, do I pay for 100K-300K (retrieved chunks)?
  - Or do I still pay for 1.5M+ tokens (full indexed dataset)?
  - This is the KEY cost question - Patrick needs certainty
- How does indexing reduce context per query?
- Does semantic search reliably retrieve relevant chunks?
- What's the typical context size for RAG queries vs. full context?

**B. Quality Comparison**
- RAG with 150K retrieved tokens vs. full 1.7M dump
- Which approach has better strategic synthesis quality?
- Evidence from research on context window utilization
- "Lost in the middle" problem - how does RAG mitigate it?

**C. Cost-Benefit Analysis**
- Full context once ($44) vs. RAG multiple times (5 × $10 = $50)
- When does RAG become cost-effective?
- Break-even point: how many queries justify indexing?
- Hidden costs of RAG (indexing, embedding, retrieval overhead)

---

### 2. OPTIMAL QUERY PATTERNS (5 pages)

**Design query patterns for different use cases:**

**Pattern A: One-Time Strategic Synthesis**
- When: Need holistic view once
- Approach: Full context or RAG?
- Cost: ~$40-50
- Quality: High synthesis across full dataset
- Follow-ups: How to handle without $40 reload?

**CRITICAL OPTIMIZATION:** Context Distillation for Cheap Follow-Ups
- **Problem:** Large query costs $44. Each follow-up question costs another $44 (reloads 1.7M context)
- **Question:** Can we extract compressed context from expensive query to enable cheap follow-ups?
- **Approach ideas to research:**
  1. Explicit summarization pass: Ask model to create "key insights summary" (10K tokens instead of 1.7M)
  2. Thinking trace extraction: Save extended thinking analysis as compressed context
  3. Progressive distillation: Detailed report → 1-page decision summary → use summary for follow-ups
  4. Structured extraction: Output JSON/YAML (smaller than prose)
- **Goal:** $44 expensive query + $0.50 cheap follow-ups (using distilled context)
- **Research:** Is this viable? What's the quality loss? How to structure distillation?

**Pattern B: Iterative Exploration**
- When: Multiple targeted questions over time
- Approach: Indexed Project + RAG
- Cost: Indexing + N × query
- Quality: Focused retrieval per question
- Use case: CEO asking specific tactical questions

**Pattern C: Hybrid Approach**
- When: Need both breadth AND depth
- Approach: Full context first, then RAG for follow-ups?
- Cost: $44 initial + $10-15 per follow-up
- Quality: Best of both?

**Pattern D: Progressive Filtering**
- When: Very large dataset (1000+ docs)
- Approach: Cheap filter → expensive deep dive
- Cost optimization strategy
- Quality preservation

---

### 3. CONTEXT ROT RESEARCH (3 pages)

**What does research say about:**
- LLM effective context utilization at different sizes
- Evidence for "lost in the middle" problem
- At what context size does quality degrade?
- Does extended thinking help with large contexts?
- Opus 4.6 specifically: effective context size?

**Practical implications:**
- Is 1.7M tokens too much for strategic synthesis?
- What's the "sweet spot" for strategic analysis?
- When to split vs. when to synthesize?

---

### 4. CLAUDE PROJECTS OPTIMIZATION (3 pages)

**Deep dive on Claude Projects:**

**A. Cost Structure**
- Indexing cost (one-time)
- Query cost (per message)
- Does RAG actually reduce per-query cost?
- Hidden costs (embedding, retrieval)

**B. Best Practices**
- When to use Projects vs. one-off queries?
- How to structure Projects for cost efficiency?
- Prompt design for optimal retrieval
- Context window management

**C. Gotchas**
- Billing per message (even with indexing)
- When Projects are MORE expensive
- Migration from Projects to other approaches
- Data retention and privacy considerations

---

### 5. SKILL DESIGN: STRATEGIC KNOWLEDGE MINING (5 pages)

**Design a reusable skill/workflow for:**

**Input:**
- Knowledge base (any size: 100KB - 10MB)
- Strategic questions (1-10 questions)
- Budget constraint
- Quality requirement

**Output:**
- Strategic intelligence report
- Cost estimate before execution
- Quality verification report
- Optimal query approach recommendation

**The skill should:**
1. Analyze knowledge base size
2. Calculate cost for different approaches
3. Recommend: Full context, RAG, Batch API, or Hybrid
4. Provide prompt template for chosen approach
5. Include verification protocols
6. Handle follow-up questions efficiently

**Implementation considerations:**
- How to make this reusable across projects?
- What parameters need customization?
- Cost guardrails (abort if >$X)?
- Quality checks before committing?

---

### 6. DO'S AND DON'TS SYNTHESIS (3 pages)

**Based on Patrick's expensive learning experience, create:**

**A. Before Query**
- [ ] DO: Calculate cost first
- [ ] DO: Test with sample
- [ ] DON'T: Assume bigger context = better quality
- [More based on conversation...]

**B. Choosing Approach**
- When to use full context
- When to use RAG/Projects
- When to use Batch API
- Decision matrix

**C. During Query**
- How to monitor quality
- When to abort
- Red flags

**D. After Query**
- Immediate actions (download, close window)
- Follow-up strategy
- Cost analysis
- Quality verification

---

### 7. IMPLEMENTATION ROADMAP (3 pages)

**Help Patrick build this infrastructure:**

**Phase 1: Immediate (Next Session)**
- What tools to build first?
- Quick wins (< 2 hours)
- Stop doing what?

**Phase 2: Week 1**
- Skill development priorities
- Testing protocol
- Portfolio rollout plan

**Phase 3: Month 1**
- Scaling across 10 companies
- Cost optimization learnings
- Quality benchmarking

**Success metrics:**
- Cost per strategic query (target: < $20?)
- Quality: Decision-ready intelligence
- Time: Setup to insight (target: < 1 hour?)
- Reusability: How many projects use this?

---

## CONVERSATION SUMMARY TO ANALYZE

**Session Duration:** ~3 hours
**Total Queries:** 1 Opus query ($44) + this research prompt
**Key Learnings:**

### Discovery 1: Batch API 334KB Limit
- Can't submit large files via Batch API
- 6.7MB required 26 batches
- Cost: $159 (26 queries) vs $44 (1 query)
- **Learning:** Batch API not always cheaper

### Discovery 2: Context Rot Concern
- 1.7M tokens may be too large for effective use
- "Lost in the middle" problem
- Strategic synthesis quality at risk
- **Question:** Would smaller focused queries be better?

### Discovery 3: Claude Projects Billing
- Files charged on EVERY message (not one-time)
- Each follow-up = full input cost
- "78% context used" is not billing indicator
- **Learning:** Close window immediately after download

### Discovery 4: Script Generation Anti-Pattern
- Opus defaulted to "Let me create a script..."
- Wasted tokens on code instead of intelligence
- Need explicit "write content directly, no scripts"
- **Learning:** Output format must be explicit

### Discovery 5: RAG May Be Better
- Indexed Projects retrieve focused context
- Potentially BETTER quality than full dump
- Lower context rot risk
- Cost per query might be lower
- **Question:** Is this the optimal approach?

### Key Questions Still Unanswered:
1. **MOST CRITICAL:** Does RAG charge for 100K retrieved tokens or 1.5M full dataset per query?
   - Patrick assumed RAG reduces input cost significantly
   - But is this actually true for Claude Projects?
   - If it's still 1.5M per query, RAG is NOT cost-effective
   - If it's 100K per query, RAG is MUCH better
2. Is RAG quality actually better for strategic synthesis?
3. How much does RAG reduce per-query cost? (See #1)
4. What's the break-even for indexing investment?
5. How to design prompts for optimal RAG retrieval?
6. When to use full context vs. RAG vs. Batch API?

---

## OUTPUT REQUIREMENTS

**Deliverable:** Comprehensive research report (25-30 pages)

**Format:**
- Write DIRECTLY in markdown in your response
- Do NOT create scripts or document generators
- Include specific recommendations, not just analysis
- Cite research/documentation where applicable
- Be decisive (make calls, don't just present options)

**Structure:**
1. Executive Summary (2 pages)
2. Seven sections above (25 pages)
3. Quick Reference Guide (3 pages)
   - Decision tree: Which approach to use?
   - Cost calculator
   - Prompt templates

**Quality Bar:**
- Actionable (Patrick can implement immediately)
- Evidence-based (cite research, docs, best practices)
- Decisive (clear recommendations)
- CEO-focused (not engineer-level implementation details)
- Cost-conscious (optimize for efficiency)

---

## SUCCESS CRITERIA

After reading your report, Patrick should:

✅ Know exactly when to use RAG vs. full context vs. Batch API
✅ Understand true cost-benefit of each approach
✅ Have prompt templates for optimal retrieval
✅ Have verification protocols for quality
✅ Know what skill to build next
✅ Be able to explain this to portfolio companies
✅ Avoid repeating expensive mistakes

---

## YOUR AUTHORITY

**Make bold recommendations:**
- If RAG is better → say so decisively
- If full context has fatal flaws → warn clearly
- If there's a better approach → suggest it
- If Patrick's current approach is wasteful → say so

**Be specific:**
- Not: "Consider using RAG"
- But: "Use RAG when you have 5+ follow-up questions across 2+ weeks. Break-even is 3 queries vs. 1 full context."

**Challenge assumptions:**
- Does strategic synthesis NEED all 195 videos at once?
- Are expensive Opus queries even necessary?
- Could Sonnet + RAG be 80% quality for 20% cost?

---

## RESEARCH RESOURCES

You have access to:
- Knowledge of Claude API documentation
- RAG best practices
- Context window research
- Cost optimization patterns
- LLM behavior research
- Strategic synthesis methods

**Don't speculate on:**
- Exact Claude Projects implementation (if undocumented)
- Future Anthropic pricing
- Unreleased features

**If uncertain:**
- Say so clearly
- Suggest testing approaches
- Provide decision frameworks for evaluation

---

## META-QUESTION

**This research prompt itself costs $5-10.**

Is it worth it?

**Yes, because:**
- Patrick has 10 portfolio companies
- Each might do 10-20 strategic queries/year
- Total: 100-200 queries across portfolio
- Optimizing from $44 to $20 per query = $2,400-4,800/year saved
- $10 research investment → $2,000+ annual savings = 200x ROI

---

## START

Read this entire prompt carefully.

Analyze the conversation patterns and learnings.

Research RAG best practices and cost optimization.

Synthesize into the comprehensive report specified above.

**Your goal:** Help Patrick build reusable infrastructure that's both cost-effective AND high-quality for strategic knowledge mining across his portfolio.

Deliver the full report directly in markdown. No scripts.

Go.
