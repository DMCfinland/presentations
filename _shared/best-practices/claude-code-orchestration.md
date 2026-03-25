# Claude Code Orchestration — Best Practices Guide
<!-- last_updated: session-28 -->
**For 1658 Holdings prompt-file projects (non-code)**

---

## Overview

Claude Code is a CLI tool that can orchestrate AI workflows across multiple companies, projects, and file types. For 1658 Holdings, we use it as the **organization layer** — building files, tracking progress, and managing multi-company operations. Mining happens in claude.ai with M365 connector; building happens here.

**Key principle**: Claude Code manages the workshop (file building, organization, Git). Claude.ai handles the deep mining (M365 search, knowledge extraction).

---

## Core Concepts

### 1. Main Session vs. Subagents

- **Main session**: Your interactive conversation with Claude Code. This is where you coordinate, make decisions, and run commands.
- **Subagents**: Specialized mini-sessions spawned by the main session to handle specific tasks (mining organization, file building, company setup, etc.).

**Rule of thumb**: Use subagents for focused, repeatable tasks with clear inputs/outputs. Use main session for coordination and decision-making.

### 2. Custom Subagents (1658 Holdings specific)

We've created 3 custom subagents for our workflow:

#### mining-organizer
- **Purpose**: Transform raw mining outputs from claude.ai into organized project files
- **Memory**: `project` level — remembers patterns for one company (e.g., Finland DMC tone, email types)
- **When to use**: After every mining session, when you've pasted raw outputs into `mining-outputs/session-N/`
- **What it does**: Reads raw mining → identifies patterns → creates organized .txt files in `project-files/` → updates ROADMAP.md checkboxes

**Example invocation**:
```
Use the mining-organizer to process the Session 1 outputs
```

#### file-builder
- **Purpose**: Build polished, final deliverables from organized mining data and templates
- **Memory**: `project` level — remembers company-specific patterns and standards
- **When to use**: After mining-organizer has run; you need final Custom Instructions, Tone Guides, etc.
- **What it does**: Reads organized data + templates → builds publication-ready files → saves to `project-files/`

**Example invocation**:
```
Use the file-builder to create the final Client Communications files
```

#### company-setup
- **Purpose**: Create new company folder structure when onboarding Company 2, 3, etc.
- **Memory**: `user` level (global) — learns from ALL companies, not just one
- **When to use**: When starting a new portfolio company
- **What it does**: Reads Finland DMC as template → creates folder tree + CLAUDE.md + ROADMAP.md + MINING_PROTOCOL.md for new company

**Example invocation**:
```
Use the company-setup agent to create the workspace for [CompanyName]
```

### 3. Built-in Subagents (Claude Code native)

#### Explore
- **Purpose**: Fast, read-only codebase exploration
- **When to use**: Quick file searches, status checks across folders, answering questions about file contents
- **What it does**: Spawns fast, cheap agent to scan files and return summary

**Example invocation**:
```
Use Explore to check the ROADMAP.md status in every company folder
```

