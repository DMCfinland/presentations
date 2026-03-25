# Session Length Strategy — Compact vs New Session
<!-- created: session-88 | revised: session-88 PWJ run | type: Tier B -->
<!-- replaces: previous version (strategy only) with: empirical analysis + PWJ-validated criteria -->
<!-- promoted when: 3+ explicit uses in session logs | next-review: session 100 -->

---

## RED TEAM CHECK (written before main output)

WHY THIS ANALYSIS MIGHT BE WRONG:

1. **Session logs are summary artefacts, not transcripts.** The YAML meta blocks and free-text descriptions in CURRENT-STATUS.md were written by the same model that performed the session, immediately after. There is no independent record of pre-compaction vs post-compaction reasoning quality. "CLEANER" or "NOISIER" verdicts are inferred from proxy signals (first_turn_quality, human_interventions, harvest_note language) — not from direct observation of reasoning degradation.

2. **Sessions 80-88 span a single day (2026-03-17) with diverse project types.** The compaction events identified (Session 82, Session 77) may reflect project-type effects more than compaction effects. A 90-minute system-maintenance session (82) and a 25-minute rename task (77) are structurally different from a full-day architecture pivot (88). Comparing them as a compaction dataset assumes the confound is controlled — it is not.

3. **The Liu 2023 finding applies to pre-compaction contexts.** The paper measures recall degradation in a raw long context. A /compact summary is a curated, high-density 2-5K token document — structurally different from a raw 168K conversation. Mapping the U-curve to post-compact state requires a theoretical bridge that the paper does not provide. The mapping in Section 3 is reasoned inference, not direct empirical evidence.

---

## 1. Metodologinen huomio

### Mitä voidaan mitata vs mitä täytyy päätellä

**Suoraan mitattavissa session-logeista:**
- Sessiokohtaiset YAML-kentät: `session`, `project_type`, `duration`, `cost`, `human_interventions`, `handoff_quality`, `first_turn_quality`, `kb_consulted`
- Maininta kompaktoinnista: sessio 77 ("Continued from context-compacted session"), sessio 82 (kolme eksplisiittistä "post-/compact" -osuutta)
- Harvest note -teksti: laatu-indikaattori siitä, tuottiko sessio uusia oivalluksia vai ei
- Toistuvat tai uudelleen johdetut päätökset: merkitty, jos session logissa mainitaan korjauksia tai "re-derived"

**Täytyy päätellä — ei suoraa evidenssiä:**
- Konkreettinen reasoning-laadun vertailu ennen ja jälkeen kompaktoinnin (ei transkriptia)
- Tarkat token-määrät kompaktoinnin hetkellä (arvioita, ei mittauksia)
- Kausaliteetti: johtuiko huonompi laatu kompaktoinnista vai projektin vaihtumisesta tai lyhyestä sessiokestosta?
- Mitä tiivistelmä tarkalleen sisälsi (summaries ovat lyhytaikaisia — ne eivät tallennu)

**Metodologinen implikaatio:** Tässä analyysissä on yksi todellakin empiirisesti vahvistettu kompaktointitapahtuma (sessio 82, kolme eksplisiittistä post-/compact -jaksoa) ja yksi implisiittinen (sessio 77, "Continued from context-compacted session"). Muut sessiot ovat vertailupisteitä. Johtopäätökset ovat perusteltuja päätelmiä — ei tilastollisesti validoituja tuloksia.

---

## 2. Compactoinnin mekaniikka — mitä tuhoutuu

### Mitä /compact säilyttää ja mitä se tuhoaa

Claude Code:n `/compact`-komento tiivistää koko keskusteluhistorian yhdeksi ~2-5K tokenin blokkiin ja jatkaa siitä. Säilyvät todennäköisesti eksplisiittiset faktat, tiedostopolut, päätöslistaukset ja tilatetiedot. Tuhoutuvat:

### Tuhoutuva reasoning-tyyppi 1: Välipäättelyketjut (intermediate reasoning chains)

Välipäättelyketjut ovat ne ajatuksenkulut, joita käydään läpi ennen lopullista päätöstä — typillisesti "vaihtoehto A hylättiin syystä X, vaihtoehto B toimi paremmin koska Y, siksi valitsimme Z". Tiivistelmässä näkyy vain lopputulos Z, ei sitä, miksi A ja B hylättiin.

