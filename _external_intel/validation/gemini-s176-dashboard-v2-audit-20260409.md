# Gemini Pro Structural Audit — Dashboard V2.0
Date: 2026-04-09 | Model: gemini-2.5-pro

## VERDICT: DISAGREE with Grok's "kill it." Direction is sound, scope needs brutal cut.

### Q1 — Kill verdict?
**Disagree.** Grok ignored NO-SAAS-CRM constraint and intentional Excel-as-MVP. Textbook advice for a different company. Direction sound, scope over-scoped.

### Q2 — Hybrid Option C reasonable?
**Yes, elegant and appropriate.** Zero-cost, zero-admin, single user = no file-locking issue. Patrick can debug every line. No framework magic.

### Q3 — Realistic 2-hour MVP (80% value)
**ONE view, ONE button. That's it:**
1. Generate single `dashboard.html` — Active Negotiations list with traffic lights
2. One "Log Call" button per company → fetch() POST to localhost:8000/log_call
3. Tiny Python server handles the POST, updates Excel, regenerates dashboard

**CUT everything else:** 3 other tabs, email drafter, log email, segment classifier, next recommended action.

### Q4 — Streamlit vs custom HTML+JS?
**Custom wins.** Streamlit adds abstraction + dependency. Custom solution = explicit, debuggable, zero dependencies beyond Python stdlib. Better for "coding CEO" maintenance.

### Q5 — mailto Finnish emails?
**Impractical for long body.** URL length limits (~2000 chars) break silently.
**Better: Two-button approach:**
1. `mailto:` button → ONLY recipient + subject (short, reliable)
2. "Copy Email Body" button → navigator.clipboard.writeText() → Sebastian pastes (Cmd+V)
Rock-solid, two-click workflow.

### Q6 — Top 3 valid Grok risks
1. **Excel fragile backend** — Mitigate: define migration trigger (2nd rep OR web-facing = Supabase). Daily git commit as backup.
2. **Multiple sources of truth** — Mitigate: dashboard = single mutation interface. Obsidian = scratchpad, not SoT. HTML = disposable view.
3. **Scope creep** — Mitigate: aggressive MVP scoping. V2.0 → V2.1 roadmap.

### Q7 — V2.0 MVP vs V2.1 split
**V2.0 (this week):** Dashboard with Active Negotiations + traffic lights + Log Call button. One .command launcher.
**V2.1 (2 weeks):** Sales Proposals tab + "Copy Email Body" + mailto combo + Log Email button.
