# 1658 Holdings — Active Session Log

> **Load trigger:** Session review, pattern harvest, compression, or "what happened in session N?"
> **NOT auto-loaded at startup.** For current status, read CURRENT-STATUS.md.

---

## Rolling Window (Last 5 Sessions)

### Session 231 | Arctic Cruises V3.3 + 7-Bridge Pipeline + Orchestrator V2 | 2026-04-15

```yaml
session: 231
date: 2026-04-15
model: sonnet-4-6
project_type: strategic-research
duration: ~180min
cost: ~$6.50
session_tier: 2
attributed_value_eur: ~€25,000
human_interventions: 8
handoff_quality: 97
longest_autonomous_task_min: 20
first_turn_quality: high
kb_consulted: yes
kb_topics: [arctic-cruises, luxury-travel-marketing, b2b-tour-operator, autonomous-pipeline-design, multi-agent-orchestration]
patterns_harvested: [autonomous-pipeline-data-contract-pattern]
harvest_note: "1 Tier A pattern: data contract before multi-wave pipeline. Grok+Gemini unanimous — P(final correct)≈0.52 without shared PRICING-MASTER.json. Progressive commits + structural gate checks + wave isolation also confirmed. Saved to _shared/best-practices/autonomous-pipeline-data-contract-pattern.md"
recon_hits: 2
recon_used: 2
protocol_friction: 1
```

**S231 Work Summary — Arctic Cruises Sprint:**

1. V3.2 build: applied all 3 bridge copy gaps (visceral mid-lake moment, Why Saimaa/Why Now section, closing urgency). SEO: JSON-LD TouristTrip schema, canonical, OG tags. Pricing fixed throughout. Committed.
2. Gemini audit (92/100): 3 fixes — testimonial placeholders → bridge quotes (Saku/UNESCO/Patrick), FinnConcierge clarified, hero CTA price anchor removed.
3. V3.3 committed ef5a520. READY_FOR_LAUNCH: YES (Gemini verdict). Push pending.
4. Commercial brief locked: `_drafts/arctic-b2b-commercial-brief.md` — 20% commission, €320/€960/€2,080 net rates, FAM 31 Aug–3 Sep, apply by 15 Jul.
5. 5 session bridges written (S232-S236): B2B flyer → FAM pack → Operator PRD → Operations → Knowledge Bible. All chmod 444.
6. Orchestrator bridge S237 V1 written. Sparred with Grok+Gemini in parallel. Both models unanimous on 4 critical failures: no data contract, self-reported manifests, no progressive commits, write collisions.
7. Orchestrator V2 written with all 4 fixes applied. Launch prompt written: `_drafts/ARCTIC-PIPELINE-LAUNCH-PROMPT.md`.

warm_pack: SESSION-BRIDGE-S237-ARCTIC-ORCHESTRATOR-V2.md

---

### Session 231 | Riikka Go-Live Plan + 5-Bridge Roadmap | 2026-04-15

```yaml
session: 231
date: 2026-04-15
model: sonnet-4-6
project_type: strategic-research
duration: ~120min
cost: ~$4.50
session_tier: 2
attributed_value_eur: ~€8,000
human_interventions: 3
handoff_quality: 96
longest_autonomous_task_min: 25
first_turn_quality: high
kb_consulted: yes
kb_topics: [riikka-outreach, bittium-intel, finnish-market, cos-hiring, linkedin-optimization, executive-search, vpl-framework]
patterns_harvested: [finnish-ceo-closing-no-risk-reversal, proof-element-needs-metric, linkedin-interest-graph-first]
harvest_note: "3 patterns. (1) Finnish CEO close: remove Anglo-American 'you lose nothing' — confidence carries the close in direct-communication cultures. (2) Proof element needs metric not just role — engineering CEOs default to evidence. (3) LinkedIn: follow companies/CEOs BEFORE updating profile = algorithm warming before profile signals = better recruiter matching."
recon_hits: 3
recon_used: 3
protocol_friction: 2
```

**S231 Work Summary:**

Plan Mode session. Riikka go-live plan built end-to-end.

1. Bridge loaded → Plan Mode → wrote full go-live plan (Phases 2-4, 5 open decisions resolved)
2. Grok+Gemini VPL spar launched in parallel (adversarial + structural). Gemini: 4-block structure perfect, specificity excellent, 3 fixes: add metric, strip consultant-speak, remove "you lose nothing" close. Grok: original gets binned.
3. Toljamo VPL finalized: 129 words, Finnish-grounded. ⚠️ Riikka must fill [X]% milestone metric.
4. Pipeline tracker built: `wiki/pipeline.md` — hybrid table + YAML, 4 initial entries.
5. AMD cover letter drafted: ≤220 words + salary brief with RSU clause (€7-8k base, not floor).
6. LinkedIn activation checklist: 8 steps in correct order (companies/CEOs FIRST = algorithm warming).
7. Entity pages updated: bittium.md + petri-toljamo.md with S231 spar results.
8. 5 forward bridges written: S232-S236 (Phase 2 → Phase 3 → Phase 4 decision gate).

Gemini model troubleshooting: `gemini-2.5-pro-preview-05-06` and `gemini-2.5-pro-preview` both returned 404. Working model: `gemini-2.5-pro` (default in gemini-api/main.py). Context pack model reference `gemini-3.1-pro-preview` is stale — update.

warm_pack: SESSION-BRIDGE-S232-RIIKKA-LINKEDIN-CONTENT.md

---

### Session 230 | Riikka Pipeline + Arctic Cruises V3/V3.1 Build | 2026-04-15

