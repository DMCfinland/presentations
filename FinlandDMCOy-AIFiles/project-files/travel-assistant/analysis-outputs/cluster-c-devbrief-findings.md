# Mining Output — Cluster C: Developer Briefs (Evolution)

Source files: Dev Brief v0.1, Dev Brief v0.7, Finland Personal Travel Assistant
Mined: 2026-02-21

---

## DECISIONS

1. [source: v0.1] The system architecture is Event-Driven Microservices on Microsoft Azure (Region: North Europe for GDPR compliance).

2. [source: v0.1] Azure OpenAI Service was chosen as the AI core, with Private Instances and Zero Data Retention configured.

3. [source: v0.1] Azure Event Grid was chosen as the event bus ("motorway") — all modules communicate via this message bus, not directly with each other.

4. [source: v0.1] Instead of building one large AI model, the team decided to build a team of specialized agents to prevent hallucinations: Master Agent (Concierge), Mood & Evaluator Agent (Psychologist), Suggestion Agent (Chef), Booking Specialist (Cashier).

5. [source: v0.1] The Master Agent is explicitly restricted: "Ei saa keksiä hintoja tai saatavuutta itse" — it must NOT invent prices or availability itself.

6. [source: v0.1] The traveler-facing interface will be a PWA (Progressive Web App) — no app store download required.

7. [source: v0.1] The Shadow Ledger was decided to be billing-ready, not just a log — a "Contract Table" database is built so that when a booking occurs, the commission is calculated immediately (e.g., Sale 200€ × 15% = 30€ receivable).

8. [source: v0.7] Architecture is locked as of v0.7: "Status: Architecture Locked."

9. [source: v0.7] A Brand Engine microservice was decided as a new component — the UI is a "blank shell" that colorizes at runtime from config (logos, CSS color variables, bot name, tone of voice).

10. [source: v0.7] The Suggestion Chef's scoring logic was decided to replace raw price with a "Value_Score" (price-quality ratio).

11. [source: Finland Personal Travel Assistant] The Suggestion Chef uses a defined scoring formula: Score = (Match×W1) + (Weather×W2) + (Value×W3) + (Margin×W4) + (Novelty×W5), where weights shift based on customer profile (budget traveler gets high W3; luxury traveler W3 = 0).

12. [source: Finland Personal Travel Assistant] The Master Agent uses a "Context Backpack" pattern: holds only the active conversation's data and drops it immediately when the topic changes.

---

## REQUIREMENTS

1. [source: v0.1] The system must create a "Magic Link" experience: after booking, the customer gets a link that opens a personal holiday assistant without registration.

2. [source: v0.1] The Ingestion & Onboarding Service must trigger from a webhook from the webshop or email confirmation, then create a user session and Magic Link.

3. [source: v0.1] The Traffic Control service must prioritize customers on the Staff Dashboard using a four-level status system: Green (AI handles), Yellow (Pending), Red (SLA breach — waiting >30min or negative sentiment), FIRE RED (emergency: hospital/police/fire — stops AI immediately and alerts staff).

4. [source: v0.1] The MVP scope (3–4 months) must include: onboarding → Magic Link → welcome message; basic RAG for Järvisydän FAQ; mood + suggestion logic based on weather and sentiment; hybrid booking (agent makes booking request via API or email); Staff Dashboard v1 with traffic lights and chat monitoring.

5. [source: v0.1] The Context Builder & RAG service must "inject" information to the Master Agent from a vector database containing Järvisydän info PDFs and menus, plus the customer profile.

6. [source: v0.1] The Optimizer & Watchdog must run nightly, anonymize data, and search for bugs and improvement targets, feeding results back into recommendation parameters.

7. [source: v0.1] Staff Command Center must provide three functions: Whisper (give advice to agent), Takeover (take over conversation), Teach (mark a solution as good training data).

8. [source: v0.7] The system must serve both direct customers (Järvisydän) and B2B partners' customers (e.g., KonTiki) — White Label is a first-class requirement, not an afterthought.

