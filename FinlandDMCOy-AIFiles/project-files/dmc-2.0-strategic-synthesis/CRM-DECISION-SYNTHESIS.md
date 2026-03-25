# CRM Decision Synthesis: Pipedrive vs Custom Second Brain

**Date:** 2026-03-10
**Research:** 3 Grok deep research rounds + 4 Claude subagents
**Verdict:** BUILD CUSTOM — unanimous across all 4 agents

---

## The One-Sentence Answer

Build custom because it's the ONLY option that solves the team's #1 complaint (data entry) while delivering what they actually want (visual pipeline + daily wins).

---

## Research Summary

### Input
- Grok Round 1: Pipedrive deep dive (15 questions)
- Grok Round 2: Pipedrive emotional appeal + adoption reality (12 questions)
- Grok Round 3: 13 CRM tools compared (travel-specific, AI-first, lightweight)
- Agent 1: UX & Adoption Architect
- Agent 2: Technical Architect
- Agent 3: DMC Operations Specialist
- Agent 4: Change Management

### All 4 Agents Agree: Build Custom

| Agent | Verdict | Key Reason |
|-------|---------|------------|
| UX/Adoption | Build custom | Build FEELINGS first, features second. Morning dashboard = P0 |
| Technical | Build custom (42/60, highest score) | Infrastructure exists. 172h / 6 weeks. €33,650 3-year TCO (cheapest) |
| DMC Ops | Build custom + TravelTree | Don't buy Moonstride. 5 features in priority order. 7-11 weeks total |
| Change Mgmt | Build custom, sell it right | Validate → Educate → Co-create. Temp Kanban week 1. Month 3 checkpoint |

---

## Why NOT Pipedrive (for tiimikeskustelu)

| Pipedrive lupaa | Todellisuus |
|---|---|
| "Vähemmän työtä" | 3-5 manuaalista toimintoa per diili MINIMISSÄÄN |
| "Kaikki yhdessä paikassa" | Ei sesongit, ei itinerarit, ei toimittajat, ei komissiot |
| "AI auttaa" | Perus-AI, ei tunne asiakashistoriaa eikä henkilökohtaista tyyliä |
| "Jaettu postilaatikko" | Vaatii erityiskonfiguraation, ei saumaton |
| "Tiimi käyttää sitä" | 50-70% CRM-käyttöönotoista epäonnistuu. "Sama valitus palaa 3kk jälkeen" |

## Why NOT Moonstride

- €595/kk = €7,140/v (kallis)
- CRM-kerros huonompi kuin meidän email-mined Second Brain
- Tiimi joutuisi syöttämään dataa KAHTEEN järjestelmään
- Operaatiokerros (Phase 5) on rakennettavissa 3-5 viikossa
- Ei M365 shared mailbox -tukea

## Why Custom Wins

| | Pipedrive | Moonstride | Custom |
|---|---|---|---|
| **Manuaalinen syöttö** | 3-5 toimintoa/diili | 2-3 toimintoa/diili | NOLLA |
| **DMC-ominaisuudet** | 0 | Kaikki | Rakennetaan tarpeen mukaan |
| **AI-syvyys** | Perus | Profilointi/chatbot | Claude + full konteksti + tyylisovitus |
| **3v TCO** | €34,780 | €38,260 | **€33,650** (halvin) |
| **Adoptio-riski** | Korkea (data entry) | Keskitaso | **Matala** (järjestelmä toimii ilman käyttäjää) |
| **Valmis käyttöön** | 1 päivä | 1-2 viikkoa | 6 viikkoa (mutta Day 1 -näkymä heti) |

---

## Toteutussuunnitelma (6 viikkoa)

### Viikko 1: "Teidän pipeline, tänään"
- **Päivä 1:** Väliaikainen Kanban Microsoft Plannerissa (10-15 aktiivista diiliä)
- **Päivä 2:** 30min tiimipalaveri — näytä taulu, kerää palaute, selitä suunnitelma
- **Päivät 3-5:** Tiimi korjaa ja täydentää omat diilinsä
- Patrick viesti: "Tässä on näkymänne — tänään. Lopullinen versio päivittyy itsestään."

### Viikko 2-3: Aamudigest + automaattiparsinta
- n8n parsii info@finlanddmc.fi → päivittäinen Teams-viesti joka aamulle
- "3 asiaa tänään: vastaa AHI:lle, seuraa Regentiä, lähetä Intrepid-tarjous"
- **Taikahetki:** Tiimi näkee diilin jota kukaan ei manuaalisesti syöttänyt

### Viikko 3-4: Proposal tracking + Kanban
- SharePoint-jakolinkit tarjouksille → "Asiakas avasi tarjouksesi klo 14:32"
- Ensimmäinen toimiva Kanban-näkymä (Next.js, Supabase Realtime)
- Kortit värikoodattuina: vihreä (ok), keltainen (huomio), punainen (riski)

### Viikko 5-6: AI-suositukset + mobiili
- AI ehdottaa seuraavaa toimenpidettä per diili
- PWA (Progressive Web App) — toimii puhelimesta, offline-tuki
- Stale deal -hälytykset Teamsiin

### Kuukausi 3: Tarkistuspiste
Jos ≥3/5 työntekijää käyttää dashboardia päivittäin → jatketaan
Jos <2/5 → rehellinen palaute + Moonstride varasuunnitelma

---

## Tiimille myyntipuhe (3 askelta)

### 1. VALIDOI (5 min)
"Kuulin teidät. Haluatte nähdä diilit yhdessä paikassa, lopettaa muistinvaraisen seurannan, ja saada järjestelmän joka oikeasti auttaa. Pipedrive on hyvä työkalu — tutkin sen perusteellisesti."

