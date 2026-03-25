# Q8: Anti-Patterns and Warnings

**Source:** Opus claude.ai Project (195 video analyses, 1.7M tokens loaded via RAG)
**Date:** 2026-02-11
**Cost context:** Cheap follow-up (files deleted from Project, conversation history retained)
**Yield:** 18 anti-patterns from ~10 videos

---

## From the CTO / Correctness Video

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| **Agreeing in the meeting, disagreeing in production** | Organizations use vagueness to reach false consensus. Everyone "agrees" on what the AI should do, then discovers in production they meant different things. | Force explicit correctness definitions with examples before any build begins. |
| **Optimizing for confident guessing over honest uncertainty** | AI trained on human feedback learns that confident answers get rewarded, even when wrong. Systems that don't explicitly reward "I don't know" will hallucinate confidently. | Explicitly define that uncertainty is an acceptable and desired output. |
| **Single-metric Goodhart's Law** | Measuring AI quality on one metric (accuracy, speed, user satisfaction) causes the system to game that metric at the expense of everything else. | Use multi-criteria measurement (truthfulness, completeness, tone, cost, refusal behavior, auditability). |

## From the Tiger Teams Video

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| **Visibility theater** | Using AI to generate dashboards, status reports, and monitoring systems that create the illusion of control without improving outcomes. Teams optimize for appearing productive rather than being productive. | Measure outcomes (shipped products, revenue, customer satisfaction), not activity. |
| **Metric optimization death spiral** | More metrics become trackable → teams optimize for metrics → real work goes underground → leadership adds more tracking → cycle repeats. | Trust small teams with autonomy, evaluate by results. |

## From the Agent Delegation Video

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| **Automating what you don't understand** | Delegating to AI a process you haven't done manually. The agent encodes your confusion rather than solving it. | Master the task manually first, then automate. You need to understand the process to articulate "done." |
| **Verification complacency** | Even proven agent workflows drift toward hallucination if verification becomes routine rubber-stamping. | Monitor verification time as an early warning metric. If it creeps up, the agent is becoming less reliable. |
| **Mixing habitats too early** | Asking one AI setup to handle research AND creation AND communication simultaneously. Creates overwhelming complexity before you've built trust in any single capability. | One habitat per agent, specialize, expand only after reliability proven. |

## From the Side Hustle / Micro-Niche Video

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| **Building without distribution** | Creating a product/tool then figuring out who wants it. Wastes time on solutions nobody uses. | Identify the user and their pain first, get their commitment, then build the minimal solution. |
| **Feature bloat when building is free** | AI removes the cost constraint on building, so the new constraint is discipline. AI will suggest more features endlessly. | Say "no" as default. Each feature must justify inclusion. "Know when to stop building the product." |

## From the Note-Taking / Second Brain Video

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| **Perfectionist organization paralysis** | Spending more time organizing notes than creating them. The organizational overhead exceeds the retrieval benefit, leading to system abandonment. | Heap-not-hierarchy. Throw information in unstructured, let AI retrieve semantically. |
| **Dirty data as AI poison** | Six-year-old wikis, outdated SharePoint sites, stale documentation. AI confidently retrieves and presents outdated information as current. | Clean data discipline — audit for currency before making AI-searchable. The Copilot critique centers on this: dirty SharePoint data + no quality framework = garbage outputs. |

## From the Platform Consolidation Video

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| **Building middleware that platforms will absorb** | Investing engineering effort in integration layers, agent orchestration, or prompt management tools that Claude Skills, GPT Actions, or native platform capabilities will commoditize within 6 months. | Before building, ask "will the platform provide this natively soon?" If yes, use the simpler approach. |
| **Complex RAG as premature optimization** | Building vector databases and retrieval systems before exhausting simple approaches. Claude Projects with markdown files give 80% of RAG value at 5% of effort. | Don't build infrastructure until you've hit retrieval limits with simpler approaches. |

## From the Post-Knowledge Economy Video

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| **Trying to outknow the machines** | Responding to AI capability by accumulating more knowledge (reading more, attending more, researching more). Knowledge is hyperinflating — accumulating more yields diminishing returns. | Shift from knowledge accumulation to judgment development, taste, and learning velocity. |

## From the o3 Pro Video

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| **Light context with heavy models** | Feeding powerful reasoning models (o3 Pro, Opus) thin context and expecting good strategic output. These models are "hungry for context" and will over-elaborate or hallucinate when context is insufficient. | Provide substantial context (documents, data, background) or use a lighter model. |

## From the Talent Development Video

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| **30-minute training theater** | Offering brief AI training sessions that create awareness without capability. Below the 5-hour documented threshold, training creates the illusion of organizational AI readiness without actual behavior change. | Invest 5+ hours per employee or don't bother. |
| **Speedrunning experience** | Using AI to skip the "grunt work" that builds domain judgment and institutional context. Junior employees reach seniority markers without the tacit knowledge that makes those roles valuable. | Accept that context accumulation still takes slow accumulation. |
