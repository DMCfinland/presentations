# Pipedrive vs Custom Second Brain CRM — Research Briefing

## Company: Finland DMC Oy
- 5-person B2B destination management company (incoming tourism to Finland)
- 107 active client companies (tour operators worldwide)
- Revenue €3.2M, 44% proposal win rate
- AHI Travel = 75% revenue (critical concentration risk)
- Uses Microsoft 365 (shared mailbox info@finlanddmc.fi, Teams, SharePoint)
- NO CRM currently — everything in email + staff memory
- Staff #1 complaint: "entering data into systems takes too long"

## Sales Cycle
Inquiry → Proposal (custom itinerary + pricing) → Revisions (1-3 rounds) → Confirmation → Operation (coordinate suppliers, guides, transport) → Post-trip follow-up → Invoicing

## DMC-Specific Needs (not in generic CRM)
- Seasonal pricing (summer/winter rates, shoulder seasons)
- Multi-destination itineraries (3-7 day programs with daily activities)
- Supplier management (hotels, restaurants, activity providers, guides)
- Commission tracking (15-20% from suppliers, exceptions for some services)
- Group size/pax tracking (affects pricing tiers)
- Post-sale operations (trip coordination, not just deal closing)
- TravelTree itinerary software integration

## Staff Map
| Staff | Role | Style |
|-------|------|-------|
| Liisa Vihermaa | Product & Sales Manager | Formal, structured |
| Laura Ilvonen | Group ops + Iceland FIT | Formal, detailed |
| Reeta Vihavainen | Program ops + repeat accounts | Warm, relationship-focused |
| Sebastian Heiskanen | FIT/boutique | Casual, creative |
| Piia Laitila | Product & Sales Manager | Professional |
| Patrick (CEO) | System builder, strategic | Builds the tools |

---

## PIPEDRIVE: What Grok Found (2 research rounds)

### Strengths
1. **Visual Kanban pipeline** — drag-and-drop, clean, "Trello for sales." Staff opens it every morning.
2. **Activity-based selling** — forces next activity on every deal. Shifts from "hit quota" to "do 5 things today."
3. **1-day onboarding** — CSV import + pipeline setup + M365 connect = operational immediately.
4. **Smart Docs** — proposal templates with auto-fill, trackable PDF (open notifications), e-signatures.
5. **M365 email sync** — auto-captures emails to deal timeline. Shared mailbox supported via team config.
6. **No-code automations** — follow-up reminders, stale deal alerts, stage moves, email sequences.
7. **AI Sales Assistant** — win probability, deal prioritization, email drafting (basic context).
8. **Mobile app** — 4.5-4.7/5 rated, full offline, pipeline + activities + logging.
9. **Projects** — deal Won → Project with Kanban phases for post-sale coordination.
10. **Reporting** — revenue by client, pipeline by stage, win rate, forecasting. Out-of-box.
11. **Price** — €220-270/month for 5 users (Professional tier).
12. **Data export** — full CSV + API bulk export, no lock-in.
13. **Finnish UI** — supported.

### Weaknesses
1. **Data entry NOT solved** — deal creation = manual. Phone calls = manual. Stage updates = click. Non-email activities = manual. "Same complaint will reappear after 2-3 months."
2. **50-70% CRM implementations fail** — adoption is #1 cause.
3. **Zero travel/DMC integrations** — no TravelTree, Tourplan, Bokun. Marketplace is 95% generic.
4. **No DMC-specific features** — no seasonal pricing, no itinerary versioning, no supplier management, no commissions, no pax tracking.
5. **AI drafting is shallow** — no full client history mining, no relationship health scores, no personalized tone per staff member.
6. **Smart Contact Data weak** — basic enrichment only, no deep LinkedIn. Poor for Asian agencies.
7. **Shared mailbox setup complex** — works but requires specific team config, not seamless.
8. **Proposal revisions = attachments/notes** — no structural revision tracking.
9. **Projects feature immature** — basic Kanban tasks, not real operations management.

### Grok Bottom Line
"Stick with custom AI Second Brain. Pipedrive doesn't solve data entry. Hybrid could work short-term."

---

## OUR CUSTOM SYSTEM: What's Designed

### Second Brain (CRM layer)
- Auto-mines M365 emails → builds client profiles (ZERO manual entry)
- 107 client profiles already extracted from proposals (session 38)
- Tracks: revenue per client, win rate, proposal history, relationship health score (5 weighted factors)
- Daily digest per staff member (open threads, next actions, alerts)
- A4 client insight pages (auto-generated weekly for top 10)
- Growth roadmap per client (strategic plans)
- Content taxonomy: 4 categories (client_interaction, team_feedback, weekly_win, growth_idea)
- Retention: 24-month rolling for interactions, indefinite for client/contact records