#### Plan
- **Purpose**: Design implementation strategy before writing code
- **When to use**: NOT RELEVANT for our prompt-file projects (we're not writing code)
- **Skip this**: We don't need Plan mode for building .txt and .md files

---

## Orchestration Patterns

### Pattern 1: Sequential Subagent Chain (Most Common)

Run multiple subagents in sequence, where each one finishes before the next starts. The main session coordinates.

**Example — full build after a mining session**:
```
1. Use the mining-organizer to process Session 1 outputs
2. Then use the file-builder to create the final Client Communications files
3. Copy the finals to the OneDrive knowledge folder
4. Mark the Session 1 build tasks done in ROADMAP.md
```

Claude Code will:
1. Spawn mining-organizer → wait for completion → show you summary
2. Spawn file-builder → wait for completion → show you summary
3. Run copy commands in main session
4. Update ROADMAP.md in main session

**When to use**: Standard workflow after every mining session. Most reliable pattern.

### Pattern 2: Parallel Subagent Spawning

Spawn multiple subagents simultaneously for independent read-only tasks.

**Example — multi-company status check**:
```
Use Explore subagents in parallel to check the ROADMAP.md status
in every company folder and give me a combined progress report
```

Claude Code will:
1. Spawn 10 Explore subagents simultaneously (one per company)
2. Each reads its company's ROADMAP.md
3. All return results at roughly the same time
4. Main session combines into single summary

**When to use**:
- Scanning multiple companies for status
- Parallel research across different folders
- Gathering data from independent sources

**Limitations**:
- Only use for READ-ONLY tasks
- Don't use for file writes (risk of conflicts)

### Pattern 3: Direct Main Session Work (No Subagents)

For simple, one-off tasks, skip subagents entirely.

**Example — quick ROADMAP update**:
```
Mark the "Install VS Code" task done in ROADMAP.md
```

Claude Code will:
1. Use Edit tool directly in main session
2. Update checkbox and add completion note
3. No subagent needed

**When to use**:
- Single file reads/edits
- Command execution (git, ls, etc.)
- Quick status checks (1-2 files)
- Simple questions

**Rule of thumb**: If the task takes <3 tool calls, do it in main session.

---

## Subagent Memory System

Your custom subagents (mining-organizer, file-builder, company-setup) have MEMORY that persists across sessions.

### How Memory Works

1. **First use**: Subagent has no memory. It learns patterns from scratch during the task.
2. **Save memory**: At task end, tell it: "Save what you learned to your memory for next time"
3. **Storage**: Memory saved to `~/.claude/agent-memory/[agent-name]/MEMORY.md`
4. **Next use**: Subagent automatically loads memory at start. It already knows company patterns.
5. **Over time**: Memory accumulates institutional knowledge like training an employee who never forgets.

### Memory Levels

- **Project memory** (mining-organizer, file-builder): Remembers one company's patterns
  - Finland DMC's tone, email types, pricing structure
  - Separate memory file per company
  - Use: Company-specific knowledge

- **User memory** (company-setup): Remembers patterns across ALL companies
  - Common folder structures, best practices, lessons learned
  - Single global memory file
  - Use: Cross-company institutional knowledge

### Best Practices for Memory

1. **Always save memory after new learnings**: Don't waste knowledge from a session
2. **Review memory periodically**: Read `~/.claude/agent-memory/[agent-name]/MEMORY.md` to see what was saved
3. **Refine memory**: If subagent saved something wrong, edit MEMORY.md directly
4. **Clear memory when needed**: Delete MEMORY.md to start fresh if patterns change

**Example memory prompt**:
```
Save the key patterns you noticed to your memory for next time
```

---

## Agent Teams (Advanced — Not Yet Needed)

Agent Teams are for parallel work across multiple companies simultaneously. **Skip this until you're building 3+ companies at once.**

### When You'll Need Agent Teams

- Building 3+ companies at the same time
- Running parallel mining-session processing across companies
- Wanting one "lead" session to coordinate multiple "worker" sessions

### How It Works

**Example (future)**:
```
Create an agent team to build all 4 Finland DMC project files simultaneously.
Spawn 4 teammates — one per project (Router, Client Comms, Proposals, Pricing).
Each reads their mining outputs and builds their final files independently.
Use delegate mode.
```

**Key rules**:
- Each teammate must own different files — two agents editing same file = overwrites
- Lead coordinates only (delegate mode) — doesn't build files itself
- Teammates can message each other but don't share context windows
- Enable with: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` in settings.json

**Current status**: Experimental feature. Start with sequential subagents, upgrade when workload justifies.

---

## Decision Tree: Which Tool for Which Job

| Situation | Use | Why |
|-----------|-----|-----|
| Process one mining session | mining-organizer subagent | Focused, has memory |
| Build final deliverables | file-builder subagent | Polished output, template-aware |
| Set up new company | company-setup subagent | Replicates pattern |
| Quick file search | Explore subagent | Fast, read-only, cheap |
| Chain multiple build steps | Sequential subagents | Main session orchestrates |
| Scan all companies at once | Multiple Explore in parallel | One summary back |
| Build 3+ companies simultaneously | Agent Teams (future) | Parallel workers |
| Routine single-company work | No subagents — main session | Simplest option |
| Update ROADMAP checkbox | No subagents — main session | Single Edit call |
| Check status of one project | No subagents — Read tool | One file, one call |

---

## Common Workflows

### Workflow 1: After Mining Session (Standard)

**Goal**: Transform raw mining from claude.ai into organized files, then build finals.

**Steps**:
1. Paste raw mining outputs into `mining-outputs/session-N/`
2. Tell Claude Code:
   ```
   Use the mining-organizer to process Session 1 outputs
   Then use the file-builder to create the final Client Communications files
   ```
3. Review generated files in `project-files/`
4. Approve and copy to OneDrive Zone B
5. Update ROADMAP.md checkboxes

**Expected result**: Raw notes → organized data → polished deliverables → deployed to SharePoint.

### Workflow 2: Company Onboarding (New Company)

**Goal**: Set up workspace for Company 2, 3, etc.

**Steps**:
1. Tell Claude Code:
   ```
   Use the company-setup agent to create the workspace for [CompanyName]
   ```
2. Review generated CLAUDE.md, ROADMAP.md, folder structure
3. Customize CLAUDE.md with company profile
4. Create OneDrive Zone B folder for company
5. Begin Phase 0 M365 setup

**Expected result**: New company folder ready, matching Finland DMC pattern.

### Workflow 3: Multi-Company Status Check

**Goal**: Get progress report across all 10 companies.

**Steps**:
1. Tell Claude Code:
   ```
   Use Explore subagents in parallel to check ROADMAP.md in all company folders
   Give me a table showing current phase and blockers for each
   ```
2. Review combined report
3. Decide which company needs attention

**Expected result**: One summary table, all companies scanned in parallel.

### Workflow 4: Build Shared Resources (Templates, Prompts, Best Practices)

**Goal**: Create reusable files in `_shared/` folder for all companies.

**Steps**:
1. Identify pattern from Finland DMC (e.g., MINING_PROTOCOL.md works well)
2. Tell Claude Code:
   ```
   Read FinlandDMCOy-AIFiles/finland-dmc-2.0/MINING_PROTOCOL.md
   Adapt it into a universal template for _shared/templates/
   ```
3. Review template
4. Save to `_shared/templates/MINING_PROTOCOL.md`
5. Update `_shared/ROADMAP.md` checkbox

**Expected result**: Reusable template available for Company 2, 3, etc.

---

## Best Practices Summary

1. **Use subagents for focused, repeatable tasks** — mining organization, file building, company setup
2. **Use main session for coordination and decisions** — reviewing, approving, updating ROADMAP
3. **Always save subagent memory after learning** — don't waste institutional knowledge
4. **Chain subagents sequentially for multi-step builds** — most reliable pattern
5. **Use parallel Explore for read-only multi-company scans** — fast status checks
6. **Skip subagents for simple single-file tasks** — direct tools are faster
7. **Upgrade to Agent Teams only when building 3+ companies simultaneously** — don't over-engineer
8. **Document learnings in _shared/best-practices/** — build institutional memory at holdings level

---

## Troubleshooting

### "Subagent didn't save memory"
**Fix**: Explicitly tell it: "Save what you learned to your memory for next time"

### "Subagent forgot previous patterns"
**Fix**: Check if `~/.claude/agent-memory/[agent-name]/MEMORY.md` exists and has content

### "Two subagents overwrote the same file"
**Fix**: Never run two subagents that write to the same file in parallel. Use sequential chain instead.

### "Main session is slow"
**Fix**: Offload focused tasks to subagents to keep main context window clean

### "Subagent failed mid-task"
**Fix**: Re-run the subagent invocation. Memory persists, so it won't lose previous learnings.

---

## Next Steps

1. Practice the Standard Workflow (Workflow 1) with Finland DMC Session 1
2. Experiment with saving and reviewing subagent memory
3. Build shared resources (_shared/) to accelerate Company 2-10 onboarding
4. Document new patterns you discover in this file