```yaml
session: 230
date: 2026-04-15
model: sonnet-4-6
project_type: strategic-research
duration: ~240min
cost: ~$9.50
session_tier: 3
attributed_value_eur: ~€15,000
human_interventions: 18
handoff_quality: 97
longest_autonomous_task_min: 20
first_turn_quality: high
kb_consulted: yes
kb_topics: [riikka-outreach, bittium-intel, linkedin-optimization, finnish-market, executive-search, luxury-travel-marketing, saimaa-competitive-positioning]
patterns_harvested: [cos-hiring-vpl-trinity, agent-feedback-v2-loop, engineering-ceo-commercial-pivot-cos-signal, executive-salary-anchoring, endemism-pristinity-discovery-irreplaceable-usp]
harvest_note: "5 patterns this session. Riikka arc: (1) VPL+Trigger+Touchpoint trinity for CoS. (2) V2 feedback loop 3-5× better output. (3) Engineering CEO + commercial pivot = highest-conviction CoS signal. (4) Candidates underprice CoS — €6k vs AMD €7-8.5k actual. Arctic arc: (5) Endemism+Pristinity+Discovery = irreplaceable moat — fixed by geography/ecology, cannot be replicated by any competitor."
recon_hits: 3
recon_used: 2
protocol_friction: 1
```

**ARC 1 — Riikka Pipeline (16-agent intelligence layer):**

Executed full S228 Riikka bridge mandate. DDSC protocol: 8 v1 research agents in parallel → held until all complete → specific feedback to each → 8 v2 agents in parallel → synthesized into 4 wiki files.

**Key finding — Bittium:** Month 13 for CEO Toljamo (externally hired, advisory background, no ops experience), 4 senior leaders reset in 12 months, Glassdoor 2.5/5 ("chaotic management"), defence revenue +42%, no CoS in org chart. Highest-conviction target. Value prop letters written (Toljamo first DM 147w + full VPL 520w + Ahnger alternative 81w). NOT yet sparred or sent.

**Key finding — AMD:** Chief of Staff Helsinki (12-month FTC) = bull's-eye match. Application angle written. Riikka's €6k ceiling below AMD's likely €7,000-8,500 range — needs recalibration.

4 wiki files built: `recruiter-patterns.md`, `riikka-role-manifest.md`, `company-research-template.md`, `linkedin-scouting-protocol.md`. Bridge: `_drafts/SESSION-BRIDGE-S231-RIIKKA-SYSTEM-GOLIVE.md`.

---

**ARC 2 — Arctic Cruises V3/V3.1 Full Website Rebuild:**

Full rewrite of `arctic-cruises-b2c.html`: V2 (1,069 lines) → V3 (1,611 lines) → V3.1 (1,705 lines).

**Decisions locked (Patrick, S230):** 3 products (Day €420 / 3-night €1,200 / 7-night €2,600). Show price with value stack first. Expert team = real locals (Captain, Saku Hyttinen founder, Laura Ilvonen, Patrick H.). Accommodation = full Saimaa resort gallery (Sahanlahti, Pistohiekka, Järvisydän, Okkolan, Kuopio) — not fixed resorts. Real map image (saimaa-waterway-map.jpg) + SVG overlay. Breakfast at resorts not on board. FinnConcierge = "AI & Human powered personal assistant."

**New sections built:** Masonry gallery + lightbox, real map + SVG route overlay, resort gallery (5 destinations + CTA), 4-card authentic team, 3-product pricing cards, full-width value stack, 2027 departure calendar (Wed May–Sep), FAQ accordion (8Q), conservation (5% drinks → FANC), hamburger nav, proper inquiry form (mailto + honeypot).

**Competitive analysis (bridge):** Saimaa beats Norwegian fjord on price parity + discovery + warmth (18-24°C vs 8-14°C) + endemic species. Different audience from Caribbean. Beats European river cruises (30-70% cheaper, nature vs cities, highest target overlap). Irreplaceable differentiator: endemism + pristinity + discovery — fixed by geography, cannot be copied.

**Commits:** `739ab76` (V3) + `ed57651` (V3.1). Push pending (hook blocks — run `git push --no-verify origin main` manually).

**Bridge:** `_drafts/SESSION-BRIDGE-S231-ARCTIC-LAUNCH.md` — 3 copy gaps + 5-session roadmap (S231–S235). Website nearly complete; S231 = copy polish + SEO + Gemini audit → DONE.

---

### Session 229 | Arctic Cruises V3 Strategy — competitive research + brand positioning + bridge | 2026-04-15

```yaml
session: 229
date: 2026-04-15
model: sonnet-4-6
project_type: strategic-research
duration: ~90min
cost: ~$3.50
session_tier: 2
attributed_value_eur: ~€2,000
human_interventions: 14
handoff_quality: 96
longest_autonomous_task_min: 20
first_turn_quality: high
kb_consulted: no
kb_topics: []
patterns_harvested: [scenery-over-species-luxury-travel, luxury-relaxation-vs-adventure-language]
harvest_note: "Two Tier A patterns harvested (source: patrick). (1) Scenery over species: lead with landscape not flagship animal in luxury nature travel. (2) No expedition/Zodiac language for luxury relaxation audience (55+, low activity, high spend)."
recon_hits: 0
recon_used: 0
protocol_friction: 2
```

Full competitive intelligence session for Arctic Cruises V3 website rebuild.

Phase 1: Explore subagent researched 9 river cruise + fjord cruise companies (Viking, Scenic, AmaWaterways, Avalon, Emerald, Hurtigruten, HX, Flåm/Nærøyfjord, small vessel operators). Full pattern analysis: pricing psychology, conversion flows, trust signals, urgency tactics, messaging frameworks across categories.

Phase 2: Gemini 2.5 Pro (comprehensive A–G strategic analysis) launched via run-gemini.sh. Result saved: `_external_intel/validation/GEMINI-saimaa-cruise-marketing-20260414.md`. Grok returned cached wrong-prompt result — not usable.

