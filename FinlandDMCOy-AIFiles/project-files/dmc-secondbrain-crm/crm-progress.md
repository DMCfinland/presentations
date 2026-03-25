# CRM Progress Tracker — DMC-SECONDBRAIN-CRM
**Companion to:** `crm-spec.json` (immutable spec)
**Mutability:** UPDATE EVERY SESSION — this is the live state file
**Last updated:** 2026-03-12 | **Updated by:** Session 72 (Patrick + Claude Code)

---

## Current State

| Field | Value |
|-------|-------|
| **Active wave** | Wave 0 (pre-build gates — in progress) |
| **Overall status** | BLOCKED — Gate 2 SQL migration constraint collision |
| **Last commit** | `fd6139d` — Wave 1A code committed |
| **DPIA status** | NOT SIGNED — required before Wave 2A |
| **BUILD-STATE.md** | DOES NOT EXIST (created by Wave 0) |

---

## Gate Status

| Gate | Description | Status | Blocker |
|------|-------------|--------|---------|
| Gate 1 | Wave 1A code committed to repo | ✅ DONE | — |
| Gate 2 | 3 SQL migrations applied to Supabase | 🔄 IN PROGRESS | `20260312000000_crm_v2.sql` constraint-already-exists error on `interactions.fk_interactions_deal` — partial prior application suspected. Need to verify which tables exist before reapplying. |
| Gate 3 | DPIA addendum signed by Patrick | ❌ NOT STARTED | Patrick signature required |
| Gate 4 | Azure Graph API Mail.Read token created | ❌ NOT STARTED | — |
| Gate 5 | n8n JWT configured | ❌ NOT STARTED | — |

---

## Wave 0 — Setup Checklist (Patrick does manually)

