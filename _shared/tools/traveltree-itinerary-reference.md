# TravelTree — Current Itinerary Builder (Manual)

**Saved:** 2026-02-11 | **Source:** Patrick (WhatsApp bookmark)
**Status:** Currently used by Finland DMC for client itineraries

## Links

- **Example itinerary:** https://traveltree.app/en/itinerary_view/?itinerary_id=5cf930808fb0ae61cdcbcd57ab0562a9
- **Platform:** https://traveltree.app

## What It Does

Web-based itinerary builder used by DMCs to create client-facing travel packages. Manual process — each itinerary assembled by hand.

## Example: Järvisydän 3-Day Package

- **Location:** Lake Saimaa, Rantasalmi (Kuru Resort / Järvisydän)
- **Day 1:** Private transfer, Lake Suite check-in, Saimaa Ringed Seal Safari (2.5h), 3-course fire menu dinner
- **Day 2:** Breakfast, stargazing snowshoe hike OR heated sleigh tour
- **Day 3:** Open / departure
- **Contact:** Sebastian Heiskanen, Finland DMC

## Structure / Features

- Tabbed navigation: Overview, Itinerary, Prices, Contacts, Booking
- Day-by-day timeline with nested activities
- Photo galleries per activity
- Google Maps integration
- Dynamic pricing calculator (VAT, quantity, confirmed vs selected)
- Supplier contact info
- Collapsible event details
- Date selector for custom timelines

## Future Opportunity: `/dmc itinerary` Skill

Using the claude-seo skill architecture pattern, build an AI-assisted itinerary builder:

| Component | Implementation |
|-----------|---------------|
| **Orchestrator** | `/dmc itinerary <brief>` — parses client request |
| **Sub-skills** | accommodation, activities, transfers, dining, pricing |
| **Reference files** | Supplier catalog, pricing sheets, seasonal availability, destination knowledge |
| **Subagents** | Source hotels, match activities, calculate logistics in parallel |
| **Output** | Structured itinerary (markdown → could feed into TravelTree or replace it) |
| **Quality gates** | Season validation, drive time checks, minimum standards |

### Prerequisites

Before building this skill:
1. Complete Finland DMC mining sessions (supplier knowledge, pricing patterns)
2. Build supplier/product reference files from real data
3. Test with 5-10 real past itineraries for validation
4. Decide: feed into TravelTree API, or build standalone output?
