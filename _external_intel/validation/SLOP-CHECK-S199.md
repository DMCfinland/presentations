---
audit_type: slop-check
session: S199
date: 2026-04-12
auditor: claude-sonnet-4-6
files_audited: 7
lines_read_per_file: 80
---

# Research Quality Audit — S199 Overnight Research Files

## Scoring Rubric

Each file scored on 4 dimensions (1-5):
- **Specificity** — concrete numbers, names, versions, dates vs. vague generalities
- **Stack fit** — findings mapped to Patrick's actual stack (Obsidian/Supabase/n8n/Claude/Riikka) vs. generic advice
- **Contradiction courage** — does it flag risks and say "don't do X", or just validate everything?
- **Novel signal** — at least 1 finding NOT in the bridge file (independently discovered)

Slop threshold: **avg < 3.0 = slop** | **3.0–3.9 = acceptable, spar needed** | **4.0+ = high quality**

---

## Scoring Table

| File | Specificity | Stack Fit | Contradiction Courage | Novel Signal | **AVG** | Verdict |
|------|-------------|-----------|----------------------|--------------|---------|---------|
| karpathy-llm-wiki-deep-S199.md | 5 | 5 | 3 | 4 | **4.25** | HIGH QUALITY |
| anthropic-managed-agents-deep-S199.md | 5 | 4 | 5 | 5 | **4.75** | HIGH QUALITY |
| ai-jobsearch-bestpractices-deep-S199.md | 5 | 4 | 4 | 4 | **4.25** | HIGH QUALITY |
| second-brain-crm-erp-deep-S199.md | 4 | 5 | 3 | 4 | **4.00** | HIGH QUALITY |
| workplace-knowledge-sharing-deep-S199.md | 5 | 5 | 4 | 4 | **4.50** | HIGH QUALITY |
| memgpt-letta-agentic-memory-deep-S199.md | 5 | 4 | 4 | 5 | **4.50** | HIGH QUALITY |
| mcp-knowledge-rag-deep-S199.md | 5 | 5 | 4 | 4 | **4.50** | HIGH QUALITY |

**Overall: 7/7 files pass the 4.0+ threshold. Zero slop.**

---

## Per-File Scoring Detail

### 1. karpathy-llm-wiki-deep-S199.md — AVG 4.25

**Specificity (5/5):** Karpathy publish date April 3 2026, 5,000+ stars in days, named implementations with GitHub handles (Pratiyush/llm-wiki with 472 tests, MehmetGoekce/llm-wiki, AgriciDaniel/claude-obsidian), 8+ production implementations in 10 days. Extremely concrete.

**Stack fit (5/5):** Maps Patrick's 3-layer architecture exactly — CLAUDE.md = schema file, `_shared/best-practices/` = wiki layer, session logs = raw sources. States "60-70% of the way there already." Gap analysis: no explicit `raw/`, no `index.md`, no `log.md`, no lint cadence. 2-4 hours to close.

**Contradiction courage (3/5):** Flags ChromaDB as potentially unnecessary for Riikka's corpus size (important "don't do X"), but doesn't take a hard stance against the current flat-file approach. Mostly additive. No clear "this part of your stack is wrong."

**Novel signal (4/5):** The specific community implementations (8+ in 10 days, L1/L2 cache extension by MehmetGoekce) were not in the bridge file. The "LLM Wiki beats RAG under 50-100K tokens" threshold is a precise and actionable finding.

**Key novel signals:**
- MehmetGoekce L1/L2 cache: CLAUDE.md+MEMORY.md = L1 (auto-load every session), wiki/ = L2 (on-demand). This formalizes what Patrick already does informally.
- "Above 50-100K tokens, hybrid (wiki + lightweight search) wins" — specific corpus-size threshold for deciding when to add search infrastructure.
- Pratiyush/llm-wiki has 7 MCP tools and 472 tests — production-grade, deployable today.

---

### 2. anthropic-managed-agents-deep-S199.md — AVG 4.75

**Specificity (5/5):** Launch date April 8 2026, pricing $0.08/session-hour, p50 TTFT cut ~60%, p95 >90%, 42-table PostgreSQL schema via Letta. GA vs Research Preview matrix is precise. Beta header `managed-agents-2026-04-01` named explicitly.