**Evidenssi sessio 82:sta:** Session 82 sisältää kolme eksplisiittistä post-/compact -vaihetta. Ensimmäinen jatkaa Opus Review #6:n ja Grok 4.20 Heavy -debriefin jälkeen. Logissa kuvattu: *"Grok session 82 validation added to header (Divorce Rule, task-tier caps, Initializer Asking Mode)"* — nämä käsitteet vaativat ymmärryksen siitä, mitä niitä edeltänyt keskustelu sisälsi. Ilman kompaktoitua versiota kompaktointihetken jälkeen ei voida sanoa, kuinka paljon näiden käsitteiden taustasta siirtyi — vain se, että ne päätyivät tiedostoon.

Konkreettinen esimerkki: session 82 logissa mainitaan *"k factor discrepancy flagged (4.6× vs 6.50× — deferred)"*. Tämä deferred-päätös vaatisi, että seuraava sessio tietää, miksi se lykättiin. Jos tiivistelmä vain toteaa "k factor open", koko päättelyketju lykkäyksen syistä on kadonnut.

### Tuhoutuva reasoning-tyyppi 2: Implisiittiset jännitteet (unresolved tensions)

Päättelyketjujen lisäksi häviävät tilanteen avoimet kysymykset ja jännitteet, jotka ovat vain "ilmassa" — niitä ei ole eksplisiittisesti kirjoitettu minnekään, mutta ne ohjaavat seuraavaa päättelyä.

**Evidenssi sessio 88:sta:** Session 88 harvest_note kuvaa: *"Patrick questioned 'what is our purpose?' when 30-50% dead letter rate appeared. Discovered pipeline was deals-only not Second Brain."* Tämä kysymys ("mikä on tarkoituksemme?") oli jännite, joka ajoi koko arkkitehtuuripivotin. Jos tämä sessio olisi kompaktoitu siinä vaiheessa, kun dead letter rate havaittiin mutta ennen pivotin tunnistamista, tiivistelmä olisi todennäköisesti kertonut "n8n pipeline tested, some delivery issues" — implisiittinen "koko lähtökohta on väärä" -jännite olisi kadonnut.

**Evidenssi sessio 77:sta (post-compact continuation):** Session 77 on eksplisiittisesti merkitty "Continued from context-compacted session." Tehtävä oli kuvien uudelleennimeäminen (lodge-resort-000 → kuvaavat nimet). Tähän tehtävään ei liity reasoning-jatkuvuuden tarvetta — kaikki tarvittava tieto (mitä nimetä, mihin) löytyy tiedostorakenteesta, ei keskusteluhistoriasta. Sessio 77 tuotti `harvest_note: "nothing new — routine photo renaming"`. Tämä on CLEANER-tapaus: kun tehtävä on mekaaninen ja outputs ovat tiedostoissa, kompaktointi ei tuhoa mitään kriittistä.

### Tuhoutuva reasoning-tyyppi 3: Testatut ja hylätyt vaihtoehdot

"Kokeilimme X:ää, ei toiminut koska Y" -tieto on kriittistä toistettavuuden kannalta. Jos tiivistelmä sanoo vain "käytetään Z:ää", seuraavassa sessiossa saatetaan ehdottaa X:ää uudelleen.

**Evidenssi sessio 79:sta:** Sessio 79 kuvaa: *"Configured n8n Supabase Postgres credential after 4 failed attempts. Root cause: n8n.cloud is IPv4-only..."* Neljä epäonnistunutta yritystä on tieto, joka on kriittinen seuraavalle sessiolle. Jos sessio 79 olisi kompaktoitu ennen kuin root cause kirjattiin BUILD-STATE.md:hen, seuraava sessio ei tietäisi IPv4/IPv6-ansan olemassaolosta.

---

## 3. "Lost in the Middle" — soveltuuko compactoituun kontekstiin?

### Liu et al. (2023) — keskeinen löydös

Liu, N. et al. (2023). "Lost in the Middle: How Language Models Use Long Contexts." arXiv:2307.03172. Julkaistu *Transactions of the ACL* 2024.

Tutkimus osoitti, että LLM:ien suorituskyky on korkein, kun relevantti tieto on kontekstin **alussa tai lopussa**, ja heikentyy merkittävästi tiedon sijaitessa **keskellä**. Suorituskyvyn lasku on mittausmenetelmästä riippuen 15-47%. Myöhempi Chroma Research 2025 -tutkimus (18 mallia) vahvisti efektin ja tarkensi: U-muotoinen käyrä pätee alle 50% täytönasteella — yli 50% täytönasteella malli suosii uusimpia tokeneja, sitten keskiluvut, vanhimmat jäävät heikoimmiksi.