9. [source: v0.7] The A/B Testing Engine must operate on two levels: Level 1 (Themes: Romance vs. Adventure), Level 2 (Hooks: Pitch v1 vs. Pitch v2), with 10–20% of recommendations reserved as "wildcard" experiments for data collection.

10. [source: Finland Personal Travel Assistant] The system must reduce routine burden on reception staff and guides ("Monelta aamiainen?", "Mikä on WiFi?") by up to 80%.

11. [source: Finland Personal Travel Assistant] The system must be a proactive seller — it must identify moments when the customer is susceptible to buying (e.g., a rainy afternoon) and offer high-margin services at that moment.

12. [source: Finland Personal Travel Assistant] The Master Agent must check a "Safety Bulletin" board before giving advice on anything risky (e.g., ice conditions). If the information is old, it must hand off to a human.

---

## TECH CHOICES

1. [source: v0.1] **Microsoft Azure** — chosen platform, Region: North Europe (GDPR). Decided.

2. [source: v0.1] **Azure OpenAI Service** — AI core, Private Instances, Zero Data Retention. Decided.

3. [source: v0.1] **Azure Event Grid** — event bus for all inter-module communication. Decided.

4. [source: v0.1] **Vector database** — used for RAG: stores Järvisydän info PDFs, menus, customer profile. Specific vendor not named. Considered/planned.

5. [source: v0.1] **SQL database** — used by the Booking Specialist to check availability and log bookings, and for the Shadow Ledger "Contract Table." Decided.

6. [source: v0.1] **PWA (Progressive Web App)** — traveler-facing UI. No app store download. Decided for both v0.1 and confirmed in v0.7.

7. [source: v0.1] **Agentic AI coding tools: Cursor, Copilot, Gemini** — used by the 3-person dev team for boilerplate generation and coding acceleration. Decided (operational).

8. [source: v0.7] **CSS Variables** — mechanism for the Brand Engine's "Chameleon System" — brand identity applied as a layer on top of a neutral base. Decided.

9. [source: v0.7] **PWA** — reconfirmed in v0.7 for the Traveler App. Design is "Chameleon System": neutral base, brand applied as a layer on top. Decided.

10. [source: v0.7] **Airbnb Trips and Booking.com Assistant** — cited as benchmarks for modern travel app UI, but explicitly "yksinkertaistettuna" (simplified). Considered as reference/inspiration.

11. [source: Finland Personal Travel Assistant] **Puppeteer (Scraper Bot)** — chosen for the Brand Engine's "One-Click Onboarding" demo feature. Scrapes partner URL (e.g., www.kontiki.org) for logo, dominant CSS colors, and font, then generates a Brand_Config_Preview in 5 seconds. Decided.

12. [source: Finland Personal Travel Assistant] **Mermaid/graph diagram** — used to visualize the system architecture (Mermaid TD graph embedded in the document). Operational tool choice.

---

## RISKS

1. [source: v0.1] Hallucination risk: The system explicitly exists because building "one giant model" would cause hallucinations — the multi-agent architecture is the mitigation. The Master Agent is explicitly forbidden from inventing prices or availability.

2. [source: v0.1] FIRE RED escalation failure: If the system does not immediately stop AI and alert staff in emergencies (hospital, police, fire), the risk is unhandled emergencies. FIRE RED status is the stated mitigation.

3. [source: v0.1] SLA breach risk: Customer waiting >30 minutes without response triggers a Red status. This implies a risk of losing customers or damaging NPS if not monitored actively.

4. [source: v0.7] Interruption risk (proactive messaging): The "Internal Monologue" logic exists specifically because the Gap Finder cronjob could wake the agent at wrong moments — e.g., "Matti nukkuu -> Abort." Without this check, the system would disturb sleeping or busy customers.

5. [source: v0.7] Data quality risk for A/B testing: 10–20% wildcard recommendations are experiments — this means a fraction of customers at any moment receive untested pitches. The risk of lower conversion or negative experience during experiment phase is implicit.

