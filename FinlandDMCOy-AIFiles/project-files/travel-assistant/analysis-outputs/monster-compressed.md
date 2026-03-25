# Finland DMC Personal Travel Assistant — Compressed Architecture & Developer Brief

**Source:** 11.12.YourPersonalTravelAssistant-JärvisydänAssitantMVP-Architerchture&DeveloperBrief.txt
**Original size:** 11,005 lines / ~548KB
**Compressed on:** 2026-02-21
**Compression purpose:** Open mining pass — preserves all decisions, tech choices, requirements

---

## 1. PRODUCT VISION

### What It Is
The Finland DMC Personal Travel Assistant (FPTA) is a hyper-personalized, proactive AI-powered travel concierge. It is not a passive chatbot — it is an autonomous recommendation engine and transaction layer that serves as a guest's "personal Suomi-expert concierge" throughout their entire journey.

### Core Promise
"The invisible guide in your pocket." Proactive, context-aware, and transactional. Operates 24/7 from booking confirmation to homecoming.

### Problem Statement
Traditional DMC operations are reactive and human-labor-dependent. Guest contact drops after booking, losing high-value upsell opportunities. The system addresses: fragmented travel information across dozens of sources, no post-booking engagement, high staff load for routine questions, and inability to serve individual tourists at scale.

### Why Build This
- AI handles 80–90% of routine interactions, freeing staff for high-value service
- Active upsell engine captures guest spending at the point of maximum intent (on-location)
- Creates scalable B2B product (White Label) that locks in travel agency partners
- Continuous learning system gets smarter with every guest interaction
- Järvisydän is the perfect pilot: closed ecosystem with accommodation, activities, and restaurants on a single property

### Two Deployments Discussed
The document covers a **Finland DMC** master platform and **Järvisydän** as the MVP pilot. Järvisydän has its own IT team and existing Oracle Opera + BookVisit integration. Finland DMC manages Järvisydän's IT and marketing. The system is designed multi-tenant from day one.

---

## 2. ARCHITECTURE

### Platform Decision: Microsoft Azure
The system is built on Microsoft Azure (Region: North Europe) for GDPR compliance. Key reason: Microsoft 365 integration (Teams, Outlook), Azure OpenAI Service provides GPT-4o with Private Endpoint (Zero Data Retention — data is NOT used to train public AI models), and EU data residency.

**Decided against:** Own payment terminals (logistical nightmare, blocks global scaling). Own LLM from scratch (cost and complexity). Single monolithic app.

### Architectural Pattern: Event-Driven Microservices
All modules communicate via a central Event Bus (Azure Event Grid). The "Motorway" metaphor: when an event fires (e.g., OrderPlaced), the bus broadcasts it and relevant microservices wake up independently. This ensures:
- If billing fails, chat still works
- Easy bug isolation and troubleshooting
- Each microservice can be deployed/updated independently (weekly deployment cadence)

### Core Stack
```
Compute:        Azure Functions (Python/Node.js) — each agent is an isolated function
Event Bus:      Azure Event Grid — system nervous system
AI Engine:      Azure OpenAI Service (GPT-4o) via Private Endpoint
Hot Storage:    Azure Cosmos DB (NoSQL) — chat history, session state
Relational:     Azure SQL Database — Ledger, Users, Products, Contracts
Vector/RAG:     Azure AI Search (Vector Store) — knowledge base
Cold Storage:   Azure Data Lake Storage Gen2 — raw logs for analytics
Frontend:       Next.js (React) PWA (Progressive Web App)
Maps:           Azure Maps API (Geo-Routing / Corridor Logic)
Translation:    Azure Translator (real-time multi-language support)
Payments:       Adyen or Stripe (split payments, AliPay, Kaspi support)
```

### Why Azure over Google
- Microsoft 365 integration (company already Microsoft-integrated)
- Azure OpenAI private instances for data security
- Enterprise GDPR compliance

### Coding Strategy: Agentic AI Development
3-person team uses AI-assisted coding (Cursor, GitHub Copilot, Gemini) for boilerplate. AI generates 70–80% of code (schemas, API connections, test suites). Human Lead Developer handles architecture decisions, security review, Oracle Opera integration edge cases, and merge approvals. A QA Agent simulates attack scenarios and user personas before production deployment.

### Data Flow: High-Level
```
Online Store (Järvisydän)
  → Webhook trigger → Ingestion Service
  → Context Builder → Master Agent Session
  → Customer gets Magic Link
  → Customer uses Traveler PWA
  → Master Agent orchestrates: Mood Evaluator (async) + Suggestion Chef (on-demand) + Booker (on transaction)
  → All events → Shadow Ledger + Data Lake
  → Nightly: Optimizer reads Data Lake → updates RAG + Product stats
```

---

## 3. FEATURES & REQUIREMENTS

