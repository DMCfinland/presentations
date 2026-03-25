# FINNCONCIERGE CODEBASE MAP
**Purpose:** Read on startup by Wave 1A, 3B agents — know what exists and what you must NOT break.
**Repo path:** `~/Desktop/FinnConcierge/`
**Type:** Turborepo monorepo — Azure Serverless AI Concierge Platform
**Last updated:** 2026-03-13 (verified against actual codebase)

---

## Repo Structure

```
~/Desktop/FinnConcierge/
├── apps/
│   └── traveler-pwa/          ← Next.js 15 + React 19 (B2C traveler UI)
│       └── src/
│           ├── app/           ← App Router (layout.tsx, page.tsx, /welcome)
│           ├── components/    ← ChatInterface.tsx (only component so far)
│           ├── lib/
│           └── styles/
├── packages/
│   └── shared-types/          ← TypeScript shared types across apps
├── services/
│   └── ingestion/             ← Python AI agents (orchestrator, mood_evaluator,
│                                 chef_agent, librarian_agent, booker_agent)
├── database/
│   ├── sql/schema.sql         ← 480 lines — THE 9 existing tables (see below)
│   └── cosmos/                ← Azure Cosmos NoSQL (session storage, RAG)
├── docs/
│   └── blueprints/            ← 8 BP docs (01-05, 07, 11) — see below
├── infrastructure/            ← Azure deployment config
├── tests/
├── turbo.json                 ← Turborepo config
└── package.json               ← "finnconcierge-monorepo"
```

---

## CRITICAL SEPARATION (D9, D14)

| System | Database | Purpose | CRM agents touch it? |
|--------|----------|---------|----------------------|
| **FinnConcierge** | Azure SQL (9 tables) | B2C traveler concierge | ❌ NEVER |
| **CRM** | Supabase Postgres (14 tables) | B2B deal management | ✅ Yes — your workspace |

---

## The 9 Existing Azure SQL Tables (schema.sql)

**⚠️ These are Azure SQL — NOT Supabase.** CRM build agents must NOT touch them.

| Table | Purpose | Critical constraint |
|-------|---------|---------------------|
| `Tenants` | Multi-tenant config | Soft-delete via is_active |
| `Users` | B2C traveler profiles + Mood Matrix | PII hashed (email_hash, phone_hash) — never store raw |
| `Providers` | Service providers (hotels, activities) | FK → Tenants |
| `Contracts` | Commission rules (waterfall pricing) | PRODUCT_SPECIFIC > SEASONAL > PARTNER_DEFAULT |
| `Itinerary` | B2C bookings & reservations | Status: CONFIRMED/PENDING/CANCELLED/COMPLETED |
| `Shadow_Ledger` | Financial audit trail | ⚠️ APPEND-ONLY — never DELETE, never UPDATE amounts |
| `Products` | Service catalog | DECIMAL(10,2) for money, never FLOAT |
| `Sessions_Archive` | Session backup (hot = Cosmos) | Has nullable `deal_id uuid` bridge column (D21) |
| `Alerts` | Staff + system notifications | Severity: LOW/MEDIUM/HIGH/CRITICAL |

**CRM Supabase tables (separate DB, your workspace):**
- Migration files in `supabase/migrations/` — 4 files applied: ai_roles, crm_v2, email_drafter_loop, seed_prompt_versions
- 14 tables: clients, contacts, interactions, deals, deal_activities, deal_stage_history, suppliers, rate_cards, deal_embeddings, staff_captures, workflow_errors, failed_emails, ai_action_log, erasure_audit_log

---

## Blueprint Status (docs/blueprints/)

| BP | File | Status |
|----|------|--------|
| BP_01 | 01_INGESTION.md | Functional |
| BP_02 | 02_MASTER_AGENT.md | Functional |
| BP_03 | 03_MOOD_EVALUATOR.md | Functional |
| BP_04 | 04_CHEF.md | Functional |
| BP_05 | 05_LIBRARIAN.md / 05_RAG_LIBRARIAN.md | Functional |
| BP_07 | 07_SHADOW_LEDGER.md | Functional |
| BP_11 | 11_TRAVELER_UI.md | Functional (B2C only) |
| BP_06 | — | Missing (confirmed session 45) |
| BP_08 | — | Missing — rebuilt as BP08-STAFF-DASHBOARD-v2.md |
| BP_09 | — | Missing (confirmed session 45) |
| BP_10 | — | Missing (confirmed session 45) |

7/11 BPs functional. BP_08 (staff dashboard) rebuilt from scratch in dmc-2.0-strategic-synthesis.

---

## Tech Stack (existing)

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 15.1 + React 19 (App Router) |
| Styling | Tailwind CSS (version TBC — update to v4 for CRM) |
| Database | Supabase PostgreSQL (schema.sql) + Azure Cosmos NoSQL |
| AI Services | Python orchestrator + 5 specialized agents |
| Infrastructure | Azure Serverless |
| Monorepo | Turborepo |

**Note:** shadcn/ui and @dnd-kit/sortable are NOT yet installed — Wave 3A (Kanban Frontend) adds these.

---

## CRM Build Location

The staff CRM will be added as a NEW app in the monorepo:

```
apps/
├── traveler-pwa/     ← existing B2C app (DO NOT MODIFY)
└── crm/              ← NEW — staff Kanban CRM (Wave 3A builds this)
    └── src/
        ├── app/(crm)/pipeline/page.tsx
        ├── components/kanban/
        └── lib/stores/
```

OR extended into traveler-pwa under a route-protected `/crm/` path — Wave 1A agent decides.

---

## Agent Integration Pattern (existing)

From AGENT_INTEGRATION_SUMMARY.md — the existing orchestration flow:
```
User message
  → Context Rehydration
  → Mood Evaluation (BP_03)
  → Intent Analysis
  → Agent Routing (Chef / Librarian / Booker)
  → Response Synthesis
```

CRM email pipeline (Wave 2A) follows the same pattern — Triple-LLM replaces the Python orchestrator for the staff-facing ingestion workflow.

---

## Key File Paths for Build Agents

| What | Where |
|------|-------|
| SQL schema (9 tables) | `~/Desktop/FinnConcierge/database/sql/schema.sql` |
| CRM migration target | `~/Desktop/FinnConcierge/database/sql/migrations/[timestamp]_crm_v2.sql` |
| Next.js app | `~/Desktop/FinnConcierge/apps/traveler-pwa/` |
| BP docs | `~/Desktop/FinnConcierge/docs/blueprints/` |
| CRM orchestration docs | `~/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/project-files/dmc-secondbrain-crm/orchestration/` |
| BUILD-STATE.md (create here) | `~/Desktop/FinnConcierge/BUILD-STATE.md` |
| DECISIONS.md (create here) | `~/Desktop/FinnConcierge/DECISIONS.md` |
| CLAUDE.md (create here) | `~/Desktop/FinnConcierge/CLAUDE.md` |

---

## What Build Agents MUST NOT Touch

- `apps/traveler-pwa/` — B2C app, do not modify
- `services/ingestion/` — mood_evaluator, chef_agent, librarian_agent, orchestrator (D14: CRM does NOT reuse these)
- `database/sql/schema.sql` — 9 Azure SQL tables, read-only reference
- `database/cosmos/` — Azure Cosmos config
- Any of the 9 existing Azure SQL tables — extend only, no drops, no renames

## What Build Agents MAY Add

- `supabase/migrations/` — new migration files (ADD only, never modify existing)
- `packages/ui/` — shared components per D23 (BaseCard, StageBadge, ValuePill, ActivityTimeline)
- `apps/crm/` — new staff CRM app (Wave 3A)
