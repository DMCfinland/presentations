# Opus Strategic Review: Research Infrastructure Gaps & Build Plan
## 1658 Holdings Oy — February 2026

---

## Your Task

You are reviewing 1658 Holdings' research infrastructure to identify strategic gaps and create a prioritized build plan. This is strategic planning work that will guide investment across 10 portfolio companies.

**Context:** Patrick has built YouTube Research KB ($89 invested, 196 videos, proven architecture). He's about to start new research projects and wants to know:
1. What infrastructure is missing?
2. What does the YouTube KB already teach us about filling these gaps?
3. What should we build first?
4. How to prioritize across competing needs?

**Your deliverables:**
1. Gap analysis with strategic impact assessment
2. YouTube KB mining for relevant insights
3. Prioritized build plan (Tier 1/2/3)
4. Resource allocation recommendations
5. Success criteria per deliverable

---

## 1. WHAT WE HAVE (Current Infrastructure)

### Research Execution Infrastructure (✅ Built)

**Three-Tier Indexing Architecture:**
- File: `_shared/best-practices/knowledge-base-indexing.md` (723 lines)
- What it covers: Routing index design, digest compression, cross-reference maps
- Quality: Comprehensive, proven with 196 videos
- Gap: Built for 50-500 items, doesn't address >500 or <50

**Research Chunking & Cost Optimization:**
- File: `_shared/best-practices/research-chunking-and-cost-optimization.md` (1,080 lines)
- What it covers: Three-tier architecture, context window failure modes, progressive filtering, batch API best practices
- Quality: Comprehensive, includes real economics ($89 project breakdown)
- Gap: Execution-focused, missing design methodology

**Context Window Failure Modes:**
- File: `_shared/best-practices/context-window-failure-modes.md` (124 lines)
- What it covers: 4 failure modes (sampling bias, primacy/recency, confident extrapolation, RAG chunk gambling), detection signals
- Quality: Empirically validated ($44 Opus session evidence)
- Gap: Detection is covered, prevention is covered, but no remediation workflow

**Workflow Decision Framework:**
- File: `_shared/workflows/WORKFLOW-DECISION-FRAMEWORK.md` (13 sections)
- What it covers: When to index vs batch vs direct load, model selection, interface selection, orchestration patterns
- Quality: Comprehensive decision trees
- Gap: Execution routing, not research design

**Model Strategy:**
- File: `MODEL-STRATEGY.md` (412 lines)
- What it covers: Opus/Sonnet/Haiku selection, orchestration patterns, cost optimization
- Quality: Proven hybrid workflows, 79-94% savings
- Gap: Model selection is solved, but not prompt design

### Strategic Frameworks (✅ Built)

**AI Deployment Principles:**
- File: `_shared/best-practices/ai-deployment-principles.md`
- What it covers: 18 principles + 18 anti-patterns for AI deployment
- Quality: Strategic, reusable across 10 companies
- Gap: Deployment is covered, but research design is not

**KB Utilization Strategy:**
- File: `_shared/best-practices/kb-utilization-strategy.md`
- What it covers: How to USE research (Phase 1-3 adoption, pull vs push)
- Quality: Strategic, from Opus review of YouTube KB
- Gap: Usage is covered, but not creation workflow

### Prompts & Templates (⚠️ Partially Built)

**Existing Opus prompts:**
- `opus-research-indexing-best-practices.md` — How to design indexes
- `opus-youtube-kb-strategic-review.md` — Utilization strategy
- `opus-document-architecture-decision.md` — Strategic architecture decisions
- Various review prompts (Järvisydän SEO, Finnish governance synthesis)

**Gap:** No systematic prompt library. Prompts are scattered. Missing:
- Mining prompts (extracting insights from sources)
- Compression prompts (creating digests) — exists in chunking doc but not cataloged
- Synthesis prompts (finding patterns across sources)
- Validation prompts (quality checking)
- One-line generation prompts (routing index summaries)

---

## 2. WHAT WE'RE MISSING (Gaps Identified)

### Gap 1: Research Design Methodology ⚠️ CRITICAL
**Problem:** We know HOW to execute research, but not how to SCOPE it.

