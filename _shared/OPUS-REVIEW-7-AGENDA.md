# Opus Review 7 — Agenda
*Valmisteltu: Sessio 92 | 2026-03-18 | Ajoitettu: ~Sessio 95*
*Tiedosto syötetään suoraan Opus-spawnauspromptiin.*

---

## Meta

```yaml
review_session: ~95
prepared_in: 92
previous_review: session-82 (review-session-80.md)
sessions_to_review: 83–94 (arvio — tarkista sessiosta 95)
model: claude-opus-4-6
scope: Patrick vahvistaa laajuuden ennen spawnausta
```

**Ennakkodatan lähde:** `_shared/SYSTEM-DEBT-ANALYSIS.md` — lue ensin.

**Standardi-osat (aja kaikissa Opus Revieweissä — CLAUDE.md kohdat 1-8):**
Utilization audit, knowledge/noise ratio, pattern quality, contradiction scan, BP file health, warm pack freshness, continuous improvement, cross-pack propagation.

**Session 95 -erityisaiheet (alla):** 3 velka-fokusta + 1 rakennekysymys.

---

## Standardi-osa: Utilization Audit (CLAUDE.md kohta 1)

**Luettavat tiedostot:**
- `~/1658HoldingsOy-AIFiles/CURRENT-STATUS.md` — Rolling Window YAML-blokit sessiot 89–94
- `~/1658HoldingsOy-AIFiles/_archive/` — S83–88 lokit (jos kompressoitu, YAML-yhteenvetoja)
- `~/1658HoldingsOy-AIFiles/_archive/opus-reviews/review-session-80.md` — edellinen katsaus (baseline)

**Mittausaukko-huomio:**
S85–88 kompressoitiin one-linereiksi ilman YAML-metatietoja (löydetty s92 analyysissa). Raportoi erikseen:
- Sessiot joilla täysi YAML-data (kb_consulted + patterns_harvested mitattavissa)
- Sessiot joilla vain one-liner (estimaatti)
- Yhteenlaskettu vs. YAML-only rate — erota nämä selvästi

**Binaarinen hyväksymisehto:**
☐ KB consulted rate (non-mining) ja harvest rate raportoitu MOLEMMILLA tavoilla (YAML-only + estimoitu koko). Yksittäinen luku ilman erottelua = HYLÄTTY.

**Haastava kysymys:**
*"Opus Review #6 (s82) raportoI KB 56% ja harvest 67%. Jos sessio 95:n numerot ovat samaa suuruusluokkaa, mutta 50% datasta on estimoitu — voiko Opus todella sanoa että trendi on 'stable'? Millä luottamustasolla?"*

---

## Aihe 1: CRM Wave 2B — Vaihtoehtoinen Polku tai Virallinen Park

**Konteksti:** Wave 2B (email → deal automatiikka, Mail.ReadWrite + Frendy OAuth2) on ollut blokattu ~12 sessiota (s80–s91). Yksikään sessio ei ole dokumentoinut vaihtoehtoista polkua.

**Luettavat tiedostot:**
1. `~/Desktop/FinnConcierge/BUILD-STATE.md` — Wave-tilanteen kooste
2. `~/Desktop/FinnConcierge/BUILD-ARTIFACTS/email-pipeline-notes.md` — Wave 2A dokumentaatio + Patrick action checklist
3. `~/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/project-files/dmc-secondbrain-crm/BUILD-PLAN-v1.md` — Wave-arkkitehtuuri (jos olemassa)
4. `~/1658HoldingsOy-AIFiles/CURRENT-STATUS.md` — Active Deliverables, Wave status

**Kysymykset Opukselle:**
- Mitkä Waves (3–5) voidaan buildata *ilman* Wave 2B:tä (ilman email-to-deal automatiikkaa)?
- Mikä on CRM:n MVP-arvo ilman email-integraatiota? Riittääkö se launch-kriteeriksi?
- Jos Frendy ei vastaa seuraavan 30 päivän aikana: mitä tehdään?