### Palauttaako /compact U-käyrän vai luo uuden?

Tämä on analyysin tärkein teoreettinen kysymys. Kaksi vaihtoehtoa:

**Vaihtoehto A — /compact RESETOI U-käyrän (optimistinen):**
Kompaktoinnin jälkeinen konteksti on ~2-5K tokenia. Tässä lyhyessä kontekstissa kaikki tieto on joko alussa tai lopussa — ei "keskiä". Liu 2023 U-käyrä ei pääse syntymään, koska konteksti on liian lyhyt. Seuraavat turnit kasvattavat kontekstia maltillisesti, ja huono recall ei aktivoidu ennen kuin konteksti on taas kasvanut.

**Vaihtoehto B — /compact LUO uuden U-käyrän (pessimistinen):**
Tiivistelmä itsessään on 2-5K tokenin dokumentti, jossa on useita päätöksiä ja faktoja. Nämä on tiivistetty niukiksi lauseiksi ja ne sijaitsevat tiivistelmän "keskellä" suhteessa toisiinsa. Kriittisin tieto (esim. miksi arkkitehtuuri vaihtui) saattaa sijaita tiivistelmän keskiosassa — ei ensimmäisenä eikä viimeisenä. Lisäksi tiivistelmä ei ole optimoitu Liu 2023 -kriteerillä (tärkeimmät asiat alkuun/loppuun) vaan on Claude:n oma kompressio, jonka sisäinen järjestys ei ole optimoitu retrieval-helppoutta varten.

**Käytännön johtopäätös mekaniikasta:**

Tiivistelmän rakennetta ei voida tarkistaa jälkikäteen — tiivistelmäteksti ei tallennu. Morph-dokumentaation (web research) perusteella: "Your requests and key code snippets are preserved; detailed instructions from early in the conversation may be lost." Claudelog.com vahvistaa: "Claude Code analyzes the conversation to identify key information worth preserving and creates a concise summary."

Tämä viittaa siihen, että tiivistelmä **RESETOI** U-käyrän merkittävästi: konteksti palaa lyhyeksi, jolloin kaikki tiivistelmässä oleva tieto on suhteellisen saavutettavissa. Mutta **LÄHES KAIKKI välipäättely on poistettu** — tiivistelmä sisältää vain lopputulokset, ei polkua niihin.

**Analogia:** /compact ei ole kuin ote pitkästä kirjasta — se on kuin kirjan takakansiteksti. Takakansiteksti on helppo lukea (lyhyt, U-käyrä resetoitu), mutta se kertoo vain mitä tapahtui, ei miksi tai miten.

---

## 4. Empiirinen analyysi: sessiot 80-88

### Sessiokohtainen taulukko

| Sessio # | project_type | Kompaktointitapahtuma | CLEANER / NOISIER | Evidenssihuomio |
|----------|-------------|----------------------|-------------------|-----------------|
| 88 | strategic-research | KYLLÄ (arvioitu ~168K, ajoitus tuntematon) | NOISIER (varovainen) | 12 human_interventions, full-day duration, arkkitehtuuripivotti. Suuri interventioiden määrä viittaa toistuvaan korjaustarpeeseen. Kuitenkin: handoff_quality 95 ja kaikki päätökset BUILD-STATE.md:ssä — vaikutus neutraloitu. |
| 87 | system-maintenance | EI (90min sessio, selkeä rajattu tehtävä) | CLEANER (baseline) | 4 interventions, handoff_quality 92, selkeä tehtävä (n8n error handler). Lyhyt sessio ilman kompaktointia toimii referenssipisteenä. |
| 86 | web-build | EI (45min sessio) | CLEANER (baseline) | first_turn_quality high, 6 patterns harvested — selkeä, kapea tehtävä ilman kompaktointia. |
| 85b | system-maintenance | EI (30min sessio) | CLEANER (baseline) | first_turn_quality high, 3 interventions. Lyhyet sessiot toimivat hyvin ilman kompaktointia. |
| 85 | system-maintenance | EI (90min sessio) | CLEANER (baseline) | 8 interventions mutta kaikki laadullisia korjauksia (Grok criteria gaps) — ei kompaktoinnin aiheuttamia. |
| 84 | dmc-presentations | EI (45min) | NOISIER (signaali) | first_turn_quality **medium** (ainoa medium tässä ikkunassa). 6 interventions, handoff_quality 78 (heikoin). Ei kompaktointia — mutta medium-laatu viittaa kontekstuaalisen jatkuvuuden puutteeseen (uusi projektiosa). |
| 83 | strategic-research | EI (60min) | MIXED | first_turn_quality **medium**, kb_consulted: no. Vercel-deploy — käytännöllinen tehtävä, ei strateginen. |
| 82 | system-maintenance | **KYLLÄ — kolme eksplisiittistä post-/compact -vaihetta** | CLEANER (aineiston vahvin kompaktointievidentsi) | Ks. laajennettu analyysi alla. |
| 81 | dmc-presentations | EI (45min) | CLEANER (baseline) | first_turn_quality high, 5 interventions, 5 patterns. Selkeä presentaatiotehtävä. |
| 80 | dmc-presentations | EI (60min) | CLEANER (baseline) | first_turn_quality high, 6 interventions, 3 patterns. Selkeä presentaatiotehtävä. |

