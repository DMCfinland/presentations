# Two-Zone Architecture — Best Practices Guide
<!-- last_updated: session-28 -->
**Workshop vs. Company Knowledge separation for 1658 Holdings**

---

## Overview

The Two-Zone Architecture separates **work-in-progress files** (Zone A) from **final, searchable knowledge** (Zone B). This enables AI mining while keeping project files organized and under version control.

**The Problem**: Claude AI needs M365 connector to search company knowledge. But you can't put work-in-progress files, mining outputs, and templates in SharePoint — too messy, too many false positives.

**The Solution**: Two separate zones with different purposes and access patterns.

---

## The Two Zones

### Zone A: Workshop (Local + Git)

**Location**: `~/1658HoldingsOy-AIFiles/` on your Mac

**Purpose**: Build, organize, and version-control AI project files

**What lives here**:
- Company folders (FinlandDMCOy-AIFiles/, Company2-AIFiles/, etc.)
- Project folders (finland-dmc-2.0/, etc.)
- Mining outputs (raw notes from claude.ai sessions)
- Project files (organized data, work-in-progress)
- Templates (reusable starting points)
- Reference files (research, examples, guides)
- ROADMAP.md files (progress tracking)
- CLAUDE.md files (Claude Code configuration)
- MINING_PROTOCOL.md files (mining instructions)
- _shared/ folder (best practices, prompts, templates)

**Version control**: Git (local only, no push to GitHub)