**Binaarinen hyväksymisehto:**
☐ Opus kirjoittaa yksiselitteisen päätöksen:
*Vaihtoehto A:* "Waves [X, Y] voidaan buildattaa ilman Mail.ReadWrite. Vaihtoehtoinen etenemispolku: [konkreettinen ensimmäinen askel]."
*TAI Vaihtoehto B:* "Wave 2B parkataan virallisesti. CRM launch goes without email auto-import. Uudelleenarviointi: [päivämäärä/triggeri]."

Epämääräinen "odota Frendyä" = HYLÄTTY.

**Haastava kysymys:**
*"Jos Wave 2B ei koskaan valmistu (Frendy vaihtaa järjestelmää, OAuth2 ei koskaan avaudu) — onko CRM silti 10x parempi kuin nykyinen Excel-pohjainen seuranta? Jos kyllä: miksi se ei ole jo live ilman email-automatiikkaa?"*

---

## Aihe 2: Cold Start -inflaatio — Arkkitehtuuripäätös

**Konteksti:** CURRENT-STATUS.md on 75K tokenia. Se ladataan joka sessio automaattisesti. Sessio 89 ylitti Yellow Zone (102K) pelkällä kompressiotehtävällä ennen varsinaista työtä. Session-Bridge Protocol on akuutin ongelman korjaus mutta ei rakenteellinen ratkaisu.

**Luettavat tiedostot:**
1. `~/1658HoldingsOy-AIFiles/CURRENT-STATUS.md` — tiedoston koko + rakenne (Meta + Current State + Rolling Window + Compressed History + Active Deliverables)
2. `~/1658HoldingsOy-AIFiles/CLAUDE.md` — Session Start protocol (kohta "Session Start")
3. `~/1658HoldingsOy-AIFiles/_shared/best-practices/session-bridge-protocol.md` — akuutin ongelman korjaus
4. `~/1658HoldingsOy-AIFiles/_shared/warm-packs.md` — Context Pack sisältö

**Kysymykset Opukselle:**
- Mikä osa CURRENT-STATUS.md:stä on oikeasti tarpeen joka sessiossa? (Meta + Current State = ~5K vs. koko 75K)
- Onko Active Deliverables -lista (50+ riviä) tarpeellinen startup-kontekstissa vai riittäisikö "top 3 open items"?
- Voidaanko Rolling Window ja Compressed History lazy-ladata (vain kun tarvitaan)?

**Binaarinen hyväksymisehto:**
☐ Opus tekee yhden konkreettisen ehdotuksen joka *voidaan toteuttaa 1 sessiossa* ja *pienentää startup-tokenia ≥30%*.
☐ Ehdotus on arkkitehtuurimuutos (tiedostojako, protokollamuutos) — ei vain "kompaktoi enemmän."
☐ Patrick on kuullut ehdotuksen ja joko hyväksynyt tai hylännyt perusteluineen.

**Haastava kysymys:**
*"Rolling Window sisältää sessiot 80-91 täysinä logeina. CLAUDE.md sanoo 'compress every 5 sessions.' Mutta Opus Review käyttää näitä logeja YAML-metriikoihin. Onko kompressio-aikataulutus (every 5) ristiriidassa Opus Review -tarpeen (kaikki YAML-blokit luettavissa) kanssa? Onko ratkaisu: kompressio tallentaa YAML-blokit erikseen ennen one-lineria?"*

---

## Aihe 3: Warm Pack -aktivointiaudit — Ensimmäinen Toteutus

**Konteksti:** Warm pack activation audit on ollut suunniteltuna mutta ei koskaan ajettu. Metodologia dokumentoitu s89:ssä (warm-pack-activation-audit.md). Viimeksi siirretty: s88 → s110 → nyt s95. Tiedämme metriikat (KB consulted %, harvest %) mutta emme tiedä *miksi* ne ovat sitä mitä ovat (warm packit toimivat vai Claude toimii ilman niitä?).