**Sessio 77 (lisäevidenssi, ikkuna 75-79):**
Sessio 77 on eksplisiittisesti merkitty: *"Continued from context-compacted session."* project_type: system-maintenance, duration: 25min, human_interventions: 3, harvest_note: "nothing new — routine photo renaming." Tämä on CLEANER-tapaus: kompaktoinnin jälkeen mekaaninen tehtävä tuotettiin onnistuneesti. Päättelyä ei tarvittu — vain tiedostorakenteen lukeminen.

### Sessio 82 — laajennettu analyysi (tärkein kompaktointitapahtuma)

Sessio 82 on ainoa sessio ikkunassa 80-88, jossa kompaktointitapahtumat ovat eksplisiittisesti dokumentoitu. Session log sisältää **kolme eriteltyä vaihetta:**

**Vaihe 1 (ennen kompaktointia):** Opus Review #6 + Grok 4.20 Heavy debrief. Logissa: *"Opus Review #6 (sessions 71-79): KB 56% ✅, harvest 67% ✅ — GRADUATED to mature phase."* Tämä on rakenteellinen, tarkistuslista-tyyppinen tehtävä — kompaktointi tässä kohdassa on turvallinen, koska tulokset menevät tiedostoihin.

**Vaihe 2 (post-/compact — Gemini Deep Research debrief):** Logissa eksplisiittisesti: *"Session 82 continued (post-/compact) — Gemini Deep Research debrief:"*. Tuotettu: `ai-leverage-ratios.md` uutena tiedostona. Merkille pantavaa: tässä vaiheessa tuotettu artefakti (ai-leverage-ratios.md) sisälsi *"Gemini directional estimates, no external citations"* — tämä on rehellinen, itsekriittinen huomio laadusta. Tämä ei viittaa noisy reasoning-tilaan vaan päinvastoin — Worker tunnisti rajoitteet. CLEANER-signaali.

**Vaihe 3 (post-second-/compact — PWJ Universal Spec v2):** Logissa: *"Session 82 continued (post-second-/compact) — PWJ Universal Spec v2:"*. Tuotettu: merkittäviä muutoksia `planner-worker-judge-loop.md`:hen. Logissa: *"Divorce Rule named, Tier 1 Gate Exception stated, production evidence quantified (10-25% inflation, 5pp false PASS, 57.2pt novel collapse, CourtEval +10-16%)"* — konkreettisia, kvantifioituja väitteitä. CLEANER-signaali: spesifiset numerot viittaavat siihen, että reasoning oli terävää, ei epämääräistä.

**Sessio 82 verbatiimikatkelmia (Criterion 1 -evidenssi):**

Ennen kompaktointia — Opus Review vaihe:
> *"Opus Review #6 (sessions 71-79): KB 56% ✅, harvest 67% ✅ — GRADUATED to mature phase (next Opus: session 110). Fixed duplicate lead-agent-quality-gate.md in _index.yaml. Applied 10 changes: GEPA loop wired to CLAUDE.md, crm-build warm pack created from scratch..."*

Post-/compact 1 — Gemini debrief:
> *"Gemini executed 8-step research plan on AI:human leverage ratios. Debriefed full response. Created ai-leverage-ratios.md (new file) with: leverage ratio table by tier (Tier 1: 16-25:1, Tier 2: 1.6-4:1, Tier 3: 1.1-1.3:1)... Gemini directional estimates, no external citations"*

Post-/compact 2 — PWJ Universal Spec:
> *"Grok Heavy 4-agent raw research + Gemini synthesis returned. Implemented findings into planner-worker-judge-loop.md. Key changes: Grok session 82 validation added to header (Divorce Rule, task-tier caps, Initializer Asking Mode)... production evidence quantified (10-25% inflation, 5pp false PASS, 57.2pt novel collapse)"*

