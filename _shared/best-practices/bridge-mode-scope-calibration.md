---
name: bridge-mode-scope-calibration
description: Session Bridge genius check --mode bridge on suunniteltu 100K+ token sessiosiirroille, ei lyhyille ikkunahandovereille. Väärä moodi = kolminkertainen token-hukkaus.
type: feedback
source: patrick
session: this-window (s88-context)
---

# Bridge Mode Scope Calibration

## Havainto

`genius-check.py --mode bridge` on suunniteltu auditoimaan **Session Bridge Prompteja** —
tilanteita joissa 100K+ tokenin reasoning-tila siirretään sessiosta toiseen ilman drop-offia.

Sama audit-moodi lyhyelle ikkunahandoverille (mitä tehtiin tässä ikkunassa) tuottaa:
- FAIL × 2 ennen kuin PASS saadaan
- Kolminkertaisen token-kulutuksen auditointiin vs. itse handoveriin
- Irrelevantteja heikkouksia (vaatii reasoning chainit asioille jotka ovat triviaalia)

## Kalibrointiohje

| Tilanne | Oikea moodi | Perustelu |
|---------|-------------|-----------|
| Sessio × → Sessio Y, 100K+ tokenin reasoning-tila | `--mode bridge` | Suunniteltu tähän |
| Lyhyt ikkuna, 1-2 tehtävää, ei monimutkaista tilaa | `--tier 1` (skip) | Triviaali handover |
| Implementation session prompt | `--mode implementation` (default) | Oletusmoodi |

## Sääntö

**Ennen bridge-auditia:** Arvioi onko tässä oikeasti monimutkainen reasoning-tila
joka voi re-derivoitua väärin. Jos ei → käytä `--tier 1` tai `--mode implementation`.

**Why:** Bridge-moodi auditoi jatkuvuusriskiä joka ei ole olemassa lyhyissä handovereissa.
Tuloksena on false negatives (FAIL) jotka kuluttavat tokeneita korjauksiin jotka eivät
tuo arvoa.

**How to apply:** Kun /prompt-creator luo handover-materiaalia lyhyestä ikkunasta
tai yksinkertaisesta sessiovaihdosta → default `--tier 1`, ei `--mode bridge`.