**Luettavat tiedostot:**
1. `~/1658HoldingsOy-AIFiles/_shared/best-practices/warm-pack-activation-audit.md` — metodologia (jos olemassa; jos ei, toteuta MEMORY.md:n protokollan mukaan)
2. `~/1658HoldingsOy-AIFiles/_shared/warm-packs.md` — kaikki 8 warm packia, Knowledge Triggers
3. `~/1658HoldingsOy-AIFiles/CURRENT-STATUS.md` — Rolling Window session logit (warm pack viittaukset)
4. `~/1658HoldingsOy-AIFiles/_archive/opus-reviews/review-session-80.md` — edellinen katsaus (cross-pack propagation actions)

**Audit-metodologia (suoraan MEMORY.md:stä):**
*"Scan session logs 83-94 (non-mining only). 'Activation confirmed' = session log references a file that is in the warm pack but NOT in the Context Pack explicitly — OR warm pack trigger language appears in session work. Exclude sessions with custom prompts that listed all files explicitly."*

**Output-muoto:**
```
Session count: N
Activations confirmed: N
Rate: N%
Verdict: WORKING ≥40% / PARTIAL 20-39% / BROKEN <20%
```

**Binaarinen hyväksymisehto:**
☐ Rate laskettu ja verdict annettu (WORKING/PARTIAL/BROKEN).
☐ Jos PARTIAL tai BROKEN: yksi konkreettinen korjaus toteutettu ennen katsauksen sulkemista.
☐ Jos BROKEN kahdessa peräkkäisessä katsauksessa: warm pack -järjestelmä ehdotetaan eläköitäväksi ja Knowledge Triggers siirretäisiin CLAUDE.md Tier A:han — Patrick päättää.

**Haastava kysymys:**
*"First_turn_quality on high 4/5 mitattavassa sessiossa. Jos warm packit eivät aktivoidu (BROKEN verdict) mutta laatu on korkea — todistaa tämä että warm packit ovat tarpeettomat? Vai todistaa se, että Claude toimii hyvin perustiedoilla mutta tekisi parempaa työtä warm packien kanssa? Miten erotat nämä kaksi ilman A/B-testiä?"*

---

## Standardi-osa: Contradiction Scan (CLAUDE.md kohta 4 — PAKOLLINEN)

**Huomio s92 analyysista:**
Seuraavat uudet patternt lisätty s82:n jälkeen — tarkista ovatko ne ristiriidassa olemassa olevien kanssa:
- `session-bridge-protocol.md` (s89) — "140K hard stop" vs. CLAUDE.md "170K hard stop"? Tarkista yhtenäisyys.
- `pwj-theater-vs-real-execution.md` (s89) — "same-model Judge = theater" vs. CLAUDE.md PWJ-kuvaus. Päivitetty?
- `warm-pack-activation-audit.md` (s89) — metodologia vs. CLAUDE.md Opus Review kohta 6. Ristiriita?

**Binaarinen hyväksymisehto:**
☐ Contradiction scan tehty kaikille s82:n jälkeen lisätyille patterneille.
☐ Jokainen ristiriita on joko poistettu tai dokumentoitu perusteluineen.

---

## Standardi-osa: BP File Health (CLAUDE.md kohta 5)

**Erityinen tarkistus s92 löydöstä:**
_index.yaml:n `uses`-laskurit ei ole johdonmukaisesti päivitetty (havaittu: last_updated: session-60). Tarkista onko s83–91 käytöt kirjattu.

**Luettava:** `~/1658HoldingsOy-AIFiles/_shared/best-practices/_index.yaml`

**Binaarinen hyväksymisehto:**
☐ Tiedostot joilla `uses: 0` viimeisen 12 session aikana: lueteltu ja Patrick-päätös pydetty (archive/keep).
☐ `_index.yaml` `last_updated` päivitetty sessioon 95.

---

## Spawn Prompt -pohja (Sessio ~95)