### Onboarding Flows (Three Scenarios)
1. **1.1 — Existing booking via travel agency:** Customer enters booking code → system validates → shows personalized welcome with booked components → asks for profile data (sizes, allergies, preferences)
2. **1.2 — Unknown travel agency code:** "Code not recognized / your agency hasn't activated FPTA → check code, contact your agency, or continue without package" → welcome to Finland, can plan new trip
3. **1.3 — Individual traveler:** Welcome to Finland, I am your personal travel assistant, we can plan your holiday together, or you can ask individual questions, I can teach you Finnish, tell you what to pack

### System Must Do (Requirements)
- Operate 24/7 without human intervention for routine interactions
- Support multiple languages with real-time translation (Italian, German, Finnish, English at minimum)
- White-label branding — same engine, different visual identity per tenant
- Magic Link access — zero registration, zero passwords
- Proactively suggest activities based on weather, mood, and itinerary gaps
- Track all monetary transactions in Shadow Ledger regardless of payment method
- Handle booking via three paths: API, email/manual, affiliate link
- Allow human staff to "whisper" instructions to the AI without the customer seeing
- Escalate to human with full context when AI cannot resolve
- Collect feedback dynamically linked to current Optimizer data needs
- Support multi-resort scaling via tenant configuration (no code changes needed for new resort)

### User-Facing Features (Customer)
- Magic Link entry (one click, no password)
- Personalized welcome with pre-built activity knowledge
- Chat with AI concierge (proactive and reactive)
- Visual itinerary timeline (confirmed / pending / suggestions)
- Home Feed with contextual hero card (weather, next activity, gap suggestion)
- Explore Hub (Netflix-style visual product catalog)
- Feedback slider (emoji-based, dynamic questions linked to Optimizer needs)
- Emergency mode (112, DMC duty, share location)
- Profile & settings (allergies, interests, language preference, agent style)
- Map with resort layout and meeting point navigation
- Push notifications / WhatsApp for time-sensitive information

### User-Facing Features (Staff Dashboard)
- 3-pane layout: Queue (priority list) / Live Context (chat + situation card) / Action Deck
- Traffic light priority queue with urgency scoring formula
- Whisper mode (staff advises AI without customer seeing)
- Takeover mode (staff takes over chat directly)
- Collision detection (prevents two staff handling same customer simultaneously)
- Dead Man's Switch (auto-return to AI if staff inactive for 10 minutes)
- Teach buttons (thumbs up/down on AI responses for training data)
- SOS / Fire Red emergency override with instant alerts
- Positivity corner (surfaces positive customer feedback to staff)
- Language translation (customer messages shown in Finnish/English regardless of source language)
- Situation card (AI-generated 2-sentence current status summary)

### Partner & B2B Features
- B2B Partner Dashboard (travel agencies see their customers in Finland, satisfaction rate, upsell revenue)
- Supplier Onboarding portal (AI scraper + human review workflow)
- Partner Portal Light (suppliers update their own availability/closure)
- Influencer / Affiliate mode (personal link, curated Top Picks, commission reporting)
- Creator Report (automated monthly stats to influencers: customers, top picks, revenue)

---

## 4. AI / INTELLIGENCE LAYER

### Orchestrator Pattern (Decided)
One Master Agent (front end) delegates to specialist agents. The Master Agent never fabricates prices or availability — it calls tools. This is the explicit anti-hallucination architecture.

### Master Agent (The Concierge)
**Role:** Front-end interface, Tone of Voice, Orchestrator.

**System Prompt architecture (layered, built dynamically):**
1. Base Layer: Safety rules, core task, hard limits (same for all tenants)
2. Brand Layer: Tone of Voice per tenant (Järvisydän = warm Savolainen host; KonTiki = professional expert guide)
3. Context Layer: User name, location, current intent, weather, next item on itinerary
4. Task Layer: Current user request

**Context Backpack (short-term memory):**
```json
{
  "user_name": "Matti",
  "location": "Järvisydän, Room 101",
  "current_intent": "Planning_Dinner",
  "weather_now": "Rainy (3mm/h)",
  "active_suggestion": "Menu_Tulirestaurant"
}
```
The backpack is dropped immediately when the conversation topic (Intent) changes. When user asks about moottorikelkka, the dinner menu is discarded.

**Gap Finder Logic:**
- Cronjob every 30 minutes wakes the Master Agent
- Agent does NOT immediately contact the customer
- Internal Monologue: checks itinerary for gaps, checks Mood (Energy level), checks time of day (no contact 22:00–08:00)
- Decision gate: only reaches out if gap + good weather + appropriate energy + right time
- If no strong reason to interrupt: wait until next cronjob cycle

**Safety Guardrail (hard-coded):**
- Ice safety, weather risks: MUST query SafetyBulletin tool first
- If SafetyBulletin data is older than 24 hours or missing: trigger Human Handover
- Northern lights: never promise, only use probability language ("forecast looks promising")

