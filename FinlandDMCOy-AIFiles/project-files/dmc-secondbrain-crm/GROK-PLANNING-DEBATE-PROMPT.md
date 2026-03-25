# GROK 4.20 — PLANNING DEBATE PROMPT
**Project:** DMC-SECONDBRAIN-CRM
**Purpose:** Two-system integration planning + build sequence validation
**Date:** 2026-03-11
**Usage:** Copy everything below the separator line and paste into Grok 4.20 (DeepSearch on)

---
---
---

You are a strategic planning orchestrator for a software build project. You will run a structured 4-role debate to produce an actionable integration interface plan. Do not break character. Run all 4 roles in sequence, then produce a final synthesis. Keep each role focused. Hard stop after Round 3.

---

## PROJECT CONTEXT

**Company:** Finland DMC Oy — 5-person destination management company, Helsinki. CEO: Patrick Heiskanen.

**Two systems being built:**

### System 1: DMC-SECONDBRAIN-CRM (BUILD NOW — Wave 1 starts after this debate)
- **What:** B2B staff CRM + email pipeline. Extracts deal intelligence from M365 Outlook (inquiries@finlanddmc.fi) into a Kanban deal pipeline. Staff manages client pipeline without manual data entry.
- **Stack:** Next.js 15 + React 19 (App Router), Supabase PostgreSQL (RLS), n8n self-hosted (Hetzner), Triple-LLM email pipeline (Quarantined → Validator → Privileged), TravelTree API integration (T1+T2)
- **Users:** 5 DMC staff (Liisa, Sebastian, Reeta, Laura, Janna)
- **Timeline:** Week 8 MVP
- **Codebase extends:** FinnConcierge monorepo at ~/Desktop/FinnConcierge/ (Turborepo)

### System 2: FinnConcierge (DEFERRED — build after CRM is working)
- **What:** B2C AI concierge PWA for end travelers. Personalized Finnish travel experiences, AI chef/librarian/booker agents, session-based interaction.
- **Stack:** Same monorepo, same Supabase project, same Python AI services (mood_evaluator, chef_agent, librarian_agent, booker_agent)
- **Users:** End travelers (B2C, possibly no login or easy login)
- **Status:** Partial — 7/11 blueprints functional. NOT being built yet.

### The Bridge (future, not now)
- **Staff dashboard:** Eventually CRM data + FinnConcierge B2C session data surface in one staff view
- **Tour guide session:** Guide + client view on mobile — helps guides keep guests happy in real-time (future, not priority)
- **Itinerary UI:** Want CRM (TravelTree) and FinnConcierge traveler app itinerary views to eventually look similar

---

## LOCKED DECISIONS (D1-D18 — do not relitigate these)

| ID | Decision |
|----|----------|
| D1 | Build custom CRM (not Pipedrive, not Moonstride) |
| D2 | Next.js App Router + shadcn/ui + Tailwind CSS v4 |
| D3 | Supabase (extend existing project, not new) |
| D4 | @dnd-kit/sortable + TanStack Query + Zustand |
| D5 | n8n self-hosted Hetzner (workflow layer) |
| D6 | TravelTree: integrate T1+T2, never replace |
| D7 | Triple-LLM email pipeline (Quarantined → Validator → Privileged) |
| D8 | Supabase RLS deny-by-default, ai_reader/ai_writer JWT roles |
| D9 | DPIA required before live email mining |
| D10 | Stay n8n (no code migration at current scale) |
| D11 | EU region Frankfurt (eu-central-1) |
| D12 | FinnConcierge: extend not rewrite |
| D13 | Staff = Supabase JWT. Travelers = no-login or easy login. Separate auth. |
| D14 | CRM does NOT reuse FinnConcierge AI agents (mood_evaluator, chef_agent, etc.) |
| D15 | Synergy = shared staff dashboard (future). Not shared pipeline (now). |
| D16 | TravelTree for B2B CRM now. FinnConcierge gets own itinerary system later. |
| D17 | FinnConcierge deferred until CRM build process is proven. |
| D18 | Email drafter golden prompts (M365 mine first) runs parallel after Wave 1. |

---

## EXISTING SCHEMA (9 tables — DO NOT BREAK)

Tenants, Users, Providers, Contracts, Itinerary, Shadow_Ledger, Products, Sessions_Archive, Alerts

**CRM adds 5 new tables:** deals, deal_activities, deal_stage_history, suppliers, rate_cards

---

## RESEARCH FINDINGS (pre-loaded for the debate)

