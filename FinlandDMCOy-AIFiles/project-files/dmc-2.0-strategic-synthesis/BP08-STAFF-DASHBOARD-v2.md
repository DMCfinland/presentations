# BP_08 Staff Dashboard v2.0 — Dual-Mode Design
**Status:** UPDATED — North Star + Opportunity Engine added (2026-03-13)
**Date:** 2026-03-10 | **Last updated:** 2026-03-13
**Owner:** Patrick Heiskanen
**Use:** Developer scope document + internal architecture reference

---

## North Star (D50 — design target for all future decisions)

> "Every morning I open the PWA and the Second Brain has already prepared my day: three hot opportunities it spotted overnight — AHI Travel's Lapland anniversary window opens in 10 days with a ready strategy and email draft; Flash Pack is 8 months dormant but their 18-month pattern says now is perfect; plus two upsell chances on current groups drawn from identical past wins. I click into each card, review the three-option brief (recommended one highlighted with risk/reward), tweak one sentence if needed, hit Approve — the agent sends the perfectly personalised message, tracks opens, and only nudges me later if required. The system remembers every client interaction, seasonal cycle, supplier rate, and successful approach from the last five years better than any of us ever could, so our tiny 5-person team operates with the memory and foresight of a 50-person operation. It surfaces what matters, suggests without ever deciding, and lets us spend every minute on the relationships that actually close deals."

**Test every new feature against:** *Does this move us closer to this experience?*

---

---

## What Changed from v1.0

v1.0 was B2C-only: traffic light monitoring for the Finland Travel Assistant (Jarvisydan guest conversations). v2.0 adds a complete B2B pipeline management layer — same app, same auth, two modes. The B2B side is needed NOW (no pipeline visibility today); the B2C side is needed before Jarvisydan go-live.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│              BP_08 Staff Dashboard v2.0                  │
│                 (Next.js PWA)                            │
│                                                         │
│  ┌─────────────────────┐  ┌──────────────────────────┐  │
│  │   B2B Pipeline Tab  │  │   B2C Monitoring Tab     │  │
│  │                     │  │                          │  │
│  │  Kanban Board       │  │  Traffic Light Dashboard │  │
│  │  Morning Dashboard  │  │  Whisper Mode            │  │
│  │  Deal Cards         │  │  Takeover Mode           │  │
│  │  Proposal Tracking  │  │  FIRE RED Escalation     │  │
│  │  Activity Nudging   │  │  Queue & Notifications   │  │
│  └─────────────────────┘  └──────────────────────────┘  │
│                                                         │
│  Shared: Auth (Azure AD B2C) · Role-based access        │
│  Shared: PWA shell · Push notifications · Audit logs    │
└─────────────────────────────────────────────────────────┘
         │                           │
    Zone 1 (B2B)               Zone 2 (B2C)
    Supabase + n8n             Cosmos DB + Event Grid
    Hetzner                    Azure North Europe
```

**Key architectural decision:** B2B and B2C use different backends (Supabase vs Cosmos DB) but share a single Next.js frontend with tab-based navigation. This reflects the existing infrastructure split — B2B pipeline data lives in the Second Brain (Supabase/Hetzner), B2C conversation data lives in Azure Zone 2.

---

## Tab 1: B2B Pipeline Management

### 1.1 Kanban Board (primary view)

**Pipeline stages (left to right):**
```
inquiry → proposal_sent → revision → confirmed → operating → invoiced
```

Drag-and-drop between stages. Backward moves require a reason (logged to deal_stage_history). Deals can move to `lost` from any stage.

**Board layout:**
```
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ INQUIRY  │ PROPOSAL │ REVISION │CONFIRMED │OPERATING │ INVOICED │
│    (8)   │   (12)   │   (5)    │   (7)    │   (3)    │   (2)    │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│┌────────┐│┌────────┐│          │          │          │          │
││AHI     ││Regent   ││          │          │          │          │
││24 pax  ││8 pax   ││          │          │          │          │
││€42,800 ││€18,200 ││          │          │          │          │
││3d ago  ││9d ago  ││          │          │          │          │
│└────────┘│└────────┘│          │          │          │          │
│┌────────┐│┌────────┐│          │          │          │          │
││Intrepid ││Exodus   ││          │          │          │          │
││...      ││...      ││          │          │          │          │
│└────────┘│└────────┘│          │          │          │          │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
  Filter: [All Staff ▾] [All Seasons ▾] [Value Range ▾] [Client Tier ▾]
