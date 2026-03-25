# Research Prompt — Claude Agent Teams
**Use in:** A new claude.ai / Claude Code window (Opus preferred)
**Purpose:** Understand Agent Teams for Finland DMC proposals + Second Brain mining
**URL to fetch:** https://code.claude.com/docs/en/agent-teams

---

## Context (paste this to the research session)

I am building a Finland DMC AI Assistant. We have:
- A proposals pipeline Excel (393 proposals, 44% win rate, top clients, revenue data)
- Email mining from M365 (Sessions 1-6: client emails, proposals, TT workflow)
- A Second Brain system being built (client profiles, win rates, staff ownership, pricing)
- A designed Email Drafter (Claude Code + n8n, 3-layer architecture)

We currently use Claude Code with **Task tool subagents** (Sonnet subagents that handle file I/O, analysis, compilation in parallel). This is what Patrick calls "subagents."

Patrick is asking about **Agent Teams** (https://code.claude.com/docs/en/agent-teams) as a DIFFERENT orchestration model. We need to understand:

---

## Research Questions

### 1. What is Agent Teams exactly?
- How does it differ from spawning Task subagents in Claude Code?
- Is it a different product, a different API, or a feature within Claude Code?
- What does the orchestration model look like? (coordinator → specialized agents?)

### 2. Capabilities vs Task subagents
| Capability | Task subagents (what we have) | Agent Teams |
|------------|-------------------------------|-------------|
| Parallel execution | Yes | ? |
| Persistent memory between agents | No | ? |
| Specialized roles | Basic | ? |
| Tool sharing | Limited (MCP bug) | ? |
| Cross-agent communication | No | ? |
| Cost | Sonnet × N calls | ? |

### 3. Is Agent Teams relevant for our use cases?

**Use case A: DMC proposals Excel — multi-angle analysis**
We have 393 proposals and want to analyze from 4 angles simultaneously:
- Client Profiler (company type, country, segment)
- Relationship Analyst (staff ownership, account health)
- Revenue Mapper (top clients, deal sizes, segments)
- Second Brain Gap Analyst (cross-reference vs email mining data)

Current approach: 4 parallel Task subagents reading the same clean extract.
Question: Would Agent Teams give us anything the Task subagent approach doesn't?

**Use case B: Email mining pipeline**
Mass email mining from M365 (Graph API). Processing thousands of emails:
- Extract client signals
- Build Second Brain profiles
- Detect trip type patterns
- Route to correct staff

**Use case C: Second Brain maintenance**
As new data comes in (new emails, new proposals, new TT itineraries),
agents that update existing profiles vs create new ones.

### 4. Practical questions
- Can Agent Teams persist state across sessions or is it still single-context?
- Does it work with MCP tools (Microsoft Graph API connector)?
- What's the cost model compared to individual Sonnet Task calls?
- Is there a way to have a "coordinator" agent that routes work to specialists?
- Can it be used outside Claude Code (e.g., in n8n workflows)?

### 5. Fetch the docs
Please fetch https://code.claude.com/docs/en/agent-teams and summarize:
- What it is (2-3 sentences)
- Key capabilities
- How to set it up
- Example use case from the docs
- Limitations and gotchas

Then give a recommendation: for our Finland DMC Second Brain project, should we use Agent Teams, Task subagents, or a hybrid? What's the right tool for which job?

---

## Output format requested

1. **What Agent Teams IS** — plain explanation (not marketing)
2. **Comparison table** — Agent Teams vs Task subagents vs n8n orchestration
3. **Recommendation** — which to use for each of our 3 use cases above
4. **Implementation sketch** — if Agent Teams fits, what would a 4-agent DMC analysis setup look like in practice?

---

*Prepared by Claude Sonnet in Claude Code, session 38, 2026-02-21*
*To be researched in a separate window with full URL access*
