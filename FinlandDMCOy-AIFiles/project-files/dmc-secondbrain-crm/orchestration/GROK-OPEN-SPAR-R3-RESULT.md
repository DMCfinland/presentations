# Grok Open Spar — Round 3 Result
**Date:** 2026-03-13 | **Model:** Grok 4 Heavy (4-agent council)
**Prompt:** `research/GROK-PROMPT-OPEN-SPAR-R3.md`
**Mode:** Fully open — no pre-loaded options or verdicts

---

## Raw Grok Output

### Section 1: What this system is capable of that we're not using yet

[Harper] **Relationship decay velocity** — measurable acceleration/deceleration in email response latency, stakeholder involvement shifts (who gets cc'd, who gets removed), and sentiment drift across 5–10-year histories. Gong and Clari surface "account health decay" scores weeks before a client goes dormant. Pure Graph API metadata — no new data source, zero entry. Fits Finnish trust culture better than opportunity surfacing: protects existing €1.5M, not chasing new deals.

[Benjamin] **Cohort pattern mining** — 40,125 estimated emails (107 clients × 7.5 years × 50 emails/yr, verified). Individual seasonal predictions are noise (3–7 observations per client, 57% accuracy in simulation). But cross-client grouping by tier + destination delivers reliable signals: "Clients like Flash Pack book Lapland Q1 with 81% conversion when contacted 10 weeks prior." Pure detection on the email corpus we already own.

[Harper] **Multi-thread stakeholder mapping** — who is copied, who replies, who is added/removed over years. Revenue Grid (2026) does this in Salesforce; our Supabase + n8n can extract the same from Graph API message metadata (sender, recipients, thread participation) without touching external data. Reveals hidden decision-makers before proposals are requested.

[Benjamin] **Disagreement with Harper:** Gong-style conversation intelligence requires call transcripts or full calendar integration. Email-only velocity + cohort mining is the only statistically valid path forward under our constraint.

### Section 2: What would break this system at scale or over time

[Benjamin] **Statistical overconfidence on low-sample claims** will break trust by Year 2. Monte Carlo on 21 consistent clients over 7 years with realistic ±3-month noise: individual "historical pattern says now is perfect" alerts are essentially random (57% hit rate). Without cohort aggregation and Bayesian weighting, staff will start ignoring the morning dashboard entirely.

[Harper] **Embedding model drift** — text-embedding-3-small is 2+ years old in 2026; by 2028 newer models make our 1536-dim vectors obsolete. Without raw_content JSONB + scheduled re-embedding pipeline, "similar historical deals" panels return increasingly irrelevant results. Time-bridging value evaporates overnight.

[Lucas] **Alert fatigue + cultural mismatch** — 5 people who already know their 107 clients intimately don't need 3–5 daily "opportunity" cards. When a single tone-deaf AI-generated re-engagement email damages a 7-year relationship, the entire Second Brain gets uninstalled.

[Benjamin] **Disagreement with Harper/Lucas:** The break is not cultural — it's failing to implement statistical guardrails before surfacing anything.

### Section 3: What a smarter competitor would do differently

[Harper] **Autonomous revenue orchestration** (Clari, Oliv AI Deal Driver) — not just surfacing opportunities but auto-updating CRM fields, generating risk reports, drafting supplier coordination tasks during operating stage. 30% less manual admin. Our judgment-line constraint forbids this; competitors use it.

[Harper] **TravelTree / operational integration** — turning the system from pre-sale memory into full-lifecycle execution. Travel-specific CRMs (moonstride, TourConnect AI) already do dynamic pricing + AI itinerary creation from historical data. Our Second Brain stops at proposal stage and leaves €1.5M operating risk entirely manual.

[Benjamin] **EU-compliant intent signals** (Cognism-style) — 20–30% more accurate dormant-client reactivation. Requires external data; we can't copy without GDPR analysis.

### Section 4: Lucas's single strongest challenge

[Lucas] **We are solving the wrong problem.** In a 5-person Finnish DMC on €1.5M with 107 long-term relationships, the real bottleneck is flawless execution during confirmed → invoiced: itinerary micro-adjustments on flight delays, supplier renegotiation under tight margins, on-ground coordination that clients remember for 10 years. Staff already know their top clients' seasonal patterns from memory. The obsession with proactive pre-sale surfacing and AI strategy drafts risks turning reliable humans into alert-checkers and producing emails that feel slightly off in a culture that values personal authenticity above all. Benjamin's math proves seasonal signals are too weak for individual confidence. Harper's examples show competitors win by integrating operations (TravelTree + calendar), not by building a fancier email memory prosthesis. Correct 3-year target: a system that removes admin from confirmed → invoiced, not one that generates more things for the team to approve before breakfast.

---

## Debrief (Claude analysis — run after Grok)

### Real Tool Calls?
- Harper cited: Gong ✓, Clari ✓, Revenue Grid ✓, Cognism ✓, moonstride ✓ (we rejected in s58), Oliv AI Deal Driver ⚠️ (verify), TourConnect AI ⚠️ (likely hallucinated — no prior trace)
- Benjamin: showed arithmetic (40,125 = 107 × 7.5 × 50) ✓ but "57% Monte Carlo" = internal estimation, not code_execution output. **Unverified claim — treat as directional, not precise.**

### Benjamin's Math — Verified
- 107 × 7.5 × 50 = 40,125 ✓
- 3–7 booking observations per client ✓ (if 1 booking/year × 7.5 years = 7–8 data points)
- **57% individual pattern accuracy: UNVERIFIED.** Grok's internal estimate. True value unknown. But the directional claim is sound: 3–7 observations is a small sample for reliable seasonal prediction. Cohort approach is statistically better.

### Agent Conflicts (do not resolve — Patrick decides)
| Conflict | Benjamin says | Harper/Lucas says |
|----------|--------------|-------------------|
| Calendar/call intelligence | Email-only is the only valid path | Gong-style requires calls (agrees with Benjamin here) |
| What breaks the system | Statistical overconfidence | Cultural mismatch (Lucas) / embedding drift (Harper) |
| Direction | Build cohort mining on what exists | Wrong problem — build operations (Lucas) |

### Lucas's Challenge — Assessment
**Half right.**
- Correct: for top 20 clients (AHI Travel = 75% revenue), staff already know seasonal patterns cold. AI memory adds little for these.
- Correct: confirmed → invoiced is where client experience is actually delivered. One failed trip loses a 10-year relationship faster than a missed re-engagement email.
- Correct: Benjamin's math shows individual pattern claims are weak (3–7 observations).
- Incomplete: for clients #40–107, staff do NOT know patterns cold. 107 clients ÷ 5 staff = 21 clients each at the tail. Memory fails there.
- The solution: TravelTree integration (D16 — already in plan, deferred). Lucas is saying it should be first, not last. This is actionable.

### Highest-Value Findings (net new vs Rounds 1+2)

1. **Relationship decay velocity** (Harper) — NEW. Response latency drift + stakeholder changes = leading indicator. Pure Graph API metadata. Zero new data source. Weeks of warning before dormancy. Not in any previous round.

2. **Statistical guardrail on individual pattern claims** (Benjamin) — CRITICAL correction to Wave 3C. We were about to surface "Flash Pack's 18-month pattern says now is perfect" — a 3-observation claim. Must switch to cohort-level predictions with explicit confidence scoring. Individual claims need Bayesian weighting + N≥10 threshold before surfacing.

3. **Lucas's direction challenge: confirmed → invoiced first** — STRATEGIC. Not invalidating pre-sale intelligence, but reprioritizing. TravelTree integration (D16) may need to move earlier in the wave plan.

4. **Cohort pattern mining** (Benjamin) — reinforces D45 but with statistical discipline. "Clients like Flash Pack" (tier + destination cohort) vs "Flash Pack specifically" is the design change.

### What This Changes

- **Wave 3C design:** Individual seasonal predictions must be replaced by cohort-level predictions with confidence scores. Only surface signals where N≥10 in cohort OR N≥5 for individual with explicit "low confidence" label.
- **Wave sequence question:** Should TravelTree operational integration (D16, confirmed → invoiced) move before Wave 3C? Patrick decides.
- **New capability to add:** Relationship decay velocity monitor — response latency + stakeholder tracking from Graph API metadata. Fits before Wave 3C as a defensive metric (protect existing revenue) vs offensive (find new).

---

## Actions Required

- [ ] **Patrick decides:** Lucas's direction challenge — is confirmed → invoiced operational integration higher priority than Wave 3C pre-sale opportunity engine?
- [ ] Verify Oliv AI Deal Driver exists and does what Harper claimed
- [ ] Update Wave 3C spawn prompt: replace individual pattern surfacing with cohort-level + confidence scoring (N thresholds)
- [ ] Add relationship decay velocity as a new signal type in Wave 3C (response latency monitoring via Graph API metadata — no new data source)
- [ ] Log D51 (statistical guardrail on pattern claims) to DECISIONS.md
