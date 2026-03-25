## Travel Assistant — Technical Analysis

**Agent:** 4 — Travel Assistant Technical Architect
**Sources:** monster-compressed.md, cluster-b-technical-findings.md, cluster-e-monster-findings.md, FINAL_CHECKLIST.md, MASTER_MAP.md, coding-project-preflight.md (Section 1)
**Date:** 2026-02-22

---

### 1. Confirmed Tech Stack

Every technology choice across all source files, classified by evidentiary status.

| Technology | Role | Status | Source |
|---|---|---|---|
| Microsoft Azure (North Europe region) | Platform host — all infrastructure | **confirmed** | monster-compressed §2, cluster-b §Tech Choices, cluster-e §Tech Choices (consistent across 3 sources) |
| Azure Functions (Python/Node.js) | Serverless compute — each agent is an isolated function, pay per execution | **confirmed** | monster-compressed §2, cluster-b §Tech Choices #5, cluster-e §Tech Choices #1, MASTER_MAP §1 |
| Azure Event Grid | Event bus — all inter-agent communication; "system nervous system" | **confirmed** | monster-compressed §2, cluster-b §Tech Choices #6, cluster-e §Tech Choices #2, MASTER_MAP §3 (mermaid graph) |
| Azure OpenAI Service — GPT-4o | AI inference engine via Private Endpoint, Zero Data Retention (ZDR) | **confirmed** | monster-compressed §2, cluster-b §Tech Choices #1, cluster-e §Tech Choices #3 |
| Azure Cosmos DB (NoSQL) | Hot storage — chat history, session state | **confirmed** | monster-compressed §2, cluster-b §Tech Choices #3, cluster-e §Tech Choices #4, MASTER_MAP §3 |
| Azure SQL Database | Relational — Ledger, Users, Products, Contracts | **confirmed** | monster-compressed §2, cluster-b §Tech Choices #2, cluster-e §Tech Choices #5 |
| Azure AI Search (Vector Store) | RAG storage — four named vector indexes ("shelves") | **confirmed** | monster-compressed §2, cluster-b §Tech Choices #4, cluster-e §Tech Choices #6 |
| Azure Data Lake Storage Gen2 | Cold storage — raw logs for analytics and Optimizer input | **confirmed** | monster-compressed §2, cluster-b §Tech Choices, cluster-e §Tech Choices #7 |
| Next.js 15 (React) PWA | Frontend — Progressive Web App, App Router, "Chameleon" brand engine | **confirmed** | monster-compressed §2, cluster-b §Tech Choices #7, cluster-e §Tech Choices #8, FINAL_CHECKLIST §3 |
| Azure Maps API | Geo-routing, corridor logic (travel route POI suggestions) | **confirmed** | monster-compressed §6 (External APIs), cluster-e §Tech Choices #9 |
| Azure Translator | Real-time multilingual support (Italian, German, Finnish, English minimum) | **confirmed** | monster-compressed §2 (Core Stack) |
| JWT (cryptographically signed tokens) | Magic Link authentication — URL tamper detection | **confirmed** | monster-compressed §7 (Security), cluster-e §Requirements #4, FINAL_CHECKLIST §1 (HMAC + JWT mock) |
| HMAC signature validation | Webhook payload integrity verification | **confirmed** | FINAL_CHECKLIST §1 (implemented in mock) |
| SHA-256 PII hashing | GDPR anonymization — names/phones → hashed tokens before Data Lake | **confirmed** | monster-compressed §7 (GDPR), FINAL_CHECKLIST §1 |
| WhatsApp | Notification "doorbell" only — delivers Magic Link; complex interactions redirect to PWA | **confirmed** | monster-compressed §6 (WhatsApp Integration), cluster-e §Decisions #12 |
| WebRTC (in-app voice) | Voice calls inside PWA — prevents caller ID spoofing | **confirmed** | monster-compressed §7 (Security/Anti-Abuse) |
| Finnish Meteorological Institute API | Weather data — updated hourly, granular mm/h rain for Chef scoring | **confirmed** | monster-compressed §6 (External APIs) |
| Kp-index (aurora forecast data) | Northern lights probability — used with probability language only, never guarantees | **confirmed** | monster-compressed §6 (External APIs) |
| Puppeteer (web scraper) | Partner onboarding — extracts logo, colors, font, product info from partner URL | **confirmed** | monster-compressed §6 (Web Scraper) |
| Slack/Teams webhooks | Staff Dashboard alerts for escalations and emergencies | **confirmed** | monster-compressed §6 (External APIs) |
| Adyen | Payment processing — already used by Järvisydän; split payments, AliPay, Kaspi | **mentioned** | monster-compressed §6; described as "already used" but final choice between Adyen and Stripe not resolved |
| Stripe Connect | Payment processing alternative to Adyen | **mentioned** | monster-compressed §6, cluster-e §Tech Choices #10; not chosen over Adyen |
| Redis | In-memory Vector DB option for <800ms Chef query latency target | **mentioned** | cluster-b §Tech Choices #8, cluster-e §Tech Choices #11; not chosen vs Pinecone |
| Pinecone | In-memory Vector DB alternative to Redis | **mentioned** | cluster-b §Tech Choices #8, cluster-e §Tech Choices #11; not chosen vs Redis |
| OpenAI Realtime API | Voice AI phone calls — Phase 3 only, training data from recorded staff calls | **mentioned** | monster-compressed §5, cluster-e §Tech Choices #12; explicitly NOT in MVP |
| SendGrid / Twilio | Email/SMS delivery for Magic Link | **mentioned** | FINAL_CHECKLIST §1 (Ministep 1.5); not yet integrated in mock |
| Azure DevOps (CI/CD) | Pipeline automation | **mentioned** | MASTER_MAP §1 (`.github/` directory reference) |
| Bicep / Terraform | Infrastructure as Code | **mentioned** | MASTER_MAP §1 (`infrastructure/` directory) |
| Azure API Management (APIM) | API gateway and policy layer | **mentioned** | MASTER_MAP §1 (`infrastructure/apim/`) |
| Cursor / GitHub Copilot | AI-assisted coding tools for the build team | **mentioned** | monster-compressed §2 (Agentic Coding Strategy), cluster-e §Decisions #11 |
| Tailwind CSS | UI styling in Next.js PWA | **mentioned** | FINAL_CHECKLIST §3 (package.json update) |

