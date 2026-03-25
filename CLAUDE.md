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
1. Read `CURRENT-STATUS.md` (CORE — ~100 lines) — Meta, Current State, Open Deliverables, Context Pack
   - **Do NOT load SESSION-LOG.md or SESSION-ARCHIVE.md at startup** — load on demand only
   - Load SESSION-LOG.md when: session review, pattern harvest, compression, "what happened in s{N}"
   - Load SESSION-ARCHIVE.md when: historical research, Opus Review metrics scan
2. Load warm pack section from `_shared/warm-packs.md` (grep the `warm_pack:` ID from context pack)
3. Show Current State to user, increment `session_number`
4. Compression due? → `session_number == next_compression`. Opus review? → check `next_opus_review` in CURRENT-STATUS.md Meta (mature phase — every 30 sessions; next: session 125)
5. **Context health (Session-Bridge Protocol — Tier A):**
   - **100-150K tokens → Soft Warning:** "Yellow Zone — suggest Session Bridge soon." Do NOT /compact above 120K.
   - **140K tokens → Hard Stop:** Trigger Session-Bridge Protocol immediately → harvest → Cognitive Snapshot → `prompt-creator --bridge` → `genius-check --mode bridge` → new session.
   - **180K tokens → FORCE bridge** (200K pricing cliff 20K away — no exceptions).
   - **Architecture Pivot (≥12 human interventions or paradigm shift):** Trigger at 100K regardless.
   - Full protocol: `_shared/best-practices/session-bridge-protocol.md`
   - **Below 100K:** Use `/compact` after phase breaks or ~turn 12. Saves ~47% of remaining session cost. See `_shared/best-practices/session-compaction-strategy.md`.

### Session End (ALWAYS do this)
1. **Pattern harvest (mandatory — always write something):** Answer: "Did anything new happen this session?"
   - **Yes** → Write a 5-line note to `_shared/best-practices/` (name, what, why, when-to-apply, source-session). Quality > quantity. **Then immediately add entry to `_shared/best-practices/_index.yaml`** — unindexed files are invisible to the system (9 files found unindexed at session 60 review).
   - **No** → Write one line in the session YAML: `harvest_note: "nothing new — [reason, e.g. routine compression / brief Q&A / no novel decisions]"`. This keeps the metric honest.
   - **Patrick corrections get `source: patrick` tag** in the BP file. These are highest-signal — fast-track to Tier A after 1 confirmation (not 3). If a Patrick correction gets ignored in a later session, escalate immediately.
   - **GEPA loop (mandatory if corrections occurred):** If Patrick made ANY correction this session → run `gepa-correction-harvest.md` process → propose a rule → add to `_index.yaml`. Corrections are the highest-signal input. One missed correction = repeated mistake.
2. **Two writes at session end:**
   - **Write A — SESSION-LOG.md:** Prepend new session entry to Rolling Window (keep last 5). Full YAML meta block + free text (10-20 lines) + warm pack pointer. Move sessions beyond last 5 to SESSION-ARCHIVE.md (one-liner format, see below).
   - **Write B — CURRENT-STATUS.md (CORE):** Overwrite Current State table + Open Deliverables (update checkboxes) + Context Pack for next session. KEEP FILE UNDER 100 LINES.
   - YAML schema (required in SESSION-LOG.md, top of every session entry):
     ```yaml
     session: [N]
     date: YYYY-MM-DD
     model: sonnet|opus|haiku
     project_type: [m365-mining|seo-geo|strategic-research|governance|document-import|corporate-knowledge|system-maintenance]
     duration: ~Xmin
     cost: ~$X
     session_tier: 1|2|3
     attributed_value_eur: ~€Y
     human_interventions: N
     handoff_quality: 0-100
     longest_autonomous_task_min: N
     first_turn_quality: high|medium|low
     kb_consulted: yes|no
     kb_topics: [list or empty]
     patterns_harvested: [list or empty]
     harvest_note: "[if nothing harvested: reason — e.g. routine compression, brief Q&A]"
     ```