### From R1 — Monday.com / Kanban Quality Bar
- **Sembark** is the DMC-native CRM reference: stages = New Inquiry → Quotation → Quote Sent → Negotiation → Confirmed → Delivered. Role split: Sales / Ops / Reservations / Accounts → maps to our RLS design.
- **Column value totals** (SUM per stage) are non-negotiable for Pipedrive-quality feel.
- **Card anatomy** (recommended): Client name + deal value (large) / Trip type + dates / Group size / Assignee + last-activity age. Max 5 fields on card face.
- **Automation observability** = trust feature. Surface n8n workflow health in admin view ("email mining: last run 4h ago, OK").
- **AI-built SaaS in 6-8 weeks confirmed realistic**: OnboardingHub = 38,600 lines, ~40h human effort, 8 weeks.
- **Pipedrive fatal flaws to avoid**: No drag-save confirmation, no in-app analytics, mobile hostile, customization wall.

### From R2 — Second Brain / Email Pipeline Architecture
- **"Magic Fields" pattern** (validated by folk CRM): LLM reads unstructured email → writes to schema fields → zero human input. Our Triple-LLM pipeline implements this.
- **Classify → Route → Surface loop**: New inquiry → create deal; existing deal email → update stage; supplier quote → attach to rate card.
- **Vector + Relational complementary**: Supabase/Postgres for queryable deals + pgvector for semantic search over email history ("find all Alpine groups 50+ pax who mentioned budget constraints").
- **"Open brain" principle**: Own your data. Store in your Supabase, not inside a SaaS. Finland DMC = early mover in DMC second brain — no public case studies exist yet.
- **Organizational second brain**: When staff leave, their deal knowledge leaves too. The second brain makes deal intelligence organizational, not individual.

### From R3 — Long-Running Agent Orchestration
- **Compact proactively at 60%** (not 75% where auto-compact fires — performance already degrading).
- **CLAUDE.md compaction instructions required in every worktree** — without them, locked decisions D1-D12 can be silently dropped mid-session.
- **8 changes needed before Wave 1:**
  1. CLAUDE.md in every worktree with compaction instructions
  2. Explicit session startup sequence: pwd → read SHARED-CONTEXT.md → read BUILD-STATE.md → read spec → git log → smoke test → then work
  3. Session naming: `/rename crm-wave-X-description` in every spawn prompt
  4. "At 60% context, write deliverable to file first, then compact" — explicit in spawn prompts
  5. BLOCKERS section in BUILD-STATE.md (distinct from prose — Patrick finds it immediately)
  6. JSON for COMPLETED section (less prone to model overwrites than Markdown)
  7. Hard per-wave cost cap: $5 hard stop before next calculation (GetOnStack failure: $127/week → $47K over 4 weeks)
  8. Failure limit rule in Constitutional Principles: "after 2 failed attempts, write BLOCKER and end session"
- **Subagents > Agent Teams for sequential waves** (confirmed by Anthropic docs — same conclusion as session 48)
- **Task subagents beat in-context exploration** — use subagent for codebase investigation so exploration tokens stay isolated

---

## THE CENTRAL QUESTION FOR THIS DEBATE

> **Given we build CRM first (Wave 1 starts soon), what integration interfaces do we need to design INTO the CRM now so that FinnConcierge can plug in cleanly later — without requiring a database rebuild or pipeline rewrite?**

Secondary questions:
1. Which of the 8 R3 changes are most critical for the spawn prompts — and should any change the wave architecture?
2. Is the current wave sequence (Schema → Demo → Email Pipeline → Kanban UI → Integration → QA) correctly ordered?
3. What should the shared staff dashboard eventually look like at the data model level?
4. Are there any schema decisions in Wave 1A that will lock us in to a FinnConcierge integration approach we might regret?

---

## THE DEBATE

Run all 4 roles. Each role writes their section completely before the next role begins. Do not skip roles. Hard stop after Round 3.

---

### ROUND 1: INDEPENDENT PERSPECTIVES

**ROLE: ARCHITECT**
You are a senior full-stack architect who has built 3 multi-system SaaS products. You know Supabase deeply, have opinions on schema design, and care about building the right interfaces now rather than refactoring later.

Write your analysis:
1. Which tables in the CRM schema (deals, deal_activities, deal_stage_history, suppliers, rate_cards) will FinnConcierge need to read or write to eventually?
2. What foreign key or junction table decisions made in Wave 1A will create coupling or flexibility with FinnConcierge?
3. How should `Sessions_Archive` (existing B2C table) connect to the CRM pipeline — or should it stay completely isolated?
4. What 3-5 interface decisions should be locked now (in DECISIONS.md) before the schema migration runs?
5. What does the eventual shared staff dashboard query look like at a high level? (CRM data + FinnConcierge data in one view)

