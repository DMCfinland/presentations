# Second Brain ERP & CRM — 6-Week Implementation Roadmap

**Date:** 2026-03-10
**Decision:** BUILD CUSTOM (unanimous across 4 agents)
**Total build estimate:** 172 hours / 6 weeks (1 full-time developer)
**3-year TCO:** EUR 33,650 (cheapest option)

---

## Pre-Build Checklist (Week 0 — Before Any Code)

Complete all items before Week 1 development begins. Target: 2-3 days.

| # | Task | Owner | Time | Done |
|---|------|-------|------|------|
| 1 | **Temporary Kanban in Microsoft Planner** — 5 columns (Inquiry / Proposal Sent / Revision / Confirmed / Operating). Populate with 10-15 active deals from current knowledge. | Patrick | 2h | [ ] |
| 2 | **Team meeting (30 min)** — Run the 3-step pitch (script below). Collect input on what staff wants on deal cards. | Patrick | 30min + prep | [ ] |
| 3 | **Database migration script** — Create 3 new tables in Supabase: `deals`, `deal_activities`, `deal_stage_history`. Apply RLS. Seed `deals` from existing 107 client profiles. | Dev | 8h | [ ] |
| 4 | **n8n workspace setup** — Create skeleton workflows W1-W4 (empty nodes, correct triggers, named). Connect M365 Graph API shared mailbox subscription. | Dev | 4h | [ ] |
| 5 | **TravelTree API enablement** — Contact Ihor Kucher. Enable T1 (create itinerary) + T2 (read itinerary). Both free. Confirm endpoints + auth. | Patrick | 1h + wait | [ ] |
| 6 | **Developer secured** — Confirm who builds this: Patrick, freelancer, or split. Book 6 weeks of availability. | Patrick | — | [ ] |
| 7 | **M365 Graph API subscription** — Verify shared mailbox webhook is active and extensible for deal classification. Test with a dummy email. | Dev | 2h | [ ] |
| 8 | **Design assets** — Export Agent 1 wireframes (morning dashboard, deal card, Kanban) as reference for frontend build. | Patrick | 1h | [ ] |

### Team Meeting Script (30 min — The 3-Step Pitch)

**Step 1: VALIDATE (5 min)**
> "Kuulin teidät. Haluatte nähdä diilit yhdessä paikassa, lopettaa muistinvaraisen seurannan, ja saada järjestelmän joka oikeasti auttaa. Pipedrive on hyvä työkalu — tutkin sen perusteellisesti."

**Step 2: EDUCATE (10 min)**
> "Pipedrive on loistava geneerisille myyntitiimeille. Mutta meillä on sesongit, itinerarit, komissioprosentit, pax-hinnoittelu — mitään näistä Pipedrive ei osaa. Ja vaikka Pipedrive näyttää kauniilta, se vaatii silti manuaalista syöttöä jokaiseen diiliin. 50-70% CRM-käyttöönotoista epäonnistuu juuri tästä syystä."

**Step 3: CO-CREATE (20 min)**
> "Tässä on mitä rakennan — ja haluan teidän panoksenne."
> - Show the Planner Kanban board (already populated)
> - Ask each person: "Mitä haluatte nähdä aamulla ensimmäisenä?"
> - Write answers on whiteboard/shared doc

**Per-person hooks:**
- **Liisa:** Tarkat komissiolaskelmat, sesonkihinnoittelu, toimittajarekisteri
- **Reeta:** Jokainen keskustelu, suositukset, asiakkaan mieltymykset — suhdeäly
- **Sebastian:** Nolla lomakkeita. Järjestelmä seuraa sähköposteja automaattisesti.
- **Laura:** Jokainen revisio, pax-muutos, toimittajavahvistus — kaikki tallessa
- **Piia:** Ammattimainen pipeline-näkymä, asiakaskortit, tarjousten seuranta

---

## Week-by-Week Implementation Plan

### Week 1: "Teidän pipeline, tänään" (Foundation + Visibility)

| What is built | Hours | Component |
|---------------|-------|-----------|
| Database schema: `deals`, `deal_activities`, `deal_stage_history` + RLS + views | 8h | Backend |
| Seed deals table from 107 client profiles (historical proposals) | 4h | Data migration |
| n8n W1: Email-to-deal pipeline (email classification + auto-creation) | 16h | Automation |
| **Week 1 total** | **28h** | |