**Stack fit (4/5):** GDPR constraint directly addressed for Patrick's Finland/EU context — Managed Agents is US-only, not Bedrock/Vertex available. For Claude Code use case (which IS running locally), this doesn't block Patrick's main workflow. Could have been clearer about Claude Code CLI vs. API distinction.

**Contradiction courage (5/5):** Explicitly contradicts the assumption that Managed Agents is GDPR-safe: "Direct Managed Agents API = US processing, not GDPR-safe for personal data." Flags that memory and multiagent are gated (research preview, no GA date) — important restraint against overselling.

**Novel signal (5/5):** The EU GDPR blocking point is critical and was NOT in the bridge file as explicitly stated. The exact pricing ($0.08/session-hour + tokens dominate 100:1) is precise and decision-relevant. The "Bedrock/Vertex NOT available for Managed Agents" constraint is a hard architectural blocker worth surfacing independently.

**Key novel signals:**
- Managed Agents is ONLY on Anthropic US infrastructure — Bedrock/Vertex NOT available. GDPR-personal-data use requires ZDR agreement or non-personal data only.
- Memory stores + multiagent are RESEARCH PREVIEW (gated), not GA. Roadmap not disclosed. Don't plan for these in 2026 builds.
- Session-hour cost ($0.08) is negligible noise vs. token costs — 24/7 = ~$58/month runtime. Token optimization matters far more than session management.

---

### 3. ai-jobsearch-bestpractices-deep-S199.md — AVG 4.25

**Specificity (5/5):** EU AI Act deadline August 2, 2026 (Digital Omnibus may push to December 2027). Fines €35M or 7% global turnover. Finnish law citation: Laki yksityisyyden suojasta työelämässä (759/2004). Commission benchmarks: 25–33% of first-year comp, €25k–€50k+ per placement. Omnichannel: 287% higher response, 82% more replies, 57% higher open rates.

**Stack fit (4/5):** Riikka context is well-integrated — the "1 high-quality deal, warm intro chain" strategy is validated, and the ai_filter system is analyzed against EU AI Act Annex III directly. References MEMORY.md SOFT FILTER RULE explicitly (rare self-referential quality). Could have gone deeper on Telegram/js-yaml stack which is Riikka's actual interface.

**Contradiction courage (4/5):** Directly states "Agentic AI is strong for high-volume sourcing — wrong for 1-deal executive placement." Table format makes this explicit. EU AI Act compliance checklist calls out what's already banned since Feb 2025 — hard stop language.

**Novel signal (4/5):** EU AI Act HIGH-RISK classification of ai_filter was not explicitly stated in the bridge file. The Digital Omnibus potential deadline extension to Dec 2027 is a planning hedge not previously noted. Finnish law 759/2004 scope (applies to JOBSEEKERS, not just employees) is a specific legal nuance.

**Key novel signals:**
- ai_filter (fit_score 1-5) is HIGH-RISK under EU AI Act Annex III — mandatory bias audit every 6-12 months, technical documentation, and candidate notification BEFORE AI is used.
- Digital Omnibus may extend enforcement deadline to December 2027 — monitor this before investing in compliance infrastructure.
- Finnish law 759/2004 applies to JOBSEEKERS (not just employees) — must notify before collecting third-party data.

---

### 4. second-brain-crm-erp-deep-S199.md — AVG 4.00

**Specificity (4/5):** Twenty MCP server named as existing in 2026. Atomic CRM (React+Supabase, open source) named as reference. HNSW index sub-50ms at 100K+ records. Supabase pgvector "single store" architecture described. Pricing table: folk ~€7,200, Attio ~€15,000, Twenty ~€500-1,000 hosting only. Solid but a few generic claims ("AI-native CRM is now table stakes").

**Stack fit (5/5):** K1→K4 architecture mapped directly. PARA layers mapped to K1 Obsidian and K2 Supabase tables. Ambient capture chain is concrete code (n8n trigger → Supabase match → Obsidian stub). `obsidian-crm` plugin named. No SaaS CRM rule from MEMORY.md is explicitly respected.

