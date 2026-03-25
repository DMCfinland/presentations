# ORCHESTRATION PLAN — DMC-SECONDBRAIN-CRM
**Version:** 1.1 | **Date:** 2026-03-12 | **Validated by:** Grok 4.20 4-agent debate (D1–D24, 2026-03-11) + Grok 4 Heavy 4-agent debate (D25–D33, CONDITIONAL GO, 2026-03-12)

---

## Summary

| Field | Value |
|-------|-------|
| **Codename** | DMC-SECONDBRAIN-CRM |
| **Type** | Product Launch (I) + Strategic Planning (J) |
| **Wave config** | Full (5 waves, ~$15-25) |
| **Timeline** | Day 1: Demo | Week 2: Staff intro | Week 8: MVP |
| **Human hours** | 60-80h architect + review (CEO) |
| **Build hours** | ~204h agent execution |
| **Primary builder** | Patrick Heiskanen (CEO) + Claude Code agent teams |
| **Grok verdict (D1–D24)** | "Viable and exciting. Smart, defensible 8-week win." |
| **Grok verdict (D25–D33)** | CONDITIONAL GO — Wave 1A starts immediately after 30-min schema update. DPIA addendum + bulk-embed script required before memory population (post-Wave 1A). |

---

## Build Wave Architecture

```
WAVE 0 — SETUP (Human: 4-6h)
├── Create project CLAUDE.md + BUILD-STATE.md + DECISIONS.md
├── Git worktree structure (one per module)
├── Supabase: enable PITR, create ai_reader/ai_writer roles
├── Configure PreCompact hook → writes BUILD-STATE.md before compression
└── Verify: n8n accessible, TravelTree API keys, Graph API Mail.Read token

WAVE 1 — FOUNDATION (Parallel, 2 agents)
├── Agent 1A: SCHEMA MIGRATOR [git worktree: schema-migration]
│   └── Extend 9→14 tables, RLS policies, indexes, GDPR retention jobs
└── Agent 1B: VIBE DEMO BUILDER [git worktree: vibe-demo]
    └── Static HTML, hardcoded data, Pipedrive-quality Kanban
    └── GATE: Sebastian + Liisa must react positively (Week 2 intro)

WAVE 2 — EMAIL PIPELINE (Sequential, 2 agents)
├── Agent 2A: N8N WORKFLOW BUILDER [after Wave 1A merged]
│   └── Triple-LLM email ingestion: Outlook → Quarantined → Validator → Privileged → Supabase
└── Agent 2B: DEAL PARSER [parallel with 2A]
    └── JSON schema, field validation, instruction-bleed detection, audit log

WAVE 3 — UI/KANBAN (Parallel, 2 agents)
├── Agent 3A: KANBAN FRONTEND [git worktree: kanban-ui]
│   └── Next.js + shadcn/ui + @dnd-kit + Supabase Realtime + Zustand
└── Agent 3B: API LAYER [git worktree: api-layer]
    └── Deal CRUD endpoints + TravelTree T1+T2 integration

WAVE 4 — INTEGRATION (Sequential, 2 agents)
├── Agent 4A: STAFF DASHBOARD + AUTH [after Wave 3 merged]
│   └── Per-staff views, adoption UX, seed with 2-3 real historical deals
└── Agent 4B: TRANSCRIPT PIPELINE [parallel with 4A, AFTER DPIA]
    └── Teams meeting transcripts → Claude extract → deal_activities

WAVE 5 — QA + SECURITY (Parallel, 3 agents)
├── Agent 5A: RED TEAM [git worktree: security-test]
│   └── Prompt injection attempts, RLS penetration, GDPR compliance check
├── Agent 5B: E2E TESTS [git worktree: e2e-tests]
│   └── Playwright: critical flows (create deal, move stage, email → card)
└── Agent 5C: HUMAN REVIEW [Patrick + 1 staff pilot]
    └── All AI-enriched cards reviewed, status: unverified → verified
```