6. [source: Finland Personal Travel Assistant] Safety advice risk: The Master Agent checks a "Safety Bulletin" board before giving advice on risky activities (e.g., ice conditions). If the bulletin is outdated, the system hands off to a human — the risk is that stale safety data could lead to dangerous advice if the handoff logic fails.

7. [source: Finland Personal Travel Assistant] Vendor lock-in risk (positive framing): The document explicitly describes B2B partner lock-in ("Vendor Lock-in positiivisessa mielessä") as a business benefit — but this is also a dependency risk if a partner decides to build their own solution.

---

## OPEN QUESTIONS

1. [source: v0.1] Specific vector database vendor not named — the document says "vector database" for RAG but does not specify which product (Pinecone, Weaviate, Azure Cognitive Search, etc.). Unresolved.

2. [source: v0.1] The Hybrid Booking mechanism is described as "API tai Email" — it is not specified which booking partners have an API and which require email fallback. Unresolved for MVP.

3. [source: v0.1] "3 hengen tiimi" (3-person team) — the team size is stated but their roles, seniority, and split of responsibilities are not defined in the brief.

4. [source: v0.7] The Suggestion Chef's weight parameters (W1–W5) are defined in formula but the actual starting values and how they are calibrated are not specified. Left as TBD.

5. [source: v0.7] The Mood Evaluator clusters customers into segments (Family_Active, Couple_Luxury, Solo_Budget) for statistical analysis — but the threshold definitions and how clusters map to product catalog are not specified.

6. [source: Finland Personal Travel Assistant] The "Instant B2B Demo" (Puppeteer scraping a partner website in 5 seconds) is described as a sales tool — but it is not stated whether this is MVP scope or a post-MVP feature.

7. [source: Finland Personal Travel Assistant] "Datan Omistajuus" (data ownership) is stated as a strategic benefit — but there is no discussion of what data is retained, for how long, GDPR consent flows for ongoing profiling, or how the User DNA profile is governed.

8. [source: Finland Personal Travel Assistant] The document references "Matkatoimisto X" (generic travel agency X) and KonTiki as B2B examples — but it is not defined how many B2B partners are targeted at launch, what onboarding looks like operationally, or pricing for the White Label tier.

---

## EVOLUTION (v0.1 → v0.7 → Finland Personal Travel Assistant)

### v0.1 (Draft / MVP Pilot — Järvisydän)
- Scope: A single-company pilot for Järvisydän. The system is conceptualized as a Finnish lakeside resort assistant.
- Architecture: 4 agents (Master, Mood, Suggestion, Booking), Azure Event Grid as event bus, Azure OpenAI with Zero Data Retention, PWA for traveler, Staff Dashboard with traffic lights.
- Business model: Implicit — commission tracking (Shadow Ledger), staff efficiency.
- Suggestion logic: Simple rule-based ("Koska sataa ja asiakas on väsynyt -> Suosittele Day Spa").
- RAG: Vector DB with Järvisydän PDFs and menus.
- No mention of multi-brand, no A/B testing, no scoring formula, no analytics pipeline.
- Status: Draft ("Luonnos").

### v0.7 (Architecture Locked — White Label Edition)
- Scope expanded: Now explicitly multi-brand ("White Label Edition") serving B2B partners (e.g., KonTiki) alongside Järvisydän.
- Key addition — Brand Engine: New microservice. UI is a "blank shell" that applies brand identity at runtime from config (logo, CSS variables, bot name, tone of voice). This is a fundamental architectural shift.
- Suggestion Chef renamed and upgraded: Now called "The Salesman," not just "The Chef." Logic shifts from simple rules to Hybrid Recommender (Stats + Context). A/B Testing Engine added (Themes + Hooks + Wildcard 10–20%). Value_Score replaces raw price.
- Mood Evaluator upgraded: Now an Async Listener (explicitly "no delay to chat"). Customers placed into statistical clusters (Family_Active, Couple_Luxury) for analytics.
- Analytics pipeline added: All interactions (Click, View, Book) logged to Analytics_Log for attribution and A/B test analysis. "Win-Win-Win" framing: High NPS + High Margin.
- Master Agent gains: "Internal Monologue" decision layer (decides whether to interrupt the customer), explicit Orchestrator role.
- UI design language added: "Chameleon System" with Airbnb Trips / Booking.com as benchmarks (simplified).
- Status: Architecture Locked — this is a significant commitment signal.