Phase 3: Patrick decisions locked. Key: (1) Scenery is the hero product not the seal; (2) PRIMARY emotion = relaxation through beauty; (3) No Zodiac/expedition language — wrong audience; (4) Conservation = 5% of drinks onboard → FANC (simple micro-contribution); (5) Hero headline: "Finland, As Only a Few Will Ever See It"; (6) Target: DACH + UK + US + Australia, older affluent low-physical-activity travelers; (7) M/S Carelia has no cabins — use resort room mosaics.

Open questions for S230: (a) 3-night product alongside 7-night? (b) Show price or inquiry-only?

**Bridge:** `_drafts/SESSION-BRIDGE-S230-ARCTIC-V3-BUILD.md` — full V3 build spec, section order, messaging, open questions, technical notes.
**Patterns:** 2 × Tier A BP files + _index.yaml updated.

---

### Session 228 | Sunseeker V5 HTML Polish — layout fixes, typos, slide removal, overlay | 2026-04-15

```yaml
session: 228
date: 2026-04-15
model: sonnet-4-6
project_type: corporate-knowledge
duration: ~45min
cost: ~$1.50
session_tier: 2
attributed_value_eur: ~€300
human_interventions: 9
handoff_quality: 88
longest_autonomous_task_min: 8
first_turn_quality: high
kb_consulted: no
kb_topics: []
patterns_harvested: [always-push-open-html, headless-chrome-pdf-fail]
harvest_note: "Two patterns: (1) Always commit+push+open after HTML edit — Patrick explicit. (2) Headless Chrome fails on JS slideshows — stream timeout >60s, manual Cmd+P required."
recon_hits: 0
recon_used: 0
protocol_friction: 2
```

Loaded SESSION-BRIDGE-S221-SUNSEEKER-HIONTA.md. Executed 3 rounds of surgical HTML edits on `jahti-clubi/sunseeker-v5.html` (6 slides, 1.53MB).

Round 1 (bridge tasks): Slide 2 rewrite → 4 stat-cards + owner names. Slide 3 breakeven removed. Slide 4 "Itsenäinen asuminen." removed. Slide 5 Vaihtoehto A/B removed. Slide 7 removed (counter 7→6). Slide 1 overlay lightened.

Round 2 (Patrick corrections): Slide 4 3-col grid restored (previous session broke it to 2-col). Majoitusvuokraus + Charter side-by-side in value-highlight. Opastettu retki removed. Typo fixed: miehißtökulua → miehistökulua. VELATON vertically centered in node. Slide 6 heavy box → lightweight (harbor visible).

PDF attempt: headless Chrome `--print-to-pdf` stream closed at 60s — JS slideshow only captures slide 1. Print CSS injected to `/tmp/sunseeker-print.html` (all slides visible). Patrick does manual Cmd+P.

GitHub Pages link delivered: https://dmcfinland.github.io/presentations/jahti-clubi/sunseeker-v5.html

**Commits:** ccabaa4, dadc6d2, fff3071 (PDF gitignore-bypassed)
**Bridge:** SESSION-BRIDGE-S228-SUNSEEKER-PDF.md (PDF manual instructions)
**Warm pack:** `SESSION-BRIDGE-S228-SUNSEEKER-PDF.md`

---

### Session 227 | AI Coding Stack Research — 3-model pipeline, Codex model update, Cursor+xAI | 2026-04-14

```yaml
session: 227
date: 2026-04-14
model: sonnet-4-6
project_type: strategic-research
duration: ~60min
cost: ~$2.50
session_tier: 2
attributed_value_eur: ~€400
human_interventions: 8
handoff_quality: 92
longest_autonomous_task_min: 15
first_turn_quality: high
kb_consulted: no
kb_topics: []
patterns_harvested: [dual-model-judge-pipeline]
harvest_note: "Two judges (Gemini + Grok 4.20) > single judge. Near-zero cost. Different company biases catch different failure classes. BP file written."
recon_hits: 0
recon_used: 0
protocol_friction: 1
```

Pure AI tool research session. No project work. Full research-loop ran on Codex model options (quality: 4/5). Two Grok spars completed (Codex model comparison + Cursor/Codex/xAI architecture).

Key decisions: (1) Codex CLI: switch run.sh from o3 → gpt-5.2-codex after A/B test — o3 is superseded and expensive, gpt-5.4 degrades in multi-turn agentic loops; (2) 3-model build pipeline validated: Claude orchestrator + gpt-5.2-codex/grok-code-fast-1 builder + dual judge (Gemini 3.1 + Grok 4.20); (3) Gemini 3 confirmed real — upgrade run-gemini.sh to gemini-3.1-pro-preview; (4) Grok-code-fast-1 in Cursor needs mandatory scope constraints (over-edits without file boundaries); (5) Claude Sonnet is valid as builder for complex/production work — "orchestrator only" is too absolute; (6) Cursor + xAI EU status cleared via Cursor Privacy Mode.

Research outputs: research/openai-codex-models-2026/ + 2 Grok spar sessions.
BP file: _shared/best-practices/dual-model-judge-pipeline.md

**Deliverables:** SESSION-BRIDGE-S227-CODING-STACK.md (chmod 444)

**Warm pack:** `SESSION-BRIDGE-S227-CODING-STACK.md`

---

### Session 226 | Arctic Cruises V2 BUILD — route map + Day 1-7 timeline + Kuopio apex | 2026-04-14

```yaml
session: 226
date: 2026-04-14
model: sonnet-4-6
project_type: strategic-research
duration: ~30min
cost: ~$1.80
session_tier: 2
attributed_value_eur: ~€1200
human_interventions: 2
handoff_quality: 96
longest_autonomous_task_min: 18
first_turn_quality: high
kb_consulted: no
kb_topics: []
patterns_harvested: [complete-write-for-large-phase-builds]
harvest_note: "For 8+ phase builds where >50% of file changes: single Write is safer and more auditable than 12+ sequential Edits. Verified: 17/17 checklist first pass, no rework. Tier 3 observation — tool selection."
recon_hits: 0
recon_used: 0
protocol_friction: 1
```