- [ ] Create project CLAUDE.md at FinnConcierge repo root
- [ ] **Create BUILD-STATE.md** (this file's current state section depends on it)
- [ ] Copy DECISIONS.md to ~/Desktop/FinnConcierge/DECISIONS.md
- [ ] Git worktrees: `crm-schema-migration`, `crm-vibe-demo` (+ 5 others per WAVE-BUILD-AGENTS.md)
- [ ] Supabase PITR enabled, ai_reader/ai_writer roles created
- [ ] PreCompact hook configured in FinnConcierge project
- [ ] Credentials verified: n8n, TravelTree API, Graph API Mail.Read token
- [ ] **Resolve Gate 2 blocker:** Query Supabase to list existing tables. Determine which migrations partially ran. Re-apply idempotently or run compensating migration.

---

## Wave 1A — Foundation: Schema + Embeddings

| Deliverable | Status | Notes |
|-------------|--------|-------|
| 14 CRM tables in Supabase | ❌ PENDING | Gate 2 blocker — migration not confirmed |
| deal_embeddings table (pgvector vector(1536)) | ❌ PENDING | D29 — Wave 1A scope |
| prompt_versions table | ❌ PENDING | D36 — email drafter loop (addendum migration `20260312000001_email_drafter_loop.sql`) |
| email_draft_sessions table | ❌ PENDING | D36 |
| email_draft_iterations table | ❌ PENDING | D36 |
| prompt_evaluations table | ❌ PENDING | D36 |
| RLS deny-by-default policies | ❌ PENDING | D8 |
| ai_reader / ai_writer roles | ❌ PENDING | D8 — created in Wave 0 gates |
| Bulk-embed 107 profiles | ❌ BLOCKED | D30 — DRY_RUN=true first, then false. **DPIA must be signed first (Gate 3)** |
| bulk-embed-107-profiles.ts script | ✅ EXISTS | Already written — awaiting DPIA + DB ready |
| Booking reference FDM-[6-char] server-side | ❌ PENDING | D27 |

---

## Wave 1B — Kanban UI (parallel with 1A)

| Deliverable | Status | Notes |
|-------------|--------|-------|
| Kanban board renders with mock deals | ❌ PENDING | |
| @dnd-kit/sortable drag-and-drop | ❌ PENDING | D4 / D26 ($8 ceiling) |
| Supabase Realtime card update | ❌ PENDING | |
| Mobile PWA tap-to-move | ❌ PENDING | |
| Staff filters (owner, stage, client) | ❌ PENDING | |

---

## Wave 2A — Email Pipeline

| Deliverable | Status | Notes |
|-------------|--------|-------|
| n8n email ingestion workflow | ❌ BLOCKED | DPIA must be signed first (D9) |
| Triple-LLM pipeline (Quarantine→Validator→Privileged) | ❌ BLOCKED | D7 |
| Teams notification on new deal | ❌ PENDING | D28 |
| Graph API Mail.Read token | ❌ BLOCKED | Gate 4 not done |
| Deals auto-created status: unverified | ❌ PENDING | |
| Webhook header-only auth (x-brain-key) | ❌ PENDING | D31 |
| Rate limiting on all ingest endpoints | ❌ PENDING | D31 |

---

## Wave 2B — Teams Transcripts

| Deliverable | Status | Notes |
|-------------|--------|-------|
| Graph API OnlineMeetings.Read.All consent | ❌ PENDING | Requires Azure admin consent |
| Teams transcript daily digest n8n workflow | ❌ PENDING | |
| Deal activities populated from transcripts | ❌ PENDING | DPIA Section 4 LIA checkboxes — Patrick to sign |

---

## Wave 3A — UI Production

| Deliverable | Status | Notes |
|-------------|--------|-------|
| Search across deals | ❌ PENDING | |
| Mobile PWA installable | ❌ PENDING | |
| Performance: <200ms Kanban load | ❌ PENDING | |
| $8 dependency budget respected | ❌ PENDING | D26 |

---

## Wave 3B — TravelTree Integration

| Deliverable | Status | Notes |
|-------------|--------|-------|
| Create itinerary from deal card (T1 API) | ❌ PENDING | D6 |
| Read itinerary status (T2 API) | ❌ PENDING | |
| New window (not iframe) | ❌ PENDING | D6 |

---

## Wave 4A — Intelligence Layer

| Deliverable | Status | Notes |
|-------------|--------|-------|
| Vector similarity search (top-5 similar deals) | ❌ PENDING | D29 |
| Semantic search UI in Kanban | ❌ PENDING | |
| 107 profiles embedded + searchable | ❌ BLOCKED | DPIA first |

---

## Wave 4B — Email Drafter

| Deliverable | Status | Notes |
|-------------|--------|-------|
| Email drafter UI (tone select + generate + approve) | ❌ PENDING | D36–D38 |
| R auto-capture via n8n on send event | ❌ PENDING | D37 |
| Prompt competition jury visible | ❌ PENDING | D38 |
| DPIA transcript section (Azure OnlineMeetings.Read.All) | ❌ BLOCKED | Patrick action |

---

## Wave 5 — QA + Security + Staff Onboarding

| Deliverable | Status | Notes |
|-------------|--------|-------|
| Security audit: no service_role in codebase | ❌ PENDING | |
| RLS verification | ❌ PENDING | |
| Webhook auth confirmed | ❌ PENDING | |
| DPIA complete + filed | ❌ PENDING | |
| Sebastian onboarding | ❌ PENDING | First adopter |
| Liisa onboarding | ❌ PENDING | Second adopter |

---

## Known Constraints Discovered During Build

| ID | Constraint | Discovered | Impact |
|----|-----------|------------|--------|
| KC1 | `20260312000000_crm_v2.sql` partially applied — constraint `interactions.fk_interactions_deal` already exists | 2026-03-12 | Gate 2 blocked — must verify table state before reapplying |
| KC2 | DPIA Section 4 LIA checkboxes unchecked | 2026-03-12 | Wave 2A + Wave 2B blocked |
| KC3 | BUILD-STATE.md does not exist | 2026-03-12 | Wave 0 incomplete — progress tracking partially blind |
| KC4 | D34/D35 numbering gap | 2026-03-12 | Not a blocker — just a documentation note |

---

## Rejection Summaries

*(Add here when a wave agent's output is rejected by the Judge. Format: wave | round | rejection reason | what was fixed)*

| Wave | Round | Reason | Fixed by |
|------|-------|--------|----------|
| — | — | No rejections yet — build not started | — |

---

## Session Log (append — newest at top)

### 2026-03-12 — Session 72
- Initializer files created: `crm-spec.json` + `crm-progress.md`
- Build status confirmed via other window: Wave 0 not started, Gate 2 blocked
- Hooks built this session: `session-end-check.sh` + `yaml-validator.sh` (Stop + PostToolUse)
- No wave work done — pre-build gate setup still in progress
- **Patrick action needed:** Resolve KC1 (verify Supabase table state), sign DPIA (Gate 3), create Graph API token (Gate 4)

---

## How to Use This File

**Session start:**
1. Read this file (current state + active blockers)
2. Read `crm-spec.json` (acceptance criteria for the wave you're on)
3. Read `BUILD-STATE.md` (once Wave 0 creates it)

**Session end:**
1. Update gate statuses above
2. Check off wave deliverables as done
3. Add any new KC (Known Constraints) discovered
4. Add rejection summary if any agent output was rejected
5. Append session log entry (newest at top)