**Missing:**
- How to define good research questions vs bad ones
- How to scope collection size (50 items? 500? When is it enough?)
- How to prioritize sources (which to include, which to skip)
- How to structure phases (pilot → scale → validate)
- Decision gates: when to continue vs stop vs pivot
- Exit criteria per phase
- Research ROI estimation BEFORE starting

**Strategic impact:** Without this, every new research project is ad-hoc. Can't replicate success systematically.

**Ask Opus to consult YouTube KB:** Query routing index for videos about:
- Research design
- Strategic planning
- Decision-making frameworks
- Systems thinking
- Scoping and prioritization

### Gap 2: Quality Assessment Framework ⚠️ CRITICAL
**Problem:** No systematic way to validate research quality.

**Missing:**
- Quality gates for routing index, digests, synthesis
- Red flags for unreliable research
- Validation checklist (10 questions before trusting research)
- When to redo vs accept "good enough"
- Contamination detection workflow (10-15% training data problem)
- Peer review protocol (when to get second opinion)
- Confidence scoring (how certain are we about each insight?)

**Strategic impact:** Without this, we might make decisions on contaminated or low-quality research.

**Ask Opus to consult YouTube KB:** Query for videos about:
- Quality control
- Trust mechanisms
- Validation frameworks
- E-E-A-T (expertise, experience, authoritativeness, trustworthiness)
- Error detection

### Gap 3: Synthesis Workflow ⚠️ MAJOR
**Problem:** Summarizing individual sources is solved. Synthesizing ACROSS 100+ sources is ad-hoc.

**Missing:**
- Step-by-step synthesis process
- Pattern recognition workflow
- Cross-referencing techniques
- Avoiding synthesis contamination
- Citation discipline (ensuring synthesis traces to sources)
- Conflicting source resolution
- From 100 sources → 5 strategic insights (systematic process)

**Strategic impact:** This is the highest-value activity (turning data into decisions) but currently the most ad-hoc.

**Ask Opus to consult YouTube KB:** Query for videos about:
- Synthesis and pattern recognition
- Second brain systems (capture → classify → surface)
- Knowledge management
- Strategic thinking
- Connecting dots

### Gap 4: Golden Prompt Library ⚠️ MAJOR
**Problem:** Reinventing prompts every time instead of reusing proven ones.

**Missing:** Organized prompt library in `_shared/prompts/research/` with:
- Mining prompts (extracting insights)
- Compression prompts (creating digests)
- Synthesis prompts (finding patterns)
- Validation prompts (quality checking)
- Honesty prompts ("what % did you read?")
- One-line generation prompts (routing index)
- Cross-reference prompts (finding connections)
- Research question design prompts (scoping a project)

**Strategic impact:** Every reused prompt saves 30-60 minutes of iteration. 20 golden prompts × 10 companies × 10 uses = 4,000 hours saved.

**Ask Opus to consult YouTube KB:** Query for videos about:
- Prompt engineering
- AI agents and automation
- Workflow design
- Reusable frameworks

### Gap 5: Integration Playbook ⚠️ CRITICAL
**Problem:** Building research is solved. USING research is not.

**Missing:**
- Research-informed decision workflow (step-by-step)
- When to consult research vs wing it (decision tree)
- Query patterns for common scenarios
- Success metric tracking (simple)
- Pre-flight checklist integration
- Team enablement (making KB useful for others, not just Patrick)

**Strategic impact:** Opus said "use KB weekly" but HOW? Without this, research sits unused (zero-adoption death spiral).

**Ask Opus to consult YouTube KB:** Query for videos about:
- Decision-making frameworks
- Knowledge management in practice
- Adoption strategies
- Behavioral design
- Trust mechanisms (getting people to use AI tools)

### Gap 6: Maintenance Cadence (MEDIUM)
**Problem:** No plan for keeping research fresh over time.

**Missing:**
- Update vs rebuild decision criteria
- Pruning protocol (removing stale content)
- Adding new sources (incremental vs batch)
- Version control for knowledge
- Expiration dating content
- Quarterly review protocol

**Strategic impact:** Without maintenance, KB value decays. Fresh research = compounding asset. Stale research = liability.