**Human Handover / Whisper mechanism:**
Staff types in Whisper field → System injects a System-role message into conversation history (invisible to customer) → Master Agent reads it as highest-priority instruction → Reformulates and delivers to customer. This also breaks AI loops (whisper clears stuck state without a separate "reboot" button).

**Tool Routing Protocol:**
- Recommendation needed → call Suggestion_Chef_Tool
- Booking needed → call Booker_Tool
- Safety question → call SafetyBulletin_Tool
- Price/availability query → call Database_Lookup_Tool
- Context exhausted / AI confused 3 times → call Human_Handover_Tool

### Mood Evaluator Agent (The Psychologist)
**Role:** Async Event Listener — "fly on the wall." Runs simultaneously with every user message, no latency added to chat.

**Output — Mood Matrix JSON (updated after every message):**
```json
{
  "user_id": "u12345",
  "cluster_id": "CL_05_German_Family",
  "last_update": "2025-12-10T14:05:00Z",
  "dimensions": {
    "energy": 40,
    "hunger": 85,
    "social_battery": 60,
    "luxury_affinity": 30,
    "nature_rawness": 80,
    "safety_need": 90,
    "foodie_focus": 20,
    "price_sensitivity": 65
  },
  "tags": [
    {"tag": "hate_smoke", "weight": 1.0, "source": "chat_history"},
    {"tag": "love_history", "weight": 0.8, "source": "explicit_feedback"},
    {"tag": "needs_childcare", "confidence": 0.9}
  ],
  "patience_meter": 100
}
```

**Dimension definitions (0–100):**
- Energy: 0 = zombie, 100 = Duracell
- Hunger: calculated from time since last meal
- Social_Battery: 0 = hermit, 100 = party
- Luxury_Affinity: 0 = budget, 100 = premium
- Nature_Rawness: 0 = comfort ("sokerista"), 100 = wilderness ("Sissi")
- Safety_Need: 0 = extreme sport, 100 = very safety-conscious
- Foodie_Focus: 0 = fuel only, 100 = gourmet is the point of travel
- Price_Sensitivity: adjusted by Value_Score (price/quality ratio), not raw price

**Clustering (for statistical optimization):**
Evaluator maps each unique customer to a named cluster (e.g., German_Active_Family, Solo_Budget, Couple_Luxury). This enables A/B testing and statistical analysis: "When Cluster X is in Mood Y, what converts best?" Cold start (first interaction): uses nationality + party size as starting signal. Cluster assignment can change as data accumulates.

**Dynamic Tag Scoring (Mood Ring 2.0):**
Tags are not on/off switches but weighted. Tags decay/grow with evidence. Example: customer asks about champagne → Luxury_Affinity +20. Customer then asks for cheap pizza → Budget_Score +30, Luxury_Affinity -10. Nightly Optimizer re-evaluates: "hybrid traveler — occasional luxury, mostly casual."

**Patience Meter:**
When patience_meter < 30: agent switches to "Silent Mode" — no upsell attempts. When customer expresses frustration: log silently, activate cooldown period (4 hours). After cooldown: approach with empathy and service, not questionnaires.

**Negative Feedback Handling (Silent Logging + Delayed Empathy):**
Do not immediately ask for feedback after negative experience. Log: `Event: Negative_Experience, Confidence: High, Topic: Price/Room`. Wait until next natural interaction or next morning. Approach: "I wanted to make sure yesterday's issue was resolved. Is the room temperature better now?"

### Suggestion Chef Agent (The Salesman)
**Role:** Mathematical optimization engine. Receives: user_id + time_window + current_location. Returns: top 2 recommendations with sales pitch.

**The Funnel (3 stages):**

**Stage 1 — Hard Filters (SQL):**
- Is product open right now?
- Available slots > 0?
- Within mobility range (car: yes/no, distance threshold)?
- Not already booked by this user today?

**Stage 2 — Smart Score (Math):**
```
Final_Score = (Base_Match * W1) + (Weather_Fit * W2) + (Value_Score * W3) + (Margin_Boost * W4) + (Novelty_Score * W5)
```
- **Base_Match:** 100 minus N-dimensional Euclidean distance between user's Mood Matrix vector and product's dimension vector (Energy, Social, Luxury, Nature_Rawness, Safety_Need — 5D to 7D space)
- **Weather_Fit:** Weather Service provides mm/h rain. Coefficient applied: Storm (>10mm/h) → outdoor products score 0; Light drizzle (1mm/h) → small penalty unless user is "Sissi" (Nature_Rawness > 80); Clear → outdoor products boost +20%. Weather also considers tomorrow's forecast for "today is better for outdoor" logic.
- **Value_Score:** NPS rating from past customers divided by price. Replaces raw price sensitivity. A budget traveler CAN buy a 200€ experience if Value_Score is "mind-blowing."
- **Margin_Boost:** If commission > 30%, add up to +10 points (Business Logic layer)
- **Novelty_Score:** Products with high Repeatability (sauna, restaurants) don't penalize repeats. Husky Safari: after first booking, Novelty drops to near-0 (don't suggest again). Products marked Repeatability: Low get heavy penalty on repeat.
- **W (Weights):** Personalized per customer cluster. Budget traveler: W3 (Value) = 0.5, W4 (Margin) = 0.05. Luxury traveler: W3 = 0.0, W4 = 0.15.

