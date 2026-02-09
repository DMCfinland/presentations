# Response to paste into the deep research conversation

Copy everything below the line into the claude.ai research conversation:

---

Good research but I need corrections on a few critical points before you finalize. Your plan doesn't match my actual situation in some key areas. Please re-research these specific points:

## CORRECTION 1: You missed the OneDrive sync bridge

Your research recommended "local Mac + Git, no OneDrive." But you missed a critical connection in my architecture:

```
Claude Code (edits local files on Mac)
       ↓ writes to
Local folder (inside OneDrive sync folder)
       ↓ auto-syncs to
SharePoint/OneDrive (cloud)
       ↓ searchable by
claude.ai M365 connector (used by staff with golden prompts)
```

My staff will use claude.ai Projects with golden prompts. Those golden prompts use the M365 connector to SEARCH SharePoint for company data (client history, pricing, supplier info). If my files are ONLY on local Mac + Git, the M365 connector can't find them.

**The question I actually need answered:** Can I keep my working folder inside OneDrive's sync folder on Mac, so Claude Code works with local files AND they auto-sync to SharePoint? What are the actual risks on Mac (not Windows) with .md and .txt files (not code)? Is this stable enough for a single-user setup?

## CORRECTION 2: Two types of files, two strategies

My project has TWO kinds of files that need different treatment:

**Type A — Build files (only I use):**
- CLAUDE.md, ROADMAP.md, MINING_PROTOCOL.md, mining outputs
- These are my workshop. Staff never sees them.
- These COULD stay local-only + Git. Staff doesn't need them.

**Type B — Company knowledge files (staff needs via M365):**
- Final golden prompts, service catalog, pricing matrix, supplier directory, client database
- These MUST be in SharePoint so the M365 connector can find them
- When claude.ai drafts an email for a staff member, it searches SharePoint for client history

Your research treated all files the same. Please research the optimal split: which files stay local+Git only, and which files should live in OneDrive-synced folders for SharePoint access?

## CORRECTION 3: I don't need GitHub yet

You recommended pushing to GitHub for backup. But if my files are in OneDrive, I already have cloud backup. Git locally gives me version history. OneDrive gives me cloud backup + SharePoint access. GitHub adds a third copy with no clear benefit for a non-developer solo user.

**Research question:** Is local Git + OneDrive sync sufficient? Or is there a specific reason I need GitHub on top of that?

## CORRECTION 4: Research "orchestrating Claude Code sessions" more deeply

The original research request was specifically about orchestrating TEAMS of Claude Code sessions. Your section 2.4 mentioned "Agent Teams" briefly but didn't go deep. I want to understand:

- How do multiple Claude Code sessions coordinate on shared files?
- The Task tool subagent system — can I have one "orchestrator" session that delegates file-building tasks to specialized sub-sessions?
- Custom subagents in .claude/agents/ — you mentioned them but didn't show how they work for a non-code project like mine
- What does "persistent memory across sessions" mean for custom subagents? Can a subagent remember what it did in the last session?

## WHAT I WANT BACK

1. Revised file storage recommendation with the OneDrive sync bridge factored in
2. Clear split: which files stay local-only vs. which go in OneDrive-synced folder
3. Deep dive on Claude Code session orchestration — subagents, Task tool, Agent Teams with examples relevant to MY project (prompt files, not software)
4. Updated action items reflecting these corrections
