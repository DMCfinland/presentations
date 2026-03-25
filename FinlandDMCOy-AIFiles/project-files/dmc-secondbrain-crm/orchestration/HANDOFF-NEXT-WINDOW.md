# Handoff — DMC-SECONDBRAIN-CRM
**From:** Session 63 (this window — long context, multiple compacts)
**To:** Fresh window
**Date:** 2026-03-11
**Purpose:** Continue from here. Do NOT re-read the long session. Everything you need is in this file + the files listed below.

---

## What Was Done This Session

### Files created/updated:
1. `DECISIONS.md` — D27–D30 appended + staff adoption pitches (locked verbatim)
2. `orchestration/WAVE-BUILD-AGENTS.md` — 5 spawn rules, Wave 1A startup sequence (5 files), deliverables expanded to 12 items, known issues section added
3. `research/nate-substack-openbrain-article-mine.md` — Full Nate B Jones article mining
4. `research/nate-substack-comments-addendum.md` — Comments mining (C1–C8 actionable items)

### Decisions locked this session (D27–D30):
- **D27:** Booking reference = `FDM-[6-char alphanumeric]`, server-side, UUID internal only
- **D28:** Capture channel = Teams `#crm-capture` (not Slack). Teams webhook → n8n → Edge Function. MCP write = secondary capture for Patrick/Sebastian in Claude Code.
- **D29:** pgvector in Wave 1A scope. deal_embeddings table with vector(1536).
- **D30:** Memory migration two-phase. Phase 1 = bulk-embed 107 profiles (Day 1). Phase 2 = staff Q&A institutional knowledge.

### NOT yet decided (D31+ candidates):
- Header-only auth + per-client keys for all ingest endpoints (C1)
- `active boolean` soft-delete on deal_embeddings (C5)
- Atomic facts chunking strategy for D30 Phase 1 bulk-embed (C4)

---

## Your Tasks

### Task 1: Add D31–D33 to DECISIONS.md
Read `DECISIONS.md` (end of file). Append three decisions:

**D31: Webhook endpoint security**
- Header-only auth (x-brain-key or Authorization: Bearer — never URL query param)
- Per-service credentials (not shared key): separate key for Teams webhook, n8n, MCP server
- Rate limiting on all ingest endpoints (Supabase Edge Function level or n8n throttle)
- Source: Robert MacNaughton security audit + Pokemon Is Awful (Substack comments, 2026-03-11)

**D32: deal_embeddings soft-delete**
- Add `active boolean default true` column to deal_embeddings schema
- Soft-delete via UPDATE active = false (never DROP rows)
- Hard-delete only via erase_contact_pii() GDPR function
- Source: Chris Maughan + Mark Madsen community pattern (Substack comments, 2026-03-11)

**D33: Atomic facts chunking for bulk-embed**
- D30 Phase 1 bulk-embed: break 107 client profiles into atomic facts before embedding
- Target: 10-20 facts per profile = 1,070–2,140 embedding rows on Day 1
- Each fact = one row in deal_embeddings (not full profile blob)
- Source: Nate B Jones atomic facts recommendation (Substack comments, 2026-03-11)

---

### Task 2: Run the Pre-Build Debate

The original orchestration plan was validated by Grok 4-agent debate BEFORE D25–D30 were added. Those decisions materially change the build scope. Run a new debate round to validate D25–D33 before Wave 1A starts.

**Use this prompt in a fresh Grok window (or Claude.ai with Opus):**

---

