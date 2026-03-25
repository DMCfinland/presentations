---
id: BP_07_SHADOW_LEDGER
title: Shadow Ledger & Commission Engine
type: Data
priority: High
complexity: M
dependencies: [BP_06_BOOKER_AGENT, BP_10_INFRA_SECURITY]
tags: [sql, finance, transactions, audit]
context_source: docs/architecture/PROJECT_CONTEXT.md
---

## 1. Purpose & Business Value

Järjestelmän taloudellinen selkäranka. Kirjaa kaikki transaktiot (API, Manuaali, Affiliate) yhteen paikkaan provisiolaskutusta varten, vaikka raha liikkuisi sovelluksen ulkopuolella.

[cite_start]**Business Value:** Varmistaa tulovirran (provisiot) ja mahdollistaa tarkan raportoinnin "Harmaan talouden" estämiseksi [cite: 6170-6179].

## 2. Agentic Flow (Logic)

* **Trigger:** Booker Agentin funktiot (`create_booking`, `update_status`).

* **Process:**

    1.  **Contract Lookup:** Hae `Contracts`-taulusta partnerin provisiosäännöt (Tuote-erityinen > Kausi > Partneri oletus).

    2.  **Calculation:** Laske `receivable_amount` (Myyntihinta * Provisio %).

    3.  **Insert:** Kirjaa transaktio `Shadow_Ledger`-tauluun.

    4.  **Status Handling:**

        * API -> `CONFIRMED`

        * Manual -> `PENDING_PARTNER`

        * Affiliate -> `REFERRED`

* **Output:** Transaktio-ID.

## 3. Data Contracts (Schema Definition)

### SQL Table: Shadow_Ledger

| Column | Type | Notes |
| :--- | :--- | :--- |
| `transaction_id` | UUID (PK) | |
| `booking_ref` | VARCHAR | Linkki Itineraryyn |
| `provider_id` | UUID (FK) | Linkki Contracts-tauluun |
| `flow_type` | ENUM | 'API', 'MANUAL', 'AFFILIATE' |
| `status` | ENUM | 'PENDING', 'CONFIRMED', 'VOIDED', 'REFERRED' |
| `total_amount` | DECIMAL(10,2) | Asiakashinta |
| `commission_pct` | DECIMAL(5,4) | esim. 0.1500 |
| `receivable_amount` | DECIMAL(10,2) | Laskutettava osuus |
| `created_at` | DATETIME | |

## 4. Edge Cases & Resilience

* **Decimal Types:** Käytä aina `DECIMAL` rahasummille, ei koskaan `FLOAT`.

* **Audit Trail:** Taulua ei saa koskaan tyhjentää (DELETE). Peruutukset hoidetaan vastakirjauksella tai statuksella `VOIDED`.

* **Orvot transaktiot:** FK-rajoitteet estävät kirjaukset olemattomille partnereille.

## 5. Success Criteria (Sub-Boss Checklist)

- [ ] Provisiolaskenta noudattaa "Waterfall"-logiikkaa (Specific -> General).
- [ ] Affiliate-linkkien klikkaukset kirjautuvat `REFERRED`-tilaan.
- [ ] ACID-transaktiot varmistavat datan eheyden.

