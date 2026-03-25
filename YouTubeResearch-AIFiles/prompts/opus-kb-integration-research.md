# Opus Research Prompt: YouTube KB Integration Design

## How to Use This Prompt
**Model:** Opus (strategic design task requiring synthesis + judgment)
**Method:** Paste this prompt into Claude Desktop or claude.ai with Opus selected.
**Attach these files** (drag into conversation before sending):
1. `knowledge-base/gold-insights/topics/knowledge-rag.md` (95 insights, ~100KB)
2. `knowledge-base/gold-insights/topics/prompting-context.md` (114 insights, ~119KB)
3. `_shared/warm-packs.md` (current warm pack system, ~7KB)

---

## Research Prompt

You are designing the integration architecture for a custom research knowledge base into an LLM-powered productivity system. This is a strategic design task — I need your architectural thinking, not execution.

### Context: What We Built

We built a YouTube research knowledge base by analyzing 172 videos from an AI strategy channel (Nate B Jones). We extracted 1,331 "gold insights" through a Sonnet batch API pass ($3). Each insight has:
- **Type:** Framework, Contrarian, Anti-Pattern, Technique, or Metric
- **Source:** Video title + author attribution
- **Evidence:** Direct quote from source material
- **Action:** Concrete implementation steps

These 1,331 insights are organized in two ways:
1. **By type** (5 flat files): gold-frameworks.md (333), gold-contrarian.md (278), gold-techniques.md (251), gold-anti-patterns.md (236), gold-metrics.md (233)
2. **By topic** (12 clustered files): Insights are cross-classified into topics based on source video tags. One insight can appear in multiple topics.

### Topic Files (12 clusters)

| Topic File | Insights | Approximate Size |
|------------|----------|-----------------|
| ai-strategy.md | 888 | ~150KB |
| agent-architecture.md | 249 | ~80KB |
| software-dev.md | 147 | ~50KB |
| leadership-org.md | 125 | ~40KB |
| prompting-context.md | 114 | ~119KB |
| career-skills.md | 97 | ~35KB |
| knowledge-rag.md | 95 | ~100KB |
| models-capabilities.md | 95 | ~35KB |
| productivity-workflows.md | 53 | ~20KB |
| security-governance.md | 44 | ~15KB |
| cost-infrastructure.md | 40 | ~15KB |
| seo-search-geo.md | 26 | ~10KB |

### Context: The System This KB Must Integrate Into

We use a **warm pack system** — project-type-specific knowledge briefings (~30-40 lines each) that get loaded at session start based on the active project. There are 7 warm packs:

1. **seo-geo** — Website SEO/GEO optimization
2. **document-import** — Document import & organization
3. **strategic-research** — Strategic research & knowledge base building
4. **m365-mining** — M365 mining & knowledge extraction
5. **governance** — Governance & compliance synthesis
6. **corporate-knowledge** — Corporate knowledge hub (multi-company)
7. **system-maintenance** — System architecture & maintenance

Each warm pack contains:
- What Works (5-7 bullets)
- What Fails (3-5 bullets)
- Key Files to Load (3-4 references)
- Model Strategy (Opus/Sonnet/Haiku guidance)
- Cost Benchmark

**The full warm-packs.md file is attached** — read it carefully to understand the current structure and references.

### Context: Session Protocol

Each session follows this lifecycle:
1. **Session start:** Load CURRENT-STATUS.md (has session counter, recent history, context pack). Context pack points to a `warm_pack: [id]` to load.
2. **During session:** Work on the active project. KB is available but NOT automatically loaded.
3. **Session end:** Update status, compile context pack for next session including `warm_pack:` pointer.

**Context budget:**
- CLAUDE.md: ~4KB (always loaded)
- MEMORY.md: ~15KB (always loaded)
- CURRENT-STATUS.md: ~25KB (always loaded)
- Warm pack (active section): ~5KB (loaded at session start)
- **Total system overhead: ~49KB (~6% of 200K context window)**
- **Hard rule: System files must never exceed 15% of context (30KB remaining budget)**

### The Problem

The YouTube KB is complete ($95 invested, 1,331 insights) but has **zero operational usage**. No session has ever loaded a topic file to inform a decision. The warm packs have vague references like `YouTube KB: "AI Broke the Web"` that point to full 35KB video files instead of the curated topic files.

The KB is shelf ware. We need to turn it into an active performance booster.

### The Constraints

