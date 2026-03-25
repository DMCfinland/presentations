# Self-Maintaining Knowledge System — Architecture Design
<!-- last_updated: session-28 -->

**Author:** Opus 4.6 (system architect)
**Date:** 2026-02-18
**Status:** APPROVED DESIGN — Sonnet implements, Opus reviews
**Version:** 1.0

---

## Design Philosophy

**The system that maintains itself is the only system that works.**

Evidence from our own data:
- Pre-Flight Checklist (CLAUDE.md) — created 2026-02-11, zero operational usage in 7 days
- _shared/best-practices/ — 13 files (292KB), zero consultations during actual work
- YouTube KB — $95 invested, routing index built, zero queries in production

**Root cause:** Documented patterns ≠ activated patterns. Rules in files get forgotten.
Rules in system prompts get executed. The gap is activation, not documentation.

**Design principle:** If a rule matters, it must be in CLAUDE.md or enforced by a skill.
Everything else is reference material for on-demand loading.

---

## Part 1: Session Lifecycle

### Architecture

```
CURRENT-STATUS.md (max 500 lines, ~10K tokens, ~5% context)
├── META BLOCK (5 lines, machine-readable)
│   session_number, window_start, next_compression, last_compressed
│
├── CURRENT STATE (100 lines, overwritten EVERY session)
│   Phase, active projects, blockers, next 3 tasks
│   Active deliverables and their status
│   Cost tracker (cumulative)
│
├── ROLLING WINDOW (300 lines, append within window)
│   Last 5 sessions, detailed log
│   Decisions made, files created, learnings
│
└── COMPRESSED HISTORY (100 lines, one-liner per session)
    Sessions before current window
    Format: "Session N (date): [key outcome] [files: N] [cost: $X]"
```

### Session Start Protocol

```
1. Read CURRENT-STATUS.md (500 lines, 5% context)
2. Increment session_number in META BLOCK
3. Display CURRENT STATE to user
4. Check: session_number == next_compression?
   YES → Flag "Compression due. Run at session end."
   NO  → Continue
5. Check: session_number % 30 == 0?
   YES → Flag "Opus review due. Schedule separately."
   NO  → Continue
```

### Session End Protocol (Simplified v2 — 2026-02-18)

```
1. ONE WRITE to CURRENT-STATUS.md:
   - Append session log (15-25 lines) to ROLLING WINDOW
   - Overwrite CURRENT STATE with fresh status
   - Set context pack: warm_pack ID + 2-3 key files + session-specific notes
   - NO grepping _index.yaml or routing-index.yaml (warm packs have the knowledge)
2. If compression flagged:
   - Compress oldest sessions to one-liners
   - Archive full text to _archive/sessions/YYYY-MM.md
   - Update META: window_start, next_compression
   - Batch-update _index.yaml usage counters (deferred from individual sessions)
3. Update ROADMAP.md checkbox if task completed
```

**Design principle:** Session end = 1 read + 1 write. All elaborate compilation
was moved to warm packs (pre-built by Opus, read-only for Sonnet).
Usage tracking deferred to compression time (every 5 sessions) to avoid
per-session bureaucracy that gets skipped under context pressure anyway.

### Compression Rules (Sonnet executes these)

What to KEEP in one-liner:
- What was accomplished (verb + noun)
- Key decisions made
- Files created/modified (count)
- Cost spent
- Blockers hit or resolved

What to DROP:
- Step-by-step descriptions of how things were done
- File content previews
- Command outputs
- Intermediate debugging steps
- Context that's captured elsewhere (MEMORY.md, best-practices)

Example compression:
```
BEFORE (62 lines):
### Session 2026-02-12 Part 16 | Phase 0 + Järvisydän SEO | ~2h
**Accomplished:**
- ✅ Fixed 2 critical issues from Opus review (backup instructions, robots.txt overwrite risk)
- ✅ Changed revenue estimate from "100k-1M€" to "+100k€" (more conservative, Opus agreed)
- ✅ Completed Opus keyword research → KEYWORD-STRATEGY-2.0.md (986 lines)
[... 56 more lines of details ...]

AFTER (1 line):
Session 24 (2026-02-12): Fixed 2 Opus-flagged issues, conservative revenue est, keyword strategy built (986L). Files: 3 modified. Cost: ~$3.
```

