# Mining Output — Cluster B: Technical Core
Source files: DD1 Brain's Logic (FI), SYSTEM_CONTEXT_v2.2, PROJECT_CONTEXT, MISSION_PROFILE_v2.2
Mined: 2026-02-21

---

## IMPORTANT FRAMING NOTE

These 4 documents cover TWO different topics:
- **DD1 + PROJECT_CONTEXT:** B2C guest-facing Travel Assistant product spec (what to build)
- **SYSTEM_CONTEXT_v2.2 + MISSION_PROFILE_v2.2:** Universal Agentic Protocol v2.2 ("Darwinian League") — a meta-framework for building AI agent systems (how to build anything)

The Darwinian League architecture may be intended as the build methodology for the Travel Assistant itself.

---

## DECISIONS

1. [source: PROJECT_CONTEXT] **Tech stack chosen: Microsoft Azure (North Europe region)** — Azure Functions (Python/Node.js), Azure Event Grid (event bus), Azure OpenAI Service GPT-4o via Private Endpoint (Zero Data Retention), Azure SQL (relational), Cosmos DB (chat logs/session state), Azure AI Search (vector RAG), Data Lake Gen2 (analytics raw logs), Next.js PWA (frontend).

2. [source: PROJECT_CONTEXT] **Architecture pattern: Orchestrator Model** — Master Agent is the only component that communicates with users. Specialist agents (Mood Evaluator, Suggestion Chef) are background microservices returning JSON on request.

3. [source: PROJECT_CONTEXT] **Multi-tenant "Chameleon" UI** — The PWA loads `tenant_config.json` on startup. Järvisydän gets brown/gold theme + "Savolainen Isäntä" persona. KonTiki gets blue/orange + "Expert Guide" persona.

4. [source: PROJECT_CONTEXT] **Data strategy: "Scrape First, Negotiate Later"** — Aggregate all destination data (commercial + non-commercial) to create value first, then convert vendors to commission partners.

5. [source: PROJECT_CONTEXT] **Business model: Win-Win-Win-Win** — Traveler (free service), DMC (commissions + efficiency), Partners (ready-to-buy customers), B2B Agencies (white-label solution).

6. [source: SYSTEM_CONTEXT_v2.2] **Agent selection: 2+1 Rule** — Every task attempted by 3 agents: King (highest ELO), Challenger (random Top-5), Wildcard (random Rookie). Anti-monopoly: 5% ELO decay per week.

7. [source: SYSTEM_CONTEXT_v2.2] **Memory architecture: MEM1 (Constant-Memory)** — Agent does not read chat log. Reads a single compressed Internal State (IS) token. On git commit, container killed, agent reborn with only IS token. Eliminates "Context Rot."

8. [source: SYSTEM_CONTEXT_v2.2] **Prompt evolution: GEPA (Genetic-Pareto Prompt Adaptation)** — When agent fails, system captures trace, breeds "Child Prompt" with specific guardrail for that error. Pareto Frontier balances speed vs. accuracy.

9. [source: DD1] **Mood profiling: Cluster archetypes** — Users "forced" into nearest archetype (e.g., "German_Active_Family") for statistical optimization. Cluster can change as data accumulates. 7 mood dimensions (0-100): Energy, Hunger, Social_Battery, Luxury_Affinity, Nature_Rawness, Safety_Need, Foodie_Focus.

10. [source: DD1] **Scoring formula (Suggestion Chef):** `Final_Score = (Base_Match*W1) + (Weather_Fit*W2) + (Value_Score*W3) + (Margin_Boost*W4) + (Novelty_Penalty)` — with Epsilon-Greedy 80/20 exploitation/exploration split.

11. [source: DD1] **A/B testing on sales hooks** — Each product has multiple "Hooks" (Family/Adventure/Nature). Champion/Challenger selection: 80% show winning Hook for cluster, 20% test challenger.

12. [source: SYSTEM_CONTEXT_v2.2] **Security: The Vault** — Agents never see API keys. They request `Vault.get('key')`. Key injected by MCP Guardian at network layer, not context layer. (OWASP Agentic Top 10 mitigation.)

---

## REQUIREMENTS

1. [source: PROJECT_CONTEXT] The Master Agent MUST query `SafetyBulletin_Tool` before answering nature/safety questions. If data >24h old → trigger human handover.

2. [source: DD1] Chef query latency MUST be under 800ms. Requires RAG indexes in memory (In-Memory Vector DB, e.g., Redis or Pinecone).

3. [source: PROJECT_CONTEXT] Staff dashboard MUST support: Whisper (human types → AI rephrases), Takeover (human disconnects AI), Teach (thumbs up/down to feed Optimizer).

4. [source: PROJECT_CONTEXT] FIRE RED protocol: Emergency/safety words detected → AI stopped immediately, human takes over.

5. [source: DD1] Gap Finder MUST run every 30 minutes as cronjob. Only active 08:00–22:00. Only fires if: session active + gap in itinerary + weather/mood threshold met.

6. [source: DD1] Manual Override: Staff dashboard "God Mode" button can force-push a product to all users in a region, bypassing algorithm.

7. [source: PROJECT_CONTEXT] Booking logic must handle 3 types: API (automated capture), Manual/Email (24h auth timeout), Affiliate (trackable link + ledger log).

8. [source: PROJECT_CONTEXT] Shadow Ledger: All transactions logged with flow_type (API/MANUAL/AFFILIATE), status, commission_pct, receivable_amount.

9. [source: SYSTEM_CONTEXT_v2.2] No code written until `todo.md` is updated. Gatekeeper (Auditor agent) validates `spec.md` for ambiguity before tournament starts.