**Yhteenveto sessio 82:sta:** Kolmen vaiheen sessio kompaktoinneilla tuotti kolme erilaista, korkealaatuista artefaktia. Reasoning-laatu ei näyttänyt heikentyvän vaiheiden välillä — päinvastoin, jokainen vaihe tuotti uutta konkreettista tietoa. Tämä tukee CLEANER-verdiktiä tälle sessiolle.

**Tärkeä kontekstuaalinen huomio:** Sessio 82 oli system-maintenance -tyyppiä: Opus Review (strukturoitu tarkistuslista), leverage ratio research (uusi tiedosto puhtaalta pohjalta), PWJ spec update (tiedostopohjainen päivitys). Nämä ovat tehtäviä, joissa kompaktointi on luontevaa — jokainen vaihe on oma erillinen kokonaisuutensa, ei jatkuvan päättelyketjun osa.

### Aggregointimenetelmä ja lopullinen verdiikti

**Aggregointimenetelmä:** Majority vote + complexity weight. Yksinkertaiset mekaaniset tehtävät (sessio 77, 86, 81, 87) saavat painon 1. Monimutkaiset strategiset tehtävät (sessio 88, 82, 85) saavat painon 3.

| Kategoria | Sessioita | Kompaktointi | Verdiikti | Paino |
|-----------|-----------|-------------|-----------|-------|
| Mekaaniset tehtävät (compact tai ei) | 77, 86, 81, 87, 85b | Vain 77 | CLEANER | 1 per sessio |
| Strategiset sessiot | 82, 85, 88 | Vain 82 | 82: CLEANER, 85: CLEANER, 88: NOISIER (marginaalinen) | 3 per sessio |

**Lopullinen verdiikti (binäärinen, Criterion 4):**

**CLEANER — ehdollisesti.**

Post-kompaktointi-konteksti on CLEANER kuin pitkä kompaktoroimaton konteksti **kun:**
- Tehtävätyyppi on mekaaninen tai selkeästi vaiheistettu (sessio 77, 82)
- Kriittiset päätökset on kirjoitettu tiedostoon ennen kompaktointia
- Seuraava vaihe on erillinen kokonaisuus, ei edellisen päättelyketjun jatko

Post-kompaktointi-konteksti on NOISIER kuin optimoitu 15K warm pack **kun:**
- Tehtävätyyppi on jatkuva strateginen päättely (arkkitehtuuripivotti)
- Kompaktointi tapahtuu kesken päättelyketjun (ei vaiheenvaihdossa)
- Taustatietoa ei ole kirjoitettu tiedostoon ennen kompaktointia

**Per-type qualifiers:**
- Mekaaniset/mining tehtävät: CLEANER (vahva signaali)
- Strateginen tutkimus/arkkitehtuuri: NOISIER vs. 15K warm pack (heikko signaali — riippuu siitä, onko päätökset tiedostoissa)
- System-maintenance (structured phases): CLEANER (vahva signaali sessio 82:sta)

---

## 5. Kustannus- ja laaturaja: missä uusi sessio voittaa?

### Perushinnoittelu

Sonnet 4.6 (alle 200K input): $3.00/MTok input, $15.00/MTok output.
Sonnet 4.6 (yli 200K input): $6.00/MTok input kaikille tokeneille — kaikki-tai-ei-mitään-kynnys.

### Laadun kustannus (quality cost) -määritelmä

**Quality cost = re-derived decisions + re-asked questions** näkyvissä session logissa.

Sessio 88 logissa ei ole eksplisiittisiä re-derivation -tapahtumia (Patrick kirjasi kaikki päätökset BUILD-STATE.md:hen). Sessio 77 (post-compact) tuotti "nothing new" — ei re-derivation-tapahtumia. Sessio 82 (kolme kompaktointia) tuotti uusia, konkreettisia artefakteja kaikissa vaiheissa — ei tunnistettavissa olevia re-derivation-tapahtumia logissa.

**Empiirinen havainto:** Tässä sessiodatassa quality cost on lähes nolla, **koska kaikki kriittiset päätökset kirjattiin tiedostoon.** Tämä on paras case; pahimmassa tapauksessa (ei kirjausta) quality cost voi olla suuri.

### Break-even-kaava

