# Grok 4.20 Debate Prompt — DMC-SECONDBRAIN-CRM D25–D33 Validation
**Version:** 2.0 | **Date:** 2026-03-12
**Purpose:** Paste entire PROMPT block below into Grok 4 (Heavy) to run native 4-agent debate.

---

## HOW TO RUN

1. Open grok.com → select **Grok 4 (Heavy)** (the multi-agent model)
2. Copy everything inside the `---PROMPT START---` / `---PROMPT END---` markers
3. Paste as your message — Grok will spawn 4 agents natively
4. When complete, paste the full output back to Claude Code

---

---PROMPT START---

You are Grok running a native 4-agent debate. Spawn four distinct agents with the identities and positions defined below. Each agent has full context of the project but argues from their own role and incentives. Let them debate naturally — cross-challenge each other, change position if persuaded, but maintain their core role bias throughout.

---

## WHAT IS BEING DEBATED

**Proposition:** Architectural decisions D25–D33 are sound, GDPR-compliant, and technically viable. The build (Wave 1A: schema migration) should start now.

**What is NOT being debated:** D1–D24 are already locked and validated by a prior Grok 4.20 4-agent debate. Do NOT relitigate those. Agents may reference them as context but may not challenge them.

---

## PROJECT CONTEXT (all agents have this)

**Project:** DMC-SECONDBRAIN-CRM — a custom AI-powered CRM for Finland DMC Oy, a 6-person destination management company (Helsinki). Built by Patrick Heiskanen (CEO) on top of FinnConcierge (existing Next.js + Supabase Turborepo monorepo). No external budget — internal build. 8-week MVP target.

**Stack:**
- Frontend: Next.js 15 App Router + shadcn/ui + Tailwind CSS v4 (existing FinnConcierge codebase)
- Database: Supabase PostgreSQL (eu-central-1, Frankfurt) — 9 existing tables, extending to 14
- Workflow: n8n self-hosted on Hetzner (8 existing workflows)
- Email: Microsoft Graph API → n8n → Triple-LLM pipeline → Supabase
- Capture: Microsoft Teams #crm-capture channel + Claude Code MCP write
- Vector search: pgvector (Supabase) + OpenAI text-embedding-3-small (1,536 dimensions)
- Staff auth: Supabase JWT with role claims (already decided, D13)
- Traveler auth (B2C): D25 below — separate from staff auth

**Scale:** 107 active clients, 393 proposals/year, €5.87M revenue. AHI Travel = 75% revenue concentration (CRITICAL account). Staff: Liisa, Laura, Reeta, Sebastian, Piia, Janna (Head of Sales).

**GDPR context:** Finland (EU). Finnish Data Protection Authority (Tietosuojavaltuutettu) — known to be aggressive on automated profiling. eu-central-1 Frankfurt data residency already in place (D11). DPIA (Art. 35) is already a locked requirement before live email mining (D9 — do not debate this).

**Existing Supabase tables (do NOT break):** Tenants, Users, Providers, Contracts, Itinerary, Shadow_Ledger, Products, Sessions_Archive, Alerts. CRM adds 5 new tables: deals, deal_activities, deal_stage_history, suppliers, rate_cards.

---

## WHAT THE PRIOR GROK DEBATE ALREADY RESOLVED (D1–D24)

These issues were raised and resolved in the first validation. Do NOT re-raise them:

- **Triple-LLM pipeline already required** (Quarantined → Validator → Privileged). Added as a required change after the prior debate. Already in Wave 2 scope.
- **DPIA already required** before any live email mining (D9, locked). Not in debate.
- **RLS deny-by-default already required** — ai_reader/ai_writer roles, no service_role in agents (D8, locked).
- **All AI-enriched records status: unverified** until human staff reviews (already in design).
- **Finnish DPA aggressiveness already flagged** — one DPIA gap = enforcement. Already acknowledged.
- **Context rot mitigations already incorporated** — BUILD-STATE.md, PreCompact hooks, weekly coherence sync, git worktrees per module.
- **8-week timeline already adjusted** (was 6 weeks, extended after prior debate).
- **Custom build over Pipedrive already decided** (D1, unanimous in prior debate). Pipedrive was formally rejected.
- **FinnConcierge B2C deferred** until CRM is working (D17). FinnConcierge and CRM are architecturally separate (D14, D15).
- **GDPR columns already required on all new tables** — mined_at, retention_policy_days, created_by_ai_pipeline, tenant_id (D19, locked).
- **Staff auth already decided** — Supabase JWT with role claims (D13). NOT magic link. D25 below is traveler (B2C) auth only.