**What staff sees:** Planner Kanban board (from Week 0) with their deals. Patrick message: "Tässä on näkymänne — tänään. Lopullinen versio päivittyy itsestään."

**Adoption milestone:** Staff corrects and completes their own deals on the Planner board. Each person claims ownership of their cards. Expect 2-3 "where is deal X?" questions — good sign, means they are engaging.

**Staged reveal moment:** Staff sees a populated board on Day 1 without entering anything.

**Risk / blocker:**
- M365 Graph API subscription delay (webhook approval can take 24h)
- Email classification accuracy below 80% on first pass — acceptable, tune in Week 2
- Developer bottleneck if also handling Week 0 tasks

**Cost:**
| Item | Amount |
|------|--------|
| Development (28h x EUR 80) | EUR 2,240 |
| Infrastructure (Supabase free tier, Hetzner existing) | EUR 0 |
| Claude API (Sonnet for email classification testing) | ~EUR 5 |
| **Week 1 total** | **~EUR 2,245** |

---

### Week 2: Morning Digest + Auto-Classification

| What is built | Hours | Component |
|---------------|-------|-----------|
| n8n W2: Stage auto-progression rules | 12h | Automation |
| n8n W3: Stale deal alerts (daily cron) | 4h | Automation |
| Daily digest Teams message (per staff member, 8:30am) | 8h | Automation + formatting |
| **Week 2 total** | **24h** | |

**What staff sees:** Every morning at 8:30, a Teams message: "3 asiaa tänään: vastaa AHI:lle, seuraa Regentiä, lähetä Intrepid-tarjous." Plus stale deal alerts for deals silent >7 days.

**Adoption milestone:** Staff reads the morning digest. First "how did it know about that?" moment when system surfaces a deal from an email nobody manually logged.

**Staged reveal moment:** "Taikahetki" — a deal appears that no one manually entered. The system mined it from email overnight.

**Risk / blocker:**
- Stage auto-progression false positives (keyword "confirm" in non-confirmation emails). Mitigation: medium-confidence transitions require staff approval (one-click in Teams).
- Daily digest too noisy. Start with top-3 only, not exhaustive list.

**Cost:**
| Item | Amount |
|------|--------|
| Development (24h x EUR 80) | EUR 1,920 |
| Claude API (Haiku for daily classification, ~50 deals) | ~EUR 3 |
| **Week 2 total** | **~EUR 1,923** |

---

### Week 3: Proposal Tracking + Kanban Frontend Start

| What is built | Hours | Component |
|---------------|-------|-----------|
| n8n W4: Proposal tracking webhook (SharePoint link analytics) | 8h | Automation |
| Frontend: Kanban board — column layout, card rendering, Supabase Realtime | 20h | Frontend (Next.js) |
| **Week 3 total** | **28h** | |

**What staff sees:** "Asiakas avasi tarjouksesi klo 14:32" notification in Teams. First preview of the real Kanban board (read-only, still rough).

**Adoption milestone:** First proposal-opened notification arrives. Staff feels connected to client's decision process. The "proposal black hole" anxiety lifts.

**Staged reveal moment:** Proposal tracking replaces guessing with data. "They opened it twice" = warm signal.

**Risk / blocker:**
- SharePoint Graph API analytics endpoint may have 4-6h delay on view detection. Fallback: Approach B (redirect link via Next.js API route, ~20 lines of code).
- Kanban drag-and-drop not ready yet — board is view-only this week. Set expectations.

**Cost:**
| Item | Amount |
|------|--------|
| Development (28h x EUR 80) | EUR 2,240 |
| Claude API | ~EUR 2 |
| **Week 3 total** | **~EUR 2,242** |

---

### Week 4: Kanban Interactive + Deal Drawer

| What is built | Hours | Component |
|---------------|-------|-----------|
| Frontend: Kanban board — drag-and-drop, filters, color coding | 20h | Frontend |
| Frontend: Deal detail drawer (activity timeline, client profile, edit fields) | 24h | Frontend |
| **Week 4 total** | **44h** | |