**Stage 3 — A/B Testing / Hook Selection (Champion/Challenger):**
Each product has multiple Sales Hooks stored in DB. Chef selects theme (Romance / Adventure / Family / Sustainability / etc.) based on customer cluster, then selects hook version:
- 80% → Champion Hook (best-performing version for this cluster)
- 20% → Challenger Hook (alternative being tested)
When Challenger accumulates 50 impressions with statistically better conversion: it becomes the new Champion.

**Wildcard / Exploration (Epsilon-Greedy, 10–20%):**
To collect data on new/untested products: randomly insert a "dark horse" (rank 5–10 product) into recommendations. If customer engages → product's statistical baseline score rises.

**Lookahead (Book Early Warning):**
When generating today's recommendations, Chef simultaneously checks tomorrow's top products for this customer type. If High-Demand product has <20% slots remaining for tomorrow: Master Agent adds "side note" to recommend booking it now.

**Geo-Routing (The Corridor):**
When customer is traveling between resorts (e.g., Sahanlahti → Järvisydän):
- Calculate route (Azure Maps API)
- Draw virtual corridor (radius: 1km if hurried, up to 50km if full free day)
- Query RAG Nature Shelf and Commercial Shelf for POIs within corridor
- Apply Mood filter (Hungry → roadside café; Nature_Lover → viewpoint; History → castle)
- Master Agent proactively suggests: "I noticed you're heading to Järvisydän today. There's a beautiful viewpoint 5 minutes off the route..."

**Manual Override (God Mode):**
Staff Dashboard has a "push" function that forces a product to top of all recommendation queues for a given resort/time window. Example use: "We have 50kg of salmon expiring tonight — push Salmon Soup to everyone." This is a critical business function.

### RAG Architecture (Universal Knowledge Library)

**Four shelves (separate Vector Indexes):**
1. **Commercial Shelf:** Product cards — name, price, availability, commission %, hooks, 5D coordinates, tags. Used by: Chef, Booker.
2. **Cultural Shelf:** Local history, stories, legends, "Did you know" content. Used by: Master Agent (storytelling filler, relationship building).
3. **Practical Shelf:** WiFi passwords, parking instructions, check-in/out rules, Safety Bulletin (ice thickness, route closures). Used by: Master Agent.
4. **Internal Shelf:** Brand guidelines per tenant (KonTiki vs. Järvisydän voice), Optimizer insights and best practices, influencer curated picks. Used by: System processes, brand engine.

**Agents access shelves directly** (fast) — the Librarian Agent only manages/curates shelves, does not act as intermediary for queries.

**Librarian Agent (maintenance, runs weekly):**
- Conflict Detection: "Website says price 50€, our DB says 45€ → create conflict ticket for Staff Dashboard"
- Freshness Check: "Christmas Menu 2024 is stale → archive automatically"
- RAG Generator: When new product enters DB, generates Context Card (natural language description of product including FAQs, restrictions, price) for Master Agent's Backpack use

**Context Card example:**
"Arctic Floating is a relaxing experience where guests float in icy water wearing a dry suit. Suitable for anyone 140cm+. Safe and warm. Price: 85€. Pickup at reception at 14:00."

### Optimizer Agent (Continuous Learning Engine)
**Not a chatbot — an analytical batch process** running nightly via Azure Functions.

**Structure:**
1. **Miner:** Reads Data Lake raw logs. Finds correlations: "When weather was bad and guest was a German family → Husky Safari conversion dropped 80%."
2. **Hypothesis Generator:** Creates improvement proposals. "Test a hook emphasizing animal welfare for German families."
3. **Editor:** Updates RAG (Internal Shelf and Commercial Shelf stats). Writes new rules for Chef: `IF Cluster=German_Active_Family AND Weather=Bad THEN Boost_Ethical_Angle`. Does NOT change code — changes knowledge.

**Nightly routines:**
- Update Best Seller rankings per cluster
- Update product Conversion_Rate and Value_Score
- Determine A/B winner (if Challenger has 50 impressions with better conversion → promote to Champion)
- Re-score tag affinities

**Strategic Missions (on-demand):**
- "Find out why product X doesn't sell to German families" → Optimizer digs into Data Lake chat logs
- Simulate campaign with Mystery Shoppers before going live

**Anonymization Pipeline (for Optimizer input):**
Before data enters Data Lake or Optimizer: names and phone numbers replaced with hashed IDs. Cluster_ID and Mood_Matrix retained (needed for analysis). Ensures GDPR compliance in learning loop.

### Mood and Data Feedback Loops

