# Grok Prompt — Opportunity Engine + Long-Term Architecture
**Date:** 2026-03-13
**Model:** Grok 4 Heavy (4-agent council)
**Round:** 2 (follow-up to Dashboard Evolution debate)
**Paste to:** grok.com → Grok 4 Heavy mode → paste entire block below

> ⚠️ **PRE-SKILL-v1.2 PROMPT — DO NOT REUSE THIS PATTERN**
> This prompt contains pre-filled answers for all questions (signals, strategy, architecture, "what we missed"). Grok echoed them back without independent reasoning. Skill updated to v1.2 on 2026-03-13. Rebuild as open research questions before rerunning.

---

## PASTE START

**ROLE ASSIGNMENT — 4-AGENT COUNCIL (same as Round 1):**

- **Agent 1 — UX/Adoption Specialist**
- **Agent 2 — Technical Architect**
- **Agent 3 — DMC Operations Expert**
- **Agent 4 — AI Systems Designer**

---

## ROUND 1 RECAP (what we already decided)

We are building a Second Brain CRM for Finland DMC Oy — a 5-person Finnish travel DMC managing B2B group sales. Stack: Supabase (Hetzner, eu-central-1, pgvector), n8n (self-hosted), Next.js PWA. 107 client profiles embedded. 14-table schema live.

Round 1 approved these improvements (already in build plan):
- **A (Wave 2B):** Time-bridging panel — surface top 3 similar historical closed deals when staff opens a deal
- **B (Wave 2A):** Staff load view — cross-category capacity panel
- **C (Later):** Pipeline health / win-rate metric — requires outcome tracking first
- **D (Wave 3A):** Proactive seasonal alerts — rate window closures surfaced before staff asks
- **E (Wave 3A+):** Supplier knowledge door — agent extracts supplier emails → rate_cards stays current

Round 1 "ONE THING WE MISSED": thumbs-up/down feedback on every panel + onboarding tooltip tour.

---

## WHAT ROUND 1 DIDN'T ADDRESS

Round 1 focused on maintaining and improving EXISTING deals. But the system's highest-value function is finding deals BEFORE they exist — proactively identifying opportunities and generating strategies for pursuing them.

Nate AI's Open Brain principles apply here too:
- **Proactive surfacing:** "Design for what you want your agent to NOTICE, not just what staff will look up."
- **Time-bridging:** "Agent memory doesn't decay" — it sees annual booking patterns, dormant accounts, seasonal cycles.
- **Cross-category reasoning:** Client tier + travel dates + destination preference + last contact + market context → opportunity signal.
- **Judgment line:** Agent spots the opportunity and surfaces it with a strategy draft → human decides whether to act → agent executes outreach.

---

## THE CORE QUESTION FOR THIS DEBATE

**We want this Second Brain CRM to be a LONG-TERM system — built once, improving over time, not replaced in 3 years.** It should proactively surface deal opportunities and draft pursuit strategies, not just track deals we already know about.

Specifically:

### Question 1 — Opportunity Signal Design

What signals should the system monitor to surface new revenue opportunities proactively? Rate each signal type:

- **Re-engagement signals:** Dormant clients (no inquiry in 12+ months) from high-revenue or high-potential tiers. Example: Flash Pack (€558K historically, orphaned 8 months).
- **Anniversary signals:** Clients who booked the same destination/season last year — "AHI Travel booked Lapland winter 2024–2025. March 2026 and no inquiry yet."
- **Market signals:** External — new route openings, flight capacity increases, competitor service gaps (this requires external data — is it worth it?).
- **Upsell signals:** Confirmed deals where group profile matches an additional product (e.g., group booked Helsinki city → add Archipelago day trip based on similar closed deals).
- **Referral signals:** Clients who completed trips with high satisfaction signals in follow-up emails — flag as referral candidates.
- **Lapsed proposal signals:** Proposals sent but not won in past years — do the reasons still apply, or is now a better time?

For each: INCLUDE / EXCLUDE / MODIFY + rationale. Then rank the 3 strongest for a 5-person DMC.

### Question 2 — Strategy Generation (not just alerting)

Current design: agent surfaces, human decides. But for opportunity signals, "decides" requires knowing WHAT to do. The system should generate a pursuit strategy, not just a flag.