**What staff sees:** Full interactive Kanban board. Cards are color-coded (green/yellow/red). Click a card to see full deal history, client profile, AI-suggested next action. Drag cards between stages.

**Adoption milestone:** Staff stops using the Planner board and switches to the real Kanban. The temporary board served its purpose — retire it.

**Staged reveal moment:** "Now I can see everything" — the Hook 1 emotional payoff from Agent 1.

**Risk / blocker:**
- This is the heaviest frontend week (44h). If developer falls behind, split Deal Drawer into Week 4 (basic) + Week 5 (full).
- Real-time sync issues with Supabase Realtime if multiple staff drag cards simultaneously. Test with 2 concurrent users.

**Cost:**
| Item | Amount |
|------|--------|
| Development (44h x EUR 80) | EUR 3,520 |
| Claude API | ~EUR 2 |
| **Week 4 total** | **~EUR 3,522** |

---

### Week 5: Daily Dashboard + AI Suggestions

| What is built | Hours | Component |
|---------------|-------|-----------|
| Frontend: Daily dashboard (personal landing page, server-rendered) | 16h | Frontend |
| AI next-action suggestions (Claude Haiku per deal, integrated into dashboard + deal drawer) | 8h | Backend + AI |
| M365 Graph API calendar integration (meeting detection -> deal activities) | 12h | Integration |
| **Week 5 total** | **36h** | |

**What staff sees:** A personal landing page: "Good morning, Reeta." Shows their deals by stage, overdue actions (red), today's activities, AI-suggested next steps per deal. Calendar meetings auto-logged.

**Adoption milestone:** Staff opens the dashboard BEFORE opening email. The system becomes the starting point for the workday.

**Staged reveal moment:** AI suggests a specific next action with full context: "AHI replied requesting aurora alternatives. Suggest: send revised itinerary with Saariselka option (their preferred region last year)."

**Risk / blocker:**
- AI suggestion quality depends on sufficient deal activity data. If deals are new (seeded this week), suggestions may be thin. Supplement with data from 107 client profiles.
- Calendar integration requires additional M365 Graph permissions (Calendars.Read). Verify in advance.

**Cost:**
| Item | Amount |
|------|--------|
| Development (36h x EUR 80) | EUR 2,880 |
| Claude API (Haiku for suggestions, ~50 deals/day) | ~EUR 5 |
| **Week 5 total** | **~EUR 2,885** |

---

### Week 6: Mobile PWA + Testing + Polish

| What is built | Hours | Component |
|---------------|-------|-----------|
| Frontend: Activity logger (quick-add calls, notes) | 8h | Frontend |
| PWA configuration (service worker, manifest, offline, push notifications) | 8h | Frontend |
| End-to-end testing + bug fixes + polish | 16h | QA |
| **Week 6 total** | **32h** (incl. 8h buffer from 172h total) | |

**What staff sees:** System works on phone. Push notification: "AHI opened your proposal." Quick actions from mobile: approve AI draft, snooze reminder, add voice note.

**Adoption milestone:** At least 2 staff members install the PWA on their phone. System usage extends beyond desktop/office hours.

**Staged reveal moment:** First push notification on mobile for a proposal view. System follows you — in a helpful way.

**Risk / blocker:**
- PWA push notifications require HTTPS + service worker registration. Verify Hetzner VPS has valid SSL cert.
- iOS PWA limitations (no background sync, limited push in some versions). Test on actual staff devices.
- Week 6 is also buffer week. If earlier weeks ran over, PWA can slide to Week 7.

**Cost:**
| Item | Amount |
|------|--------|
| Development (32h x EUR 80) | EUR 2,560 |
| Claude API | ~EUR 3 |
| **Week 6 total** | **~EUR 2,563** |

---

## Cost Summary (6 Weeks)

| Week | Dev Hours | Dev Cost (EUR 80/h) | Infrastructure | Claude API | Total |
|------|-----------|---------------------|----------------|------------|-------|
| 0 (Pre-build) | 15h | 1,200 | 0 | 0 | **1,200** |
| 1 | 28h | 2,240 | 0 | 5 | **2,245** |
| 2 | 24h | 1,920 | 0 | 3 | **1,923** |
| 3 | 28h | 2,240 | 0 | 2 | **2,242** |
| 4 | 44h | 3,520 | 0 | 2 | **3,522** |
| 5 | 36h | 2,880 | 0 | 5 | **2,885** |
| 6 | 32h | 2,560 | 0 | 3 | **2,563** |
| **Total** | **207h** | **16,560** | **0** | **20** | **16,580** |

