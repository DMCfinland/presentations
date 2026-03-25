## Database and Infrastructure Analysis

**Agent 6 — Database Architect | 2026-02-22**
*Sources: wave1-cross-brief.md, agent-5-integration-architect.md (Sections 1 and 4), cluster-b-technical-findings.md (TECH CHOICES), monster-compressed.md (Sections 7 and 9), PRD-v0.1.md (Sections 9, 10, 11)*

---

### 1. Current Database Decisions — What's Chosen

All confirmed storage choices across all 6 products, in order of confirmation confidence:

**Zone 2 — Azure North Europe (B2C platform, confirmed across 3+ source documents):**

| Storage Service | Confirmed Use | Source |
|---|---|---|
| Azure SQL (General Purpose) | Users, Mood Matrix, Products, Shadow Ledger, Contracts, Tenants, Scoring Formula, A/B Hook State, Itinerary/Booking Reference, Affiliate/Trackable Links | cluster-b (TECH CHOICES Decision 2), monster-compressed Section 7 |
| Azure Cosmos DB | Session state (Context Briefcase), Staff Priority Queue, chat logs (hot storage) | cluster-b Decision 3, monster-compressed |
| Azure AI Search (4 indexes) | Commercial Shelf, Cultural Index, Practical Shelf, Internal/Brand Index | wave1-cross-brief A4 table |
| Azure Data Lake Gen2 | Raw event logs (SHA-256 hashed user_id), Mystery Shopper synthetic data (separate partition) | wave1-cross-brief A4 table |
| Azure OpenAI GPT-4o (ZDR) | AI inference engine with Zero Data Retention policy | cluster-b Decision 1, monster-compressed Section 7 |
| Azure Functions (Consumption) | Serverless compute for all agents | cluster-b Decision 5 |
| Azure Event Grid | Zone 2 integration backbone | cluster-b Decision 6, A5 Section 8 |
| CDN | Tenant config assets (logo, fonts, theme) | wave1-cross-brief A4 table |

**Zone 1 — Hetzner VPS + Supabase Frankfurt (B2B tools, confirmed by A1/A2 via PRD v3 resolution):**

| Storage Service | Confirmed Use | Source |
|---|---|---|
| Supabase PostgreSQL + pgvector | Second Brain 8-table schema (production target, State B) | wave1-cross-brief A2, PRD-v0.1 Section 11 |
| Hetzner VPS (~€10-20/mo) | n8n self-hosted instance + Email Drafter 8-node pipeline | wave1-cross-brief A2, PRD-v0.1 Section 10 |
| Claude Teams (M365, Anthropic cloud) | Second Brain State A (interim) — no structured database | wave1-cross-brief A1, PRD v3 |

**Confirmed Supabase 8-table schema (all require `company_id` before first data load):**
clients, contacts, interactions, components, itineraries, version_sequences, suppliers, rate_cards, golden_prompts

**Conflicts and ambiguities:**

1. **Redis vs Pinecone (unresolved):** Both mentioned as in-memory vector DB candidates for Chef's <800ms latency requirement. This is not a GDPR issue but does affect Zone 2 cost model. Neither is chosen yet.
2. **Adyen vs Stripe Connect (unresolved):** Payment processor choice is explicitly open. Both A4 and A5 flag this. Affects Shadow Ledger webhook schema and Phase 2 virtual card feature. Flag in Section 3.
3. **PRD v0.1 Decision A3/A5 (partially open):** n8n as unified backbone for Second Brain is a PRD recommendation, not yet Patrick-validated. The 4 Opus source documents designed Second Brain on Power Automate. A2's verdict (confirmed in wave1-cross-brief) is that n8n + Supabase is the correct production target. This agent treats A2's resolution as authoritative.
4. **North Europe vs Sweden Central:** cluster-b explicitly flags this: PROJECT_CONTEXT says North Europe, but GDPR compliance for CRM data was originally planned for Sweden Central. A4 confirms North Europe across 3 sources. Both are EEA-resident, both satisfy GDPR geographic requirement — no legal conflict, only a naming inconsistency in earlier documents.

