# AI Deployment Principles for Portfolio Companies
<!-- last_updated: session-28 -->

**Source:** Synthesized by Opus from ~30 YouTube video analyses (Q7-Q8, Q11 follow-ups)
**Date:** 2026-02-11
**Scope:** Universal principles applicable across all 10 portfolio companies
**Evidence base:** Named frameworks from AI strategy content (Nate B Jones, Founders Podcast, others)
**Contamination note:** ~10-15% of content may be Opus training knowledge rather than video-specific insight. Named frameworks (e.g., "Ferrari failure mode," "imperfection budget") are verified from videos. Generic advice ("start small," "iterate") may be training data. For decisions, always validate against specific source files in `knowledge-base/videos/`.

---

## Before Deploying AI Anywhere

### 1. Define Correctness First
> "You cannot choose RAG vs. agents, model selection, or architecture until you answer: what would correct even mean here?"

Before any AI project, answer: **What does "done right" look like for this specific task?** This is not a technical question — it's a business question. Skip it and you'll build something that's confidently wrong.

**Apply to:** Every AI initiative across all 10 companies.

### 2. Match Model to Task (Avoid the Ferrari Failure Mode)
Don't use the most powerful model for every task. An overpowered model over-elaborates and wastes resources — like driving a Ferrari to the grocery store.

**Rule of thumb:**
- Haiku: Routine classification, extraction, formatting
- Sonnet: Analysis, summarization, content generation
- Opus: Strategic decisions, novel synthesis, high-stakes reasoning

### 3. The 5-Hour Training Threshold
Employees receiving **5+ hours of structured AI training** become regular users. Most organizations offer 30 minutes and wonder why adoption fails.

**For 1658 Holdings:** Budget 5 hours per employee. Target the 201-level gap (applied judgment, not basics or technical deep-dives).

---

## How to Deploy AI Agents

### 4. The 80% Reliable Rule
> 100% ambition creates 60% reliability requiring 100% verification = net negative.
> 80% scope with 95% reliability requires only 20% verification = 5x more net value.

**Less capability, more value.** Constrain what agents can do. This is counterintuitive but consistently proven.

### 5. Progressive Trust Expansion
Don't give agents full access on day one. Follow the flywheel:

```
Clear articulation → Reliable outcome → Verified success →
Increased trust → Broader delegation → More context → Better articulation
```

Start with one agent in one domain ("one little guy in one habitat"). Expand only after trust is earned.

### 6. Build Proof Systems Into Prompts
Verification mechanisms go INTO prompts (source URLs, screenshots, audit trails), not added after. If you're checking work manually, the agent architecture is wrong.

### 7. The Articulation Bottleneck
> The ability to clearly describe "what done looks like" is THE competitive advantage.

Technical AI capability is commoditizing. The scarce skill is articulation — being able to tell the AI exactly what you want. This skill compounds. Train for it.

---

## Strategic Positioning

### 8. Build on Intelligence-Resistant Problems
Problems that more intelligence doesn't solve: coordination between systems/people, physical-digital bridges, workflow completion requiring approvals/stages.

**For 1658 Holdings:** Hotels, tourism, DMC operations are full of intelligence-resistant problems. These are moats because LLMs won't commoditize them.

### 9. Constraint Migration
> Each wave of technology abundance doesn't eliminate constraints — it migrates them downstream to the next bottleneck.

When AI solves knowledge work, the constraint migrates to: execution, coordination, judgment, physical logistics. Position at the next bottleneck, not the current one.

### 10. Distribution Before Product
> Invert the build sequence: Distribution → Problem → Product

Don't build AI tools and then look for users. Start with the distribution channel (existing customer relationships, existing workflows), identify the problem, then build.

---

## Management & Organization

### 11. Tiger Teams, Not Magnifying Glass
Two approaches to AI in organizations:
- **Tiger teams:** Small empowered pods (5 people) using AI for execution. **This wins.**
- **Magnifying glass:** Using AI for surveillance, dashboards, visibility. **This creates a doom loop.**

The visibility trap: More tracking → teams optimize for metrics → real work goes underground → leadership feels blind → adds more tracking.

### 12. Task-Mission Decoupling
> If AI does 30% of tasks, does that bring you 30% closer to mission or hollow out the role?

Before automating a role's tasks, check whether the tasks ARE the mission or just support it. Automating support tasks frees humans for mission. Automating mission tasks hollows the role.

### 13. Don't Automate Trust-Building Roles
Concierge, host, relationship manager — these roles build trust through human presence. Augment them with AI (better information, faster prep), never replace them.

---

## Knowledge Architecture

### 14. Heap-Not-Hierarchy
> Throw information into an unstructured heap and let AI organize/retrieve semantically, rather than maintaining human-designed folder hierarchies.

Three levels of folder depth maximum. Beyond that, rely on search. Invest in clean data and metadata, not folder trees.

### 15. Fool's Gold Detection
The most valuable human skill in the AI era is recognizing when AI output looks right but isn't. Train this skill explicitly — it's the difference between AI augmentation and AI hallucination risk.