**Access**:
- You: Claude Code for file building and organization
- Staff: None (this is your private workshop)
- Claude AI: No M365 access (these files don't need to be searched)

**File types**: Everything — .md, .txt, .docx, raw notes, half-finished drafts, experiments

**Sync**: None (local only)

---

### Zone B: Company Knowledge (OneDrive → SharePoint)

**Location**: `~/OneDrive - 1658 Holdings/AI Files/[CompanyName]/` on your Mac, synced to SharePoint

**Purpose**: Deployable knowledge base searchable by Claude AI via M365 connector

**What lives here**:
- **FINAL deliverables only**
- Custom Instructions files (.txt)
- DOs and DON'Ts files (.txt)
- Tone Guides (.txt)
- Best Lines (.txt)
- Example emails (.txt)
- Proposal templates (.txt or .docx)
- Pricing guidelines (.txt)
- Supplier rate cards (.xlsx or .txt)
- Staff quick reference guides (.md or .pdf)

**Version control**: None (OneDrive handles versioning)

**Access**:
- You: Manual file copy from Zone A after approval
- Staff: Read-only via SharePoint (can download for reference)
- Claude AI: M365 connector search (this is the primary purpose)

**File types**: Final, polished files only — no drafts, no mining outputs, no templates

**Sync**: OneDrive automatic sync to SharePoint

---

## File Flow: Zone A → Zone B

### Standard Workflow

1. **Mine** in claude.ai (using M365 connector to search company data)
2. **Paste** raw mining outputs into Zone A `mining-outputs/session-N/`
3. **Organize** with mining-organizer subagent → creates organized files in Zone A `project-files/`
4. **Build** with file-builder subagent → creates final deliverables in Zone A `project-files/`
5. **Review** and approve final files
6. **Copy** approved files from Zone A to Zone B OneDrive folder
7. **Wait** 5-10 minutes for OneDrive sync to SharePoint
8. **Validate** that Claude AI can find the files via M365 search

### Copy Commands

**Manual copy (current approach)**:
```bash
cp /Users/patrickheiskanen/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/finland-dmc-2.0/project-files/Client_Communications_Custom_Instructions.txt ~/OneDrive\ -\ 1658\ Holdings/AI\ Files/Finland\ DMC/
```

**Future**: Could automate with script or Claude Code command.

---

## Decision Tree: Which Zone?

| File Type | Zone A | Zone B | Why |
|-----------|--------|--------|-----|
| Raw mining notes | ✅ | ❌ | Work in progress |
| Organized mining data | ✅ | ❌ | Still being refined |
| Draft custom instructions | ✅ | ❌ | Not ready for AI search |
| Final custom instructions | ✅ | ✅ | Needs to be in both |
| DOs/DON'Ts (final) | ✅ | ✅ | Needs to be in both |
| Tone Guide (final) | ✅ | ✅ | Needs to be in both |
| Example emails (final) | ✅ | ✅ | Needs to be in both |
| Templates (blank) | ✅ | ❌ | Only for building new companies |
| ROADMAP.md | ✅ | ❌ | Progress tracking only |
| CLAUDE.md | ✅ | ❌ | Claude Code config only |
| MINING_PROTOCOL.md | ✅ | ❌ | Mining instructions only |
| Best practices guides | ✅ | Maybe | Zone A for sure, Zone B if staff need it |
| Prompt library | ✅ | ❌ | Building tool only |
| Staff quick reference | ✅ | ✅ | Staff need it in SharePoint |
| Research reports | ✅ | ❌ | Background only |

**General rule**: If Claude AI needs to search it during daily operations, copy to Zone B. Otherwise, Zone A only.

---

## Folder Structure Comparison

### Zone A Structure (Example: Finland DMC)
```
FinlandDMCOy-AIFiles/
├── CLAUDE.md (company-level config)
└── finland-dmc-2.0/
    ├── CLAUDE.md (project-level config)
    ├── ROADMAP.md (progress tracker)
    ├── MINING_PROTOCOL.md (mining instructions)
    ├── mining-outputs/
    │   ├── session-1/
    │   │   ├── raw-notes.txt
    │   │   └── mining-report.md
    │   └── session-2/
    ├── project-files/
    │   ├── Client_Communications_Custom_Instructions.txt (final)
    │   ├── DOs_and_DONTs.txt (final)
    │   ├── Tone_Guide.txt (final)
    │   └── organized-data/ (intermediate)
    ├── templates/
    │   ├── Custom_Instructions_Template.txt
    │   └── DOs_and_DONTs_Template.txt
    └── reference/
        ├── M365_Research.md
        └── Golden_Prompt_v4.txt
```

### Zone B Structure (Example: Finland DMC)
```
OneDrive - 1658 Holdings/
└── AI Files/
    └── Finland DMC/
        ├── Client_Communications_Custom_Instructions.txt
        ├── DOs_and_DONTs.txt
        ├── Tone_Guide.txt
        ├── Best_Lines.txt
        ├── Example_Email_New_Inquiry.txt
        ├── Example_Email_Follow_Up.txt
        ├── Proposal_Template.txt
        ├── Pricing_Guidelines.txt
        ├── Supplier_Rates.xlsx
        └── Staff_Quick_Reference.pdf
```

**Key difference**: Zone B is FLAT and CLEAN. Only final, searchable files. No subfolders, no work-in-progress.

---

## OneDrive Setup (When Admin Returns)

### Initial Setup Steps

1. **Sign into OneDrive**:
   - Open OneDrive app on Mac
   - Sign in with M365 Global Admin account
   - Wait for initial sync to complete

2. **Create Zone B folder structure**:
   ```
   ~/OneDrive - 1658 Holdings/AI Files/
   ```

3. **Create company subfolders**:
   ```
   ~/OneDrive - 1658 Holdings/AI Files/Finland DMC/
   ~/OneDrive - 1658 Holdings/AI Files/Company2/
   ...
   ```

4. **Test sync**:
   - Create test.txt in Finland DMC folder
   - Wait 5 minutes
   - Check SharePoint web interface
   - Verify file appears

5. **Test M365 search**:
   - In claude.ai with M365 connector
   - Ask: "Find test.txt in AI Files folder"
   - Verify Claude can find and read it

6. **Document sync time**:
   - How long from file save to SharePoint availability?
   - Typical: 5-10 minutes
   - Plan accordingly when deploying new files

### Ongoing Zone B Management

- **Copy only final files**: Never copy drafts, mining outputs, or templates
- **Flat structure**: Keep Zone B folders flat (no deep nesting)
- **Clear naming**: Use descriptive file names (no "draft_v2_final_FINAL.txt")
- **Version via filename**: If needed, use dates (Custom_Instructions_2026-02-10.txt)
- **Clean up old versions**: Remove outdated files when updating
- **Document in ROADMAP**: Track which files are deployed to Zone B

---

## Git + OneDrive Integration

### How It Works

- **Zone A**: Git repository (local only, no push to GitHub)
- **Zone B**: OneDrive sync (automatic to SharePoint)
- **No conflict**: The two systems don't overlap

**Git workflow**:
1. Work in Zone A
2. Commit changes locally: `git add . && git commit -m "message"`
3. History preserved, can roll back if needed
4. No push to GitHub — this is private work

**OneDrive workflow**:
1. Copy final files from Zone A to Zone B
2. OneDrive auto-syncs to SharePoint
3. No manual commits needed
4. Claude AI can search via M365 connector

**Key insight**: Zone A needs version control (iterative work). Zone B needs sync (deployment). Different tools for different jobs.

---

## Benefits of Two-Zone Architecture

### For You (CEO)
- **Clean separation**: Work-in-progress vs. finished knowledge
- **Version control**: Git tracks every change in Zone A
- **Safe experimentation**: Try new approaches without polluting company knowledge
- **Clear deploy step**: Explicit approval before files go live
- **Rollback capability**: Git history lets you undo mistakes

### For Staff
- **Clean SharePoint**: Only see final, approved files
- **No confusion**: No drafts or half-finished work
- **Easy discovery**: Claude AI finds the right files via M365 search
- **Clear reference**: Staff quick reference guides in known location

### For Claude AI
- **High signal**: Only final, relevant files in search results
- **No noise**: No mining outputs, templates, or drafts
- **Predictable structure**: Flat folders, clear naming
- **Fast search**: Fewer files to index = faster results

---

## Common Pitfalls to Avoid

### ❌ Don't: Put everything in Zone B
**Why**: Claude AI search gets polluted with drafts, templates, and work-in-progress files. Staff see confusion.

### ❌ Don't: Skip Zone A and work directly in OneDrive
**Why**: No version control, no backup, no separation of work-in-progress.

### ❌ Don't: Copy files to Zone B before review
**Why**: Unfinished work becomes searchable by Claude AI and visible to staff.

### ❌ Don't: Create deep folder hierarchies in Zone B
**Why**: Harder for Claude AI to search, harder for staff to find files.

### ❌ Don't: Use vague file names in Zone B
**Why**: "final.txt" tells no one what the file contains.

### ✅ Do: Build and iterate in Zone A until perfect
**Why**: Version control, safety, separation of concerns.

### ✅ Do: Copy only approved finals to Zone B
**Why**: Clean, searchable, trustworthy company knowledge.

### ✅ Do: Use clear, descriptive file names in Zone B
**Why**: Both humans and AI can understand what each file is.

### ✅ Do: Keep Zone B flat and organized
**Why**: Easy discovery, fast search, clear structure.

---

### Pattern: dual-project-output
**Source:** Session 20 | **When to apply:** Any M365 mining session; any project where Zone A files move to Zone B

Design mining output formats to serve both zones without mining twice. Zone A files should be detailed and AI-readable (full context, markdown, all metadata). Zone B files should be clean and human-readable (simplified, concise, flat structure). The transition is a Sonnet compression step — not a re-mining step.

Workflow: Mine once with rich detail in Zone A → Sonnet compresses to Zone B format → copy the compressed version. Never use Zone A mining outputs directly in Zone B and never mine a second time to produce a "cleaner" version. The rich detail in Zone A is the source of truth; Zone B is the deployment artifact.

---

## Future Enhancements

### Potential Improvements

1. **Automated copy script**: Shell script or Claude Code command to copy approved files
2. **Deploy checklist**: Validation before copying to Zone B (file size, naming, completeness)
3. **Zone B inventory**: Markdown file listing all deployed files per company
4. **Sync monitoring**: Alert if OneDrive sync fails or takes too long
5. **Cross-company shared files**: Some files (best practices) might live in shared Zone B folder

### What NOT to Build

- ❌ Automated sync from Zone A to Zone B (you want explicit approval)
- ❌ Git tracking of Zone B (OneDrive versioning is sufficient)
- ❌ Complex folder structures in Zone B (keep it simple)
- ❌ Automated deployment without review (manual gate is important)

---

## Quick Reference

### Zone A (Workshop)
- **Location**: `~/1658HoldingsOy-AIFiles/`
- **Version control**: Git (local only)
- **Access**: You via Claude Code
- **Contents**: Everything (drafts, mining, templates, finals)
- **Purpose**: Build and organize

### Zone B (Company Knowledge)
- **Location**: `~/OneDrive - 1658 Holdings/AI Files/`
- **Version control**: OneDrive
- **Access**: You, staff (read), Claude AI (M365 search)
- **Contents**: Final files only
- **Purpose**: Deploy and search

### Workflow
1. Mine in claude.ai
2. Build in Zone A
3. Review and approve
4. Copy to Zone B
5. Wait for sync
6. Validate AI search

---

## Next Steps

1. Complete OneDrive setup when admin returns
2. Create Zone B folder structure (AI Files/Finland DMC/)
3. Test sync and M365 search with dummy file
4. Document sync timing
5. Build first final files in Zone A
6. Copy to Zone B and validate
7. Update this guide with lessons learned