### Gap 7: Cross-Project Synthesis (MEDIUM)
**Problem:** Multiple KBs exist independently (YouTube, Finnish governance, DMC mining).

**Missing:**
- Meta-index across projects
- Connection discovery (KB A insight → KB B application)
- Cross-KB query workflow
- Compound insights (synthesizing across KBs)

**Strategic impact:** The value is in CONNECTIONS. Multiple siloed KBs miss cross-domain insights.

### Gap 8: Research ROI Measurement (LOWER)
**Problem:** No framework for measuring whether research pays off.

**Missing:**
- Leading indicators (queries/week, hit rate)
- Lagging indicators (decisions influenced, time saved)
- Keep/expand/sunset decision framework
- Cost tracking per project
- Value attribution

**Strategic impact:** Can't optimize what we don't measure. But measurement overhead can exceed value.

---

## 3. YOUR DELIVERABLES

### Deliverable 1: Gap Analysis with Strategic Impact (Priority Matrix)

For each gap (1-8 above), assess:

**Strategic Impact:**
- What happens if we DON'T fill this gap?
- What's the cost of the gap over 12 months across 10 companies?
- Is this blocking current work or future expansion?

**Build Effort:**
- Hours to build (rough estimate: <2h / 2-8h / >8h)
- Cost to build (rough estimate: $0 / $1-10 / >$10)
- Requires new research or synthesis of existing work?

**Dependencies:**
- What must be built first?
- What's the critical path?

**Output format:**
```
| Gap # | Name | Impact (1-5) | Effort (1-5) | Priority Score | Tier |
|-------|------|--------------|--------------|----------------|------|
| 1     | Research Design | 5 | 3 | High | Tier 1 |
...
```

Priority Score: High (build first), Medium (build next), Low (defer)
Tier 1 = Blocking current work (build immediately)
Tier 2 = Improves current work (build within 30 days)
Tier 3 = Enables future expansion (build when needed)

### Deliverable 2: YouTube KB Mining Results

**Task:** Query the YouTube KB routing index for relevant insights about the 8 gaps.

For each gap, identify:
1. Which videos (by title and ID) contain relevant insights?
2. What specific frameworks, principles, or patterns apply?
3. Are there any anti-patterns or warnings?
4. What's the ONE best video to read in full for this gap?

**Sources to check:**
- Routing index: `YouTubeResearch-AIFiles/knowledge-base/_index/routing-index.yaml` (196 entries)
- Topic map: `YouTubeResearch-AIFiles/knowledge-base/_index/topic-map.yaml` (136 topics)
- Pattern map: `YouTubeResearch-AIFiles/knowledge-base/_index/pattern-map.yaml` (15 patterns)
- Greatest hits: `YouTubeResearch-AIFiles/knowledge-base/_index/greatest-hits-10.md` (top 10 videos)

**Key topics to search:**
- Research design: systems-thinking, strategic-planning, decision-frameworks
- Quality assessment: trust-mechanisms, validation, E-E-A-T
- Synthesis: pattern-recognition, second-brain, capture-classify-surface
- Prompts: prompt-engineering, ai-agents, automation
- Integration: behavioral-design, adoption, workflow-design
- Maintenance: sustainability, compounding, long-term-thinking

**Output format per gap:**
```
Gap 1: Research Design Methodology
- Relevant videos: [list 3-5 with IDs]
- Key frameworks: [e.g., "capture-classify-surface from video 002"]
- Anti-patterns: [e.g., "don't build before validating need - video 023"]
- Best deep-dive: [ONE video to read in full]
- Applied to this gap: [2-3 sentences on how KB insights solve this gap]
```

### Deliverable 3: Prioritized Build Plan (Tier 1/2/3)

