# TravelTree API — Status & Plan

## Contact: Ihor Kucher (TravelTree)
- WhatsApp conversation 2026-02-21
- Call booking: https://meetings-eu1.hubspot.com/ihor-kucher
- Status: Initial answers received. Call pending (after team check on pricing workflow).

## Account Status
- Finland DMC already on **Pro plan** (auto-upgraded from old Agent plan)
- Price locked for 1 year from January 2026
- Pro gives access to API features + priority feature requests

## API Answers from Ihor (2026-02-21)

| # | Feature | Answer | Cost | Available |
|---|---------|--------|------|-----------|
| 1 | Create itinerary via API (send data → get link) | **Yes** | Free setup | NOW — just needs enabling |
| 2 | Read itinerary content via API | **Yes, can build** | Free setup | NOW — just needs enabling |
| 3 | Export component library as data | Paid feature, needs scoping | TBD | Needs call |
| 4 | Pricing via API | Possible, but recommends built-in system | Free (built-in) or paid (API) | Built-in: on roadmap |
| 5 | Update components via API | On dev roadmap, free for Pro | Free | On roadmap (timeline unknown) |
| 6 | Webhooks (client view notifications) | **Not answered** | — | Unknown |
| 7 | Iframe embedding | Not recommended | N/A | Settled — new window + API instead |

## TT Pricing System Upgrade (in testing)
Ihor disclosed upcoming pricing features:
- Season-based pricing per item
- Min/max group size pricing
- Improved accommodation price calculation
- Supplier price list upload + auto-conversion
- Timeline: in testing now, no release date given

## Our Plan

### Phase 1: Mine TT links from emails (NEXT)
- Extract all TravelTree itinerary links from mass-mined emails
- Map: which staff member, which client, which itinerary, which proposal
- Build picture of how TT is actually used before deciding on API integration
- This requires no API access or TT cooperation

### Phase 2: Decide API scope (after mining + team check)
- Check with Laura/Liisa: why is pricing done in email, not TT?
- Based on mining results: what's the real workflow? How central is TT?
- Book call with Ihor once we know what we actually need
- Q1+Q2 (create + read API) are free and ready — low-hanging fruit

### Phase 3: Build integration (after call)
- Start with create + read API (free, available now)
- Evaluate whether TT's new pricing covers DMC needs or if API pricing is needed
- Component export (Q3) only if mining shows we need bulk data

## Open Questions
- [ ] Q6: Does TT send notifications when client views itinerary? (ask on call)
- [ ] Why does the team price in email instead of TT? (ask Laura/Liisa)
- [ ] What does the TT link mining reveal about actual usage patterns?