---

## THE 9 DECISIONS BEING DEBATED (D25–D33)

**D25: FinnConcierge traveler auth = magic link only (B2C travelers, not staff)**
Note: Staff auth is already settled as Supabase JWT (D13). This decision is for the deferred B2C traveler PWA (FinnConcierge) — occasional mobile users, not daily work tool.
Rationale: Passwordless, zero friction for mobile B2C users, no password management overhead. Google social as optional second path.
Concern to debate: 15-min OTP expiry — traveler on a hiking trip gets email, can't click for 20 min. Also: is this worth locking now when FinnConcierge B2C is deferred (D17)?

**D26: Wave 3A cost ceiling = $8 (one-time exception for Kanban UI wave)**
Rationale: Wave 3A installs @dnd-kit + TanStack + builds full drag-drop Kanban + Supabase Realtime. Legitimately exceeds $5 standard cap. All other waves stay at $5.
Prior incident cited: GetOnStack undetected agent loop → $47K over 4 weeks. Hence all caps.
Concern to debate: Does setting a one-time $8 exception establish a precedent that undermines the cap system entirely?

**D27: Booking reference format = FDM-[6-char alphanumeric], server-side generated**
Rationale: Unguessable (IDOR-safe), human-readable (can dictate by phone), short. Maps internally to deal_id UUID. UUID never exposed externally.
Concern to debate: None community-raised. Debate on merits — is 6 chars sufficient entropy? Any format clashes with TravelTree's own reference format?

**D28: Knowledge capture = Microsoft Teams #crm-capture channel**
Rationale: Teams already open on every staff screen. Zero new tool adoption. Staff posts with prefixes: `decision:` / `person:` / `insight:` / `meeting:`. Teams webhook → n8n → Supabase Edge Function → embedding → deal_embeddings.
Technical issue already identified: Teams webhook retries if n8n response > 3 seconds → duplicate embedding rows. Fix requires: (1) return 200 immediately, (2) process async, (3) unique index on teams_message_id. Must be in Wave 2A scope.
Also: Raw Teams message text includes `<@U12345>` mentions, `<https://url|label>` links, `:emoji:` codes — all poison embedding quality. Strip markup before embedding call.
Concern to debate: Is Teams capture channel sufficient, or will staff simply forget to post and revert to email? Does prefix-format discipline require training that won't happen?

**D29: pgvector added in Wave 1A schema migration (not backlog)**
Rationale: ALTER TABLE on live data + backfill migration is painful and risky at 500+ rows. Add deal_embeddings table now (30 min) vs. painful migration later. Schema: id uuid, deal_id uuid FK → deals.id, embedding vector(1536), content_text text, model_used text, active boolean default true, created_at timestamptz.
Technical reality: Wave 1A schema agent does the migration. The embedding model (OpenAI text-embedding-3-small) is not wired until Wave 2A. deal_embeddings table exists but stays empty until D30 bulk-embed runs.
Concern to debate: Is it sound to add a table whose consuming code doesn't exist yet? What is the risk of schema-without-implementation sitting for 2+ weeks?

**D30: Memory migration = two-phase (Phase 1: bulk-embed 107 client profiles; Phase 2: staff Q&A)**
Rationale: "Every other AI you connect starts with that foundation instead of zero." Day 1 semantic search over 4 years of historical deal intelligence. Staff won't adopt a system that's empty on day 1.
Phase 1: Break 107 client profiles into atomic facts (D33 below) → bulk-embed → deal_embeddings table. Runs after Wave 1A merges.
Phase 2: Structured Q&A with each staff member → capture institutional knowledge as embeddings.
GDPR note: 107 profiles come from already-mined email data (mining already done). The new step is embedding them into vector space.
Concern to debate: Does embedding historical client profiles into pgvector constitute a NEW processing activity requiring expanded DPIA scope beyond the original email mining DPIA? These are profiles of EU business contacts (travel agents, buyers). The original DPIA covers email mining — does it cover vector embedding of the resulting intelligence?

