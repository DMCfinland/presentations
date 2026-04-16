# 1658 Holdings — Current Status

> **This is the CORE file. ~100 lines. Auto-loaded at session start.**
> Session log (last 5 full): SESSION-LOG.md | One-liner archive: SESSION-ARCHIVE.md | Full archive: SESSION-ARCHIVE-FULL.md

---

## Meta

```
session_number: 238
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
| **Current Phase** | S238 COMPLETE — Arctic pipeline done (7 docs, MANIFEST). Grok/Gemini spar done. 15 operator targets identified. S240 bridge written: operator website research → B2C improvements. |
| **⚠️ KIIREINEN** | **M365 MC1266911 — Deadline 1.5.2026.** admin.microsoft.com → Copilot → AI providers → Anthropic → Enable. Sebastian tai Patrick. |
| **Active Projects** | 1. **Arctic Cruises website** ← S240 bridge ready (operator research → B2C improvements)<br>2. **Riikka outreach** — IQM URGENT (send by Apr 25). 5 VPL drafts ready.<br>3. **M365 MC1266911** ⚠️ deadline May 1. |
| **Last Session** | S238 — Arctic Wave 4 complete. Grok/Gemini spar (NOT READY, Patrick corrections overrode). DACH competitors verified (none comparable). 15 operator targets identified. |
| **Next 3 Tasks** | 1. **S240 operator website research** → B2C improvements (bridge ready)<br>2. **Riikka IQM VPL** — spar + send by Apr 25 (IPO June deadline)<br>3. **M365 MC1266911** ⚠️ deadline May 1 |

---

## Open Deliverables

- [ ] **Parkkimaksu 60€** ← maksa ennen **26.4.2026**
- [ ] **M365 MC1266911** ⚠️ ← Enable ennen 1.5.2026
- [ ] **git push origin main** ← Arctic pipeline not yet pushed live
- [x] **Arctic Pipeline 7 docs** ✅ — committed, MANIFEST written (`01a3fb0`)
- [ ] **Arctic B2C improvements** ← S240 bridge. 5 parallel operator research agents → apply patterns
- [ ] **✓ checkmarks B2B flyer** ← replace with brand icons (need lake land 2.0 brand guide path from Patrick)
- [ ] **Riikka IQM VPL** ← spar + send by **Apr 25** (IPO June 2026 hard deadline)
- [ ] **Riikka AMD application** ← submit by 2026-04-22
- [ ] **Toljamo VPL** ← Riikka fills [X]% metric first
- [ ] **Tonttirahoitus outcomes** ← Sebastian HETU + kokoustulokset
- [ ] **COSME grant** ← Maakuntaliitto + DE/IE-partneri 30.4. deadline
- [ ] **Geopark Conference 17.9.2026** ← Patrick contacts Mikko Ikäheimo week 17

---

## Context Pack — S239 (next session)

```
warm_pack_primary: SESSION-BRIDGE-S240-OPERATOR-WEBSITE-RESEARCH.md

key_files_arctic:
  - ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html
  - ~/1658HoldingsOy-AIFiles/output/arctic-cruises-outreach/operator-target-list.md
  - ~/1658HoldingsOy-AIFiles/output/PRICING-MASTER.json
  - ~/1658HoldingsOy-AIFiles/MANIFEST-COMPLETE.md

key_files_riikka:
  - ~/Desktop/ai-headhunter/wiki/pipeline.md
  - ~/Desktop/ai-headhunter/wiki/companies/iqm-quantum.md   # URGENT Apr 25
  - ~/Desktop/ai-headhunter/outputs/BLOCKER-metric-needed.md

arctic_competitive_reality:
  no_comparable_dach_product: true   # verified S238 web research
  vessel_max_pax: 100
  subsidies: true
  usp: "WILDERNESS — unbuilt nature, Lappeenranta-Kuopio route not operated ~50 years"
  marketing_angle: "Remote lake wilderness rare in today's world"

operator_tier1:
  - "Abercrombie & Kent (UK) — HNWI wilderness charters"
  - "Hapag-Lloyd (DE) — MS Europa, German ultra-HNW discovery"
  - "Saga Cruises (UK) — 100% 50+, fleet expanding 2027"
  - "PONANT (DE+UK) — 92-184 pax, Smithsonian intellectual travel"
  - "Riverside Luxury Cruises (DE) — ultra-luxury river, new-format identity"

tools_confirmed:
  gemini: "bash ~/run-gemini.sh --prompt-file /tmp/prompt.txt --model gemini-2.5-pro --output-file /tmp/out.txt"
  grok: "python3 ~/.claude/skills/grok-heavy-browser/main.py 'prompt' --model Expert --background"
```