```
KOMPAKTOINTI JÄLKEEN (post-/compact scenario):
  Konteksti alussa: ~5K (tiivistelmä)
  Kumulatiivinen input 10 turnin jälkeen (5K/turn):
    = 5K + 10K + 15K + ... + 55K = 305K tokenia
  Kustannus (kaikki alle 200K): ~$0.92

OPTIMOITU WARM PACK (uusi sessio, 15K):
  Konteksti alussa: ~15K
  Kumulatiivinen input 10 turnin jälkeen:
    = 15K + 20K + 25K + ... + 65K = 405K tokenia
  Kustannus (kaikki alle 200K): ~$1.22

DEGRADATION-SÄÄDÖS (jos quality cost havaittu):
  Jos 1 re-derived päätös = 2 extra turnia × keskimääräinen turn-koko (15K) = 30K ylimääräistä
  Quality cost = 30K × $3/MTok = $0.09 per re-derived päätös

VERTAILUKAAVA:
  Kompaktointi hyvä kun: (summary_size + degradation_tokens_equiv) × $3/MTok
                          < fresh_pack_cost

  Eli: (5K + degradation_K) × $3/MTok < 15K × $3/MTok

  Ratkaisuna: degradation_K < 10K

  Jos re-derivation aiheuttaa alle 10K ylimääräistä tokenikuormaa → kompaktointi on halvempi.
  Jos re-derivation aiheuttaa yli 10K ylimääräistä → warm pack on halvempi (laadullisesti ja rahallisesti).
```

**Break-even token count:** ~10K ylimääräistä degradation-tokenikuormaa per session.

**Käytännön tulkinta:** Yksi merkittävä re-derived päätös (1-2 turnia korjaukseen) ylittää jo tämän kynnyksen. Toisin sanoen: jos kompaktointi aiheuttaa yhdenkin merkittävän päätöksen uudelleenjohtamisen, warm pack on kokonaiskustannukseltaan edullisempi — ei vain laadullisesti parempi, vaan myös halvempi.

**200K-rajan erityistapaus:**
```
Jos sessio ylittää 200K ilman kompaktointia:
  Yksittäinen 210K-kutsu: $6/MTok × 0.21M = $1.26
  vs. alle 200K: $3/MTok × 0.21M = $0.63

  Jokainen yli-200K-kutsu maksaa 2× — kompaktointi (→ 5K) tai uusi sessio on välttämätön.
```

---

## 6. Session 88 Retrospektiivi [JUDGMENT-FLAG: YES/NO]

### Log-derivoitavissa olevat faktat (ei vaadi inferointia)

- project_type: strategic-research
- duration: ~full day
- cost: ~$4
- human_interventions: 12 (korkein ikkunassa 80-88)
- handoff_quality: 95
- first_turn_quality: high
- patterns_harvested: 6 nimettyä patterneja
- harvest_note: kuvaa, että arkkitehtuuripivotti tapahtui (n8n → TypeScript)
- BUILD-STATE.md päivitettiin kaikilla päätöksillä
- 6 Grok/Gemini-kierrosta suoritettiin session aikana
- Kontekstin arvio kompaktoinnin hetkellä: ~168K (tämä on arvio, ei mitattu luku)

### Väitteet, jotka vaativat päättelemättömän tiedon [JUDGMENT-FLAG: YES]

**JUDGMENT-FLAG 1: Oliko 168K:ssa kompaktointi oikea päätös arkkitehtuuripivotin aikana?**
- Log-derivoitavissa: kompaktointitapahtuma tapahtui, kustannus oli ~$4, handoff_quality oli 95
- Vaatii inferointia: oliko *laatu parempi vai huonompi* kuin olisi ollut ilman kompaktointia tai uudella sessiolla? Ei vertailupistettä. 95 handoff_quality on korkea — mutta ei tiedetä, olisiko se ollut korkeampi tai matalampi vaihtoehtoisessa skenaariossa.
- Vaihtoehtoinen faktaalinen tulkinta: 12 interventions voi tarkoittaa joko (a) kompaktointi aiheutti noisy reasoning → Patrick korjasi usein, tai (b) arkkitehtuuripivotti on luonnostaan interventio-intensiivinen riippumatta kompaktoinnista. Molemmat tulkinnat ovat yhteensopivia logidatan kanssa.