**Customer feedback collection — Dynamic (Strategic Data Gathering Mission):**
Optimizer sets current data need (e.g., "We need Value_Score data for product X"). UI surfaces contextually appropriate question at right moment (only when customer Mood is positive). Formats:
- Emoji slider (😠…😐…🤩) for general vibe
- Binary (Hinta-laatu suhde: Kyllä/Ei)
- Likert scale linked to current A/B hook test

**Immediate reward on positive feedback:**
Confetti animation + "Great! We'll find you more like this." → Customer understands their feedback shapes their own experience.

**Mystery Shopper Agents:**
- Deployed by Watchdog or Analyzer before new feature release
- Multiple personas: "Karen" (complains about everything), "Lost Backpacker" (vague questions), "Big Spender" (tests upsell)
- Synthetic data labeled separately (Data_Source: Synthetic, Weight: 1.0 initially, drops to 0.0 after >1000 real users)
- Can be used to pre-test campaign hooks before exposing to real customers
- Separate storage to prevent contamination of real conversion stats

---

## 5. BUILD PLAN

### Timeline (agreed)
- **Week 1–2 (Warmup):** Azure environment setup, database schemas, "Hello World" agent, integration testing
- **Months 2–3 (Sprint):** Core logic coding, UI build, Järvisydän data ingestion
- **Result:** MVP live after 3 months from start

### MVP Scope — Järvisydän Pilot (Phase 1)
**IN:**
- Single resort: Järvisydän only
- Languages: Finnish + English (translation layer active for other languages)
- Booking: Järvisydän API if available; email automation for others
- Provisio: Shadow Ledger tracking, manual invoicing from report
- AI: Weather + Mood-based recommendation logic
- Staff Dashboard v1: Traffic lights, chat monitoring, whisper
- No cashback implemented yet (system designed to add it later)
- No Holiday Builder / Travel Builder yet (pre-booking flow)
- No voice calls
- No self-service Partner Portal (DMC sends reports manually)
- Payment: handled on-site or via partner; no in-app card processing in MVP

**OUT (Phase 2+):**
- Travel Builder (pre-booking trip planning flow)
- Integrated payments / virtual card / automatic cashback
- Partner self-service portal
- Voice mode (AI phone calls)
- Full multi-resort expansion beyond Järvisydän
- Automated invoice generation at scale
- Direct AliPay/Kaspi integration (though Adyen/Stripe supports these)

### Phase 2 — Expansion
- Holiday Builder: pre-booking trip planning wizard (B2B and B2C versions)
- Additional resorts: adding new tenant = new `tenant_config.json` entry + new RAG data. Zero code changes.
- Scaling Järvisydän → Saimaa regional: same architecture, new brand config, new product data

### Phase 3 — Platform
- Licensing to other DMCs in Finland and internationally (revenue model shift)
- Voice AI phone calls (OpenAI Realtime API + training data from recorded staff calls)
- Full fintech layer (virtual DMC card, real-time split payments, automatic cashback tiling)

### Modular Deep Dive Documents Planned (DD0–DD7)
The conversation produced a series of detailed specification documents:
- **DD0:** Strategic Vision & Value Proposition (for stakeholders/investors)
- **DD1:** Intelligence Architecture (Master Agent, Mood, Chef — for AI architects)
- **DD2:** Data Architecture & RAG Strategy (for database architects)
- **DD3:** Booking & Finance Architecture (for backend devs and CFO)
- **DD4:** UI/UX Specifications & Brand Engine (for frontend devs)
- **DD5:** Operational Manual & Staff Dashboard (for ops team)
- **DD6:** IT Infrastructure & DevOps (for DevOps engineers)
- **DD7:** Prompt Library & Persona Bible (for prompt engineers)

---

## 6. INTEGRATIONS

### Existing at Järvisydän
- Oracle Opera hotel management system (~40 apps integrated)
- BookVisit e-commerce platform
- Järvisydän IT team available to participate
- Finland DMC controls Järvisydän's online store → direct webhook access, no email parser needed

### Booking Integrations (Three Paths)

**Type A — Full API (Oracle/BookVisit):**
`GET /availability` → Authorization (card hold) → `POST /book` → Capture payment → Log to Ledger

**Type B — Manual/Email (partners without API):**
Send email/SMS to partner with CONFIRM/DENY link → Authorization hold (valid 24h, not 7 days) → Partner confirms → Capture → Partner rejects or timeout → Auto-Void Authorization (funds released immediately) → Customer gets apology + new recommendation from Chef

**Type C — Affiliate Link:**
Generate trackable URL (`https://partner.com/book?ref=DMC_ID&promo=CODE`) → Log to Ledger as `Status: REFERRED_PENDING` → Agent asks user 2h later "Did you complete the booking?" → If yes: `USER_REPORTED_SUCCESS` → Reconcile against partner affiliate report monthly

