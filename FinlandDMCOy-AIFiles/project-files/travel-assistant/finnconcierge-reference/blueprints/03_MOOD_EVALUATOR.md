---
id: BP_03_MOOD_EVALUATOR
title: Mood Evaluator (The Psychologist)
type: Logic
priority: Critical
complexity: L
dependencies: [BP_02_MASTER_AGENT]
tags: [nlp, profiling, sentiment-analysis, async]
context_source: docs/architecture/PROJECT_CONTEXT.md
---

## 1. Purpose & Business Value

Taustaprosessi, joka analysoi asiakkaan viestintää ja päivittää psykologista profiilia (`Mood_Matrix`) reaaliajassa. Ei vastaa asiakkaalle suoraan.

[cite_start]**Business Value:** Mahdollistaa hyper-personoidun myynnin ja estää "tone-deaf" -tilanteet (esim. lisämyynti vihaiselle asiakkaalle) [cite: 6157-6160].

## 2. Agentic Flow (Logic)

* **Trigger:** Event Grid: `USER_MESSAGE_RECEIVED` (Async).

* **Process:**

    1.  **Analyze:** Aja viesti LLM:n läpi "Psychologist"-promptilla.

    2.  **Extract Dimensions:** Arvioi asteikolla 0-100: `Energy`, `Social`, `Luxury`, `Nature`, `Safety`, `Foodie`, `Price`.

    3.  **Detect Tags:** Tunnista avainsanat (esim. "savu" -> `hate_smoke`).

    4.  **Update Profile:** Laske liukuva keskiarvo SQL-kantaan (uusi tieto painottuu).

    5.  **Cluster:** Mäppää käyttäjä lähimpään Arkkityyppiin (esim. `German_Active_Family`).

    6.  **Safety Valve:** IF Sentiment = Negative -> Laske `Patience_Meter`. IF < 30 -> Emit `ALERT_NEGATIVE_MOOD`.

## 3. Data Contracts (Schema Definition)

### [cite_start]Mood Matrix JSON (SQL: Users.profile_meta) [cite: 6159]

```json
{
  "archetype": "German_Active_Family",
  "last_updated": "2025-12-11T12:00:00Z",
  "dimensions": {
    "energy": 70,
    "social_battery": 40,
    "luxury_affinity": 30,
    "nature_rawness": 80,
    "safety_need": 90,
    "foodie_focus": 20,
    "price_sensitivity": 60
  },
  "tags": ["hate_smoke", "love_history"],
  "patience_meter": 90
}
```

## 4. Edge Cases & Resilience

* **Kylmäkäynnistys:** Jos historiaa ei ole, käytä Ingestion-vaiheen dataa (Kansalaisuus + Seurue) oletusarvoina.

* **Lyhyet viestit:** "Ok", "Joo" -> Älä päivitä matriisia drastisesti (Weight: 0.1).

* **Sarkasmi:** Promptin tulee tunnistaa sarkasmi, jotta sentimentti ei vääristy.

## 5. Success Criteria (Sub-Boss Checklist)

- [ ] Async-käsittely ei hidasta Master Agentin vastausta.
- [ ] JSON-arvot pysyvät rajoissa 0-100.
- [ ] Negatiivinen palaute triggeröi hälytyksen Staff Dashboardille.
- [ ] Klusterointi päivittyy dynaamisesti käytöksen muuttuessa.

