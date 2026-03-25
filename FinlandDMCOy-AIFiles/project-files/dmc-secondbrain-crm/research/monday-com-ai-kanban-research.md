# Monday.com AI Kanban Research
**Date:** 2026-03-11 | **Agent:** R1

---

## Key Findings (top 8 most actionable)

### F1 — Monday.com's Kanban totals deal value per column automatically
Every Kanban column in Monday CRM shows the aggregate deal value at the bottom. This is table-stakes for a "Pipedrive-quality" feel. Users scan the board and instantly know how much revenue is in each stage without opening a single card. **For our build:** implement a `SUM(deal_value)` footer on every pipeline column, rendered in currency. Non-negotiable.
- Source: https://tech.co/crm-software/monday-crm-review

### F2 — Monday.com's AI SDR Agent: the benchmark for AI-assisted pipeline (2025–2026)
Monday's SDR Agent calls or emails new leads within seconds of entry, qualifies them through adaptive conversations, logs every interaction with a detailed summary + call recording + next steps, and books meetings. Only pre-qualified leads reach the human sales rep. The CRM stays current automatically — no manual logging required.
**For our build:** We cannot match this in phase 1, but the *principle* is the bar: the system should log activity automatically (from email mining) and surface summaries on the deal card. The human should never need to type what just happened.
- Source: https://monday.com/blog/crm-and-sales/ai-sdr-agent/ | https://support.monday.com/hc/en-us/articles/31002285812882-monday-CRM-AI-Sales-Agent

### F3 — Card content is fully user-configurable; restraint is the quality signal
Monday's Kanban cards let admins choose which columns appear on the card face. The UX benchmark from 2025 card design research is clear: **restraint = quality**. Show 3–5 fields max on the card surface. If everything is visible at a glance, nothing stands out. Premium CRMs surface: title, stage, value, one date, one status pill.
**For our build:** DMC deal card should show: client name, trip dates, group size, deal value, last-activity-age (e.g. "3d ago"). That's it on the card face. Everything else lives in the expanded panel.
- Sources: https://support.monday.com/hc/en-us/articles/4405723870994-The-Cards-View | https://uxplanet.org/ultimate-guide-for-designing-ui-cards-59488a91b44f

### F4 — The "AI-built SaaS in weeks" benchmark: 38,600 lines in 8 weeks with ~40h human effort
A documented 2025–2026 case: OnboardingHub — a full Rails SaaS with auth, multi-tenancy, Stripe billing, media library, and tests — was built in ~8 weeks across 727 commits with roughly 25–45 hours of actual human effort. The human acted as PM/architect/reviewer; Claude did bulk implementation. A second case: Batko.ai built a full platform in under 5 weeks, zero lines written by human.
**For our build:** This confirms the 6-week implementation roadmap is realistic. The bottleneck is human decision-making and review, not build speed.
- Sources: https://world.hey.com/cpinto/building-a-complete-saas-product-with-only-claude-code-cca13895 | https://batko.ai/blog/build-saas-with-claude-code

### F5 — Sembark is the closest existing DMC-native CRM; study its pipeline stages
Sembark is the leading DMC-specific CRM (2026). Key features: 60-second quote generation with auto-costing and multi-currency, lead capture API integrated with Facebook/Instagram/Google Ads, smart tour calendar (daily/weekly/monthly), role-based access (Owner, Manager, Sales, Ops, Reservations, Accounts), and supplier payment tracking. Pipeline stages implied: Lead Capture → Quotation → Quotation Sent → Confirmed → Operations → Completed.
**For our build:** Sembark's role separation (Sales vs Ops vs Reservations vs Accounts) should map directly to our access control model. Their 6-stage pipeline is the DMC-native reference.
- Source: https://sembark.com/best-travel-crm-software-suite-dmc/

### F6 — Pipedrive's fatal flaws to avoid (ranked by frequency)
1. **Support is unreachable** — users report waiting days, accounts shut down without resolution
2. **Reporting is shallow** — cross-data cohort analysis requires external tools; basic reports only
3. **Customization hits a wall** — fine for simple pipelines, breaks for complex or industry-specific workflows
4. **Constant bugs** — new technical issues appear weekly; platform hangs, emails fail to save
5. **Billing surprises** — charged for add-ons not ordered; no refunds
6. **Mobile app poor** — "not easy to use" is the most common mobile complaint
7. **Product team ignores feedback** — ships features users didn't ask for, ignores repeated requests
**For our build:** Avoid the reporting gap by building a deal analytics view from day 1 (even simple). Avoid the customization wall by making pipeline stages configurable. The "bugs" issue is really a reliability issue — Supabase Realtime with optimistic UI updates prevents the "did my drag save?" anxiety.
- Sources: https://www.folk.app/articles/pipedrive-problems | https://www.g2.com/products/pipedrive/reviews