```

**Filters:** staff owner, season (summer/winter/shoulder), value range, client tier (Gold/Silver/Bronze).

**Real-time updates:** Supabase Realtime (WebSocket subscription on `deals` table). When n8n auto-creates or updates a deal from email, all open dashboards update instantly. No polling.

**Library:** `@dnd-kit/sortable` (MIT, 15KB gzipped, React/Next.js compatible).

### 1.2 Deal Cards

Each card on the Kanban board displays:

```
┌─────────────────────────────┐
│ [green] AHI Travel — Summer '26 │  ← Left border = health color
│ Helsinki + Lapland 7d        │  ← Itinerary summary
│ 24 pax · €42,800            │  ← Group size + value
│ Proposal v2 sent 3 days ago │  ← Current status
│ Opened 2x                   │  ← Proposal tracking signal
│ → Reeta                     │  ← Owner
│ Next: Send revised pricing   │  ← AI-suggested action
└─────────────────────────────┘
```

**Health score color coding (left border):**
| Color | Condition |
|-------|-----------|
| Green | On track — client engaged in last 7 days |
| Yellow | Attention — 7-14 days since last contact OR revision overdue |
| Red | At risk — 14+ days silent OR deadline approaching |
| Blue | Confirmed/operating — no sales action needed |

**Urgency signals:**
- Pulsing border: action overdue by 2+ days
- "Hot" badge: client opened proposal 3+ times (high intent)
- "Expiring" badge: seasonal pricing window closing

**Data sources per card:**
- Deal data: `deals` table (value, pax, stage, dates)
- Client context: `clients` table via join (revenue_tier, relationship_health_score)
- Last interaction: `interactions` table (most recent timestamp)
- Win probability: calculated from historical win rate + stage duration + season

Server-side Supabase view (`deal_cards`) pre-joins all sources.

### 1.3 Morning Dashboard

Personalized landing page. What staff sees at 8:30am:

```
┌─────────────────────────────────────────────────────────┐
│  Good morning, Reeta               Monday 10 March 2026 │
│                                                          │
│  YOUR DAY                          PIPELINE SNAPSHOT     │
│  ┌──────────────────────┐          Inquiry    ████ 8     │
│  │ 3 things today:      │          Proposal   ██████ 12  │
│  │  □ Reply AHI Travel  │          Revision   ███ 5      │
│  │  □ Follow up Regent  │          Confirmed  ████ 7     │
│  │  □ Send Intrepid Q   │          Operating  ██ 3       │
│  └──────────────────────┘                                │
│                                                          │
│  OVERNIGHT                         ALERTS                │
│  4 new emails parsed               [red] Regent: 9 days │
│  2 proposals viewed                [yellow] Exodus:      │
│  AHI itinerary confirmed               revision due tmrw │
│                                                          │
│  [View Pipeline]  [View Emails]  [View Proposals]        │
└─────────────────────────────────────────────────────────┘
```

**Design decisions:**
- Personal greeting — the system knows WHO is logged in
- "3 things today" is AI-generated from overnight email analysis (NOT manual entry — this is the killer difference from Pipedrive)
- Pipeline snapshot uses horizontal bars (visual, not numeric)
- "Overnight" shows what the AI processed while staff slept — reinforces zero-entry value
- Alerts use traffic light colors matching deal card health scores
- Generated server-side via Supabase query (no Realtime needed for static morning view)

### 1.4 Activity Nudging

AI-powered next-action suggestions. Replaces Pipedrive's manual "add activity" with "approve AI recommendation."

**Flow:**
1. n8n monitors shared mailbox continuously (M365 Graph API subscription)
2. New email classified: `new_inquiry` | `existing_deal` | `non_deal`
3. AI suggests next action with context: _"AHI replied requesting aurora alternatives for March group. Suggest: send revised itinerary with Saariselka option (their preferred region last year). Draft ready — review and send?"_
4. Staff clicks: **[Send as-is]** / **[Edit first]** / **[Dismiss]**
5. Action completes → system auto-logs to `deal_activities`, suggests next step

**Daily rhythm (Teams notifications via n8n W3):**
| Time | Notification |
|------|-------------|
| 08:30 | Morning briefing: "3 items need your attention today" |
| 12:00 | Midday nudge (only if morning items unaddressed): "Regent follow-up still open" |
| 16:30 | End-of-day summary: "You handled 4/5 items. AHI response carries to tomorrow." |

**Stage auto-progression rules (n8n W2):**

| Trigger Event | Detection Method | Stage Transition | Confidence |
|---------------|-----------------|------------------|------------|
| Client sends inquiry email | Email classification (Sonnet) | → `inquiry` (new deal) | High |
| Staff sends email with PDF attachment | Attachment MIME check + subject match | → `proposal_sent` | High |
| Client replies to proposal | Reply-to threading (M365 conversationId) | No auto-move | N/A |
| Staff sends revised proposal | 2nd+ PDF to same thread | → `revision` | Medium |
| Client confirms (keyword: "confirm", "book", "proceed") | NLP detection | → `confirmed` + staff alert | Medium — staff must approve |
| Trip dates pass | Date comparison (departure_date < today) | → `invoiced` reminder | High |

Medium-confidence transitions create a pending notification. Staff approves with one click.

### 1.5 Stale Deal Alerts

| Color | Days Since Last Activity | Action |
|-------|------------------------|--------|
| Green | < 7 days | No alert |
| Yellow | 7-14 days | Yellow badge on card + included in morning briefing |
| Red | > 14 days | Red badge + Teams notification + Patrick alerted |

Daily cron (n8n W3, 08:00 Helsinki): queries deals where stale_days > 7, generates Teams adaptive card per staff member with Haiku-generated 1-line follow-up suggestions. Cost: ~€0.01/day.

### 1.6 Proposal Tracking

**Primary method: SharePoint sharing links (Approach A)**
1. Staff uploads proposal PDF to SharePoint
2. n8n generates sharing link via Graph API
3. Link sent to client instead of PDF attachment
4. Graph API analytics polled every 4 hours: `GET /drives/{id}/items/{id}/analytics`
5. First view detected → `deal_activity` (type = `proposal_viewed`) + Teams notification to deal owner

**Notification to staff:** _"AHI Travel opened your proposal at 14:32, viewed for 4 minutes"_

**Fallback: Redirect link (Approach B)**
For clients whose email systems block SharePoint preview:
- Custom URL: `proposals.finlanddmc.fi/p/{token}`
- Next.js API route (~20 lines) logs access + serves PDF + triggers n8n webhook

**Pipeline integration:** `proposal_viewed` updates `deals.last_activity`. If deal is in `proposal_sent` and no reply within 3 days after view, W3 generates: _"Client viewed your proposal 3 days ago but hasn't replied — consider a follow-up."_

---

## Tab 2: B2C Conversation Monitoring

All requirements from bp08-mvp-scope.md v1.0 preserved without changes. This tab is the go-live safety net for the Finland Travel Assistant (Jarvisydan guest conversations).

### 2.1 Traffic Light Dashboard (real-time)

- Live list of active Travel Assistant conversations (Cosmos DB queue)
- Color coding: **Green** (normal), **Yellow** (needs review), **Red** (escalated)
- Filters: resort, guest mood score, time since last message
- Both Finland DMC staff view and Jarvisydan staff view (role-based)

### 2.2 Whisper Mode

- Staff sends private hint/suggestion to the AI mid-conversation. Guest does not see it.
- AI incorporates the hint in its next response.
- Full audit log: whisper content, timestamp, AI reaction, staff ID.
- Without Whisper, escalation is binary (watch or full takeover). At scale with 100+ concurrent conversations, binary escalation is operationally disruptive.

### 2.3 Takeover Mode

- One-click full human takeover — staff takes over conversation from AI
- Seamless handoff; full conversation history visible to staff
- Auto-notification to Jarvisydan reception if needed
- AI resumes after staff marks conversation resolved

### 2.4 FIRE RED Escalation

- One-click FIRE RED → immediate human takeover + notification to Jarvisydan staff on duty + full audit log entry
- Auto-escalation triggers (configurable by resort admin):
  - Profanity detected
  - Health/accessibility keywords (Article 9 GDPR risk)
  - >5 minutes no AI response
  - Guest explicitly requests human or booking
- Notification channels: in-app + email (push notification as Phase 3+ enhancement)

### 2.5 Queue and Notifications

- Mobile-friendly view (phone priority — staff often away from desk)
- Browser alerts for Yellow/Red items (no sound by default; configurable)
- Full audit log (who saw what, when, what action taken) — required for DPIA and EU AI Act Art 50

---

## Shared Infrastructure

### Authentication and Authorization

**Provider:** Azure AD B2C (consistent with existing FinnConcierge codebase)

**Role-based access:**
| Role | B2B Tab | B2C Tab | Notes |
|------|---------|---------|-------|
| Finland DMC staff | Full access | Full access | Pipeline + monitoring |
| Jarvisydan staff | No access | Full access | Guest monitoring only |
| Patrick (admin) | Full access + admin | Full access + admin | Config, user management |

### Frontend Stack

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Framework | Next.js | Consistent with FinnConcierge codebase |
| Deployment | PWA (Progressive Web App) | Same codebase for desktop + mobile, offline support, push notifications |
| Drag-and-drop | @dnd-kit/sortable | MIT, 15KB gzipped, React-native |
| B2B real-time | Supabase Realtime (WebSocket) | 1 persistent connection per client, instant updates |
| B2C real-time | Azure Event Grid + WebSocket | Cosmos DB change feed → dashboard |
| Styling | Tailwind CSS | Already in FinnConcierge |

### PWA Capabilities

| Feature | B2B | B2C |
|---------|-----|-----|
| Offline read | Yes — cached pipeline view, deal cards | No — real-time conversations require connectivity |
| Offline write | Yes — queue actions, sync when online | No |
| Push notifications | Proposal opened, stale deal, morning briefing | Yellow/Red escalation, FIRE RED |
| Home screen install | Yes | Yes |

### Database Architecture

**B2B (Zone 1 — Supabase/Hetzner):**
- 3 new tables: `deals`, `deal_activities`, `deal_stage_history`
- Added to existing 9-table Second Brain schema
- RLS: `company_id = current_setting('app.company_id')`
- Pre-joined view: `deal_cards` (deals + clients + interactions)

**B2C (Zone 2 — Azure North Europe):**
- Cosmos DB: conversation history, audit log
- Event Grid: guest conversation events
- No direct connection to Zone 1

### n8n Workflows (4 new, B2B only)

| Workflow | Trigger | Action |
|----------|---------|--------|
| W1: Email → Deal | New email in shared mailbox | Classify → create/update deal → log activity |
| W2: Stage Auto-Progression | Email classified as deal-related | Apply stage transition rules → log to history |
| W3: Stale Deal Alerts | Daily cron 08:00 | Query stale deals → Teams adaptive card per staff |
| W4: Proposal Tracking | HTTP webhook / Graph API poll | Log proposal view → notify deal owner |

---

## Non-Functional Requirements

| Requirement | B2B Tab | B2C Tab |
|-------------|---------|---------|
| Data zone | Zone 1 only (Supabase/Hetzner) | Zone 2 only (Azure Event Grid + Cosmos DB) |
| GDPR | Company data, standard processing | Pseudonymized guest IDs only (no names) |
| Uptime | 99.5% (business hours) | 99.9% (24/7 — guest-facing dependency) |
| Latency | Kanban load < 2s, drag-drop < 500ms | Whisper → AI < 10s, Takeover/FIRE RED < 30s |
| Concurrent users | 5 staff (pipeline) | 100 conversations without degradation |
| Access control | Role-based: DMC staff only | Role-based: DMC + Jarvisydan staff |
| Audit | Deal stage changes, activity log | Full session reconstruction (DPIA/AI Act) |
| Mobile | PWA with offline (B2B pipeline cached) | PWA online-only (real-time required) |

---

## Implementation Phases

### Phase 1: B2B Kanban + Daily Dashboard (Weeks 1-3)
**Rationale:** B2B is needed NOW — zero pipeline visibility today. Staff has no way to see deal status without checking email threads manually.

| Week | Deliverable | Hours |
|------|-------------|-------|
| 1 | Database schema (deals, deal_activities, deal_stage_history) + RLS + migrations | 8 |
| 1 | n8n W1: email-to-deal auto-creation pipeline | 16 |
| 1 | Seed deals table from existing 107 client profiles | 4 |
| 2 | Frontend: Kanban board with drag-and-drop | 40 |
| 2 | n8n W2: stage auto-progression rules | 12 |
| 3 | Frontend: Morning dashboard (personalized) | 16 |
| 3 | n8n W3: stale deal alerts (Teams notifications) | 4 |
| 3 | Frontend: Deal detail drawer (activity timeline, client context, editing) | 24 |
| **Total** | | **124h** |

**Day 1 experience:** Staff opens dashboard → sees their deals already populated from email mining → personal morning briefing with 3 priorities → Kanban board with color-coded health scores. Zero data entry required.

**Milestone gate:** Staff sees a populated pipeline with accurate deal data. Morning briefing arrives in Teams at 08:30. Kanban updates in real-time when emails arrive.

### Phase 2: Proposal Tracking + AI Activity + PWA (Weeks 4-6)
**Rationale:** Layer on the "wow" features — proposal open notifications, AI-suggested actions, mobile access.

| Week | Deliverable | Hours |
|------|-------------|-------|
| 4 | Proposal tracking: SharePoint sharing links + Graph API analytics | 12 |
| 4 | n8n W4: proposal view webhook + notifications | 8 |
| 4 | Frontend: Activity logger (quick-add calls, notes) | 8 |
| 5 | AI activity suggestions: Sonnet generates next-action per deal | 16 |
| 5 | One-click approve/edit/dismiss for AI suggestions | 8 |
| 5 | M365 Graph API calendar integration (meetings → deal activities) | 12 |
| 6 | PWA shell: service worker, offline cache (B2B pipeline), push notifications | 16 |
| 6 | Mobile-optimized views: swipeable Kanban, morning dashboard | 12 |
| 6 | Testing + polish (B2B complete) | 16 |
| **Total** | | **108h** |

**Milestone gate:** "Client opened your proposal at 14:32" notification works. AI suggestions appear with one-click approval. PWA installs to home screen with offline pipeline view.

### Phase 3: B2C Traffic Light + Whisper + Takeover + FIRE RED (Weeks 7-10)
**Rationale:** Required before Jarvisydan B2C go-live (BP_11). B2C cannot launch without the human safety net.

| Week | Deliverable | Hours |
|------|-------------|-------|
| 7 | B2C tab shell + Azure Event Grid subscription + Cosmos DB read | 16 |
| 7 | Traffic Light dashboard (conversation list, color coding, filters) | 24 |
| 8 | Whisper Mode (private hint → AI incorporation → audit log) | 24 |
| 8 | Takeover Mode (one-click handoff, conversation history, AI resume) | 20 |
| 9 | FIRE RED escalation (auto-triggers, multi-channel notification) | 16 |
| 9 | Queue and notification system (browser alerts, mobile push) | 12 |
| 10 | Role-based access verification (DMC vs Jarvisydan views) | 8 |
| 10 | Load testing: 100 concurrent conversations | 12 |
| 10 | DPIA/AI Act audit log verification | 8 |
| 10 | Integration testing (B2B + B2C tabs together) | 16 |
| **Total** | | **156h** |

**Milestone gate:** All four B2C components functional (Traffic Light + Whisper + Takeover + FIRE RED). 100 concurrent conversations handled. Audit logs reconstruct full sessions. Go-live gate satisfied per Goal Document Section 7.

### Total Development Estimate

| Phase | Hours | Weeks (1 dev) |
|-------|-------|---------------|
| Phase 1: B2B Kanban + Dashboard | 124 | 3.1 |
| Phase 2: Proposal Tracking + AI + PWA | 108 | 2.7 |
| Phase 3: B2C Monitoring | 156 | 3.9 |
| **Total** | **388** | **~10 weeks** |

**Budget estimate:** 388h x €80/h = **€31,040** (one developer, full-time).

Compared to v1.0 (B2C-only, €8k-€14k for 6-8 weeks): v2.0 adds the complete B2B pipeline layer. The B2B portion is 232h / €18,560 — close to the Technical Architect's 172h estimate plus PWA and polish.

---

## Monthly Running Cost (incremental, after build)

| Service | Current | B2B Added | B2C Added | New Total |
|---------|---------|-----------|-----------|-----------|
| Hetzner VPS (n8n + services) | €10-20 | €0 (same VPS) | — | €10-20 |
| Supabase | €0-25 | €0 (3 tables, <1% load) | — | €0-25 |
| Claude API (Haiku classification + Sonnet suggestions) | ~€5 | ~€5 | — | ~€10 |
| Azure (Cosmos DB + Event Grid) | €0 | — | ~€20-40 | ~€20-40 |
| n8n | €0 (self-hosted) | €0 | — | €0 |
| **Monthly increment** | | **~€5** | **~€20-40** | **~€25-45** |

---

## Acceptance Criteria

### B2B Pipeline (Phases 1-2)

- [ ] Kanban board displays all active deals with correct stage positioning
- [ ] Drag-and-drop moves deals between stages with < 500ms latency
- [ ] Stage changes logged to `deal_stage_history` with timestamp, actor, and reason (for backward moves)
- [ ] New inquiry emails auto-create deals within 5 minutes of arrival
- [ ] Morning dashboard shows personalized 3-priority list per staff member
- [ ] Morning Teams notification arrives by 08:30 Helsinki time
- [ ] Stale deal alerts: green < 7d, yellow 7-14d, red > 14d — colors match on cards and in alerts
- [ ] Proposal tracking: "client opened at [time]" notification delivered within 4 hours of view
- [ ] AI activity suggestions generate relevant next-actions with one-click approve
- [ ] Medium-confidence stage transitions create pending notification (not auto-move)
- [ ] PWA installs to home screen on iOS Safari and Chrome Android
- [ ] Offline mode: B2B pipeline viewable without connectivity (cached data)
- [ ] Deal cards display: client name, value, pax, health color, days in stage, owner, next action
- [ ] Filters work: by staff owner, season, value range, client tier
- [ ] Real-time updates: deal changes by one staff member visible to others within 2 seconds

### B2C Monitoring (Phase 3)

- [ ] Handles 100 concurrent conversations with < 5% false escalations in load test
- [ ] Whisper → AI response confirmed in < 10s across 20 test conversations
- [ ] Takeover + FIRE RED trigger confirmed in < 30s
- [ ] DPIA/AI Act auditors can reconstruct full session from audit logs
- [ ] Role-based access verified: DMC staff sees B2B + B2C; Jarvisydan staff sees B2C only
- [ ] Mobile view tested on iOS Safari and Chrome Android
- [ ] FIRE RED auto-escalation triggers fire correctly for: profanity, health keywords, >5min silence, human request
- [ ] Notification channels confirmed: in-app + email for Yellow/Red/FIRE RED

### Shared

- [ ] Azure AD B2C authentication works for both tabs
- [ ] Tab switching is instant (no full page reload)
- [ ] Role-based tab visibility enforced server-side (not just UI hiding)
- [ ] Push notifications work on PWA (both B2B and B2C alert types)
- [ ] Full audit trail for all user actions across both tabs

---

## Out of Scope (Future Phases)

- God Mode (full conversation injection, analytics control)
- Whisper analytics (what hints work best)
- Advanced B2B reporting (win rates, revenue forecasting, pipeline velocity)
- Multi-resort aggregate views
- Commission and supplier management (Phase 5 operations layer)
- TravelTree deep integration (beyond proposal link tracking)
- B2C push notifications (email sufficient for MVP; push is Phase 3+ enhancement)

---

## Risk Register

| Risk | Impact | Mitigation |
|------|--------|------------|
| B2B adoption: staff ignores Kanban | Medium | Zero-entry design = system works without staff. Morning briefing pulls them in. Month 3 checkpoint: if < 2/5 staff use daily → pivot to Moonstride. |
| B2C latency: Whisper > 10s at scale | High | Load test at 100 conversations in Phase 3 week 10. Azure Event Grid scales horizontally. |
| Two-zone complexity: debugging across Supabase + Cosmos DB | Medium | Clean tab separation — B2B never touches Cosmos DB, B2C never touches Supabase. No cross-zone queries. |
| PWA offline sync conflicts (B2B) | Low | Offline is read-only. Write actions queue and sync with last-write-wins. 5 users = minimal conflict risk. |
| Scope creep: B2B features expand before B2C ships | High | Phase gates enforced. B2C must ship before Jarvisydan go-live. No Phase 2 feature additions after week 4. |

---

## Key Files Reference

| File | Contents |
|------|----------|
| CRM-DECISION-SYNTHESIS.md | CRM research — why custom wins, team pitch, 6-week plan |
| AGENT-1-UX-ADOPTION.md | UX blueprint — emotional hooks, morning dashboard mockup, deal card design |
| AGENT-2-TECHNICAL-ARCHITECT.md | Technical architecture — database schema, n8n workflows, TCO analysis |
| bp08-mvp-scope.md | Original B2C-only scope (v1.0) — preserved in full as Tab 2 |

---

*BP_08 Staff Dashboard v2.0 | 2026-03-10 | Dual-mode: B2B pipeline + B2C monitoring | Supersedes bp08-mvp-scope.md*
