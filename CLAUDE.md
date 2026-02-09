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