### External APIs Required
- **Weather:** Finnish Meteorological Institute API (Ilmatieteen laitos) — updated hourly, granular mm/h
- **Northern Lights:** Kp-index data for aurora forecast
- **Maps:** Azure Maps API for geo-routing / corridor logic
- **Email:** SMTP/SendGrid for partner request emails and SMS gateway
- **Payments:** Adyen (already used by Järvisydän) or Stripe Connect for split payments
- **Messaging:** Slack/Teams webhooks for Staff Dashboard alerts
- **Voice (future):** OpenAI Realtime API

### Web Scraper for Partner Onboarding
DMC staff enters URL → Puppeteer scraper reads site → extracts logo, primary color, font, product info → AI Content Agent generates tags, hooks, 5D coordinates → Staff reviews and approves → Product goes live in SQL + RAG

**Brand Importer for B2B Demo:**
Same scraper used to instantly demo the White Label concept in sales meetings. Enter partner URL → 5 seconds → live demo with their branding.

### WhatsApp Integration (Hybrid Channel)
WhatsApp used as "doorbell": notification arrives in WhatsApp with Magic Link. Customer clicks → opens Traveler PWA. Agent can receive simple WhatsApp replies. For anything complex, app redirects to PWA. Rationale: WhatsApp cannot show visual calendar, cannot process Apple Pay, cannot brand the UI.

---

## 7. CONSTRAINTS & DECISIONS

### GDPR / Data Privacy
- Data stays in Azure EU tenant — does not leave Microsoft's EU infrastructure
- Zero Data Retention policy with Microsoft: our data NOT used to train public AI models
- PII Masking before data enters Data Lake (names, phones → hashed tokens)
- Cluster_ID retained post-anonymization (required for Optimizer)
- Row-Level Security (RLS) at database level: every query forced to include `WHERE user_id = CURRENT_USER`
- Tenant isolation: Matti's agent cannot access Pekka's data even if confused
- Customer data stays in Azure SQL (owned by us) — we decide retention rules
- For GDPR Article 28 compliance: DPA agreement with Microsoft recommended

### Security / Anti-Abuse
- Service is free but protected against abuse: only valid reservation OR verified phone number unlocks access
- Magic Link tokens are cryptographically signed (JWT-style) — URL tampering breaks link
- Affiliate links use signed tokens — `?source=kontiki` cannot be forged to divert commissions
- Payment security delegated to device (Apple Pay / Google Pay / FaceID) — we never touch card numbers
- Voice calls happen inside the app (WebRTC) not PSTN — caller ID spoofing impossible
- AI cannot confirm prices or availability without querying a tool — hard-coded in System Prompt

### No Own Payment Terminals (Decided Against)
Physical payment terminals: "Do not under any circumstances build own terminals. Logistical nightmare (maintenance, faults, distribution, certifications), blocks global scaling."

### Payment Split Logic (Future Fintech)
- Customer pays with DMC Travel Card (Visa/Mastercard virtual prepaid card)
- Partner gets 100% of transaction value (normal card payment at their terminal)
- DMC receives transaction data in real-time
- Commission calculated in cloud: system invoices partner monthly for agreed %
- Cashback credited to customer wallet balance
- This is Phase 2/3 — not in MVP

### Performance Targets
- Chef query must complete in under 800ms
- Requires in-memory Vector DB (Redis or Pinecone) for RAG indexes
- Chef fallback: if no response in 800ms, Master Agent delivers "generic emergency list" (restaurant, walk)

### Cost Management
- Serverless (Azure Functions) — pay only per execution, not idle time
- Short-term memory (Backpack) dropped when topic changes — prevents token bloat
- Cronjob for Gap Finder (cheap, simple code) + AI decision gate (expensive, only when needed)
- Mood JSON stored in DB, not re-derived from conversation history each time (100x cheaper)

### Agentic Coding Strategy (Team Model)
- 3-person team is realistic for MVP in 3–4 months IF architecture is clean
- AI Junior Developers (Cursor/Copilot) handle 70–80% of boilerplate
- Human Lead Developer is architect: approves structure, reviews security, handles Oracle Opera legacy integration
- QA Agent simulates scenarios before production
- Principle: "Build, don't plan endlessly. Code reveals truth faster than meetings."

### Wiki / Documentation
- Decided: Notion-style living wiki (not PDF documents)
- Structure mirrors code modules
- Decision Log: every architectural decision recorded with date and reason
- Wiki-Librarian Agent: reads Git commits → auto-updates relevant wiki pages
- Rule: "If you change the code, you change the Wiki."

### Multi-Tenancy from Day 1 (Decided)
The system is built multi-tenant from the start. Adding a new resort = new row in tenant config DB. No code change required. All tenant data is isolated at DB level via `tenant_id` on every table.

---

## 8. OPEN QUESTIONS

The following were explicitly left unresolved or deferred:

1. **Oracle Opera anti-corruption layer:** API complexity to be mapped when Järvisydän IT team is engaged. An adapter layer (Anti-Corruption Layer) is planned between Booker Agent and Opera.