### What Happens to ROADMAP.md

**Current:** 1,475 lines (76% session logs, growing 62 lines/session)
**New role:** Project PLANNING only. No session logs.

```
ROADMAP.md (new structure, ~300 lines stable):
├── PHASE DEFINITIONS (what each phase means)
├── PROJECT TRACKER TABLE (company × status matrix)
├── ACTIVE PROJECT PLANS (checkbox lists for current work)
└── BACKLOG (future work, prioritized)

No session logs. Those live in CURRENT-STATUS.md.
```

---

## Part 2: Three-Tier Pattern System

### The Problem

13 best-practice files (292KB) in _shared/best-practices/.
Zero operational consultations.
Patterns documented but never activated.

### The Architecture

```
TIER A: ACTIVE RULES                    → In CLAUDE.md (always loaded, always enforced)
  - 10-15 battle-tested do's/don'ts
  - Promoted from Tier B after 3+ successful uses
  - Demoted to Tier B if not relevant for 90 days
  - MAX: 30 lines in CLAUDE.md

TIER B: REFERENCE PATTERNS              → In _shared/best-practices/ (load on demand)
  - Full documentation with context
  - Accessed via routing index or topic search
  - Where new patterns start their lifecycle
  - No size limit per file

TIER C: HISTORICAL CONTEXT              → In _archive/ (rarely loaded)
  - Why decisions were made
  - Raw session logs
  - Superseded patterns
  - Only loaded when debugging or revisiting
```

### Pattern Lifecycle

```
 DISCOVERED (during work)
     │
     ▼
 DOCUMENTED (Tier B: _shared/best-practices/)
     │
     ├── Used 3+ times successfully
     │       │
     │       ▼
     │   PROMOTED (Tier A: CLAUDE.md rule)
     │       │
     │       ├── Still relevant → stays in Tier A
     │       └── Not triggered in 90 days → demoted to Tier B
     │
     └── Not used in 90 days
             │
             ▼
         ARCHIVED (Tier C: _archive/)
```

### Tier A Rules (Initial Set — for CLAUDE.md)

These are validated by 24 sessions of empirical evidence:

```markdown
## Operational Rules (Tier A — Battle-Tested)

### Cost
- Calculate cost BEFORE executing any query over $1
- Test with 10-20% sample before full batch
- Use system field for Batch API prompt caching (90% discount)
- Use Haiku for mechanical work (categorization, sorting) — 60x cheaper than Opus

### Quality
- Mine first, build after — never create deliverables from templates alone
- Design for single-shot extraction (assume no follow-ups on expensive queries)
- Split large prompts into focused requests — prevents lazy responses
- Positive instructions > negative ("only use source language" > "don't add commentary")

### Safety
- Never load files >500KB without checking size first
- Never glob-read entire directories (knowledge-base/videos/ = 7MB)
- Don't send follow-ups in expensive Project windows — download and close
- Don't let LLMs write scripts when you asked for markdown

### Session
- Overwrite CURRENT STATE, append session logs, compress every 5 sessions
- Flag reusable patterns immediately when discovered
- Update project checkboxes in ROADMAP.md when completing tasks
```

### Tier B Reference Index

