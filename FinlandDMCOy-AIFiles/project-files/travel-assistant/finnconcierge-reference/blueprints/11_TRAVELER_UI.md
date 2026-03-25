---
id: BP_11_TRAVELER_UI
title: Traveler PWA (Frontend)
type: UI
priority: High
complexity: M
dependencies: [BP_01_INGESTION, BP_02_MASTER_AGENT]
tags: [nextjs, pwa, brand-engine, mobile-first]
context_source: docs/architecture/PROJECT_CONTEXT.md
---

## 1. Purpose & Business Value

Asiakkaan käyttöliittymä. "Kameleontti"-sovellus, joka latautuu Magic Linkistä ilman asennusta ja mukautuu dynaamisesti brändin ilmeeseen (Järvisydän vs. KonTiki).

[cite_start]**Business Value:** Poistaa käytön esteet ja tuo palvelun asiakkaan taskuun 24/7 [cite: 6196-6209].

## 2. Agentic Flow (Logic)

* **Initialization:**

    1.  Parse URL: `?token=XYZ&tenant=jarvisydan`.

    2.  **Brand Engine:** Hae `tenant_config.json` (värit, logot, fontit).

    3.  **CSS Injection:** Aseta CSS-muuttujat (`--primary-color`, `--font-header`) lennosta.

    4.  **Auth:** Validoi token API:ssa.

* **Views:**

    * **Feed:** "Nyt tapahtuu" -kortti (Contextual Hero) + Sää.

    * **Timeline:** Pystysuuntainen jana (Vahvistetut / Pending / Ehdotukset).

    * **Explore:** Visuaalinen "Netflix"-karuselli Chefin suosituksille.

    * **Chat:** Kelluva overlay (FAB), aina saatavilla.

## 3. Data Contracts (Schema Definition)

### [cite_start]Tenant Config JSON (Frontend Theme) [cite: 6199-6208]

```json
{
  "tenant_id": "jarvisydan",
  "assets": {
    "logo_url": "/assets/js/logo.svg",
    "avatar_url": "/assets/js/host_matti.png"
  },
  "theme": {
    "colors": {
      "primary": "#4A3B2A",
      "accent": "#C5A065",
      "background": "#F5F5F0"
    },
    "fonts": {
      "header": "Playfair Display",
      "body": "Lato"
    },
    "ui_mode": { "radius": "8px" }
  }
}
```

## 4. Edge Cases & Resilience

* **Offline Mode:** Service Worker kätkee staattiset assetit ja viimeisimmän Itinerary-datan ("Offline First").

* **Token Expiry:** Jos token vanhenee, ohjaa "Tilaa uusi linkki" -sivulle (Älä pyydä salasanaa).

* **Huono yhteys:** Skeleton-loaderit datalle, optimoidut kuvat (Next/Image).

## 5. Success Criteria (Sub-Boss Checklist)

- [ ] Lighthouse Performance score > 90.
- [ ] Teemavaihto toimii ilman välkkymistä (FOUC).
- [ ] PWA on asennettavissa ("Add to Home Screen").
- [ ] Chat overlay toimii saumattomasti navigaation päällä.