Note: 207h exceeds original 172h estimate by 35h (Week 0 prep + deal seeding + buffer). Infrastructure cost is EUR 0 incremental — Hetzner VPS + Supabase free tier already running. Monthly ongoing after launch: ~EUR 3/mo Claude API + EUR 320/mo maintenance (4h x EUR 80).

---

## 10 "Stolen Features" — Implementation Schedule

Features sourced from Grok Round 3 research across 13 CRM tools. Mapped to specific build weeks.

| # | Feature | Source | Week | Phase | Component |
|---|---------|--------|------|-------|-----------|
| 1 | **Auto-enrichment + magic fields** — zero manual contact creation from email mining | Attio / Folk | W1-2 | MVP | n8n W1 email-to-deal pipeline |
| 2 | **Next-activity forcing with AI suggestions** — system recommends next step per deal | Pipedrive philosophy + AI | W5 | MVP | AI suggestion engine (Haiku) |
| 3 | **Deal rotting + stale alerts to Teams** — 7/14/21-day silence warnings | HubSpot | W2 | MVP | n8n W3 stale deal alerts |
| 4 | **Pax + seasonal pricing calculator** — auto-price from rate cards with commission logic | Moonstride | Phase 2 (M2) | Phase 2 | Rate Card Manager + Pricing Calculator |
| 5 | **AI proposal draft with full context** — cover email + pricing block, client-tone matched | Folk + Claude | Phase 2 (M2-3) | Phase 2 | Email Drafter integration |
| 6 | **Auto-moving Kanban from email signals** — pipeline cards progress based on email content | Monday + n8n | W2 | MVP | n8n W2 stage auto-progression |
| 7 | **Commission + supplier bookkeeping** — auto-tracked per deal with exception rules | Moonstride | Phase 2 (M2) | Phase 2 | Supplier Rate Card Manager |
| 8 | **Trackable proposal links with view notifications** — "client opened at 14:32" | Pipedrive Smart Docs | W3 | MVP | n8n W4 + SharePoint tracking |
| 9 | **Mobile offline updates** — PWA with push notifications | Pipedrive / Monday | W6 | MVP | PWA service worker |
| 10 | **Self-hosted data layer** — own all data, no vendor lock-in | Twenty CRM | W1 | MVP | Supabase (already self-managed) |

**MVP (Weeks 1-6): Features 1, 2, 3, 6, 8, 9, 10** — 7 of 10 features ship in the initial build.

**Phase 2 (Months 2-3): Features 4, 5, 7** — These require the Rate Card Manager (supplier data migration: 3-5 days of manual data work) and Email Drafter integration. Build estimate: 5-7 additional weeks.

---

## Dependencies and Blockers

### 1. Developer Availability

| Option | Pros | Cons | Recommendation |
|--------|------|------|----------------|
| **Patrick builds it** | Zero communication overhead, deep domain knowledge | Takes Patrick away from CEO duties for 6 weeks | Only if no other option |
| **Freelancer (full-time, 6 weeks)** | Dedicated build capacity, EUR 80/h market rate | Needs onboarding on Supabase/n8n/Next.js stack + domain knowledge | **Recommended** — Patrick specs, freelancer builds |
| **Split (Patrick specs + freelancer executes)** | Best of both — Patrick's domain + freelancer's dev time | Coordination overhead, needs clear specs per week | **Best option if freelancer is strong on Next.js** |

**Action needed:** Secure a freelancer by end of Week 0. Requirements: Next.js, Supabase, n8n experience. 6-week contract, full-time. Budget: EUR 16,560.

### 2. M365 Graph API — Shared Mailbox Webhook

| Item | Status | Action |
|------|--------|--------|
| Mail subscription on info@finlanddmc.fi | Already active (Email Drafter uses it) | Extend classification to tag deal-relevant emails |
| Calendar read permissions | Not yet enabled | Request `Calendars.Read` scope in Azure AD app registration |
| OneDrive/SharePoint analytics | Available on existing plan | Verify `analytics` endpoint returns view data for sharing links |
| Graph webhook renewal | Webhooks expire after 3 days (mail) | n8n cron to auto-renew subscriptions every 2 days |

