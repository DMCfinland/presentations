# Email: Järvisydän IT — API & Integration Inquiry
**Status:** Draft — review before sending
**Sensitivity:** High — organization in fragile state, frame as enabling better guest experience
**Sender:** [Finland DMC staff contact — Patrick to decide who sends this]
**Recipient:** Järvisydän IT contact (name TBD)
**Date:** [Patrick to send after deciding timing]

---

## Suggested approach

Send from a Finland DMC staff member (not Patrick directly), framing it as a guest experience improvement project that benefits Järvisydän. Keep the first email lightweight — just the introduction and two questions. Don't dump all API requirements at once.

**Two-phase communication:**
1. **Email 1 (this draft):** Introduce the project, ask about BookVisit webhook and API documentation.
2. **Email 2 (after IT responds):** Follow up on Oracle Opera API scope based on their response.

---

## Draft Email

**Subject:** Järvisydän guest experience project — quick API question

Hi [Name],

We're working on a guest experience improvement that we think could add real value for Järvisydän visitors — a personalized travel assistant that helps guests discover activities, make plans, and get recommendations during their stay.

Our first step is simple: we'd like to send guests a personalized link in their booking confirmation email so they can access a digital assistant tailored to their visit. We understand booking confirmations currently go out through DUVE based on Opera reservations.

Two quick questions to get started:

1. **BookVisit:** Does BookVisit send a webhook notification when a booking is confirmed? If so, is there documentation we could look at?

2. **API documentation:** Is there documentation available for the Oracle Opera setup at Järvisydän — specifically around reservation events or booking confirmation hooks? We're in early planning and just want to understand what's available before we get further into design.

We know your team has a lot going on right now, and we want to make this as easy as possible on your end. Happy to work at whatever pace makes sense.

Best,
[Sender name]
Finland DMC Oy

---

## What we're NOT asking in email 1

- Full Oracle Opera API access / sandbox environment (save for email 2)
- Booking creation API (this is Phase 3, build trust first)
- Any system changes or integrations (just documentation for now)

---

## What to listen for in their response

| Signal | Meaning |
|--------|---------|
| "BookVisit has webhooks, here's the docs" | Fast path — magic link pipeline doable quickly |
| "BookVisit doesn't do webhooks" | Need alternative (Opera polling or DUVE trigger) |
| "Opera has a REST API, here's documentation" | Green light for Phase 2 Booker Agent |
| "Opera is heavily customized, no external API" | Type B fallback confirmed — staff manually confirms bookings |
| Long response time / no response | Escalate gently via Patrick directly |

---

## Context for Patrick

- DUVE is already sending confirmation emails from Opera — the magic link just needs to be injected into that email
- BookVisit handles activity/restaurant/experience bookings (not room bookings)
- Oracle Opera handles room reservations
- We can build and validate the Travel Assistant without Opera API (manual booking confirmation fallback)
- The most valuable thing this email can return: BookVisit webhook documentation + any indication of Opera API availability

---

*Draft | 2026-02-22 | Session 50*
