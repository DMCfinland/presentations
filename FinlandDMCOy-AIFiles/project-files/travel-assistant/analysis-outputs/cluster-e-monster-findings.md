# Mining Output — Cluster E: Monster Doc (Järvisydän MVP Architecture & Developer Brief)
Source: monster-compressed.md (compressed from 11,005 lines / 548KB original)
Mined: 2026-02-21

---

## DECISIONS

1. [section: Architecture] Microsoft Azure (Region: North Europe) was selected as the platform for GDPR compliance, Microsoft 365 integration (Teams, Outlook), Azure OpenAI Service with Private Endpoint (Zero Data Retention — data NOT used to train public AI models), and EU data residency.

2. [section: Architecture] Event-Driven Microservices pattern was decided. All modules communicate via Azure Event Grid as a central Event Bus. Rationale: if billing fails, chat still works; easy bug isolation; each microservice can be deployed/updated independently.

3. [section: Architecture] Decided against own LLM from scratch (cost and complexity), own payment terminals ("do not under any circumstances build own terminals — logistical nightmare, blocks global scaling"), and single monolithic app.

4. [section: AI Layer] Orchestrator pattern decided: one Master Agent (front end) delegates to specialist agents. Master Agent never fabricates prices or availability — it calls tools. Explicit anti-hallucination architecture.

5. [section: AI Layer] Context Backpack (short-term memory) is dropped immediately when the conversation topic (Intent) changes — prevents token bloat and stale context contamination.

6. [section: AI Layer] Four separate RAG shelves (Vector Indexes) decided: Commercial Shelf, Cultural Shelf, Practical Shelf, Internal Shelf. Agents access shelves directly (fast); the Librarian Agent only manages/curates — does not act as intermediary for live queries.

7. [section: Build Plan] MVP is scoped to Järvisydän only (single resort), Finnish + English languages, no in-app card processing, no cashback, no Holiday Builder, no voice calls, no self-service Partner Portal. Timeline: 3 months from start.

8. [section: Architecture] Multi-tenancy built from day one: adding a new resort = new row in tenant config DB, no code changes required. All tenant data isolated via `tenant_id` on every table.

9. [section: Architecture] Wiki/documentation: Notion-style living wiki decided (not PDF documents). Structure mirrors code modules. Wiki-Librarian Agent reads Git commits and auto-updates relevant wiki pages. Rule: "If you change the code, you change the Wiki."

10. [section: Constraints] Payment security delegated to device (Apple Pay / Google Pay / FaceID) — we never touch card numbers. Voice calls happen inside the app (WebRTC, not PSTN) to make caller ID spoofing impossible.

11. [section: Constraints] Agentic coding strategy decided: 3-person team with AI Junior Developers (Cursor/Copilot) handling 70–80% of boilerplate. Human Lead Developer is architect — approves structure, reviews security, handles Oracle Opera legacy integration. QA Agent simulates scenarios before production.

12. [section: Constraints] WhatsApp used as "doorbell" only: notification with Magic Link arrives via WhatsApp, customer clicks to open the Traveler PWA. Agent can receive simple WhatsApp replies; complex interactions redirect to PWA. Rationale: WhatsApp cannot show visual calendar, cannot process Apple Pay, cannot brand the UI.

---

## REQUIREMENTS

1. [section: Features] The system MUST operate 24/7 without human intervention for routine interactions.

2. [section: Features] The system MUST support multiple languages with real-time translation — Italian, German, Finnish, and English at minimum.

3. [section: Features] White-label branding required: same engine, different visual identity per tenant, controlled via `tenant_config.json`.

4. [section: Features] Magic Link access required — zero registration, zero passwords. Tokens must be cryptographically signed (JWT-style) so URL tampering breaks the link.

5. [section: Features] The system MUST proactively suggest activities based on weather, mood, and itinerary gaps.

6. [section: Features] All monetary transactions MUST be tracked in Shadow Ledger regardless of payment method (API, manual, or affiliate).

7. [section: Features] Human staff MUST be able to "whisper" instructions to the AI without the customer seeing. Whisper also functions as a loop-breaker — clears stuck AI state without a separate reboot button.

8. [section: Features] The system MUST escalate to human with full context when AI cannot resolve an issue after 3 failed attempts.

9. [section: AI Layer] Safety guardrail (hard-coded): ice safety and weather risks MUST query SafetyBulletin tool first. If SafetyBulletin data is older than 24 hours or missing, trigger Human Handover immediately.

10. [section: Constraints] Performance target: Chef (Suggestion) query MUST complete in under 800ms. Fallback: if no response in 800ms, Master Agent delivers a "generic emergency list" (restaurant, walk).

11. [section: Constraints] GDPR: PII (names, phone numbers) MUST be masked before data enters Data Lake or Optimizer — replaced with hashed tokens. Cluster_ID and Mood_Matrix are retained post-anonymization (required for Optimizer).