2. **Payment flow for Phase 2:** Exact cashback mechanics, virtual card issuing partner (Stripe Issuing vs. Adyen Issuing), and whether DMC needs an e-money license for the virtual wallet — not resolved.

3. **Täti's (domain expert aunt's) Customer Timeline:** Patrick's aunt was assigned to write the "perfect guest journey timeline" for Järvisydän (single resort). Content not yet received at time of conversation end. This timeline was to serve as the canonical source for Trigger Engine and proactive messaging content.

4. **Trigger Engine exact timing logic:** How precise can the Gap Finder be with the Shadow Schedule? At what point does concierge decide "enough data to interrupt"? Left for iterative refinement via A/B testing.

5. **Scoring formula exact weights per cluster:** Initial W values not defined. Plan: start with Tabula Rasa defaults, let Optimizer converge over first 90 days.

6. **Mystery Shopper data weight decay function:** Exact formula for reducing synthetic data weight as real data accumulates — not defined. Plan: manual step-down at 100, 500, 1000 real user milestones.

7. **Cashback reconciliation at scale:** How to auto-reconcile affiliate commissions without manual monthly report matching. Deferred to Phase 2.

8. **Influencer onboarding process:** No formal agreement structure defined. Commission model, content rights, branding control limits — not yet formalized.

9. **Supplier deposit / advance payment model:** Whether DMC should hold deposits to pre-pay partners — not resolved. Current assumption: invoice monthly on actuals.

---

## 9. FINLAND DMC vs JÄRVISYDÄN

### Järvisydän as MVP
- Järvisydän is the pilot deployment
- Järvisydän IT team participates in development
- Järvisydän's Oracle Opera and BookVisit are the primary booking integrations
- Finland DMC controls Järvisydän's online store → direct webhook, instant Magic Link on purchase
- Järvisydän has ~40 integrated services in Opera
- System branded as "Järvisydän Host" persona: warm, Savolainen style, rento (relaxed)

### Finland DMC as Platform
- Finland DMC is the platform owner and B2B seller
- Finland DMC has 1,000+ pre-planned holiday packages (available for Phase 2)
- Finland DMC provisioned the architecture for all future resorts and travel agencies
- Finland DMC can white-label the assistant for partner travel agencies (KonTiki example)
- Finland DMC manages the Optimizer, data analytics, contract database, partner reporting
- Finland DMC staff operates the Staff Dashboard / Command Center

### Architectural Differences
- Järvisydän MVP: single-tenant config, post-booking assistant only, no Holiday Builder
- Finland DMC platform: multi-tenant from day 1, eventually includes Holiday Builder (pre-booking), supports travel agencies as white-label clients, influencer affiliate mode, and licensing to other DMCs globally
- Both use identical code and infrastructure — distinction is purely in tenant configuration and data scope

### Brand Persona Variants
| Tenant | Name | Style | Colors |
|---|---|---|---|
| Järvisydän (direct) | Järvisydän Host | Warm, savolainen, storytelling | Brown/Gold |
| KonTiki (B2B) | KonTiki Guide | Professional, precise, expert | Dark Blue/Orange |
| Influencer (affiliate) | [Influencer name] | Influencer's curated picks style | Scraped from their IG/site |
| Finland DMC (default) | Finland DMC Assistant | Balanced, helpful, Suomi expert | DMC brand colors |

### Magic Link Entry Points
- **Järvisydän:** Triggered immediately on purchase in online store (Webhook). Agent created within 5–10 seconds. Customer sees "Preparing your personal assistant…" animation, then Magic Link appears on thank-you page. Link also sent via email/SMS.
- **Travel agency booking:** Varausvahvistus (booking confirmation) email sent to customer includes Magic Link. Parser reads email OR Ingestion Service detects booking via API.
- **Individual traveler / direct to Finland DMC:** Landing on finlanddmc.fi → prompts to start planning → enters Holiday Builder flow (Phase 2)

### Järvisydän-Specific Decisions
- Use Järvisydän IT team for API mapping phase
- Webhook from Järvisydän online store directly to DMC Azure cloud (no email parser needed for MVP)
- Järvisydän's BookVisit product catalog as starting source for Commercial Shelf
- Safety Bulletin maintained by Järvisydän guides (ice thickness, route closures) — updated daily via Staff Dashboard

---

## APPENDIX: KEY TECHNICAL SCHEMAS

### User Profile (Ingestion Output / Context Briefcase)
```json
{
  "session_id": "sess_xyz_123",
  "agent_identity": "Matkatoimisto X Assistant (Powered by FinlandDMC)",
  "user_profile": {
    "name": "Mario Rossi",
    "segment": "International / Couple",
    "language": "it",
    "history_notes": "Visits: 1. Sensitivity: Cold temperatures.",
    "status": "VIP (High Spender)"
  },
  "trip_details": {
    "location": "Hotel Järvisydän",
    "dates": "2025-12-10 to 2025-12-14",
    "booked_items": ["Suite 101", "Husky Safari"],
    "budget_remaining": "High"
  },
  "agent_persona": {
    "name": "Järvisydän Assistant",
    "language_mode": "Translation (IT<->EN)",
    "tone": "Warm & Welcoming"
  },
  "service_level": {
    "human_access": true,
    "ai_autonomy": "High"
  }
}
```