Arctic Cruises B2C website V2 — executed pre-approved plan (glimmering-chasing-petal.md) from SESSION-BRIDGE-S225-ARCTIC-V2-BUILD.md. Single Write of complete rewritten HTML (999→~1100 lines). 8 phases executed in one operation.

Key changes delivered: (1) Single product — removed 3-Night Classic entirely; (2) Hero meta updated to 7-Night Closed Loop weekly rhythm; (3) New #route-map section with inline SVG (7 stops, Kuopio r=14 apex, Lappeenranta double-ring, outbound + return paths); (4) Two-column sticky layout: SVG map left, scrollable Day 1-7 timeline right; (5) Day 3+4 Kuopio apex treatment (dark navy #1a2332); (6) Return divider "The Return — Same Waters, Different Light"; (7) Seal PRD-required phrase added; (8) IntersectionObserver scroll activation (replaced switchTab); (9) Nav Route link; (10) Pricing table Classic row removed; (11) Sanctuary tags updated.

UX decision not in plan: route map + itinerary MERGED into one section (required for sticky layout to work). Correct call.

Push blocked by two-layer hook system — Patrick to run `git push --no-verify origin main` manually.

Verification: Explore subagent ran 17-item checklist → 17/17 PASS.

**Deliverables:** `arctic-cruises-b2c.html` V2 committed `f955ebb` · SESSION-BRIDGE-S227-ARCTIC-V2-VISUAL-POLISH.md (chmod 444)

**Warm pack:** `SESSION-BRIDGE-S227-ARCTIC-V2-VISUAL-POLISH.md`

---

### Session 225 | Riikka Wiki Build — Bittium deep entity + 5 subagents + CoS letter | 2026-04-14

```yaml
session: 225
date: 2026-04-14
model: sonnet-4-6
project_type: strategic-research
duration: ~60min
cost: ~$2.50
session_tier: 2
attributed_value_eur: ~€1200
human_interventions: 4
handoff_quality: 93
longest_autonomous_task_min: 12
first_turn_quality: high
kb_consulted: yes
kb_topics: [wiki-entity-page-pattern, you-centric-outreach]
patterns_harvested: [subagent-bash-permission-required]
harvest_note: "General-purpose subagents need Bash/WebFetch pre-approved — one agent (Hulkko) failed silently. Pattern: prompt subagents with permission context or handle low-priority research in main thread."
recon_hits: 2
recon_used: 2
protocol_friction: 2
```

S225 = Riikka Wiki Build session. S224 was Arctic Cruises (already done); this session executed the S224 bridge mandate (Riikka wiki).

5 parallel subagents launched:
- agent-ahnger ✅ — Full Ahnger profile: Åbo Akademi ChemEng, PE (Helmet Capital 4yr), Patria 5yr VP, Bittium Jan 2025. Finland-Swede. Chairman MarshallAI. Low public profile.
- agent-toljamo ✅ — Toljamo deep: Elektrobit 14yr (Nokia-DNA, 1996-2010), Anite/Keysight 9yr (sold wireless testing tools), HT Growth 3yr, Bittium board 2018-2025, CEO Apr 2025. Active LinkedIn, 264 comments on appointment.
- agent-rohde ✅ — D-LBO failure confirmed: €2.9B contract, 2 test failures (May+Nov 2025), "danger to life", delayed to 2030s. Bittium = a4ESSOR partner (with R&S) → opportunity is supplementary ESSOR contracts, not head-to-head replacement. Rheinmetall = primary alternative integrator.
- agent-q1 ✅ — FY2025 confirmed: EUR 119.3M (+40.1%), EBIT EUR 19.4M (16.3%). FY2026 guidance: EUR 140-155M / EUR 26-32M. Q1 2026 due April 29 (silent period). EBIT correction: 16.3% = margin, absolute = EUR 19.4M.
- agent-hulkko ❌ — Bash blocked in subagent session. Hulkko = stub only.

Wiki built: ~/Desktop/ai-headhunter/wiki/
- companies/bittium.md ← full schema (strategic context, financials, transformation gap, D-LBO angle, competitive position, application angles)
- contacts/erik-ahnger.md ← deep profile (PE→defense arc, Finland-Swede, outreach notes)
- contacts/petri-toljamo.md ← deep profile (Nokia-DNA, Keysight CEO, board insider 6yr, key quotes)
- applications/bittium-cos-20260414.md ← CoS application letter (FI+EN), Gemini validation pending
- _index.md ← master index

EBIT correction: internal records had "EUR 16.3M EBIT" which was wrong — 16.3% is the margin. Absolute = EUR 19.4M. Corrected in wiki.

**Warm pack:** `SESSION-BRIDGE-S225-ARCTIC-V2-BUILD.md` (Arctic V2 is the next build session)

---

### Session 224 | Arctic Cruises — B2C Website V2 spar + PRD legal review + plan approved | 2026-04-14

```yaml
session: 224
date: 2026-04-14
model: sonnet-4-6
project_type: strategic-research
duration: ~60min
cost: ~$2.00
session_tier: 2
attributed_value_eur: ~€800
human_interventions: 8
handoff_quality: 95
longest_autonomous_task_min: 8
first_turn_quality: high
kb_consulted: no
kb_topics: []
patterns_harvested: [grok-plan-refinement-diminishing-returns]
harvest_note: "Grok improves plans technically in round 1 (integrate), but rounds 2+ are tone-only rewrites. Stop updating after round 1. S224 had 3 ExitPlanMode rejections — rounds 2+3 were identical content."
recon_hits: 0
recon_used: 0
protocol_friction: 3
```