**D31: Webhook endpoint security — header-only auth, per-service keys, rate limiting**
Source: Robert MacNaughton security audit of Nate B Jones' open-source "Open Brain" implementation (same pgvector + Supabase stack we're using).
Four vulnerabilities in the reference implementation we must not repeat:
1. Auth key as URL query param → logs in browser history, server logs, proxy logs
2. Single shared key across all services → one breach = rotate everything
3. No rate limiting on ingest endpoints → leaked key = unlimited extraction
4. Embedding model provider retention policies not disclosed (GDPR implication)
Decision: header-only auth (x-brain-key or Authorization: Bearer), per-service credentials (separate keys for Teams webhook, n8n, MCP server), rate limiting at Supabase Edge Function level.
Concern to debate: Per-service key rotation management adds operational overhead for a 1-person build team. Is this proportionate for a 6-person company with a private self-hosted system?

**D32: deal_embeddings soft-delete — active boolean; hard-delete only via GDPR erasure function**
Source: Community pattern from Mark Madsen (gist). Addresses missing thought lifecycle in reference implementation.
Decision: Deletion = UPDATE active = false. Hard-delete only via erase_contact_pii() GDPR erasure function. All queries filter WHERE active = true.
Rationale: GDPR deletion log requires audit trail proving erasure occurred.
Concern to debate: Art. 17 right to erasure is absolute — does "active = false" (data still in database, still in vector store) satisfy the legal obligation? Or must embedding vectors be actually deleted from the pgvector index when a data subject exercises erasure rights?

**D33: Atomic facts chunking for D30 bulk-embed**
Rationale: Semantic queries return specific matching facts, not averaged-out profile blobs. Each atomic fact = one row in deal_embeddings. Example: "AHI Travel: senior Nordic traveler segment, 75% of DMC revenue" (one embedding).
Scale: 107 profiles × 10-20 facts each = 1,070–2,140 embedding rows on Day 1.
API: OpenAI text-embedding-3-small. Rate limit: 3,000 requests/minute on Tier 1. At 2,140 rows, well within rate limits.
Concern to debate: Does breaking 107 client company profiles into atomic facts constitute automated profiling of identifiable individuals under GDPR Art. 22? Travel agent company profiles include: individual contact names, behavioral patterns, budget ranges, preferences. Each atomic fact is a statement about a business relationship — but the business contacts are natural persons.

---

## DEBATE INSTRUCTIONS

Debate the proposition: **"D25–D33 are sound and Wave 1A should start."**

Each agent argues from their role. Cross-challenge each other where your positions conflict. The most important unresolved questions are:

1. **D30 + D33 GDPR scope:** Does bulk-embedding 107 client profiles as atomic facts require an expanded DPIA before Wave 1A? (DPA vs Sebastian)
2. **D32 erasure compliance:** Does soft-delete (active=false) satisfy Art. 17 right to erasure, or must vector embeddings be physically deleted? (DPA vs Engineer)
3. **D28 capture discipline:** Will staff actually use #crm-capture with prefix formats, or is this a channel that gets abandoned in week 2? (Janna vs Sebastian)
4. **D25 timing:** Should B2C traveler auth be locked now when FinnConcierge B2C is explicitly deferred? (Janna vs Sebastian — is this premature decision-making or smart pre-planning?)
5. **D31 proportionality:** Is per-service key management overhead proportionate for a 6-person private system? (Engineer vs DPA)

---

## THE FOUR AGENTS

### Agent 1 — SEBASTIAN HEISKANEN (Staff, Early Adopter)
**Role:** Junior sales staff, 20s. First AI tool at work. He will be the first pilot user.
**Core bias:** Speed and simplicity. Any delay or added complexity = bad. "Just ship it."
**What he knows:** He's been told zero data entry, the system gets smarter every week. He's excited. He checked his email on his phone from a client site last week and missed a Teams message. He's not technical.
**Attack angle:** Challenge anything that delays Wave 1A or adds pre-build compliance work. Push back on concerns that are theoretical rather than practical. Argue that the DPIA for D30/D33 is over-engineering — these are business profiles, not health records. On D25: he actually wants magic link because he hates passwords. On D28: he will use #crm-capture if it takes 10 seconds, won't if it takes 2 minutes.

### Agent 2 — JANNA KANKKUNEN (Head of Sales, Pipedrive Power User)
**Role:** Head of Sales, 35+, has used Pipedrive for 3 years. Skeptical of custom builds.
**Core bias:** Workflow integrity. Adoption failure = her problem. "Pipedrive is rejected, fine — but this better work on day 1."
**What she knows:** The custom build decision is locked (D1). Her job is to make sure what gets built actually works for her team. She's protective of her staff's time. She controls rollout.
**Attack angle:** Challenge D28 (Teams capture) — her staff already uses email for everything, adding another channel with format discipline is a training burden. Challenge D25 timing — why lock B2C traveler auth now when we're not building B2C for months? Is this analysis paralysis? Challenge D26 — if Wave 3A gets $8, what stops every wave from requesting an exception? She'll accept GDPR delays if the DPA makes a good case.