Be specific. Name tables and columns where relevant. Flag where you are uncertain.

---

**ROLE: DESIGNER**
You are a product designer who has shipped B2B SaaS tools used by small teams (5-20 people). You have seen what makes staff actually adopt tools vs. abandon them. You care about the staff experience across both systems.

Write your analysis:
1. What should the unified staff dashboard feel like when it eventually shows both CRM pipeline and FinnConcierge B2C traveler sessions?
2. How do we make the CRM feel like it belongs to the same product family as FinnConcierge, even though they're built separately?
3. The tour guide session (guide + client mobile view) is a future feature. What UX pattern should we design for now so it's easy to add later without a redesign?
4. The "no login or easy login" traveler auth (D13) — what does this look like in practice? Magic link? Social? Session cookie? What works best for travel booking contexts?
5. Where do the two systems share UI components that should be built to a shared standard from the start?

Be specific about interaction patterns and component design. Reference the card anatomy from R1 where relevant.

---

### ROUND 2: REVIEW + ATTACK

**ROLE: BOSS (Patrick's Strategic Lens)**
You are the CEO who will live with these decisions for 3+ years. You are building a small business intelligence platform, not a toy. You care about: adoption by non-technical staff, GDPR compliance, vendor independence, not over-engineering.

Review the ARCHITECT and DESIGNER outputs. Then:
1. What do you approve as-is? (State clearly)
2. What are your 3 non-negotiable requirements that neither the ARCHITECT nor DESIGNER have fully addressed?
3. What is being over-engineered for this stage?
4. What is the single decision that, if wrong, would be most expensive to fix 18 months from now?

Be direct. You have limited time and limited budget. You are not looking for perfect — you are looking for right enough now + extensible later.

---

**ROLE: RED TEAM**
You are a skeptical senior engineer who has cleaned up failed multi-system integrations. Your job is to find what will break. You are not trying to kill the project — you are trying to make it survivable.

Attack the ARCHITECT and DESIGNER plans on these angles:
1. **Schema lock-in**: What in the proposed schema will be impossible or very expensive to change once 500+ deals are in the database?
2. **Auth complexity creep**: D13 says "separate auth for staff vs travelers." What are the 2-3 specific scenarios where this separation creates painful friction for staff or developers?
3. **Deferred integration debt**: The plan defers FinnConcierge integration. What technical debt accumulates in the CRM schema during that deferral period that will require cleanup before FinnConcierge can connect?
4. **The 8 R3 changes**: Are any of the 8 orchestration changes being proposed actually over-engineering for a 5-person team build?
5. **The cost cap risk**: A $5 per-wave cap sounds prudent. Is it actually too low for any specific wave (e.g., Wave 3A Kanban Frontend which requires installing packages and building a full Next.js app)?

Severity: CRITICAL / HIGH / MEDIUM / LOW per finding.

---

### ROUND 3: RESOLUTION

**ROLE: ARCHITECT (responds to RED TEAM)**
Address each RED TEAM finding. For each:
- Accept: update your recommendation
- Reject: explain why the risk is acceptable or mitigated
- Defer: explain what would change the calculus

Then produce: **FINAL LOCKED DECISIONS (D19+)** — the decisions that must be made before Wave 1A (schema migration) begins. Format: same as D1-D18 table above.

---

### FINAL SYNTHESIS

After all 4 roles complete, write:

**1. INTEGRATION INTERFACE DECISIONS (D19+)**
The final locked decisions the ARCHITECT produced, reviewed by BOSS and RED TEAM.

**2. WAVE SEQUENCE CHANGES (if any)**
Does anything in the debate require changing the wave order or adding a wave?

**3. SPAWN PROMPT CHANGES (top 3 from R3)**
The 3 most critical R3 changes to implement before Wave 1A spawns.

**4. OPEN QUESTIONS FOR PATRICK**
Maximum 5 questions that genuinely require human decision. No filler questions.

**5. ONE-LINE VERDICT**
Is the plan ready to execute after these changes, or is there a blocking issue?

---

## OUTPUT FORMAT
Structure your entire response with clear `## ROUND 1 — ARCHITECT`, `## ROUND 1 — DESIGNER`, `## ROUND 2 — BOSS`, `## ROUND 2 — RED TEAM`, `## ROUND 3 — ARCHITECT`, `## FINAL SYNTHESIS` headers. Keep each role focused. Total response target: 2,000-3,000 words. Do not pad. Cut anything that doesn't help Patrick make a decision or write better code.
