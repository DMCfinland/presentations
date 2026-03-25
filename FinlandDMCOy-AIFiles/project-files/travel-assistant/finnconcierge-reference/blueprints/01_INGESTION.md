---
id: BP_01_INGESTION
title: Ingestion & Identity Service
type: Logic
priority: Critical
complexity: M
dependencies: [BP_10_INFRA_SECURITY, BP_07_SHADOW_LEDGER]
tags: [azure-functions, magic-link, onboarding, identity]
context_source: docs/architecture/PROJECT_CONTEXT.md
---

## 1. Purpose & Business Value

Tämä moduuli on järjestelmän "suu". Se ottaa vastaan varausdatan ulkoisesta lähteestä (esim. BookVisit, CRM), luo käyttäjäidentiteetin ja generoi salasanattoman pääsyn ("Magic Link").

**Business Value:** Poistaa lataus- ja kirjautumiskynnyksen ("Zero Friction"). [cite_start]Mahdollistaa "Scrape First, Negotiate Later" -strategian luomalla käyttäjäprofiilin heti ensimmäisestä kontaktista[cite: 6134].

## 2. Agentic Flow (Logic)

Toteutetaan Azure Functionilla (`fn-ingestion`).

* **Trigger:** HTTP Webhook (Partner E-com) TAI Manuaalinen trigger Staff Dashboardilta.

* **Process:**

    1.  **Validate Signature:** Tarkista HMAC-allekirjoitus (varmista lähde).

    2.  **User Resolution:**

        * Query SQL `Users`: `SELECT id FROM Users WHERE email_hash = @hash OR phone_hash = @hash`.

        * IF found: Hae olemassa oleva `user_id`.

        * ELSE: Luo uusi käyttäjä, genero UUID, tallenna.

    3.  **Itinerary Injection:**

        * Muunna saapunut varausdata standardiin `ItineraryItem`-muotoon.

        * Insert SQL `Itinerary`: Status `CONFIRMED`.

    4.  **Session Creation:**

        * Luo JWT-token (claims: `user_id`, `tenant_id`, `exp`).

        * Tallenna sessio Cosmos DB:hen (Hot Storage).

    5.  **Magic Link Generation:**

        * Format: `https://app.finlanddmc.fi/welcome?token={jwt}&tenant={tenant_id}`.

    6.  **Dispatch:** Lähetä SMS/Email (SendGrid/Twilio).

* **Output:** Emit Event Grid: `USER_ONBOARDED` (Payload: `user_id`, `source`).

## 3. Data Contracts (Schema Definition)

### Input Schema (Webhook Payload)

```json
{
  "source": "bookvisit",
  "tenant_id": "jarvisydan",
  "reservation_id": "RES-998877",
  "customer": {
    "first_name": "Matti",
    "last_name": "Meikäläinen",
    "email": "matti@example.com",
    "phone": "+358401234567",
    "language": "fi"
  },
  "stay": {
    "start": "2025-12-24",
    "end": "2025-12-26",
    "unit": "Panorama Suite"
  }
}
```

### Persistence (Azure SQL: Users)

* `user_id` (PK, UUID)
* `tenant_id` (FK, Varchar)
* `email_hash` (Varchar, Indexed)
* `phone_hash` (Varchar, Indexed)
* `created_at` (Timestamp)

## 4. Edge Cases & Resilience

* **Missing Contact Info:** Jos sekä sähköposti että puhelin puuttuvat -> Log Error & Alert Staff (Manuaalinen käsittely).

* **Duplicate Webhook:** Idempotency-tarkistus reservation_id:n perusteella. Älä luo tuplavarausta.

* **API Down:** Jos SQL ei vastaa, puskuroi pyyntö Azure Service Bus -jonoon.

## 5. Success Criteria (Sub-Boss Checklist)

- [ ] Webhook endpoint on suojattu (API Key / HMAC).
- [ ] Käyttäjäduplikaatit estetty (Hash lookup).
- [ ] Magic Link ohjaa oikeaan tenant-näkymään.
- [ ] GDPR: PII-data (Email/Phone) on suojattu/hashattu lokeissa.

