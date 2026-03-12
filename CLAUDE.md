# 1658 Holdings Oy — AI Files Workshop

## Foundational Principle

**QUALITY OVER QUANTITY. ALWAYS.**

- Better context > more context
- Focused retrieval > full dump
- Compressed insights > verbose analysis
- High-value patterns > exhaustive documentation
- Proven templates > custom solutions
- Strategic decisions > endless options

This principle guides every optimization, every tool, every workflow.

---

## What This Is
Central workspace for building AI-powered workflows across 10 portfolio companies.
Finland DMC Oy is the pilot company. Others will follow the same pattern.

## Structure
- Each company: `[CompanyName]-AIFiles/` subfolder with its own CLAUDE.md and ROADMAP.md
- Shared resources: `_shared/` folder (templates, prompt library, best practices)
- Each company has a `project-files/` folder for FINAL deliverables
- **Company documents:** `documents/` folder at holdings root (centralized, not per-company)
  - See `_shared/best-practices/document-architecture.md` for naming rules and taxonomy
  - Naming: `{prefix}-{cat}-{description}-{date}.{ext}` (e.g., `dmc-corp-board-minutes-2024-03.pdf`)
  - 7 categories: corp, con, fin, emp, ops, prop, ico
  - Inter-company docs always in `documents/_holdings/inter-company/`

## Two-Zone Architecture
- **This folder (Zone A):** Workshop — build files, mining outputs, progress tracking
- **OneDrive folder (Zone B):** Company Knowledge — final files synced to SharePoint for M365 search
- Claude Code works here in Zone A. Finished files get copied to Zone B.

---

## Session Protocol

### Session Start (ALWAYS do this)
1. Read `CURRENT-STATUS.md` — has status, recent sessions, and context pack with warm pack ID
2. Load warm pack section from `_shared/warm-packs.md` (grep the `warm_pack:` ID from context pack)
3. Show Current State to user, increment `session_number`
4. Compression due? → `session_number == next_compression`. Opus review? → check `next_opus_review` in CURRENT-STATUS.md Meta (bootstrap phase; next: session 70)
5. **Context health:** In file-heavy sessions (corporate-knowledge, strategic-research), use `/compact` after phase breaks or ~turn 12. All key outputs should already be in `.md` files before compacting. Saves ~47% of remaining session cost. See `_shared/best-practices/session-compaction-strategy.md`.

### Session End (ALWAYS do this)
1. **Pattern harvest (mandatory — always write something):** Answer: "Did anything new happen this session?"
   - **Yes** → Write a 5-line note to `_shared/best-practices/` (name, what, why, when-to-apply, source-session). Quality > quantity. **Then immediately add entry to `_shared/best-practices/_index.yaml`** — unindexed files are invisible to the system (9 files found unindexed at session 60 review).
   - **No** → Write one line in the session YAML: `harvest_note: "nothing new — [reason, e.g. routine compression / brief Q&A / no novel decisions]"`. This keeps the metric honest.
   - **Patrick corrections get `source: patrick` tag** in the BP file. These are highest-signal — fast-track to Tier A after 1 confirmation (not 3). If a Patrick correction gets ignored in a later session, escalate immediately.
2. **One write to CURRENT-STATUS.md** — append session log + overwrite Current State + set context pack:
   - Session log: open with a YAML meta block (machine-parseable for Opus review), then free text
   - YAML schema (required, at top of every session log):
     ```yaml
     session: [N]
     date: YYYY-MM-DD
     model: sonnet|opus|haiku
     project_type: [m365-mining|seo-geo|strategic-research|governance|document-import|corporate-knowledge|system-maintenance]
     duration: ~Xmin
     cost: ~$X
     first_turn_quality: high|medium|low
     kb_consulted: yes|no
     kb_topics: [list or empty]
     patterns_harvested: [list or empty]
     harvest_note: "[if nothing harvested: reason — e.g. routine compression, brief Q&A]"
     ```
   - Then free text: what was done, files created/modified (keep to 10-20 lines)
   - Context pack: `warm_pack: [project-type-id]` + list 2-3 key files for next session + any session-specific notes
   - No grepping required — warm packs already contain the knowledge
3. If compression due: compress oldest sessions to one-liners, archive full text
4. Usage tracking in `_index.yaml`: defer to compression time (every 5 sessions), not every session

