# CLAUDE.md Hierarchy — Best Practices Guide
<!-- last_updated: session-28 -->
**Four-level configuration system for 1658 Holdings**

---

## Overview

CLAUDE.md files configure how Claude Code behaves in different contexts. We use a **four-level hierarchy** to define instructions from most general (user-wide) to most specific (project-level). This prevents repetition and ensures consistency across 10 portfolio companies.

**The hierarchy** (most general → most specific):
1. **User level**: `~/.claude/CLAUDE.md` (Patrick's defaults for ALL projects)
2. **Holdings level**: `~/1658HoldingsOy-AIFiles/CLAUDE.md` (all 10 companies)
3. **Company level**: `~/1658HoldingsOy-AIFiles/[CompanyName]-AIFiles/CLAUDE.md` (one company)
4. **Project level**: `~/1658HoldingsOy-AIFiles/[CompanyName]-AIFiles/[project]/CLAUDE.md` (one project)

**Inheritance rule**: More specific levels override more general levels. Project-level instructions override company-level, which override holdings-level, which override user-level.

---

## Level 1: User-Level CLAUDE.md

**Location**: `~/.claude/CLAUDE.md`

**Scope**: ALL Claude Code sessions, across all projects and folders

**Purpose**: Patrick Heiskanen's personal defaults and identity context

**What belongs here**:
- Your identity (name, role, company)
- Your working environment (Mac, tools, preferences)
- Universal rules that apply to EVERY session
- Cross-project patterns (two-zone architecture, session habits)
- Default behaviors you want everywhere

**What does NOT belong here**:
- Company-specific information (that's Level 3)
- Project-specific instructions (that's Level 4)
- Instructions that only apply to some projects

### Example User-Level CLAUDE.md

```markdown
# Patrick Heiskanen — Claude Code Defaults

## Identity
- CEO, 1658 Holdings Oy (Heiskanen family portfolio, 10 operating companies, ~50 employees)
- Working from Mac, using Claude Code for file organization and orchestration
- Mining happens in claude.ai with Opus + M365 connector — NOT here

## Universal Rules
- This is a prompt/config file project, NOT software
- All outputs are .md and .txt files — no code compilation
- Always check ROADMAP.md at session start and show current status
- When completing tasks, update ROADMAP.md checkboxes immediately
- Mine first, build after — never create final files from templates alone

## Two-Zone File System
- **Zone A (Workshop):** ~/1658HoldingsOy-AIFiles/ — local + Git, only Patrick uses
- **Zone B (Company Knowledge):** OneDrive-synced folder → SharePoint → M365 searchable by staff
- After building a final file in Zone A, ask if it should be copied to Zone B (OneDrive)

## Session Habits
1. Read ROADMAP.md first, show CURRENT STATUS block
2. Confirm what was done last session and what's next
3. Ask if continuing from where we left off or doing something specific
4. At session end: update ROADMAP.md, add session log entry, suggest next steps
```

---

## Level 2: Holdings-Level CLAUDE.md

**Location**: `~/1658HoldingsOy-AIFiles/CLAUDE.md`

**Scope**: All companies within 1658 Holdings (Finland DMC, Company 2, etc.)

**Purpose**: Define structure and patterns common to all 10 portfolio companies

**What belongs here**:
- Project structure (company folders, _shared/ folder)
- Two-zone architecture (Zone A vs. Zone B)
- Universal commands (status, mark done, new session, etc.)
- Company onboarding pattern
- Cross-company rules

**What does NOT belong here**:
- User identity (that's Level 1)
- Company-specific details (that's Level 3)
- Project-specific workflows (that's Level 4)

### Example Holdings-Level CLAUDE.md

```markdown
# 1658 Holdings Oy — AI Files Workshop

## What This Is
Central workspace for building AI-powered workflows across 10 portfolio companies.
Finland DMC Oy is the pilot company. Others will follow the same pattern.

## Structure
- Each company: `[CompanyName]-AIFiles/` subfolder with its own CLAUDE.md and ROADMAP.md
- Shared resources: `_shared/` folder (templates, prompt library, best practices)
- Each company has a `project-files/` folder for FINAL deliverables

## Two-Zone Architecture
- **This folder (Zone A):** Workshop — build files, mining outputs, progress tracking
- **OneDrive folder (Zone B):** Company Knowledge — final files synced to SharePoint for M365 search
- Claude Code works here in Zone A. Finished files get copied to Zone B.

## Commands (work in any company subfolder)
| Command | Action |
|---------|--------|
| `status` | Show current company's ROADMAP.md CURRENT STATUS block |
| `mark [task] done` | Update checkbox + add completion note in ROADMAP.md |
| `new session` | Add new session log entry with today's date |
| `end session` | Summarize work, update ROADMAP.md, suggest next steps |
| `build [project]` | Assemble final files from mining data, offer to copy to Zone B |
| `show [project] files` | List files in project-files/[project]/ |
| `full status` | Show status + list all files across all directories |

## Company Onboarding Pattern
When adding a new company:
1. Create `[CompanyName]-AIFiles/` folder
2. Create company CLAUDE.md with company profile
3. Create project subfolder with ROADMAP.md and MINING_PROTOCOL.md
4. Create matching OneDrive Zone B folder for final files
5. Follow the same mining → build → upload cycle as Finland DMC
```

---

## Level 3: Company-Level CLAUDE.md

**Location**: `~/1658HoldingsOy-AIFiles/[CompanyName]-AIFiles/CLAUDE.md`

**Scope**: One portfolio company (e.g., Finland DMC)

**Purpose**: Company identity, business context, and company-wide patterns

**What belongs here**:
- Company name, business model, industry
- Company size (staff count, structure)
- Company-wide context (market, geography, clients)
- Company-level projects and structure
- M365 setup details (Teams channels, Claude Projects)
- Company-specific rules

**What does NOT belong here**:
- Holdings-wide structure (that's Level 2)
- Project-specific workflows (that's Level 4)

### Example Company-Level CLAUDE.md

```markdown
# Finland DMC Oy — AI Files

## Company Profile
- **Name**: Finland DMC Oy (Destination Management Company)
- **Business**: Inbound tourism to Finland — itineraries, experiences, logistics
- **Staff**: 5 people (3 sales, 1 operations, 1 admin)
- **Market**: International tour operators, corporate incentive groups, high-end leisure
- **Geography**: Helsinki-based, covering all of Finland

## M365 Setup
- **Claude Teams**: 5 seats, all staff invited
- **M365 Connector**: Enabled, Global Admin connected
- **Shared Mailbox**: info@finlanddmc.fi (primary data source)
- **Teams Channels**:
  - #ai-feedback (staff ratings for Claude drafts)
  - #client-intel (phone notes, client history)
  - #supplier-notes (rates, availability, contacts)
  - #best-practices (internal knowledge)

## Projects Structure
- `finland-dmc-2.0/` — Main Claude AI implementation project
  - 4 Claude Projects: DMC Router, Client Communications, Proposals & Itineraries, Pricing & Analysis
  - 5 mining sessions (email mining, proposals, pricing)
  - ROADMAP.md tracks Phase 0-6 implementation
  - MINING_PROTOCOL.md defines mining process

## Company Context for Claude AI
- Email-heavy business (shared mailbox is primary workflow)
- Client communications must be warm, personal, knowledgeable
- Proposals combine logistics + local expertise + pricing
- Pricing is complex (activities, accommodation, transport, markup)
- Returning clients are majority of business — relationship-driven

## Company-Specific Rules
- All final files built here must be copied to OneDrive Zone B: `~/OneDrive - 1658 Holdings/AI Files/Finland DMC/`
- Use shared mailbox (info@finlanddmc.fi) as primary M365 search target
- Follow Finland DMC tone: friendly, knowledgeable, not salesy
- Always check #client-intel before drafting client emails
```

---

## Level 4: Project-Level CLAUDE.md

**Location**: `~/1658HoldingsOy-AIFiles/[CompanyName]-AIFiles/[project]/CLAUDE.md`

**Scope**: One specific project within a company (e.g., finland-dmc-2.0)

**Purpose**: Project-specific workflows, file structure, and task instructions

**What belongs here**:
- Project goals and scope
- Project folder structure
- Project-specific workflows (mining, building, testing)
- Custom subagents for this project
- File organization rules
- Project-specific commands

**What does NOT belong here**:
- Company-wide context (that's Level 3)
- Holdings-wide patterns (that's Level 2)

### Example Project-Level CLAUDE.md

```markdown
# Finland DMC 2.0 — Claude Code Configuration

## Project Overview
Implementation of Claude AI for Finland DMC's core workflows:
- DMC Router (task classification)
- Client Communications (email drafting)
- Proposals & Itineraries (proposal building)
- Pricing & Analysis (quote generation)

## Folder Structure
```
finland-dmc-2.0/
├── CLAUDE.md (this file)
├── ROADMAP.md (progress tracker)
├── MINING_PROTOCOL.md (mining instructions)
├── mining-outputs/
│   ├── session-1/
│   ├── session-2/
│   └── ...
├── project-files/
│   ├── organized-data/
│   └── finals/
├── templates/
└── reference/
```

## Custom Subagents (Project-Specific)
- **mining-organizer**: Processes raw mining outputs into organized project files
- **file-builder**: Builds final deliverables from organized data and templates

## Workflows

### After Mining Session
1. Paste raw outputs into `mining-outputs/session-N/`
2. Run: `Use the mining-organizer to process Session N outputs`
3. Review organized files in `project-files/organized-data/`
4. Run: `Use the file-builder to create the final [ProjectName] files`
5. Review finals in `project-files/finals/`
6. Copy approved files to OneDrive Zone B
7. Update ROADMAP.md checkboxes

### Building Custom Instructions
1. Read organized mining data
2. Read templates from `templates/`
3. Follow Golden Prompt v4 structure
4. Include DOs/DON'Ts, Tone Guide, Best Lines, Examples
5. Save to `project-files/finals/`

## File Naming Conventions
- Custom Instructions: `[ProjectName]_Custom_Instructions.txt`
- Supporting files: `DOs_and_DONTs.txt`, `Tone_Guide.txt`, `Best_Lines.txt`
- Examples: `Example_Email_[Type].txt`
- Organized data: Keep in `organized-data/` subfolder

## Project-Specific Rules
- Always read ROADMAP.md before starting work
- Update ROADMAP.md checkboxes immediately after completing tasks
- Never create final files from templates alone — mining first
- All files must be .txt or .md (no .docx in project-files)
- Example emails must be real, anonymized emails from mining — not fabricated
```

---

## Inheritance and Override Rules

### How Inheritance Works

When Claude Code starts in a folder, it reads CLAUDE.md files from **most general to most specific**:

1. Reads `~/.claude/CLAUDE.md` (user level)
2. Reads `~/1658HoldingsOy-AIFiles/CLAUDE.md` (holdings level)
3. Reads `~/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/CLAUDE.md` (company level)
4. Reads `~/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/finland-dmc-2.0/CLAUDE.md` (project level)

**Override rule**: If a more specific level defines the same thing as a more general level, the more specific level wins.

### Example: Session Habits Override

**User level** says:
```markdown
## Session Habits
1. Read ROADMAP.md first, show CURRENT STATUS block
2. Confirm what was done last session
```

**Project level** says:
```markdown
## Session Habits
1. Read ROADMAP.md first
2. Read MINING_PROTOCOL.md second
3. Ask which mining session to work on
```

**Result**: When working in that project, Claude Code follows the project-level session habits (reads both ROADMAP.md and MINING_PROTOCOL.md). The user-level habit is overridden.

### Example: Command Override

**Holdings level** defines:
```markdown
| `status` | Show current company's ROADMAP.md CURRENT STATUS block |
```

**Project level** defines:
```markdown
| `status` | Show CURRENT STATUS from ROADMAP.md + list all files in project-files/finals/ |
```

**Result**: When working in that project, the `status` command shows both ROADMAP status and finals listing. The project-level command overrides holdings-level.

---

## Best Practices by Level

### User-Level Best Practices

✅ **Do**:
- Define your identity and working environment
- Set universal rules that apply everywhere
- Define session habits you want in all contexts
- Keep it concise (1-2 pages max)

❌ **Don't**:
- Put company-specific information
- Put project-specific workflows
- Repeat information from Claude Code's built-in instructions

### Holdings-Level Best Practices

✅ **Do**:
- Define folder structure and file organization
- Define commands that work across all companies
- Define the company onboarding pattern
- Explain two-zone architecture

❌ **Don't**:
- Put company names and business details
- Put project-specific workflows
- Repeat user-level identity information

### Company-Level Best Practices

✅ **Do**:
- Provide rich company context (business, staff, market)
- Define M365 setup and Teams channels
- List company-level projects
- Define company-specific tone and rules

❌ **Don't**:
- Put project implementation details
- Repeat holdings-level structure information
- Put individual employee details (unless relevant)

### Project-Level Best Practices

✅ **Do**:
- Define project scope and goals
- Define folder structure for this project
- Define project-specific workflows
- Define file naming conventions

❌ **Don't**:
- Repeat company context
- Repeat holdings-level commands
- Put user-level preferences

---

## Common Patterns

### Pattern 1: Commands at Multiple Levels

Commands can be defined at holdings level and overridden at project level.

**Holdings level**:
```markdown
| `status` | Show current company's ROADMAP.md CURRENT STATUS block |
```

**Project level**:
```markdown
| `status` | Show ROADMAP.md CURRENT STATUS + mining session progress |
```

**Result**: Different behavior depending on where you invoke the command.

### Pattern 2: Shared Context with Specific Examples

Company level provides general context; project level provides specific examples.

**Company level**:
```markdown
## Company Context for Claude AI
- Email-heavy business (shared mailbox is primary workflow)
- Client communications must be warm, personal, knowledgeable
```

**Project level**:
```markdown
## Client Communications Tone
- Warm opening: "It's wonderful to hear from you!"
- Knowledgeable: Always mention specific Finnish experiences
- Personal: Reference past interactions if found in #client-intel
```

**Result**: Project level adds specificity to company-level context.

### Pattern 3: Universal Rules with Project Exceptions

User level sets default; project level makes exception.

**User level**:
```markdown
## Universal Rules
- All outputs are .md and .txt files — no code compilation
```

**Project level**:
```markdown
## File Types
- Custom instructions: .txt
- ROADMAP and guides: .md
- Supplier rates: .xlsx (exception for structured data)
```

**Result**: Project can make exceptions to user-level rules when justified.

---

## Decision Tree: Which Level?

| Content | Level | Reason |
|---------|-------|--------|
| Your name and role | User | Applies to all your work |
| Two-zone architecture | Holdings | All companies use this pattern |
| Finland DMC business model | Company | Specific to one company |
| finland-dmc-2.0 folder structure | Project | Specific to one project |
| "Always check ROADMAP first" | User | Universal habit |
| "Commands work in any company subfolder" | Holdings | Cross-company feature |
| "5 staff members, shared mailbox" | Company | Company-specific context |
| "4 Claude Projects: Router, Comms, Proposals, Pricing" | Project | Project-specific scope |
| Session habits | User | Default for all sessions |
| Company onboarding pattern | Holdings | Cross-company process |
| M365 setup details | Company | Company-specific infrastructure |
| Mining workflow | Project | Project-specific process |
| Custom subagents | Project | Project-specific tools |

---

## Maintenance and Evolution

### When to Update Each Level

**User level**:
- You change your working preferences
- You discover universal rules from experience
- You change your tools or environment

**Holdings level**:
- You refine cross-company structure
- You add new universal commands
- You improve the onboarding pattern

**Company level**:
- Company changes size or structure
- M365 setup changes
- New company-wide projects added
- Business model evolves

**Project level**:
- Workflow improvements discovered
- New custom subagents added
- File structure changes
- New phases or tasks added

### How to Refine CLAUDE.md Files

1. **After each session**: Note what instructions would have helped
2. **Weekly**: Review and refine based on actual usage
3. **Monthly**: Cross-level review — check for duplication or contradictions
4. **Quarterly**: Major update — incorporate learnings from multiple companies

### Version Control

- All CLAUDE.md files in Zone A are Git-tracked
- Check diffs before committing: `git diff CLAUDE.md`
- Use clear commit messages: "Add mining workflow to project CLAUDE.md"
- Tag major versions: `git tag v1.0-finland-dmc-claude-md`

---

## Common Pitfalls

### ❌ Don't: Duplicate content across levels
**Problem**: Same instruction in user and holdings CLAUDE.md
**Fix**: Keep it at the most general level where it applies

### ❌ Don't: Put project details in company CLAUDE.md
**Problem**: Company CLAUDE.md lists specific mining sessions
**Fix**: Move to project CLAUDE.md

### ❌ Don't: Forget to override when needed
**Problem**: Holdings-level command doesn't quite fit project
**Fix**: Override in project CLAUDE.md with project-specific version

### ❌ Don't: Over-specify at user level
**Problem**: User CLAUDE.md has Finland DMC-specific details
**Fix**: Move company details to company CLAUDE.md

### ✅ Do: Think "who needs this information?"
**Fix**: If all sessions need it → user. If all companies need it → holdings. If one company needs it → company. If one project needs it → project.

---

## Quick Reference

| Level | Location | Scope | Examples |
|-------|----------|-------|----------|
| User | `~/.claude/CLAUDE.md` | All sessions | Identity, universal rules, session habits |
| Holdings | `1658HoldingsOy-AIFiles/CLAUDE.md` | All companies | Structure, commands, onboarding |
| Company | `[Company]-AIFiles/CLAUDE.md` | One company | Business context, M365, staff |
| Project | `[Company]-AIFiles/[project]/CLAUDE.md` | One project | Workflows, folder structure, subagents |

**Inheritance**: User → Holdings → Company → Project (most specific wins)

---

## Next Steps

1. Review your current CLAUDE.md files at all 4 levels
2. Check for duplication — move content to correct level
3. Add missing context at appropriate levels
4. Test overrides — ensure project-level instructions work
5. Document learnings in this guide
6. Apply pattern to Company 2-10 as you onboard them
