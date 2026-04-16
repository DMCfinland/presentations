# Riikka Outreach Quality — Grok Spar Prompt
# Valmis pastettavaksi | S189 | 2026-04-12
# Status: PRE-FLIGHT PASS — paste manuaalisesti Grok Expert -modessa

---

## Tulokset S190 alussa: paste Grok UI:hin → Expert mode → kopioi vastaus tähän alle

---

## GROK EXPERT PROMPT (valmis)

**Valitse Grok UI:ssa: Expert mode**

```
OUTPUT FORMAT: Per-question numbered answers labeled [Harper]/[Benjamin]/[Lucas] where applicable + a rewritten sample outreach email in Finnish at the end. Rate the current message on a 1-10 scale with explicit scoring criteria. Surface agent disagreements — do not resolve them.

GOAL: Tell me exactly what changes would most increase reply rates for this Finnish B2B outreach pipeline targeting industrial/technology companies. Be specific and direct.

CONTEXT:
- A Python-based AI headhunter pipeline generates Finnish outreach emails for an experienced candidate.
- Candidate: 20+ years in Business Development / Innovation Management. Past employers: Nokia, Metso Automation, John Deere, Comatec Group (built innovation hub from scratch). Two master's degrees (KTM Global Innovation Management + MBA Leading Business Transformation). 4.5 years international (Hong Kong, Germany, UK). Languages: Finnish, English, German, Swedish. Location: Oulu, Finland. Target: industrial/technology companies 200-5000 employees.
- Current pipeline flaw: RAG retrieves relevant STAR stories from the candidate profile but does NOT inject them into the message. The hook is generic. Employer names are not mentioned.

<current_outreach>
Subject: "Kiinnostunut Outokumpun strategiakehitys-roolista — Matti?"
Body: "Hei Matti, Seurasin Outokumpun kehitystä ja jäin miettimään, miten strategiakehitys-alueella kasvunne sopisi omaan taustaani. Olen liiketoiminnan kehittämisen ja innovaatiojohtamisen asiantuntija, jolla on 20+ vuoden kokemus kansainvälisistä rooleista ja etsin seuraavaa roolia, jossa voisin tuoda konkreettista lisäarvoa. Olisiko sinulla 15 minuuttia ensi viikolla lyhyelle puhelulle?"
Follow-up D+7: "Hei Matti, Kirjoitin viime viikolla Outokumpusta — onko aiheella hetki?"
Follow-up D+14: "Hei Matti, Viimeinen muistutus: jos Outokumpussa sopii strategiakehitys-osaajalle rooli, löydät minut täältä. Kaikki hyvää!"
</current_outreach>

QUESTIONS (answer each explicitly):
1. Top 3 improvements for Finnish B2B reply rate — industrial/engineering target?
2. STAR story in first message or save for reply thread?
3. "15 min phone call" CTA — right for Finnish culture or is email/LinkedIn better?
4. How should RAG hits personalize the message — what to pull, where to inject?
5. Rate current message 1-10 with explicit criteria.
Also: write a rewritten version using Nokia/Metso as credibility anchors + specific trigger + achievement snippet.

COLLABORATION PROTOCOL: Hierarchical. Harper: Finnish B2B email reply rates + Nordic outreach best practices 2024-2026. Lucas: argue against STAR stories in cold emails + argue Finns respond to brevity not substance. Benjamin: verify any conversion rate claims.

CONSTRAINTS: Direct and specific. Pipeline-implementable at scale. Finnish industrial culture is conservative. Surface agent disagreements.

VERBOSITY: Full depth per question. Do not compress.
```

---

## Gemini — S190 alussa aja plain modessa

```bash
bash ~/run-gemini.sh --prompt-file /tmp/riikka_outreach_spar.txt
```

Prompti on vielä /tmp/riikka_outreach_spar.txt:ssä — tai kopioi yllä olevasta.

---

## Grok vastaus (lisätään S190 alussa)

[PASTE GROK RESPONSE HERE]

## Gemini vastaus — 2026-04-12 S189

**RATING: 4/10**

### Top 3 parannusta (Gemini)

**1. Hyper-personalisoitu hook — yrityskohtainen tieto**
"Seurasin kehitystä" = mass email signaali. Tilalle: spesifi viittaus yrityksen julkiseen strategiaan/uutiseen.
> "Luin kiinnostuneena Outokummun vuosikertomuksesta liittyen kiertotaloustavoitteisiinne — miten yli 20v kokemukseni innovaatiojohtamisesta voisi tukea juuri tätä."

**2. Nokia/Metso/Comatec nimillä + kvantifioitu tulos heti**
"20+ vuoden kokemus" = tyhjää. Tilalle:
> "Comatec Groupille nollasta rakentamani innovaatioyksikkö osoittaa kykyni tuoda konkreettista lisäarvoa."

**3. Arvolisäävät follow-upit — ei nagging**
D+7: tuo uuden relevantin palastelman (kansainvälinen kokemus, kv-liiketoiminta)
D+14: tarjoa case-esimerkki → "lähetän sähköpostilla tai LinkedInissä, jos puhelu ei sovi"

### STAR-tarina ensimmäisessä viestissä? → KYLLÄ
Yksi tiivistetty, kvantifioitu achievement suoraan ensimmäiseen viestiin. Koko tarina myöhemmin.

### CTA: 15 min puhelu → OK mutta tarjoa vaihtoehtoja
> "Tai olisiko lyhyt sähköpostivaihto tai LinkedIn-viesti sopivampi alku?"

### RAG-injektiostrategia (konkreettinen)
| Kohta | Mitä injektoidaan |
|---|---|
| Subject | company_name + yrityksen strategiasana |
| Hook | yrityksen spesifi uutinen/tavoite → Riikan relevantti achievement |
| Body §1 | 1-2 achievement + employer name (Nokia/Metso/Comatec) |
| Body §2 | kv-kokemus tai MBA tai 100 prosessia — se joka osuu parhaiten |
| CTA | linkki takaisin hookin yritysinsightiin |
| Follow-upit | jokainen tuo UUDEN palastelman profiilista |

### Mitä puuttuu (Gemini)
1. Yrityskohtainen hook — nolla tutkimuksen merkkiä
2. Nokia/Metso/Comatec poistettu — kriittinen virhe teollisuusyrityksiä lähestyttäessä
3. Achievement truncated → "kansainvälisistä rool" = epäammattimainen
4. Follow-upit liian lyhyet + ei uutta arvoa
5. CTA vain Riikan tarve, ei vastaanottajan hyöty