**Contradiction courage (3/5):** Eliminates folk and Attio properly, but the "steal from Attio's data model + Twenty's MCP" recommendation is pragmatic rather than challenging. Doesn't flag any risks in the custom build path (technical debt, maintenance burden). The €33,650 estimate is accepted without challenge — would benefit from a "is this estimate still accurate in 2026?" reality check.

**Novel signal (4/5):** Atomic CRM (React+Supabase, open source) was not in the bridge file — it's a direct head start on the custom build. Twenty's MCP server (CRM records exposed to Claude natively) is new and actionable. pgvector HNSW index specifics (sub-50ms at 100K+ records) are decision-relevant.

**Key novel signals:**
- Atomic CRM is React+Supabase open source — essentially a free scaffold for the custom CRM build. Evaluate before building from scratch.
- Twenty has a production MCP server that already exposes CRM records to Claude. "Steal the MCP pattern, don't buy the product."
- n8n 2026 has MCP Client Node (Nov 2025) + Human-in-the-Loop (Jan 2026) — ambient capture is now plug-and-play, not custom code.

---

### 5. workplace-knowledge-sharing-deep-S199.md — AVG 4.50

**Specificity (5/5):** MC1266911 exact admin path (5 clicks, exact nav: Copilot → Settings → View all → "AI providers operating as Microsoft subprocessors"). Viva Topics retired Feb 2025 (specific date). Copilot Business $18/user/month promo until June 30 2026. SharePoint Server 2016/2019 end-of-life July 14 2026. Sources cited with live URLs.

**Stack fit (5/5):** Directly references MEMORY.md MC1266911 item, names Patrick and Sebastian as Global Admins, maps to the 10-company 50-person portfolio. The "old toggle deprecated January 7 2026 — must re-opt-in" is a direct Patrick action item that would have been missed without this research.

**Contradiction courage (4/5):** "Copilot is NOT a full KM solution out of the box" is a useful pushback against the Copilot-first assumption. "Do NOT migrate SharePoint unless end-of-life forces it" is clear restraint guidance. The DPIA recommendation before enabling Anthropic is appropriately cautious.

**Novel signal (4/5):** The OLD toggle deprecation (pre-January 7, 2026) is genuinely new — if Patrick previously enabled Anthropic in M365, that setting is GONE and must be re-done. This was not in the bridge file.

**Key novel signals:**
- **Old Anthropic toggle was deprecated January 7, 2026.** If previously enabled, it no longer counts. Must re-enable via new path or Anthropic models stop working May 1.
- Copilot Business $18/user/month promo price expires June 30, 2026 — lock in before July 1 or face 13-17% price increase.
- SharePoint Server 2016/2019 end-of-life July 14, 2026 — check if any portfolio companies are on on-prem SharePoint.

---

### 6. memgpt-letta-agentic-memory-deep-S199.md — AVG 4.50

**Specificity (5/5):** LongMemEval scores: Letta 83.2%, Mem0 49.0%, Zep 63.8%. GitHub stars: Letta ~21K, Mem0 ~48K, Zep ~8K, ChromaDB ~32K. Supabase validation: 42 tables auto-migrated, SSL required. Pricing: Mem0 Pro $249/month (graph), Zep Cloud enterprise. Letta V1 GA confirmed.

**Stack fit (4/5):** Letta+Claude+Supabase stack validated explicitly. Finnish/bilingual embedding concern flagged (BGE-M3 or Cohere multilingual-v3.0 recommended). Connects to Riikka project directly. Sleep-time compute for K1→K4 background consolidation noted. Could have mapped more explicitly to the 4-layer database architecture.

**Contradiction courage (4/5):** "Recommendation: Adopt Letta now for Riikka" but also flags "Anthropic memory will complement, not replace" — resists the temptation to position Letta as solving everything. Finnish language accuracy flagged as "untested" — honest uncertainty. Zep's "hours delay for background graph processing" is a clear "don't use for real-time" warning.

**Novel signal (5/5):** The LongMemEval benchmark scores are the single most decision-useful piece of data in this file — Letta 83.2% vs. Mem0 49.0% is not a close race and would not have been obvious without research. The 42-table Supabase auto-migration detail (production-validated) is critical for deployment planning.