```
You are running a 3-round adversarial debate to validate the DMC-SECONDBRAIN-CRM build plan. This plan was previously validated (D1–D24). New decisions D25–D33 have been added. Your job: find flaws before the build starts.

## Project context
Finland DMC Oy — 5-person destination management company. Building a custom CRM on FinnConcierge (Next.js + Supabase) with AI-powered deal intelligence. Budget: €0 (internal build), 8-week MVP target.

## New decisions to debate (D25–D33):

D25: Magic link auth (Supabase email OTP, 15-min expiry, httpOnly cookie)
D26: Wave 3A cost ceiling = $8 (one-time exception — @dnd-kit + TanStack + Kanban)
D27: Booking reference = FDM-[6-char alphanumeric], server-side generated
D28: Capture channel = Teams #crm-capture, Teams webhook → n8n → Supabase Edge Function → pgvector
D29: pgvector in Wave 1A scope — deal_embeddings table vector(1536) from day 1
D30: Memory migration two-phase — bulk-embed 107 client profiles Day 1, staff Q&A Phase 2
D31: Webhook security — header-only auth, per-service keys, rate limiting
D32: deal_embeddings soft-delete — active boolean, hard-delete only via GDPR function
D33: Atomic facts chunking — 10-20 facts per client profile before embedding

## Four debate personas (argue independently, then cross-challenge):

**Persona A — Sebastian Heiskanen (staff, early adopter)**
Attack angle: "What actually ships on Day 1?" Push for the simplest possible first-day experience. Challenge anything that delays the vibe demo or adds complexity to initial onboarding.

**Persona B — Janna Kankkunen (Head of Sales, Pipedrive power user)**
Attack angle: "Pipedrive does this already." Push on feature completeness, workflow disruption, and migration risk. Challenge the Teams capture channel friction vs. existing email habits.

**Persona C — Finnish DPA (data protection authority)**
Attack angle: GDPR compliance gaps. Challenge: Is the DPIA scope sufficient for pgvector embeddings of client data? Does atomic facts chunking constitute automated profiling? Is soft-delete sufficient or does erasure require embedding deletion?

**Persona D — Technical skeptic (Senior engineer)**
Attack angle: "This will break in production." Challenge: Teams webhook latency vs. 3-second retry window (duplicate embeddings). pgvector on Wave 1 before email pipeline = schema with no data. Magic link 15-min expiry = poor UX for mobile users in poor connectivity.

## Debate protocol:
Round 1: Each persona gives their independent assessment (150 words max each).
Round 2: Each persona responds to ONE finding from another persona they most disagree with.
Round 3: Each persona gives final verdict: PROCEED / PROCEED WITH CONDITION / BLOCK + one-line reason.

## Output:
After 3 rounds, give a SUMMARY TABLE:
| Decision | Verdict | Required change (if any) |
|----------|---------|--------------------------|

Then: 3 REQUIRED CHANGES (if any) before Wave 1A starts.
Then: OVERALL VERDICT: GO / CONDITIONAL GO / NO-GO
```

---

### Task 3: Update ORCHESTRATION-PLAN.md with debate results

After the debate:
1. Update ORCHESTRATION-PLAN.md header: `**Version:** 1.1 | **Validated by:** Grok 4.20 debate (D1–D24) + [model] debate (D25–D33, 2026-03-11)`
2. Add any REQUIRED CHANGES as amendments to WAVE-BUILD-AGENTS.md
3. If OVERALL VERDICT = CONDITIONAL GO: add conditions to PRE-SPAWN CHECKLIST

---

## Key Files to Read Before Starting

| File | Purpose |
|------|---------|
| `DECISIONS.md` | All D1–D30 locked decisions |
| `orchestration/WAVE-BUILD-AGENTS.md` | Spawn prompts for all waves |
| `orchestration/ORCHESTRATION-PLAN.md` | Wave architecture + timeline |
| `orchestration/QUALITY-GATES.md` | Constitutional principles + acceptance criteria |
| `research/nate-substack-comments-addendum.md` | C1–C8 findings from community |

**Do NOT read:**
- `research/nate-substack-openbrain-article-mine.md` (large — only if you need architecture reference)
- Any file in `finland-dmc-2.0/mining-outputs/` (mining data — not needed for this task)

---

## Injection Risk Clearance

The Substack comments pasted this session were reviewed for prompt injection. Content was authentic technical discussion (versioning gists, security fixes, Hono route debugging). No "act as X" or "disregard instructions" patterns detected. Safe to use.

---

## Wave 0 Status (Patrick does manually — not yet started)

From WAVE-BUILD-AGENTS.md Wave 0:
- [ ] Create project CLAUDE.md at FinnConcierge repo root
- [ ] Create BUILD-STATE.md
- [ ] Copy DECISIONS.md to ~/Desktop/FinnConcierge/DECISIONS.md
- [ ] Git worktrees: crm-schema-migration, crm-vibe-demo
- [ ] Supabase PITR enabled, ai_reader/ai_writer roles created
- [ ] PreCompact hook configured
- [ ] Credentials verified: n8n, TravelTree API, Graph API Mail.Read token

Patrick starts Wave 0 manually. You (fresh window) run debate + D31–D33 while Wave 0 is being set up.
