---
company: Finland DMC Oy
warm_pack_id: strategic-research
last_updated: 2026-03-12
---

# Finland DMC Oy — Context Card

Load this at session START before any external source mining.
It overrides generic assumptions from external articles, tutorials, and community posts.

---

## Tech Stack (overrides source defaults)

| External default | Finland DMC reality |
|-----------------|---------------------|
| Slack | Microsoft Teams (M365) |
| Google Workspace | Microsoft 365 |
| Zapier | n8n (self-hosted on Hetzner) |
| Firebase | Supabase (Frankfurt EU region) |
| Stripe / generic payments | TravelTree (itinerary + pricing tool) |
| Any email provider | Microsoft Outlook / Exchange (inquiries@finlanddmc.fi) |
| OpenAI GPT | Claude (Sonnet 4.6 default) |

**Flag any recommendation that contradicts this card before applying it.**

---

## Staff (roles relevant for system + adoption context)

| Name | Role | AI adoption profile |
|------|------|---------------------|
| Patrick Heiskanen | CEO, architect, primary AI user | Builds the system |
| Sebastian Heiskanen | FIT / boutique travel | Early adopter — zero-entry pitch |
| Janna Kankkunen | Head of Sales | Pipedrive power user — "why not Pipedrive?" |
| Liisa Vihermaa | Product & Sales Manager | Data-oriented — sees what we have |
| Reeta Vihavainen | Program ops + repeat accounts | Needs approval on every AI action |
| Laura Ilvonen | Group ops + Iceland FIT | TravelTree-heavy user |
| Piia Laitila | Product & Sales Manager | Professionalism focus |

---

## Standing Overrides (common source conflicts)

- **"Memory migration"** = bulk-embedding 107 existing client profiles from mining outputs (not a generic concept)
- **"Staff capture channel"** = Teams `#crm-capture` (not Slack, not a new tool)
- **"CRM"** = custom-built on FinnConcierge (Next.js + Supabase), NOT Pipedrive/Moonstride
- **"Booking reference"** = FDM-[6-char] format (D27), maps to deal_id UUID internally
- **"Auth"** = Staff: Supabase JWT with role claims. Travelers (B2C): magic link 60min + resend button (D25)
- **"Email pipeline"** = Microsoft Graph API Mail.Read on inquiries@finlanddmc.fi → n8n → Supabase Edge Function
- **"AI capture"** = two channels: Teams #crm-capture (staff) + MCP write (Patrick/Sebastian in Claude Code)

---

## Locked Decisions (do not relitigate without a D-number)

- D3: Extend existing Supabase project (not new)
- D8: RLS deny-by-default, ai_reader/ai_writer JWT roles
- D9: DPIA required before live email mining
- D10: Stay n8n (no migration to other automation tools)
- D11: EU Frankfurt region, Supabase DPA signed
- D28: Capture = Teams #crm-capture (not Slack)
- D29: pgvector in Wave 1A (not backlog)
- D31: Header-only auth on all ingest endpoints

Full decisions: `project-files/dmc-secondbrain-crm/DECISIONS.md`

---

## GDPR + Legal Context

- Jurisdiction: Finnish law + EU GDPR
- DPA: Finnish tietosuojavaltuutettu (not a generic EU authority)
- Data residency: Supabase Frankfurt (EU) — requirement for Finnish clients
- DPIA: Required before live email mining starts (Wave 2A gate)
- Soft-delete ≠ erasure: physical DELETE via erase_contact_pii() is required for Art. 17

---

## Project Context (active 2026-03-12)

- **CRM build:** DMC-SECONDBRAIN-CRM, Wave 0 not yet started (Patrick doing manually)
- **Status:** CONDITIONAL GO from Grok debate. D31–D33 locked. DPIA addendum pending.
- **Next gate:** DPIA addendum → bulk-embed script can run (D30/D33)
- **Key file:** `project-files/dmc-secondbrain-crm/orchestration/HANDOFF-NEXT-WINDOW.md`
