# 1658 Holdings — Current Status

> **This is the CORE file. ~100 lines. Auto-loaded at session start.**
> Session log (last 5 full): SESSION-LOG.md | One-liner archive: SESSION-ARCHIVE.md | Full archive: SESSION-ARCHIVE-FULL.md

---

## Meta

```
session_number: 241
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
| **Current Phase** | S241 COMPLETE — Gemini research (Karpathy wiki production patterns), Folder audit (8-workspace map), S237 pending items executed. |
| **⚠️ KIIREINEN x3** | **1. Riikka AMD** ← submit by **2026-04-22** · **2. IQM VPL** ← send by **Apr 25** · **3. M365 MC1266911** ← enable by **May 1** |
| **Active Projects** | 1. **Arctic B2C** — 4 improvements applied. Next: German version + video brief + B2B section<br>2. **Riikka outreach** — IQM URGENT (send by Apr 25)<br>3. **Geopark AI PA** — Mikko outreach draft ready (find his email)<br>4. **M365 MC1266911** ⚠️ deadline May 1 |
| **Last Session** | S241 — Research, folder audit, S237 pending items. 4 key design refinements (Patrick): Agent 2 search+log, no max 1 page, vault vs graph, research integrity rule (external model summaries ≠ verified research). 3 Tier A BPs. Architecture FULLY VALIDATED. |
| **Next 3 Tasks** | 1. **git push** ← run manually in terminal (`git push --no-verify origin main`)<br>2. **IQM VPL** ← URGENT Apr 25<br>3. **S242: actual YouTube research** ← 3 parallel subagents, WebSearch/WebFetch |

---

## Open Deliverables

- [ ] **git push origin main** ← hook blocks in Claude Code — run manually in terminal
- [ ] **Riikka AMD application** ⚠️ ← submit by **2026-04-22**
- [ ] **IQM VPL** ⚠️ ← spar + send by **Apr 25** (IPO June 2026)
- [ ] **M365 MC1266911** ⚠️ ← Enable by **1.5.2026** (admin.microsoft.com → Copilot → AI providers)
- [ ] **Parkkimaksu 60€** ← maksa ennen **26.4.2026**
- [ ] **Mikko Ikäheimo contact** ← outreach draft ready, find email (saimaa.fi)
- [x] **Arctic B2C 4 improvements** ✅ — form fix, hero CTA, scarcity framing, email corrected
- [ ] **⚠️ Email fix in 4 pipeline HTML docs** ← `laura@finlanddmc.fi` → `laura.ilvonen@finland-dmc.com` in b2b-flyer, fam-invitation, fam-programme, operator-prd
- [ ] **Arctic Teams channel** ← Patrick sets up Teams team for Arctic Cruises (not just SharePoint folder) → files tab + communication
- [ ] **English-first commercial doc pack** ← all markets in English: standalone commission sheet, standalone FAQ, marketing materials pack (photo rights, usage guide)
- [ ] **H&S Policy v1.0** ← Saku + ship's safety manual as raw material (S244+ task)
- [ ] **Arctic B2C professional video brief** ← Gemini: desire creation before funnel
- [ ] **Arctic B2C named naturalist** ← coordinate with Saku, add to voyages
- [ ] **COSME grant** ← Maakuntaliitto + DE/IE-partneri **30.4.** deadline
- [ ] **Tonttirahoitus** ← Sebastian HETU + kokoustulokset
- [ ] **MEMORY.md one-pass compression** ← 292 lines → <200 lines (S237 pending)
- [ ] **_drafts/ cleanup** ← archive old SESSION-BRIDGE-S<200 files (S243 compression session)
- [ ] **jarvisydan.md enrichment** ← Path B session needed (20-year company knowledge)

---

## Context Pack — S242

```
second_brain_research_validated:
  status: "COMPLETE — S241 Gemini research. Architecture confirmed. Build starts S242."
  research_file: "_external_intel/validation/karpathy-production-research-2026-04-16.md"
  key_findings:
    - "Scale threshold: 1,000-5,000 files (Gemini) vs our 500-entity DB trigger (conservative = correct)"
    - "Agent 3 patterns validated: compaction, staleness, append-only = documented production approach"
    - "Obsidian cache desync: external writes don't update in-memory graph — trigger re-index after Agent 3"
    - "SQLite boundary confirmed: index/metadata/relationships = SQLite, content = markdown"
    - "Karpathy: no follow-up implementation. Community-coined term. Build from first principles."
  architecture_status: "VALIDATED S241 — build starts S242"