Example output for a re-engagement signal:
```
OPPORTUNITY: Flash Pack — 8 months dark
Last booking: Summer 2024, €189K, Archipelago route, 22 pax
Assigned to Janna (orphaned after she left — NOW unassigned)
Signal: No contact since July. Q1 is their typical planning window.
Strategy options:
  A) Warm re-introduction from new contact (Liisa) — frame as "new point of contact" email
  B) Product-first approach — lead with new 2026 Archipelago itinerary before re-introducing
  C) Wait for them to reach out — low risk if they're a loyal returning client
Recommended: A — reason: 8 months dark + account reassignment = re-introduction is natural and professional
[Send A] [Send B] [Dismiss — they'll reach out] [Edit strategy]
```

Should the system generate this kind of strategic brief? What are the risks? What's the minimum viable version for Wave 3A?

### Question 3 — Long-Term Architecture for a Durable System

We want this to last 5+ years without a rewrite. What architectural decisions made NOW determine whether the system stays relevant as AI models improve?

Specifically evaluate:
- **Data ownership:** All intelligence in our own Supabase (no SaaS lock-in). Is this still the right call in 2028 when SaaS CRMs may have comparable AI? What would make us regret this?
- **Embedding model lock-in:** We chose text-embedding-3-small (1536-dim). OpenAI controls this. What's the risk in 3 years? Should we plan for re-embedding now (store raw content separately from embeddings)?
- **n8n self-hosted vs managed:** n8n Cloud is now available. At what point does self-hosting become a maintenance burden that exceeds the cost savings?
- **Model routing:** We use Sonnet for classification, Haiku for mechanical work. In 2 years, today's Haiku-level capability may cost 10x less. Does the architecture need a model abstraction layer?
- **Schema evolution:** 14 tables now. In 2 years: add integrations (TravelTree API, accounting, HR). What schema design decisions prevent future migration pain?

For each: APPROVE current decision / FLAG as future risk / CHANGE NOW + rationale.

### Question 4 — What Should the System Know That We Haven't Thought Of

Based on what you know about:
- How successful B2B sales teams use CRM intelligence
- How AI second brain systems have evolved 2024–2026
- The specific context of a 5-person travel DMC with 107 clients and €1.25M pipeline

What capability or data signal are we NOT considering that would have the highest impact in 12 months?

---

## CONSTRAINTS (same as Round 1, carry forward)

- 5 staff users. Don't overengineer.
- Zero data entry. All intelligence from email, calendar, proposals — not from staff manually entering anything.
- Judgment line sacred. Strategy is SUGGESTED, not auto-sent. Human approves every outreach.
- GDPR: all data in Supabase (Hetzner, EU). No client PII to US services without DPA.
- Budget: €80/h developer. Each feature must earn its build cost.
- Don't delay Wave 2A (email pipeline in progress).

---

## VERDICT FORMAT

### For Question 1 (Opportunity Signals):
Rate each signal: INCLUDE / EXCLUDE / MODIFY + 1-line rationale
Then: **Top 3 priority signals for Wave 3A**

### For Question 2 (Strategy Generation):
- Should the system generate strategic briefs? YES / NO / LIMITED VERSION
- If yes: what's the minimum viable brief for Wave 3A?
- What's the highest risk in auto-generating strategies?

### For Question 3 (Long-Term Architecture):
For each item: APPROVE / FLAG (risk + timeline) / CHANGE NOW
Then: **2 decisions we must make before Wave 3A to avoid technical debt**

### For Question 4 (What We're Missing):
Each agent proposes ONE capability we haven't considered. Council votes on which is highest impact. Single winner with full rationale.

---

## FINAL ASK

After verdicts: give us a **"Second Brain CRM North Star"** — a single paragraph that describes what this system looks like at its best in 3 years, written as if a staff member is describing their workday using it. This is the design target we test every future decision against.

## PASTE END

---

## After Running Grok

Save the full response as:
`FinlandDMCOy-AIFiles/project-files/dmc-secondbrain-crm/orchestration/GROK-DEBATE-OPPORTUNITY-ENGINE-RESULT.md`

Then:
1. Add approved opportunity signals as **Wave 3A: Opportunity Engine** to WAVE-BUILD-AGENTS.md
2. Add North Star paragraph to BP08-STAFF-DASHBOARD-v2.md header
3. Flag any architecture change decisions to DECISIONS.md (D43+)
