---
name: Pre-Spar Doc Compression via Parallel Subagents
description: When sparring large docs with Grok (3KB prompt limit), compress each doc to 150-word extract via parallel subagents first. Produces sharper spar with specific Lucas objections.
type: feedback
tier: B
source: S238
confirmed: 1
---

## Rule

Before building a Grok spar prompt for large documents (>10KB each), launch parallel subagents to compress each doc into focused extracts. Do NOT try to fit raw documents into the prompt.

**Why:** Grok Expert browser has a 3KB prompt limit via clipboard (or ~5KB via --prompt-file). Raw HTML/MD docs are 10-80KB each. Cramming summaries defeats the purpose — you want Grok to attack specific claims, not generic summaries. Subagent compression extracts exactly the right 150 words from each doc.

**How to apply:**
1. 3 parallel subagents, one per doc (or one per doc category)
2. Each subagent extracts: top 5 claims, all pricing, key differentiators, target audience, weakest claim
3. Combine extracted outputs → build Grok prompt (<5KB total)
4. Subagent overhead: ~18-26s, ~35-45K tokens per agent
5. Result: prompt is surgical, not summarized — Lucas gets real claims to attack

**Evidence — S238:** 3 subagents compressed arctic-cruises-b2b-flyer.html (26KB), arctic-cruises-operator-prd.html (49KB), arctic-cruises-knowledge-bible.md (79KB) → ~450 words each. Built 4.7KB Grok prompt. Lucas surfaced 3 hard operator objections with specific language ("We cannot put unnamed resorts in our brochure — full stop"). Quality of adversarial output noticeably higher than when feeding raw docs.

**Template subagent prompt:**
```
Read [FILE]. Extract ONLY (max 150 words):
1. TOP 5 CLAIMS (specific, verifiable)
2. ALL PRICING (exact figures)
3. KEY DIFFERENTIATORS (3 bullets)
4. TARGET AUDIENCE PROFILE
5. ONE WEAKEST CLAIM (most challengeable)
No commentary. No intro. Just extracted data.
```
