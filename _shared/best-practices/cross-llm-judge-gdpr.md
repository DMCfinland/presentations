# Cross-LLM Judge — API Privacy & GDPR Reference

**Decision date:** 2026-03-17 | **Updated:** 2026-03-17 (Round 2 Grok research)
**Source:** Grok Heavy (Harper+Benjamin+Lucas) × 2 rounds + Patrick session 85

## Decision

**Use Mistral Large 3 (Mistral AI La Plateforme) as the automated cross-LLM Judge.**

Rationale: EU-native company (France), EU-only infrastructure (OVHcloud/Deutsche Telekom),
binding French/EU law only — no CLOUD Act / FISA exposure. Full data sovereignty.
Smaller Elo gap to Sonnet 4.6 Worker than Gemini Flash. Lucas: Gemini fails first on subtle
false PASSes; Mistral failure mode (over-literal) is less dangerous for a Judge.

**Benchmark evidence (LMArena Elo, March 2026):**
- Claude Sonnet 4.6 (Worker): 1446 | MMLU-Pro 87.3% | AAII 65
- Mistral Large 3 (Judge): **1428** (-18 pts) | MMLU-Pro 81% | AAII 40
- Gemini 2.5 Flash: 1412 (-34 pts) | MMLU-Pro 83.2% | AAII 56
- Composite score (7 criteria normalized): Mistral 81.2 vs Gemini 78.4

Neither model is smarter than Sonnet 4.6. Gap is small enough for structured PASS/FAIL
evaluation — Judge needs to be hard to fool, not more creative than the Worker.

**Cross-validation: Gemini Deep Research independently confirmed Mistral Large 3 (March 2026)**
Key new finding: Gemini Flash has "sycophancy bias" — agrees with Worker's confident tone rather
than checking logic. Flash = System 1 (fast/intuitive). Mistral = System 2 (slow/analytical).
For a Judge, System 2 is required. Mistral's MoE architecture enforces structured schema strictness.
Mistral Large 3 is also open-weights — self-hosting possible if data sensitivity requires zero cloud.

**Previous decisions revised:**
- Round 1: Vertex AI → revised out (CLOUD Act applies to Google US parent regardless of EU region)
- Round 2: Gemini 2.5 Flash vs Mistral → Mistral wins (compliance + smaller capability gap)
- Round 3: Gemini cross-validation → Mistral confirmed independently (sycophancy bias finding added)

---

## Model comparison — EU-available, no-training, Judge-capable (Grok-verified 2025-2026)

| Model | Provider | EU region | No-training guarantee | Cost/call (20K+2K tokens) | Monthly (500 calls) | GDPR risk |
|-------|----------|-----------|----------------------|--------------------------|---------------------|-----------|
| **Mistral Large 3** | **Mistral AI (EU-native)** | **EU-native (France/OVH/DT)** | **Yes — EU law, no US jurisdiction** | **$0.013** | **$6.50** | **LOW** |
| Gemini 2.5 Flash | Google Vertex AI | europe-west1/west3/west4 | Yes — Service Terms §17 + ZDR | $0.011 | $5.50 | MED |
| Mistral Large 3 | AWS Bedrock EU | Ireland/Milan/Frankfurt/Paris | Yes — Bedrock + Mistral commitments | $0.015 | $7.65 | MED |
| GPT-4o | Azure OpenAI EU | West/North Europe, Switzerland | Yes — Microsoft Product Terms + DPA | $0.070 | $35.00 | MED |
| Claude 3.5 Sonnet | AWS Bedrock EU | Frankfurt/Paris/Milan/Stockholm | Yes — Bedrock + Anthropic | $0.180 | $90.00 | MED |

**All MED-risk providers = US parent company → CLOUD Act applies regardless of EU region or DPA.**
Only Mistral AI (EU-native) achieves LOW risk.

---

## Why Mistral wins over Vertex AI

| Criterion | Mistral Large 3 | Vertex AI (Gemini Flash) |
|-----------|----------------|--------------------------|
| EU jurisdiction | French/EU law only | US parent (Google) — CLOUD Act applies |
| CLOUD Act exposure | None | Yes (metadata/control plane reachable) |
| Data residency | EU-native infrastructure | EU-region, but US parent |
| No-training guarantee | Contractual + EU law | Contractual + Service Terms §17 |
| Cost/month (500 calls) | $6.50 | $5.50 |
| Reasoning capability (Judge) | Strong (instruction-following) | Strong |
| GDPR risk tier | LOW | MED |

$1/month difference is not a factor. Compliance gap is significant.

---

## Contractual steps for Mistral (do in order)