### 2. OPETA (10 min)
"Pipedrive on loistava geneerisille myyntitiimeille. Mutta meillä on sesongit, itinerarit, komissioprosentit, pax-hinnoittelu — mitään näistä Pipedrive ei osaa. Ja vaikka Pipedrive näyttää kauniilta, se vaatii silti manuaalista syöttöä jokaiseen diiliin. 50-70% CRM-käyttöönotoista epäonnistuu juuri tästä syystä."

### 3. LUO YHDESSÄ (20 min)
"Tässä on mitä rakennan — ja haluan teidän panoksenne. Mitä haluatte nähdä aamulla ensimmäisenä? Mikä tekisi tästä työkalun jonka oikeasti avaatte?"

### Henkilökohtaiset kärjet:
- **Liisa:** "Tarkat komissiolaskelmat, sesonkihinnoittelu, toimittajarekisteri — kaikki meidän tarpeisiin räätälöity"
- **Reeta:** "Järjestelmä muistaa jokaisen keskustelun, suositukset, asiakkaan mieltymykset — suhdeäly"
- **Sebastian:** "Nolla lomakkeita. Järjestelmä seuraa sähköposteja automaattisesti. Keskity itinerareihin."
- **Laura:** "Jokainen revisio, jokainen pax-muutos, jokainen toimittajavahvistus — kaikki tallessa"
- **Piia:** "Ammattimainen pipeline-näkymä, asiakaskortit, tarjousten seuranta — rakennettu DMC:lle"

---

## Tekniset avainpäätökset

| Päätös | Valinta | Peruste |
|---|---|---|
| Database | Supabase (3 uutta taulua: deals, deal_activities, deal_stage_history) | Olemassa oleva infra, RLS, Realtime |
| Automaatio | 4 uutta n8n-workflowta | Email→deal, stage auto, stale alerts, proposal tracking |
| Frontend | Next.js (FinnConcierge-pohja), 4 komponenttia | Kanban, deal drawer, dashboard, activity logger |
| Proposal tracking | SharePoint-jakolinkit + Graph API analytics | Ei ulkoista palvelua, M365 jo käytössä |
| Mobiili | PWA (Progressive Web App) | Sama koodipohja, offline, push-ilmoitukset |
| TravelTree | Integraatio (T1+T2 API, ilmainen) | TT = esityskerros, meidän = hinnoittelu + älykkyys |
| Moonstride | EI osta | €7,140/v, CRM huonompi, ops rakennettavissa 3-5vk |
| Pipedrive | EI osta | Ei ratkaise data entry -ongelmaa |

---

## Kustannukset (3 vuotta)

| | Vuosi 1 | Vuosi 2 | Vuosi 3 | 3v yhteensä |
|---|---|---|---|---|
| **Custom** | €18,370 | €7,640 | €7,640 | **€33,650** |
| Pipedrive + AI | €16,180 | €9,300 | €9,300 | €34,780 |
| Moonstride + AI | €15,100 | €11,580 | €11,580 | €38,260 |

Custom on 3 vuodessa halvin JA ainoa joka ratkaisee data entry -ongelman.

---

## Top 10 "varastettavaa ideaa" kaikista CRM-työkaluista

1. **Auto-enrichment + magic fields** (Attio/Folk) → nolla manuaalista kontaktien luontia
2. **Next-activity forcing AI-suosituksilla** (Pipedrive-filosofia AI:lla)
3. **Deal rotting + stale alerts Teamsiin** (HubSpot)
4. **Pax + sesonkihinnoittelulaskuri** (Moonstride)
5. **AI-tarjousdrafti täydellä kontekstilla** (Folk + Claude)
6. **Kanban joka liikkuu automaattisesti sähköpostin perusteella** (Monday + n8n)
7. **Komissio- ja toimittajakirjanpito automaattisesti** (Moonstride)
8. **Trackable proposal -linkit avausilmoituksilla** (Pipedrive Smart Docs → SharePoint)
9. **Mobiili offline-päivitykset** (Pipedrive/Monday)
10. **Self-hosted data layer** (Twenty) → omistetaan kaikki itse

---

## Tiedostot

| Tiedosto | Sisältö |
|---|---|
| [PIPEDRIVE-RESEARCH-BRIEFING.md](FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/PIPEDRIVE-RESEARCH-BRIEFING.md) | Koottu briefing (Grok 1+2+3 + meidän suunnitelmat) |
| [GROK-PROMPT-PIPEDRIVE.md](FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/GROK-PROMPT-PIPEDRIVE.md) | Grok-promptti 1 (Pipedrive deep dive) |
| [GROK-PROMPT-PIPEDRIVE-FOLLOWUP.md](FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/GROK-PROMPT-PIPEDRIVE-FOLLOWUP.md) | Grok-promptti 2 (vetovoima + adoptio) |
| [GROK-PROMPT-CRM-LANDSCAPE.md](FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/GROK-PROMPT-CRM-LANDSCAPE.md) | Grok-promptti 3 (13 CRM-työkalua) |
| [AGENT-1-UX-ADOPTION.md](FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/AGENT-1-UX-ADOPTION.md) | UX & Adoption -analyysi (223 riviä) |
| [AGENT-2-TECHNICAL-ARCHITECT.md](FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/AGENT-2-TECHNICAL-ARCHITECT.md) | Tekninen arkkitehtuuri + TCO (245 riviä) |
| [AGENT-3-DMC-OPERATIONS.md](FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/AGENT-3-DMC-OPERATIONS.md) | DMC-operaatiot + supplier design (270 riviä) |
| [AGENT-4-CHANGE-MANAGEMENT.md](FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/AGENT-4-CHANGE-MANAGEMENT.md) | Muutosjohtaminen + tiimipuhe (235 riviä) |