### F7 — Monday.com's Autopilot Hub (Nov 2025): automation observability is a feature
Monday shipped an "Autopilot hub" — a central view showing all automations, their health, usage stats, and connections. Users can see what's running, what's failing, and why.
**For our build:** In our n8n workflow stack, surface automation health in the admin view. A simple status table (workflow name, last run, status, next run) removes the "is the auto-mining working?" anxiety for staff. This is a trust feature, not a power-user feature.
- Source: https://ir.monday.com/news-and-events/news-releases/news-details/2025/monday-com-Expands-AI-Powered-Agents-CRM-Suite-and-Enterprise-Grade-Capabilities/default.aspx

### F8 — Travel DMC pipeline integration pattern: booking event triggers CRM update automatically
The documented pattern for travel CRM integration: when a booking is created in a reservations platform, the integration automatically (1) creates/updates the client record, (2) generates follow-up tasks, (3) updates lifecycle stage, (4) adds booking amount to pipeline forecast, (5) schedules email reminders. Zero manual entry.
**For our build:** The email-to-deal n8n workflow should replicate this chain. A new confirmed booking email from a supplier should auto-update the deal stage, log the booking value, and create a follow-up task. This is the zero-entry promise.
- Source: https://dmcquote.com/blog/post/travel-crm-systems-best-options-small-agencies

---

## UX Quality Bar

These are the specific patterns that separate Pipedrive-quality from cheap Kanban CRM:

| Pattern | Cheap | Pipedrive/Monday-quality |
|---------|-------|--------------------------|
| Column totals | None or opt-in | Always visible, currency-formatted, auto-updating |
| Drag-and-drop | Page reload or lag | Instant optimistic update, smooth animation, persists to DB in background |
| Card density | Too much info OR too little | 4–5 curated fields; title is largest element |
| Empty state | Blank column | Helpful prompt ("No deals here. Drag one over or add a deal.") |
| Last activity | Not shown | Visible on card as relative time ("3d ago") — triggers anxiety if stale |
| Deal value | In list view only | On card AND in column total |
| Stage change | Manual dropdown | Drag = stage change (single interaction) |
| Mobile | Desktop crammed into phone | Touch-friendly card tap, swipe to change stage |
| Loading state | Spinner blocking UI | Skeleton cards that fill in (perceived performance) |
| Color system | Random colors | Semantic: green=on track, yellow=stale, red=overdue |

### Card anatomy for DMC deal (recommended)
```
┌─────────────────────────────────┐
│ [CLIENT NAME]              €4,2k │  ← title + value (largest elements)
│ Arctic Safari · 14–18 Mar        │  ← trip type + dates
│ 12 pax                           │  ← group size
│ ●●● Reeta · 3d ago              │  ← assignee + last activity age
└─────────────────────────────────┘
```
- Color bar on left edge = stage health (green/yellow/red)
- Hover reveals: source channel, next action due
- Click opens full deal panel (no page navigation)

### Drag-and-drop implementation note
Use `@dnd-kit/sortable` (already validated in FinnConcierge codebase). Key behaviors:
1. Optimistic update: move card visually before DB confirms
2. Column total updates instantly as card moves
3. If DB save fails: card snaps back with error toast
4. On touch: hold 300ms to initiate drag (prevents scroll conflict)

---

## What to AVOID

Drawn from Pipedrive complaints + Monday.com user reviews:

### Hard avoids (break trust immediately)
- **No column totals** — users feel blind without pipeline value visibility
- **Drag that doesn't save** — if a drag doesn't persist and user doesn't know, they stop trusting the system
- **No last-activity indicator** — sales reps need to know which deals are going cold; invisible staleness = lost deals
- **Slow page loads on pipeline** — the board must feel instant; Supabase Realtime subscription on page load, not polling
- **Reporting that requires export** — basic metrics (deals by stage, average close time, win rate) must be in-app

### UX anti-patterns (kill adoption)
- Showing too many fields on the card face (more than 6 = cognitive overload)
- Requiring multiple clicks to change a deal stage
- Opening a new page instead of a slide-over panel for deal details
- No empty state guidance (blank columns look broken)
- Mobile-hostile dense tables