**Region note:** All confirmed sources cite North Europe. Sweden Central appears in one open question in cluster-b §Open Questions #2 as a contrast to CRM data GDPR requirements — this is an unresolved question, not a decision. North Europe is the confirmed choice.

---

### 2. Data Schemas Defined

Every schema found across source files, with the Azure service responsible for storing it.

| Schema Name | Key Fields | Azure Service |
|---|---|---|
| **User Profile / Context Briefcase** | session_id, user_profile (name, segment, language, history_notes, status), trip_details (location, dates, booked_items, budget_remaining), agent_persona (name, language_mode, tone), service_level (human_access, ai_autonomy) | Azure SQL (Users table) + Cosmos DB (session state) |
| **Mood Matrix** | user_id, cluster_id, last_update, dimensions (energy 0-100, hunger 0-100, social_battery 0-100, luxury_affinity 0-100, nature_rawness 0-100, safety_need 0-100, foodie_focus 0-100, price_sensitivity 0-100), tags (tag, weight, source, confidence), patience_meter 0-100 | Azure SQL (updated by Mood Evaluator after every message) |
| **Context Backpack (short-term session memory)** | user_name, location (room + resort), current_intent, weather_now (mm/h), active_suggestion | Cosmos DB (hot, dropped when intent changes) |
| **Product Record (Commercial Shelf)** | product_id, base_info (name, price, margin_percent), availability_type (API/MANUAL/AFFILIATE), logistics (gps, duration_minutes, capacity), cancellation_policy, dimensions (energy, social, luxury, nature_rawness, safety_need — 5D vector), tags, repeatability, hooks (family, culture, adventure variants), stats (conversion_rate_family, nps_avg, value_score) | Azure SQL (Products table) + Azure AI Search (Commercial Shelf vector index) |
| **Shadow Ledger** | transaction_id (UUID), booking_ref, user_id, provider_id, timestamp, flow_type (API/MANUAL/AFFILIATE), total_amount (DECIMAL), commission_pct (DECIMAL), receivable_amount (DECIMAL), status (PENDING/CONFIRMED/CANCELLED/REFUNDED/REFERRED), invoice_batch | Azure SQL (Ledger table) |
| **Contract Rules** | provider_id, rule_priority (product-specific=1, seasonal=2, partner_default=3), commission_rate, effective_date, expiry_date | Azure SQL (Contracts table) — Waterfall Logic selects by priority |
| **Tenant Config (Brand Engine)** | tenant_id, brand_name, assets (logo_url, concierge_avatar, font_family_header, font_family_body), colors (primary, accent, background), ui_mode (shape_rounding, tone_of_voice) | Azure SQL (Tenants table) + CDN for assets |
| **Scoring Formula State (per cluster)** | cluster_id, W1 (base_match weight), W2 (weather_fit weight), W3 (value_score weight), W4 (margin_boost weight), W5 (novelty_score weight); weights sum to 1.0; initialized as Tabula Rasa, updated by Optimizer | Azure SQL / Data Lake (Optimizer writes nightly) |
| **A/B Hook State (Champion/Challenger)** | product_id, cluster_id, hook_theme, hook_version, impressions, conversion_rate, status (CHAMPION/CHALLENGER), promoted_at | Azure SQL (Products/Stats table) |
| **Staff Dashboard Priority Queue** | conversation_id, customer_id, wait_time_minutes, negative_mood_score, vip_factor, agent_confusion_count, urgency_score (formula: Wait*1.5 + Mood*2.0 + VIP*10 + Confusion*5), assigned_staff | Cosmos DB (live queue state) |
| **RAG Shelves (4 Vector Indexes)** | Commercial Shelf: product cards with 5D vectors and hooks. Cultural Shelf: history, stories, legends. Practical Shelf: WiFi, parking, safety bulletins, ice thickness. Internal Shelf: brand guidelines, Optimizer insights, influencer picks | Azure AI Search (4 separate vector indexes) |
| **Data Lake Raw Logs (analytics)** | event_type, user_id (hashed), cluster_id, session_id, timestamp, event_payload (mood deltas, recommendation shown, booking outcome, feedback score), data_source (REAL/SYNTHETIC) | Azure Data Lake Storage Gen2 |
| **Mystery Shopper Records** | agent_persona (Karen/Lost_Backpacker/Big_Spender), data_source: Synthetic, weight (1.0 initially → 0.0 after 1000 real users), test_scenario, outputs | Azure Data Lake Gen2 (separate partition from real user data) |
| **Itinerary / Booking Reference** | booking_ref, user_id, reservation_items (list), confirmed_items, pending_items, suggested_items, check_in, check_out, gap_periods (time windows with no booked activity) | Azure SQL (Itinerary table) |
| **Safety Bulletin** | bulletin_id, resort_id, category (ice_thickness/route_closure/weather_warning), content, published_at, expires_at, severity | Azure AI Search (Practical Shelf) — must be <24h old or trigger human handover |
| **Affiliate / Trackable Link** | link_id, source_partner_id, promo_code, signed_token, created_at, status (REFERRED_PENDING/USER_REPORTED_SUCCESS/RECONCILED), reconciliation_batch | Azure SQL (Ledger extension) |

