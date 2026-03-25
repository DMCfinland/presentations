# SHARED CONTEXT — DMC-SECONDBRAIN-CRM Build
**Version:** 1.0 | **Date:** 2026-03-11 | **Status:** APPROVED — Build authorized

> This file is the single source of truth for all build agents. Every agent reads this first.
> Do NOT begin work without reading this. Do NOT override any LOCKED DECISION.

---

## Mission

Build a Second Brain-powered CRM+ERP for Finland DMC Oy that:
- Auto-mines 4 years of M365 emails into structured client intelligence
- Delivers Pipedrive-quality Kanban UI
- Integrates TravelTree API (T1+T2) — never replaces it
- Achieves near-zero manual data entry
- Is safe for real client data from day one

**Codename:** DMC-SECONDBRAIN-CRM
**Owner:** Patrick Heiskanen (CEO, builder)
**Timeline:** Demo Day 1 | Staff intro Week 2 | MVP Week 8

---

## Company Context

**Finland DMC Oy** — boutique Scandinavian DMC, 6 staff, Helsinki
- 107 active client companies, 393 proposals/year, €5.87M revenue
- AHI Travel = 75% revenue concentration (CRITICAL account)
- Staff: Liisa, Laura, Reeta, Sebastian, Piia, Janna
- Phased rollout: Sebastian → Liisa → iterate → Reeta (highest UX bar)