### Email Drafter (proposal layer)
- AI writes personalized proposals using full client context + history
- Golden prompts per task type (13 identified)
- Staff tone matching (Laura formal, Reeta warm, Sebastian casual)
- Commission rules enforced automatically (15-20%, exceptions for Solitary etc.)
- Win-rate engine: tracks which itinerary components win deals
- n8n 8-node automated pipeline: email arrives → classify → lookup → draft → review

### Staff Dashboard (BP_08 — pipeline layer)
- Designed but NOT yet built
- Traffic light for B2C conversations (Green/Yellow/Red)
- Was designed for B2C guest monitoring, NOT B2B pipeline
- Does NOT currently include: Kanban pipeline, deal tracking, activity logging

### Infrastructure
- Claude AI (Sonnet 4.6 default, Opus for complex)
- Supabase (PostgreSQL + pgvector) — 8-table schema designed
- n8n (self-hosted, Hetzner Frankfurt)
- Next.js frontend (FinnConcierge codebase exists)
- M365 Graph API for email/calendar/SharePoint access
- Multi-tenant: company_id + RLS for portfolio companies

### What's Missing from Our Plan (gaps Pipedrive fills)
1. **No visual pipeline/Kanban for B2B deals** — BP_08 is B2C only
2. **No activity-based selling system** — no "next action" enforcement
3. **No proposal tracking** — no "client opened your PDF" notifications
4. **No mobile-first design** — FinnConcierge is desktop-focused
5. **No day-1 usability** — system requires weeks of building
6. **No drag-and-drop UX** — current design is data-centric, not interaction-centric

---

## CRM LANDSCAPE: What Grok Found (13 tools compared)

### Best Contenders (from 13 tools)

**Moonstride (€595/month, DMC-specific):**
- Only tool combining real CRM pipeline + full DMC ops (itinerary, suppliers, commissions, pax, seasonal pricing)
- AI profiling + chatbot + content writer/translator
- Kanban pipeline view
- BUT: no native M365 shared mailbox, not zero-entry, not self-hosted
- Data entry burden: 8/10 (good but not perfect)

**Attio ($145-300/month, AI-first):**
- Auto-enrichment from emails/websites/LinkedIn = near zero manual entry
- Excellent pipeline + AI suggestions
- BUT: no M365 shared mailbox, no DMC features
- Data entry burden: 9/10

**Folk CRM ($110-240/month, "CRM for people who hate CRMs"):**
- Auto-populates contacts from email + AI assistants for follow-ups
- Pipeline Kanban, strong M365 Outlook sync
- BUT: no DMC features, no shared mailbox native
- Data entry burden: 9/10

**Twenty (€0, open-source, self-hostable):**
- Self-host on Hetzner alongside Supabase, full API/webhooks
- Can wire Claude AI directly into it
- BUT: requires development to add DMC features
- Data entry burden: 9/10 (with AI layer)

**HubSpot Free ($0-75/month):**
- Surprisingly capable free tier: full pipeline, email tracking, tasks
- Strong M365 integration
- BUT: no DMC features, AI basic, scales expensive

### Key Finding: The Industry Gap
NO tool combines real sales CRM (pipeline, activities, zero-entry) with real DMC ops (itinerary, suppliers, commissions, pax). The industry is split: generic CRM or tour ops tool, never both.

### Top 10 Features to Steal (build into custom system)
1. Auto-enrichment + magic fields (Attio/Folk) — zero manual contact creation
2. Next-activity forcing with auto-suggestions (Pipedrive via AI)
3. Drag-and-drop itinerary builder with live supplier pricing (Tourwriter/Moonstride)
4. Pax-range + seasonal pricing calculator (Moonstride)
5. AI proposal drafter with full history + relationship health (Folk + Claude)
6. Deal rotting + stale alerts pushed to Teams (HubSpot)
7. Commission & supplier ledger auto-tracked from bookings
8. Visual Kanban pipeline that auto-moves on email replies (Monday + n8n)
9. Mobile offline updates with photo attachments (Pipedrive/Monday)
10. Self-hosted data layer (Twenty style) — own everything

### Why Teams Love Pipedrive (emotional drivers)
1. Kanban = feeling of control — see everything at a glance
2. Activities = daily wins — "do 5 things" removes quota anxiety
3. Instant value — operational in 1 day vs weeks
4. Smart Docs — trackable proposals with open notifications
5. Mobile — works offline, in the field

### The Adoption Truth
- 50-70% of CRM implementations fail (adoption #1 cause)
- "Same complaint will reappear after 2-3 months" — Grok's honest assessment
- Minimum viable entry per deal even with all automations: 3-5 manual actions
- Custom system with email mining: ZERO manual entry

---

## THE QUESTION FOR EACH AGENT

Given ALL the above: Should Finland DMC buy Pipedrive, build custom, or go hybrid? Each agent analyzes from their specific angle and produces a concrete recommendation with implementation specifics.