Create `_shared/best-practices/_index.yaml`:
```yaml
# Pattern Reference Index
# Grep this file to find relevant patterns before starting work

patterns:
  - file: document-architecture.md
    one_line: "Centralized documents/ with {prefix}-{cat}-{desc}-{date} naming, 7 categories"
    use_when: "Setting up new company, importing documents, organizing files"
    validated: true
    times_used: 13  # 13 company imports

  - file: finnish-corporate-governance-and-document-drafting.md
    one_line: "OYL compliance, HHJ standards, bilingual templates, vuosikello"
    use_when: "Board meetings, shareholder decisions, annual governance calendar"
    validated: true
    times_used: 3  # batch prompts A/B/C

  - file: research-chunking-and-cost-optimization.md
    one_line: "Batch API size limits, prompt caching, progressive filtering"
    use_when: "Running batch jobs, large research queries, cost estimation"
    validated: true
    times_used: 5  # YouTube batch, governance batch, Jarvisydan batch

  - file: context-window-failure-modes.md
    one_line: "Empirical evidence from 1.7M token tests — what breaks and when"
    use_when: "Planning large context loads, debugging context-related failures"
    validated: true
    times_used: 2

  - file: RAG-BEST-PRACTICES.md
    one_line: "When to use RAG vs full context vs Batch API"
    use_when: "Choosing query architecture for new research project"
    validated: true
    times_used: 2

  - file: claude-md-hierarchy.md
    one_line: "Four-level CLAUDE.md config: global > project > company > feature"
    use_when: "Setting up new company or project, modifying system behavior"
    validated: true
    times_used: 1

  - file: two-zone-architecture.md
    one_line: "Zone A (Workshop) vs Zone B (Company Knowledge via OneDrive/SharePoint)"
    use_when: "Deciding where a file should live, setting up sync"
    validated: true
    times_used: 1

  - file: claude-code-orchestration.md
    one_line: "Non-code projects with Claude Code: subagents, skills, prompt files"
    use_when: "Building new workflow, designing skill, planning subagent use"
    validated: true
    times_used: 1

  - file: claude-code-skill-architecture.md
    one_line: "Skill structure: commands/*.md + skills/*/SKILL.md + .local.md"
    use_when: "Building a new Claude Code skill"
    validated: false
    times_used: 0

  - file: kb-utilization-strategy.md
    one_line: "When/how to query YouTube KB: tier 1-3 decisions, trigger rules"
    use_when: "Starting new project, making strategic decision"
    validated: false
    times_used: 0

  - file: ai-deployment-principles.md
    one_line: "Universal AI deployment principles for 10 portfolio companies"
    use_when: "Planning AI rollout for new company, training staff"
    validated: false
    times_used: 0

  - file: api-key-security-2026.md
    one_line: "macOS Keychain, env vars, security best practices for API keys"
    use_when: "Setting up API key, configuring batch scripts"
    validated: false
    times_used: 0

  - file: knowledge-base-indexing.md
    one_line: "Research on KB indexing strategies: routing index, topic maps"
    use_when: "Building index for new knowledge base"
    validated: true
    times_used: 1  # YouTube KB routing index
```

---

## Part 3: YouTube KB Activation

### The Problem

$95 invested. 196 analyses. Routing index built. Pre-Flight Checklist written.
Zero queries in 7 days of active work.

### Why It's Not Activating

1. **Pre-Flight is a suggestion, not a gate.** CLAUDE.md says "ALWAYS" but nothing enforces it.
2. **5-step ritual is too heavy.** Nobody does 5 steps before starting work.
3. **No success stories.** No demonstrated value → no habit formation.
4. **Building > Using.** The next task always feels more urgent than checking references.

### The Fix: Reduce Friction to Zero

**Replace the 5-step Pre-Flight with a 1-step check:**

```markdown
## KB Quick-Check (in CLAUDE.md)
Before starting a NEW project or making a STRATEGIC decision:
  grep -i "[topic keywords]" YouTubeResearch-AIFiles/knowledge-base/_index/routing-index.yaml
If matches found: read the one_line field. If relevant, load the full file.
If no matches: proceed without KB. Log "KB checked: no match" in session.
```

**That's it.** One grep. 2 seconds. Not a ritual.

### Tracking

Add to session log template:
```
KB consulted: [yes/no] [topic if yes]
```

After 10 sessions of tracking, we'll know if it's being used. If not, the KB is reference-only (Tier C) and we stop trying to force it into daily workflow.

### When KB Actually Adds Value