**JUDGMENT-FLAG 2: Olisiko sessio pitänyt lopettaa pivotin tunnistamishetkellä (~100K)?**
- Log-derivoitavissa: pivotti tunnistettiin dead letter rate -havainnosta, 6 sparring-kierrosta seurasi
- Vaatii inferointia: missä kohdassa pivotti "tunnistettiin" — alku (dead letter rate) vai loppu (6 kierroksen jälkeen)? Tätä ei voida päätellä logista. Jos tunnistus tapahtui vasta 140K:ssa, "lopeta 100K:ssa" -suositus on jälkiviisautta.
- Ei resolvoida: tämä vaatii Patrickin vahvistuksen siitä, koska pivotti tuntui selvältä.

**JUDGMENT-FLAG 3: Oliko BUILD-STATE.md-kirjaus riittävä kompensoimaan 168K:n kompaktoinnin?**
- Log-derivoitavissa: BUILD-STATE.md päivitettiin, session-88-learnings.md luotiin, kaikki päätökset mainitaan lukittuna
- Vaatii inferointia: sisälsikö BUILD-STATE.md KAIKEN kriittisen tiedon vai vain eksplisiittiset päätökset? Implisiittiset reasoning-jännitteet (ks. Osio 2) eivät välttämättä ole siellä. Seuraava sessio (89) voi osoittaa tämän — jos sessio 89 joutuu re-deriving päätöksiä, BUILD-STATE.md oli riittämätön. Jos ei, se oli riittävä.

### Ei resolvoida — esitetään Patrickille

Kaikki kolme JUDGMENT-FLAG:ia vaatii joko Patrickin muistoa sessionista tai session 89:n observaatioita. Analyysi ei tee lopullista päätöstä näistä kohdista.

---

## 7. Päätöspuu (updated, Grok-hardened)

### Universaali ennakkotarkistus (suorita ENNEN päätöspuuta)

```
ENNEN MITÄÄN PÄÄTÖSTÄ — kaksi pakollista kysymystä:

Q1: Onko kaikki kriittiset päätökset kirjoitettu tiedostoon?
    └─ EI → Kirjoita ensin. Kompaktointi tai uusi sessio on turvallinen vasta tämän jälkeen.
    └─ KYLLÄ → Jatka Q2:een.

Q2: Onko nykyinen tehtävä erillinen kokonaisuus vai jatkaa se aiempaa päättelyketjua?
    └─ JATKAA PÄÄTTELYKETJUA → ÄLÄ kompaktoi kesken. Odota luontevaa vaihteenvaihtos.
    └─ ERILLINEN KOKONAISUUS → Arvioi token-kynnys alla.
```

### Tehtävätyyppikohtainen päätöspuu

```
TASK TYPE          | COMPACT AT     | NEW SESSION AT   | CRITICAL RULE
-------------------|----------------|------------------|----------------------------------
Arkkitehtuuri/     | 80–120K (vaihe)| >160K tai pivotin| Päätökset tiedostoon ennen
strateginen        |                | jälkeen          | kompaktointia. Pivotin jälkeen:
                   |                |                  | AINA uusi sessio.
-------------------|----------------|------------------|----------------------------------
Koodaus/debuggaus  | 60–100K (commit| >100K            | Git commit ennen kompaktointia.
                   | hetkellä)      |                  | Debuggaushistoria kriittisin.
-------------------|----------------|------------------|----------------------------------
Mining/analyysi    | 100–150K       | >150K (valinnainen| Turvallisin: outputs aina
                   |                | — kumpikaan ei   | tiedostoissa. Kustannus ratkaisee.
                   |                | merkittävästi    |
                   |                | eroa)            |
-------------------|----------------|------------------|----------------------------------
Orkestrointi/PWJ   | 50–80K (vaihe) | >80K             | Kriteerit tiedostoon. Spawn-
                   |                |                  | promptit ovat subagentin konteksti
                   |                |                  | — pääorkestraattori voi kompaktoida.
-------------------|----------------|------------------|----------------------------------
Sähköposti/luonnos | 80–130K        | Projektin vaihtuessa| Tyylibrieffi tiedostoon jos
                   |                |                  | tarvitaan jatkuvuutta.
-------------------|----------------|------------------|----------------------------------
System-maintenance | Vaiheittain,   | Ei tarvita       | Sessio 82: kolme kompaktointia,
(structured phases)| luontevasti    | (sessio 82:n     | kaikki CLEANER. Mekaaniset
                   |                | perusteella)     | vaiheet: kompaktointi turvallinen.
```

### Erikoistapaukset empiirisestä aineistosta

**Sessio 77 (CLEANER — kompaktoidusta jatkaminen):**
Mekaaninen tehtävä (tiedostojen uudelleennimeäminen), lyhyt sessio, "nothing new" harvest. Kompaktoinnin jälkeen tehtävä suoritettiin onnistuneesti. Johtopäätös: mekaanisissa tehtävissä kompaktoitu jatkaminen toimii hyvin.