---

## Timeline

| Week | Milestone | Gate |
|------|-----------|------|
| Day 1 | Static HTML vibe demo | Sebastian shows to Liisa |
| Week 2 | Staff intro (read-only demo) | Positive reaction from Sebastian + Liisa |
| Week 3 | Schema + RLS + n8n pipeline live | Zero data leaks in red team test |
| Week 4 | Kanban UI working with test data | Human review: "feels like Pipedrive" |
| Week 5 | DPIA completed + documented | Before ANY live email mining starts |
| Week 6 | Historical email mining (small batch test) | 90%+ extraction accuracy on 50 emails |
| Week 7 | TravelTree integration + staff dashboard | Reeta can create itinerary from deal card |
| Week 8 | MVP: all staff using daily | Sebastian + Liisa daily usage confirmed |

---

## Cost Estimate

| Phase | Estimated cost |
|-------|---------------|
| Wave 0: Setup | ~$0 |
| Wave 1: Foundation | ~$2-4 |
| Wave 2: Email pipeline | ~$3-5 |
| Wave 3: UI/Kanban | ~$4-6 |
| Wave 4: Integration | ~$3-5 |
| Wave 5: QA + Security | ~$3-5 |
| **Total orchestration** | **~$15-25** |
| Infrastructure (Supabase Pro + n8n Hetzner) | ~€30/month |

---

## Context Rot Prevention Protocol

**Non-negotiable rules (apply every session):**

1. Session START: read `BUILD-STATE.md` + `git log --oneline -20` (not full history)
2. Work ONE module per session
3. Session END: update `BUILD-STATE.md` CURRENT STATE + NEXT SESSION + any arch decision to `DECISIONS.md`
4. Compact BEFORE hitting 50K tokens (set threshold in suggest-compact.sh)
5. Git tags at phase boundaries: `schema-v1`, `rls-complete`, `kanban-v1`, `api-v1`
6. Weekly coherence sync: Monday morning, CEO reads all state files fresh

**Build state files (create in Wave 0):**
- `BUILD-STATE.md` — dynamic state (COMPLETED / CURRENT STATE / NEXT SESSION / DECISIONS LOG)
- `DECISIONS.md` — append-only; format: `[date] DECISION: [what] BECAUSE: [why] REJECTED: [alternatives]`
- `CLAUDE.md` (project root) — static rules: tech stack, naming conventions, forbidden patterns

**PreCompact hook:** Configure in `~/.claude/settings.json` to write current state to `BUILD-STATE.md` before any compression.

---

## Agent Spawn Rules (apply to all wave agents)

Every agent spawn prompt MUST include:
1. "Read SHARED-CONTEXT.md first"
2. "Read BUILD-STATE.md — start from NEXT SESSION section"
3. "Your task (ONE thing only): [specific deliverable]"
4. "Locked decisions (do not relitigate): [D1-D12 from SHARED-CONTEXT.md]"
5. "Write output to: [exact file path]"
6. "End with: update BUILD-STATE.md NEXT SESSION section"
7. "Constitutional principles" block (see QUALITY-GATES.md)
8. "DO NOT: read entire codebase / make undocumented arch decisions / exceed [N] files"

---

## Red Team Personas (for Wave 5 and ongoing reviews)

| Persona | Attack angle | When to invoke |
|---------|-------------|----------------|
| **Reeta** | High UX bar, first AI tool at work, will not adopt if confusing or unsafe | Every UI change |
| **Janna Kankkunen** (Head of Sales) | "Why isn't this Pipedrive?" — knows CRM deeply | Feature completeness review |
| **Stressed staff member** | "What if it sends something wrong to a client?" | Any automation feature |
| **Security red team** | Prompt injection via Outlook, RLS bypass, GDPR gaps | Every email pipeline change |
| **Finnish DPA** | Automated profiling, missing DPIA, no deletion pipeline | Before live email mining |