**Blocker risk: LOW.** M365 connector already authenticated. Extensions are permission additions, not new connections.

### 3. Supplier Rate Card Data Migration

**Not needed for MVP (Weeks 1-6).** Required for Phase 2 features 4, 5, 7.

| Task | Effort | Who |
|------|--------|-----|
| Identify all current rate card sources (Excel files, emails, PDFs) | 0.5 days | Patrick + Liisa |
| Design import template (CSV/Excel matching rate_cards schema) | 0.5 days | Dev |
| Manual data entry: ~200 supplier services x seasonal variants | 2-3 days | Liisa or intern |
| Validate: commission exceptions, expired rates, missing suppliers | 0.5 days | Patrick |
| **Total** | **3-5 days** | |

**Schedule:** Start during Week 4-5 in parallel with frontend build. Data ready by end of Week 6 for Phase 2 kickoff.

### 4. TravelTree API Enablement

| API | Status | Cost | Action |
|-----|--------|------|--------|
| T1 — Create itinerary | Available, needs enabling | Free | Contact Ihor, request activation |
| T2 — Read itinerary content | Available, needs enabling | Free | Contact Ihor, request activation |
| T3 — Export component library | Paid, scope TBD | TBD | Defer to Phase 2. Schedule call with Ihor in Month 2. |

**Blocker risk: MEDIUM.** T1+T2 enablement depends on Ihor's response time. Email in Week 0, follow up in Week 1 if no response. T1+T2 are not critical-path for MVP — the Kanban and digest work without TravelTree. Integration becomes important in Phase 2 when proposal building is automated.

### 5. Dependency Map

```
Week 0: Planner board ─────────────────────────────────────────────> Staff uses immediately
Week 0: DB migration ──> Week 1: n8n W1 (email→deal) ──> Week 2: n8n W2 (auto-stage)
                                                          Week 2: n8n W3 (stale alerts)
Week 0: M365 webhook ──> Week 1: Email classification ──> Week 2: Daily digest
                          Week 3: n8n W4 (proposal tracking)
Week 3: Kanban start ──> Week 4: Kanban interactive + Deal drawer
                          Week 5: Dashboard + AI suggestions
                          Week 6: PWA + Activity logger

CRITICAL PATH: DB migration → n8n W1 → Kanban board → Deal drawer → Dashboard
```

---

## Month 3 Checkpoint

**Date target:** ~12 weeks after Week 1 start (accounts for 6 weeks build + 6 weeks of live usage).

### 6 Adoption Metrics

| # | Metric | Target | How to Measure | Source |
|---|--------|--------|----------------|--------|
| 1 | Daily digest open rate | >60% of staff, >4 days/week | Teams read receipts or email tracking | Agent 4 |
| 2 | Pipeline board visits | >3x/week per staff member | Next.js page view analytics (simple counter) | Agent 4 |
| 3 | Manual corrections decreasing | Week-over-week downward trend | Count feedback messages / correction requests | Agent 4 |
| 4 | "I didn't know about that" moments | >2 per staff member (cumulative) | Ask in monthly feedback sessions | Agent 4 |
| 5 | Staff-initiated feature requests | >1 per person (cumulative) | Track in shared doc or Planner | Agent 4 |
| 6 | Pipedrive mentions | Zero or declining to zero | Listen in meetings and Teams | Agent 4 |

### Decision Gate Criteria

| Outcome | Criteria | Action |
|---------|----------|--------|
| **CONTINUE** (target) | 3+ of 5 staff use daily digest regularly AND pipeline board is default deal-status check | Proceed to Phase 2: Rate Card Manager, Pricing Calculator, Email Drafter integration |
| **ADJUST** | 2 of 5 staff engaged, others indifferent | Run brutally honest feedback session. Fix specific blockers. Extend trial by 4 weeks. |
| **PIVOT to Moonstride** | <2 of 5 staff engaged after adjustments | Execute data export plan (below). Deploy Moonstride as operations layer. Keep Second Brain as intelligence backend. |

### Data Export Plan (If Pivot Needed)

If the Month 3 checkpoint triggers a pivot to Moonstride:

