# Gemini 2.5 Pro — Arctic Cruises Website V2 UX Audit
**Session:** S222 | **Date:** 2026-04-14 | **Status:** COMPLETE (5/5 questions answered)

---

## Executive Summary
Replace current setup with cohesive, story-driven narrative. Core components: **stylized vertical route map** + **single scrollable visual timeline**. Premium, mobile-first, justifies €2,800pp.

---

## 1. Route Map — Design Decision: VERTICAL (mandatory)

- Mobile-first: vertical aligns with natural scrolling. Horizontal requires awkward side-scrolling.
- Synergy: vertical map placed alongside vertical timeline, stops animate as user scrolls.
- "Subway map" philosophy (reference: Viking, Silversea): shows sequence/connection, not perfect geography.

**Full SVG/CSS spec:**
- `<svg viewBox="0 0 150 800">` with curved `<path>` for route line
- Each stop: `<g class="map-stop" data-day="N">` with two concentric circles + label
- Kuopio (turnaround): larger circle, distinct styling, centered label
- CSS: `position: sticky; top: 100px` — stays on screen while user scrolls itinerary
- Active state (JS): gold fill (#C49A6C), scaled outer ring, bold label
- Route line: `stroke-dasharray: 5 5` for journey feel
- Advanced: animate `stroke-dashoffset` on scroll to draw route in real-time

---

## 2. Itinerary Section — Decision: REPLACE ACCORDION

Accordion is a UX failure for this price point. Replace with single day-by-day vertical timeline.
- Removes confusing "Classic vs. Full Loop" ambiguity
- Scrolling = effortless discovery; clicking accordion = work
- **Industry reference: Hurtigruten** uses sticky map + scrollable day timeline. Proven, high-converting for premium cruise segment.

---

## 3. Return Journey Narrative

**"Return same way" is catastrophic luxury marketing language.**

Decision: Do NOT use two tabs (Outbound/Return). Single continuous Days 1–7 scroll.
- Days 1–4 (Outbound): tone = Discovery & Anticipation
- Day 4–5 (Kuopio): The Pinnacle / urban turning point
- Days 5–7 (Return): tone = Reflection & Immersion — different light, changed perspective

Example headline for Day 6: *"Savonlinna, A Farewell Sunrise"* — morning light reveals details missed on outbound.

---

## 4. Kuopio Treatment — "Urban Heart," NOT Sanctuary Card

Decision: Do NOT use the same sanctuary card format as Järvisydän. Different design treatment.
- Different background color or city-skyline icon vs. nature icon
- Two full day entries:
  - Day 4: Arrival & Urban Exploration — market square, restaurants, city atmosphere
  - Day 5: Puijo Tower & Lakeside Culture — panoramic view, nature-city contrast
- Positions Kuopio as major highlight and narrative turning point, not just another stop

---

## 5. CSS/SVG Map Implementation Spec (developer-ready)

```
Container: position sticky; top: 100px (desktop) | position static (mobile <800px)
SVG: viewBox="0 0 150 800" — vertical orientation
Route line: <path> with gentle curve, stroke-dasharray: 5 5
Stop markers: <g class="map-stop" data-day="N">
  - Outer circle: r=varies (Kuopio largest), fill=white, stroke=--accent
  - Inner dot: r=smaller, fill=--accent (default) → #C49A6C (active)
  - Active: outer ring scales 1.15, inner dot fills gold, label bold
Labels: right-aligned (most) | centered above (Kuopio apex)
Night badges: small pills below overnight stops
Mobile: SVG stacks above timeline, height=auto, non-sticky
Advanced (optional): stroke-dashoffset animation on scroll for route draw-in
```