3. **If compression due:** Move oldest Rolling Window sessions out of SESSION-LOG.md → append one-liners to SESSION-ARCHIVE.md.
   - **One-liner format (Task B — machine-parseable for Opus Review):**
     ```
     S{N} ({date}) kb:{yes/no} harvest:{yes/no} cost:{~$X} tier:{1-3} value:{~€Y} — {description, 1-2 sentences}
     ```
   - Extract kb/harvest/cost/tier/value from the session's YAML block before compressing.
   - Keep CURRENT-STATUS.md CORE under 100 lines at all times.
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
6. **Warm pack freshness + activation audit** — Check `last_curated` timestamps. Packs >10 sessions stale (bootstrap) or >30 sessions stale (mature): refresh triggers. **Then run activation audit:** scan session logs for trigger matches per warm pack. Rate: WORKING ≥40% / PARTIAL 20-39% / BROKEN <20%. If BROKEN in 2 consecutive reviews → retire system. Methodology: `_shared/best-practices/warm-pack-activation-audit.md`.
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
Three distinct modes — choose based on task structure (arXiv:2512.08296, cross-validated Grok+Gemini 2026-03-16):
- **Main thread + task subagents (centralized orchestration):** Default for parallel analysis. Main thread = orchestrator + validator. Subagents = isolated executors. Error amplification 4.4× (contained by validation). This is what we call "task subagents" — it IS centralized coordination.
- **Single agent:** Best for sequential tasks with deep state dependencies. Coordination degrades -39% to -70% on sequential work.
- **Agent Teams (peer debate):** ONLY when: (1) overlapping targets requiring real-time debate, (2) high-entropy exploration, AND (3) base model accuracy < ~45% baseline. Above saturation threshold (β = -0.408), adding peer agents adds noise. Rarely justified with Sonnet/Opus.
- **Validation bottleneck is mandatory.** Without orchestrator review, isolated executors amplify errors 17.2×. PWJ loop = the validation mechanism. Never aggregate subagent outputs without review.
- **Use /pwj before spawning any subagent for a deliverable from 2+ source files.** Run structured intake (6 questions) first — vague criteria → vague output. Skip only for single-file edits or tasks with live credentials. (skill: `~/.claude/skills/pwj/SKILL.md`)
  - **When writing done criteria:** load `_shared/best-practices/pwj-bridge-prompt-quality.md`. Key rules: test production failure (not presence); Integrated Eval Sets = 10–20 cases per class; statistical graduation triggers need N≥99 per subclass for CI upper bound <3% (not N≥50 — see pwj-stat-guardrail-n99.md).
  - **For bridge prompts:** run the 6-item self-check in `_shared/best-practices/session-bridge-protocol.md` (PWJ Bridge Prompt Self-Check section) before finalizing.
- **Same-model Judge = theater.** PWJ with the same model as Worker produces guaranteed PASS (hallucination consensus). External model mandatory for verification: Grok Step 3.5 OR Mistral Step 5. (source: S89 empirical finding)
- **Never skip source material — distill instead.** "SKIP IF 130K+" = false economy; $0.50 savings propagates incomplete analysis downstream. (source: patrick, confirmed session 48)

### PWJ Tool-Lock (Hard-Coded — No Exceptions)
<!-- Added: session-100 | Source: Gemini Senior Architect Directive S97-99 audit -->

**FORBIDDEN — do NOT answer in the main thread. Invoke `/pwj` immediately:**
- Any prompt containing "PWJ INTAKE" or structured intake fields (Goal / Done Criteria / Tier / Constraints)
- Any prompt referencing "Tier 1/2/3" framing for a deliverable
- Technical Specifications (new system specs, architecture docs, interface contracts)
- Architecture Pivots (changing how two or more systems interact)
- Strategic Research (multi-source synthesis producing a recommendation or decision)

**OPTIONAL — judgment call (/pwj recommended but not required):**
- Single-file edits, typo/formatting fixes
- Simple file moves, renames, or path corrections
- Quick Q&A with no structured deliverable output

**Task Matrix:**

| Task Type | PWJ Required? |
|-----------|--------------|
| Technical spec / architecture doc | MANDATORY |
| Architecture pivot (≥2 systems) | MANDATORY |
| Strategic research + recommendation | MANDATORY |
| Multi-source deliverable (2+ files) | MANDATORY |
| Single-file edit / typo / format | Optional |
| Simple file move / rename | Optional |
| Quick Q&A (no deliverable) | Optional |

**Why hard-coded:** S97-99 audit identified "First-Action Failure" — Claude skips /pwj and rushes to linear execution, producing Checklist Theater (validates presence, not logic). Tool-Lock prevents this.

### Integration Specs — Time-Boxing (MO-1, source: S103)
- Any integration spec with a time constraint (e.g., "≤5 minutes") MUST use a `PREREQUISITE (one-time setup)` block before numbered steps. This block is NOT counted in the per-session total.
- Per-session total uses steady-state step times only. One-time setup costs are amortized.
- If maximum-estimate total exceeds constraint due to a one-time condition: apply this rule, not a criteria game.

### Regex Specs — Execution Order (MO-2, source: S103)
- Any spec with multiple regex passes on the same text MUST specify execution order explicitly.
- CAPS normalization MUST run before urgency/authority patterns — "HETI" is not matched by `\bheti\b` until lowercased. Silent production failure if order is wrong.
- Template: add "Pattern execution order" section to all regex-heavy specs.

### Upstream Writes Flags, Downstream Reads Only (MO-5, source: S103)
- When two system layers share state (e.g., S3→S4, S4→S5), the upstream layer writes ALL interface fields before downstream runs.
- Downstream NEVER re-derives fields from raw input — reads upstream output schema only.
- Missing field = route to human. Never silent default. Enforce via NOT NULL + schema validation.

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