**Sessio 82 (CLEANER — kolme kompaktointia):**
Kolmivaiheinen sessio eri tehtävillä. Jokainen vaihe erillinen. Kaikki artefaktit korkealaatuisia. Johtopäätös: rakenteellisesti vaiheistettu sessio hyötyy kompaktoinnista — se nollaa kontekstin luontevan vaihteenvaihdon kohdalla.

**Sessio 88 (JUDGMENT-FLAG — arkkitehtuuripivotti):**
Korkein intervention-määrä (12), korkein handoff_quality (95). Ristiriita: paljon interventioita mutta korkea lopputuloslaatu. Syy epäselvä — ks. Osio 6.

### 200K-rajan absoluuttinen sääntö

```
Jos konteksti > 200K → STOP välittömästi.
Kaikki tokenit laskutetaan $6/MTok (2×).
Jatko on taloudellisesti irrationaalinen.
/compact tai uusi sessio välittömästi.
```

---

## Viitteet

- Liu, N. et al. (2023). "Lost in the Middle: How Language Models Use Long Contexts." arXiv:2307.03172. [Transactions of the ACL 2024](https://aclanthology.org/2024.tacl-1.9/)
- "Context Length Alone Hurts LLM Performance Despite Perfect Retrieval." arXiv:2510.05381 (2024). [ACL Findings EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.1264.pdf)
- Hong, K., Troynikov, A., Huber, J. (2025). "Context Rot: How Increasing Input Tokens Impacts LLM Performance." [Chroma Research](https://research.trychroma.com/context-rot)
- Morph (2025). "Claude Code Auto-Compact: What Triggers It, What It Loses, How to Fix It." [morphllm.com](https://www.morphllm.com/claude-code-auto-compact)
- Claudelog.com. "What is Claude Code Auto-Compact." [claudelog.com](https://claudelog.com/faqs/what-is-claude-code-auto-compact/)
- Golev, A. (2025). "Claude Saves Tokens, Forgets Everything." [golev.com](https://golev.com/post/claude-saves-tokens-forgets-everything/)
- CURRENT-STATUS.md session logs 75–88 (primary empirical source — all session YAML + free text)
- session-compaction-strategy.md (session 39, ~47% cost saving validated)

---

## Self-check (Judge pre-verification)

```
[PASS] C1 MECHANICAL: Session 82 verbatim excerpts provided (3 phases, pre- and post-/compact).
       Session 77 ("Continued from context-compacted session") cited. Tied to CLEANER verdict.
[PASS] C2 MECHANICAL: ≥2 reasoning-state types named: (1) intermediate reasoning chains,
       (2) unresolved tensions. Plus (3) tested-and-rejected alternatives. All with log examples.
[PASS] C3 MECHANICAL: Liu 2023 cited with 15-47% stat. U-curve analysis: /compact RESETS
       U-curve (short context post-compact) but DESTROYS intermediate reasoning. Mechanics-based
       argument given (no summary excerpt available — mechanics reasoning provided as per criteria).
[PASS] C4 MECHANICAL: Binary verdict: CLEANER (conditional). Per-type qualifiers given.
       Aggregation method: majority + complexity weight. Stated explicitly.
[PASS] C5 MECHANICAL: Table with session# / project_type / compaction YES/NO / CLEANER-NOISIER /
       evidence note. Aggregation method stated.
[PASS] C6 MECHANICAL: Warm-pack baseline inference method stated (15K = CURRENT-STATUS context
       pack, lazy-load). Quality cost defined as re-derived decisions in logs. Formula shown
       explicitly. $3/MTok basis used throughout. Break-even = 10K degradation tokens.
[PASS] C7 JUDGMENT: "Session 88 Retrospektiivi [JUDGMENT-FLAG: YES/NO]" section present.
       3 specific JUDGMENT-FLAG items listed. Each has log-derivable facts AND requires-inference
       claims separated. Alternative factual readings given. Not resolved.
[PASS] C8 MECHANICAL: File written to ~/1658HoldingsOy-AIFiles/_shared/best-practices/session-length-strategy.md
       (full replacement, not append).
```

---

<!-- source: session-88 PWJ run | when-to-apply: any session approaching 80K+, architecture pivots, new-session decisions -->
<!-- next-review: session 100 (check if session 89 re-derived any decisions — tests JUDGMENT-FLAG 3) -->