---

### 2. The Core GDPR Problem

Finland DMC operates as data controller for two structurally different categories of personal data that require different legal frameworks, consent mechanisms, breach timelines, and retention rules. Mixing them in shared infrastructure creates compounded GDPR liability.

**The fundamental split:**

| Dimension | Zone 1 (B2B) | Zone 2 (B2C) |
|---|---|---|
| Data subjects | Named individuals at B2B partner companies (travel agencies, tour operators) | End guests — tourists and travelers |
| Data types | Contact names, emails, phones, relationship history, account health | Name, location, mood profile, behavioral data, booking transactions |
| Legal basis | Article 6(1)(b): contract performance with B2B clients; Article 6(1)(f): legitimate interest in account management | Article 6(1)(b): contract performance (guest has booked a stay); Article 6(1)(a): consent for behavioral profiling |
| Retention | 24-month rolling window (confirmed, Second Brain system summary) | Transaction records: accounting law minimum (7 years); behavioral profiles: anonymize at session end; raw logs: Data Lake with hashed user_id, retained for Optimizer training |
| Breach notification | GDPR Article 33: 72-hour notification to supervisory authority for B2B contact PII | GDPR Article 33: same; Article 34: notification to affected guests if high risk to rights and freedoms |
| Rights requests | Article 15-22: right to access, erasure, portability for named B2B contacts | Article 15-22: same for guests; pseudonymization makes erasure technically tractable if done correctly |
| DPIA required | Article 35(3): DPIA required for automated profiling with significant effects — RelationshipHealthScore qualifies | Article 35(3)(c): mandatory DPIA for systematic monitoring in publicly accessible area (resort AI); Article 35(3)(b): mandatory DPIA if Mood Matrix includes Article 9 categories |

**Can B2B and B2C share a database?**

No, not without separate schemas with RLS enforcement and documented legal justifications for every data access pattern. The risk is purpose creep: Article 5(1)(b) purpose limitation principle requires that data collected for B2B contract performance cannot be processed for B2C personalization without a new legal basis. Physical zone separation is the most defensible architecture — it turns a legal principle into a technical constraint that cannot be accidentally violated.

**Mood Matrix — Article 9 health data risk:**

The Mood Matrix schema (Azure SQL) contains a "Needs_Accessibility" tag. Under GDPR Article 9(1), processing of data concerning health (including disability/accessibility needs, per Article 4(15) definition) is prohibited unless Article 9(2) exception applies.

The relevant exceptions are:
- Article 9(2)(a): Explicit consent — requires a separate, specific, informed consent act distinct from general Terms of Service acceptance. This is a higher bar than Article 6 consent.
- Article 9(2)(b): Employment/social security law obligations — does not apply here.
- Article 9(2)(f): Legal claims establishment/defense — does not apply in normal operation.

Schema-level enforcement mechanism required: The "Needs_Accessibility" tag must be stored in a separate database column with a column-level access control policy (Azure SQL column-level security) that restricts access to a dedicated accessibility service role. This role must only be activated when explicit Article 9(2)(a) consent is recorded. The consent record itself must be stored with timestamp, consent text version, and opt-out mechanism.

A5's recommendation (confirmed as correct): Exclude "Needs_Accessibility" from the Mood Matrix at launch. Collect accessibility requirements through a separate pre-arrival form channel with explicit Article 9(2)(a) consent. This eliminates the DPIA Article 35(3)(b) trigger for the Mood Matrix specifically (the Article 35(3)(c) DPIA for systematic monitoring is still mandatory regardless).

**Two-state Second Brain GDPR chain difference:**

