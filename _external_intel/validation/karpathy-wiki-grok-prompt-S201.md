---
type: external-spar-prompt
format: T3_ADVERSARIAL_JUDGE
date: 2026-04-13
session: S201
topic: Karpathy LLM Wiki — Second Brain fit analysis for 3 contexts
target: Grok Auto/Expert
ready_to_paste: true
---

# T3: ADVERSARIAL_JUDGE — Karpathy LLM Wiki Second Brain Fit

## Role Assignment

You are an expert adversarial reviewer with deep experience in knowledge management systems, RAG architectures, and enterprise AI deployment. Your job is to attack the weakest assumptions in this analysis — NOT to validate it.

Be brutal. Find the hidden failure modes. Rate fit honestly.

---

## Context

Patrick Heiskanen runs 1658 Holdings Oy (10 portfolio companies, ~50 employees, Finland). He is evaluating whether to adopt the **Karpathy LLM Wiki pattern** (published April 3 2026) as a Second Brain layer across three distinct contexts:

**Architecture under consideration:**
- Three-layer stack: `raw/` (immutable sources) → `wiki/` (LLM-maintained markdown pages) → `CLAUDE.md` (schema/rules)
- Core claim: LLM Wiki beats RAG for corpora under ~50-100K tokens (index-based lookup sufficient, synthesis paid once at ingest vs. every query)
- Current stack: CLAUDE.md (271 lines, battle-tested) + 136 BP files in `_shared/best-practices/` + MEMORY.md + Obsidian (2 vaults) + ChromaDB (Riikka headhunter pipeline)
- The analysis claims Patrick is "60-70% of the way there already" — gap is structural formalization, not a rebuild

**Key tool being evaluated:** `Pratiyush/llm-wiki` (MCP server, 7 tools, Claude Code adapter, 472 tests)

---

## Three Contexts to Attack

### Context A — Full Portfolio (Holdings KB)
- 10 operating companies, ~50 employees
- Obsidian + Supabase 4-layer stack (K1 Obsidian → K2 Supabase SoT → K3 Power BI → K4 Git)
- 136 BP files currently in `_shared/best-practices/`
- Claude Code sessions run by Patrick only (single user on Zone A)
- The analysis recommends: migrate BP files to `wiki/concepts/`, create `index.md`, install Pratiyush MCP

**Attack these 3 assumptions:**
1. "136 BP files = wiki layer — just add index.md and you're done." Is this structurally sound, or does the BP file format conflict with Karpathy wiki page semantics (entity-centric vs. pattern-centric)?
2. "Patrick is a single user so no concurrent edit conflicts." Is this true given Claude Code + Claude Desktop + potential future cron agents all writing to the same wiki directory?
3. "LLM Wiki is 57% cheaper than RAG at this scale." Does this cost analysis hold if the query pattern is not "find pre-synthesized answer" but "cross-reference 10 BP files to answer a novel question" — which is the actual Holdings use case?

**Fit rating (1-10):** ___
**Reasoning:** ___

---

### Context B — Finland DMC B2B CRM
- <200 B2B customers (tour operators, travel agencies, DMC partners)
- Current stack: Excel + Obsidian MVP (deliberately avoiding SaaS CRM)
- Active projects: Arctic FAM trip 2026 (40-80 operators), group sales pipeline
- B2B relationship depth: each partner has 3-5 years of meeting notes, contracts, pricing history
- The analysis did NOT specifically address this context — this is a gap

**Attack these 3 assumptions:**
1. "LLM Wiki works for B2B CRM entity pages." A CRM requires structured fields (last contact date, deal stage, contract value). Wiki markdown is freeform. Does the Karpathy pattern degrade to a glorified notes folder for CRM use, lacking the structured queries that make a CRM useful?
2. "Excel + Obsidian MVP is sufficient for <200 customers." At what point does the combination of LLM Wiki + Excel become MORE complex than a simple structured DB (e.g., Supabase), and has that point already been reached with an active 40-80 partner FAM pipeline?
3. "Partner relationship knowledge compounds in wiki." Is this realistic for B2B relationships where the critical knowledge is events + dates + commitments (calendar-dependent), not concepts? Does wiki synthesis miss the temporal dimension that makes CRM valuable?

**Fit rating (1-10):** ___
**Reasoning:** ___

---

### Context C — Riikka Headhunter AI Pipeline
- Active Python pipeline: `ai_filter_v4.py` + ChromaDB + Telegram (InlineKeyboardMarkup)
- Corpus: candidate profiles + employer KB (estimated 100-200 leads, growing)
- Current query pattern: semantic similarity search over candidate profiles
- The analysis recommends: replace or layer over ChromaDB with LLM Wiki, citing "smaller corpus fits in index"
- Critical: this is a live system, Riikka is non-technical, Patrick is the sole maintainer

**Attack these 3 assumptions:**
1. "100-200 leads comfortably fits in 50-100K token index." This assumes each lead page is ~250-500 tokens. A real headhunter profile with LinkedIn data, interview notes, employer match scoring, and follow-up history is 1,000-3,000 tokens per lead. At 200 leads × 2,000 tokens = 400K tokens — well above the threshold. Does the "fits in context" claim collapse at realistic data density?
2. "ChromaDB can be replaced with LLM Wiki for semantic search." Headhunter use case requires semantic similarity (find candidates similar to this profile, find employers matching these criteria) — this is a vector search problem, not a wiki lookup problem. Does replacing ChromaDB with markdown pages fundamentally break the core query type?
3. "Adding a wiki layer on top of ChromaDB reduces complexity." The pipeline already has ai_filter_v4.py complexity. Adding a parallel wiki layer (with its own ingest, lint, index) doubles the maintenance surface. For a non-technical end user (Riikka) and a sole maintainer (Patrick), is this a net complexity gain that creates fragility rather than resilience?

**Fit rating (1-10):** ___
**Reasoning:** ___

---

## Cross-Context Attack

All three contexts share one assumption worth attacking globally:

**"The Karpathy pattern is mature enough for production in April 2026."**

The original Gist was published April 3 2026 — 9 days before this analysis was written. Community implementations (Pratiyush/llm-wiki, MehmetGoekce/llm-wiki) are days old. The 472 tests in Pratiyush/llm-wiki sound impressive, but what is the actual production track record?

- Is adopting a 9-day-old community framework for knowledge management of a 10-company portfolio prudent?
- What is the blast radius if Pratiyush/llm-wiki introduces a breaking change or goes abandoned in 30 days?
- Should Patrick wait 90 days for the pattern to stabilize before migrating 136 battle-tested BP files?

---

## Output Format Required

For each context (A, B, C):
1. **Three attack verdicts** — is the assumption valid, partially valid, or false? Why?
2. **Fit rating (1-10)** with one sentence justification
3. **Biggest hidden risk** not covered in the original analysis

Then:
4. **Cross-context verdict** on the maturity assumption
5. **Top 3 recommended changes** to the adoption plan based on your attack findings
6. **Overall portfolio fit (1-10)** — is this worth Patrick's time right now?

Be direct. No hedging. If the analysis has a fatal flaw, say so.