12. [section: Features] Service access gate: only valid reservation OR verified phone number unlocks access. The service is free but protected against abuse.

---

## TECH CHOICES

1. [section: Architecture] Azure Functions (Python/Node.js) — CHOSEN for compute. Each agent is an isolated function. Serverless — pay only per execution, not idle time.

2. [section: Architecture] Azure Event Grid — CHOSEN as Event Bus (system nervous system).

3. [section: Architecture] Azure OpenAI Service (GPT-4o) via Private Endpoint — CHOSEN as AI engine. Zero Data Retention policy.

4. [section: Architecture] Azure Cosmos DB (NoSQL) — CHOSEN for hot storage (chat history, session state).

5. [section: Architecture] Azure SQL Database — CHOSEN for relational data (Ledger, Users, Products, Contracts).

6. [section: Architecture] Azure AI Search (Vector Store) — CHOSEN for RAG/vector indexes.

7. [section: Architecture] Azure Data Lake Storage Gen2 — CHOSEN for cold storage (raw logs for analytics).

8. [section: Architecture] Next.js (React) PWA (Progressive Web App) — CHOSEN for frontend.

9. [section: Architecture] Azure Maps API — CHOSEN for geo-routing and corridor logic.

10. [section: Architecture] Adyen or Stripe (split payments, AliPay, Kaspi support) — CONSIDERED for payments. Adyen already used by Järvisydän. Final choice between Adyen and Stripe Connect not resolved in MVP scope. Own payment terminals REJECTED.

11. [section: Constraints] Redis or Pinecone — CONSIDERED for in-memory Vector DB to meet the 800ms Chef query performance target. Not finalized.

12. [section: Build Plan] OpenAI Realtime API — CONSIDERED for voice AI phone calls in Phase 3. Training data would come from recorded staff calls. Not in MVP.

---

## RISKS

1. [section: AI Layer] Hallucination risk: AI could fabricate prices or availability. Mitigated by hard-coded System Prompt rule: Master Agent CANNOT confirm prices or availability without querying a tool. No exceptions.

2. [section: AI Layer] Northern lights over-promising: the system must never promise aurora sightings — only use probability language ("forecast looks promising"). Hard-coded constraint.

3. [section: Integrations] Oracle Opera anti-corruption layer complexity: API complexity is unknown until Järvisydän IT team is engaged. An adapter layer (Anti-Corruption Layer) is planned between Booker Agent and Opera. Risk: integration edge cases fall outside AI-generated code competency.

4. [section: Constraints] Mystery Shopper data contamination: synthetic data from test personas must be labeled separately (Data_Source: Synthetic) and stored in separate storage to prevent contamination of real conversion stats.

5. [section: Constraints] Affiliate link commission fraud: affiliate links use signed tokens — `?source=kontiki` cannot be forged. Manual monthly reconciliation against partner affiliate reports required in MVP (automation deferred to Phase 2).

6. [section: AI Layer] Patience Meter failure mode: if patience_meter drops below 30, agent MUST switch to Silent Mode (no upsell). If this guardrail fails and the system upsells an already-frustrated guest, relationship damage follows. Cooldown period after negative experience is 4 hours.

7. [section: AI Layer] Gap Finder over-interruption: cronjob runs every 30 minutes. Multiple gate conditions required (gap + good weather + appropriate energy + right time, no contact 22:00–08:00) to prevent guest fatigue from excessive proactive messages.

8. [section: Constraints] Scoring formula weight cold start: exact W values for the Suggestion Chef scoring formula are not defined. Plan is to start with Tabula Rasa defaults and let Optimizer converge over first 90 days — meaning recommendations will be suboptimal during this period.

9. [section: Constraints] Type B booking authorization timeout risk: manual/email partner confirmation holds authorization for 24 hours only (not 7 days). If partner does not respond, auto-void is triggered and customer gets apology + new recommendation. Risk: partner responsiveness directly impacts guest experience.

10. [section: Build Plan] 3-person team timeline risk: team is realistic for MVP in 3–4 months only IF architecture is clean. Principle cited: "Build, don't plan endlessly. Code reveals truth faster than meetings."

---

## OPEN QUESTIONS

1. [section: Open Questions] Oracle Opera anti-corruption layer: API complexity to be mapped when Järvisydän IT team is engaged. An adapter layer is planned but scope is unknown.

2. [section: Open Questions] Payment flow for Phase 2: exact cashback mechanics, virtual card issuing partner (Stripe Issuing vs. Adyen Issuing), and whether DMC needs an e-money license for the virtual wallet — not resolved.

3. [section: Open Questions] Täti's (domain expert aunt's) Customer Timeline: Patrick's aunt was assigned to write the "perfect guest journey timeline" for Järvisydän. Content not yet received at time of conversation end. This timeline is the canonical source for the Trigger Engine and proactive messaging content.