Arctic Cruises B2C website V2 planning session. Loaded S222 Arctic bridge, fired Gemini + Grok spars in parallel. Gemini (complete, 5/5): vertical SVG map + sticky layout + single Day 1-7 timeline = correct UX for €2,800pp. Grok website spar partial (CDP capture issue — only 1 line). Patrick also pasted a separate Grok PRD legal review (EU PTD compliance, superlatives, organiser clarity) — saved to external_intel.

Plan Mode: 8 changes specified across hero, voyage section, new route map section (SVG inline, 7 stops, scroll-activated), itinerary rebuild (Days 1-7, return divider, Kuopio apex), seal disclaimer (line 404 existing text close but not exact). Grok refined plan 3× — round 1 technical (integrated: rootMargin, WCAG, SVG accessibility, pricing qualifiers), rounds 2-3 tone-only (not integrated after pattern identified).

Key discoveries from live file: section is "Curate Your Voyage" (not "Choose Your Voyage"), seal section already has "We do not guarantee sightings" at line 404 but needs exact PRD phrase.

**Deliverables:** SESSION-BRIDGE-S225-ARCTIC-V2-BUILD.md (chmod 444) · GEMINI+GROK spar results to external_intel · Plan approved + saved at ~/.claude/plans/glimmering-chasing-petal.md · GROK-SPAR-arctic-prd-legal-review-S222.md (PRD v3.1 action items)

**Warm pack:** `SESSION-BRIDGE-S225-ARCTIC-V2-BUILD.md`

---

### Session 223 | Riikka — Bittium syvätutkimus + 5 company entity + outreach briefing + Gemini spar | 2026-04-14

```yaml
session: 223
date: 2026-04-14
model: sonnet-4-6
project_type: strategic-research
duration: ~90min
cost: ~$3.50
session_tier: 2
attributed_value_eur: ~€1500
human_interventions: 6
handoff_quality: 92
longest_autonomous_task_min: 9
first_turn_quality: high
kb_consulted: yes
kb_topics: [riikka-profile, bittium-outreach, company-wiki-entities]
patterns_harvested: [you-centric-outreach-reframe]
harvest_note: "You-centric reframe: alkuperäinen viesti 6/10 (I-centric), Gemini sparrattu versio 9/10. Kaikki cold outreach pitää aloittaa heidän haasteestaan, ei omasta hausta. Universaalisesti sovellettava."
recon_hits: 2
recon_used: 2
protocol_friction: 1
```

Riikka AI headhunter S223 — täysi outreach pipeline rakennettu. Plan Mode + 5 rinnakkaista company research -subagenttiä (Bittium, Nokia Oulu, JOT Automation, Plugit Finland, ALTEN Finland). Selector valitsi Bittiumin (score 10/10) — ainoa jolla eksplisiittinen "data-driven scalable model" -pilari strategiassa, uusi CEO Petri Toljamo ja VP BD Erik Ahnger molemmat ulkopuolelta tuotuja muutosagentteja, Glassdoor 2.5/5 = transformaatioarkkitehdille täydellinen ympäristö.

Bittium syvätutkimus (erillinen subagent): EUR 119.3M / 16.3% EBIT 2025, Indra-deal EUR 140M total, CMD syyskuu 2025 = 4 pilaria, Rohde & Schwarz D-LBO -epäonnistuminen Saksassa avaa markkinaraon. Kaikki johtoryhmän jäsenet uusia (2025–2026) — external-hire-aalto = muutosagendalle tilausta.

Gemini 2.5 Pro spar: alkuperäinen LinkedIn DM 6/10 (I-centric), kirjoitettiin uusi 9/10 versio (You-centric: "Petri Toljamon mandaatti asettaa klassisen eksekointihaasteen insinöörivetoiselle organisaatiolle"). Grok partial capture — tekninen ongelma, yksirivinen vastaus. Pipeline-korjaukset: CoS hakusanat + kuntarekry-suodatin tiukennettu.

**Deliverables:** 5 entity pagea · pipeline-tracker.yaml · bittium-briefing v2 (Gemini-sparrattu) · job_scraper.py korjattu · SESSION-BRIDGE-S223 protected

**Warm pack:** `SESSION-BRIDGE-S223-RIIKKA-BITTIUM.md`

---

### Session 222 | Tonttirahoitus — Arviokirja löytyi, vuokrasopimukset kartoitettu, pakettitilanne | 2026-04-14

```yaml
session: 222
date: 2026-04-14
model: sonnet-4-6
project_type: strategic-research
duration: ~45min
cost: ~$1.20
session_tier: 2
attributed_value_eur: ~€2000
human_interventions: 9
handoff_quality: 85
longest_autonomous_task_min: 6
first_turn_quality: high
kb_consulted: yes
kb_topics: [tonttirahoitus, rahoituspaketti, kiinteistöarvio]
patterns_harvested: [captive-tenant-bank-argument]
harvest_note: "Captive tenant -argumentti: vuokranmaksun laiminlyönti = toiminnan alasajo. Järvisydän-spesifinen mutta yleisesti sovellettava kiinteistörahoituksessa."
recon_hits: 2
recon_used: 1
protocol_friction: 2
```

Tonttirahoituspaketin due diligence -sessio. Löydettiin olemassa oleva arviokirja (Lahden Kiinteistönotariaatti, 15.9.2025, vakuusarvo, Markus tilaaja) — G8-tilaus peruttu, säästetään ~3vk + €2-5k. Rasitustodistus 1-169 löytyi jo arkistosta. Kiinteistötunnus haamu korjattu: bridgeissä esiintynyt 681-418-1-150 poistettu wiki-entiteetistä ja selvittaja-hakemus-luonnoksesta — oikea tunnus on **681-418-1-106** (Järvisydän, 15.4 ha). Tämä vahvistettu suoraan arviokirjasta.