### Product Record (Product Warehouse)
```json
{
  "product_id": "act_reindeer_01",
  "base_info": {"name": "Reindeer Visit", "price": 50, "margin_percent": 20},
  "availability_type": "API | MANUAL | AFFILIATE",
  "logistics": {"gps": "62.0N, 28.7E", "duration_minutes": 120, "capacity": 20},
  "cancellation_policy": "Free cancel up to 24h before",
  "dimensions": {
    "energy": 20, "social": 50, "luxury": 40,
    "nature_rawness": 40, "safety_need": 100
  },
  "tags": ["animals", "culture", "slow", "family_friendly"],
  "repeatability": "medium",
  "hooks": {
    "family": "Safe and fun experience for the whole family...",
    "culture": "Authentic connection to northern tradition..."
  },
  "stats": {
    "conversion_rate_family": 0.15,
    "nps_avg": 4.8,
    "value_score": 4.2
  }
}
```

### Shadow Ledger (SQL Table)
| Column | Type | Description |
|---|---|---|
| transaction_id | UUID | Primary key |
| booking_ref | VARCHAR | Link to Itinerary table |
| user_id | UUID | Who bought? |
| provider_id | UUID | Who delivered? (link to Contracts) |
| timestamp | DATETIME | When did transaction occur? |
| flow_type | ENUM | API / MANUAL / AFFILIATE |
| total_amount | DECIMAL | Customer paid (e.g., 200.00) |
| commission_pct | DECIMAL | Contract rate (e.g., 0.15) |
| receivable_amount | DECIMAL | Our share (30.00) — this is what gets invoiced |
| status | ENUM | PENDING / CONFIRMED / CANCELLED / REFUNDED / REFERRED |
| invoice_batch | VARCHAR | Which batch invoice (e.g., "2025-12_ArcticDogs") |

### Scoring Formula
```
Final_Score = (Base_Match * W1) + (Weather_Fit * W2) + (Value_Score * W3) + (Margin_Boost * W4) + (Novelty_Score * W5)

Where W1+W2+W3+W4+W5 = 1.0 and weights vary by customer archetype:
- Budget traveler:  W1=0.30, W2=0.20, W3=0.35, W4=0.05, W5=0.10
- Luxury traveler:  W1=0.40, W2=0.30, W3=0.00, W4=0.20, W5=0.10
- (Exact weights TBD by Optimizer after initial data collection)
```

### Staff Dashboard Priority Queue
```
Urgency_Score = (Wait_Time_Minutes * 1.5) + (Negative_Mood_Score * 2.0) + (VIP_Factor * 10) + (Agent_Confusion * 5)
```

### Tenant Config (Brand Engine)
```json
{
  "tenant_id": "jarvisydan",
  "brand_name": "Järvisydän",
  "assets": {
    "logo_url": "https://assets.dmc.fi/js/logo.svg",
    "concierge_avatar": "https://assets.dmc.fi/js/host_matti.png",
    "font_family_header": "'Playfair Display', serif",
    "font_family_body": "'Lato', sans-serif"
  },
  "colors": {
    "primary": "#4A3B2A",
    "accent": "#C5A065",
    "background": "#F5F5F0"
  },
  "ui_mode": {
    "shape_rounding": "8px",
    "tone_of_voice": "warm_host"
  }
}
```

### System Prompt Template (Base Structure)
```
IDENTITY: You are the [BRAND_NAME] Personal Assistant.
Tone: [BRAND_TONE]
Language: Detect user language. Reply in user's language. Log internal reasoning in English.

CORE OBJECTIVES:
1. Proactively enhance the guest's stay (suggest relevant experiences)
2. Solve problems immediately (concierge services)
3. Ensure safety (check SafetyBulletin before nature advice)

THE BACKPACK (Current Context):
- User: [USER_NAME]
- Location: [ROOM_NUMBER] inside [RESORT_NAME]
- Weather Now: [WEATHER_DATA]
- Next Activity: [NEXT_ITEM] at [TIME]

TOOL USE PROTOCOL (STRICT):
1. DO NOT hallucinate prices or availability
2. Recommendation needed → call Tool_SuggestionChef
3. Booking needed → call Tool_Booker
4. Safety question → check Safety_DB; if data >24h old → Human_Handover
5. Cannot resolve after 3 attempts → call Human_Handover

INTERNAL MONOLOGUE (before responding):
1. Identify Intent
2. Check Mood (angry? → stop selling)
3. Check Gap (time for activity suggestion?)
4. Formulate response
```
