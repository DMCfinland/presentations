# System Debt Analysis — Opus Review 7 Preparation
*Sessio 92 | 2026-03-18 | Sonnet 4.6 | Valmistelu (EI itse katsaus)*

---

## Mittausikkuna

**Sessiot analysoitu:** 83–91 (9 sessiota sitten Opus Review #6 / session 82)
**Sessiot joilla täysi YAML-data:** S83, S84, S89, S90, S91 = 5 sessiota (56%)
**Sessiot kompressoitu one-linereiksi (ei YAML):** S85, S85b, S86, S87, S88 = 5 mini/täysiä sessiota (44%)

### Metriikat (YAML-sessiosta laskettuna)

| Metriikka | Arvo | Tavoite | Status |
|-----------|------|---------|--------|
| KB consulted (non-mining, YAML-sessioista: 5/5) | 3/5 = **60%** | >40% | ✅ |
| Patterns harvested (kaikki sessiot joilla YAML) | 3/5 = **60%** | >20% | ✅ |
| Sessiot joilla YAML puuttuu (mittausaukko) | 5/10 = **50%** | 0% | ⚠️ |

**Huomio:** Kompressio s85–88 → one-liners (session 91) tuhosi YAML-blokit. 50% datakato mittauksissa. Opus Review #6:ssa kaikilla sessioilla oli YAML → trendejä ei voi verrata luotettavasti.

---

## TOP 3 Järjestelmävelkaa

Järjestyskriteeri: (1) Vaikutus HIGH/MEDIUM/LOW → (2) Kumuloituminen (sessioita) → (3) Korjaustyö (sessioita)

---

### VELKA 1: CRM Wave 2B Rakenteellinen Jumiutuminen

| Kenttä | Arvo |
|--------|------|
| **Nimi** | CRM Wave 2B Structural Stall |
| **Vaikutus** | HIGH |
| **Kumuloituminen** | ~12 sessiota (s80 → s91) |
| **Korjaustyö** | 1 sessio (päätös) |

**Evidenssi sessionumeroviittauksilla:**
- S89 session_notes: *"DMC CRM Wave 2B: still blocked on Frendy OAuth2."*
- S90 session_notes: *"CRM Wave 2B: blocked on Frendy OAuth2."*
- S91 Current State: *"Blockers: Frendy OAuth2 still pending."*
- S92 Current State: *"Blockers: Frendy OAuth2 still pending (12+ sessions)."*
- CURRENT-STATUS.md Active Deliverables: `[ ] DMC CRM Wave 2B — pre-gates: apply SQL files + test single email + run bulk-embed + Frendy OAuth2 setup` — avoimena sessiosta 79.

**Vaikutusarvio:**
Wave 2B on email pipeline (email → deal automatiikka). Tämä on CRM:n korkein liiketoiminta-arvo -ominaisuus. 12 sessiota jumissa tarkoittaa että CRM ei tuota arvoa Waves 1A/1B:n jälkeen. Lisäksi: jos Wave 2B ei etene, Waves 3-5 (embed, UI, reporting) myös odottavat.

**Miksi rakenteellinen (ei vain kalenteriongelma):**
Frendy OAuth2 on ulkoinen blokkeri. Unilateraalinen polku (mitä voidaan rakentaa ilman Mail.ReadWrite) ei ole dokumentoitu. Jokainen sessio toistaa "waiting on Frendy" ilman vaihtoehtoista skenaariota.

**Ehdotettu korjaus:**
Opus Review 7:ssa: kirjoita eksplisiittisesti mitä CRM:n osista voidaan rakentaa ilman Frendy OAuth2 (Waves 3-5?). Jos vaihtoehtoinen polku olemassa → depriorisoi Wave 2B virallisesti + käynnistä vaihtoehtoinen polku. Jos ei → dokumentoi "Wave 2B on parked, CRM launch goes without email auto-import."

---

### VELKA 2: Cold Start -inflaatio / Kontekstibudjetti

| Kenttä | Arvo |
|--------|------|
| **Nimi** | Cold Start Context Inflation |
| **Vaikutus** | HIGH |
| **Kumuloituminen** | Pysyvä (kasvaa joka sessio) |
| **Korjaustyö** | 3+ sessiota (arkkitehtuurinen muutos) |

**Evidenssi sessionumeroviittauksilla:**
- S89 Cognitive Snapshot: *"Juuri kompressoitiin sessiot 85-88 yksiriveihin. Nyt 102K tokenia — Yellow Zone."* (Session 89 ylitti Yellow Zone kompressiotehtävällä ennen varsinaista työtä.)
- S91 bridge prompt mental_model_anchors: *"Cold Start -inflaatio on suurin yksittäinen järjestelmävelka — ~100K ennen mitään työtä."*
- CLAUDE.md Meta-note: `next_compression: 96` — kompressio aikataulutettu 5 session välein, mutta startup-kustannus kasvaa silti.
- Memory MEMORY.md: *"140K Yellow Zone: At 100-150K tokens → soft warning. At 170K → hard stop."* — threshold asetettu sen takia, että sessiot alkavat ~100K:ssa.

**Vaikutusarvio:**
Session-Bridge Protocol (s89) ratkaisee akuutin ongelman (yksittäiset sessiot jotka ylittyvät) mutta ei rakenteellista syytä. Jokainen sessio lataa:
1. CLAUDE.md (~8K) — kaikki Tier A säännöt
2. CURRENT-STATUS.md (~75K!) — koko Rolling Window + Compressed History + Active Deliverables
3. Memory + system-reminders (~10K)
4. Context Pack warm pack -tiedostot (~5-15K)

CURRENT-STATUS.md 75K on suurin yksittäinen kuorma. Se kasvaa joka sessio kun Rolling Window laajenee. S91 lopetus: 75K lataus joka sessio tarkoittaa että puolet käytettävissä olevasta budjetista on kulutettu ennen ensimmäistäkin käyttäjän viestiä.

**Ehdotettu korjaus:**
Opus Review 7:ssa: arvioi voidaanko CURRENT-STATUS.md jakaa:
- `CURRENT-STATUS-CORE.md` (Meta + Current State + Next Tasks = ~5K, ladataan aina)
- `CURRENT-STATUS-HISTORY.md` (Rolling Window + Compressed History = ~65K, ladataan vain jos tarvitaan)
- `CURRENT-STATUS-DELIVERABLES.md` (Active Deliverables matrix = ~5K, ladataan projektin mukaan)

Tämä voisi pienentää automaattisen latauksen ~75K → ~10K.

---

### VELKA 3: Warm Pack -aktivoinnin Mittausaukko

| Kenttä | Arvo |
|--------|------|
| **Nimi** | Warm Pack Activation Blind Spot |
| **Vaikutus** | MEDIUM |
| **Kumuloituminen** | 10 sessiota (s82 → s92) |
| **Korjaustyö** | 1 sessio (audit) |

**Evidenssi sessionumeroviittauksilla:**
- S82 (Opus Review #6): kaikki warm packit päivitettiin `last_curated: 2026-03-17`. Aktivointiaste ei mitattu tässä katsauksessa.
- S89 patterns_harvested: `[warm-pack-activation-audit]` — audit-metodologia dokumentoitu mutta ei ajettu.
- Memory (session startup): *"⚑ SESSION 110 OPUS REVIEW TASKS: WARM PACK ACTIVATION AUDIT (PWJ-style, session 88)"* — audit siirrettiin s88:aan (ei toteutunut), sitten s110:een, nyt s95:een.
- _index.yaml header: `# USAGE TRACKING: Increment 'uses' and update 'last_used' at session end` — ei ole johdonmukaisesti toteutunut (tarkista alla).

**Warm pack freshness check:**
Kaikki 8 warm packia: `last_curated: 2026-03-17` = 10 sessiota sitten.
Mature phase threshold: >30 sessiota ennen päivitystä. Ei vielä kriittinen — mutta onko sisältö oikeaa?

**Kriittinen kysymys:** Opus Review #6 lisäsi uusia Knowledge Triggers warm packeihin (agentic-coding-patterns, coding-project-preflight, lead-agent-quality-gate). Ovatko ne lauenneet CRM-sessioissa (s85, s88)? Vastausta ei löydy S85–88 one-linereista.

**Vaikutusarvio:**
Jos warm packit eivät aktivoidu, Knowledge Triggers ovat kuolleita linkkejä. Parempi konteksti → parempi ensimmäisen käännöksen laatu → vähemmän iterointia. S82-S92 YAML-sessioissa first_turn_quality: high 4/5 kertaa — voiko tämä olla *despite* toimimattomien warm packien (eli Claude toimii hyvin ilman niitä), vai *because* warm packit toimivat?

**Ehdotettu korjaus:**
Aja warm-pack-activation-audit.md metodologia sessioille 83-91 (non-mining). Laske:
- Aktivoituiko warm pack ID:tä vastaava tieto sessiossa (viittaako session log warm packin tiedostoihin)?
- Verdict: WORKING ≥40% / PARTIAL 20-39% / BROKEN <20%
- Jos PARTIAL/BROKEN: yksi korjaus ennen katsauksen sulkemista.

---

## Neljäs Kandidaatti: Kompressio Tuhoaa YAML-Mittaukset

Tämä on löydetty tässä analyysissa — ei ollut ennakkoon tiedossa.

| Kenttä | Arvo |
|--------|------|
| **Nimi** | Compression-Induced Measurement Blindness |
| **Vaikutus** | MEDIUM |
| **Kumuloituminen** | Rakenteellinen (joka kompressiokierros) |
| **Korjaustyö** | 1 sessio (protokollamuutos) |

**Evidenssi:**
- S91 kompressio: S85–88 YAML-blokit korvattiin one-linereilla. Tämä tuhoaa kb_consulted, patterns_harvested, first_turn_quality -tiedot.
- Vaikutus: Opus Review 7 voi arvioida vain 5/10 sessiota luotettavasti (50% datakato).
- Opus Review #6:ssa kaikki 9 sessiota oli täysin mitattavissa.

**Ehdotettu korjaus:**
Lisää kompressioprotokollaan: ennen one-liner-muunnosta, lisää kompakti YAML-tiivistelmä:
```
S85: kb_consulted:no, harvest:yes(2), cost:~$3, project:crm-build
```
Tämä lisää ~50 merkkiä/sessio one-lineristä — ei merkittävä kustannus, mutta pitää metriikat mitattavana.

**Suositus:** Lisää TOP 3:een tai tee siitä erillinen korjausehdotus Opus Review 7:ssa.

---

## Yhteenveto

| Prioriteetti | Velka | Vaikutus | Sessioita | Korjaus |
|-------------|-------|---------|----------|--------|
| 1 | CRM Wave 2B Structural Stall | HIGH | 12 | Päätös: vaihtoehtoinen polku tai park |
| 2 | Cold Start Context Inflation | HIGH | Pysyvä | CURRENT-STATUS.md jako (~3+ sessiota) |
| 3 | Warm Pack Activation Blind Spot | MEDIUM | 10 | Audit (1 sessio) |
| +bonus | Compression-Induced Measurement Blindness | MEDIUM | Rakenteellinen | Kompressioprotokolla +50 merkkiä/sessio |

*Sessio 92 — Preparation only. Opus Review 7 ~sessio 95.*
