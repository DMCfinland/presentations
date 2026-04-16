# 1658 Holdings — Current Status

> **This is the CORE file. ~100 lines. Auto-loaded at session start.**
> Session log (last 5 full): SESSION-LOG.md | One-liner archive: SESSION-ARCHIVE.md | Full archive: SESSION-ARCHIVE-FULL.md

---

## Meta

```
session_number: 239
window_start: 234
next_compression: 243
next_opus_review: 244
last_compressed: 2026-04-16 (S231-S232 at S238)
last_opus_review: 2026-04-12 (S184 — Opus Review 10)
phase: mature (every 30 sessions)
```

---

## Current State

| Field | Value |
|-------|-------|
| **Current Phase** | S239 COMPLETE — Arctic B2C operator research (5 operators) + 4 website improvements applied + Grok/Gemini spar. Email corrected. |
| **⚠️ KIIREINEN x3** | **1. Riikka AMD** ← submit by **2026-04-22** · **2. IQM VPL** ← send by **Apr 25** · **3. M365 MC1266911** ← enable by **May 1** |
| **Active Projects** | 1. **Arctic B2C** — 4 improvements applied. Next: German version + video brief + B2B section<br>2. **Riikka outreach** — IQM URGENT (send by Apr 25)<br>3. **Geopark AI PA** — Mikko outreach draft ready (find his email)<br>4. **M365 MC1266911** ⚠️ deadline May 1 |
| **Last Session** | S239 — 5-operator website research (A&K, Hapag, PONANT, Saga, Scenic). 4 HTML improvements. Form fixed. Email corrected. Grok+Gemini spar: PONANT consumer hypothesis calibrated. |
| **Next 3 Tasks** | 1. **git push** ← hook blocks, run manually in terminal<br>2. **IQM VPL** ← URGENT Apr 25<br>3. **Arctic German version** ← biggest gap per spar |

---

## Open Deliverables

- [ ] **git push origin main** ← hook blocks in Claude Code — run manually in terminal
- [ ] **Riikka AMD application** ⚠️ ← submit by **2026-04-22**
- [ ] **IQM VPL** ⚠️ ← spar + send by **Apr 25** (IPO June 2026)
- [ ] **M365 MC1266911** ⚠️ ← Enable by **1.5.2026** (admin.microsoft.com → Copilot → AI providers)
- [ ] **Parkkimaksu 60€** ← maksa ennen **26.4.2026**
- [ ] **Mikko Ikäheimo contact** ← outreach draft ready, find email (saimaa.fi)
- [x] **Arctic B2C 4 improvements** ✅ — form fix, hero CTA, scarcity framing, email corrected (`a2aa7aa`)
- [ ] **Arctic B2C German version** ← biggest gap per Grok spar (DACH 37% of market)
- [ ] **Arctic B2C professional video brief** ← Gemini: desire creation before funnel
- [ ] **Arctic B2C named naturalist** ← coordinate with Saku, add to voyages
- [ ] **Arctic B2C B2B section** ← needs: commission %, trade contact (patrick's call)
- [ ] **COSME grant** ← Maakuntaliitto + DE/IE-partneri **30.4.** deadline
- [ ] **Tonttirahoitus** ← Sebastian HETU + kokoustulokset

---

## Context Pack — S240

```
key_files_arctic:
  - ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html
  - ~/1658HoldingsOy-AIFiles/output/arctic-cruises-outreach/website-improvement-spec.md
  - ~/1658HoldingsOy-AIFiles/output/arctic-cruises-outreach/operator-target-list.md

key_files_riikka:
  - ~/Desktop/ai-headhunter/wiki/companies/iqm-quantum.md   # URGENT Apr 25
  - ~/Desktop/ai-headhunter/outputs/BLOCKER-metric-needed.md

arctic_consumer_framing_corrected:
  consumer: "DACH river/lake cruise buyer — contemplative slow travel"
  not: "Aspirational PONANT expedition buyer"
  price_anchor: "AmaWaterways/Viking €3,500-€9,000 vs our €2,600 — CONFIRMED CORRECT"
  ponant_role: "B2B partner target (they sell us), not consumer competitor"

arctic_next_gaps:
  gap_A: "German/DACH language version — 37% of European river/lake market"
  gap_B: "Professional video + hero photography brief to Saku/Laura"
  gap_C: "Named naturalist per voyage — coordinate with Saku"
  gap_D: "B2B trade section — needs: commission %, trade contact from Patrick"

tools_confirmed:
  gemini: "bash ~/run-gemini.sh --prompt-file /tmp/prompt.txt --model gemini-2.5-pro --output-file /tmp/out.txt"
  grok: "python3 ~/.claude/skills/grok-heavy-browser/main.py 'prompt' --model Expert --background"
```
