# Warm Packs — Project-Type Knowledge Briefings
# Load the matching warm pack at session start based on active project type.
# Each pack: ~25-35 lines of battle-tested insights for that project type.
# Unified Knowledge Triggers (YouTube KB + Best Practices) + Deep Dive per pack.
# Updated: 2026-03-19 | Last Opus review: Session 95 | Next Opus review: Session 125 (mature phase)

---

## seo-geo | Website SEO/GEO Optimization
<!-- last_curated: 2026-03-17 -->

### What Works
- Orchestrated Sonnet specialist teams: 4 agents in parallel beats one comprehensive agent
- GEO > SEO for 2026: AI search growing 50-100% YoY, 12-18 month first-mover window
- Structure content for AI extraction: FAQ format, comparison tables, clean 18-token extractable sentences
- llms.txt + entity descriptions = AI citation fuel
- Conservative revenue estimates ("+100k" not "100k-1M") build trust with team

### What Fails
- v1 email tone was robotic — always match the team's communication style
- English duplicates waste time — decide language upfront (Finnish-only for Järvisydän)
- Verbose content underperforms — less is more, focus beats breadth
- Missing backup instructions = critical risk (Opus caught this, user didn't)

### Model Strategy
- Sonnet: ALL SEO/GEO work — research, competitive analysis, content packages, quality review (Sonnet beats Opus on office productivity 1633 vs 1606 Elo)
- Opus: NOT needed for SEO/GEO work
- Haiku: Not used for SEO/GEO (requires judgment)

### Cost Benchmark
- Full v3.0 package: ~$5-8 (Sonnet specialists, same quality at 1.67× savings)
- Always calculate before parallel agent launch

### Required Reads (load at session start — not optional)
- `bp: two-zone-architecture.md` — Zone A/B output structure; every SEO session produces deliverables for Zone B

### Knowledge Triggers
<!-- Planning mode: focus on breadth triggers (alternatives, risks). Execution mode: focus on precision triggers (constraints, costs, steps). -->
- Content architecture beats content volume — 18-token extractable sentences outperform 30K guides → Structure for AI citation, not human reading (topics/seo-search-geo.md, 26 insights)
- GEO = architect for AI memory effect — what AI cites becomes canonical → Build passage-level citability into every page (topics/seo-search-geo.md)
- Over-specification kills creative output (Goldilocks principle) → Brief strategically, don't template-fill (topics/prompting-context.md)
- YouTube KB has zero SEO/tourism video coverage — skip KB topic lookup for industry-specific SEO; use BP files and external research instead → Don't waste context loading KB for SEO content questions
- Dual-project-output: Build both working files (Zone A) and clean deliverables (Zone B) in every production session → Prevents "build it twice" overhead at deployment time (bp: two-zone-architecture.md)
- Session compaction: After 10-12 turns or completing a phase (research → build), use /compact → saves ~47% of remaining session cost; all outputs already in .md files so near-zero performance loss (bp: session-compaction-strategy.md)

- Cold Start Discovery Mode: before any file reads in a new session, ask 3 strategic questions (Purpose / Business Goal / Definition of Done) → lock as Session DNA → then load context. User intent frames which files to load, not vice versa. (bp: cold-start-discovery-mode.md, session 92)

### Deep Dive (load on demand)
- "How do I optimize content for AI search citations?" → `topics/seo-search-geo.md` (26 insights, ~10KB)
- "How should I structure my prompt strategy for content generation?" → `topics/prompting-context.md` (114 insights, ~119KB)
- "Which topic file covers my current question?" → `_topic-index.md` (2KB routing index)

---

## document-import | Document Import & Organization
<!-- last_curated: 2026-03-17 -->

### What Works
- Phase 1 bash renames (free, 2 min) → Phase 2 Haiku categorization ($0.05/130 files)
- Finnish keyword detection for auto-categorization (liiketoiminta→ops, sopimus→con)
- _arkisto standardization across all companies
- Sonnet spot-check on 10% sample validates Haiku ($0.50 to prevent $20 mistakes)
- Three-folder-depth maximum — deeper = lost files

### What Fails
- Folder names too technical ("yritys") — use intuitive Finnish ("hallinto")
- Vague categories ("toiminta") — be specific ("luvat-ja-vakuutukset")
- macOS Finder creates curly-brace folders — fix with bash escaping
- Duplicate folders silently split collections (Lomakylä velkakirjat: 85 files in 2 places)

### Model Strategy
- Sonnet: ALL import work — quality validation, architecture decisions, bash orchestration
- Haiku: Bulk categorization ($0.05/130 files)
- Opus: NOT needed for document import

### Cost Benchmark
- 8,255 files organized: $0.07 total (Haiku only, bash free)
- Quality gate: $1-2 (Opus spot-check)
- Never skip the sample test

### Required Reads (load at session start — not optional)
- `bp: document-architecture.md` — naming conventions and 7-category taxonomy; always needed before touching files

### Knowledge Triggers
<!-- Planning mode: focus on breadth triggers (alternatives, risks). Execution mode: focus on precision triggers (constraints, costs, steps). -->
- Subcorpus semantic structure — organize with explicit meaning before applying AI → Taxonomize first, process second (topics/knowledge-rag.md)
- 78% of AI struggles trace to data readiness, not model capability → Invest 60-70% of effort in data organization (topics/knowledge-rag.md)
- _inbox/ staging + 7-category taxonomy (corp/con/fin/emp/ops/prop/ico) is the proven import pattern → Apply naming convention `{prefix}-{cat}-{description}-{date}.{ext}` before any AI processing (bp: document-architecture.md, 14KB)
- Session compaction: Use /compact after completing each import phase (bash renames → Haiku categorization → Opus spot-check) → saves ~47% if session runs long (bp: session-compaction-strategy.md)

- Cold Start Discovery Mode: before any file reads in a new session, ask 3 strategic questions (Purpose / Business Goal / Definition of Done) → lock as Session DNA → then load context. User intent frames which files to load, not vice versa. (bp: cold-start-discovery-mode.md, session 92)

### Deep Dive (load on demand)
- "How should I design the folder structure or naming schema?" → `topics/knowledge-rag.md` (95 insights, ~100KB)
- "Which topic file covers my current question?" → `_topic-index.md` (2KB routing index)
- "What are the naming conventions and taxonomy rules?" → `bp: document-architecture.md` (14KB)
- "How do I prepare files for Zone B / OneDrive sync?" → `bp: two-zone-architecture.md` (12KB)

---

## strategic-research | Strategic Research & Knowledge Base Building
<!-- last_curated: 2026-03-17 -->

### What Works
- Single Sonnet pass extraction ($2.97) — kills 3-stage Haiku→Sonnet→Opus ($10)
- File-by-file processing guarantees 100% coverage (vs bulk: 6-15% actual processing)
- 5 insight types, max 12/doc, positive instructions > negative
- Three-tier retrieval: routing index (5KB) → gold nuggets (~50KB) → full analyses (7MB)
- Design for single-shot extraction — assume no follow-ups on expensive queries
- External AI cross-validation: after internal synthesis, send to Grok/GPT-4 for open-ended challenge (catches regulatory gaps, different priors)

### What Fails
- Loading 1M+ tokens ≠ reading 1M+ tokens ($44 Context Rot lesson: only 6.5% processed)
- Haiku compression ADDS contamination risk (training data "wearing the video's costume")
- Building without using = shelf ware (YouTube KB: $95 invested, zero operational usage in 7 days)
- LLMs default to scripts — say "Write markdown directly, NO scripts"
- 3-stage pipelines when single pass is cheaper
- Skipping source material in multi-agent analysis ("SKIP IF 130K+" = false economy)

### Model Strategy
- Sonnet: ALL strategic-research work — extraction, synthesis, quality audit, go/no-go decisions (Sonnet beats Opus on financial analysis 63.3% vs 60.1%)
- Opus: ONLY for GPQA-level cross-source synthesis requiring multi-hop reasoning
- Haiku: ONLY for mechanical categorization/tagging. Never for extraction.

### Cost Benchmark
- 196-video extraction: $1.89 (Batch API + Sonnet)
- Single Opus strategic review: $3-5 (batch)
- Context Rot lesson: $44 wasted on bulk loading

### Required Reads (load at session start — not optional)
- `bp: research-chunking-and-cost-optimization.md` — batch API limits, cost modeling; calculate before any extraction job

### Knowledge Triggers
<!-- Planning mode: focus on breadth triggers (alternatives, risks). Execution mode: focus on precision triggers (constraints, costs, steps). -->
- Curated 10K tokens outperform unsorted 1M — match context to task mode (planning=breadth, execution=precision) → Load topic files selectively, never dump (topics/knowledge-rag.md, 95 insights)
- Deliverable from 2+ source files → use /pwj before spawning any subagent. Run 6-question intake first. Direct subagent spawn without intake = vague criteria → vague output. (skill: ~/.claude/skills/pwj/SKILL.md, Grok-validated 2026-03-17)
- Schema-driven summarization preserves semantics; blind compression destroys signal → Use structured templates for extraction, not "summarize this" (topics/prompting-context.md, 114 insights)
- Forgetting is technology, not bug — active curation > passive accumulation → Compress and curate at defined intervals, don't just append (topics/knowledge-rag.md)
- First-Turn Usefulness Rate = primary metric for prompt quality → Track whether prompts work on first try (topics/prompting-context.md)
- Build three-tier index (routing index → gold nuggets → full source) when corpus exceeds 50 items → Don't skip the index layer, it prevents the "build first, use never" trap (bp: knowledge-base-indexing.md, 33KB)
- Watch for extrapolation signals: "might," "could suggest," "possibly indicates" → Flag and quarantine; extraction must stay within source evidence (bp: RAG-BEST-PRACTICES.md, 52KB)
- Mid-session-checkpoint: Save intermediate results to files at natural breakpoints in sessions >30 minutes → Prevents total loss on crash or context-out, especially during multi-hour extraction (bp: mid-session-checkpoint.md)
- Session compaction: At phase break (research → synthesis) or ~turn 10-12, use /compact → saves ~47% of remaining session cost; research outputs already in files = near-zero loss (bp: session-compaction-strategy.md)
- Session Bridge: at 100K-150K tokens → soft warning, suggest Bridge. At 140K → hard stop, trigger Session-Bridge Protocol (harvest → Cognitive Snapshot → prompt-creator --bridge → genius-check --mode bridge → new session). Do NOT /compact above 120K. (bp: session-bridge-protocol.md)
- External AI cross-validation: after completing any major synthesis (goal doc, multi-agent deliverable), challenge it with an external AI using an open-ended prompt → catches regulatory gaps and different priors before committing to execution (bp: external-ai-cross-validation.md)
- Never skip source material in multi-agent analysis — distill instead. "SKIP IF 130K+" is false economy; $0.50 saved propagates incomplete analysis downstream (Tier A rule, source: patrick)
- Task subagents > Agent Teams for sequential-wave analysis — 3-4× cheaper, same quality. Only use Agent Teams when same-wave agents need real-time debate (Tier A rule, source: patrick)
- Pre-brief reduces corrections: include 5-line company context brief at session START when mining external sources (Substack, YouTube, docs, community) → prevents mid-session correction rounds when source conflicts with company tool choices (bp: pre-brief-reduces-corrections.md, source: patrick)
- Cross-skill upgrade via Grok: when a skill feels stale or underperforms, run a /grok-spar Research Debate to research latest best practices → upgrade the skill with Grok's research claims, fact-check via WebSearch, apply only verified claims (bp: cross-skill-upgrade-via-grok-spar.md)
- Lead Agent quality gate: for any multi-step subagent task, run structured intake first — Goal + Done criteria + Tier + Constraints + Output format. Same-model red-teaming = hallucination consensus — use structured checklist instead. (bp: lead-agent-quality-gate.md, session 71)
- Planner-Worker-Judge empirical data: Worker accuracy 33% on meta-analysis. Always verify HIGH-severity findings independently. File manifest prevents false "file missing" claims. (bp: planner-worker-judge-loop.md, session 74)
- Cohort prediction discipline: N<5 = coin flip. Cohort_strong/individual_ok/suppressed tiers apply to ANY signal surfaced from research mining. (bp: cohort-vs-individual-prediction.md, source: patrick D51)
- PWJ theater: same-model Judge = guaranteed PASS (hallucination consensus). External model mandatory for verification: Grok Step 3.5 OR Mistral Step 5. (bp: pwj-theater-vs-real-execution.md, session 89)

- Cold Start Discovery Mode: before any file reads in a new session, ask 3 strategic questions (Purpose / Business Goal / Definition of Done) → lock as Session DNA → then load context. User intent frames which files to load, not vice versa. (bp: cold-start-discovery-mode.md, session 92)

### Deep Dive (load on demand)
- "How should I design this knowledge system or retrieval flow?" → `topics/knowledge-rag.md` (95 insights, ~100KB)
- "How do I optimize my prompts or context engineering?" → `topics/prompting-context.md` (114 insights, ~119KB)
- "Which topic file covers my current question?" → `_topic-index.md` (2KB routing index)
- "How do I validate extraction quality or prevent hallucination?" → `bp: RAG-BEST-PRACTICES.md` (52KB)
- "How do I optimize batch API costs or chunking strategy?" → `bp: research-chunking-and-cost-optimization.md` (24KB)
- "How should I build the index layer for this corpus?" → `bp: knowledge-base-indexing.md` (33KB)
- "After synthesis, how do I validate against blind spots?" → `bp: external-ai-cross-validation.md`

---

## m365-mining | M365 Mining & Knowledge Extraction
<!-- last_curated: 2026-03-17 -->

### What Works
- Desktop mines → Code organizes → Desktop/Projects deploy (three-environment architecture)
- 5-session extraction sequence: Outbound → Inbound → Router → Proposals → Pricing
- Mailbox delegation for email access (grant to sales@finland-dmc.com)
- Mining-first: 15h mining before writing one custom instruction
- Progressive trust expansion: constrain what agents can do, expand as validated
- Task subagents > Agent Teams for sequential-wave mining (3-4× cheaper, same quality)

### What Works (continued)
- Claude Code in VS Code HAS M365 MCP access (email, SharePoint, Teams, calendar, read_resource) — use /m365-mine skill for structured extraction (discovered session 57)

### What Fails
- Validate mining architecture before committing to 15-hour workflow (30-min test first)
- Don't assume email access — test delegation separately
- Skipping source material in agent-based extraction ("SKIP IF 130K+" = false economy)

### Model Strategy
- Sonnet: Workflow design, organizing mined data, building custom instructions, compression
- Haiku: Categorizing extracted items (email types, document types)
- Opus: NOT needed for m365-mining (workflow design doesn't require GPQA reasoning)

### Cost Benchmark
- DMC workflow design: $2-3 (Opus batch)
- Full 10-company rollout estimate: $30-50 (15h × 10 companies, but 7h savings after first)
- Efficiency projection: Save ~45h across portfolio

### Required Reads (load at session start — not optional)
- `bp: agent-orchestration-patterns.md` — subagents vs Agent Teams vs n8n; every mining session involves orchestration decisions

### Knowledge Triggers
<!-- Planning mode: focus on breadth triggers (alternatives, risks). Execution mode: focus on precision triggers (constraints, costs, steps). -->
- Planning leverage exhibits power law returns — 2x upfront planning = 10x execution quality → Invest in anchor prompts before mining, not after (topics/knowledge-rag.md)
- Sub-agents need narrow scoped views, not shared transcripts → Scope mining prompts tightly per document type (topics/prompting-context.md)
- Conversational intelligence compounds — treat multi-turn threads as strategic IP → Archive successful mining conversations as templates (topics/knowledge-rag.md)
- Batch API has 334KB per-request byte limit (not token limit) → Calculate payload size before submission; split large requests (bp: research-chunking-and-cost-optimization.md, 24KB)
- Zone B files must be flat-structured for SharePoint sync — no nested subfolders beyond company/category → Validate output structure before copy to OneDrive (bp: two-zone-architecture.md, 12KB)
- Session compaction: m365-mining sessions run long (5+ searches). Use /compact between search blocks (e.g. after outbound block, before inbound) → saves ~47%, and all mined data is already in files (bp: session-compaction-strategy.md)
- Never skip source material when spawning subagents for extraction — distill instead of skipping. SKIP = false economy that propagates incomplete data. (Tier A rule, source: patrick)
- Self-check capability matching: design agent self-checks to measure things agents can actually assess. Quantitative metrics (token counts, costs) → unreliable. Qualitative categories (light/medium/heavy context load) → honest data. (bp: session 47 pattern)
- Pre-brief reduces corrections: before any external-source mining session, add 5-line company context brief (tool decisions, standing overrides) → prevents mid-session correction rounds when source conflicts with company choices (bp: pre-brief-reduces-corrections.md, source: patrick)

- Cold Start Discovery Mode: before any file reads in a new session, ask 3 strategic questions (Purpose / Business Goal / Definition of Done) → lock as Session DNA → then load context. User intent frames which files to load, not vice versa. (bp: cold-start-discovery-mode.md, session 92)

### Deep Dive (load on demand)
- "How should I design the mining workflow or automate steps?" → `topics/productivity-workflows.md` (53 insights, ~20KB)
- "How do I orchestrate multiple mining agents or searches?" → `topics/agent-architecture.md` (249 insights, ~80KB)
- "Which topic file covers my current question?" → `_topic-index.md` (2KB routing index)
- "How do I optimize batch extraction job costs?" → `bp: research-chunking-and-cost-optimization.md` (24KB)
- "How do I prepare mined files for Zone B deployment?" → `bp: two-zone-architecture.md` (12KB)
- "Choosing orchestration approach?" → `bp: agent-orchestration-patterns.md` (subagents vs teams vs n8n)

---

## governance | Governance & Compliance Synthesis
<!-- last_curated: 2026-03-17 -->

### What Works
- Split large prompts into 3 focused Opus prompts — prevents lazy/commentary responses
- Batch API ($1) vs claude.ai Projects ($15-24) for legal synthesis
- 195KB→39KB compression (80%) preserving ALL legal requirements
- Vuosikello format: monthly obligations with responsible party and deadline
- RED/YELLOW/GREEN validation for 12 document types

### What Fails
- Master prompt = shallow commentary (Opus gets lazy on broad prompts)
- Anti-laziness instructions needed: "Complete all sections. Do not summarize or skip."
- Don't mix governance with other topics — legal work needs focused context

### Model Strategy
- Opus: ALL governance synthesis (legal accuracy requires highest capability)
- Sonnet: Template formatting, deadline tracking, vuosikello updates
- Haiku: Never for governance (legal errors = liability)

### Cost Benchmark
- Full governance synthesis: ~$1 (3 Opus batch prompts)
- Never use Haiku for legal work — $0.01 savings not worth the risk

### Required Reads (load at session start — not optional)
- `bp: finnish-corporate-governance-and-document-drafting.md` — RED/YELLOW/GREEN checklist + vuosikello; always the core reference for Finnish compliance work

### Knowledge Triggers
<!-- Planning mode: focus on breadth triggers (alternatives, risks). Execution mode: focus on precision triggers (constraints, costs, steps). -->
- Proprietary rubrics = real moat — encode what "quality" means in your context → Build governance rubrics from mined best practices, not generic templates (topics/knowledge-rag.md)
- The "87% accurate" design philosophy — AI needs excellent human escalation paths → Design governance outputs with explicit human review gates (topics/knowledge-rag.md)
- Scope separation is legal necessity — personal/professional context must never cross → Enforce strict domain boundaries in compliance outputs (topics/security-governance.md, 44 insights)
- Finnish corporate governance has mandatory RED/YELLOW/GREEN validation for 12 document types → Run compliance check against vuosikello before declaring any governance deliverable complete (bp: finnish-corporate-governance-and-document-drafting.md, 40KB)
- Design for 87% accuracy with excellent human escalation paths → Build explicit review gates into governance outputs, never ship without human checkpoint (bp: ai-deployment-principles.md, 11KB)
- Session compaction: Governance sessions often run long (multiple document reviews). Use /compact after completing each section (e.g. after board minutes review, before tilinpäätös) → saves ~47%, all findings already in files (bp: session-compaction-strategy.md)

- Cold Start Discovery Mode: before any file reads in a new session, ask 3 strategic questions (Purpose / Business Goal / Definition of Done) → lock as Session DNA → then load context. User intent frames which files to load, not vice versa. (bp: cold-start-discovery-mode.md, session 92)

### Deep Dive (load on demand)
- "What are the compliance, privacy, or security requirements?" → `topics/security-governance.md` (44 insights, ~15KB)
- "How should I design organizational governance structures?" → `topics/leadership-org.md` (125 insights, ~40KB)
- "Which topic file covers my current question?" → `_topic-index.md` (2KB routing index)
- "What are the Finnish corporate governance rules and vuosikello requirements?" → `bp: finnish-corporate-governance-and-document-drafting.md` (40KB)
- "How do I design human review gates for governance outputs?" → `bp: ai-deployment-principles.md` (11KB)

---

## corporate-knowledge | Corporate Knowledge Hub (Multi-Company)
<!-- last_curated: 2026-03-17 -->

### What Works
- 4-phase architecture: external knowledge → document index → targeted extraction → Q&A layer
- Checkpoint at $50-100 before Phase 3 (prevents YouTube KB's "build first, use never" trap)
- A4 company summaries + inter-company relationship maps as output format
- Documents: store originals, read KNOWLEDGE-SUMMARY.md only (AI reads summaries, never originals)
- Progressive complexity: validate each phase before scaling
- Validated: Järvisydän pilot (sessions 33–44) proved 7-layer protocol across 5 entities

### What Fails
- Don't load all company documents into context (7MB+ per company)
- Don't skip external knowledge phase (websites + Patrick's knowledge first, cheapest)
- Don't proceed past Phase 2 without explicit checkpoint approval

### Model Strategy
- Sonnet: ALL corporate-knowledge work — Phase 0 research, inter-company analysis, document indexing, summary building, relationship mapping, financial analysis (Sonnet beats Opus on financial analysis)
- Opus: ONLY for cross-company legal/governance synthesis requiring multi-hop reasoning (GPQA-level)
- Haiku: Metadata extraction from document headers (titles, dates, parties)

### Cost Benchmark
- Phase 0 research: $15-25 (orchestrated Opus in claude.ai)
- Phase 1-2 document indexing: $5-15 (Sonnet + Haiku)
- Phase 3 deep extraction: $50-100 (CHECKPOINT REQUIRED)

### Required Reads (load at session start — not optional)
- `bp: company-intelligence-protocol.md` — 7-layer framework; always governs "learn a company" session sequencing

### Knowledge Triggers
<!-- Planning mode: focus on breadth triggers (alternatives, risks). Execution mode: focus on precision triggers (constraints, costs, steps). -->
- Second Brain has 5 portable layers: capture → process → store → retrieve → reason → Build every company knowledge hub on this architecture (topics/knowledge-rag.md)
- Memory advantage compounds over 10-20 years — structured > random accumulation → Start now, imperfect is fine, late starters can't recover (topics/knowledge-rag.md)
- Vendor-neutral formats prevent lock-in — markdown with export mechanisms → Keep everything in .md with clear metadata (topics/knowledge-rag.md)
- Every company knowledge hub needs a 5-15K token index document before deep extraction begins → Compress first, don't skip to Q&A layer (bp: knowledge-base-indexing.md, 33KB)
- Audit data currency before making anything AI-searchable — stale knowledge is worse than no knowledge → Check document dates and flag anything >2 years old for review (bp: RAG-BEST-PRACTICES.md, 52KB)
- Dual-project-output: Mining sessions produce both Zone A files (working) and Zone B-ready files (flat, SharePoint-synced) → Plan output format before extraction, not after (bp: two-zone-architecture.md)
- Mid-session-checkpoint: Save intermediate results to files at natural breakpoints in sessions >30 minutes → Prevents total loss on crash or context-out (bp: mid-session-checkpoint.md)
- Mining-output-transfer: Paste mining output blocks directly in VS Code, not Claude Code context → Avoids double-context waste; Code should read files, not receive pasted content (bp: mining-output-transfer.md, source: patrick)
- Session compaction: corporate-knowledge sessions run long (multiple Excel files, board minutes, tilinpäätös). Use /compact after each phase → saves ~47%; all analysis already in .md files (bp: session-compaction-strategy.md)
- Session Bridge: at 100K-150K tokens → soft warning, suggest Bridge. At 140K → hard stop, trigger Session-Bridge Protocol (harvest → Cognitive Snapshot → prompt-creator --bridge → genius-check --mode bridge → new session). Do NOT /compact above 120K. (bp: session-bridge-protocol.md)
- Pre-distill before subagents: for large datasets (Excel 16K columns, 400-row email threads), pre-distill to focused extract BEFORE spawning subagents → prevents context overwhelm in subagent (bp: agent-orchestration-patterns.md)
- Company intelligence protocol: 7 layers in order (Identity→Documents→Governance→Financial History→Forecast→Operations→People→Synthesis). Always do Layer 1 document inventory before extracting anything. Gate at Layer 5 (costs $10-30, Patrick approval required) → Load when starting any "learn a company" session (bp: company-intelligence-protocol.md)
- Never skip source material in multi-agent analysis — distill instead. $0.50 skip savings propagates incomplete analysis downstream (Tier A rule, source: patrick)
- Self-check capability matching: when designing agent self-checks, measure things agents can actually assess. Token counts = fiction. Context load scale (light/medium/heavy) = honest. (session 47 pattern)
- Pre-brief reduces corrections: when mining external sources (Substack, YouTube, market reports) for any company knowledge session, add a 5-line company context brief at session start → prevents costly mid-session correction rounds (bp: pre-brief-reduces-corrections.md, source: patrick)
- Lead Agent quality gate: for any multi-step subagent task, run structured intake first — Goal + Done criteria + Tier + Constraints + Output format + Escalation trigger. Same-model red-teaming = hallucination consensus. (bp: lead-agent-quality-gate.md, session 71)
- Multi-model validation: before spawning build agents on security-sensitive design, run Grok Heavy + Gemini adversarial → catches architectural gaps pre-commit. (bp: multi-model-architecture-validation.md, session 78)

- Cold Start Discovery Mode: before any file reads in a new session, ask 3 strategic questions (Purpose / Business Goal / Definition of Done) → lock as Session DNA → then load context. User intent frames which files to load, not vice versa. (bp: cold-start-discovery-mode.md, session 92)

### Deep Dive (load on demand)
- "How should I architect the company knowledge system?" → `topics/knowledge-rag.md` (95 insights, ~100KB)
- "How do I design organizational knowledge sharing?" → `topics/leadership-org.md` (125 insights, ~40KB)
- "Which topic file covers my current question?" → `_topic-index.md` (2KB routing index)
- "How do I build the company knowledge index?" → `bp: knowledge-base-indexing.md` (33KB)
- "How do I validate retrieval quality or data freshness?" → `bp: RAG-BEST-PRACTICES.md` (52KB)
- "What are the document storage standards across companies?" → `bp: document-architecture.md` (14KB)
- "Choosing between subagents / Agent Teams / n8n?" → `bp: agent-orchestration-patterns.md` (orchestration decision guide)

---

## crm-build | CRM & Agentic Pipeline Build
<!-- last_curated: 2026-03-17 -->

### What Works
- Wave architecture: each wave = spawn prompt + quality gate + acceptance criteria → never build open-ended
- Planner-Worker-Judge loop: spawner sets ACCEPTANCE CRITERIA, judge red-teams output, max 3 rounds
- Git worktrees (7) for parallel wave development — no branch conflicts
- Supabase shared pooler for n8n.cloud (IPv4-only issue solved: shared pooler port 6543, Ignore SSL ON)
- Multi-model validation before build: Grok Heavy (2 rounds) + Gemini (1 adversarial round) before spawning — catches security/GDPR gaps
- Build-state tracking: BUILD-STATE.md in FinnConcierge repo, updated every session
- Verified live against Supabase (SQL query), not just file existence — prevents phantom-complete gates

### What Fails
- Worker accuracy 33% on meta-analysis (2/6 findings real) — always verify Worker findings independently
- File existence ≠ gate complete — Worker marks gates ✅ based on files, not live DB state. Run SQL to verify.
- Same-model red-teaming = hallucination consensus — use structured ACCEPTANCE CRITERIA, not "review for quality"
- Pre-loading Grok prompts with expected verdicts = validation theater — open question format only
- n8n.cloud is IPv4-only: Supabase direct and dedicated pooler are IPv6 → use shared pooler only

### Model Strategy
- Sonnet: ALL build work — schema, migrations, spawn prompts, code review, quality gates
- Opus: NOT needed for CRM build (Sonnet beats Opus on coding 79.6% vs 80.8%, same quality 5× cheaper)
- Haiku: NOT needed (judgment work throughout)

### Cost Benchmark
- Full CRM build (~10 waves): estimated $50-100 (mostly Claude Code agent sessions)
- Multi-model validation: ~$3-5 per round (Grok free + Claude subagents ~$0.50 each)

### Required Reads (load at session start — not optional)
- `~/Desktop/FinnConcierge/BUILD-STATE.md` — current wave status + all Patrick actions
- `bp: agentic-pipeline-security.md` — 11 constitutional principles; load before ANY wave that processes external input

### Knowledge Triggers
- Lead Agent quality gate: for any Tier 2/3 build task, run structured intake BEFORE starting — Goal + Done criteria + Tier + Constraints + Output format + Escalation trigger. Same-model red-teaming = hallucination consensus — use checklist. (bp: lead-agent-quality-gate.md, session 71)
- Planner-Worker-Judge empirical data: Worker accuracy 33% on meta-analysis, 100% on deliverable. File manifest prevents false "file missing" claims. HIGH-severity findings need independent verification. (bp: planner-worker-judge-loop.md, session 74)
- Cohort prediction over individual: N<5 = ~57% accuracy = coin flip. Three tiers: cohort_strong/individual_ok/suppressed. Suppressed NEVER surfaces. Apply to any CRM signal, recommendation, or prediction. (bp: cohort-vs-individual-prediction.md, source: patrick D51)
- Multi-model validation before build: run Grok Heavy + Gemini adversarial round before spawning any security-sensitive build agent. Prevents architectural mistakes that are expensive to undo. (bp: multi-model-architecture-validation.md, session 78)
- Agentic coding patterns: Sub-Boss pattern lifts quality 65→92% on complex agents; Judge Agent catches 7× more errors than human review. Load before designing any complex agentic build. (bp: agentic-coding-patterns.md, session 56)
- Coding project preflight: 9-phase checklist — correctness definition, PRD brain files, architecture choice, team composition, quality gates, error recovery, prompt rules, cost, anti-patterns. Run before committing to wave architecture. (bp: coding-project-preflight.md, session 56)
- Verifiability spectrum: classify each gate — Tier 1 (machine-checkable via SQL), Tier 2 (expert-checkable with criteria), Tier 3 (judgment). Most CRM quality gates are Tier 1 or 2. Define acceptance criteria upfront. (bp: nate-ai-verifiability-spectrum.md, session 71)
- Deliverable from 2+ source files → use /pwj before spawning any subagent. Run 6-question intake first. For CRM builds: Standard criticality (cap=5), cross-family Grok Judge mandatory. Do NOT spawn Wave workers without PWJ intake. (skill: ~/.claude/skills/pwj/SKILL.md, Grok-validated 2026-03-17)
- Security first: agentic pipeline security 11 principles — input sanitization, RLS on all tables, credential isolation, volume protection, prompt injection defense. Load before any wave that processes email/external input. (bp: agentic-pipeline-security.md, session 78)
- GEPA correction loop (mandatory session-end): if Patrick made ANY correction this session → run gepa-correction-harvest → propose rule → add to _index.yaml. (bp: gepa-correction-harvest.md)
- Session compaction: CRM build sessions load BUILD-STATE.md + spawn prompts + schema files. Use /compact after initial audit, before making changes. Saves ~47%. (bp: session-compaction-strategy.md)
- Session Bridge: at 100K-150K tokens → soft warning, suggest Bridge. At 140K → hard stop, trigger Session-Bridge Protocol (harvest → Cognitive Snapshot → prompt-creator --bridge → genius-check --mode bridge → new session). Do NOT /compact above 120K. (bp: session-bridge-protocol.md)

- Cold Start Discovery Mode: before any file reads in a new session, ask 3 strategic questions (Purpose / Business Goal / Definition of Done) → lock as Session DNA → then load context. User intent frames which files to load, not vice versa. (bp: cold-start-discovery-mode.md, session 92)

### Deep Dive (load on demand)
- "What are the wave spawn prompts?" → `~/Desktop/FinnConcierge/orchestration/WAVE-BUILD-AGENTS.md`
- "What decisions have been locked?" → `~/Desktop/FinnConcierge/DECISIONS.md`
- "What's the full schema?" → `~/Desktop/FinnConcierge/docs/SECOND-BRAIN-ERP-CRM-v2.md` (19 sections)
- "What are the security requirements?" → `bp: agentic-pipeline-security.md`
- "How should I design the agent orchestration?" → `bp: agentic-coding-patterns.md` + `bp: agent-orchestration-patterns.md`

---

## system-maintenance | System Architecture & Maintenance
<!-- last_curated: 2026-03-17 -->

### What Works
- Context Pack auto-loading: compile at session END, load at session START (zero friction)
- Three-tier patterns: Tier A (CLAUDE.md) → Tier B (_shared/) → Tier C (_archive/)
- Compression every 5 sessions: one-liners + archive full text
- Opus designs, Sonnet maintains — $0.10/session vs $1.50/session
- Session counter in Meta block drives automated maintenance triggers

### What Fails
- Pre-Flight Checklist had ZERO activation in 7 days (search-based = friction = ignored)
- Root-level file accumulation (32 temporary files, 76% of root)
- ROADMAP.md grew to 1,475 lines when used for session logs (now fixed)
- Don't let system files exceed 300 lines (CURRENT-STATUS.md budget)

### Model Strategy
- Sonnet: ALL maintenance work (compression, archiving, context pack compilation, contradiction fixes, warm pack updates)
- Opus: ONLY for 10-session review (GPQA-level synthesis of session patterns across multiple sessions)
- Haiku: Never for system work (requires judgment about what to keep/archive)

### Cost Benchmark
- Annual maintenance: ~$25/year (Sonnet every session + Opus every 30)
- System review: $1-2 (Opus batch every 30 sessions)
- Context budget: CLAUDE.md 4KB + MEMORY.md 15KB + STATUS 25KB + warm pack 5KB = ~49KB (~6% of 200K)

### Required Reads (load at session start — not optional)
- `bp: self-maintaining-knowledge-system.md` — full system design doc; governs all architectural decisions

### Knowledge Triggers
<!-- Planning mode: focus on breadth triggers (alternatives, risks). Execution mode: focus on precision triggers (constraints, costs, steps). -->
- Architecture is bottleneck when swapping models produces no improvement → Test with different models to diagnose constraints (topics/prompting-context.md)
- Stable prefix + variable suffix enables 10x cache improvement → Keep CLAUDE.md/MEMORY.md stable, session context variable (topics/prompting-context.md)
- Four-tier memory mirrors computer architecture: cache/RAM/disk/artifact → Working context minimal, session logs complete, long-term searchable (topics/prompting-context.md)
- Activation gap: documented patterns ≠ activated patterns — if it matters, auto-load it → Measure actual usage, not existence; archive what doesn't fire (bp: self-maintaining-knowledge-system.md, 24KB)
- Subagent decision threshold: <3 tool calls = do in main session; 3+ calls or multi-file reads = spin up subagent → Don't over-delegate simple tasks, don't under-delegate complex ones (bp: claude-code-orchestration.md, 13KB)
- Session compaction: system-maintenance sessions read many files (warm-packs, _index.yaml, CLAUDE.md, multiple BP files). Use /compact after initial audit, before making changes → saves significant cost (bp: session-compaction-strategy.md)
- Session Bridge: at 100K-150K tokens → soft warning, suggest Bridge. At 140K → hard stop, trigger Session-Bridge Protocol (harvest → Cognitive Snapshot → prompt-creator --bridge → genius-check --mode bridge → new session). Do NOT /compact above 120K. (bp: session-bridge-protocol.md)
- KB worth consulting? → Tier 1 = clear KB topic match, load first. Tier 2 = partial match, grep first. Tier 3 = unique domain, skip KB. Never load topic files >100KB without confirming relevance first.
- GEPA correction loop (mandatory session-end): if Patrick made ANY correction this session → run gepa-correction-harvest.md → propose rule → add to _index.yaml. Corrections are highest-signal input. (bp: gepa-correction-harvest.md)
- Cross-skill upgrade pattern: when a skill underperforms, use /grok-spar Research Debate to stress-test it → fact-check Grok claims via WebSearch → upgrade with verified changes only (bp: cross-skill-upgrade-via-grok-spar.md, session 66)
- Lead Agent quality gate: for any complex multi-step task (Tier 2/3), run structured intake BEFORE starting — 6 questions: Goal + Done criteria + Tier + Constraints + Output format + Escalation trigger. Then run autonomously to done-criteria. Critical: same-model red-teaming = hallucination consensus — always use structured ACCEPTANCE CRITERIA checklist. (bp: lead-agent-quality-gate.md, session 71)
- Verifiability spectrum: classify work before delegating — Tier 1 (machine-checkable), Tier 2 (expert-checkable with criteria), Tier 3 (genuine judgment). Most work that seems Tier 3 is actually Tier 2 if criteria defined upfront. (bp: nate-ai-verifiability-spectrum.md, session 71)
- PWJ theater: same-model Judge = guaranteed PASS (hallucination consensus). External model mandatory for verification: Grok Step 3.5 OR Mistral Step 5. (bp: pwj-theater-vs-real-execution.md, session 89)
- Compression measurement blindness: before compressing sessions to one-liners, write compact YAML summary (kb, harvest, cost, tier, value) to preserve Opus Review metrics. Without this, 50% data loss per compression cycle. (bp: compression-induced-measurement-blindness.md, session 92)
- Session Bridge threshold (updated session 95): 140K = hard stop (not 170K). 180K = FORCE bridge. Matches session-bridge-protocol.md spec.

- Cold Start Discovery Mode: before any file reads in a new session, ask 3 strategic questions (Purpose / Business Goal / Definition of Done) → lock as Session DNA → then load context. User intent frames which files to load, not vice versa. (bp: cold-start-discovery-mode.md, session 92)

### Deep Dive (load on demand)
- "How do I optimize system prompts or context architecture?" → `topics/prompting-context.md` (114 insights, ~119KB)
- "Which model should I use for this task?" → `topics/models-capabilities.md` (95 insights, ~35KB)
- "Which topic file covers my current question?" → `_topic-index.md` (2KB routing index)
- "How should I review system architecture or maintenance protocols?" → `bp: self-maintaining-knowledge-system.md` (24KB)
- "How do I optimize subagent usage or tool delegation?" → `bp: claude-code-orchestration.md` (13KB)
- "Is there a context window issue I need to debug?" → `bp: context-window-failure-modes.md` (7KB)