4. [section: Open Questions] Trigger Engine exact timing logic: how precise can the Gap Finder be with the Shadow Schedule? At what point does the concierge decide "enough data to interrupt"? Left for iterative refinement via A/B testing.

5. [section: Open Questions] Scoring formula exact weights per customer cluster: initial W values not defined. Plan: start with Tabula Rasa defaults, let Optimizer converge over first 90 days.

6. [section: Open Questions] Mystery Shopper data weight decay function: exact formula for reducing synthetic data weight as real data accumulates — not defined. Plan: manual step-down at 100, 500, and 1,000 real user milestones.

7. [section: Open Questions] Cashback reconciliation at scale: how to auto-reconcile affiliate commissions without manual monthly report matching. Deferred to Phase 2.

8. [section: Open Questions] Influencer onboarding: no formal agreement structure defined. Commission model, content rights, branding control limits — not yet formalized.

9. [section: Open Questions] Supplier deposit / advance payment model: whether DMC should hold deposits to pre-pay partners — not resolved. Current assumption: invoice monthly on actuals.

---

## JÄRVISYDÄN vs FINLAND DMC DIFFERENCES

### Deployment Scope
- **Järvisydän MVP:** Single-resort config, post-booking assistant only, no Holiday Builder (pre-booking flow), Finnish + English only, booking via Järvisydän API or email automation, provisional Shadow Ledger with manual invoicing from report.
- **Finland DMC Platform:** Multi-tenant from day one, eventually includes Holiday Builder (pre-booking), white-label for travel agencies, influencer affiliate mode, licensing to other DMCs globally.

### Integration Differences
- **Järvisydän:** Has Oracle Opera hotel management system (~40 apps integrated) and BookVisit e-commerce. Järvisydän IT team participates in development. Finland DMC controls Järvisydän's online store → direct webhook access → no email parser needed for MVP.
- **Finland DMC (travel agency bookings):** Ingestion via booking confirmation email parser OR API detection. Magic Link sent inside `Varausvahvistus` (booking confirmation) email.

### Magic Link Entry Points
- **Järvisydän:** Triggered immediately on purchase in online store (Webhook). Agent created within 5–10 seconds. Customer sees "Preparing your personal assistant…" animation, then Magic Link appears on thank-you page. Also sent via email/SMS.
- **Travel agency booking:** Magic Link included in booking confirmation email. Parser reads email OR Ingestion Service detects booking via API.
- **Individual traveler (Phase 2):** Landing on finlanddmc.fi → Holiday Builder flow.

### Brand Persona
| Tenant | Name | Style | Colors |
|---|---|---|---|
| Järvisydän (direct) | Järvisydän Host | Warm, savolainen, storytelling | Brown/Gold |
| KonTiki (B2B) | KonTiki Guide | Professional, precise, expert | Dark Blue/Orange |
| Influencer (affiliate) | [Influencer name] | Influencer's curated picks style | Scraped from their IG/site |
| Finland DMC (default) | Finland DMC Assistant | Balanced, helpful, Suomi expert | DMC brand colors |

### Data & Operations
- **Järvisydän:** Safety Bulletin maintained by Järvisydän guides (ice thickness, route closures) — updated daily via Staff Dashboard. BookVisit product catalog is starting source for Commercial Shelf.
- **Finland DMC:** Manages Optimizer, data analytics, contract database, and partner reporting. Operates the Staff Dashboard / Command Center.

### Code Relationship
Both Järvisydän and Finland DMC use identical code and infrastructure. The distinction is purely in tenant configuration and data scope — not in separate codebases.

---

## NOTABLE QUOTES

1. "The invisible guide in your pocket." — Core product promise. Proactive, context-aware, and transactional. Operates 24/7 from booking confirmation to homecoming.

2. "Master Agent never fabricates prices or availability — it calls tools. This is the explicit anti-hallucination architecture."

3. "Do not under any circumstances build own terminals. Logistical nightmare (maintenance, faults, distribution, certifications), blocks global scaling."

4. "When patience_meter < 30: agent switches to 'Silent Mode' — no upsell attempts." — The system is designed to stop selling before the guest has to ask it to.

5. "The Optimizer does NOT change code — it changes knowledge." — All learning is RAG and data updates, not code deployments. A/B winners are promoted by overwriting Champion hooks, not redeploying.

6. "Adding a new resort = new row in tenant config DB. No code change required." — Multi-tenancy principle that makes the platform licensing model viable.

7. "AI handles 80–90% of routine interactions, freeing staff for high-value service. Active upsell engine captures guest spending at the point of maximum intent (on-location)." — The twin business justifications for the entire system.

8. "Build, don't plan endlessly. Code reveals truth faster than meetings." — Development philosophy driving the 3-month MVP timeline with a 3-person team.