10. [source: SYSTEM_CONTEXT_v2.2] Collaborative Repair: If winner's code fails Red Team, losers (other agents) offered repair job. Repair valid only if changed tokens < 10% of file.

11. [source: PROJECT_CONTEXT] Language detection: If user speaks Italian → reply in Italian, but log internal thoughts in English.

12. [source: DD1] Patience meter (0-100): If < 30, activate "Silent Mode" — no upselling.

---

## TECH CHOICES

1. [source: PROJECT_CONTEXT] **CHOSEN — Azure OpenAI GPT-4o (Private Endpoint, Zero Data Retention)** as AI engine. Explicitly Azure, not generic OpenAI.

2. [source: PROJECT_CONTEXT] **CHOSEN — Azure SQL** for relational data (ledger, users, products).

3. [source: PROJECT_CONTEXT] **CHOSEN — Cosmos DB** for chat logs and session state (hot storage).

4. [source: PROJECT_CONTEXT] **CHOSEN — Azure AI Search** for vector RAG storage.

5. [source: PROJECT_CONTEXT] **CHOSEN — Azure Functions (Python/Node.js)** as serverless compute/microservices.

6. [source: PROJECT_CONTEXT] **CHOSEN — Azure Event Grid** as event bus connecting all agents.

7. [source: PROJECT_CONTEXT] **CHOSEN — Next.js PWA** as frontend.

8. [source: DD1] **MENTIONED — Redis or Pinecone** as in-memory vector DB options for <800ms latency requirement. Not definitively chosen between them.

9. [source: SYSTEM_CONTEXT_v2.2] **CHOSEN (for agentic build framework) — ELO ranking** for agent selection. Replaces static role assignment.

10. [source: SYSTEM_CONTEXT_v2.2] **CHOSEN (for code changes) — AST (OpenRewrite)** is mandatory. Regex is explicitly banned.

11. [source: SYSTEM_CONTEXT_v2.2] **MENTIONED — Shapley Counterfactual Credit Assignment (Kuang et al., 2025)** for agent incentive math.

12. [source: PROJECT_CONTEXT] **MENTIONED — Azure Functions (North Europe region)** — not Azure Sweden Central (contrast: Second Brain used Sweden Central for GDPR).

---

## RISKS

1. [source: DD1] Hallucination risk on prices/availability — hard constraint: "DO NOT hallucinate prices or availability." Must use Tool calls, not memory.

2. [source: DD1] Safety data staleness — if SafetyBulletin data >24h old, system must escalate. Nature advice (ice thickness, northern lights) is a liability risk.

3. [source: DD1] "Chef latency" bottleneck — if recommendation engine exceeds 800ms, fallback to generic list (Restaurant, Walk). Degraded user experience.

4. [source: SYSTEM_CONTEXT_v2.2] "Free-rider" agents — without Shapley value enforcement, agents can pass tests without contributing. Degrades system quality over time.

5. [source: SYSTEM_CONTEXT_v2.2] Context rot — long chat history causes hallucination loops. MEM1 solves this but requires strict git-commit-triggered resets.

6. [source: SYSTEM_CONTEXT_v2.2] Excessive Agency (OWASP Agentic Top 10) — agents doing too much outside their scope. Mitigated by The Vault and strict tool protocols.

7. [source: PROJECT_CONTEXT] Data aggregation legal risk — "Scrape First, Negotiate Later" strategy carries licensing and terms-of-service risk before vendor agreements are in place.

8. [source: DD1] Novelty Penalty edge case — if a product is "High Repeatability" (e.g., sauna), must not apply novelty penalty. Requires explicit product flagging.

---

## OPEN QUESTIONS

1. [source: DD1] Redis vs. Pinecone not resolved — which in-memory vector DB for <800ms Chef latency?

2. [source: PROJECT_CONTEXT] North Europe vs. Sweden Central for Azure deployment — PROJECT_CONTEXT says North Europe, but GDPR compliance for CRM data requires EU data residency. Are these the same legal region?

3. [source: SYSTEM_CONTEXT_v2.2] Is the "Darwinian League" build framework intended for building the Travel Assistant specifically, or is it a general agentic coding protocol Patrick developed?

4. [source: SYSTEM_CONTEXT_v2.2] How does the Darwinian League relate to the Travel Assistant build phases — is Patrick planning to use competitive multi-agent coding to build the product itself?

5. [source: PROJECT_CONTEXT] "B2B Agencies: White-label solution for their customers" — is this a planned revenue stream from Day 1, or aspirational?

6. [source: DD1] Optimizer night job — who runs this? Requires cron infrastructure and data science pipeline not described elsewhere.

---

## NOTABLE QUOTES

1. [DD1] *"Järjestelmän älykkyys ei asu yhdessä mallissa, vaan se on jaettu Orkestraattori-malliin. Tämä estää hallusinaatiot ja mahdollistaa modulaarisen kehityksen."* — "The system's intelligence does not reside in one model but is distributed in the Orchestrator Pattern. This prevents hallucinations and enables modular development."

2. [PROJECT_CONTEXT] *"The invisible guide in your pocket. Proactive, context-aware, and transactional."* — Core product promise.

3. [PROJECT_CONTEXT] *"Scrape First, Negotiate Later."* — Explicit data strategy.

4. [SYSTEM_CONTEXT_v2.2] *"Be cynical about 'happy paths.' Assume everything breaks."* — Tone mandate for system design.

5. [DD1] *"Chef ei arvo. Se suodattaa."* — "Chef doesn't guess. It filters." — Core philosophy of the recommendation engine.
