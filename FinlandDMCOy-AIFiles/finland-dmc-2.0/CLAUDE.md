# CLAUDE.md — Finland DMC 2.0 Project Configuration

## What This Project Is

Finland DMC Oy is a 5-person destination management company in Finland.
This is NOT a code project. We are building an AI-powered workflow system using Claude Teams with 4-5 execution projects (Router, Client Comms, Proposals, Pricing, optional Internal Ops).

All outputs are `.txt` and `.md` files — prompt files, tone guides, example libraries, mining reports.
No code compilation. No software builds. No test suites.

## How This System Works

1. **Mining sessions** happen in **claude.ai** (Opus + M365 search connector) — NOT here in Claude Code
2. **Claude Code** organizes output files, tracks progress, and builds final project files from mining data
3. The user will paste or upload mining session reports into `mining-outputs/`
4. Claude Code's job: organize, refine, and assemble final files in `project-files/`

## On Every Session Start

1. Read `ROADMAP.md` and display the CURRENT STATUS block
2. Briefly confirm what was done last session and what's next
3. Ask if the user wants to continue from where we left off or do something specific

## Folder Structure

```
finland-dmc-2.0/
├── CLAUDE.md                    ← You are here (project config)
├── ROADMAP.md                   ← Progress tracker — THE file
├── MINING_PROTOCOL.md           ← Standard mining session process
├── mining-outputs/              ← Reports from claude.ai mining sessions
│   ├── session-1-client-comms-outbound/
│   ├── session-2-inbound-emails/
│   ├── session-3-router/
│   ├── session-4-proposals/
│   └── session-5-pricing/
├── project-files/               ← FINAL files for pasting into Claude Projects
│   ├── router/
│   ├── client-comms/
│   ├── proposals/
│   └── pricing/
├── templates/                   ← Example/reference files — NOT final
└── reference/                   ← Research docs, PRD, M365 findings
```

## Commands

These are natural-language shortcuts the user may type:

| Command | Action |
|---------|--------|
| `status` | Read ROADMAP.md, show the CURRENT STATUS block |
| `mark [task] done` | Find the task in ROADMAP.md, change `[ ]` to `[x]`, add completion note |
| `new session` | Add a new session log entry to ROADMAP.md with today's date |
| `end session` | Summarize what was done, update ROADMAP.md status + session log, suggest next steps |
| `build [project]` | Create/update final files in `project-files/[project]/` from mining data |
| `show [project] files` | List current files in `project-files/[project]/` |
| `show mining [N]` | List files in `mining-outputs/session-[N]-*/` |
| `full status` | Show ROADMAP.md CURRENT STATUS + list all files across all directories |

## How to Handle Mining Outputs

When the user pastes or uploads mining session content:

1. Identify which session it belongs to (1-5)
2. Save raw report to `mining-outputs/session-[N]-[topic]/mining-report.md`
3. Extract individual components (examples, patterns, guidelines) into separate files
4. Ask if the user wants to start building final project files from this data

## How to Build Project Files

When the user says `build [project]`:

1. Check what mining data exists in `mining-outputs/`
2. Check what files already exist in `project-files/[project]/`
3. List what can be built and what's still missing
4. For each file: draft it, show a summary, ask for approval before saving
5. Save approved files to `project-files/[project]/`

## Project → File Mapping

| Project | Files Needed |
|---------|-------------|
| **Router** | Custom_Instructions.txt, Inbound_Email_Patterns.txt |
| **Client Comms** | Custom_Instructions.txt, DOs_and_DONTs.txt, Tone_Guide.txt, Best_Lines.txt, 8x Example_Email_*.txt |
| **Proposals** | Custom_Instructions.txt, DOs_and_DONTs.txt, Tone_Guide.txt, Best_Lines.txt, Proposal_Structure_Template.txt, 2-3x Example_Proposal_*.txt, Supplier_Rates_Reference.txt |
| **Pricing** | Custom_Instructions.txt, DOs_and_DONTs.txt, Pricing_Guidelines.txt, Supplier_Rates_Reference.txt |

## Key Principles

- **Mine first, build after.** Never create final files from templates — always from real mined data.
- **One golden prompt per project.** Each project gets one carefully crafted Custom_Instructions.txt.
- **Real language only.** Tone guides and example files must come from actual Finland DMC emails, not generic AI writing.
- **Simplest thing that works.** No over-engineering. These are text files, not software.