Vuokrasopimukset kartoitettu: toimisto+parkkialue (1-106, ~1700 m²) = **6 000 €/v**, kausi 2023–2048. Loput L1–L10 sopimukset (arviokirjasta: 10 vuokra-aluetta) lukematta — kokonaisvuokra selvitettävä Teemulta tai lukemalla sopimukset. Isän tieto 80k€ linjassa alkuperäisen S217 lähde-dokumentin kanssa — 120k€ on todennäköisesti uusi neuvottelutavoite.

Teams-viesti Teemulle kirjoitettu (lyhyt, ihmismäinen). Captive tenant -argumentti muodostettu pankkia varten: parkkialueet + tiet + rantavyöhyke = Järvisydän ei toimi ilman näitä. DSCR 2.13× (80k) riittää rahoitukseen.

**Paketti puuttuvat:** Sebastian HETU (17.4.) + Teemu-vastaus (30.4.) + MML-todistukset (tilata nyt) + Liite TA/V (Patrick täyttää).

**Deliverables:** Kiinteistötunnus korjattu 2 tiedostossa · Teams-viesti Teemulle · captive-tenant-bank-argument.md · pakettitilanne selvillä

**Warm pack:** `SESSION-BRIDGE-S222-VUOKRA80K.md` + `SESSION-BRIDGE-S222-RAHOITUSPAKETTI-FINAL.md`

---

*(Sessions S220-S221 archived to SESSION-ARCHIVE-FULL.md + SESSION-ARCHIVE.md at S226 compression, 2026-04-14)*


### Session 220 | Arctic Cruises — PRD v3 World-Class + B2C Website Live | 2026-04-14

```yaml
session: 220
date: 2026-04-14
model: sonnet-4-6
project_type: strategic-research
duration: ~60min
cost: ~$2.80
session_tier: 2
attributed_value_eur: ~€4000
human_interventions: 5
handoff_quality: 93
longest_autonomous_task_min: 20
first_turn_quality: high
kb_consulted: yes
kb_topics: [arctic-cruises, b2c-product-design, web-conversion, expedition-travel, conservation-storytelling]
patterns_harvested: []
harvest_note: "nothing new — execution sprint from spar results. All architectural decisions made in S219 bridge. Both Grok+Gemini spars fired + integrated. PRD v3 + HTML built in sequence."
recon_hits: 2
recon_used: 2
protocol_friction: 1
```

Loaded S219 Arctic B2C bridge. Fired Grok Expert (189 sources, 52s thinking) + Gemini 2.5 web conversion audit in parallel. Grok: 5 changes to 95+/100 — named conservation (FANC/Metsähallitus), expedition team, full inclusions matrix, Carelia refit framing, narrative-first storytelling. Gemini: 65/100 web readiness — section reorder (Signature Moments → position 3), 9 progressive CTAs, E-E-A-T section, hero video brief.

Built PRD v3 (~3,000 words, 10 sections + appendix) integrating all findings. Then converted full PRD to world-class single-page HTML website — sticky header, 11 sections, tab accordions for itineraries, 9 CTAs, expedition team cards, E-E-A-T block, partner logos. Deployed to GitHub Pages.

**Deliverables:** `ArticCruises-AIFiles/project-files/arctic-cruises-customer-prd-v3.md` · `arctic-cruises-b2c.html` (live) · 2 spar intel files · `SESSION-BRIDGE-S220-ARCTIC-B2C-LIVE.md` (chmod 444)

**Live URL:** `https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html`

**Open placeholders:** expedition team names/photos · €X conservation amount · cabin count for 2027

**Warm pack:** `SESSION-BRIDGE-S220-ARCTIC-B2C-LIVE.md`

---

### Session 218 | Tonttirahoitus — Siivous + Kaikki doc-päivitykset + Projekti-esitys + S219 Bridge | 2026-04-13

```yaml
session: 218
date: 2026-04-13
model: sonnet-4-6
project_type: document-import
duration: ~45min
cost: ~$1.20
session_tier: 2
attributed_value_eur: ~€800
human_interventions: 4
handoff_quality: 90
longest_autonomous_task_min: 15
first_turn_quality: high
kb_consulted: no
kb_topics: []
patterns_harvested: []
harvest_note: "nothing new — execution-only session. All logic from S217 bridge. Bulk file ops: delete 9 old files, archive 8 bridges, rewrite 5 docs, build 10 new .docx via pandoc."
recon_hits: 0
recon_used: 0
protocol_friction: 1
```

Ladattu S218 bridge. **Vaihe 1 — Siivous:** poistettu 6 temp-tiedostoa + 3 vanhentunutta, arkistoitu 8 vanhaa landplot-bridgeä `_archive/landplot-bridges/`. **Vaihe 2 — Päivitykset:** G1 (VSV 3200→2400€), G2 täysin uudelleenkirjoitettu (myyjä Markus→V&V Holidays Oy, kauppahinta 450k→325k€, G8-blokkerilauseke), G3 (LKJS+JS vahvistettu), Cover Letter (557k→423k€, DSCR 2,44→3,20×, LTV 31,8→24,2%), Cashflow (kaikki stressitestit 423k:n pohjalta). **Vaihe 3:** `landplot-projekti-2026.md` 7-osainen päätuotos rakennettu. Kaikki vanhat .docx poistettu → 10 uutta pandocilla. S219 bridge luotu: avoimen blokkerianalyysi (G8/Sebastian HETU/Tengman/Junno) + rebuild-komento.

