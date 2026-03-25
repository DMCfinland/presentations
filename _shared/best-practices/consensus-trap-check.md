# Consensus Trap Check — "Perfectly Wrong" Execution Prevention

**Source:** Cursor Swarm Master-Skills v2.4 via S116, Grok-validated
**Type:** Quality gate pattern
**Confidence:** 0.7

---

## The Pattern

Before spawning any agent, asking any model, or finalizing any criteria — run this self-check:

> **"Could all agents execute this perfectly and still produce the wrong output?"**

If YES → rewrite the goal or criteria before proceeding. The trap is real when instructions are technically correct but missing the actual intent.

---

## Why It Matters

Multi-agent systems amplify initial direction errors. If the Initializer (Planner/CoS) gives a subtly wrong instruction:
- All 15 agents execute it correctly → all 15 outputs are wrong
- Judge approves because output matches criteria → criteria were the bug
- Costs 10× more to fix than catching at intake

Single-agent (Claude Code) same risk, lower amplification. Still dangerous in Tier 3 / high-stakes tasks.

---

## Common Trigger Cases

| Symptom | What It Looks Like | Fix |
|---------|-------------------|-----|
| **Metric gaming** | "Improve session handoff quality" → Claude adds more text to hit word count | Rewrite: "Reduce human interventions next session by X" |
| **Format over substance** | "Write a structured spec" → Claude writes headings + bullets with no real decisions | Rewrite: "Spec must enable a developer to build X without asking follow-up questions" |
| **Tool confusion** | "Research transcript pipeline options" → Claude researches general options, not our constraint set | Add: "Constraint: must work with existing n8n + Supabase stack" |
| **Audience mismatch** | "Write for Frendy" → Claude writes technical docs when Frendy needs step-by-step UI instructions | Add: "Audience: IT admin who has never used PowerShell" |

---

## Where to Apply This Check

**Mandatory:**
- PWJ Step 1 item 8 (now in SKILL.md)
- Before any multi-model research task
- Before spawning Cursor Swarm CoS

**Recommended:**
- Before sending any prompt to external AI (Grok, Gemini) — check: "Am I asking for what I actually need?"
- Opus Review: audit Tier A rules in CLAUDE.md — are any written in a way that could be executed correctly but wrongly?

---

## The Self-Critique Formula

```
CONSENSUS TRAP CHECK:
- My goal/criteria as written: [X]
- If executed perfectly: the output would be [Y]
- Is Y actually what I need? [YES / NO + rewrite]
- What's the gap between Y and what I actually need? [describe]
```

Run this silently before confirming any intake. 30 seconds. Prevents 2-3 full Worker rounds.

---

## CLAUDE.md Audit Application

Every Opus Review: scan Tier A rules for Consensus Trap patterns.
Ask for each rule: "Could following this rule perfectly lead to wrong behavior in an edge case?"
If yes: add an exception clause or sharpen the condition.

Example: "Mine first, build after" — edge case: mining session returned low-quality data.
Should this rule have: "...unless mining quality score <0.6, in which case flag and ask"?
