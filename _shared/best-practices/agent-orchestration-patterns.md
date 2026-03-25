# Agent Orchestration Patterns
**Version:** 1.0
**Source:** Session 38 research (2026-02-21) — Agent Teams vs Task Subagents comparison
**Validated:** Finland DMC Second Brain project

---

## The Three Tools and When to Use Each

| Tool | What it is | Use when |
|------|-----------|---------|
| **Task subagents** | Sonnet subprocess spawned by main thread. Reports back to caller. No cross-agent talk. | Parallel read/analyze tasks on same data. Fast, cheap, stable. |
| **Agent Teams** | Experimental. Full independent Claude Code sessions with shared mailbox. Can message each other directly. | Agents need to debate/challenge findings across multiple data sources. Context limits force specialization. |
| **n8n + Claude API** | Workflow automation. Claude API call as one node in a larger automated flow. | Recurring pipelines triggered by events (new email, new proposal, new itinerary). Production-scale. |

---

## Decision Rules

**Use Task subagents when:**
- Parallel read/analyze tasks on the same data (e.g., 4 analysts reading one proposals extract)
- Agents don't need to talk to each other — each produces independent output
- Task is single-session, ad-hoc
- Need stability (subagents are production-ready, Agent Teams is experimental)

**Use Agent Teams when:**
- Each agent specializes in ONE data source (proposals / emails / TT itineraries / pricing)
- Context limits prevent one agent from holding all data simultaneously
- Agents need to challenge each other's findings ("Client Profiler says luxury, Revenue Mapper says mid-market — reconcile")
- You have 3+ distinct data sources that need cross-referencing
- ⚠️ ONLY after all data sources are loaded — premature before you have the full dataset

**Use n8n + Claude API when:**
- Trigger-based: "new email arrives → process it"
- Recurring: daily/weekly batch updates to Second Brain
- Production scale: thousands of items, not dozens
- Needs to run without a human in the loop

---

## Critical Technical Facts

### MCP tools in subagents
**MCP tools are NOT available in background subagents.**
The M365 connector (Graph API, SharePoint, Teams, Calendar) is MCP.
→ Any subagent doing M365 work MUST run foreground (blocking, not background).
→ In Claude Code: main thread does M365 searches, subagents compile/analyze the results.
→ In production: use n8n with the M365 connector directly.

### Agent Teams — known limitations (Feb 2026)
- Experimental — disabled by default. Enable: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings.json
- Session resumption is broken — lead can't resume in-process teammates
- Cost: significantly higher than subagents (each teammate = full Claude instance)
- Nesting (agents spawning agents) not supported
- Each teammate inherits MCP tools from the lead ✓

### Custom subagent files
Define reusable specialists in `.claude/agents/` with `.md` files:
```yaml
---
name: client-profiler
description: Analyzes company type, country, and market segment from DMC proposal data
tools: Read, Grep, Glob
model: sonnet
---
System prompt here...
```
Benefit: reusable across sessions, consistent behavior, no need to re-describe the role each time.

### Memory persistence for subagents
Add `memory: project` to a subagent's config to let it accumulate knowledge across sessions.
Use for Second Brain agents that need to remember patterns from previous enrichment runs.

---

## Finland DMC — Orchestration Roadmap

### NOW: Task subagents (4-angle proposals analysis)
4 parallel analysts read `proposals-clean-extract.md` independently:
- Client Profiler → client profiles for Second Brain
- Relationship Analyst → staff ownership + account health
- Revenue Mapper → concentration risk + top clients
- Second Brain Gap Analyst → what's missing from current Second Brain

Defined as custom agents in `FinlandDMCOy-AIFiles/.claude/agents/`.

### SOON: n8n pipeline (email automation)
New email arrives → M365 webhook → n8n → Claude API (Batch) → extract signals → write Second Brain update.
Does NOT run in Claude Code. Runs as automated workflow.

### LATER: Agent Teams (cross-source synthesis)
**Trigger:** When ALL three data sources are loaded:
1. Proposals pipeline (done ✓)
2. Mass email mining (pending — Azure Graph API access)
3. TT itinerary archive (pending — TT Pro API)

At that point, one agent can't hold proposals + emails + TT data + pricing simultaneously.
Agent Teams allows each specialist to own one source and communicate findings:
- Agent A: "Kontiki sent 52 proposals, 87% win rate, all FIT"
- Agent B: "Kontiki emails show seasonal Jan-Mar peak, always asks same 3 questions"
- Agent C: "Kontiki TT itineraries use 4 recurring components: Nordic Walk, Sauna, Rowboat, Dinner"
- Coordinator: synthesizes → Golden Prompt + pre-filled component recommendation

This is where cross-agent communication adds real value that subagents can't provide.

---

## CONTEXT ISOLATION — Why Fresh Context is a Feature, Not a Bug

Subagents do NOT inherit the conversation history or main thread context. This is deliberate.

**What a subagent gets:**
- ✅ Exactly what you write in the Task prompt parameter
- ✅ Access to the same filesystem tools
- ❌ Conversation history (invisible to it)
- ❌ Session knowledge (who Patrick is, what session number, what project)

**Why this is good:**
1. **Predictable cost** — subagent input tokens = only what you wrote in the prompt. No surprise context carry-over.
2. **No context contamination** — the subagent can't be confused by earlier conversation tangents. It has exactly the facts it needs.
3. **Reusable** — the same subagent prompt works regardless of which session it's invoked from.
4. **Forces clarity** — if you can't write a self-contained prompt, the task isn't well-defined yet.

**Quality implication:** Detailed prompts are not overhead — they are the entire knowledge transfer mechanism. The prompt IS the briefing. Include: file paths, column meanings, known benchmarks, staff codes, and expected output format. A vague prompt = a vague result.

**Pattern:** Main thread = strategic context holder. Subagent = specialist with a clean briefing.

---

## PRE-DISTILLATION PROTOCOL — Before spawning subagents on large data

**Validated session 38:** 4-subagent DMC proposals analysis.

The orchestrator (main thread) should NEVER pass raw data files to subagents when a pre-distilled summary already exists. Instead:

```
Step 1 — Main thread extracts/analyzes raw data → writes ANALYSIS.md
Step 2 — Main thread identifies minimal input per agent angle (2-5K tokens each)
Step 3 — Spawn subagents with: ANALYSIS.md + targeted slice only
Step 4 — Each agent writes its output to a specific output path
Step 5 — Main thread synthesises outputs
```

**Token comparison (DMC proposals session 38):**
- Raw approach: 4 agents × 59KB extract = 60K input tokens
- Pre-distilled approach: 4 agents × ANALYSIS.md (2K) = 8K input tokens
- **Saving: ~87% fewer input tokens**

**When pre-distillation isn't enough (→ use Agent Teams instead):**
- Each data source is so large that summarising it loses critical nuance
- Agents need to challenge each other's findings (not just produce independent outputs)
- 3+ distinct sources need full-context reconciliation simultaneously

**The Client Profiler exception (session 38):** The profiler still needed to grep the raw 59KB extract per company to compute individual totals. This is acceptable — the profiler's job was to BUILD profiles, not just read the summary. For future runs: pre-generate a deduplicated company index (company|revenue|wins|proposals → ~5KB) before spawning it.

---

*Source: Research session 38. Patrick's correction (source: patrick): "orchestrated teams ≠ subagents — they are different tools." Agent Teams is for cross-source debate; subagents are for parallel independent analysis.*