### Opus Review
**Bootstrap phase (sessions 1-60):** Every 10 sessions. No hard limit on improvements — prioritize highest-impact first, but fix everything clearly broken.
**Mature phase (after targets met):** Every 30 sessions. No hard limit on improvements — prioritize highest-impact first.
**Graduate when:** KB consulted >40% (non-mining sessions only) AND pattern harvest >20% sustained over 2 consecutive reviews AND trend is STABLE OR IMPROVING (not declining). Declining metrics = stay bootstrap regardless of absolute threshold.

Triggered when `session_number % 10 == 0` (bootstrap) or `session_number % 30 == 0` (mature). Opus runs a full system health check:

1. **Utilization audit** — Parse YAML meta blocks in session logs since last review. Count separately:
   - **Non-mining sessions** (`project_type` ≠ m365-mining): KB consulted target >40%. Mining sessions extract new knowledge; consulting KB during mining is structurally wrong.
   - **All sessions:** pattern harvest target >20%.
   Report both rates. Graduate threshold uses non-mining KB rate only.
2. **Knowledge/noise ratio** — Read all Knowledge Triggers in warm-packs.md. For each trigger: did it fire in any session log? Remove triggers with zero activations. Promote high-fire triggers to CLAUDE.md Tier A if >3 uses.
3. **Pattern discovery quality** — Review patterns harvested since last review. Are they reusable or one-offs? Archive one-offs. Strengthen high-value ones with evidence from additional sessions. **Separately track `source: patrick` patterns:** Were they applied in subsequent sessions? Any ignored? Ignored Patrick corrections = system failure, fix immediately.
4. **Contradiction scan** — Check whether any two active Tier A rules or Knowledge Triggers give conflicting guidance. Conflicting patterns = actively harmful. Resolve by keeping the more specific/recent one and archiving the other.
5. **BP file health** — Check `_index.yaml` usage counts. Files with 0 uses since last review: flag for Patrick's decision (archive or integrate harder). Files with >5 uses: check if they need updating.
6. **Warm pack freshness** — Check `last_curated` timestamps. Packs >10 sessions stale (bootstrap) or >30 sessions stale (mature): refresh triggers from latest topic files and BP files.
7. **Continuous improvement** — What worked better this cycle vs last? What's still not activating? Propose up to 3 concrete changes to improve the system for the next review cycle.
8. **Cross-pack propagation** — Review patterns harvested since last review. For each pattern: does it apply to other project types beyond where it was discovered? If yes, add it to those warm packs too. A pattern found in DMC mining that applies universally should appear in all 7 packs.

Output: Write findings to `_archive/opus-reviews/review-session-[N].md`. Update `_index.yaml`, warm-packs.md, and CLAUDE.md as needed. Steps 4 (contradiction scan) and 8 (cross-pack propagation) require changes to be applied immediately, not just noted.

---

## Operational Rules (Tier A — Battle-Tested)

These rules are validated across 50+ sessions. Follow them without exception.