1. Create account at console.mistral.ai (La Plateforme)
2. Select enterprise tier or sign DPA equivalent (available on request)
3. Confirm data stays in EU infrastructure (OVHcloud/Deutsche Telekom) — documented in privacy policy
4. Use `mistral-large-latest` model via API — no extra configuration needed for EU residency
5. In Judge calls: standard API call, no special flags needed for training exclusion (default excluded)

**Fallback:** If Mistral service degrades → Vertex AI (europe-west1, Gemini 2.5 Flash, ZDR configured) as secondary. Accept MED risk for fallback only.

---

## Implementation path

**Option A — Bash + curl (solo/manual)**
```bash
curl -X POST https://api.mistral.ai/v1/chat/completions \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mistral-large-latest",
    "messages": [{"role": "user", "content": "JUDGE_PROMPT_HERE"}],
    "temperature": 0.1
  }'
```
Cost: ~$0.013/Judge call.

**Option B — n8n webhook Judge (integrated)**
- n8n node: HTTP Request → api.mistral.ai/v1/chat/completions
- Input: PWJ output file path + criteria + FAIL context
- Output: PASS/FAIL JSON response → feed back into loop
- Integrates with existing CRM n8n infrastructure

**Next step to implement:** /service skill → Mistral API key setup → test curl call → wire into /pwj loop.

---

## Cost estimate (~500 Judge calls/month)

Using Mistral Large 3 (20K input + 2K output tokens/call):
- Input: 500 × 20K × $0.50/MTok = $5.00
- Output: 500 × 2K × $1.50/MTok = $1.50
- **~$6.50/month total for 500 Judge calls**

vs same-model Sonnet Judge: ~$90/month (Claude 3.5 Sonnet via Bedrock)
vs Vertex AI Gemini Flash: ~$5.50/month (MED risk — saved $1, added CLOUD Act exposure)

---

## Lucas's residual risk (acknowledged, not eliminated)

Even Mistral: relies on OVHcloud/Deutsche Telekom as infrastructure partners.
Partner contracts could theoretically change. Data at rest is encrypted, but key management
via partners introduces a thin residual layer.

**This is materially lower than CLOUD Act exposure** — French/EU law governs, no US sovereign
compulsion path exists. Residual Mistral risk is operational (partner reliability), not legal.
Accepted.

**Do not send in any Judge call:** raw client names, exact financial figures, personally
identifying info. Send anonymized/summarized outputs for judgment. Belt + suspenders.

---

## Mistral Large 3 Judge System Prompt (Gemini-designed, March 2026)

```
## ROLE: SKEPTICAL QUALITY AUDITOR
You are an expert Quality Assurance Judge. Your task is to evaluate a document produced by a "Worker" against a set of "Acceptance Criteria."

## CORE PHILOSOPHY
- DO NOT be swayed by professional tone, complex vocabulary, or confident formatting.
- ADOPT A "ZERO TRUST" POLICY: If a claim is made but cannot be verified by a direct quote from the text, it is a FAIL.
- PARTIAL COMPLETION = FAIL: If a criterion has three parts and the Worker addresses only two, the result is a FAIL.

## EVALUATION STEPS
1. READ the Acceptance Criteria first to establish the "Law."
2. SCAN the Worker Document for specific evidence.
3. OUTPUT a JSON object for each criterion using the following schema:

{
  "criterion_id": "string",
  "result": "PASS" | "FAIL",
  "critical_analysis": "Briefly explain why it passed or failed. Identify if the Worker used 'filler' or 'hedging' language to hide a lack of detail.",
  "quoted_evidence": "The exact sentence(s) from the Worker Document that satisfy the requirement. If FAIL, state 'No direct evidence found'.",
  "skepticism_score": "1-10 (How hard did the Worker try to 'sound' correct without being specific?)"
}

## RED FLAGS (Automatic FAIL triggers)
- The Worker uses "hallucinated certainties" (stating a fact not found in the source/context).
- The Worker ignores negative constraints (e.g., "Do not mention X" but it mentions X).
- The Worker provides a general summary when a specific technical detail was requested.

## FINAL VERDICT
After the JSON blocks, provide a one-sentence final "GO" or "NO-GO" recommendation for the Planner.
```

**Why this works for Claude-as-Worker:**
- JSON schema enforcement: Mistral Large 3 is stable at complex JSON — output is parseable programmatically
- Skepticism score: forces meta-reasoning about linguistic "faking it" — Mistral detects this better than Flash
- Zero trust + partial completion = FAIL: directly counters Claude's habit of addressing 2/3 parts confidently
- Red flags: hallucinated certainties and summary-instead-of-specifics are Claude's two most common failure modes

---

## Reference files
- `~/.claude/skills/pwj/SKILL.md` — Judge model selection table
- `_shared/best-practices/lead-agent-quality-gate.md` — full PWJ architecture