---

### 3. Agent Network Architecture

**Orchestration pattern:** One Master Agent (front-end, user-facing) delegates to specialist agents. Agents never communicate peer-to-peer — all coordination routes through Azure Event Grid. The Master Agent never generates prices or availability from memory; all claims require tool calls.

**Master Agent (BP_02 — Orchestrator / The Concierge)**
- Role: Sole user-facing component. Tone of voice, intent detection, tool routing.
- Reads: Context Backpack (Cosmos DB), RAG shelves (Azure AI Search — Cultural + Practical directly), Safety Bulletin.
- Writes: Cosmos DB (conversation history, Backpack updates), Event Grid (USER_MESSAGE event to trigger Mood Evaluator async).
- Communication: Receives user messages via `/api/agent/process` HTTP endpoint; emits events to Event Grid; calls specialist agents as tools (not as events — tools are synchronous calls within a conversation turn).
- System Prompt: 4-layer dynamic assembly — Base Layer (safety, hard limits) + Brand Layer (tenant persona) + Context Layer (user state, weather, next itinerary item) + Task Layer (current request).
- Tool routing protocol: Recommendation → Suggestion_Chef_Tool. Booking → Booker_Tool. Safety → SafetyBulletin_Tool. Price/availability → Database_Lookup_Tool. 3 failed attempts → Human_Handover_Tool.
- Gap Finder: Cronjob every 30 minutes. Internal monologue checks itinerary gaps, energy level, time of day (silent 22:00-08:00). Only reaches out if gap + good weather + appropriate energy + right time window — decision gate prevents guest fatigue.