**Deliverables:** 10 × .md + 10 × .docx (kaikki ajantasaiset luvut) · `SESSION-BRIDGE-S219-LANDPLOT-BANK-READY.md`

**Warm pack:** `SESSION-BRIDGE-S219-LANDPLOT-BANK-READY.md`

---

### Session 219 | Arctic Cruises — Deck Fixes + Strategy Pivot + 4× Spar + Customer PRD Bridge | 2026-04-13

```yaml
session: 219
date: 2026-04-13
model: sonnet-4-6
project_type: strategic-research
duration: ~90min
cost: ~$3.50
session_tier: 2
attributed_value_eur: ~€3000
human_interventions: 8
handoff_quality: 92
longest_autonomous_task_min: 20
first_turn_quality: high
kb_consulted: yes
kb_topics: [arctic-cruises, b2b-deck, product-positioning, grok-spar, gemini-api, fam-strategy]
patterns_harvested: [b2c-first-product-sequencing, fam-urgency-without-capacity]
harvest_note: "2 Tier 1 BPs. Strategic pivot: Patrick confirmed B2C-first build order. Both Grok+Gemini rated deck 45/100. 4× external spars (deck quality ×2 + PRD positioning ×2). Unanimous: 'Grand Cruise on Lake Saimaa' > 'Arctic Cruises' for B2C. 'Finland's Last Secret' hook. Agency hook: 'Chase seals no one else on Earth can see — from a floating hotel.' Deck parked pending Customer PRD."
recon_hits: 2
recon_used: 2
protocol_friction: 2
```

Loaded S217 Arctic deck bridge. Applied 5 fixes to `arctic-cruises-operator.html` (11 slides). Deep factual audit: 7 issues found. 4× Grok+Gemini spar. Patrick confirmed: €320 net, ~500 seals, no Savonlinna overnight, FAM capacity suppressed, "Grand Cruise on Lake Saimaa" as B2C name, FinnConcierge = cruise AI. PRD bridge written (chmod 444). Operator deck parked — correct order is Customer PRD first.

**Patrick decisions locked:** Net €320, ~500 seals, no Savonlinna overnight, no FAM number published, Grand Cruise on Lake Saimaa = B2C name, FinnConcierge = cruise assistant, build order: PRD → deck v3 → FinnConcierge.

**Deliverables:** `arctic-cruises-operator.html` (11 slides, not deployed) · `SESSION-BRIDGE-S218-ARCTIC-PRD-CUSTOMER.md` · 4× spar intel files · `b2c-first-product-sequencing.md` (Tier 1) · `fam-urgency-without-capacity.md` (Tier 1)

**Warm pack:** `SESSION-BRIDGE-S218-ARCTIC-PRD-CUSTOMER.md`

---

### Session 217-COSME [PARALLEL] | COSME Grant Pipeline + Consortium Design | 2026-04-13

```yaml
session: 217-COSME
date: 2026-04-13
model: sonnet-4-6
project_type: strategic-research
duration: ~120min
cost: ~$3.50
session_tier: 2
attributed_value_eur: ~€5000
human_interventions: 8
handoff_quality: 90
longest_autonomous_task_min: 20
first_turn_quality: high
kb_consulted: yes
kb_topics: [audio-pipeline, codex-wrapper, cosme-grant, eu-consortium-design]
patterns_harvested: [audio-to-analysis-pipeline, cosme-thematic-route-eligibility, eu-consortium-payroll-norm]
harvest_note: "3 harvests: (1) Audio→Gemini→Claude→Codex→Gemini pipeline BP luotu. (2) COSME thematic route = Finland voi osallistua ilman fyysistä yhteyttä. (3) EU-konsortiossa jokainen partneri maksaa omalta palkkalistaltaan — WP-leader EI siirry lead-organisaatiolle."
recon_hits: 2
recon_used: 2
protocol_friction: 2
```

**Mitä tehtiin:**
- Q&A-tallenne (59MB) transkriboitu Gemini 2.5 Prolla → 295 riviä, 8314 sanaa
- Codex-analyysi ajettiin isolated-tilassa → kattava eligibility-matriisi
- Gemini strategic judge → LOW probability nyt, MEDIUM jos Maakuntaliitto+PM löytyy 2vk
- Gemini consortium spar → "dream team" design: FI+DE+IE+PL, 6 partneria
- Grok kill vectors → KV: Maakuntaliitto DMO-status todistamaton = automaattinen hylkäys
- DMC-GRANT-STRATEGY-2026.md päivitetty → Section 8 COSME lisätty
- Session bridge: `SESSION-BRIDGE-S217-COSME-CONSORTIUM.md`

**Kriittiset löydöt:**
- COSME vaatii MIN 4 maata + min 3 DMO:ta + min 2 BSO:ta
- Thematic route sallittu → Saimaa ei tarvitse fyysistä yhteyttä Shannoniin
- Saksa (Mecklenburg) = paras partneri (9/10)
- Finland DMC = WP2-leader, ~€200k projektibudjetti, oma palkkalista OK

**Warm pack:** `SESSION-BRIDGE-S217-COSME-CONSORTIUM.md`

---

### Session 216-AC [PARALLEL] | Arctic Cruises — Operator Deck Build + Double Spar + Positioning Shift | 2026-04-13

```yaml
session: 216-AC
date: 2026-04-13
model: sonnet-4-6
project_type: strategic-research
duration: ~120min
cost: ~$3.00
session_tier: 2
attributed_value_eur: ~€3000
human_interventions: 9
handoff_quality: 88
longest_autonomous_task_min: 20
first_turn_quality: high
kb_consulted: yes
kb_topics: [html-presentation, b2b-sales-deck, contact-sheet-workflow, gosaimaa-cdn]
patterns_harvested: [contact-sheet-photo-workflow, fam-invite-not-info, s8-pricing-split, premium-not-luxury-heritage, alcohol-inclusion-framing]
harvest_note: "5 patterns. BP written: contact-sheet-photo-workflow.md. template-notes.md updated: FAM=invite/S8-split/premium-not-luxury/alcohol-framing. grok-spar/NOTES.md created (echo bug). Grok echo bug second confirmed occurrence."
recon_hits: 2
recon_used: 2
protocol_friction: 2
```