The 196 videos are strongest for:
1. **AI agent design** (32 videos) — when building new workflows
2. **AI strategy** (28 videos) — when planning company rollouts
3. **Prompt engineering** (20 videos) — when designing prompts for batch jobs
4. **Enterprise AI** (11 videos) — when advising portfolio companies

They're weakest for:
- Finnish/EU regulatory (0 videos)
- Tourism/hospitality (0 videos)
- SEO/digital marketing (0 videos)
- Financial modeling (0 videos)

**Implication:** Don't check KB for Järvisydän SEO work. DO check for AI workflow design, company training plans, or strategic decisions about AI adoption.

---

## Part 4: Model-Specific Operating Principles

### Model Selection Matrix

```
┌─────────────────────────────────────────────────┐
│                 TASK COMPLEXITY                  │
│                                                  │
│  HIGH ┌──────────────┐                           │
│       │    OPUS      │  Design, review, audit    │
│       │  $15/$75/M   │  Every 30 sessions        │
│       │  ~$2-5/task  │  System architecture       │
│       └──────────────┘  Cross-project synthesis   │
│                                                  │
│  MED  ┌──────────────┐                           │
│       │   SONNET     │  Build, execute, compress  │
│       │  $3/$15/M    │  Every session             │
│       │  ~$0.05-0.50 │  File creation, coding     │
│       └──────────────┘  Structured extraction     │
│                                                  │
│  LOW  ┌──────────────┐                           │
│       │    HAIKU     │  Classify, sort, tag       │
│       │  $0.25/$1.25 │  Batch jobs only           │
│       │  ~$0.01/task │  Document import           │
│       └──────────────┘  No judgment required      │
│                                                  │
└─────────────────────────────────────────────────┘
```

### Opus Operating Principles

**Role:** Architect. Strategic reviewer. Quality auditor.

