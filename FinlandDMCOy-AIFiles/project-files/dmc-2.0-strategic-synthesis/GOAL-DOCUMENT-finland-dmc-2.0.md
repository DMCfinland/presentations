# Finland DMC 2.0 — Goal Document
## Version 0.1 | Synthesized from 7 specialist agents | 2026-02-22
*Lead synthesis by Opus 4.6 | Agents A1–A7 by Sonnet 4.6*

---

## 0. Correctness Boundaries & Synthesis Methodology

### Synthesis methodology applied
- **Evidence weighting:** Agent claims citing specific file+section outweigh general claims. When agents disagreed, the agent with documentary evidence wins; the other position is preserved as a named option for Patrick.
- **All conflicts resolved or explicitly escalated.** No silent conflict suppression.
- **Assumption audit:** All 7 agents' self-check "Assumptions validated" lines reviewed. Unvalidated assumptions flagged in Section 11.
- **Non-obvious insights elevated.** Agent 7's organizational capacity analysis and Agent 2's adoption flywheel concern are the highest-value non-obvious findings — neither was in the original problem framing.
- **Redundancy eliminated.** BP_08 as go-live blocker was independently raised by A3, A4, A5, and A7. Consolidated into one strong statement with all four sources.

### Fatal errors (destroy trust, must never happen)
- Speculating about Travel Tree API capability — cite `traveltree-api-status.md` only
- Processing named B2B contact PII in Claude Teams before Anthropic DPA + Article 46 SCCs are verified
- Deploying B2C Traveler PWA without Staff Dashboard (BP_08) live — confirmed by A3, A4, A5, A7
- Mixing Zone 1 (B2B) and Zone 2 (B2C) data in shared infrastructure without physical separation

### Acceptable uncertainty (system may express honestly)
- Oracle Opera API surface at Järvisydän — scope unknown, engage IT to determine
- Adyen vs Stripe Connect final choice — both viable, requires Patrick decision
- DPIA outcome — may require architectural changes, GDPR counsel must assess
- Second deployment identity — pipeline not yet validated

