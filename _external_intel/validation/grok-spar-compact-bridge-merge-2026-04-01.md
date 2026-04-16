# Grok Spar: Compact → Session Bridge Merge
**Date:** 2026-04-01 | **Source:** Session 139/141 analysis
**Purpose:** Validate or destroy the idea of replacing /compact with session bridge triggers

---

## PASTE THIS TO GROK HEAVY (4-agent council mode):

```
CONTEXT:
I run Claude Code (AI coding agent) as a solo CEO managing 10 companies. My sessions run 30-90 minutes with 50-100+ tool calls. Claude Code has a 200K token context window with a pricing cliff (2x cost above 200K).

CURRENT STATE (two separate systems):
1. **Compact hook:** A JavaScript hook fires at 40 tool calls, suggesting /compact (which summarizes and truncates conversation history). This is LOSSY — Claude decides what survives, reasoning chains get flattened, nuance disappears.
2. **Session Bridge Protocol:** At 140K tokens (manual check), I trigger a structured handoff: harvest patterns → cognitive snapshot → build a bridge prompt → start new session with that prompt. The bridge is CURATED — I choose what survives. The bridge IS the next session's startup prompt.

PROPOSED MERGE:
Replace the compact hook entirely. Instead:
- Hook tracks context usage (proxy: tool call count, since hooks don't get token count directly)
- At ~80% context → trigger session bridge building (not compacting)
- Bridge prompt captures: decisions made, failed approaches, current state, next steps, warm context
- New session starts with the bridge prompt
- No lossy compression ever. All context transitions are curated.

ATTACK THIS IDEA ON THESE DIMENSIONS:

1. **Context cliff edge case:** What happens if Claude hits 100% context BEFORE the bridge is built? Building a bridge prompt itself costs tokens. Is there a deadlock where you need context to build the prompt but have no context left?

2. **Tool-call count as proxy for context %:** Tool calls vary wildly in token cost (a Read of a 2000-line file vs a 5-line Bash command). Is tool-call count a reliable enough proxy, or will sessions blow past the threshold silently?

3. **Cognitive load on the CEO:** Manual bridge building requires Patrick to be present and attentive. What happens during overnight autonomous runs (research-loop cron jobs) where no human is available to curate the bridge?

4. **Mid-session value:** Some sessions have 3 distinct phases (research → plan → execute). Compacting between phases IS valuable — it drops the research noise before execution. Does the "never compact" rule hurt phase transitions?

5. **Comparison to progressive disclosure:** claude-mem (44K stars) uses progressive disclosure — AI-compressed summaries that expand on demand. Is this a third option that's better than both compact and bridge?

6. **The 80% threshold:** Why 80% and not 70% or 90%? What's the evidence that 80% gives enough room to build a bridge prompt? How many tokens does bridge building typically consume?

7. **Hybrid approach:** Is the right answer not "compact OR bridge" but "compact for autonomous runs, bridge for attended sessions"? Or even "micro-compact (drop tool results only) + bridge at threshold"?

OUTPUT FORMAT:
For each dimension: ATTACK (what's wrong) → DEFEND (steelman the proposal) → VERDICT (kill, modify, or approve).
Then: one overall recommendation with specific implementation changes.
```

---

## Expected reversals to watch for:
- "Tool-call count is unreliable" → may need statusline integration or a different proxy
- "Autonomous runs need compact" → may need a hybrid approach
- "80% is wrong" → may need empirical calibration
- "Progressive disclosure is better than both" → may need to study claude-mem deeper