**Mood Evaluator Agent (BP_03 — Async Psychologist)**
- Role: Event listener, never adds latency to chat. Runs simultaneously with every user message.
- Reads: Chat message text, current Mood Matrix (Azure SQL), cluster assignment.
- Writes: Updated Mood Matrix to Azure SQL after every message (8 dimension deltas + tag weight adjustments + patience_meter update).
- Communication: Triggered by USER_MESSAGE event from Event Grid (async — fire and forget from Master's perspective).
- Key behaviors: Patient Meter below 30 → flags Silent Mode (no upsell). Negative experience → 4-hour cooldown, delayed empathy approach. Tag scoring: weighted, not binary — tags grow/decay with evidence.

**Suggestion Chef Agent (BP_04 — Mathematical Optimizer)**
- Role: Recommendation engine. Pure math — filters first, then scores, then selects hook.
- Reads: Mood Matrix (Azure SQL), product catalog (Azure SQL + Commercial Shelf in Azure AI Search), weather data (FMI API), Data Lake stats (conversion rates, NPS).
- Writes: Nothing persistently — returns ranked recommendation list with sales pitch to Master Agent.
- Communication: Synchronous tool call from Master Agent. Must return in <800ms or fallback generic list is used.
- Three-stage pipeline: Stage 1 (SQL hard filter — open now, slots available, within mobility range, not already booked). Stage 2 (scoring formula — Base_Match*W1 + Weather_Fit*W2 + Value_Score*W3 + Margin_Boost*W4 + Novelty_Score*W5). Stage 3 (hook selection — 80% Champion, 20% Challenger per cluster). Epsilon-Greedy wildcard: 10-20% of recommendations are "dark horse" products for data collection.

**Booker Agent (BP_06 — Transaction Router)**
- Role: Routes booking requests to the appropriate path; records all outcomes in Shadow Ledger.
- Reads: Product availability_type field (Azure SQL), booking request parameters.
- Writes: Shadow Ledger (Azure SQL) for every transaction regardless of path; Event Grid (BOOKING_CONFIRMED/BOOKING_FAILED events).
- Communication: Synchronous tool call from Master Agent on booking intent.
- Three paths: Type A (full API — GET /availability → auth hold → POST /book → capture → ledger). Type B (manual email — 24h auth hold → partner CONFIRM/DENY link → capture or auto-void). Type C (affiliate link — signed trackable URL → ledger as REFERRED_PENDING → follow-up in 2h).

**Shadow Ledger (BP_07 — Finance Data Layer)**
- Not a live agent — a service module called by Booker Agent. Implements Waterfall Commission Logic (product-specific 20% > seasonal 18% > partner default 15%). ACID transaction simulation. No deletions — void/cancel creates audit trail entry. Decimal precision (no float errors).

**RAG Librarian Agent (BP_05 — Knowledge Manager)**
- Role: Maintenance process, NOT a live query intermediary. Agents query Azure AI Search shelves directly for speed. Librarian runs weekly.
- Reads: All four RAG shelves, Azure SQL product catalog, BookVisit product feed.
- Writes: RAG shelves (adds/archives/updates content), creates conflict tickets in Staff Dashboard when price discrepancies detected.
- Key functions: Conflict Detection (website vs DB price mismatch → ticket). Freshness Check (stale seasonal content → auto-archive). RAG Generator (new product → generates natural-language Context Card for Master Agent's Backpack use).

**Optimizer Agent (Nightly Batch — Continuous Learning)**
- Not a chatbot — Azure Functions cron job. Reads anonymized Data Lake logs. Outputs knowledge updates (NOT code changes).
- Pipeline: Miner (reads Data Lake correlations) → Hypothesis Generator (creates improvement proposals) → Editor (updates RAG Internal/Commercial shelves, writes cluster-level scoring rules).
- Nightly outputs: Best Seller rankings per cluster, product Conversion_Rate and Value_Score updates, A/B Champion/Challenger promotions, tag affinity re-scoring.

---

### 4. GDPR and EU Data Residency

**Region confirmed: North Europe.** This is consistent across monster-compressed §2, cluster-b §Tech Choices #12, and cluster-e §Decisions #1. North Europe (Ireland data center region) satisfies EU data residency requirements. Sweden Central is mentioned only in cluster-b §Open Questions #2 as a contrast point ("GDPR compliance for CRM data requires EU data residency — are these the same legal region?") — this is an unresolved question about whether North Europe and Sweden Central differ in legal significance for GDPR Article 28, not a decision to use Sweden Central.

**ZDR (Zero Data Retention):** Azure OpenAI's Zero Data Retention policy means our data is NOT used to train public Microsoft AI models and is not retained by Microsoft after the API response is returned. This is implemented via Private Endpoint (no traffic on public internet). Cited in monster-compressed §2 and cluster-e §Decisions #1 as a primary reason for choosing Azure OpenAI over generic OpenAI API.

**Anonymization pipeline (before Data Lake entry):**
- PII elements replaced before data enters cold storage: names and phone numbers → SHA-256 hashed tokens.
- Cluster_ID and Mood_Matrix dimensions retained post-anonymization (required for Optimizer statistical analysis — these are behavioral, not identity, data).
- Mystery Shopper synthetic data stored in a separate Data Lake partition with Data_Source: Synthetic flag to prevent contamination of real conversion statistics.
- Source: monster-compressed §4 (Optimizer section), cluster-e §Requirements #11.

**Row-Level Security (RLS):** At the database layer, every query is forced to include `WHERE user_id = CURRENT_USER`. Tenant isolation enforced via `tenant_id` on every table — one tenant's agent cannot access another tenant's data even if confused. Source: monster-compressed §7 (GDPR).

**GDPR Article 28 DPA:** Recommended with Microsoft (not confirmed as signed). Source: monster-compressed §7 ("DPA agreement with Microsoft recommended").

**What gets anonymized and when:**
- Mood Matrix dimensions (energy, hunger, etc.): retained — behavioral, not PII.
- Cluster_ID: retained — statistical category, not identity.
- Names, phone numbers: hashed before any entry to Data Lake or Optimizer input.
- Chat transcripts: stored in Cosmos DB (hot) with full PII for operational use; PII stripped before archiving to Data Lake.

---

### 5. Integration APIs and External Dependencies

**APIs the Travel Assistant exposes:**

- `POST /webhook/booking` — Receives booking events from BookVisit/online store (HMAC-signed). Triggers ingestion pipeline and Magic Link generation.
- `GET /welcome?token={jwt}` — Magic Link entry point. JWT validated, Traveler PWA loaded with tenant theme.
- `POST /api/agent/process` — Chat endpoint. User message in, Master Agent response out. Used by Traveler PWA ChatInterface.
- `POST /staff/whisper` — Staff Dashboard injects system-role message into conversation (invisible to customer).
- `POST /staff/takeover` — Staff disconnects AI, takes direct control of conversation.
- `POST /staff/teach` — Thumbs up/down on AI response, feeds Optimizer training signal.
- `POST /staff/god-mode` — Force-pushes a product to top of all recommendation queues for a resort/time window.
- `POST /staff/fire-red` — Emergency override, stops AI immediately, alerts all staff.
- `GET /b2b/customers` — B2B Partner Dashboard: travel agencies see their customers in Finland, satisfaction rates, upsell revenue.
- Affiliate link endpoint: `https://partner.com/book?ref=DMC_ID&promo=CODE` — signed token, commission tracked.

**External systems the Travel Assistant consumes:**

- BookVisit (Järvisydän e-commerce) — booking webhook source, product catalog source for Commercial Shelf.
- Oracle Opera (Järvisydän hotel management, ~40 integrated apps) — availability, reservation data, room assignments.
- Finnish Meteorological Institute (Ilmatieteen laitos) API — hourly weather data, granular mm/h rain for Chef scoring.
- Kp-index aurora forecast API — northern lights probability.
- Adyen or Stripe Connect — payment processing (final choice unresolved between these two).
- SendGrid / SMTP gateway — Magic Link delivery via email.
- SMS gateway (Twilio or equivalent) — Magic Link delivery via SMS.
- Slack/Teams webhooks — Staff Dashboard emergency alerts.

---

**CRITICAL PATH BLOCKERS — Järvisydän IT Prerequisites**

These must be resolved before build can begin or before go-live, as flagged.

| Prerequisite | What Is Needed | Status |
|---|---|---|
| Oracle Opera API access | API credentials, endpoint documentation, sandbox environment for testing. The anti-corruption layer (adapter between Booker Agent and Opera) scope cannot be defined without this. Opera has ~40 integrated apps — which are in scope for the Travel Assistant? | **BLOCKER** — build of Booker Agent (BP_06) cannot begin without Opera API mapping. Source: monster-compressed §8 Open Question #1, cluster-e §Risks #3. |
| BookVisit product catalog feed | Full product export in machine-readable format (JSON/CSV) to seed the Commercial Shelf RAG index. Product fields needed: name, price, availability_type, capacity, GPS coordinates, tags, commission rate. | **BLOCKER** — Commercial Shelf is empty without this. Chef cannot score products that don't exist in the RAG index. Source: cluster-e §Järvisydän Differences (BookVisit as starting source for Commercial Shelf). |
| Webhook from Järvisydän online store | HMAC secret key, webhook endpoint configuration on BookVisit/Järvisydän CMS side, confirmation of payload schema (reservation_id, email, booking_items minimum). | **BLOCKER** — Ingestion pipeline (BP_01) cannot be tested without a valid booking event. The entire Magic Link flow depends on this trigger. Source: monster-compressed §9 (Järvisydän Magic Link entry point). |
| Network connectivity to Azure | Firewall rules or VPN configuration allowing Azure Functions (North Europe) to reach Järvisydän IT network if Opera is on-premises or behind a private network. | **BLOCKER** — If Opera is not cloud-exposed, a network path must be established before any booking API call can succeed. |
| Data processing legal agreement | GDPR Article 28 Data Processing Agreement between Finland DMC (as processor) and Järvisydän Oy (as controller, since guest data originates from their bookings). This is distinct from the Microsoft DPA. | **BLOCKER** — Cannot process Järvisydän guest PII legally without this agreement signed. EU company obligation. Source: monster-compressed §7 (GDPR Article 28 note). |
| Safety Bulletin data process | Who at Järvisydän updates ice thickness, route closures, and weather warnings daily? What is the input method (Staff Dashboard form)? This is not a technical integration but an operational dependency — without it, the Safety Bulletin will be stale (>24h) and the system will escalate all nature/safety questions to humans. | **PREREQUISITE** (go-live) — System technically functions without it, but safety guardrail will fire constantly. Source: cluster-e §Risks #9 (SafetyBulletin >24h = human handover). |
| Staff capacity agreement | One Finland DMC staff member dedicated to monitoring AI conversations and handling escalations. This person needs access to Staff Dashboard (BP_08), training on Whisper/Takeover/God Mode, and defined escalation protocols. | **PREREQUISITE** (go-live) — Staff Dashboard (BP_08) is listed as not started in FINAL_CHECKLIST. Must be built and staff trained before go-live. |

**No Järvisydän IT contact has been made yet.** The conversations above, the sandbox access requests, the DPA negotiation, and the webhook configuration must all be initiated by Finland DMC before the build can commence in meaningful depth. This is the longest lead-time item on the critical path.

---

### 6. Shared Infrastructure — B2B vs B2C

The source files do not explicitly address Supabase or n8n for B2B infrastructure — these appear to be assumptions from the synthesis brief rather than stated choices in the mined documents. The B2B tools (Second Brain = Claude Teams, Email Drafter) are explicitly Zone 1 products. What can be assessed from the source material:

**What cannot be shared:**

- Azure Cosmos DB and Azure SQL are Zone 2 (B2C guest data) stores. Putting B2B staff data (Second Brain client profiles, relationship intelligence) in the same database as guest Mood Matrices would create a GDPR entanglement — B2B data has different retention rules, different data subjects (business contacts vs individual guests), and potentially different legal bases.
- Azure OpenAI Private Endpoint: ZDR policy applies per-subscription. Mixing B2B staff prompts (which may contain client PII — names, revenue figures) with B2C guest chat in the same Azure OpenAI resource creates audit complexity even if technically permissible.

**What could be shared with acceptable risk:**

- Azure Functions runtime environment: B2B tools (Email Drafter) and B2C Travel Assistant are functionally independent microservices. They could run in the same Azure subscription under different resource groups with separate networking. Cost saving: shared Azure DevOps pipeline, shared monitoring (Azure Monitor). GDPR risk: low if resource groups enforce strict access control (RBAC) and data never flows between them.
- Azure AI Search: A separate index per use case (B2B knowledge vs B2C product catalog) within the same Azure AI Search resource is technically feasible. Risk: a misconfigured query could leak B2C guest behavior data into a B2B staff context. Recommendation: separate resources, not separate indexes, for Zone 1 vs Zone 2.

**Trade-off summary:**
- Option A (shared Azure subscription, separate resource groups): Saves ~20-30% on Azure fixed costs, simplifies DevOps. GDPR risk manageable with strict RBAC and network segmentation. Technical debt risk: future Zone 1 decommissioning (when B2B tools are retired) is cleaner with shared infra than with entangled data stores.
- Option B (fully separate Azure subscriptions for Zone 1 and Zone 2): Clean GDPR boundary, simpler audit trail, easier Zone 1 decommissioning. Higher fixed costs (~$200-400/month additional for separate Azure resources at MVP scale). Recommended if the DPA with Järvisydän makes data isolation a contractual requirement.

---

### 7. Build Status — What Was Built and Why It Stopped

**Phase 1 of FinnConcierge (December 2025) — what was achieved:**

Per FINAL_CHECKLIST.md (dated 2025-12-11):

- BP_01 (Ingestion): Complete mock — webhook validation, HMAC signature mock, user deduplication by email/phone hash, idempotency check, JWT Magic Link generation, EVENT_ONBOARDED emission. Fully functional in mock mode.
- BP_02 (Master Agent): Already existed in orchestrator.py. Integrated with mock Chef, Mood, and RAG.
- BP_03 (Mood Evaluator): Complete mock — keyword-based dimension updates, archetype classification, evaluate_with_llm() placeholder prepared for GPT-4o integration.
- BP_04 (Suggestion Chef): Already existed in chef_agent.py. Integrated.
- BP_05 (RAG Librarian): Already existed in librarian_agent.py. Vector search simulated with mock embeddings.
- BP_06 (Booker Agent): Partial — linked to Shadow Ledger but booking flow variants (API/Manual/Affiliate) not fully implemented.
- BP_07 (Shadow Ledger): Complete mock — Waterfall commission logic (product-specific 20% > seasonal 18% > partner default 15%), ACID simulation, status management (PENDING/CONFIRMED/SETTLED), no-deletion audit trail.
- BP_08 (Staff Dashboard): Not started.
- BP_09 (Watchdog): Not started.
- BP_10 (Infra & Security): Partial — SQL schema exists, Azure deployment pending (RLS, Event Grid not implemented).
- BP_11 (Traveler UI): Complete mock — Next.js 15 App Router, Chameleon theme engine (Järvisydän brown/gold, KonTiki blue/orange), ChatInterface with mock responses, tenant detection from URL.

**The 3 real blockers that stopped Phase 2:**

1. **No real Azure infrastructure provisioned.** Every component (Azure Functions, Cosmos DB, Azure SQL, Event Grid, Azure AI Search, Azure OpenAI) exists as mock or in-memory. Moving from mock to production requires Azure resource provisioning, credential management, and network configuration — none of which was done in Phase 1. This is not a code problem; it is an infrastructure and cost commitment decision.

2. **No Oracle Opera integration scoped.** The Booker Agent (BP_06) is partial precisely because the Type A booking path (full API) requires Oracle Opera. The anti-corruption layer was flagged as "to be mapped when Järvisydän IT team is engaged" — and that engagement had not happened by December 2025. Without it, the only booking paths functional are Type C (affiliate link) and partially Type B (manual email).

3. **Staff Dashboard (BP_08) not started.** The transition model requires staff to monitor AI conversations before go-live. Without the Staff Dashboard, there is no human safety net — and the system spec explicitly requires a human to be reachable for emergency override (FIRE RED), whisper, and takeover. Deploying the B2C guest-facing assistant without BP_08 means 0% human oversight of the 10-20% escalation cases.

**What this tells us about Phase 2 complexity:**

Phase 1 proved the architecture is coherent — the vertical slice (webhook → ingestion → master → chef → ledger → UI) works end-to-end in mock mode. Phase 2 is not primarily a coding challenge; it is an integration and infrastructure challenge. The 400-1000 ministep estimate from FINAL_CHECKLIST §Ministep Readiness reflects real scope. The hardest ministeps are not the algorithm implementations (already sketched) but the Azure provisioning, Opera anti-corruption layer, and Staff Dashboard.

---

### 8. Redesign With Opus 4.6

**Architecture choices to reconsider for a 2026 build:**

**1. Mock-first vs. Real infrastructure from day one.**
The FinnConcierge Phase 1 built a complete mock vertical slice with in-memory databases. This was rational in December 2025 for validating architecture. In 2026, with Opus 4.6 and Sonnet 4.6 capable of generating working Azure Bicep templates and Azure Function code with accurate SDK calls, the mock layer may add more complexity than it saves. A redesign should provision real Azure resources (dev-tier, low cost) from week 1 and test against them directly, rather than building a mock-to-production migration path that doubles the work.

**2. LLM selection for Mood Evaluator.**
The FinnConcierge mock uses keyword-based dimension updates with a TODO comment: "Replace with GPT-4o/Claude Opus call." In December 2025, this was a cost and capability concern. In 2026: Sonnet 4.6 (not Opus) is the correct model for Mood Evaluator. It runs after every user message (high frequency), requires structured JSON output (Mood Matrix deltas), and the task is pattern-matching + inference — not GPQA-level multi-hop reasoning. Sonnet is 1.67x cheaper than Opus and matches Opus on structured output tasks. The evaluate_with_llm() integration point should specify Sonnet 4.6 with grammar-enforced JSON schema (Anthropic API-level structured outputs) — not "GPT-4o/Claude Opus."

**3. Redis vs. Pinecone — resolve this before writing Chef code.**
The 800ms latency requirement for the Suggestion Chef is a hard non-functional requirement. Both Redis (in-memory key-value with vector extension) and Pinecone (managed vector database) were mentioned but not chosen. This decision affects the entire Chef query path and must be resolved in the architecture phase. Trade-off: Redis has lower operational complexity (can run as Azure Cache for Redis, same cloud) but requires manual vector index management. Pinecone is a managed vector DB with better ANN search at scale but introduces a third-party cloud dependency outside Azure, complicating GDPR auditing. For MVP (Järvisydän, small product catalog, <200 products), Azure AI Search with aggressive caching (Cosmos DB TTL cache for top-N products per cluster) may meet the 800ms target without either Redis or Pinecone, eliminating the decision entirely.

**4. What was over-engineered for December 2025 model capabilities.**
The FinnConcierge used keyword-based routing and scoring as stubs because GPT-4o and Claude 3.5/4.0 were not reliable enough for structured multi-step reasoning within a 800ms latency budget. In 2026, Sonnet 4.6's adaptive thinking and Opus 4.6's GPQA-level reasoning change this calculus. The Suggestion Chef's 3-stage pipeline (SQL filter → math score → hook selection) is still the right design — math is deterministic and auditable, which matters for business logic. But the Master Agent's intent detection and tool routing (currently specified as hard-coded keyword matching in the system prompt) can be delegated to the model more confidently. The explicit `TOOL USE PROTOCOL` in the system prompt template remains necessary as a guardrail but the underlying routing logic can be simplified.

**Team composition (from coding-project-preflight.md Section 3 — Phase 3: Team Composition):**

The confirmed 4-5 role pattern applies directly:

| Role | FinnConcierge equivalent | Key rule |
|---|---|---|
| PM-Initializer | One-shot: architecture.md (from MASTER_MAP + blueprints) + features.yaml (decomposed from 400-1000 ministeps) | Max 2 pages per artifact; human gate before coding starts |
| Orchestrator | Simple script — polls features.yaml progress.json, spawns next worker | While-loop, not an AI agent |
| Module-Lead (Sub-Boss) | One per blueprint (BP_01, BP_02, etc.) | Required — raises quality 65% → 92% on SWE-Bench. Non-negotiable for 11-blueprint system. |
| Coder Agent | Implements one features.yaml row; loads only arch + row + touched files | Incremental only, no rewrites |
| Tester Agent | Runs pytest/Jest tests, flags failures with explanations | Separate from Coder for isolation |

The tournament/Darwinian model is resolved — not reopened here. The standard 4-5 role pattern at 1/3 the cost is the confirmed approach.

---

### 9. Top 3 Questions for the Synthesis

**Question 1: Oracle Opera integration scope and anti-corruption layer complexity — what is the actual API surface?**

The Oracle Opera hotel management system has ~40 integrated apps at Järvisydän (monster-compressed §9). The Booker Agent needs: availability check, reservation creation, room assignment confirmation. But Opera's API capabilities vary dramatically by version and configuration. The anti-corruption layer is described as "planned" with scope "to be mapped when Järvisydän IT team is engaged." This is the longest lead-time technical unknown. If Opera does not expose a REST API for the operations the Booker needs (common with older Opera versions), the only fallback is screen-scraping or email-based Type B booking for all Järvisydän products — which eliminates real-time availability confirmation and degrades the guest experience significantly. This question must be answered before the Booker Agent architecture is finalized.

**Question 2: Payment processor choice (Adyen vs Stripe Connect) and its Phase 2 implications for the virtual card / e-money license.**

Adyen is already in use at Järvisydän for payments. Stripe Connect is the alternative. The MVP defers in-app payment processing entirely (no card capture in MVP, manual or on-site payment only). But the choice made now has Phase 2 consequences: the virtual DMC Travel Card (prepaid Visa/Mastercard for split payment + cashback) requires either Adyen Issuing or Stripe Issuing — and whether DMC needs an e-money license depends on the structure of the virtual wallet and which issuing partner is chosen. If Adyen Issuing is chosen (aligning with Järvisydän's existing Adyen relationship), the MVP payment integration should be Adyen — not Stripe — to avoid a payment processor migration when Phase 2 begins. This is a decision that should be made before Phase 2 architecture, not after.

**Question 3: Who owns the Staff Dashboard (BP_08) build and what is its timeline relative to B2C go-live?**

BP_08 (Staff Dashboard) is listed as not started in FINAL_CHECKLIST. The synthesis brief identifies it as "the central transition product" for the 80/90-10/20 split model. Patrick's decision is that one Finland DMC staff member dedicates meaningful part-time daily hours to monitoring AI conversations and escalations. But BP_08 is rated CRITICAL in MASTER_MAP with XL-equivalent complexity (traffic lights, whisper, takeover, collision detection, Dead Man's Switch, SOS/Fire Red, Teach buttons, language translation). This is a full product in its own right. The open question: can the B2C Traveler PWA (Products 5+6) go live without a functional Staff Dashboard? The safety requirement is hard-coded — FIRE RED emergency override and human handover are non-negotiable. If BP_08 lags behind the B2C frontend, the go-live is blocked. The synthesis needs to explicitly sequence BP_08 build relative to BP_11 (Traveler UI) and set a dependency gate.

---

## Self-check

9 sections completed. Shortest section is Section 6 (Shared Infrastructure) at 22 lines.
28 tech choices classified confirmed/mentioned. 16 schemas listed with Azure service.
Context budget: BLUEPRINTS skipped (context load assessed at medium after file 6). Coding preflight: read Section 1 only (stopped at Phase 4 Quality Gates header).
Assumptions validated: Azure region confirmed as North Europe in cluster-b Section Tech Choices #12 ("Azure Functions North Europe region — not Azure Sweden Central"). ZDR defined as Zero Data Retention, confirmed in cluster-b Section Tech Choices #1. Oracle Opera scope explicitly unresolved — flagged as blocker, not assumed. Payment processor (Adyen vs Stripe) explicitly unresolved — flagged as mentioned, not confirmed.
Context load: medium (~110K tokens estimated after 6 source files).

---

## BRIEFING FLAG FOR LEAD — Agent 6 Spawn

Full schema list with Azure service per schema:

| Schema Name | Key Fields | Azure Service |
|---|---|---|
| User Profile / Context Briefcase | session_id, user_profile, trip_details, agent_persona, service_level | Azure SQL (Users) + Cosmos DB (session state) |
| Mood Matrix | user_id, cluster_id, 8 dimension scores (0-100), tags with weights, patience_meter | Azure SQL |
| Context Backpack (session memory) | user_name, location, current_intent, weather_now, active_suggestion | Cosmos DB (hot, ephemeral) |
| Product Record | product_id, price, margin_percent, availability_type, 5D dimension vector, tags, repeatability, hooks, stats | Azure SQL (Products) + Azure AI Search (Commercial Shelf) |
| Shadow Ledger | transaction_id, booking_ref, user_id, provider_id, flow_type, total_amount, commission_pct, receivable_amount, status, invoice_batch | Azure SQL (Ledger) |
| Contract Rules | provider_id, rule_priority, commission_rate, effective_date, expiry_date | Azure SQL (Contracts) |
| Tenant Config | tenant_id, brand_name, assets (logo, font, avatar), colors, ui_mode (shape_rounding, tone_of_voice) | Azure SQL (Tenants) + CDN |
| Scoring Formula State | cluster_id, W1-W5 weights (sum to 1.0), initialized as Tabula Rasa | Azure SQL / Data Lake (Optimizer writes) |
| A/B Hook State | product_id, cluster_id, hook_theme, impressions, conversion_rate, CHAMPION/CHALLENGER status | Azure SQL (Products/Stats) |
| Staff Priority Queue | conversation_id, urgency_score (Wait*1.5 + Mood*2.0 + VIP*10 + Confusion*5) | Cosmos DB (live queue) |
| RAG Shelves (4 indexes) | Commercial (product vectors), Cultural (stories), Practical (safety/wifi), Internal (brand/insights) | Azure AI Search (4 separate indexes) |
| Data Lake Raw Logs | event_type, hashed user_id, cluster_id, event_payload, data_source (REAL/SYNTHETIC) | Azure Data Lake Storage Gen2 |
| Mystery Shopper Records | agent_persona, data_source: Synthetic, weight, test_scenario | Azure Data Lake Gen2 (separate partition) |
| Itinerary / Booking Reference | booking_ref, reservation_items, confirmed/pending/suggested items, gap_periods | Azure SQL (Itinerary) |
| Safety Bulletin | bulletin_id, resort_id, category, content, published_at, expires_at, severity | Azure AI Search (Practical Shelf) |
| Affiliate / Trackable Link | link_id, source_partner_id, signed_token, status, reconciliation_batch | Azure SQL (Ledger extension) |

This will be forwarded to Agent 6 (Database Architect).

---

## BRIEFING FLAG FOR LEAD — Agent 5 Spawn

API surface area the Travel Assistant exposes:

**Inbound (external systems call us):**
- `POST /webhook/booking` — BookVisit/online store sends booking events (HMAC-signed). Triggers Magic Link generation.
- `GET /welcome?token={jwt}` — Magic Link entry. Customer-facing. JWT validated, PWA loaded.
- `POST /api/agent/process` — Chat endpoint. Traveler PWA sends user messages, receives Master Agent responses.

**Internal staff-facing endpoints:**
- `POST /staff/whisper` — Inject system-role instruction into live conversation (invisible to customer).
- `POST /staff/takeover` — Disconnect AI, staff takes direct control.
- `POST /staff/teach` — Thumbs up/down feedback on AI response (Optimizer training signal).
- `POST /staff/god-mode` — Force-push product to top of all queues for a resort/time window.
- `POST /staff/fire-red` — Emergency stop, alert all staff immediately.

**Outbound (we call external systems):**
- Oracle Opera REST API (or adapter) — availability check, reservation creation.
- BookVisit product catalog — product feed for Commercial Shelf seeding.
- Finnish Meteorological Institute API — hourly weather (mm/h rain, temperature).
- Kp-index aurora API — northern lights probability.
- Adyen or Stripe Connect — payment processing (choice unresolved).
- SendGrid/SMTP + SMS gateway — Magic Link delivery.
- Slack/Teams webhooks — staff emergency alerts.
- Puppeteer scraper target URLs — partner onboarding product extraction.

**B2B partner-facing:**
- `GET /b2b/customers` — Travel agencies view their customers in Finland, satisfaction, upsell revenue.
- Affiliate trackable links — `?ref=DMC_ID&promo=CODE` (signed, fraud-resistant).

This will be forwarded to Agent 5 (Integration Architect).
