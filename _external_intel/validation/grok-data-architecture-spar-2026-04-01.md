# Grok Heavy Spar — Data Architecture v1.0
**Date:** 2026-04-01 | **Mode:** Heavy (4-agent council)
**Target:** 1658 Holdings Data Storage Architecture v1.0

## Overall Verdict: NO GO (3/4 zones)
- Zone A: CONDITIONAL GO
- Zone B: NO GO (accidental sync/share risk)
- Zone C: NO GO (n8n reliability + ICM weakness + YT-laki + "staff never opens Obsidian")
- Zone D: NO GO (Excel MVP data decay + co-authoring)

## Key Challenges

### Excel MVP (Lucas + Benjamin + Harper)
- Data decays ~22%/year, 70.3% in worst cases
- Co-authoring creates version conflicts, format drift, no row-level audit
- Threshold cracks at 50-100 concurrent editors (not 200)
- Missing fields zero out scoring categories → biased toward cleanest records
- Alternative proposed: Supabase free tier from day 1

### n8n Cloud (Harper)
- "95% of workflows die within 48 hours" (community reports)
- Memory leaks in AI agent nodes, silent failures
- Cloud Starter limits burn fast with LLM calls
- Solo CEO can't provide monitoring needed

### ICM Folder Isolation (Benjamin)
- Security-by-obscurity: n8n workflow with Python node can os.walk other folders
- Not true sandbox — containment fails when LLM decides to explore

### YT-laki (Lucas)
- Post-2025 amendments: 50+ employees = continuous dialogue requirement
- Scorer + @booker = "technological change affecting work organisation"
- One missed employee-rep meeting = entire rollout illegal
- EU AI Act transparency obligations phasing 2025-2027

### Personal AI Secretary (Lucas)
- GDPR consent + AI Act + YT-laki dialogue = insurmountable for solo CEO
- Enhancement → surveillance dependency
- Hallucinated routing creates phantom tasks

### Unidirectional Flow (Lucas)
- "Culture beats architecture" — one curious sales rep or accidental share breaks it
- Family company = informal access patterns

### Scoring Model Gaps (Benjamin)
- Missing: competitor activity, group-size potential, NPS, shoulder-season differentiation
- No imputation strategy for missing fields → noisy output
- Complete cases avg 35pts vs overall 22.4pts (simulation)

## Agent Conflicts (unresolved)
1. Benjamin vs Lucas: Excel feasible locally vs data too dirty
2. Harper vs Benjamin: n8n unreliable vs Python scoring straightforward
3. Lucas vs Harper: YT-laki hard stop vs sparse precedents
4. Benjamin vs Harper: ICM not true sandbox vs smart low-budget containment