### Evidence requirements
- Architecture recommendations cite: file + section (e.g., cluster-b §Tech Choices #1)
- Price/availability claims cite: traveltree-api-status.md + date (2026-02-21, Ihor Kucher WhatsApp)
- B2B/B2C boundary uses: GDPR Article references (A5 Section 4, A6 Section 2)
- TT API capabilities cite: traveltree-api-status.md only — no other source authoritative

---

## 1. What Finland DMC 2.0 Is (Executive Definition)

Finland DMC Oy is a 5-person B2B destination management company that earns 15% commission on every booking it facilitates. Today, every one of those bookings requires a human staff member to write a proposal from scratch, maintain a relationship, and manually coordinate the booking. Revenue scales linearly with headcount. When a staff member leaves — as Janna Kankkunen did in August 2024 — she takes €633K in managed relationships with her.

Finland DMC 2.0 is the deliberate transformation of this company into an information-capital business. The goal is for AI to handle 80–90% of guest interactions automatically, earning the same 15% commission at a fraction of the marginal cost per booking. At 10,000 guests per year with €150 average AI-assisted spend, that is €225,000 in platform commission revenue with near-zero additional staff time. At 20 resort tenants, it reaches €1,350,000. The commission rate does not change. The volume and the marginal cost do.

The transformation happens in two simultaneous tracks. Track 1 (B2B, transition period): capture the institutional knowledge that currently lives in staff heads, use AI to draft proposals faster, and build the human oversight infrastructure that makes automated guest conversations safe. Track 2 (B2C, permanent): deploy an AI travel assistant for resort guests that earns commission on every activity and service booked through the conversation. Järvisydän resort is the first real-world deployment of Track 2. It is not a test — it is the first product.

---

## 2. The Six Products — Roles and Relationships

| Product | Zone | Serves | Produces | Needs From | Owned By |
|---------|------|--------|----------|------------|---------|
| Second Brain | Zone 1 (B2B) | Finland DMC staff | Client profiles, interaction history, RelationshipHealthScore, A4 briefing sheets | Email Drafter outcome signals, Staff Dashboard escalation events | Finland DMC |
| Email Drafter | Zone 1 (B2B) | Finland DMC staff | Personalized proposals with TT links, version_sequences (conversion signal), interaction records | Second Brain client context, TT itinerary links (T1/T2), inbound email | Finland DMC |
| Staff Dashboard | Zone 1+2 boundary | Finland DMC + Järvisydän staff | Human oversight layer: Traffic Light, Whisper, Takeover, God Mode, FIRE RED | Travel Assistant conversation stream, Staff Priority Queue | Finland DMC |
| TT Itinerary Drafter | Zone 1 (B2B) | Finland DMC staff | TT itinerary links for proposals | Second Brain client defaults, TT API T1/T2 (free, enabled on request) | Finland DMC |
| Finland Travel Assistant | Zone 2 (B2C) | Resort guests globally | Shadow Ledger commissions, Mood Matrix behavioral data, booking_source metadata | Oracle Opera API (BLOCKER), BookVisit catalog feed (BLOCKER), Järvisydän DPA (BLOCKER) | Finland DMC (platform) |
| Järvisydän Travel Assistant | Zone 2 (B2C) | Järvisydän guests | Commission revenue at resort scale, proof-of-concept for multi-tenant model | P5 platform live, BP_08 complete, all 6 pre-go-live requirements met | Finland DMC (platform owner) / Järvisydän (data controller) |

**Key integration dependencies:**
- Second Brain → Email Drafter: the core B2B personalization seam. State A: manual M365 copy-paste. State B: n8n NODE 2 automated pull (gated on Supabase schema + contact data import).
- Travel Assistant → Staff Dashboard: hard dependency. BP_08 must be live before B2C conversations begin. No workaround.
- Shadow Ledger → Second Brain: one permitted Zone 2→Zone 1 crossing. Anonymized operator_id + revenue_tier only. Daily batch. No guest PII crosses.

---

## 3. Shared Data Architecture — Recommendation

**Option C: Federated.** Unanimous across all 6 technical agents (A1–A6) through independent convergence. The synthesis adopts this without modification.

**Architecture:**
- **Zone 1 (B2B):** Hetzner VPS (Frankfurt, ~€10–20/mo) + Supabase PostgreSQL + pgvector (EU-native, German data center). Hosts: n8n Email Drafter pipeline, Second Brain production schema (9 tables), booking_source_metadata batch table.
- **Zone 2 (B2C):** Azure North Europe (Ireland). Hosts: all 16 Travel Assistant schemas across Azure SQL, Cosmos DB, Azure AI Search (4 indexes), Azure Data Lake Gen2.
- **No shared integration middleware.** n8n is Zone 1's backbone. Azure Event Grid is Zone 2's backbone. They do not connect.

**Two permitted boundary crossings (both Zone 2 → Zone 1):**
1. Anonymized booking source metadata: operator_id + revenue_tier + booking_count — no guest_id, no name, no behavioral data. Daily batch. Legal basis: GDPR Article 6(1)(f) legitimate interest. Stored in 9th Supabase table (`booking_source_metadata`), isolated from main 8-table schema by RLS.
2. Pseudonymized guest satisfaction via B2B Partner Dashboard (`GET /b2b/customers`): satisfaction scores aggregated or pseudonymized at the API layer before travel agencies access them. Requires Article 13 guest disclosure + Article 28 DPA with each travel agency.

**GDPR boundary (plain-text diagram):**
```
ZONE 1 (Hetzner/Frankfurt — EEA-resident)        ZONE 2 (Azure North Europe — EEA-resident)
┌────────────────────────────────────────┐         ┌────────────────────────────────────────┐
│ Supabase:                              │         │ Azure SQL: Guest profiles, Mood Matrix, │
│  clients, contacts, interactions,      │         │  Shadow Ledger, Products, Contracts,    │
│  components, itineraries,             │         │  Tenants, Itinerary/Booking Reference   │
│  version_sequences, suppliers,         │  ══════▶│ Cosmos DB: Session state, Staff Queue  │
│  rate_cards, golden_prompts,          │  batch  │ Azure AI Search: 4 RAG indexes          │
│  booking_source_metadata (9th)        │  metadata│ Data Lake Gen2: hashed event logs       │
└────────────────────────────────────────┘  only  └────────────────────────────────────────┘
         Article 6(1)(f) — no guest PII crosses
```

**Cost:**
- Zone 1: €160–195/month
- Zone 2 (pilot <100 guests): €244–370/month
- Zone 2 (live 1,000 guests): €640–850/month
- **Total at live scale: €800–1,045/month** (A6 Section 4, Option C)

**Pre-deployment schema requirement (non-negotiable):** All 9 Supabase tables must have `company_id` added BEFORE first data load. This is not a future migration — retrofitting after data exists risks mixing company-level data in version_sequences, destroying the win-rate signal. Day 0 prerequisite.

---

## 4. Integration Architecture — The Nervous System

**Backbone: n8n (Zone 1) + Azure Event Grid (Zone 2). No shared layer.**

```
ZONE 1 INTEGRATION (n8n on Hetzner)
─────────────────────────────────────────────────────────────────────
  Email arrives → n8n NODE 1 (parse) → NODE 2 (Supabase lookup)
  → NODE 3 (Haiku task detection) → NODE 4 (context assembly)
  → NODE 5 (Claude API draft) → NODE 6 (modular assembly)
  → NODE 7 (Teams delivery) → NODE 8 (Supabase interaction log)

  Second Brain State A → B transition trigger:
  Supabase loaded with company_id on all 9 tables + contact data imported
  → n8n NODE 2 replaces manual M365 copy-paste bridge

ZONE 2 INTEGRATION (Azure Event Grid)
─────────────────────────────────────────────────────────────────────
  BookVisit webhook → POST /webhook/booking → Ingestion (BP_01)
  → Magic Link generation → GET /welcome?token={jwt} → Traveler PWA

  Guest message → POST /api/agent/process → Master Agent
  → EVENT_USER_MESSAGE → Mood Evaluator (async)
  → Suggestion Chef call (sync, <800ms) → response

  Escalation → Staff Priority Queue (Cosmos DB) → BP_08 Staff Dashboard
  → POST /staff/whisper or /takeover or /fire-red
```

**Integration flows by priority:**

| Flow | Status | Required For |
|------|--------|-------------|
| Email → n8n → Claude draft | Ready to build | Email Drafter Day 1 |
| TT API T1/T2 (enable) | Free, contact Ihor now | Email Drafter + TT Itinerary Drafter |
| BookVisit webhook → Magic Link | BLOCKER: Järvisydän IT | B2C go-live |
| Oracle Opera → Booker Agent | BLOCKER: API scope unknown | Real-time booking |
| BP_08 ↔ BP_11 live connection | Build in parallel | B2C go-live |
| Shadow Ledger → booking_source batch | Daily job, deferred | Revenue attribution |
| B2B Partner Dashboard (pseudonymized) | Deferred | Year 2 |
| Oracle Opera (full API path) | Deferred: Type B manual until Opera confirmed | Phase 2 |

**TT API integration (citing traveltree-api-status.md, 2026-02-21):**
- T1 (create itinerary via API): YES — free, available now, needs enabling. Unblocks Email Drafter → TT workflow immediately.
- T2 (read itinerary content): YES — free, available now, needs enabling.
- T3 (component library export): PAID — scope TBD, needs call with Ihor. Commercial Shelf seeding blocked until resolved.
- Q6 (client view notifications): UNANSWERED — ask on Ihor call.

---

## 5. GDPR and EU Compliance — Clear Rules

These are rules, not recommendations. Non-compliance is a legal violation.

**Rule 1: Named B2B contact PII (names, emails, phones) MUST NOT enter Claude Teams until Anthropic DPA (GDPR Article 28) is verified and Article 46 transfer mechanism (SCCs) is executed.** Legal basis: Claude Teams uses Anthropic infrastructure with no EU data residency as of Feb 2026. Company-level non-PII records (revenue tier, preferred destination) are lower risk but still require DPA verification. Source: A1 Section 6, A6 Section 3.

**Rule 2: Supabase on Hetzner Frankfurt is the ONLY permissible storage for named B2B contact PII in production (State B).** Hetzner Frankfurt = German data center, EEA-resident, no transfer mechanism required. Execute DPA with Supabase and Hetzner before first data load. Source: A6 Section 3.

**Rule 3: No guest PII may cross the Zone 1 / Zone 2 boundary in identifiable form.** The only permitted crossing is: anonymized operator_id + revenue_tier via daily batch (GDPR Article 6(1)(f) legitimate interest, documented in Article 30 Record of Processing Activities). The B2B Partner Dashboard must pseudonymize or aggregate guest data before travel agencies access it. Source: A5 Section 4, A6 Section 6.

**Rule 4: Mood Matrix "Needs_Accessibility" tag MUST NOT be stored at launch.** This tag constitutes health-adjacent data under GDPR Article 4(15) and likely triggers Article 9(1) prohibition unless Article 9(2)(a) explicit consent is obtained (separate, specific, informed — not bundled with T&Cs). Collect accessibility requirements via a separate pre-arrival form with explicit consent. Source: A3 Section 5, A5 Section 4, A6 Section 2.

**Rule 5: A DPIA (Article 35) is mandatory before go-live with personal data.** Two independent triggers: Article 35(3)(c) — systematic monitoring of individuals in a publicly accessible area (resort AI assistant monitoring all guest interactions); potentially Article 35(3)(a) — automated evaluation affecting individuals (RelationshipHealthScore profiling of B2B contacts). A Finnish GDPR-qualified legal counsel must be identified and commissioned immediately. The DPIA alone may take 6–8 weeks. Source: A3 Section 5, A6 Section 7.

---

## 6. Open Architecture Decisions — Resolved vs. Remaining

### Resolved by synthesis

| Decision | Resolution | Source |
|----------|-----------|--------|
| Infrastructure architecture | Option C Federated (Zone 1 Hetzner/Supabase, Zone 2 Azure) | A6 Section 6 — unanimous across A1–A6 |
| Email Drafter stack | n8n + Supabase (Verdict B — PRD v3 covers Second Brain only) | A2 Section 5 — documentary evidence from both PRD v3 and EMAIL-DRAFTER-DESIGN.md |
| TT API T1/T2 | Free, available now — enable immediately | traveltree-api-status.md (T1/T2 confirmed) |
| Azure region | North Europe — confirmed across 3 sources | A4 Section 1 (cluster-b §Tech Choices, monster-compressed §2, cluster-e §Tech Choices) |
| Second Brain interim | Claude Teams PRD v3 is correct for transition period | A1 Section 7 — correct for months 1–6, not end-state |
| Supabase 9th table | booking_source_metadata — dedicated, RLS-isolated | A6 Section 6 — answers A5's open question |
| Mood Matrix Article 9 | Exclude Needs_Accessibility at launch | A5 Section 4, A6 Section 2 — converged independently |
| Multi-tenancy schema | company_id on all 9 Supabase tables before first data load | A2 Section 7, A6 Section 6 — Day 0, not Phase 2 |

### Escalated to Patrick (decisions with two explicit options)

**Decision 1: Payment processor — Adyen or Stripe Connect?**
- Option A: Adyen — EU-headquartered (Amsterdam), no Article 46 SCCs required, already in use at Järvisydän, stronger GDPR track record. Higher onboarding complexity.
- Option B: Stripe Connect — faster developer onboarding, US-headquartered (requires Article 46 SCCs). Phase 2 virtual card implications differ.
- Trade-off: Adyen has GDPR advantage and alignment with Järvisydän's existing setup; Stripe is faster to integrate at MVP scale. Phase 2 virtual card feature depends on this choice now.
- **Recommended: Adyen** (GDPR grounds + Järvisydän alignment), but Patrick must confirm.

**Decision 2: Anthropic DPA verification timeline**
- Option A: Verify Anthropic DPA immediately (1–2 weeks); execute SCCs for Article 46 transfer; proceed with Claude Teams for company-level records only until verified.
- Option B: Skip Claude Teams for all personal data; go straight to Supabase State B (requires 4+ weeks of schema + contact data import work before Second Brain is useful).
- Trade-off: Option A allows immediate PRD v3 deployment but has a legal gap window; Option B is cleaner but delays staff adoption.
- Patrick must decide and document the chosen transfer mechanism in the Article 30 Record of Processing Activities.

**Decision 3: DPIA ownership and commissioning**
- Who commissions: Patrick (as DPO-equivalent for Finland DMC Oy)
- When: Immediately — 6–8 week lead time before go-live
- Scope: Both B2B Second Brain (automated profiling of contacts) and B2C Travel Assistant (systematic guest monitoring)
- Budget: Finnish GDPR legal counsel — estimate €3,000–8,000 for first DPIA
- This is not a future task. It is on the critical path to Järvisydän launch.

**Decision 4: Järvisydän IT engagement — who initiates, when, what to ask**
- This must be initiated by Patrick immediately. No architecture decision can substitute for it.
- First contact: Introduce the project, request Oracle Opera API documentation + sandbox environment + BookVisit catalog export format.
- Expected lead time: 4–12 weeks for hotel PMS API access (industry standard).
- Architecture fallback if Oracle Opera does not expose a usable REST API: Booker Agent Type B only (manual email confirmation, no real-time availability). Guest experience degrades — guests cannot get instant booking confirmation.

**Decision 5: Staff equity structure**
- Source documents (cluster-a-vision-findings.md) indicate the equity/compensation structure was announced as "details next week" and is still unresolved.
- This is blocking the organizational change management that drives staff adoption (A7 Section 8).
- Staff at 60–70% scared or angry (cluster-a source, Risk #3) will not adopt Products 1 and 2 without concrete incentive alignment.

---

## 7. Recommended Build Sequence

| Phase | Products | What Gets Built | Why This Order |
|-------|----------|----------------|----------------|
| **Phase 0 — Now (before any code)** | All | (1) Enable TT T1/T2 APIs (contact Ihor — free, 1 day). (2) Initiate Järvisydän IT contact (Oracle Opera + BookVisit + webhook). (3) Commission Finnish GDPR legal counsel (DPIA, Anthropic DPA, Järvisydän DPA). (4) Add company_id to Supabase schema before data load. (5) Communicate concrete equity structure to staff. | All 5 actions are critical path blockers with external lead times that no code sprint can compress. Starting them on Day 1 determines launch date more than any technical build decision. |
| **Phase 1 — Month 1–2** | P1 (interim), P2 | (1) PRD v3 Claude Teams setup (Second Brain State A — days, not weeks). (2) n8n Hetzner VPS provisioning + Supabase schema (all 9 tables with company_id). (3) Email Drafter Phase 1: 8-node n8n pipeline, golden prompts for top 5 task types, Supabase connection. (4) Staff onboarding to both tools — change management begins. | Second Brain State A unblocks Email Drafter value immediately. Phase 1 generates the version_sequences data and golden prompt feedback needed for Phase 2 quality. Staff adoption starts here — every week of delay compounds the adoption gap. |
| **Phase 2 — Month 2–4** | P3, P4, P5 (foundation) | (1) BP_08 + BP_11 parallel build begins. BP_08 (Staff Dashboard): Traffic Light, Whisper, Takeover, FIRE RED. BP_11 (Traveler PWA): Järvisydän theme, Magic Link, chat interface. (2) BookVisit catalog ingestion → Commercial Shelf → Chef Agent scoring. (3) DPIA completed, filed. (4) Järvisydän DPA and commercial terms negotiated and signed. | BP_08 and BP_11 must be parallel — neither can validate without the other. BP_08 is the go-live gate. DPIA and DPA must complete before guest PII enters the system. |
| **Phase 3 — Month 4–8** | P6, P1 (State B) | (1) Järvisydän go-live: BP_08 complete + DPIA filed + all 10 non-technical pre-go-live items met (A3 Section 6). (2) Measure AI autonomous resolution rate — target 85%/30 days. (3) Second Brain migration to Supabase State B when: Anthropic DPA verified + contact data imported from email mining sessions. (4) Identify and sign second tenant. | Go-live is gated on BP_08, not BP_11. The second tenant validates the multi-tenant architecture and begins building the cross-resort dataset that constitutes Finland DMC's long-term moat. |

**Non-negotiable go-live gates for Phase 3 (Järvisydän):**
- BP_08 Staff Dashboard functional (Traffic Light + Whisper + Takeover + FIRE RED minimum)
- GDPR Article 28 DPA between Finland DMC and Järvisydän signed
- DPIA completed and filed
- Updated guest privacy notice live on jarvisydan.com
- Commission structure agreement signed
- Safety Bulletin governance: named owner, update protocol, liability terms
- Järvisydän IT: Oracle Opera API (or Type B fallback confirmed), BookVisit webhook live, booking catalog ingested
- Staff trained: Järvisydän reception + Finland DMC monitoring staff

---

## 8. The North Star

Finland DMC 2.0 succeeds when the majority of its commission revenue requires no human proposal-writing time. Every other metric is a proxy for this structural shift.

**The weekly metric Patrick reads:** AI-assisted booking revenue as a percentage of total Finland DMC commission revenue. Measured via Shadow Ledger `booking_source_metadata` against total commission ledger. When this number crosses 50%, Finland DMC has crossed the threshold — it is no longer a DMC that uses AI; it is an AI platform that was formerly a DMC.

| Metric | Current State | 6-Month Target | 12-Month Target | Measurement |
|--------|--------------|----------------|-----------------|-------------|
| AI-assisted commission % | 0% (no B2C product) | 5% (Järvisydän pilot live) | 25% (Järvisydän at scale + 1-2 tenants signed) | Shadow Ledger booking_source / total commission ledger |
| AI autonomous resolution rate | Not measurable (BP_08 not built) | 70% (Järvisydän pilot baseline) | 85% sustained / 30 days (bridge threshold) | Staff Dashboard intervention logs / total conversations closed |
| Staff time per €1K commission | Measure at Month 1 (baseline) | –20% vs baseline | –50% vs baseline | Time tracking in Staff Dashboard + proposal logs |

**The bridge threshold:** When AI autonomous resolution rate exceeds 85% sustained over a 30-day rolling window (measured in BP_08 Staff Dashboard), monitoring burden becomes manageable at scale. Below this threshold, the transition model is a trap — staff monitoring scales linearly with guest volume. Above it, monitoring becomes exception-handling. This metric is the most important number in Finland DMC 2.0 until it crosses 85%.

---

## 9. The Five Biggest Risks (Ranked)

| # | Risk | Probability | Impact | Mitigation |
|---|------|-------------|--------|------------|
| 1 | **BP_08 (Staff Dashboard) not built before B2C launch** — confirmed independently by A3, A4, A5, A7. Go-live blocker. If BP_08 lags, the transition model doesn't exist — it is an AI with no human safety net. | HIGH (already true: not started, XL complexity) | CRITICAL (blocks entire B2C revenue model) | Make BP_08 the primary build constraint. Parallel with BP_11. Set BP_08 completion as the hard go-live gate. No exceptions. |
| 2 | **Organizational capacity overextension (Patrick as single point of failure)** — A7 Section 8. 5-person company asked to build 6 products, engage Järvisydän IT, commission DPIA, manage staff cultural change, negotiate contracts, and run the existing DMC business simultaneously. | HIGH (structural, not hypothetical) | CRITICAL (default outcome if not addressed) | Separate build decisions from operational decisions. Engage external counsel for GDPR (DPIA, DPAs). Engage a technical PM or second developer for BP_08 build. Patrick focuses on: Järvisydän IT engagement, equity structure, staff change management. |
| 3 | **DPIA/legal prerequisites not completed before go-live** — A3 Section 5, A6 Section 7. DPIA is mandatory (Article 35(3)(c) and 35(3)(b)). No Finnish GDPR counsel identified. Lead time: 6–8 weeks minimum. DPIA may require architectural changes. | HIGH (clock is already running) | CRITICAL (go-live legally blocked without it) | Commission Finnish GDPR counsel immediately (Phase 0). Budget €3,000–8,000. Scope: Second Brain profiling + Travel Assistant systematic monitoring. Allow 8 weeks before planned launch date. |
| 4 | **Järvisydän IT engagement delayed — critical path blocker** — A4 Section 5, A5 Section 9 Q2. Oracle Opera API credentials, BookVisit catalog, booking webhook, DPA — all require Järvisydän IT cooperation. Hotel PMS API access: 4–12 weeks industry standard. | HIGH (already true: not initiated) | HIGH (determines Phase 3 launch date) | Initiate contact immediately (Phase 0). Ask for: Oracle Opera API docs + sandbox, BookVisit catalog export format, webhook endpoint configuration. Simultaneously: design Type B manual booking fallback so build can proceed without Opera confirmation. |
| 5 | **Staff adoption failure (flywheel never ignites)** — A2 Section 8, A7 Section 2. Email Drafter value depends on staff actually using it and rating drafts. Cultural shift from author to editor requires deliberate change management. 60–70% of staff are currently scared or angry (cluster-a source). | MEDIUM (manageable if addressed explicitly) | HIGH (Products 1-2 permanently at Phase 1 capability if adoption fails) | Resolve equity structure concretely (not "details next week"). Identify 1-2 early adopter staff members to pilot Products 1-2 before full rollout. Build feedback mechanisms into tools (Friday review cycle is designed correctly — execute it). Do not launch Email Drafter as a mandate; launch as a choice with visible wins. |

---

## 10. Conflicts and Disagreements Between Agents

All major conflicts were resolved during synthesis. No silent suppressions.

| Conflict | A Position | B Position | Resolution |
|----------|-----------|-----------|------------|
| Second Brain storage (Teams vs Supabase) | A1: PRD v3 Claude Teams = correct interim | A2: Supabase = production target | **RESOLVED:** Sequential, not competing. PRD v3 = Phase 0–1 interim. Supabase = production target after migration trigger. A2's framing is correct (PRD v3 Client Communications project IS Email Drafter in manual mode). |
| Zone 1 → Zone 2 data flow | A1: nothing crosses in transition period | A3: Shadow Ledger booking metadata flows Z2→Z1 | **RESOLVED by A5:** Anonymized operator metadata (no guest PII) permitted under Article 6(1)(f). A1's rule is correct for guest PII; A3's observation is correct for anonymized business intelligence. |
| Mood Matrix Article 9 | A3: health data risk | A4: documented without flagging | **RESOLVED by A5+A6:** Exclude Needs_Accessibility at launch. Both are correct — A3 identified the risk, A4 documented the schema, A5/A6 resolved it. |
| Payment processor (Adyen vs Stripe) | A4+A5+A6: Adyen preferred (GDPR + Järvisydän alignment) | No counter-position from other agents | **ESCALATED TO PATRICK:** Synthesis recommends Adyen; Patrick must decide and commit before Phase 2 architecture. |
| Staff Dashboard build ownership | A4+A5: go-live blocker, XL, not started | No counter-position | **ESCALATED TO PATRICK:** Who builds BP_08? External contractor, internal build with Patrick as PM? This is the single most important resource allocation decision in the roadmap. |

---

## 11. What This Document Does NOT Answer

These are the questions for Patrick's next decision session. Every item below was raised by one or more agents and cannot be resolved by synthesis alone.

**Commercial and organizational:**
1. At what booking volume does Finland DMC need to hire a dedicated platform operations role? (A7 Q1 — no staffing model exists for running a multi-tenant AI platform)
2. What are the contractual terms protecting Finland DMC's cross-resort data rights at Järvisydän renewal? (A7 Q2 — first tenant has de facto pricing power in Year 1 if they represent 100% of platform revenue)
3. Which 1658 Holdings portfolio company is the second deployment? Does the pipeline justify the multi-tenant architecture investment? (A7 Q3 — pipeline not validated)
4. What is the concrete equity structure for Finland DMC staff? (cluster-a source: "details next week" — unresolved, blocking adoption)
5. What is the minimum booking volume that makes the platform financially sustainable per tenant? (A3 Q2 — no platform cost model exists)

**Technical (require external information):**
6. Oracle Opera API surface at Järvisydän: what endpoints are available for availability check and reservation creation? (A4 Q1 — cannot design Booker Agent BP_06 without this)
7. TT T3 component library export: scope, cost, timeline? (A5 Section 3 — Commercial Shelf is partially blocked without this)
8. Adyen onboarding timeline and minimum volume requirements for Finland DMC? (A6 Q1 — needed before payment processor decision is final)

**Legal:**
9. Anthropic DPA: does it satisfy GDPR Article 28 and does it include Article 46 SCCs for transfers to the US? (A1 Q2, A6 Q2 — blocking named contact PII in Claude Teams)
10. DPIA scope: does the B2B Second Brain RelationshipHealthScore also trigger Article 35(3)(a), requiring a separate DPIA from the B2C Travel Assistant DPIA? (A6 Q3 — Finnish GDPR counsel must assess)
11. Who is legally liable when the AI gives advice based on a stale Safety Bulletin? (A3 Q1 — no document defines the liability chain between Finland DMC, Järvisydän, and the guest)

---

*Finland DMC 2.0 Goal Document v0.1 — synthesized from 7 specialist agents by Opus 4.6*
*Agent team: dmc-synthesis | 2026-02-22 | Estimated synthesis cost: ~$17-22 USD*