---

## Cost & Efficiency

### 16. The 10-Minute / 25-Minute Rule
90% of value comes in the first 10 minutes. The last 10% requires 15 more minutes. For most tasks, stop at 10 minutes. Only polish when the output is customer-facing.

### 17. Simplicity Beats Infrastructure
Natural language iteration with minimal overhead outperforms elaborate scaffolding, RAG systems, and prompt engineering frameworks. Start simple. Add complexity only when simple fails.

### 18. Large Context ≠ Processed Context
Loading 1M+ tokens costs $44 but the model samples ~15%. File-by-file processing guarantees 100% coverage at lower total cost. See `context-window-failure-modes.md` for full evidence.

---

## Quick Reference: Which Principle for Which Company?

| Principle | CEO | DMC Team | Hotel Ops | All Companies |
|-----------|-----|----------|-----------|---------------|
| Define correctness first | x | x | x | x |
| Ferrari failure mode | x | | | x |
| 5-hour training threshold | | x | x | x |
| 80% reliable rule | x | x | | x |
| Progressive trust | | x | x | x |
| Intelligence-resistant problems | x | | x | |
| Constraint migration | x | | | |
| Tiger teams | x | | | x |
| Don't automate trust roles | | | x | |
| Heap-not-hierarchy | x | | | x |
| Large context warning | x | | | |

---

## Anti-Patterns: What NOT to Do

*Source: Opus Q8 extraction. 18 anti-patterns from ~10 videos. These prevent $50K mistakes.*

### Before Building

| Anti-Pattern | One-Line Rule |
|-------------|---------------|
| **Agreeing in meeting, disagreeing in production** | Force explicit correctness definitions with examples before any build. |
| **Automating what you don't understand** | Master the task manually first. Agent encodes your confusion otherwise. |
| **Building without distribution** | Identify user + pain first, get commitment, THEN build. |
| **Building middleware platforms will absorb** | Ask: "Will the platform provide this natively in 6 months?" |
| **Complex RAG as premature optimization** | Claude Projects + markdown gives 80% of RAG at 5% effort. Don't overbuild. |

### During Deployment

| Anti-Pattern | One-Line Rule |
|-------------|---------------|
| **Optimizing for confident guessing** | Explicitly define that "I don't know" is acceptable output. |
| **Single-metric Goodhart's Law** | Multi-criteria measurement: truthfulness, completeness, tone, cost, auditability. |
| **Mixing habitats too early** | One agent, one domain. Expand only after reliability proven. |
| **Feature bloat when building is free** | "No" is default. Each feature must justify inclusion. |
| **Dirty data as AI poison** | Audit for currency before making AI-searchable. Old SharePoint = garbage outputs. |
| **Light context with heavy models** | Opus/o3 Pro need substantial context. Thin input = hallucination. |

### Organizational

| Anti-Pattern | One-Line Rule |
|-------------|---------------|
| **Visibility theater** | Measure outcomes (shipped, revenue, satisfaction), not activity dashboards. |
| **Metric optimization death spiral** | Trust small teams with autonomy. Evaluate by results. |
| **Verification complacency** | Monitor verification time. If it creeps up, agent is degrading. |
| **30-minute training theater** | 5+ hours or don't bother. Below threshold creates false readiness. |
| **Speedrunning experience** | Junior staff still need slow context accumulation. AI can't replace grunt-work learning. |
| **Trying to outknow the machines** | Shift from knowledge accumulation to judgment development. |
| **Perfectionist organization paralysis** | Heap-not-hierarchy. Let AI retrieve semantically. |

---

## Cross-Cutting Strategic Insights

*Source: Opus Q11 — connections between videos that produce insights neither contains alone.*

### The Articulation Stack
Organizational correctness definition (CTO video) IS the enterprise version of individual articulation skill (agent video). Train both: employees learn to describe "what done looks like" + organization defines "what correct means."

### Internal Distribution-First
Don't build AI tools for "the organization." Find the 3-5 person tiger team that already uses the workflow daily, build for them, let it spread. Distribution before product applies internally too.

### The Imperfection Budget
Every AI system needs an explicit acceptable error rate, documented and shared. 80% agent reliability with zero burden beats 100% with overwhelming burden. 85% retrieval accuracy with zero organization beats 100% with system abandonment. Define the budget upfront.

### Clean Before You Search
Heap-not-hierarchy for **personal** knowledge (your notes, transcripts). Correctness-first for **organizational** knowledge (shared docs, official records). Don't apply the same architecture to both.

### The Specification Gap
The most AI-resistant CEO skill: precise specification under social pressure — forcing clarity when everyone is comfortable with vagueness. Making the implicit explicit, especially when uncomfortable.

### Two Phases of AI Maturity
Phase 1 (exploration): iterate fast, embrace imperfection, conversational debugging. Phase 2 (production): systematic optimization, measured quality, reliable floors. The mistake: applying Phase 2 discipline during Phase 1, or Phase 1 messiness during Phase 2.