1. **Knowledge/noise ratio must stay optimal** — Loading 888 ai-strategy insights into every session is worse than loading nothing
2. **Context budget is real** — 30KB remaining budget for KB content per session
3. **Zero friction** — If it requires manual effort to use the KB, it won't get used (Pre-Flight Checklist had zero activation in 7 days)
4. **Per-project relevance** — A DMC email mining session needs different insights than an SEO optimization session
5. **Maintainability** — The system must survive adding new insights without manual curation
6. **One source of truth** — Curated excerpts in warm packs will drift from topic files unless we have an update mechanism

### My Initial Proposal (Evaluate This)

I proposed a three-level integration:

| Level | What | Where | When |
|-------|------|-------|------|
| **Embedded** | Top 3-5 highest-value insights per project type | Directly in warm pack text | Every session of that type |
| **Pointer** | Topic file path + size warning | `### KB Deep Dive` section in warm pack | Load on demand when question arises |
| **Never** | Full video files, ai-strategy.md (888 insights) | Referenced in HOW-TO-USE-THIS-KB.md only | Only for targeted research |

With this mapping:

| Warm Pack | Embed (top 5) | Pointer (load on demand) |
|-----------|---------------|--------------------------|
| seo-geo | seo-search-geo (26) | prompting-context (114) |
| m365-mining | productivity-workflows (53) | agent-architecture (249) |
| strategic-research | knowledge-rag (95) | prompting-context (114) |
| governance | security-governance (44) | leadership-org (125) |
| corporate-knowledge | knowledge-rag (95) | leadership-org (125) |
| document-import | (none) | (none) |
| system-maintenance | (none) | (none) |

### Your Research Tasks

**IMPORTANT: Before answering, read the two attached KB topic files (knowledge-rag.md and prompting-context.md) thoroughly.** These contain 209 insights from our own research about knowledge management, RAG systems, context engineering, and prompting strategies. Use them to inform your design — this is a meta-task: using the KB to design how to use the KB.

Also read the attached warm-packs.md to understand the current system.

Then answer these questions:

#### 1. Architecture Evaluation
Is my three-level (Embedded / Pointer / Never) integration the right approach? What are the failure modes? What alternatives should I consider? Consider what the knowledge-rag and prompting-context insights say about optimal context loading.

#### 2. Curation Strategy
For the "Embedded" level — how should I select which 3-5 insights to embed per warm pack? Options:
- **Manual curation** (Patrick picks the best) — high quality but doesn't scale
- **Type-based** (always include 1 Framework + 1 Anti-Pattern + 1 Technique) — balanced but mechanical
- **Impact-based** (pick insights that most directly improve session outcomes) — ideal but subjective
- **Something else?**

What does the KB itself suggest about effective retrieval and context loading?

#### 3. Drift & Maintenance
How do we prevent embedded insights from going stale when new insights are added? The topic files will grow as we analyze more videos. Should embedded selections be timestamped? Auto-refreshed? Tied to the compression cycle (every 5 sessions)?

#### 4. Large File Strategy
ai-strategy.md (888 insights, ~150KB) is too big to load but contains the most broadly applicable insights. How should we make it accessible? Options:
- Create a "best of ai-strategy" curated subset (~30 insights)
- Split it into 3-4 sub-topics
- Leave it as deep-dive-only
- Something else?

#### 5. Activation Mechanism
The Pre-Flight Checklist failed because it required searching — zero activation in 7 days. How do we ensure KB insights actually get used? What does the KB say about proactive recall vs. on-demand retrieval?

#### 6. Cross-Project Intelligence
Some insights apply across ALL project types (e.g., "mine first, build after"). Should there be a "universal insights" layer that loads regardless of warm pack? How small must it be to justify always-on loading?

#### 7. Measurement
How do we know if the KB integration is actually improving outcomes? What should we track? Consider the KB's own metrics insights.

### Output Format

Write your response as a structured design document with:
1. **Executive Summary** — 5-line verdict on the integration approach
2. **Architecture Decision** — your recommended design (modify or replace my proposal)
3. **KB Insights Applied** — which specific insights from knowledge-rag.md and prompting-context.md informed your design, and how
4. **Implementation Plan** — concrete steps to build this, in priority order
5. **Risks & Mitigations** — what could go wrong and how to prevent it
6. **Maintenance Protocol** — how to keep it working as the KB grows

Do not write code or scripts. Write markdown directly. Think strategically — this is an architecture decision that will shape how 10 companies use AI knowledge across hundreds of future sessions.