### Cost
- Calculate cost BEFORE executing any query over $1
- Test with 10-20% sample before full batch
- Use `system` field for Batch API prompt caching (90% discount after request #1)
- Use Haiku for mechanical work (categorization, sorting) — 60x cheaper than Opus

### Quality
- Mine first, build after — never create deliverables from templates alone
- Design for single-shot extraction (assume no follow-ups on expensive queries)
- Split large prompts into focused batch requests — prevents lazy/commentary responses
- Positive instructions > negative ("only use source language" > "don't add commentary")
- For any Excel file: run sniffer first before smart extractor — see `excel-mining-protocol.md` v2.0

### Orchestration
- **Task subagents > Agent Teams for sequential-wave analysis.** Use Agent Teams ONLY when same-wave agents need overlapping targets requiring real-time debate. (3-4× cheaper, same quality — source: patrick, confirmed session 48)
- **Never skip source material — distill instead.** "SKIP IF 130K+" = false economy; $0.50 savings propagates incomplete analysis downstream. (source: patrick, confirmed session 48)

### Safety
- Check file size before loading; files >500KB require size-first verification
- Read directories selectively; glob-read of knowledge-base/videos/ (7MB) would overflow context
- Extract responses from Project windows, then close; follow-ups multiply cost
- When requesting markdown output, specify "Write markdown directly, NO scripts" — LLMs default to code

### Models — Right Model, Right Task
- **Opus 4.6 (1.67× Sonnet cost — $5/$25 vs $3/$15 per MTok):** Use ONLY for tasks where it uniquely wins:
  - **GPQA expert reasoning** (91.3% vs 74.1%): multi-hop deductive chains, complex legal/financial synthesis across many sources, scientific analysis
  - **Large corpus retrieval WITH reasoning**: needle-in-haystack where understanding context is required (not just finding it)
  - **Opus reviews themselves** — system health, pattern audits, architectural decisions
  - **NOT for:** strategic planning, architecture, quality review, financial analysis, coding — Sonnet matches or beats Opus on all of these
  - **RULE: When running AS Opus, spin up Sonnet subagents for execution work of 3+ tool calls.** For <3 calls, Opus can execute directly.
  - 1M context window available (same as Sonnet beta) — use for corpora too large for Sonnet's 200K
- **Sonnet 4.6 ($3/$15 per MTok):** Default for ALL work. Matches/beats Opus on: coding (79.6% vs 80.8%), computer use (72.5% vs 72.7%), office productivity (1633 vs 1606 Elo), financial analysis (63.3% vs 60.1%).
  - **Adaptive thinking built-in** — automatically reasons deeply when needed, no manual configuration
  - **1M context window (beta)** — use for large corpora; no longer need Opus just for context size
  - ⚠️ **200K pricing cliff:** Above 200K input tokens ALL tokens cost 2× ($6/$22.50). Default: stay under. Cross intentionally only (estimate first — 200K ≈ 150KB text). Session tax: ~16K base + ~5K/turn → /compact before turn 15 in file-heavy sessions.
- **Haiku 4.5 ($1/$5 per MTok — 3× cheaper than Sonnet):** Classify, sort, tag. Batch jobs only. Never for creative or judgment work.
- **Context isolation:** Subagents start fresh — no conversation history inherited. Write complete self-contained prompts with all needed context (file paths, codes, benchmarks, expected output). Vague prompt = vague result.
- Decision tree: GPQA-level reasoning or >200K reasoning → Opus. Everything else → Sonnet. Volume/mechanical → Haiku.
- Full strategy + pricing: `_shared/claude-pricing-reference.md` | `_shared/best-practices/model-strategy.md`

### KB-Validated Universals
- Mode-aware context > volume — curated 10K tokens outperform unsorted 1M (knowledge-rag)
- Principles-based guidance scales; rules-based breaks at first edge case (knowledge-rag)
- Embed retrieval keys, not knowledge dumps — trigger recall, don't preload (prompting-context)

---

## Commands

| Command | Action |
|---------|--------|
| `status` | Read CURRENT-STATUS.md, show Current State + Context Pack summary |
| `full status` | Show status + company matrix + list all active project files |
| `mark [task] done` | Update checkbox in ROADMAP.md + CURRENT-STATUS.md deliverables |
| `new session` | Increment session_number, start new session log entry |
| `end session` | One write to CURRENT-STATUS.md (log + status + warm pack pointer), compress if due |
| `build [project]` | Assemble final files from mining data, offer to copy to Zone B |
| `show [project] files` | List files in project-files/[project]/ |
| `compress` | Force session log compression (archive + one-liners) |

---

## Company Onboarding Pattern
When adding a new company:
1. Create `[CompanyName]-AIFiles/` folder for AI work products
2. Create company CLAUDE.md with company profile
3. Create project subfolder with ROADMAP.md and MINING_PROTOCOL.md
4. Create `documents/{company-slug}/` with category subfolders (corp, con, fin, emp, ops, prop)
5. Register company prefix in `documents/_index.md`
6. Create matching OneDrive Zone B folder for final files
7. Follow the same mining → build → upload cycle as Finland DMC

## Pattern Tracking

When discovering reusable patterns during work:
1. Flag immediately with: `PATTERN: [name] — [one-line description]`
2. Document in `_shared/best-practices/` (Tier B)
3. After 3+ successful uses → propose promotion to Tier A (this file's Operational Rules)
4. Patterns not used in 90 days → archive to `_archive/`

Reference: `_shared/best-practices/_index.yaml` — routing index for all documented patterns
Full design: `_shared/best-practices/self-maintaining-knowledge-system.md`