### Product anti-patterns (kill long-term trust)
- Shipping features no one asked for while ignoring reported bugs
- No automation health visibility ("is the email mining even running?")
- Customization that works for simple cases but breaks at edge cases
- Billing/plan changes that surprise users

---

## Travel / DMC Specific

### Pipeline stages for a Finland DMC (derived from Sembark + DMC industry pattern)
Recommended 6-stage pipeline mapping to our Supabase schema:
1. **New Inquiry** — lead just arrived (email mined or manual)
2. **Quotation** — proposal being built
3. **Quote Sent** — waiting for client response
4. **Negotiation** — back-and-forth on scope/price
5. **Confirmed** — signed/deposit received; handoff to Ops
6. **Delivered** — trip completed; follow-up/upsell opportunity

Stage 5→6 transition should trigger an automatic Ops task creation (hotel/transfer/guide bookings).

### DMC-specific fields on deal card (beyond generic CRM)
- **Trip dates** (date range, not just close date)
- **Group size** (pax count)
- **Trip type** (Arctic Safari / City Break / Corporate Event / etc.)
- **Source channel** (TravelTree / direct / agency / referral)
- **Nationality of group** (affects supplier selection and language)
- **Seasonal flag** (winter = Northern Lights season; summer = Midnight Sun)

### What generic CRMs miss for DMCs
- Itinerary builder integration (Sembark's core differentiator; we use TravelTree for this)
- Multi-currency quoting (€ vs £ vs $ for different markets)
- Supplier rate card lookup within deal context
- Group size driving automatic capacity checks
- Seasonal availability context in pipeline view

### DMC Quote Blog insight on travel CRM integration
The documented best practice: CRM + booking tool integration should create a closed loop where a confirmed booking automatically updates all downstream CRM records. This is exactly our n8n email-to-deal workflow goal. The security concern (shared PII across systems) is real — our Supabase row-level security handles this.

---

## AI-Built Product Reference Architecture

From the OnboardingHub and Batko.ai case studies, the human-AI build pattern that works:

| Role | Human | Claude Code |
|------|-------|-------------|
| Architecture | Decides schema, component boundaries | Implements from spec |
| UI | Reviews screenshots, approves patterns | Builds components |
| Business logic | Writes acceptance criteria | Codes and tests |
| Debugging | Identifies symptom | Diagnoses and fixes |
| Time split | ~10–15% of total effort | ~85–90% |

**Key success factor from OnboardingHub:** Human acted as PM/architect, not coder. 25–45 hours of human time over 8 weeks = ~3–6h/week. Matches our 6-week roadmap if Patrick reviews output each week rather than coding.

---

## Sources

- https://ir.monday.com/news-and-events/news-releases/news-details/2025/monday-com-Expands-AI-Powered-Agents-CRM-Suite-and-Enterprise-Grade-Capabilities/default.aspx
- https://tech.co/crm-software/monday-crm-review
- https://support.monday.com/hc/en-us/articles/25548698480914-monday-CRM-s-AI-features
- https://support.monday.com/hc/en-us/articles/360013348719-Sales-pipeline-management-with-monday-CRM
- https://support.monday.com/hc/en-us/articles/4405723870994-The-Cards-View
- https://support.monday.com/hc/en-us/articles/31002285812882-monday-CRM-AI-Sales-Agent
- https://monday.com/blog/crm-and-sales/ai-sdr-agent/
- https://monday.com/w/ai
- https://crm.org/news/monday-crm-review
- https://www.folk.app/articles/pipedrive-problems-here-are-3-signs-its-time-to-consider-an-alternative
- https://www.g2.com/products/pipedrive/reviews
- https://www.trustpilot.com/review/pipedrive.com
- https://www.capterra.com/p/132666/Pipedrive/reviews/
- https://world.hey.com/cpinto/building-a-complete-saas-product-with-only-claude-code-cca13895
- https://batko.ai/blog/build-saas-with-claude-code
- https://aiagenteconomy.substack.com/p/claude-built-claude-cowork-in-10
- https://sembark.com/best-travel-crm-software-suite-dmc/
- https://sembark.com/crm-for-dmc/
- https://dmcquote.com/blog/post/travel-crm-systems-best-options-small-agencies
- https://coaxsoft.com/blog/end-to-end-guide-to-destination-management-software
- https://uxplanet.org/ultimate-guide-for-designing-ui-cards-59488a91b44f
- https://bricxlabs.com/blogs/card-ui-design-examples
- https://github.com/BloopAI/vibe-kanban
- https://nextjs.org/blog/agentic-future