> **⚠️ PÄIVITETTY s93:ssa (2026-03-19):** CURRENT-STATUS.md on refaktoroitu 3-tiedostoksi.
> Rolling Window on nyt **SESSION-LOG.md**:ssä, arkisto **SESSION-ARCHIVE.md**:ssä.
> Vanha spawn prompt (s92) olisi lukenut tyhjää 77-rivin CORE-tiedostoa ja menettänyt 10 sessiota mittausdataa.

```
Sinä olet Opus 4.6. Suorita Opus Review 7 järjestelmälle.
Katsausikkuna: sessiot 83–[current-1].

⚠️ ARKKITEHTUURIMUUTOS S93: CURRENT-STATUS.md on nyt 77-rivin CORE-tiedosto.
Lue SESSION-LOG.md Rolling Windowia varten. Lue SESSION-ARCHIVE.md metriikaviittauksia varten.

Lue JÄRJESTYKSESSÄ — älä kirjoita mitään ennen kaikkien lukemista:
1. ~/1658HoldingsOy-AIFiles/_shared/OPUS-REVIEW-7-CONTEXT.md   ← ENSIN (s92 state of union)
2. ~/1658HoldingsOy-AIFiles/_shared/SYSTEM-DEBT-ANALYSIS.md   (3 velka-analyysia)
3. ~/1658HoldingsOy-AIFiles/_shared/OPUS-REVIEW-7-AGENDA.md   (tämä tiedosto — erityisaiheet)
4. ~/1658HoldingsOy-AIFiles/SESSION-LOG.md                    ← Rolling Window (s89-92B YAML-blokit)
5. ~/1658HoldingsOy-AIFiles/SESSION-ARCHIVE.md                ← Sessiot 79-88 inline-metriikat
6. ~/1658HoldingsOy-AIFiles/CURRENT-STATUS.md                 (CORE: Meta + Current State)
7. ~/1658HoldingsOy-AIFiles/_archive/opus-reviews/review-session-80.md  (baseline)
8. ~/1658HoldingsOy-AIFiles/CLAUDE.md                         (Opus Review -kohdat 1-8)
9. ~/1658HoldingsOy-AIFiles/_shared/best-practices/_index.yaml
10. ~/1658HoldingsOy-AIFiles/_shared/warm-packs.md

MITTAUSOHJE (Session Archive -metriikat):
SESSION-ARCHIVE.md käyttää inline-formaattia: S{N} ({date}) kb:{y/n} harvest:{y/n} cost:{~$X} tier:{1-3} value:{~€Y} — {kuvaus}
Sessiot 79-88: metriikat luettavissa suoraan. Sessiot 1-78: ?-merkki = data ei saatavilla.
Laske KB-rate ja harvest-rate ERIKSEEN: (a) YAML-only sessiot 89-94, (b) estimoitu kaikki 83-94.

Toteuta kaikki standardi-osat (1-8) JA kolme erityisaihetta.
Kirjoita löydökset: ~/1658HoldingsOy-AIFiles/_archive/opus-reviews/review-session-95.md
Toteuta kaikki muutokset välittömästi (contradiction scan + cross-pack propagation = PAKOLLISIA).

Patrick vahvistaa laajuuden ennen spawnausta.

S93 AIHE 4 (lisätty s93 context surgery jälkeen):
CURRENT-STATUS.md 3-tiedostoarkkitehtuuri on nyt live (s93). Tarkista:
- Onko CLAUDE.md:n Session Start protocol synkronoitu uuden rakenteen kanssa?
- Onko startup hook päivitetty lataamaan CORE-tiedosto, ei 900-rivin vanhaa versiota?
- Onko SESSION-ARCHIVE.md:n inline YAML -format dokumentoitu CLAUDE.md:n kompressio-ohjeessa?
Binaarinen ehto: ☐ Kaikki kolme löydöstä tarkistettu, mahdolliset ristiriidat korjattu.
```

---

*Valmisteltu: Sessio 92 | Päivitetty: Sessio 93 | Sonnet 4.6 | 2026-03-19*
*Seuraava vaihe: ~Sessio 95 — Opus 4.6 spawn + Patrick scope-vahvistus*