### Agent 3 — FINNISH DPA INSPECTOR (Tietosuojavaltuutettu)
**Role:** Finnish Data Protection Authority official. Enforces GDPR Art. 17, Art. 22, Art. 35.
**Core bias:** Compliance is non-negotiable. Ambiguity = enforcement risk. Fines are real.
**What she knows:** The prior Grok debate already flagged Finnish DPA as aggressive on automated profiling. DPIA for email mining is already locked (D9). She knows Triple-LLM is already in scope. She is NOT here to re-raise solved issues. She is here to evaluate whether D25–D33 introduce NEW processing activities not covered by the existing DPIA scope.
**Attack angle:**
- D30 + D33: The existing DPIA covers email mining. Embedding 107 client profiles into pgvector is a NEW processing activity (vector representations of individuals' business behaviors). This likely triggers an expanded DPIA before Wave 1A — not before live email mining (already required), but before the bulk-embed itself.
- D32: Art. 17 right to erasure requires that personal data be erased. "Active = false" with data still in the database and still indexed in pgvector does NOT satisfy this. The embedding vector IS personal data if it encodes patterns about an identifiable person. Physical deletion from the pgvector index is required.
- D33: Atomic facts about a natural person (travel agent named Jonas Schmidt at AHI Travel, his preferences, his decision patterns) = personal data under GDPR Art. 4(1). Automated generation and storage of these facts = automated profiling. Art. 22 applies.
- D31: Rate limiting is good but she wants confirmation the API key rotation log is auditable.

### Agent 4 — SENIOR ENGINEER (Technical Skeptic)
**Role:** Senior backend engineer, 10+ years. Has seen creative architectures fail in production.
**Core bias:** "This will break in the way you least expect."
**What he knows:** The existing 9-table schema. The Triple-LLM pipeline is already required. BUILD-STATE.md context rot mitigations are already in place. He is NOT here to re-raise context rot (already mitigated). He is here to find production failure modes in D25-D33 specifically.
**Attack angle:**
- D28: Teams webhook retry window = 3 seconds. If n8n processes synchronously, it will regularly exceed 3 seconds → duplicate embedding rows. The decision includes "return 200 immediately + process async" — but was a unique index on teams_message_id actually added to the schema design? If not, duplicates will silently corrupt the deal_embeddings table.
- D29: deal_embeddings gets vector(1536) in Wave 1A. The embedding model (OpenAI text-embedding-3-small = 1,536 dims) isn't wired until Wave 2A. If the embedding model ever changes (text-embedding-3-large = 3,072 dims), the column dimension is locked and requires a DROP + recreate. Is 1,536 the right dimension to hardcode now?
- D32: The erase_contact_pii() function is referenced in D32 but doesn't exist yet. Wave 1A schema agent will create the deal_embeddings table without this function. There's a window (Wave 1A to Wave 5A) where the table exists, data enters it, and the erasure mechanism doesn't exist. What's the risk window?
- D33: The bulk-embed script is not in any wave's scope. Wave 1A adds the schema. D30 says "bulk-embed runs after Wave 1A merges." Who builds the bulk-embed script? Which agent? If it's not in a wave's spawn prompt, it won't get built.

---

## OUTPUT FORMAT

After the debate, produce:

### VERDICT TABLE
| Decision | Sebastian | Janna | Finnish DPA | Senior Engineer | FINAL VERDICT |
|----------|-----------|-------|-------------|-----------------|---------------|
| D25 | | | | | LOCK / LOCK WITH CONDITION / BLOCK |
| D26 | | | | | |
| D27 | | | | | |
| D28 | | | | | |
| D29 | | | | | |
| D30 | | | | | |
| D31 | | | | | |
| D32 | | | | | |
| D33 | | | | | |

### REQUIRED CHANGES (if any)
List changes that must be made before Wave 1A starts. Format:
- [Dx] [Change required] — raised by [agent]

### OVERALL VERDICT
**GO** — all decisions locked, Wave 1A starts now.
**CONDITIONAL GO** — Wave 1A starts after completing: [specific list].
**NO-GO** — [blocking issue] must be resolved first.

---PROMPT END---