### Finland Personal Travel Assistant (Strategic + Full Detail Snapshot)
- This document is not a version — it is a dual-audience document: a sales/business case document AND a full technical snapshot ("kaikki tai ei mitään" — everything, nothing filtered, for later carving into MVP).
- Business framing fully developed: "Share of Wallet" maximization, B2B Killer App, 80% routine reduction, Data Ownership as strategic asset. These framings were absent or implicit in v0.1–v0.7.
- Brand Engine gains concrete demo workflow: Puppeteer scrapes partner URL → extracts logo/colors/font → generates Brand_Config_Preview in 5 seconds → sales demo on tablet. This is operationalized, not just conceptual.
- Scoring formula made explicit: Score = (Match×W1) + (Weather×W2) + (Value×W3) + (Margin×W4) + (Novelty×W5) with weight logic tied to customer profile.
- Mood Evaluator fully detailed: Signals catalogued (text sentiment, keywords, metadata: response speed, time of day, location). Output is a full Mood Matrix JSON with Segments (cluster), Dynamic Moods (0–100: Energy, Hunger, Social, Nature_Tolerance, Price_Sensitivity), and Tags (Loves_Sauna, Hates_Smoke, Needs_Accessibility).
- Master Agent gains Safety Guard: Checks Safety Bulletin before risky advice; hands off if data is stale.
- Context Backpack pattern named: Master Agent holds only active conversation data and drops it when topic changes (short-term memory scoping).
- Architecture diagram formalized: Mermaid flowchart with named layers (Front End Layer, The Brain/Microservices, Data Layer).
- Data stores named more specifically: "Backpack" (Short-Term/Context), "Product RAG" (Inventory/Warehouse), "User DNA" (History & Mood/Profile).

### What was removed or de-emphasized across versions
- The "Järvisydän-only" framing disappears by v0.7 — the product is now a platform.
- Simple if-then suggestion logic ("Koska sataa -> Suosittele Day Spa") replaced by the scoring formula and A/B engine.
- The Shadow Ledger/commission tracking (prominent in v0.1) does not appear prominently in v0.7 or the FPTA document — it may have been deferred or absorbed into the Booking & Ledger module.
- The Optimizer & Watchdog (nightly anonymized data review) is not mentioned in v0.7 or FPTA — unclear if dropped or deferred.

---

## NOTABLE QUOTES

1. [source: v0.1] "Emme rakenna yhtä jättiläistä, vaan tiimin erikoistuneita agentteja estääksemme hallusinaatiot." — ("We are not building one giant, but a team of specialized agents to prevent hallucinations.") This is the core architectural rationale stated plainly.

2. [source: Finland Personal Travel Assistant] "Muutamme passiivisen majoitusmyynnin aktiiviseksi, 24/7 rullaavaksi elämysbisnekseksi, joka voittaa sekä sydämet (NPS) että lompakot (Kate)." — ("We turn passive accommodation sales into an active, 24/7 rolling experience business that wins both hearts (NPS) and wallets (Margin).")

3. [source: v0.7] The v0.7 document is 58 lines total (1.8KB). It is deliberately compressed — "Architecture Locked" signals decisions made, not documentation of full scope. What it omits is as significant as what it contains.

4. [source: Finland Personal Travel Assistant] "Internal Monologue: 'Gap Finder herätti minut -> Onko nyt hyvä hetki puhua? -> Ei, Matti nukkuu -> Abort.'" — This illustrates the agent's self-interruption logic: the system reasons about whether to disturb the customer before acting.

5. [source: Finland Personal Travel Assistant] "Tämä laskee myynnin kynnystä valtavasti." — ("This lowers the sales threshold enormously.") Said of the Puppeteer-powered instant B2B demo — the 5-second brand preview is framed as a sales conversion mechanism, not just a technical feature.