**Best practices:**
- Give Opus COMPLETE context — it excels with full picture
- Ask for DECISIONS, not execution ("Which approach?" not "Build this")
- Use for cross-project synthesis (sees patterns across companies)
- Use for system design (this document is an Opus product)
- Use for quality gates (review Sonnet's output before delivery)

**Anti-patterns:**
- Don't use Opus to write files (expensive, Sonnet is equally good at execution)
- Don't use Opus for formatting or structural changes
- Don't use Opus when the decision is already made (just execute with Sonnet)
- Don't ask Opus multiple simple questions — batch into one strategic prompt

**Cost control:**
- Opus reviews every 30 sessions (~monthly): $3-5 per review
- Annual Opus budget: ~$50-75 for system maintenance
- Each Opus session should produce a design doc that Sonnet follows for weeks

### Sonnet Operating Principles

**Role:** Builder. Executor. Compressor. Maintainer.

**Best practices:**
- Give Sonnet CLEAR RULES from Opus designs
- Sonnet excels at: structured output, templates, YAML/markdown, following specifications
- Use Sonnet subagents for parallel work (audit, search, build)
- Sonnet is the default for ALL session work in Claude Code
- Best at: following templates, compression, file building, structured extraction

**Anti-patterns:**
- Don't ask Sonnet to make architectural decisions
- Don't ask Sonnet to evaluate its own output quality
- Don't give Sonnet open-ended creative briefs without structure

**Sonnet-specific prompting:**
- Be explicit about output format (YAML, markdown table, checklist)
- Provide examples of desired output
- Use positive instructions ("only include X") over negative ("don't add Y")
- Cap output length explicitly ("max 12 items", "under 100 lines")

### Haiku Operating Principles

**Role:** Classifier. Sorter. Simple transformer.

**Best practices:**
- Narrow task scope: one decision per call
- Explicit rules: "If filename contains X, category = Y"
- Finnish keyword matching: proven at 100% accuracy for document categorization
- Batch processing: 2,408 files at $0.01-0.02 per company
- Perfect for: file sorting, metadata extraction, simple categorization

**Anti-patterns:**
- Don't ask Haiku for creative work or nuanced judgment
- Don't use Haiku for compression (adds contamination risk — validated finding)
- Don't chain Haiku outputs without verification
- Don't use for multi-step reasoning

---

## Part 5: Document Knowledge Architecture

### Principle

Documents are STORAGE. Summaries are CONTEXT.
The AI system never loads original documents. It loads company knowledge summaries.

### Architecture

```
documents/                          ← STORAGE (Zone A, never auto-loaded by AI)
├── _holdings/
│   ├── inter-company/
│   ├── arviokirjat/
│   └── [category folders]
├── finland-dmc-oy/
│   ├── corp/ con/ fin/ emp/ ops/ prop/
│   └── _arkisto/
├── jarvisydan-oy/
└── [future companies]/

[Company]-AIFiles/                  ← AI CONTEXT (summaries + deliverables)
├── CLAUDE.md                       Company profile + rules
├── KNOWLEDGE-SUMMARY.md            ← THE ROUTING LAYER FOR DOCUMENTS
│   Contains:
│   - Company overview (10 lines)
│   - Document inventory by category (count + key files)
│   - Key numbers (revenue, employees, locations)
│   - Document gaps (what's missing)
│   - Cross-references to holdings docs
│   - Last updated date
├── project-files/                  AI-generated deliverables
└── [project-specific folders]
```

### KNOWLEDGE-SUMMARY.md Template

```markdown
# [Company Name] — Document Knowledge Summary

**Last updated:** [date]
**Total documents:** [N] across [N] categories
**Source:** documents/[company-slug]/

## Company Profile
- [2-3 line description]
- Revenue: [X], Employees: [N], Locations: [list]

## Document Inventory
| Category | Count | Key Files | Notes |
|----------|-------|-----------|-------|
| corp     | 12    | Board minutes 2023-2025, Articles of Association | Up to date |
| con      | 8     | Supplier agreements, client contracts | 3 expiring 2026 |
| fin      | 15    | Annual reports 2020-2025, tax filings | Missing Q4 2025 |
| emp      | 5     | Employment contracts | Template needed |
| ops      | 3     | Licenses, permits | Renewal due 2026-06 |
| prop     | 7     | Lease agreements, property valuations | |

## Key Cross-References
- Holdings inter-company loan: documents/_holdings/inter-company/[file]
- Shared insurance policy: documents/_holdings/[file]

## Gaps
- [ ] Missing: Q4 2025 financial statements
- [ ] Missing: Updated employment contract template
- [ ] Needed: Property insurance renewal documentation
```

### Build Process

```
SONNET reads documents/[company]/ → counts files per category
  → identifies key documents by filename
  → writes KNOWLEDGE-SUMMARY.md
  → flags gaps and missing items

OPUS reviews summaries across all companies
  → identifies cross-company patterns
  → flags systemic gaps
  → updates holdings-level strategy
```

### What NOT to Index

- Individual document contents (PDFs, contracts, etc.)
- Scanned images
- Duplicate versions
- Archived/superseded documents
- Any file in _arkisto/ subfolders

---

## Part 6: Self-Improvement Loop

### The Compound Engine

```
SESSION N:     Work happens, learnings accumulate
SESSION N END: Sonnet compresses, updates status, flags patterns
EVERY 5:      Sonnet deep-compresses session logs
EVERY 10:     Sonnet reviews pattern index, updates validation counts
EVERY 30:     Opus reviews entire system:
               - Are Tier A rules still relevant?
               - Should any Tier B patterns be promoted?
               - Are there Tier B patterns that were never used? → Archive
               - Is the routing index accurate?
               - Has the session template drifted? → Correct
               - System performance metrics:
                 - Context efficiency (target: 5-20% on status)
                 - Pattern activation rate (target: >50%)
                 - KB consultation rate (target: 1x/week)
                 - Compression ratio (target: 10:1)
```

### Metrics to Track

```yaml
# Added to session log template
metrics:
  context_on_status: "X%"        # Target: 5-20%
  kb_consulted: "yes/no [topic]" # Target: 1x/week
  patterns_applied: "N [names]"  # Target: 1+ per session
  new_patterns_found: "N"        # Flag for Tier B documentation
  session_cost: "$X.XX"          # Track spend
```

### Quality Gates

Before promoting a pattern from Tier B to Tier A:
1. Used successfully 3+ times (validated)
2. Applies across 2+ projects or companies (generalizable)
3. Has a clear, actionable rule formulation (<2 lines)
4. Doesn't duplicate an existing Tier A rule

Before archiving a pattern from Tier B to Tier C:
1. Not referenced in any work session for 90+ days
2. No upcoming project that would use it
3. Not foundational to system architecture

---

## Part 7: Implementation Plan

### Phase 1: Skeleton (Sonnet, 30 minutes)

1. Create CURRENT-STATUS.md from ROADMAP.md top section
2. Create _archive/2026-02-february/import-project/
3. Move 28 root-level IMPORT-*/MERGE-*/PLAN-* files to archive
4. Create _shared/best-practices/_index.yaml
5. Add Tier A rules to CLAUDE.md
6. Slim ROADMAP.md to planning-only (remove session logs)

### Phase 2: Session Template (Sonnet, 15 minutes)

1. Define session log template with metrics fields
2. Update CLAUDE.md session start/end protocols
3. Add compression trigger logic (session_number % 5)
4. Test with one session cycle

### Phase 3: Pattern Activation (Sonnet, 30 minutes)

1. Replace Pre-Flight Checklist with 1-step KB Quick-Check
2. Create pattern reference index (_index.yaml)
3. Add "KB consulted" and "patterns applied" to session template
4. Document first successful KB query (break the zero)

### Phase 4: First Opus Review (Opus, at session 30)

1. Review compressed session history (sessions 1-30)
2. Evaluate pattern activation rates (uses/last_used data from _index.yaml)
3. Propose Tier A promotions/demotions based on usage data
4. Assess CURRENT-STATUS.md effectiveness
5. **Refresh warm packs** (`_shared/warm-packs.md`):
   - Identify new project types from session history
   - Update existing warm packs with lessons from last 30 sessions
   - Add cross-company insights (patterns proven at company A → surface for company B)
   - Remove warm pack entries not used in 30 sessions
   - Update project_types registry in _index.yaml
6. Recommend system improvements for next 30 sessions

---

## Appendix: Cost Model

| Activity | Frequency | Model | Cost/Instance | Annual (156 sessions) |
|----------|-----------|-------|---------------|----------------------|
| Session start/end | Every session | Sonnet | $0.02 | $3.12 |
| Compression | Every 5 sessions | Sonnet | $0.10 | $3.12 |
| Pattern review | Every 10 sessions | Sonnet | $0.20 | $3.12 |
| Opus system review | Every 30 sessions | Opus | $3.00 | $15.60 |
| **Total maintenance** | | | | **$24.96/year** |

Compare to current: 55% context waste → slower responses, more expensive sessions,
earlier context compression, lost institutional knowledge.

**ROI:** ~$25/year maintenance cost prevents hundreds of dollars in wasted context
and hours of manual cleanup.

---

## Appendix: File Size Budgets

```
ALWAYS LOADED (< 5% context = < 10K tokens = < 40KB):
  CLAUDE.md            ~4KB  (current: 3.5KB)
  CURRENT-STATUS.md    ~25KB (target: 500 lines × ~50 chars)
  MEMORY.md            ~15KB (current: ~12KB)
  ─────────────────────────────
  Total:               ~44KB (~11K tokens, ~5.5% of 200K context)

LOADED ON DEMAND (< 20% context per file):
  _shared/best-practices/[file].md     10-50KB each
  [Company]-AIFiles/ROADMAP.md         ~15KB each
  routing-index.yaml                   ~87KB
  ─────────────────────────────
  Load 1-2 per session as needed

NEVER AUTO-LOADED:
  documents/                           Gigabytes
  knowledge-base/videos/               7MB total
  _archive/                            Growing
  consolidated-videos-context.md       6.85MB (QUARANTINED)
```

---

**END OF DESIGN DOCUMENT**

*This document was designed by Opus 4.6. Implementation by Sonnet.
Review cycle: Every 30 sessions by Opus.*
