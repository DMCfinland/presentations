# INTAKE — DMC-SECONDBRAIN-CRM

PROJECT_TYPE: I (Product Launch) + J (Strategic Planning)
WAVE_CONFIG: Full ($15–25)
DATE: 2026-03-11

---

## Mission
Build a Second Brain-powered CRM+ERP for Finland DMC Oy that auto-mines 4 years of M365 emails into structured client intelligence, delivers Pipedrive-quality UI, integrates TravelTree (never replaces it), and achieves near-zero manual data entry — with a phased staff rollout starting Sebastian → Liisa → iterate → Reeta.

---

## Deliverables Required

1. **Vibe Demo** — Static HTML, hardcoded data, Pipedrive-quality Kanban UI. Ready for Sebastian+Liisa intro within 2 weeks. Purpose: stop Pipedrive pressure by showing something better already exists.
2. **Technical PRD** — Full product requirements: 14-table Supabase schema, TT API (T1+T2) integration, M365 Graph API email mining, n8n workflows, security spec (prompt injection defense, RLS, GDPR), eval framework per feature.
3. **Sprint Plan** — Day-by-day/week-by-week: demo Day 1 (tomorrow), staff intro Week 2, 6-week MVP, with premade eval criteria per feature and context rot mitigation strategy.
4. **Agent Spawn Prompts** — Complete wave architecture for orchestrated Claude Code build. Each agent has correctness criteria, file ownership, constitutional principles, token budget.
5. **Adoption Playbook** — Per-person pitches (Sebastian/Liisa/Reeta), stress-aware onboarding script, explicit "nothing goes to clients without your approval" guarantee documentation.

---

## Success Definition

- **Win condition:** Sebastian + Liisa use system daily within 2 weeks. Reeta adopts after first iteration. Pipedrive conversation ends.
- **Quality criteria:**
  1. Zero hallucinations in client data — every displayed fact traceable to source email/proposal
  2. Prompt injection defense — no inbound email content can alter agent behavior or data state
  3. Staff adoption — all 3 pilot users complete first real workflow without Patrick's help
- **Risk tolerance:** Low — production system, real client data, security is a hard constraint

---

## Target Audiences

2 audiences:
- **Patrick (builder)** — complete technical spec, agent spawn prompts, security requirements
- **DMC staff (Sebastian, Liisa, Reeta)** — UI that feels easy, safe, and Pipedrive-quality on first use

---

## Forbidden Words / Anti-Patterns

- "Replaces TravelTree" — existential threat to staff comfort (TT stays; future replacement is an option, not a plan)
- "AI decides" / "automated sending" — control anxiety (staff always in control)
- "Migration" / "import" — sounds like data loss risk
- "Beta" / "prototype" — undermines trust; call it "your system"
- "Manual data entry required" — the very problem being solved
- **Build anti-pattern:** Mock/hardcoded data presented as real in non-demo contexts (Red Team hunts this)
- **Build anti-pattern:** Agent builds something that looks good but doesn't function under real usage

---

## Red Team Configuration

**Main risks:**
1. Staff non-adoption — Reeta highest bar, will spot friction; Liisa needs visible data wins; Sebastian is easiest
2. Build context rot — multi-session, multi-agent coherence degrades; system becomes unreliable
3. Prompt injection via Outlook — inbound client emails as attack vector into AI chain
4. AHI Travel data quality — 75% revenue concentration, wrong data = serious business risk
5. Vibe-coded trap — system looks good in demo, breaks under real usage or can't be improved

**Key critic personas:**
- **Reeta** (high UX bar, first AI tool at work, will not adopt if interface is confusing or feels unsafe)
- **Janna Kankkunen** (Head of Sales, knows CRM deeply — "why isn't this Pipedrive?")
- **Stressed staff member** (first AI tool, "what if it sends something wrong to a client?")
- **Security red team** (prompt injection hunter — tests every API endpoint and inbound data path)

---

## Source Documents

All in `~/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/`:
- `project-files/dmc-2.0-strategic-synthesis/SECOND-BRAIN-ERP-CRM-v2.md` — 19-section spec, 14-table schema
- `project-files/dmc-2.0-strategic-synthesis/BP08-STAFF-DASHBOARD-v2.md` — dual B2B+B2C dashboard design
- `project-files/dmc-2.0-strategic-synthesis/IMPLEMENTATION-ROADMAP-6W.md` — 6-week week-by-week plan
- `project-files/dmc-2.0-strategic-synthesis/CRM-DECISION-SYNTHESIS.md` — build-vs-buy decision rationale
- `finland-dmc-2.0/mining-outputs/proposals-2024/SECOND-BRAIN/` — 107 client profiles, 393 proposals (seed data)
- FinnConcierge codebase (Next.js, existing 9-table Supabase schema) — on Patrick's Desktop
- Small email mining samples (partial, Sessions 1–3+5 done)

---

## Web Research Needed

Yes — search before build starts:
1. Monday.com AI-orchestrated 2-week build (reference for quality bar + team structure)
2. Multi-agent context rot prevention in long-running builds (2025 best practices)
3. Claude Code multi-session context management strategies
4. Supabase Row Level Security for multi-tenant AI agent systems
5. Prompt injection defense patterns for RAG + email ingestion pipelines
6. Next.js + Supabase Kanban CRM architecture patterns (component library, state management)

---

## Constraints

- **GDPR:** 4 years client email data → data minimization; anonymize before AI processing where possible
- **No client-facing actions without staff approval** — hard requirement, non-negotiable, built into every agent's constitutional principles
- **Prompt injection:** All inbound email content treated as untrusted — no direct execution, sanitized before any AI processing
- **Agent boundaries:** Some agents are read-only; no unplanned agent-to-agent communication; each agent owns its file, no cross-writes
- **Backup:** Indestructible backup strategy — eventually managed behind Frendy IT; versioned Supabase + Git
- **TravelTree:** Integrate (T1+T2 APIs), never replace — architecture must keep TT replacement as a future option without requiring it now
- **Context management:** /compact at convenient phase boundaries during planning AND build — never lose context without first writing state to .md files

---

## Configuration

- **Fact-check level:** High — every architectural claim needs a working reference or documentation link; very low hallucination tolerance
- **Wave config:** Full ($15–25)
- **Deadline:** Demo MVP Day 1 (tomorrow); Staff intro (Sebastian + Liisa) within 2 weeks
- **Human veto:** Yes — Wave 1.5 (architecture quality check) + Wave 2.5 (PRD draft quality check). Agents also ask clarifying questions inside VS Code when uncertain (don't proceed on assumptions).
- **Codename:** DMC-SECONDBRAIN-CRM
