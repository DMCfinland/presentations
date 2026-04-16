# Gemini Deep Research — Data Architecture Validation
**Date:** 2026-04-01 | **Mode:** Deep Research
**Purpose:** Fact-check Grok Heavy claims on 1658 Holdings data architecture

## Summary: Grok was mostly FUD, architecture is viable

---

## Q1: n8n Cloud "95% die in 48h"
**VERDICT: OVERSTATED / ANECDOTAL**
- 95% figure = misconfigured self-hosted + Simple Memory usage, NOT Cloud
- n8n Cloud: ~99.8% uptime (StatusGator 2025), one 17h outage Feb 2026
- No financially backed SLA on Starter/Pro — Enterprise only
- "Memory leaks" = Simple Memory (volatile RAM). Fix: use Postgres Chat Memory.
- Starter 2,500 exec/month sufficient for 5 workflows (~1,500 used)
- Monitoring: execution logs + error triggers + global Error Workflow available

**Action:** Use Postgres Chat Memory (not Simple). Set up Error Workflow → Teams #technical.

## Q2: YT-laki "post-2025 amendments"
**VERDICT: PARTIALLY CORRECT — threshold actually ROSE**
- July 2025 amendment: threshold rose from 20 → 50 employees (NOT lowered)
- JS at ~50 staff = exactly at threshold for full obligations
- Scoring tool = "technological change" under Section 31
- Requirement: ongoing continuous dialogue (säännöllinen vuoropuhelu) — at least annually
- NOT "one missed meeting = illegal" — breach = hyvitys up to ~€35k/employee
- EU AI Act: B2B sales scoring = Minimal Risk. No heavy documentation needed.
- Minimum path: inform staff, discuss in meeting, record dialogue, basic AI literacy training

**Action:** Document YT-laki dialogue before tier-3 deployment. Not a hard blocker — a process requirement.

## Q3: Power BI + Supabase "community-demo"
**VERDICT: OUTDATED claim. Stable in 2026.**
- Method: PostgreSQL connector + Supavisor connection string (port 5432/6543)
- Stable for Scheduled Refresh (up to 8x/day on Pro). Import Mode recommended.
- DirectQuery works but slower. Not needed for our scale.
- ⚠️ "Old Import" for SharePoint Excel deprecated July 2026 — use Web URL connector
- Migration Excel → Supabase: swap Data Source, map columns. Power Query logic stays.

**Action:** Use Import Mode + Scheduled Refresh. Plan Excel connector migration before July 2026.

## Bonus: Data Decay 22%/year
**VERDICT: VERIFIED but contextual**
- 22.5% annual = real baseline (Landbase 2026, Forbes)
- 70.3% = upper bound for high-turnover industries (tech/SaaS), NOT hospitality
- Hospitality B2B: ~18-25% estimated
- At 200 records: ~4 contacts invalid/month, ~45/year
- 2-3 staff maintaining registry will notice key contact changes
- Sales waste: 27.3% of time on bad leads (540h/year)

**Action:** Add 6-month staleness flag to scorer. Consider email verification API later.

## n8n Starter Tier Limits (important finding)
- 2,500 exec/month — sufficient for JS alone
- BUT: 10 companies × 5 workflows × 30 days = 1,500 → thin margin
- No environment variables on Starter → credential management hard for 10 companies
- Recommendation: Start with Starter for JS only. Pro (€60/mo) when scaling to other companies.
