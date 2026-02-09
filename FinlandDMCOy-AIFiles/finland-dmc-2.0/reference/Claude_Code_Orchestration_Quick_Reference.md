# Claude Code Orchestration — Practical Reference Guide
## For 1658 Holdings prompt-file projects (non-code)

---

## Your 3 Custom Subagents

You already have these installed at `~/.claude/agents/`. Here's when and how to use each one.

### mining-organizer

**When to use**: After a mining session in claude.ai. You've pasted raw outputs into `mining-outputs/session-N/` and need them sorted into structured project files.

**How to invoke**:
```
Use the mining-organizer to process the Session 1 outputs
```

**What it does**: Reads raw mining output → identifies email types/patterns → creates organized .txt files in `project-files/` → updates ROADMAP.md checkboxes. Has project-level memory, so it remembers Finland DMC patterns across sessions.

### file-builder

**When to use**: After mining-organizer has run. You have organized data and need polished final deliverables (Custom Instructions, Tone Guides, etc.).

**How to invoke**:
```
Use the file-builder to create the final Client Communications files
```

**What it does**: Reads organized data + templates → builds publication-ready .txt files → saves to `project-files/`. After approval, you tell Claude Code to copy them to the OneDrive zone.

### company-setup

**When to use**: When onboarding a new portfolio company (Company 2, 3, etc.).

**How to invoke**:
```
Use the company-setup agent to create the workspace for [CompanyName]
```

**What it does**: Reads Finland DMC structure as template → creates matching folder tree, CLAUDE.md, ROADMAP.md, MINING_PROTOCOL.md for the new company. Has user-level memory, so it learns the pattern across all companies.

---

## Chaining Subagents (The Orchestrator Pattern)

You can chain subagents in one conversation. This is your main orchestration tool right now.

**Example — full build after a mining session:**
```
1. Use the mining-organizer to process Session 1 outputs
2. Then use the file-builder to create the final Client Communications files
3. Copy the finals to the OneDrive knowledge folder
4. Mark the Session 1 build tasks done in ROADMAP.md
```

Claude Code runs them sequentially — each subagent finishes before the next starts. The main session sees a summary from each one and coordinates the flow.

**Example — parallel research across companies:**
```
Use Explore subagents in parallel to check the ROADMAP.md status
in every company folder and give me a combined progress report
```

This spawns fast read-only agents that scan multiple folders simultaneously.

---

## Subagent Memory — How It Builds Over Time

Your mining-organizer and file-builder both have `memory: project`. This means:

- First use: The agent has no memory. It learns your patterns from scratch.
- After use: Tell it "Save what you learned to your memory." It writes to `.claude/agent-memory/mining-organizer/MEMORY.md`.
- Next session: It loads that memory automatically. It already knows Finland DMC's tone, email types, pricing patterns.
- Over time: The memory file accumulates institutional knowledge — like training a new employee who never forgets.

**Practical tip**: At the end of any subagent task, say:
```
Save the key patterns you noticed to your memory for next time
```

The company-setup agent has `memory: user` (global), so it remembers lessons from ALL companies, not just one.

---

## Agent Teams — When You'll Need Them (Not Yet)

Agent Teams are for when you're doing parallel work across multiple companies simultaneously. You don't need them for Finland DMC alone.

**When to graduate to Agent Teams:**
- Building 3+ companies at the same time
- Running parallel mining-session processing across companies
- Wanting one "lead" session to coordinate multiple "worker" sessions

**How it would look (future example):**
```
Create an agent team to build all 4 Finland DMC project files simultaneously.
Spawn 4 teammates — one per project (Router, Client Comms, Proposals, Pricing).
Each reads their mining outputs and builds their final files independently.
Use delegate mode.
```

**Key rules for Agent Teams:**
- Each teammate must own different files — two agents editing the same file = overwrites
- The lead coordinates only (in delegate mode) — it doesn't build files itself
- Teammates can message each other but don't share context windows
- Enable with: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` in settings.json
- Currently experimental — start with subagents, upgrade when the workload justifies it

---

## Quick Reference: Which Tool for Which Job

| Situation | Use | Why |
|-----------|-----|-----|
| Process one mining session | mining-organizer subagent | Focused, has memory |
| Build final deliverables | file-builder subagent | Polished output, template-aware |
| Set up new company | company-setup subagent | Replicates the pattern |
| Quick file search across folders | Explore subagent (built-in) | Fast, read-only, cheap |
| Chain multiple build steps | Subagents in sequence | Main session orchestrates |
| Scan all companies at once | Multiple Explore subagents in parallel | One summary back |
| Build 3+ companies simultaneously | Agent Teams (future) | Parallel workers, shared task list |
| Routine single-company work | No subagents — just Claude Code directly | Simplest option |

---

## What to Say vs. What Happens

| You say | Claude Code does |
|---------|-----------------|
| "Use the mining-organizer" | Spawns subagent → reads mining-outputs/ → organizes → returns summary |
| "Run mining-organizer and file-builder in sequence" | Spawns #1, waits for result, spawns #2 |
| "Check all company ROADMAPs in parallel" | Spawns multiple Explore agents simultaneously |
| "Build [project]" | Your CLAUDE.md command → assembles files → offers to copy to OneDrive |
| "Save what you learned to memory" | Subagent writes patterns to MEMORY.md for next time |
| "Create an agent team" | Spawns lead + teammates with shared task list (experimental) |