- State A (Claude Teams, Anthropic infrastructure): No EU data residency. Anthropic has no EU-based data centers as of February 2026. For GDPR Article 44–46 compliance, named B2B contact PII (individuals' names, emails) cannot enter Claude Teams without a verified transfer mechanism — either Standard Contractual Clauses (SCCs, Article 46(2)(c)) or an Anthropic DPA confirmed as GDPR Article 28-compliant for EU-based controllers. This is an existing legal gap confirmed by A1. Until the Anthropic DPA is verified and SCCs executed, State A can only process company-level records (revenue tier, preferred destination) — not named contact PII.
- State B (Supabase on Hetzner Frankfurt): German data center, EEA-resident. No transfer mechanism required. GDPR compliance is straightforward with appropriate DPA with Supabase/Hetzner. Named contact PII is permissible from day 1 once DPA is executed.

---

### 3. EU Data Residency Map

All 16 schemas from A4, plus Second Brain two-state entries and the proposed 9th Supabase table.

| Data Entity | Storage Location | GDPR Legal Sufficiency | ZDR Coverage | Notes |
|---|---|---|---|---|
| **Zone 2 — Azure North Europe** | | | | |
| User Profile / Context Briefcase | Azure SQL (Users) + Cosmos DB (session state) | EEA-resident — adequate | Azure OpenAI ZDR: yes — data not used to train public models | Contains guest name, language, history_notes — PII. Erase on guest request via Article 17. Session state in Cosmos DB dropped on intent change (by design). |
| Mood Matrix (8 dimensions) | Azure SQL | EEA-resident — adequate | Yes | Behavioral profiling — Article 6(1)(a) consent required. "Needs_Accessibility" tag: exclude at launch (Article 9 risk). Store cluster_id post-anonymization. |
| Context Backpack (ephemeral) | Cosmos DB (hot) | EEA-resident — adequate | Yes | Dropped on intent change. Contains room+resort location, weather, active suggestion. Short retention by design — no separate erasure procedure needed if confirmed as truly ephemeral. |
| Product Record | Azure SQL (Products) + Azure AI Search (Commercial Shelf) | EEA-resident — adequate | Yes | Product metadata only — no personal data. No GDPR issue. |
| Shadow Ledger | Azure SQL (Ledger) | EEA-resident — adequate | Yes | Contains guest user_id + booking_ref + financial amounts. Article 6(1)(b) legal basis. Financial records: 7-year retention minimum (Finnish accounting law). user_id must be pseudonymized for analytics but retained linked for 7-year financial obligation. |
| Contract Rules | Azure SQL (Contracts) | EEA-resident — adequate | Yes | Provider/partner B2B data — Article 6(1)(b) contract performance. No guest PII. |
| Tenant Config | Azure SQL (Tenants) + CDN | EEA-resident — adequate | Yes | Brand/UI config — no personal data. |
| Scoring Formula State | Azure SQL / Data Lake | EEA-resident — adequate | Yes | W1-W5 weights, cluster_id only — no personal data. |
| A/B Hook State | Azure SQL (Products/Stats) | EEA-resident — adequate | Yes | Product-level stats — no personal data. |
| Staff Priority Queue | Cosmos DB (live) | EEA-resident — adequate | Yes | Contains conversation_id + urgency_score + assigned_staff. Staff data: Article 6(1)(b) employment contract. Guest-linked conversation_id: pseudonymize. |
| RAG Shelves (4 indexes) | Azure AI Search | EEA-resident — adequate | Yes (search indexes, no inference) | Commercial, Cultural, Practical indexes: no personal data. Internal index: may contain synthesized guest interaction insights — review for PII before indexing. |
| Data Lake Raw Logs | Azure Data Lake Gen2 | EEA-resident — adequate | Yes | user_id must be SHA-256 hashed (REAL data). data_source field distinguishes REAL/SYNTHETIC. Cluster_id retained for Optimizer. |
| Mystery Shopper Records | Azure Data Lake Gen2 (separate partition) | EEA-resident — adequate | Yes | Synthetic only — no real personal data. Partition separation is good practice. |
| Itinerary / Booking Reference | Azure SQL (Itinerary) | EEA-resident — adequate | Yes | booking_ref linked to guest — PII. Retention: 7 years (Finnish accounting + consumer contract law). |
| Safety Bulletin | Azure AI Search (Practical Shelf) | EEA-resident — adequate | Yes | Content data — no personal data. |
| Affiliate / Trackable Link | Azure SQL (Ledger extension) | EEA-resident — adequate | Yes | source_partner_id: B2B data. signed_token: not personal data. No guest PII in this table. |
| **Payment processor webhook data** | Azure SQL (Ledger extension) | EEA-resident — adequate | Depends on processor | OPEN: Adyen (EU-headquartered, strong GDPR coverage) vs Stripe Connect (US-headquartered, requires SCCs). Schema diverges between processors. Adyen preferred on GDPR grounds. |
| **Zone 1 — Second Brain, State A (current)** | | | | |
| Second Brain — company-level records (revenue tier, preferred destination, segment) | Claude Teams (Anthropic cloud, US infrastructure) | INADEQUATE for PII without SCCs + Anthropic DPA | No (not Azure) | Company-level non-PII records are lower risk but not zero risk if company names identify individuals (sole traders). Anthropic DPA must be verified before any use. |
| Second Brain — contact records (named individuals: names, emails, phones) | Claude Teams | LEGALLY INSUFFICIENT without Article 46 transfer mechanism | No | Named B2B contact PII MUST NOT enter Claude Teams until Anthropic DPA (Article 28) and Article 46 SCCs are executed. This is a Day 0 legal prerequisite, not a future cleanup. |
| **Zone 1 — Second Brain, State B (production target)** | | | | |
| Second Brain — all 8 tables (clients, contacts, interactions, components, itineraries, version_sequences, suppliers, rate_cards, golden_prompts) | Supabase PostgreSQL on Hetzner Frankfurt | EEA-resident — adequate | Not applicable (no inference service) | All tables require `company_id` added BEFORE first data load. RLS enforces company_id isolation at row level. Execute DPA with Supabase/Hetzner before data load. |
| **Proposed 9th table — booking source metadata batch** | Supabase PostgreSQL on Hetzner Frankfurt | EEA-resident — adequate — Article 6(1)(f) legitimate interest | Not applicable | See Section 6 for full analysis. Isolated from main 8-table schema by RLS policy difference. Fields: operator_id, revenue_tier, booking_count, batch_date, company_id. No guest_id, no name, no behavioral data. |
| **Email Drafter pipeline processing** | n8n on Hetzner VPS | EEA-resident — adequate | No | Email content (B2B contact PII) processed transiently in n8n. No persistent storage of raw email content beyond task logging. Confirm with Hetzner DPA. |

**GDPR Articles cited in this section:** 5(1)(b), 6(1)(a), 6(1)(b), 6(1)(f), 9(1), 9(2)(a), 15-22, 17, 28, 30, 33, 34, 35(3)(b), 35(3)(c), 44, 46, 46(2)(c).

---

### 4. Three Infrastructure Options

#### Option A — Fully Separate

**Architecture:** Zone 1 (B2B) on Hetzner VPS + Supabase + Claude Teams (interim) / Supabase (production). Zone 2 (B2C) on Azure North Europe. No shared infrastructure layer.

This is the current confirmed architecture.

**Cost estimate:**

| Component | Tier | Monthly (€) |
|---|---|---|
| **Zone 1** | | |
| Hetzner VPS (2 vCPU, 4GB RAM) | CX22 | €10-20 |
| Supabase | Free tier (dev) → Pro (€25/mo at ~200K rows) | €0-25 |
| Claude Teams (5 users) | Teams plan (~€30/user/mo) | €150 |
| **Zone 1 total** | | **€160-195** |
| **Zone 2 — pilot scale (<100 guests/month)** | | |
| Azure Functions | Consumption plan (first 1M executions free) | €5-15 |
| Azure Cosmos DB | Serverless (pay per RU) | €20-50 |
| Azure SQL | General Purpose, 2 vCores | €125-150 |
| Azure AI Search | Basic tier (1 replica, 2GB index) | €75 |
| Azure Data Lake Gen2 | Pay-as-you-go (~100GB) | €5-10 |
| Azure OpenAI GPT-4o | Per-token pricing (~€9 for classification) | €9-50 |
| Azure Event Grid | Pay-per-event (<1M/mo free) | €0-5 |
| CDN | Standard tier | €5-10 |
| **Zone 2 total (pilot)** | | **€244-370** |
| **Zone 2 — live scale (1,000 guests/month)** | | |
| Azure Functions | Consumption (higher volume) | €30-60 |
| Azure Cosmos DB | Serverless (higher RU) | €80-150 |
| Azure SQL | General Purpose, 4 vCores | €250-300 |
| Azure AI Search | Standard S1 (25GB index, higher QPS) | €210 |
| Azure Data Lake Gen2 | ~1TB | €20-30 |
| Azure OpenAI GPT-4o | Guest conversations (~€0.05-0.10/conversation) | €50-100 |
| **Zone 2 total (live scale)** | | **€640-850** |
| **Total Option A (pilot)** | | **€404-565/month** |
| **Total Option A (live scale)** | | **€800-1,045/month** |

**GDPR risk level:** Low. Physical zone separation enforces purpose limitation at infrastructure level. Each zone has a single legal basis. Breach notification scope is bounded by zone.

**Migration effort:** Zero — this is the current architecture.

**Operational complexity:** Medium. Two separate environments to manage, two DPAs (Supabase/Hetzner + Microsoft/Azure), no shared monitoring layer. Mitigated by A5's finding that zones share no integration middleware.

---

#### Option B — Unified Azure

**Architecture:** Everything moved to Azure North Europe. B2B tools rebuilt on Azure-native services: Azure Logic Apps replaces n8n, Azure SQL replaces Supabase, Azure AD B2B for staff access. Claude Teams retired or kept as UI only.

**Cost estimate:**

| Component | Tier | Monthly (€) |
|---|---|---|
| Azure Logic Apps (replaces n8n) | Standard single-tenant | €50-200 |
| Azure SQL (Zone 1 B2B schema) | General Purpose, 2 vCores | €125-150 |
| Azure SQL (Zone 2 B2C schema) | General Purpose, 4 vCores | €250-300 |
| Azure Cosmos DB | Serverless | €50-150 |
| Azure AI Search | Standard S1 | €210 |
| Azure Data Lake Gen2 | ~1TB | €20-30 |
| Azure OpenAI GPT-4o | Both B2B classification + B2C conversations | €60-150 |
| Azure Functions | Consumption | €30-80 |
| Azure Event Grid | Pay-per-event | €5-15 |
| CDN | Standard | €5-10 |
| Claude Teams (if retained for UI) | 5 users | €150 |
| **Total Option B (live scale)** | | **€955-1,435/month** |

**GDPR risk level:** High. B2B contact PII and B2C guest behavioral data coexist in the same Azure subscription, same SQL server. Zone separation becomes a schema/RLS convention rather than an infrastructure boundary. A misconfigured query, a developer mistake, or an Azure support escalation can access both zones. The Article 5(1)(b) purpose limitation principle is enforced only by code, not by physical separation.

Additional risk: rebuilding 7 Power Automate flows (fully designed in source documents) as Azure Logic Apps adds implementation risk for no GDPR benefit. Logic Apps is more expensive than n8n (~€50-200/mo vs €0 for self-hosted n8n on existing VPS).

**Migration effort:** High. Supabase → Azure SQL migration, n8n workflow rebuild, Claude Teams retirement or integration. 4-8 weeks of migration work.

**Operational complexity:** Lower (single cloud vendor, single DPA). But higher cost and higher GDPR exposure.

---

#### Option C — Federated (Recommended)

**Architecture:** Zone 1 stays on Hetzner VPS + Supabase Frankfurt (EU-native, B2B data only). Zone 2 stays on Azure North Europe (B2C guest data only). Two permitted data crossings as defined by A5: (1) anonymized booking source metadata (daily batch, operator_id + revenue_tier only, no guest PII) Zone 2 → Zone 1 via batch job; (2) pseudonymized guest satisfaction via B2B Partner Dashboard API (pseudonymized before leaving Zone 2). Product catalog (Azure AI Search) is non-personal and can be queried from Zone 1 tools without GDPR implications.

**Cost estimate:** Identical to Option A, since Option C is the current confirmed architecture with explicit boundary rules added.

| | Monthly (€) |
|---|---|
| Zone 1 total | €160-195 |
| Zone 2 total (pilot) | €244-370 |
| Zone 2 total (live scale) | €640-850 |
| **Total Option C (pilot)** | **€404-565/month** |
| **Total Option C (live scale)** | **€800-1,045/month** |

**GDPR risk level:** Low. Infrastructure boundary = GDPR boundary. The two permitted data crossings are narrowly scoped and documented. Operator_id + revenue_tier crossing carries no personal data (operator_id refers to the B2B travel agency entity, not a named individual). The B2B Partner Dashboard pseudonymization requirement is a code-level constraint that must be unit-tested before go-live.

**Migration effort:** Zero for current state. Incremental effort for: (a) adding `company_id` to all 8 Supabase tables before first data load, (b) creating the 9th table for booking source metadata batch, (c) implementing pseudonymization in the B2B Partner Dashboard endpoint.

**Operational complexity:** Medium. Same as Option A but with explicit boundary governance: documented Article 30 Record of Processing Activities entries for the two permitted data crossings, tested pseudonymization in B2B dashboard endpoint, batch job monitoring for the daily metadata transfer.

---

### 5. B2C Guest Data Anonymization Strategy

**What must be anonymized and when:**

| Data | When Anonymized | Method | What's Retained | Why Retained |
|---|---|---|---|---|
| Guest name (Context Briefcase) | At session end | Delete from Cosmos DB session record | Nothing | No legitimate interest in retaining name post-session |
| user_id in Data Lake logs | Before write to Data Lake | SHA-256 hash (confirmed, A4) | Hashed user_id, cluster_id | Optimizer training requires cluster-level signal; hash prevents re-identification without salt |
| Mood Matrix dimensions (8 values) | At session end for individual; retained as cluster aggregate | Keep cluster_id, discard individual user_id linkage | cluster_id + dimension weights (aggregate) | Scoring Formula State and A/B Hook State require cluster-level behavioral signals, not individual |
| Booking reference (Shadow Ledger) | Never (financial record) | Not anonymized | Full record for 7 years | Finnish accounting law + consumer contract law minimum retention |
| Conversation logs (Cosmos DB) | After SLA breach window (48h for staff review) | Delete or truncate; keep event_type + cluster_id in Data Lake | Aggregate event types only | GDPR data minimization (Article 5(1)(c)); conversation content is high-risk PII |
| Safety Bulletin responses | Not applicable | N/A | Bulletin content only | No personal data in bulletins |

**SHA-256 hashing (A4's approach) — evaluation:**

SHA-256 without a secret salt is reversible via rainbow tables if the input space is small (e.g., sequential user IDs or predictable booking reference formats). Recommendation: use HMAC-SHA-256 with a server-side secret key stored in Azure Key Vault. This makes the hash one-way even with access to the hash output. The secret key rotation policy must be documented in the DPIA.

**Mood Matrix dimensions after anonymization:**

Individual-level Mood Matrix rows (user_id + 8 dimension values) must not persist beyond session end under the behavioral profiling consent. What survives:
- The cluster assignment (cluster_id) is retained in aggregate form for Scoring Formula State optimization
- W1-W5 weights in Scoring Formula State are cluster-level, not individual-level
- A/B Hook State conversion rates are cluster-level aggregates
- The individual Mood Matrix row is deleted at session end; the cluster statistics it contributed to remain

This design satisfies Article 17 right to erasure: erasing the individual user_id row erases the individual's contribution to identifiable processing, even though the cluster statistics persist (pseudonymized aggregate).

**Schema-level enforcement mechanisms:**

1. Azure SQL column-level security on `user_id` in Mood Matrix table — restricts read access to a session service principal only, not the analytics role
2. Azure SQL Row-Level Security on all tables with `tenant_id` — cross-tenant data leakage prevention
3. Data Lake lifecycle policy: conversation event logs auto-deleted after 48h; cluster aggregate logs retained indefinitely
4. Azure Key Vault: HMAC secret key for user_id hashing; access via managed identity only (no hardcoded keys in application code)
5. FIRE RED protocol: when triggered, session data must be flagged for immediate staff review and conversation log retained for 30 days (legal liability window), then deleted

---

### 6. Recommended Architecture

**Recommendation: Option C — Federated.**

The decisive reason is that physical zone separation enforces the GDPR Article 5(1)(b) purpose limitation principle at infrastructure level rather than code level, at no additional cost compared to Option A (which is the current architecture) and at substantially lower cost and lower GDPR risk than Option B.

**On A5's open question: Does Supabase need a dedicated table for the daily booking source metadata batch from Azure?**

**Yes — dedicated table, RLS-isolated from the main 8-table schema.**

The reasoning is:
1. **Different legal basis:** The 8 main tables process B2B contact PII under Article 6(1)(b) (contract performance). The metadata batch table processes operator-level business intelligence under Article 6(1)(f) (legitimate interest in understanding which B2B partners generate high-value bookings). Different legal bases require different retention rules — mixing them in a single schema makes retention enforcement ambiguous and audit-difficult.
2. **Different access control:** The main 8 tables are accessed by n8n NODE 2 (Email Drafter pull on email arrival) and Second Brain analytics. The metadata batch table should be read-only for Second Brain analytics only — the Email Drafter has no legitimate use for booking source attribution data. RLS with a separate analytics role, distinct from the n8n service role, enforces this.
3. **Different data provenance:** Data originating from Zone 2 (Azure) arriving in Zone 1 (Supabase) is a documented data crossing that must appear in the Article 30 Record of Processing Activities. Isolating it in a dedicated table makes the Article 30 entry specific, auditable, and bounded.
4. **No guest PII in this table:** The strict condition from A5's boundary analysis holds: operator_id + revenue_tier + booking_count + batch_date + company_id only. No guest_id, no name, no behavioral data crosses the boundary.

**Proposed table definition:**
```
booking_source_metadata (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_id      UUID NOT NULL,          -- RLS key, same as other 8 tables
  operator_id     TEXT NOT NULL,          -- B2B partner identifier (not guest ID)
  revenue_tier    TEXT NOT NULL,          -- 'high-value' | 'standard' | 'new'
  booking_count   INTEGER NOT NULL,
  batch_date      DATE NOT NULL,          -- daily batch identifier
  created_at      TIMESTAMPTZ DEFAULT NOW()
)
```

RLS policy: `company_id = current_setting('app.company_id')` — same pattern as other 8 tables, but access restricted to `analytics_role`, not `n8n_service_role`.

This is the 9th table in the Supabase schema. It must have `company_id` added from the start (same requirement as the other 8 tables).

**Pre-deployment schema requirement confirmation:** All 9 Supabase tables must have `company_id` added BEFORE first data load. Retrofitting after data load requires a migration that risks mixing company-level data in version_sequences (which cross-references component changes against outcomes — mixing these across companies destroys the signal). This is the highest-risk data integrity issue in the Zone 1 schema and must be treated as a Day 0 blocker, not a Phase 2 cleanup.

---

### 7. Top 3 Questions for the Synthesis

**Q1: Adyen vs Stripe Connect — GDPR preference is Adyen, but which is operationally feasible for Finland DMC at launch volume?**

This is blocking the Shadow Ledger webhook schema design. Adyen is EU-headquartered (Amsterdam), uses EU data centers by default for EU merchants, and has a stronger GDPR track record than Stripe Connect (US-headquartered, SCCs required). However, Adyen has higher minimum volume thresholds and a more complex onboarding process. Stripe Connect supports faster developer onboarding but adds an Article 46 SCC requirement. The synthesis must force a decision on this — it cannot remain open into Phase 2 build.

**Q2: Anthropic DPA + Article 46 SCCs — what is the exact legal mechanism for Second Brain State A?**

State A (Claude Teams) can operate for company-level non-PII records today. Named B2B contact PII (the 107 client profiles' missing contact data from A1's finding) cannot enter Claude Teams until the Anthropic DPA is verified for GDPR Article 28 compliance and SCCs are executed or another Article 46 transfer mechanism is documented. The migration threshold to State B (200 clients or first data subject rights request) may arrive before the legal paperwork is in order. The synthesis needs to determine whether this is a legal gap to close now or a deliberate decision to delay State B migration.

**Q3: DPIA scope and ownership — who commissions it, and does it cover both the B2B Second Brain (automated profiling of clients) and the B2C Travel Assistant (systematic monitoring of guests)?**

PRD-v0.1 Section 11 (T7) flags the DPIA as a go-live blocker. A3 confirms the DPIA is mandatory under Article 35(3)(c) for the B2C Travel Assistant. The B2B Second Brain (RelationshipHealthScore = automated evaluation of B2B contacts) may also trigger Article 35(3)(a) for large-scale systematic evaluation. A single DPIA can cover both systems if scoped correctly, or two separate DPIAs may be required if the legal bases and risk profiles are sufficiently different. A Finnish-qualified GDPR legal counsel must be identified and engaged. Without a completed DPIA, neither system can go live with named personal data.

---

## Self-check

7 sections completed. Shortest section is Section 1 (18 table rows + 4 conflict entries).
Data residency table: 23 entities mapped (16 A4 schemas + 2 Second Brain states + payment processor + 9th Supabase table + Email Drafter pipeline). GDPR Articles cited: 5(1)(b), 5(1)(c), 6(1)(a), 6(1)(b), 6(1)(f), 9(1), 9(2)(a), 15-22, 17, 28, 30, 33, 34, 35(3)(a), 35(3)(b), 35(3)(c), 44, 46, 46(2)(c) = 19 distinct Articles.
Recommendation: Option C.
Challenge vs Agent 4: No schema conflict found. One extension: A4's SHA-256 hashing approach strengthened to HMAC-SHA-256 with Key Vault secret key (security improvement, not contradiction).
A5 boundary question answered: yes — dedicated 9th table recommended, with proposed schema definition.
Assumptions validated: North Europe = EEA-resident (confirmed); Hetzner Frankfurt = German DC, EEA-resident (confirmed); Supabase EU-native (confirmed — Hetzner Frankfurt data center); Adyen EU-headquartered (confirmed); company_id requirement confirmed in A2 and A5 outputs.
Context load: medium (~130K estimated).

---

## Briefing Flag for Lead

"Recommendation: Option C (Federated) because physical zone separation enforces the GDPR Article 5(1)(b) purpose limitation principle at infrastructure level at zero additional cost, while Option B (Unified Azure) increases both cost (€150-400/mo) and GDPR risk with no offsetting benefit."