**Mitä tehtiin:** Photo search (GoSaimaa CDN). Contact sheet updated. Deck built: `arctic-cruises-operator.html` (10 diaa). 2× Gemini spar → 5 fixes. Positioning shift: premium (not luxury), €320 net/€400 list, 20% min commission, no alcohol, FAM 80 quality-selected. Bridge S217-ARCTIC built.

**Key: source: patrick** — "Premium not luxury for heritage vessel."

**Warm pack:** `SESSION-BRIDGE-S217-ARCTIC-DECK-BUILD.md`

---

### Session 218 | Wiki + Obsidian + Session End Protocol Redesign — Grok+Gemini Spar | 2026-04-13

```yaml
session: 218
date: 2026-04-13
model: sonnet-4-6
project_type: system-maintenance
duration: ~45min
cost: ~$1.20
session_tier: 2
attributed_value_eur: ~€1500
human_interventions: 4
handoff_quality: 93
longest_autonomous_task_min: 15
first_turn_quality: high
kb_consulted: yes
kb_topics: [karpathy-wiki, obsidian-integration, session-end-protocol, session-compression]
patterns_harvested: [wiki-entity-page-pattern, session-end-wiki-delta-stub]
harvest_note: "2 Tier A BPs. Grok+Gemini spar killed naive deferred-compile approach (both 3/10 independently). Revised: wiki stays in Zone A not Obsidian vault, session end = stub+delta only, compilation at session startup. KV3 (directory split) = THE real blocker — fixed by Obsidian vault → Zone A root."
recon_hits: 1
recon_used: 1
protocol_friction: 1
```

**Deliverables:** `wiki-entity-page-pattern.md` (Tier A) · `session-end-wiki-delta-stub.md` (Tier A) · GROK+GEMINI spar files · bridge S217-WIKI (chmod 444) · wiki/log.md updated

**Warm pack:** `SESSION-BRIDGE-S217-WIKI-OBSIDIAN-PROTOCOL-REDESIGN.md`

---

### Session 217 | Tonttirahoitus — Grok+Gemini spar + 5 dok päivitys + logic lock | 2026-04-13

```yaml
session: 217
date: 2026-04-13
model: sonnet-4-6
project_type: document-import
duration: ~90min
cost: ~$2.50
session_tier: 2
attributed_value_eur: ~€2000
human_interventions: 6
handoff_quality: 82
longest_autonomous_task_min: 15
first_turn_quality: high
kb_consulted: yes
kb_topics: [landplot-financing, session-bridge-protocol, grok-spar]
patterns_harvested: [multi-session-logic-lock, vieraspantinantaja-rakenne]
harvest_note: "2 Tier 1 harvests (source: patrick): (1) Logic lock ennen analyysia — multi-session projekteissa ydinlogiikka kirjattava ja tarkistettava ENNEN kuin Grok/Gemini-löydöksiä kirjoitetaan dokumentteihin. (2) Markus = vieraspantinantaja — menettää tontit, ei myy. Luovutusvoittovero = väärä kehys."
recon_hits: 2
recon_used: 2
protocol_friction: 4
```

**Mitä tehtiin:** Luettu S216 bridge + 5 vanhentunutta landplot-dokumenttia. Päivitetty human-package v3 (V&V myyjäksi, 325k€, DSCR 3.20×). Grok+Gemini spar. **Patrick korjasi VAKAVASTI:** Markus = vieraspantinantaja — ei myyjä, ei kassasuoritusta. Kaikki 4 dokumenttia → v3. Tiedostoauditointi: 3 poisto + 8 arkisto + 9 päivitystarvetta.

**Warm pack:** `SESSION-BRIDGE-S218-LANDPLOT-CLEANUP-AND-DECK.md`

---

*(Sessions S203, S210–S216 archived to SESSION-ARCHIVE-FULL.md + SESSION-ARCHIVE.md at S219 compression, 2026-04-13)*

*(Session 209 archived to SESSION-ARCHIVE.md at S214 compression, 2026-04-13)*

*(Sessions S184–S208 archived to SESSION-ARCHIVE-FULL.md + SESSION-ARCHIVE.md at S209 compression, 2026-04-13)*

*(Sessions 174-184 archived to SESSION-ARCHIVE-FULL.md + SESSION-ARCHIVE.md at S189 compression, 2026-04-12)*

*(Sessions 163-173 archived to SESSION-ARCHIVE-FULL.md + SESSION-ARCHIVE.md at S180 compression, 2026-04-12)*

*(Sessions 160-162 archived to SESSION-ARCHIVE-FULL.md + SESSION-ARCHIVE.md at S170 compression, 2026-04-02)*

*(Sessions 155-159 archived to SESSION-ARCHIVE-FULL.md + SESSION-ARCHIVE.md at S165 compression, 2026-04-02)*

*(Sessions 151-154 archived to SESSION-ARCHIVE-FULL.md + SESSION-ARCHIVE.md at S159 compression, 2026-04-02)*
*(Sessions 147-150 archived to SESSION-ARCHIVE-FULL.md + SESSION-ARCHIVE.md at S154 Opus Review 9 compression, 2026-04-02)*
*(Sessions 142-143 archived at S149 compression, 2026-04-02)*
*(Sessions 138B-141 archived at S146-S149 compressions, 2026-04-01/02)*
*(Sessions 131-138A archived at S141 compression, 2026-04-01)*
