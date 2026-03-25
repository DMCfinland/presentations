---
id: BP_02_MASTER_AGENT
title: Master Agent (Orchestrator)
type: Logic
priority: Critical
complexity: XL
dependencies: [BP_05_RAG_LIBRARIAN, BP_03_MOOD_EVALUATOR, BP_04_SUGGESTION_CHEF]
tags: [openai, orchestration, context-aware, stateful]
context_source: docs/architecture/PROJECT_CONTEXT.md
---

## 1. Purpose & Business Value

Järjestelmän "aivot" ja asiakasrajapinta. [cite_start]Master Agent ylläpitää keskustelun kontekstia, hallitsee brändin äänensävyä (Tone of Voice) ja orkestroi alihankkija-agenttien (Chef, Booker) työtä[cite: 6149].

**Business Value:** Tarjoaa yhtenäisen, turvallisen ja hyper-personoidun kokemuksen ilman hallusinaatioita.

## 2. Agentic Flow (Logic)

* **Trigger:** Event Grid: `CHAT_MESSAGE` tai `GAP_FINDER_CRON`.

* **Process:**

    1.  **Context Rehydration:**

        * Hae Cosmos DB:stä `SessionState` (viimeiset 10 viestiä).

        * Hae SQL:stä `UserProfile` (nimi) ja `Itinerary` (tulevat tapahtumat).

        * Hae `Context Backpack` (lyhytmuisti: mistä juuri puhuttiin).

    2.  **Internal Monologue (Reasoning):**

        * Aja "Chain of Thought": *Tunnista intentio -> Tarkista Mood -> Tarkista Turvallisuus*.

        * *Decision Gate:* Jos aihe on "Safety" (jää/sää) -> Tarkista `SafetyBulletin`. [cite_start]Jos data vanhaa -> `HANDOVER_TO_HUMAN`[cite: 6155].

    3.  **Tool Routing:**

        * `Call_Chef`: Jos käyttäjä pyytää suositusta.

        * `Call_Booker`: Jos käyttäjä haluaa ostaa.

        * `Query_RAG`: Jos kysymys on faktatietoa (aukioloajat).

    4.  **Response Synthesis:**

        * Generoi vastaus käyttäen System Promptia (Brändi: "Savolainen isäntä" vs "Opas").

* **Output:** WebSocket/SignalR viesti käyttäjälle + Event `AGENT_RESPONDED`.

## 3. Data Contracts (Schema Definition)

### Context Backpack (Runtime JSON)

```json
{
  "user_name": "Matti",
  "current_location": "Room 101",
  "active_intent": "planning_dinner",
  "weather_snapshot": { "condition": "Rain", "precip": "3mm" },
  "safety_check": { "ice_thickness": "40cm", "timestamp": "2025-12-11T08:00" }
}
```

### Persistence (Cosmos DB: Sessions)

* `session_id` (PK)
* `messages` (Array: User/Assistant roles)
* `backpack` (JSON)
* `last_active` (Timestamp)

## 4. Edge Cases & Resilience

* **Hallusinaatiot:** System Prompt pakottaa käyttämään työkaluja faktoihin. "If you don't know, ask a human."

* **Kielimuuri:** Kääntää viestit lennosta Staff Dashboardille (FI/EN), mutta vastaa käyttäjälle tämän kielellä.

* **Hätätilanne:** Avainsanat "Apua", "Hätä", "112" ohittavat LLM:n ja laukaisevat FIRE_RED -hälytyksen.

## 5. Success Criteria (Sub-Boss Checklist)

- [ ] System Prompt latautuu dynaamisesti (Tenant Config).
- [ ] Internal Monologue (Reasoning) tallentuu lokeihin debuggausta varten.
- [ ] Turvallisuuskysymykset eivät koskaan perustu arvaukseen.
- [ ] Context Window pysyy hallinnassa (tiivistä vanhat viestit).