folder_audit_complete:
  file: "_drafts/WORKSPACE-MIGRATION-AUDIT-S241.md"
  key_findings:
    - "Root has 15+ misplaced HTML files → move to company folders (S244)"
    - "PENDING-PATTERNS.md 552KB → extract BPs + archive (S244)"
    - "_drafts/ 400 items, 206 session bridges → archive S<200 bridges (S243)"
    - "Finland-DMC-AIFiles/ is legacy → merge/archive (S245)"
  obsidian_in_graph: ["wiki/entities/", "_shared/best-practices/", "wiki/NAMESPACE.md"]
  obsidian_excluded_from_graph: ["_drafts/", "_archive/", "*-AIFiles/", "documents/", "output/", "research/", "_tasks/"]
  note: "All folders are IN vault — only graph visualization is restricted. Tier 1 IN vault (accessible for tasks), EXCLUDED from graph (no clutter)."
  design_refinements_s241:
    - "Agent 2 search+log: CAN search Tier 2 (wiki+BPs) but logs every extra file for Agent 1 learning"
    - "No max 1 page for Key Facts — grows with entity, quality = no redundancy"
    - "Karpathy Tier 3 = open question → S242 YouTube research (VERIFIED, not Grok/Gemini summary)"
    - "Research integrity rule: external model summaries labeled UNVERIFIED, not treated as primary research"

next_session_bridges:
  s242: "_drafts/SESSION-BRIDGE-S242-ACTUAL-RESEARCH.md (3 parallel subagents, WebSearch/WebFetch)"
  s243: "_drafts/SESSION-BRIDGE-S243-PLANNING.md (reconcile research → write BUILD-SPEC-S244.md)"
  s244: "First build session (scaffolding, agent prompts, synthetic test)"

s237_pending_status:
  completed_this_session:
    - "wiki/_incoming/ created with README"
    - "wiki/entities/companies/jarvisydan.md stub created"
    - "NAMESPACE.md updated with jarvisydan + _incoming"
  still_pending:
    - "MEMORY.md one-pass compression (292 → <200 lines)"
    - "_drafts/ old bridge archive (S243)"
    - "git push --no-verify (manual terminal)"

key_files_arctic:
  - ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html
  - ~/1658HoldingsOy-AIFiles/output/arctic-cruises-outreach/website-improvement-spec.md

key_files_riikka:
  - ~/Desktop/ai-headhunter/wiki/companies/iqm-quantum.md   # URGENT Apr 25
  - ~/Desktop/ai-headhunter/outputs/BLOCKER-metric-needed.md

arctic_consumer_framing_corrected:
  consumer: "DACH river/lake cruise buyer — contemplative slow travel"
  price_anchor: "AmaWaterways/Viking €3,500-€9,000 vs our €2,600 — CONFIRMED CORRECT"
  ponant_role: "B2B partner target (they sell us), not consumer competitor"

arctic_decisions_s243:
  languages: "English-first ALL markets — no per-country language versions yet"
  sharepoint: "Teams team channel — Patrick sets up (not just SP folder)"
  hs_policy: "Saku + ship safety manual as raw material → impressive final doc"
  word_exports: "Still valid — HTML pipeline is primary, .docx as backup/print"
  immediate_fix: "Email laura@finlanddmc.fi → laura.ilvonen@finland-dmc.com in 4 HTML docs"

arctic_doc_gaps:
  critical: "Email fix in b2b-flyer, fam-invitation, fam-programme, operator-prd"
  english_pack_missing:
    - "Standalone commission/rates sheet (distributable PDF)"
    - "Standalone FAQ doc (distributable PDF)"
    - "Marketing materials pack (photo rights + usage guide for operators)"
  later: "Named naturalist per voyage (Saku to confirm), H&S Policy v1.0 (Saku + ship manual)"

tools_confirmed:
  gemini: "bash ~/run-gemini.sh --prompt-file /tmp/prompt.txt --model gemini-2.5-pro --output-file /tmp/out.txt"
  grok: "python3 ~/.claude/skills/grok-heavy-browser/main.py 'prompt' --model Expert --background"
  note_grok_echo: "max 1 Grok Expert call per Claude Code session (S164 echo bug)"
```