**Existing assets to use (not rebuild):**
- FinnConcierge codebase: Next.js, on Patrick's Desktop
- Supabase: NEW project (https://fjfztbdcjoptkwbzwoub.supabase.co). Fresh empty DB. Agent 1A creates all 14 CRM tables from scratch. The 9 Azure SQL tables (FinnConcierge) are separate — do NOT touch them
- n8n: self-hosted on Hetzner, 8 existing workflows
- TravelTree: Pro plan, T1+T2 APIs available NOW
- Seed data: 107 client profiles in `FinlandDMCOy-AIFiles/finland-dmc-2.0/mining-outputs/proposals-2024/SECOND-BRAIN/`

---

## LOCKED DECISIONS (do not relitigate — see DECISIONS.md for rationale)

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Build custom (not Pipedrive, not Moonstride) | CRM Decision Synthesis, session 58, unanimous |
| D2 | Next.js App Router + shadcn/ui + Tailwind CSS v4 | Existing FinnConcierge codebase |
| D3 | New Supabase project (created 2026-03-12) + PITR backup | FinnConcierge uses Azure SQL — CRM gets fresh Supabase. URL: https://fjfztbdcjoptkwbzwoub.supabase.co (eu-central-1 Frankfurt) |
| D4 | @dnd-kit/sortable + TanStack Query + Zustand | 2025 consensus Kanban stack |
| D5 | n8n self-hosted Hetzner (keep as workflow layer) | Production viable at DMC scale |
| D6 | TravelTree: integrate T1+T2, never replace | Staff trust; replacement kept as future option |
| D7 | Triple-LLM email pipeline | Quarantined → Validator → Privileged |
| D8 | Supabase RLS deny-by-default | ai_reader/ai_writer roles, no service_role in agents |
| D9 | DPIA required before live email mining | Finnish DPA Art. 35(3)(c), mandatory |
| D10 | n8n → code migration deferred | Stay n8n until >50K executions/month |
| D11 | EU region: Frankfurt (eu-central-1) | GDPR data residency |
| D12 | FinnConcierge: extend not rewrite | 7/11 BPs functional, don't break what works |

---

## Architecture Overview

```
[M365 Outlook - inquiries@]
         ↓ Graph API Mail.Read (single mailbox)
[n8n: Email Ingestion Workflow]
  L1: Plain text extract + Unicode normalize + HTML strip
  L2: QUARANTINED Claude (no tools) → structured JSON
  L3: VALIDATOR Claude (schema check + instruction-bleed detection)
  L4: Supabase upsert (deals + deal_activities) status: unverified
  L5: Teams notification to assigned staff
         ↓
[Supabase PostgreSQL - eu-central-1]
  14 tables (extending existing 9)
  RLS: ai_reader/ai_writer roles (JWT auth, not service_role)
  PITR backup enabled (Pro plan)
  Weekly pg_dump → external vendor (S3 Object Lock)
         ↓
[Next.js App Router + shadcn/ui]
  Kanban: @dnd-kit/sortable + fractional indexing
  Realtime: Supabase WAL → TanStack Query invalidation
  Mobile: Serwist PWA + tap-to-move stage selector
         ↓
[TravelTree API - T1+T2]
  Create + Read itinerary (free, available NOW)
  New window + API (not iframe)
         ↓
[M365 Teams Meeting Transcripts]
  Daily: Graph API → Claude extract → deal_activities
  (Requires Teams transcription enabled at tenant level)
```

---

## Security Requirements (Non-Negotiable)

1. **No service_role key in any agent or n8n workflow** — JWT auth only
2. **ai_reader/ai_writer roles have no DELETE policy** — deny-by-default enforced
3. **Triple-LLM pipeline** — no raw email text reaches the privileged write context
4. **Graph API scope: Mail.Read only, scoped to single mailbox** — not all-mailbox
5. **No send-email capability in ingestion agent** — ever
6. **All AI-enriched records: status: unverified** until human staff touches them
7. **DPIA completed and documented** before ANY live email mining begins
8. **Audit log** on every agent action with email message_id as correlation key

---

## Forbidden Words (in all client-facing and staff-facing UI copy)

- "Replaces TravelTree" — say "works alongside TravelTree"
- "AI decides" / "automated sending" — say "suggested for your review"
- "Migration" / "import" — say "your history, now searchable"
- "Beta" / "prototype" — say "your system"
- "Manual data entry required" — this is the problem being solved, not a feature

---

## Staff Profiles (for UI/UX agents)

| Staff | Adoption bar | What wins them | Risk |
|-------|-------------|----------------|------|
| Sebastian | LOW — easiest | Zero-entry, fast | None |
| Liisa | MEDIUM | Data wins, pipeline visibility | Will compare to Pipedrive |
| Laura | MEDIUM | Completeness, operations | Integration with existing ops |
| Reeta | HIGH — hardest | Must feel safe, simple | First AI tool at work, will not adopt if confusing |
| Piia | MEDIUM | Professional quality | |
| Janna | HIGH (Head of Sales) | "Why isn't this Pipedrive?" | Knows CRM deeply |

**Adoption sequence:** Sebastian → Liisa → iterate → Reeta
**Staff must always be in control.** No client-facing action without explicit approval.

---

## Source Documents for Wave 1 Agents

All in `~/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/`:
- `project-files/dmc-2.0-strategic-synthesis/SECOND-BRAIN-ERP-CRM-v2.md` — 19-section spec, 14-table schema
- `project-files/dmc-2.0-strategic-synthesis/BP08-STAFF-DASHBOARD-v2.md` — dual B2B+B2C dashboard
- `project-files/dmc-2.0-strategic-synthesis/IMPLEMENTATION-ROADMAP-6W.md` — week-by-week plan
- `project-files/dmc-2.0-strategic-synthesis/CRM-DECISION-SYNTHESIS.md` — build-vs-buy rationale
- `finland-dmc-2.0/mining-outputs/proposals-2024/SECOND-BRAIN/` — 107 client profiles
- `project-files/dmc-secondbrain-crm/INTAKE.md` — project intake
- `project-files/dmc-secondbrain-crm/GROK-VALIDATION.md` — Grok architecture validation
- `project-files/dmc-secondbrain-crm/orchestration/QUALITY-GATES.md` — acceptance criteria

---

## Build State Files (update every session)

| File | Purpose | Update frequency |
|------|---------|-----------------|
| `BUILD-STATE.md` | Dynamic current state | Every session end |
| `DECISIONS.md` | Append-only architectural log | When any arch decision made |
| `CLAUDE.md` (project root) | Static rules + conventions | Rarely — only when rule changes |

**Weekly coherence sync:** Every Monday, CEO reads BUILD-STATE.md + DECISIONS.md fresh before spawning any agents.