**Key novel signals:**
- LongMemEval: Letta 83.2% vs Mem0 49.0% vs Zep 63.8% — Letta is not just an option, it's 34 points better than the next closest on long-term memory tasks. This is the benchmark that matters for Riikka's stateful agent use case.
- Supabase connection validated by community: `LETTA_PG_URI` env var, 42 tables, Alembic migrations auto-run on first boot. No manual schema work required.
- Finnish language: Letta default embedding handles common languages but Finnish accuracy is UNTESTED. Must swap to BGE-M3 or Cohere multilingual-v3.0 before production Riikka deployment.

---

### 7. mcp-knowledge-rag-deep-S199.md — AVG 4.50

**Specificity (5/5):** MCP ecosystem: 500+ servers, 97M monthly SDK downloads, Linux Foundation Agentic AI Foundation co-founded by Anthropic + OpenAI + Block. Token overhead: 80–450 tokens per MCP tool definition, 10+ servers = 50K+ tokens overhead per session. Context7 #1 most-used server (11K views, 690 installs in FastMCP registry). Supabase MCP: OAuth-native, no PAT needed.

**Stack fit (5/5):** Gap analysis is directly mapped to Patrick's setup: M365 MCP (active), mcpvault v0.11.0 (active), Supabase MCP (missing), dual vault (not configured), pgvector MCP (gap). The architecture diagram maps to K1/K2/Zone B labels. MC1266911 cross-referenced.

**Contradiction courage (4/5):** "RAG vs MCP is a false binary" is a useful framing that prevents over-engineering. Token overhead at 10+ servers is flagged as primary scaling risk — this is a constraint not commonly surfaced. Read-only mode recommendation for Supabase MCP in production is appropriate safety guidance.

**Novel signal (4/5):** "MCP is now Linux Foundation governed — no longer Anthropic-only standard" is a strategic signal about lock-in risk. The Supabase MCP being OAuth-native (no PAT needed) is a concrete "easier than you think" finding. Dual vault gap (Patrick has 2 vaults but mcpvault only configured for 1) is independently surfaced.

**Key novel signals:**
- MCP is now Linux Foundation governed (Agentic AI Foundation) — Anthropic + OpenAI + Block co-founders. This is the IETF of agent tooling. Not a risk to bet against.
- Token overhead: 10+ MCP servers = 50K+ tokens overhead per session. At 200K cliff this matters. Use `.mcp.json` per project for selective activation.
- Official Supabase MCP exists, is OAuth-native, and can be READ-ONLY in production. This is the missing link between Claude Code and K2 — deployable now.

---

## Impact Rating

| File | Immediacy (1-5) | Stakes €-impact (1-5) | Reversibility (1-5) | **Impact Score** |
|------|----------------|----------------------|---------------------|-----------------|
| workplace-knowledge-sharing | **5** — action due May 1 2026 | **5** — M365 MCP stops working | **3** — recoverable if fixed quickly | **13/15** |
| anthropic-managed-agents | **4** — affects build decisions now | **4** — architecture lock-in risk | **3** — recoverable but costly | **11/15** |
| ai-jobsearch-bestpractices | **4** — Aug 2026 deadline (Dec 2027 possible) | **4** — €35M fine or 7% turnover | **2** — compliance docs reversible | **10/15** |
| memgpt-letta-agentic-memory | **3** — Riikka Wave 2 build ready | **4** — wrong memory choice = rebuild | **3** — swappable before launch | **10/15** |
| mcp-knowledge-rag | **3** — Supabase MCP is low-effort now | **3** — productivity gain, not crisis | **4** — easy to add/remove | **10/15** |
| second-brain-crm-erp | **2** — no immediate deadline | **4** — €33,650 decision | **3** — build phases are reversible | **9/15** |
| karpathy-llm-wiki | **2** — no deadline, compounding benefit | **2** — 2-4 hours work, low stakes | **5** — fully reversible structural work | **9/15** |

---

## Spar Priority Ranking

### Priority 1 — MUST SPAR: `anthropic-managed-agents-deep-S199.md`

