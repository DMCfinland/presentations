# BP_08 Staff Dashboard — MVP Scope Document
**Status:** Corrected — Whisper + Takeover added back (were missing from Grok draft; required by Goal Document Section 7)
**Date:** 2026-02-22
**Use:** Send to developers for fixed-price or T&M quotes

---

## Project Overview

**Product:** Staff Dashboard MVP (BP_08) — Go-live Safety Net
**Owner:** Patrick Heiskanen
**Timeline:** 6–8 weeks (start after Phase 0 complete, ~10 March 2026)
**Budget target:** €8k–€14k (one focused developer + review cycles)
**Dependency:** BP_08 must be functional before B2C Järvisydän go-live (BP_11)

---

## Why This Exists

The Finland Travel Assistant (B2C) deploys AI to handle guest conversations autonomously. Staff Dashboard is the human safety net that makes autonomous AI deployable: staff can monitor, hint, take over, or escalate in real time. Without it, the 80/20 AI-human split required for the transition model does not exist.

Per Goal Document Section 7 go-live gates:
> "BP_08 Staff Dashboard functional (Traffic Light + Whisper + Takeover + FIRE RED minimum)"

All four components are required minimum for go-live. None are deferrable.

---

## Core Requirements (MVP)

### 1. Traffic Light Dashboard (real-time)
- Live list of active Travel Assistant conversations (Cosmos DB queue).
- Color coding: **Green** (normal), **Yellow** (needs review), **Red** (escalated).
- Filters: resort, guest mood score, time since last message.
- Both Finland DMC staff view and Järvisydän staff view (role-based).

### 2. Whisper Mode *(required minimum)*
- Staff sends private hint/suggestion to the AI mid-conversation. Guest does not see it.
- AI incorporates the hint in its next response.
- Full audit log: whisper content, timestamp, AI reaction, staff ID.
- *Why required:* Without Whisper, escalation is binary — watch or full takeover. At scale with 100+ concurrent conversations, binary escalation is operationally disruptive. Whisper allows lightweight guidance without handoff overhead.

### 3. Takeover Mode *(required minimum)*
- One-click full human takeover — staff takes over conversation from AI.
- Seamless handoff; full conversation history visible to staff.
- Auto-notification to Järvisydän reception if needed.
- AI resumes after staff marks conversation resolved.

### 4. FIRE RED Escalation *(required minimum)*
- One-click FIRE RED → immediate human takeover + notification to Järvisydän staff on duty + full audit log entry.
- Auto-escalation triggers (configurable by resort admin):
  - Profanity detected
  - Health/accessibility keywords (Article 9 GDPR risk)
  - >5 minutes no AI response
  - Guest explicitly requests human or booking
- Notification channels: in-app + email (push notification as Phase 3+ enhancement).

### 5. Queue & Notification (supporting)
- Mobile-friendly view (phone priority — staff often away from desk).
- Browser alerts for Yellow/Red items (no sound by default; configurable).
- Full audit log (who saw what, when, what action taken) — required for DPIA and EU AI Act Art 50 documentation.

---

## Non-Functional Requirements

| Requirement | Spec |
|-------------|------|
| Zone | Zone 2 only (Azure Event Grid + Cosmos DB — no Zone 1 data) |
| GDPR | Pseudonymized guest IDs only (no names in dashboard) |
| Uptime | 99.9% |
| Escalation latency | Whisper → AI response <10s; Takeover/FIRE RED trigger <30s |
| Concurrent conversations | Handle 100 without degradation |
| Access control | Role-based: Finland DMC monitors vs. Järvisydän staff |

---

## Out of Scope for MVP (Phase 3+)

- God Mode (full conversation injection, analytics control)
- Whisper analytics (what hints work best)
- Advanced performance dashboards
- Multi-resort aggregate views
- Push notifications (email sufficient for MVP)

---

## Acceptance Criteria

- [ ] Handles 100 concurrent conversations with <5% false escalations in load test
- [ ] Whisper → AI response confirmed in <10s across 20 test conversations
- [ ] Takeover + FIRE RED trigger confirmed in <30s
- [ ] DPIA/AI Act auditors can reconstruct full session from audit logs
- [ ] Role-based access verified (Finland DMC cannot see Järvisydän-only fields and vice versa)
- [ ] Mobile view tested on iOS Safari and Chrome Android

---

## Deliverables Requested in Quote

1. Wireframes (Figma) for all 4 core components
2. Azure deployment plan (Event Grid + Cosmos DB topology)
3. 6–8 week sprint plan (2-week cycles, milestones, handoff points)
4. Fixed-price or time-and-materials quote with breakdown

---

## Architecture Context (for developer)

- **Zone 2:** Azure North Europe
- **Event backbone:** Azure Event Grid (guest conversation events)
- **Data store:** Cosmos DB (conversation history, audit log)
- **Auth:** Azure AD B2C (staff login, role-based)
- **Frontend:** Web app (Next.js preferred — consistent with existing FinnConcierge codebase at Desktop/FinnConcierge/)
- **Integration:** Reads events from Zone 2 only — no direct connection to Zone 1 (Supabase/Hetzner)

---

*BP_08 MVP scope doc | Session 49 | Corrected: added Whisper + Takeover per Goal Document Section 7 minimum | 2026-02-22*