**Tier 1: Build Immediately** (blocking current work)
For each Tier 1 item:
- What exactly to build (file name, structure, 5-section outline)
- Estimated effort (hours)
- Estimated cost (if any LLM processing needed)
- Who should build it (Patrick, Sonnet, Opus, hybrid)
- Dependencies (what must exist first)
- Success criteria (how do we know it's done?)
- Validation method (how do we know it's good?)

**Tier 2: Build Within 30 Days** (improves current work)
Same format as Tier 1.

**Tier 3: Build When Needed** (enables future expansion)
Same format, but include:
- Trigger condition (when does this become Tier 1?)
- Deferral risk (what's the cost of waiting?)

### Deliverable 4: Resource Allocation Recommendations

**Budget:**
- Build cost estimate (LLM processing for any Opus-heavy research)
- Maintenance cost estimate (quarterly updates)
- Total investment over next 90 days

**Time:**
- Patrick's time (strategic work only Opus can't do)
- Sonnet automation (what can be automated)
- Opus synthesis (what needs highest-quality thinking)

**Sequencing:**
- Critical path (what must be built first)
- Parallel tracks (what can be built simultaneously)
- Quick wins (what delivers value fastest)

### Deliverable 5: Success Criteria & Decision Gates

**Success criteria per deliverable:**
For each Tier 1 item, define:
- What "done" looks like (observable output)
- What "good" looks like (quality bar)
- What "used" looks like (adoption signal)

**Decision gates:**
- After Tier 1 complete: Should we proceed to Tier 2? (criteria)
- After 30 days: Is this infrastructure delivering value? (metrics)
- After 90 days: Expand, maintain, or sunset? (framework)

---

## 4. ADDITIONAL CONTEXT

### Project Constraints
- **Budget:** Conservative. Prefer $0-10 builds over $50+ builds.
- **Time:** Patrick has ~5-10 hours/month for strategic infrastructure work.
- **Urgency:** New research project starting soon (needs design methodology).
- **Scale:** Must work across 10 portfolio companies (reusability critical).

### Success Definition
- **Leading indicator:** Patrick uses new infrastructure within 7 days of build
- **Lagging indicator:** Infrastructure referenced in 3+ projects within 90 days
- **ROI threshold:** 10x return (1 hour build → saves 10 hours, or prevents $10K mistake)

### Design Principles (from ai-deployment-principles.md)
- Quality over quantity
- Proven templates over custom solutions
- High-value patterns over exhaustive documentation
- Focused retrieval over full context
- Compressed insights over verbose analysis

---

## 5. OUTPUT FORMAT

Your response should be structured exactly like this:

```markdown
# Strategic Review: Research Infrastructure Gaps & Build Plan
## 1658 Holdings Oy — [Date]

---

## EXECUTIVE SUMMARY (1 page max)

**Strategic Verdict:** [One sentence: goldmine / solid foundation / needs work / pivot]

**Top 3 Priorities:** [What to build first, with one-sentence rationale each]

**Top 3 Risks:** [What could go wrong if we don't address these gaps]

**One-Sentence Recommendation:** [The single most important action to take]

---

## GAP ANALYSIS & PRIORITY MATRIX

[Table with all 8 gaps scored and tiered]

**Tier 1 Justification:** [Why these gaps are blocking current work]

**Tier 2 Rationale:** [Why these gaps improve but don't block]

**Tier 3 Deferral:** [Why these can wait + trigger conditions]

---

## YOUTUBE KB MINING RESULTS

### Gap 1: Research Design Methodology
- Relevant videos: [...]
- Key frameworks: [...]
- Anti-patterns: [...]
- Best deep-dive: [...]
- Applied to this gap: [...]

[Repeat for all 8 gaps]

### Cross-Gap Insights
[Any patterns or connections discovered across multiple gaps]

---

## TIER 1 BUILD PLAN (Build Immediately)

### Build 1: [Name]
**File:** `_shared/[category]/[filename].md`
**Effort:** X hours
**Cost:** $X
**Builder:** [Patrick/Sonnet/Opus/Hybrid]
**Dependencies:** [None / Must have X first]

**5-Section Outline:**
1. [Section name + 1-sentence description]
2. [Section name + 1-sentence description]
3. [Section name + 1-sentence description]
4. [Section name + 1-sentence description]
5. [Section name + 1-sentence description]

**Success Criteria:** [Observable output + quality bar]
**Validation Method:** [How to verify it's good]

[Repeat for all Tier 1 items]

---

## TIER 2 BUILD PLAN (Build Within 30 Days)

[Same format as Tier 1]

---

## TIER 3 BUILD PLAN (Build When Needed)

[Same format, plus trigger conditions]

---

## RESOURCE ALLOCATION

**Budget (90 days):**
- LLM processing: $X
- Maintenance: $X
- Total: $X

**Time (90 days):**
- Patrick strategic time: X hours
- Automated (Sonnet): X hours equivalent
- Strategic synthesis (Opus): X sessions

**Critical Path:**
[Sequence diagram or bullet list showing what must be built in order]

**Quick Wins:**
[Items that deliver value in <2 hours of work]

---

## SUCCESS CRITERIA & DECISION GATES

### Tier 1 Success Criteria
[Per-deliverable observable outcomes]

### Decision Gate 1: After Tier 1 Complete
**Proceed to Tier 2 if:**
- [ ] [Criterion]
- [ ] [Criterion]
- [ ] [Criterion]

**Pivot if:**
- [ ] [Red flag]
- [ ] [Red flag]

### Decision Gate 2: 30-Day Review
**Metrics to check:**
- [Leading indicator]
- [Usage signal]
- [Value delivered]

**Expand if:** [Criteria]
**Maintain if:** [Criteria]
**Sunset if:** [Criteria]

---

## APPENDIX: KEY YOUTUBE KB VIDEOS

[List the 10 most relevant videos for research infrastructure work, with IDs and one-line summaries]

---
```

---

## 6. CRITICAL REQUIREMENTS

**Honesty:**
- If a gap isn't actually critical, say so. Don't build infrastructure for infrastructure's sake.
- If YouTube KB doesn't have relevant insights for a gap, say so. Don't force connections.
- If you're uncertain about priority/effort/cost, say so and provide ranges.

**Pragmatism:**
- Prefer $0-10 builds over $50+ builds
- Prefer 2-hour builds over 8-hour builds
- Prefer reusing existing work (synthesis) over new research
- Prefer Sonnet-buildable over Opus-required

**Strategic Thinking:**
- Consider dependencies (critical path)
- Consider reusability (1 build → 10 companies)
- Consider compounding (infrastructure that makes future work easier)
- Consider adoption (will people actually use this?)

**Citation Discipline:**
- When referencing YouTube KB, cite specific video IDs
- When proposing frameworks, cite source (KB, existing doc, or "new synthesis")
- Ensure all synthesis traces to sources (avoid training data contamination)

---

## 7. FILES YOU HAVE ACCESS TO

**You should read/reference:**
- `_shared/best-practices/knowledge-base-indexing.md`
- `_shared/best-practices/research-chunking-and-cost-optimization.md`
- `_shared/best-practices/context-window-failure-modes.md`
- `_shared/workflows/WORKFLOW-DECISION-FRAMEWORK.md`
- `MODEL-STRATEGY.md`
- `_shared/best-practices/ai-deployment-principles.md`
- `YouTubeResearch-AIFiles/knowledge-base/_index/routing-index.yaml` (196 video entries)
- `YouTubeResearch-AIFiles/knowledge-base/_index/topic-map.yaml`
- `YouTubeResearch-AIFiles/knowledge-base/_index/pattern-map.yaml`
- `YouTubeResearch-AIFiles/batch-results/youtube-kb-strategic-review.md` (Opus's previous strategic review)

**When recommending builds, check:**
- Is there an existing doc that covers this partially?
- Can we extract/synthesize from existing work?
- Or do we need new research?

---

## 8. SPECIAL INSTRUCTIONS

**YouTube KB Query Strategy:**
For each gap, you should:
1. Check topic-map for relevant tags
2. Check pattern-map for relevant strategic patterns
3. Scan routing index one_line summaries for keyword matches
4. Identify 3-5 most relevant videos per gap
5. Check if those videos are in greatest-hits-10 (high quality signal)

**Don't just list videos — explain the connection:**
- Bad: "Video 002 covers second brain systems"
- Good: "Video 002's capture-classify-surface framework directly applies to Gap 3 (Synthesis Workflow) — the 'surface' step is the missing piece in our current approach"

**Synthesis over search:**
- Don't just find relevant videos — synthesize insights across them
- Identify patterns ("3 videos mention trust mechanisms, suggesting this is critical for Gap 2")
- Find anti-patterns ("No videos cover research design directly, but 5 cover related scoping frameworks")

---

**Begin your strategic review now.**
