# 1658 Holdings — Current Status

> **This is the CORE file. ~100 lines. Auto-loaded at session start.**
> Session log (last 5 full): SESSION-LOG.md | One-liner archive: SESSION-ARCHIVE.md | Full archive: SESSION-ARCHIVE-FULL.md

---

## Meta

```
session_number: 232
window_start: 223
next_compression: 232
next_opus_review: 244
last_compressed: 2026-04-14 (S220-S221 at S226)
last_opus_review: 2026-04-12 (S184 — Opus Review 10)
phase: mature (every 30 sessions)
```

---

## Current State

| Field | Value |
|-------|-------|
| **Current Phase** | S231 COMPLETE — Arctic Cruises V3.3 live + 5-bridge launch roadmap (S232-S236) + orchestrator pipeline (S237 V2, Grok+Gemini sparred). All commercial knowledge locked. |
| **⚠️ KIIREINEN** | **M365 MC1266911 — Deadline 1.5.2026.** admin.microsoft.com → Copilot → AI providers → Anthropic → Enable. Sebastian tai Patrick. |
| **Active Projects** | 1. **Arctic Cruises Launch Pipeline** ← S237 orchestrator ready. Run: `claude --dangerously-skip-permissions` + paste launch prompt<br>2. **Riikka Phase 2 ACTIVATION** ← LinkedIn + AMD + Toljamo VPL<br>3. **M365 MC1266911** ⚠️ deadline 1.5. |
| **Last Session** | S231 — Arctic Cruises V3.3 (92/100 Gemini), 7-bridge roadmap, S237 orchestrator V2 (Grok+Gemini sparred, 4 fixes: data contract + progressive commits + structural gates + wave isolation). |
| **Next 3 Tasks** | 1. **Run S237 orchestrator** — `claude --dangerously-skip-permissions` → paste ARCTIC-PIPELINE-LAUNCH-PROMPT.md<br>2. **Patrick: git push origin main** (Arctic V3.3 live)<br>3. **M365 MC1266911** ⚠️ deadline 1.5. |

---

## Open Deliverables

- [ ] **Parkkimaksu 60€** ← maksa ennen **26.4.2026**
- [ ] **M365 MC1266911** ⚠️ ← Enable ennen 1.5.2026
- [ ] **git push origin main** ← Arctic V3.3 not yet live (run in terminal)
- [x] **Arctic Cruises B2C Website V3.3** ✅ — COMPLETE (1,778 lines, Gemini 92/100)
- [ ] **Arctic Cruises Launch Pipeline S237** ← orchestrator V2 ready to run
- [ ] **Riikka LinkedIn activation** ← Patrick → forward checklist to Riikka NOW
- [ ] **AMD application** ← Riikka to submit within 7 days of S231
- [ ] **Toljamo VPL** ← Riikka fill [X]% metric before sending
- [ ] **Tonttirahoitus 17.4. outcomes** ← Sebastian HETU + kokoustulokset tallentamatta
- [ ] **COSME grant** ← Maakuntaliitto + DE/IE-partneri 30.4. deadline
- [ ] **Supabase MCP** ← 15 min setup
- [ ] **mcpvault dual vault** ← js/ vault lisäys

---

## Context Pack — S232 (next session)

```
warm_pack: SESSION-BRIDGE-S237-ARCTIC-ORCHESTRATOR-V2.md  # Run the pipeline

key_files:
  - ~/1658HoldingsOy-AIFiles/_drafts/ARCTIC-PIPELINE-LAUNCH-PROMPT.md          # PASTE THIS to launch
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S237-ARCTIC-ORCHESTRATOR-V2.md  # Full spec
  - ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md             # Commercial truth
  - ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html                            # B2C reference

arctic_pipeline_state:
  b2c_website: "COMPLETE V3.3 — Gemini 92/100. Committed ef5a520. Push pending."
  live_url: "https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html"
  push_command: "git push origin main (manual — hook blocks --no-verify)"
  commercial_brief: "_drafts/arctic-b2b-commercial-brief.md ✅ (pricing locked)"
  bridges_written: "S232-S236 ✅ (5 session specs) + S237-V2 ✅ (orchestrator)"
  launch_prompt: "_drafts/ARCTIC-PIPELINE-LAUNCH-PROMPT.md ✅ (ready to paste)"
  pricing_master: "NOT YET WRITTEN — orchestrator writes this at session start"

  deliverables_pipeline:
    S232: "B2B Flyer — arctic-cruises-b2b-flyer.html"
    S233: "FAM Pack — fam-invitation.html + fam-programme.html"
    S234: "Operator PRD — arctic-cruises-operator-prd.html"
    S235: "Operations Brief — booking-prd.md + laura-operations-brief.md"
    S236: "Knowledge Bible — arctic-cruises-knowledge-bible.md"

  key_commercial_data:
    net_rates: "Day €320 / 3N €960 / 7N €2,080 (20% early partner)"
    fam: "31 Aug–3 Sep 2026 · Complimentary · 50 operators · Apply by 15 Jul 2026"
    contact: "laura@finlanddmc.fi"
    deadline: "15 July 2026 (early partner application)"

riikka_system_state:
  phase: "Phase 2 ACTIVATION — LinkedIn + AMD + Toljamo VPL ready"
  toljamo_vpl: "SPARRED ✅ — Riikka must fill [X]% metric before sending"
  amd_application: "Cover letter drafted ✅ — Riikka to submit by 2026-04-22"
  linkedin_checklist: "brain/outreach/linkedin-activation-checklist-20260415.md"
  pipeline_tracker: "~/Desktop/ai-headhunter/wiki/pipeline.md ✅"

tonttirahoitus_state:
  aikataulu: "17.4. → Teemu 30.4. → paketti 6.5. → pankki 8.5. → tarjous 1.6. → kaupat 15.6."

tools_confirmed:
  gemini: "bash ~/run-gemini.sh --prompt-file /tmp/prompt.txt --model gemini-2.5-pro --output-file /tmp/out.txt"
  transcribe: "bash ~/run-transcribe.sh <audio> --format speakers --model gemini-2.5-pro --output-file /tmp/out.txt"

coding_stack_v2:
  orchestrator: "Claude Code (DDSC, architecture, autonomous + heavy builder)"
  judge_1: "Gemini 2.5 Pro — gemini-2.5-pro (NOT gemini-3.1-pro-preview — stale reference)"
  judge_2: "Grok Auto/Expert (adversarial spar)"
```