| Step | Action | Time |
|------|--------|------|
| 1 | Export `deals` table as CSV (all fields) | 10 min |
| 2 | Export `deal_activities` as CSV | 10 min |
| 3 | Export `clients` + `contacts` tables as CSV | 10 min |
| 4 | Map exported fields to Moonstride import format (CRM module) | 2-4h |
| 5 | Import into Moonstride via their API or CSV import | 1-2h |
| 6 | Verify deal count, client count, activity count match | 30 min |
| 7 | Keep Second Brain running as backend intelligence (email mining, client profiles, relationship health) | Ongoing |
| 8 | Wire n8n to push email-mined data into Moonstride via their API | 8-16h |
| **Total pivot effort** | | **1-3 days** |

**Key principle:** No data is lost in a pivot. Supabase data exports cleanly. The Second Brain's intelligence layer (107 client profiles, relationship health scores, interaction history) remains valuable regardless of which frontend CRM is used.

---

## Phase 2 Preview (Months 2-3, Post-MVP)

These features begin after Week 6 MVP launch, built in parallel with live system usage.

| Feature | Weeks | Depends On | Priority |
|---------|-------|------------|----------|
| Rate Card Manager (Feature 4 — supplier CRUD UI) | 1-2w | Supplier data migration complete | High |
| Auto-Pricing Calculator (Feature 1 — commission logic) | 1w | Rate Card Manager live | High |
| Email Drafter integration (Feature 2 — auto-draft proposals) | 4-6w | Pricing Calculator + golden prompts | High |
| Supplier Booking Workflow (Phase 5 ops gap) | 3-4w | Rate Card Manager | Medium |
| Win-Rate Engine (Feature 5 — component analytics) | 2-3w | 50+ labeled deal outcomes in DB | Medium |
| Operational Document Generator (daily program sheets) | 1-2w | Supplier Booking Workflow | Low |
| TravelTree T3 integration (component library export) | 1w | Call with Ihor, pricing agreed | Low |

**Phase 2 total estimate:** 13-20 weeks (overlapping with ongoing maintenance). Builds the operations layer that makes Moonstride unnecessary.

---

## Quick Reference: What Ships When

| Week | Staff Sees | Emotional Hook |
|------|-----------|---------------|
| 0 | Planner Kanban with their deals | "I can see everything — today" |
| 1 | (Backend work, no visible change) | — |
| 2 | Morning digest in Teams at 8:30 + stale deal alerts | "It read my emails and told me what to do" |
| 3 | "Client opened your proposal at 14:32" notification | "I'm connected to the client's decision" |
| 4 | Real Kanban board — drag, filter, color-coded cards | "Now I can see everything — for real" |
| 5 | Personal dashboard + AI next-action suggestions | "It knows what I should do and why" |
| 6 | Mobile PWA + push notifications | "It's always with me" |

---

## Handoff Notes for Developer

**Stack:** Next.js (FinnConcierge codebase) + Supabase (existing 9-table schema) + n8n (self-hosted on Hetzner) + M365 Graph API (authenticated)

**Key files to read first:**
- `AGENT-2-TECHNICAL-ARCHITECT.md` — full database schema, n8n workflow specs, frontend component specs
- `AGENT-1-UX-ADOPTION.md` — wireframes (morning dashboard, deal card, Kanban layout)
- `AGENT-3-DMC-OPERATIONS.md` — commission logic, supplier data model, TravelTree boundary
- `EMAIL-DRAFTER-DESIGN.md` — existing n8n pipeline design (extend, don't rebuild)

**Critical technical decisions already made:**
- Drag-and-drop library: `@dnd-kit/sortable` (MIT, 15KB gzipped)
- Real-time: Supabase Realtime (WebSocket, not polling)
- Proposal tracking: SharePoint sharing links + Graph API analytics (primary), redirect link (fallback)
- Mobile: PWA (not native apps)
- Stage auto-progression: medium-confidence transitions require staff approval (not auto-move)
- Deal card view: Supabase SQL view joining `deals` + `clients` tables (server-side, not N+1 queries)

**Definition of done per week:** Feature works end-to-end with real data. No "demo mode" or hardcoded values. Ship at 70% polish — team feedback refines the remaining 30%.