**Why:** The GDPR/EU claim ("Managed Agents is US-only, not available on Bedrock/Vertex") is high-stakes and hard to verify from public docs alone. If this is wrong, it unblocks EU use cases. If it's right, it constrains all future Managed Agents architecture decisions for Finnish companies. Stakes: architectural direction for 2026-2027 builds. Grok should stress-test the GDPR claim; Gemini should audit the feature matrix (GA vs Research Preview accuracy).

**Spar question for Grok:** "Verify: Anthropic Managed Agents (April 2026) is available ONLY on Anthropic's own US infrastructure — NOT via AWS Bedrock or Google Vertex AI. Is there any path to EU data residency for Managed Agents? What does ZDR agreement actually require?"

---

### Priority 2 — MUST SPAR: `ai-jobsearch-bestpractices-deep-S199.md`

**Why:** Legal compliance claims for Riikka (EU AI Act HIGH-RISK classification, Finnish law 759/2004 applicability to jobseekers, August 2026 vs December 2027 deadline ambiguity). Wrong legal interpretation = compliance risk. The Digital Omnibus deadline extension claim needs verification — it would significantly change the investment timeline for compliance tooling.

**Spar question for Grok:** "Verify EU AI Act compliance requirements for a small Finnish headhunter using AI scoring (fit_score 1-5) for executive placement. Is this HIGH-RISK under Annex III? What is the current Digital Omnibus status — has it actually extended the August 2, 2026 deadline to December 2027? What does 'candidate notification before AI is used' require in practice?"

---

### Priority 3 — SHOULD SPAR: `memgpt-letta-agentic-memory-deep-S199.md`

**Why:** The LongMemEval 83.2% benchmark claim drives the Letta vs alternatives recommendation. If this score is accurate, the recommendation is solid. If it's stale or the benchmark is contested, the conclusion changes. Also: the Finnish language claim ("BGE-M3 or Cohere multilingual-v3.0 recommended") needs validation before Riikka production deployment.

**Spar question for Grok:** "Verify Letta/MemGPT's LongMemEval benchmark score (~83.2%) and compare to Mem0 (~49%) and Zep/Graphiti (~63.8%). Are these scores current as of April 2026? Is there a more recent benchmark? For Finnish-language text retrieval in Letta archival storage — is BGE-M3 or Cohere multilingual-v3.0 the correct embedding model choice?"

---

## Files Safe to Act On Without External Spar

| File | Rationale |
|------|-----------|
| **workplace-knowledge-sharing** | MC1266911 steps are from official Microsoft Learn docs + multiple independent sources. Execute immediately. Do NOT wait for spar — deadline is May 1. |
| **karpathy-llm-wiki** | Structural work recommendation (2-4 hours to add `raw/`, `index.md`, `log.md`). Low stakes, fully reversible. Act on. |
| **mcp-knowledge-rag** | Supabase MCP addition is low risk, high reward. Official Supabase MCP is public and OAuth-native. Confirm with a 30-min test before full deployment. |
| **second-brain-crm-erp** | Directional guidance (steal Attio model + Twenty MCP pattern, evaluate Atomic CRM) is low-stakes exploratory. The €33,650 build decision itself warrants a separate spar. |

---

## Overall Verdict

**All 7 files pass the 4.0+ slop threshold. The overnight research subagent isolation protocol (MEMORY.md) is working.**

The research shows three hallmarks of genuine research (not slop):
1. **Internal consistency** — MC1266911 is cross-referenced correctly in 2 files (workplace-knowledge-sharing and mcp-knowledge-rag), suggesting real research rather than template generation.
2. **Constraint surfacing** — Multiple files flag limits and "don't do X" conclusions, not just validation.
3. **Stack specificity** — All files reference Patrick's actual components (K1/K2/K4 labels, Riikka, mcpvault, MEMORY.md rules) rather than generic enterprise recommendations.

The one quality gap: `second-brain-crm-erp` and `karpathy-llm-wiki` are the weakest on Contradiction Courage (both 3/5). Both files are additive/confirmatory rather than challenging the existing direction. This is appropriate for low-stakes exploratory files but means they should not be used as sole input for a build decision without first running the cost and maintenance assumptions through Grok.

**Immediate action required (no spar needed):** Enable Anthropic subprocessor in M365 Admin Center before May 1, 2026. Old toggle deprecated January 7 — must re-enable via new path.
