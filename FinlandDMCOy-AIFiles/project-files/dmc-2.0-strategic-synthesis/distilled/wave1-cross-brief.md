# Wave 1 Cross-Brief
**Lead-authored | 2026-02-22 | For Agent 5 and Agent 6 spawn prompts**
*Replaces full-output reads for A5 and A6 — ~30K token savings each*

---

## Quality Gate Status — All 4 Agents PASS

| Agent | Lines | Context Load | Gate |
|-------|-------|-------------|------|
| A1 Second Brain | 240 | Light (<100K) | ✅ PASS |
| A2 Email Drafter | 219 | Light (<100K) | ✅ PASS |
| A3 TA Vision | 169 | Light (<100K) | ✅ PASS |
| A4 TA Technical | 363 | Medium (~110K) | ✅ PASS |

All agents: specific content in every section, file+section citations present, trade-offs with dual options, Top 3 Questions genuinely blocking. No CRITICAL UPDATES contradictions.

---

## Agent 1 — Second Brain Analyzer

### 3-Bullet Key Conclusions
1. **PRD v3 verdict: CORRECT for transition period, NOT end-state.** Claude Teams Projects eliminates the highest-risk technical dependency (single Power Automate Premium license on other users' messages) and reduces build time from 12–16 weeks to days. Build Second Brain on Claude Teams now. Migration threshold: ~200 clients or first GDPR data subject rights request — whichever comes first. Do not migrate before this threshold.
2. **107 client profiles = ZERO contact names.** The proposals-data-summary data confirms: all 107 company records in client-profiles.yaml have no contact names, emails, or phone numbers. Contact data exists only in email-mining session outputs (sessions 1-3). Second Brain's usefulness as a personalization tool is blocked until contact data is imported. This is Day 1 data work, not a post-launch cleanup.
3. **GDPR blocker: Anthropic Claude Teams has no EU data residency.** Original architecture used Azure Sweden Central + Microsoft DPA. PRD v3 moves to Anthropic infrastructure, which has no EU data residency as of Feb 2026. Anthropic's DPA must be verified for GDPR Article 28 compliance and Article 44–46 transfer mechanism before any B2B contact data (named individuals) enters Claude Teams. This is a legal prerequisite for launch, not a future concern.

### Self-Check Highlights
- Assumptions validated: "Claude Teams only" confirmed in PRD v3 Section 1 Decision Table; 107-client count from proposals-data-summary; 24-month retention from second-brain-system-summary Storage Rules; Anthropic EU residency gap confirmed in second-brain-system-summary PRD v3 Supersession Check.
- 6 trade-offs with dual options documented (Sections 7 and 8).
- Top 3 Questions all identify specific system failure modes (storage gap, GDPR transfer mechanism, orphaned account routing).

---

## Agent 2 — Email Drafter Analyzer

### 3-Bullet Key Conclusions
1. **Stack verdict: Verdict B — n8n/Supabase confirmed, PRD v3 applies to Second Brain only.** Evidence is structural: PRD v3 describes a human-in-the-loop Claude Teams conversation; EMAIL-DRAFTER-DESIGN.md describes an automated 8-node n8n pipeline triggered on email arrival. The PRD v3 Client Communications project IS Email Drafter in its earliest manual form — it precedes the n8n automation, not replaces it. The Supabase schema (8 tables, pgvector, PostgreSQL RLS) is the production Second Brain target.
2. **Supabase sharing between Second Brain and Email Drafter: FEASIBLE with one prerequisite.** Single instance with PostgreSQL Row-Level Security enforcing `company_id` isolation. All 8 tables (clients, contacts, interactions, components, itineraries, version_sequences, suppliers, rate_cards, golden_prompts) need `company_id` added BEFORE first data load — retrofitting after data load is painful. Component win-rate calculations will mix unrelated company data without this isolation.
3. **Staff edit patterns are the highest-value implicit feedback signal in the system.** Every staff edit to an AI draft, every regeneration, every 48-hour no-reply alert generates an implicit quality signal. This signal feeds the golden prompt improvement flywheel on Friday review cycles. The version_sequences table (component changes correlated with Won/Lost outcomes) is the most valuable conversion-quality dataset in the entire product stack.

### Self-Check Highlights
- PRD v3 verdict explicitly stated in Section 5 with evidence from both PRD v3 and EMAIL-DRAFTER-DESIGN.md.
- Specific field names cited throughout: staff_owner, relationship_tier, last_contact, commission_pct, company_id.
- Commission exceptions documented: Solitary restaurant (0%), yoga (0%), catering fees (0%), "Stay Longer"/"Early Bird" (0%).
- Assumptions validated: PRD v3 scope checked in Section 5 via PRD v3 change log and executive summary.

---

## Agent 3 — Travel Assistant Vision Analyzer

### 3-Bullet Key Conclusions
1. **Revenue model quantified: 15% commission × OTA volume = structurally different business.** At €150 avg AI-assisted guest spend: €22,500/year at 1,000 guests, €225,000 at 10,000, €1,350,000 at 20 tenants × 3,000 guests. If avg spend is €300 (the AI is designed as a proactive seller), revenue doubles. The structural shift: marginal cost per additional guest is near zero. Finland DMC's current model scales linearly with staff; the TA model scales with platform, not headcount.
2. **Mood Evaluator Accessibility tags = potential Article 9 health data (mandatory DPIA).** The Mood Matrix includes "Needs_Accessibility" tag. Under GDPR Article 9, health/disability data requires explicit consent (Article 9(2)(a)) — a higher bar than legitimate interests. It also triggers a mandatory DPIA under Article 35(3)(b). This is a go-live blocker, not a future compliance nicety. The entire DPIA is mandatory under Article 35(3)(c) regardless of the Accessibility tag, due to systematic monitoring of individuals.
3. **10 non-technical pre-go-live requirements, 3 most blocking.** (1) DPA between Finland DMC and Järvisydän Oy (GDPR Article 28 — Finland DMC processes Järvisydän guest PII as a processor; must be signed before any guest data enters the system). (2) Commission structure agreement (Shadow Ledger records 15% commission automatically — cannot go live without agreed commercial terms). (3) Safety Bulletin governance (who owns it, who updates it, who is liable when advice follows a stale bulletin — no current document defines this liability chain).

### Self-Check Highlights
- 11 GDPR Article citations (Articles 5, 6, 9, 15-22, 28, 30, 35, 44, 46).
- Revenue model quantified with specific numbers across 3 scenarios (Section 2).
- Section 6: 10 discrete numbered pre-go-live requirements.
- Assumptions validated: 15% commission confirmed in cluster-c-devbrief-findings.md v0.1; Chameleon confirmed in cluster-a-vision-findings.md Decision 12.

---

## Agent 4 — Travel Assistant Technical Architect

### 3-Bullet Key Conclusions
1. **29 technologies documented (18 confirmed, 11 mentioned); 16 data schemas mapped to Azure services.** Confirmed core: Azure Functions, Event Grid, Azure OpenAI GPT-4o (ZDR), Cosmos DB, Azure SQL, Azure AI Search, Data Lake Gen2, Next.js 15 PWA, Azure North Europe region. Unresolved: Redis vs Pinecone (800ms Chef latency), Adyen vs Stripe Connect (payment processor — has Phase 2 virtual card implications), Sweden Central vs North Europe distinction. BLUEPRINTS skipped (context medium ~110K after 6 files — correct decision).
2. **No Järvisydän IT contact has been made yet — this is the critical path.** 5 BLOCKERS before build can meaningfully proceed: (a) Oracle Opera API credentials + endpoint docs + sandbox (Booker Agent BP_06 architecture cannot be finalized without this); (b) BookVisit product catalog feed (Commercial Shelf is empty without it; Chef cannot score products that don't exist); (c) Booking webhook from Järvisydän online store (Ingestion pipeline BP_01 cannot be tested); (d) Network path from Azure North Europe to Opera if on-premises; (e) GDPR Article 28 DPA with Järvisydän Oy.
3. **Staff Dashboard (BP_08) is CRITICAL, not started, and a go-live hard blocker.** Phase 1 FinnConcierge: 7 blueprints complete in mock mode, BP_08 (Staff Dashboard) NOT STARTED, BP_09 (Watchdog) NOT STARTED. BP_08 includes Traffic Light, Whisper, Takeover, God Mode, FIRE RED, Safety Net, SLA breach alerts — rated XL complexity. FIRE RED emergency override is a hard safety requirement. B2C Traveler PWA (BP_11) cannot go live without BP_08. Build sequence must treat BP_08 as parallel priority alongside BP_11.

### Self-Check Highlights
- 28 tech choices classified confirmed/mentioned with source citations.
- 16 schemas with specific field names and Azure services (full table in agent output + briefing flag).
- Critical path blockers table with 7 entries (5 BLOCKERS + 2 PREREQUISITES).
- BLUEPRINTS correctly skipped (context ~110K after 6 source files — within budget ceiling).
- Assumptions validated: North Europe confirmed across 3 sources; ZDR defined per cluster-b; Oracle Opera scope explicitly flagged as unresolved blocker.

---

## Briefing Flags — For A5 Spawn Prompt

### A1 → A5: Second Brain Data Exposures
Data outputs Second Brain would expose to other products:
- **Interaction Records (24-month history, per client):** Enables Email Drafter to personalize proposals with specific references to past programs, sentiment, and relationship history — e.g., "your Aurora series last January." Critical for Flagship clients (AHI Travel, Wikinger Reisen).
- **RelationshipHealthScore (1–10, per client, updated weekly):** Enables Staff Dashboard to surface account risk alerts alongside AI conversation monitoring — one unified risk view. CRITICAL: AHI Travel concentration (75% revenue), HIGH: Flash Pack orphan (€558K, no account owner since JK departure Aug 2024).
- **Client Records (revenue tier, preferred destination, segment, margin avg, staff_owner):** Enables Email Drafter proposal pre-population (correct tone/pricing tier) and TT Itinerary Drafter destination/group-size defaults.

### A2 → A5: Confirmed Email Drafter Stack
Stack: n8n (self-hosted, Hetzner VPS ~€10/month), 8-node automated pipeline triggered on email arrival. Supabase (PostgreSQL + pgvector) for Second Brain data. Claude API direct: Haiku (~€0.001/email) for task detection, Sonnet (~€0.01) for most drafts, Opus (~€0.05) for complaints/emergencies. PRD v3 Claude Teams = interim manual-mode predecessor; production stack = n8n + Supabase.

Open constraint for A5: Supabase schema needs `company_id` multi-tenancy field added to all 8 tables BEFORE first data load. Phase 2 delivery interface (Teams adaptive cards vs plain text) is unresolved and affects build timeline.

### A4 → A5: Travel Assistant API Surface
**Inbound endpoints (external systems call TA):**
- `POST /webhook/booking` — BookVisit sends booking event (HMAC-signed), triggers Magic Link generation
- `GET /welcome?token={jwt}` — Magic Link entry, customer-facing
- `POST /api/agent/process` — Chat endpoint; Traveler PWA sends messages, Master Agent responds

**Staff-facing endpoints:**
- `POST /staff/whisper` — Inject system-role instruction (invisible to customer)
- `POST /staff/takeover` — Disconnect AI, staff takes over
- `POST /staff/teach` — Thumbs up/down, Optimizer training signal
- `POST /staff/god-mode` — Force-push product to all recommendation queues
- `POST /staff/fire-red` — Emergency stop, alert all staff

**Outbound (TA calls external):**
- Oracle Opera (availability check, reservation creation) — BLOCKER: API scope unknown
- BookVisit product catalog feed — BLOCKER: machine-readable format not yet provided
- Finnish Meteorological Institute API — hourly weather
- Kp-index aurora API — northern lights probability
- Adyen or Stripe Connect — payment (choice unresolved)
- SendGrid/SMTP + SMS gateway — Magic Link delivery
- Slack/Teams webhooks — staff emergency alerts

**B2B partner-facing:**
- `GET /b2b/customers` — Travel agencies see their customers in Finland + satisfaction + upsell revenue

---

## Briefing Flags — For A6 Spawn Prompt

### A4 → A6: Full Schema List with Azure Services

| Schema | Key Fields | Azure Service |
|--------|-----------|---------------|
| User Profile / Context Briefcase | session_id, user_profile (name, segment, language, history_notes), trip_details (location, dates, booked_items), agent_persona, service_level | Azure SQL (Users) + Cosmos DB (session state) |
| Mood Matrix | user_id, cluster_id, 8 dimensions (0-100 each: energy, hunger, social_battery, luxury_affinity, nature_rawness, safety_need, foodie_focus, price_sensitivity), tags (weight, confidence), patience_meter | Azure SQL |
| Context Backpack (ephemeral) | user_name, location (room+resort), current_intent, weather_now (mm/h), active_suggestion | Cosmos DB (hot, dropped on intent change) |
| Product Record | product_id, price, margin_percent, availability_type (API/MANUAL/AFFILIATE), 5D dimension vector, tags, repeatability, hooks (family/culture/adventure variants), stats (conversion_rate, nps_avg, value_score) | Azure SQL (Products) + Azure AI Search (Commercial Shelf) |
| Shadow Ledger | transaction_id (UUID), booking_ref, user_id, provider_id, flow_type, total_amount (DECIMAL), commission_pct, receivable_amount, status (PENDING/CONFIRMED/CANCELLED/REFUNDED/REFERRED), invoice_batch | Azure SQL (Ledger) |
| Contract Rules | provider_id, rule_priority (product=1, seasonal=2, default=3), commission_rate, effective_date, expiry_date | Azure SQL (Contracts) |
| Tenant Config | tenant_id, brand_name, logo_url, concierge_avatar, font_family, colors (primary/accent/background), ui_mode | Azure SQL (Tenants) + CDN |
| Scoring Formula State | cluster_id, W1-W5 weights (sum to 1.0) — initialized Tabula Rasa, updated nightly by Optimizer | Azure SQL / Data Lake |
| A/B Hook State | product_id, cluster_id, hook_theme, impressions, conversion_rate, CHAMPION/CHALLENGER status | Azure SQL (Products/Stats) |
| Staff Priority Queue | conversation_id, urgency_score (Wait×1.5 + Mood×2.0 + VIP×10 + Confusion×5), assigned_staff | Cosmos DB (live queue) |
| RAG Shelves (4 indexes) | Commercial (product vectors+hooks), Cultural (stories/history), Practical (safety/WiFi bulletins), Internal (brand/Optimizer insights) | Azure AI Search (4 separate indexes) |
| Data Lake Raw Logs | event_type, user_id (SHA-256 hashed), cluster_id, event_payload, data_source (REAL/SYNTHETIC) | Azure Data Lake Gen2 |
| Mystery Shopper Records | agent_persona, data_source: Synthetic, weight (1.0→0.0 after 1,000 real users) | Azure Data Lake Gen2 (separate partition) |
| Itinerary / Booking Reference | booking_ref, reservation_items, confirmed/pending/suggested, gap_periods | Azure SQL (Itinerary) |
| Safety Bulletin | bulletin_id, resort_id, category (ice/route/weather), content, published_at, expires_at, severity | Azure AI Search (Practical Shelf) |
| Affiliate / Trackable Link | link_id, source_partner_id, signed_token, status (REFERRED_PENDING/RECONCILED), reconciliation_batch | Azure SQL (Ledger extension) |

---

## Briefing Flags — For A7 Spawn Prompt

### A2 → A7: Conversion Data Email Drafter Could Contribute
Every sent proposal writes an interaction record with `proposal_value_eur`, `tt_url`, `task_type`, and a `conversion` boolean + `outcome` label (Won/Lost/Still active) set by staff after client response. The `version_sequences` table captures exactly which itinerary components were added or removed between proposal versions, cross-referenced against final outcome — making it possible to identify which changes correlate with booking confirmation. This conversion-quality signal is unavailable in any commercial DMC tool.

### A3 → A7: Revenue Model Shift (3 sentences)
Finland DMC is transitioning from earning 15% commission on approximately 100 annual group bookings (B2B, relationship-dependent, staff-intensive) to earning 15% commission on every individual guest transaction across a network of resort tenants (B2C, automated, infinitely scalable). At 10,000 guest stays per year with €150 average AI-assisted spend, this generates €225,000 in commission revenue with no incremental labor cost beyond platform hosting and exception handling. The structural shift is not the commission rate — it is the elimination of the linear relationship between revenue and staff headcount, which is the core mechanism enabling Finland DMC to operate as an OTA-class volume business while maintaining DMC-quality local knowledge.

---

## Cross-Wave Conflicts and Tensions Identified

### Conflict 1: Two Different "Second Brains" in the System
- **A1** analyzes Second Brain as Claude Teams Projects (PRD v3 simplification) — Teams channels as data sinks, M365 connector for retrieval, no structured database.
- **A2** relies on Second Brain as a Supabase PostgreSQL schema (8 tables including clients, contacts, interactions) with pgvector for semantic search.
- **Resolution (by A2):** These are sequential, not competing. PRD v3 Teams-channel model is the Phase 0-1 interim; Supabase schema is the production target. PRD v3 Client Communications project = Email Drafter in manual mode, which automates into n8n+Supabase. **A5 must draw the integration map noting both states: current (Teams) and future (Supabase).**

### Conflict 2: Zone 1 → Zone 2 Data Flow Ambiguity
- **A1:** "B2C Travel Assistant gets nothing from Second Brain in transition period. Zone 1 data must not flow into Zone 2."
- **A3:** "Booking source data (operator reference) from Shadow Ledger flows to Second Brain to identify which B2B operators send high-value guests."
- **A4:** B2B Partner Dashboard (`GET /b2b/customers`) exposes guest satisfaction data to travel agencies.
- **Tension:** The Zone 1 / Zone 2 boundary is described at different levels of specificity. Shadow Ledger booking metadata (not PII) flowing to Second Brain appears permitted. Named guest data is prohibited. **A5 must draw the exact legal line with GDPR Article citations.**

### Conflict 3: Mood Evaluator Health Data — Not Flagged in Technical Spec
- **A3** flags that Mood Evaluator's "Needs_Accessibility" tag may = Article 9 health data, requiring explicit consent and mandatory DPIA.
- **A4** documents the full Mood Matrix schema (8 dimensions including tags with "Needs_Accessibility") without flagging this specific GDPR concern.
- **Implication for A6:** The Mood Matrix schema (Azure SQL) may need to be treated as special category data (Article 9) for the accessibility dimension. This changes consent, retention, and DPIA requirements for that specific field. **A6 must flag this in the data residency table.**

### Conflict 4: Payment Processor — No Agent Has Made a Call
- **A4** documents Adyen vs Stripe Connect as unresolved, with Phase 2 virtual card implications.
- No other agent addresses this.
- **A5 and A6 must both note this as an open dependency** that blocks Phase 2 integration design.

### No Contradiction With CRITICAL UPDATES
All agents correctly treated FinnConcierge as informational only. All agents avoided speculating about TT API (none needed TT API in Wave 1). Build methodology not reopened. PRD v3 treated as provisional with challenge rights (A1 and A2 both challenged and justified their positions).

---

## Agent 5 (Integration Architect) — Pre-Spawn Summary

**What A5 needs from this brief:**
- A1 briefing: 3 data entities Second Brain exposes + GDPR gap on Claude Teams
- A2 briefing: n8n/Supabase stack confirmed, company_id constraint, phase 2 interface open
- A4 briefing: Full API surface (inbound + outbound + staff endpoints)
- Conflict 1: Two-state Second Brain (Teams now, Supabase future) — map both in integration diagram
- Conflict 2: Zone 1/Zone 2 boundary — A5's critical output is to draw the legal line
- Conflict 4: Payment processor open — note in integration map

**A5 must read:** wave1-cross-brief.md (this file) as primary. Deep-read A1 Sections 2/3/4 and A4 Sections 2/5/6 only if cross-brief raises specific questions. Then read PRD v3 (40KB) and traveltree-api-status.md (4KB).

---

## Agent 6 (Database Architect) — Pre-Spawn Summary

**What A6 needs from this brief:**
- A4 briefing: Full 16-schema table with Azure services (in this document)
- A5 boundary message: TBD (A5 output not yet available — A6 will receive it in spawn prompt)
- Conflict 3: Mood Matrix "Needs_Accessibility" tag may = Article 9 health data — flag in Section 2
- Conflict 4: Payment processor open — note in data residency table
- Conflict 1: Two-state Second Brain — Supabase vs Teams data classification differs

**A6 must read:** wave1-cross-brief.md (this file) + A5 output Sections 1 and 4 only (after A5 completes).

---

*End of wave1-cross-brief.md | Lead: team-lead@dmc-synthesis | 2026-02-22*
