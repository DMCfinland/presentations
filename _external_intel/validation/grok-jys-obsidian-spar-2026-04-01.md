# Grok Spar — JYS Obsidian Knowledge Architecture
**Date:** 2026-04-01 | **Model:** Grok Auto (Heavy modal blocked — upgrade required)
**Chat:** https://grok.com/chat?rid=51040ff3-8f91-4965-bf07-17edfa3d9f8c
**Sources cited:** 189

---

## VERDICTS

| Decision | Verdict |
|---|---|
| Tier 3 Group Sales Second Brain as first feature | **NO GO** |
| Excel + Obsidian local MVP as data foundation | **NO GO** |
| Conditional GO | Only if 4 conditions met (see below) |

---

## KEY REVERSALS (act on these)

### [Benjamin] REVERSED — Scoring model fatally under-specified
Missing mandatory fields:
- **Historical revenue / lifetime value** — #1 omission. Without it, €50k corporate client = same weight as €5k school group. Scoring is random noise.
- Customer segment (wedding / conference / incentive / sports)
- Last quote/proposal date + outcome
- Contact-person decision authority

### [Lucas] REVERSED — Excel+Obsidian MVP is wrong foundation
Supabase first instead: typed schemas, row-level security, audit logs, Claude Code querying, zero migration pain later. Can be spun up in one afternoon. Excel = technical debt Finnish hospitality SMEs universally regret.

### [Lucas] REVERSED — Tier 3 first is wrong priority
B2B high-value sales is the WORST place to introduce unproven AI:
- Staff trust evaporates after 2-3 wrong "next contact" recommendations
- Low frequency = feedback loop is MONTHS long
- Tier 4 (customer-facing, high volume) gives rapid iteration signals first — build trust there, then move to Tier 3

### [Harper] YT-laki MISSED — LEGAL GATE
Yhteistoimintalaki (Co-operation Act) requires mandatory staff consultation before implementing significant changes to work processes for 50-person company. A "next proactive contact" AI that assigns sales tasks alters core job function = triggers YT procedure. Must be documented before ANY staff feature goes live.

---

## CONFIRMED (architecture elements that held)

- [Benjamin] Local _PRIVATE zone + Claude Code isolation is a defensible Art. 32 GDPR technical control
- [Harper] Finnish SME AI adoption is high (66% of firms) — staff acceptance will be faster than other markets
- [Lucas] Tiered Obsidian structure is elegant for cumulative access and blast-radius containment

---

## 3 ARCHITECTURAL RISKS NAMED

1. **[Benjamin] Parsing fragility** — Claude Code script reading .xlsx + .md files will break on: Excel date-format drift, non-standard Markdown headings, staff free-text without YAML frontmatter. No validation layer = silent bad data = wrong sales actions.

2. **[Benjamin/Harper] Tier synchronisation debt** — Distilled zone manually created from private zone. Any drift = GDPR Art. 5(1)(d) accuracy violations + legally unreliable Tier 3 suggestions.

3. **[Harper] Scalability cliff at 200+ customers** — Excel concurrency + Obsidian file bloat + local script runtime forces migration under fire. Finnish hospitality SMEs show this pattern universally at 12-18 months.

---

## GDPR FINDINGS [Harper]

- Zero fines issued purely for "Excel on Mac" local storage in 2025-2026
- BUT enforcement cases (Finnish SA precedent, €856k) for:
  - Undefined retention periods (most common)
  - Inadequate Art. 32 technical/organisational measures
  - Data minimisation failures (old records never purged)
- **Local files = zero auditability** — regulators demand proof of who accessed what, when, why

**[Harper] vs [Lucas/Benjamin] UNRESOLVED:** Harper: zero direct enforcement against local Excel/Mac. Lucas/Benjamin: local Mac inherently non-compliant on auditability. "Appropriate technical measures" cannot be satisfied on a solo CEO's laptop.

---

## FATAL ASSUMPTION [Lucas]

"The CEO can personally maintain perfect, audit-ready data hygiene across Excel + Obsidian + local scripts indefinitely while also running a 10-company hospitality group."

If data quality degrades (inevitable with staff turnover + seasonal peaks) → every higher tier becomes garbage + GDPR accuracy principle breached.

---

## WHAT WAS MISSED (not in original plan)

- No automated data-retention/deletion policy (direct violation path)
- No mobile access story for field staff (lake resort sales happen on-site)
- No fallback when Claude Code model version changes + scoring drifts
- No cost model for Supabase migration (tech debt tax)
- No monitoring of AI suggestion acceptance rate (GDPR automated decision-making proof)

---

## CONDITIONAL GO — 4 requirements

1. Historical revenue field + customer segment added to scoring model
2. Supabase migration completed BEFORE any staff exposure
3. YT-laki consultation documented
4. Retention/deletion automation in place from day 1
