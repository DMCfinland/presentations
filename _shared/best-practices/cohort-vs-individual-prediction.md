# Cohort-vs-Individual Prediction Discipline

**Type:** feedback | **Source:** patrick + Grok R3 Benjamin, session 75 | **Tier:** B | **Confidence:** 0.7

---

When an AI system makes predictions from a client/user's historical data, individual observation counts below 10 produce ~57% accuracy — statistically indistinguishable from a coin flip. Surfacing a "confident" individual-level prediction at this accuracy destroys staff trust in the system permanently.

**The pattern:** Group clients into cohorts (by tier + primary category, e.g. 'gold_lapland'). Apply confidence tiers:
- **cohort_strong** (cohort_n ≥ 10): surface with no caveat → 90% accuracy
- **individual_ok** (n_observations ≥ 5): surface with explicit "Low confidence — limited history" label → 70% accuracy
- **suppressed** (n_observations < 5): NEVER surface as standalone signal. Feeds cohort_n only.

**Why:** Benjamin (Grok R3) Monte Carlo: 107 clients × 7.5yr × 50 emails/yr = 40,125 data points total, but individual pattern detection = 3–7 bookings per client = 57% hit rate. When staff approve an AI recommendation that turns out wrong at coin-flip rate, the system gets abandoned. The data math is not intuitive — always compute it before claiming "historical patterns show X."

**How to apply:** Any AI system making predictions from historical data with thin individual samples (N<10):
1. Compute cohort groups (tier + category or other natural grouping)
2. Apply the three-tier confidence schema above
3. Write rationale language differently per tier: cohort_strong → "Clients like X (gold tier, Lapland) book Q1 with 81% conversion — 10-week lead is the pattern." individual_ok → "Based on N bookings, window typically opens [month] — low confidence, treat as directional."
4. Never write confident rationale for individual_ok signals
5. Suppress-tier signals never appear in output — they are internal data only

**Domain:** CRM opportunity signals, seasonal marketing triggers, churn prediction, any "now is the right time" AI claim. Applies universally across portfolio.

**Locked as D51** in DMC CRM DECISIONS.md (2026-03-13). Non-negotiable — cannot be loosened without explicit Patrick approval.
