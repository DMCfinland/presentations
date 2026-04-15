# Grok Spar — Arctic Orchestrator Architecture Attack
**Source:** Claude fallback (browser automation blocked — Bash permission denied)  
**Mode:** Cross-Validate | Adversarial Architecture Review  
**Date:** 2026-04-15  
**Prompt file:** /tmp/grok-spar-arctic-orchestrator-20260415.txt

---

## PREFLIGHT NOTE
Browser automation (Grok Expert CDP) could not execute — Bash permission denied in this session. This response is a best-effort senior architect analysis written directly by Claude, acting adversarially per the task brief. **Before building the pipeline, manually paste `/tmp/grok-spar-arctic-orchestrator-20260415.txt` to Grok Expert for live tool-augmented analysis (Harper web_search + Benjamin code_execution).**

---

## ATTACK ANALYSIS

### 1. Architecture Flaws — Silent Failures

**Failure mode:** The deepest architectural flaw is that the pipeline has no shared truth state. Each wave reads files written by the previous wave, but there is no schema contract between waves. A subagent in Wave 2 reads Wave 1's flyer HTML and extracts pricing — but it does this via free-text reading, not a structured data contract. If the flyer says "from €279/day" and the PRD needs net rates, the Wave 2 subagent must infer the net rate from marketing copy. That inference will be wrong or inconsistent.

**Why dangerous autonomous:** Silent. No exception is thrown. The PRD gets built with a hallucinated net rate. Wave 3 and Wave 4 inherit it. The Knowledge Bible contains authoritative-sounding wrong numbers.

**Concrete fix:** Add a `PRICING-MASTER.json` written by the orchestrator before Wave 1 fires. All subagents read from this single source. Pricing consistency grep becomes a schema validation, not a text search.

---

### 2. Dependency Chain Risk — Error Propagation

**Failure mode:** The sequential dependency chain (W1→W2→W3→W4) means quality degrades multiplicatively. If Wave 1 has 85% quality (one doc slightly off), Wave 2 inherits that and adds its own 15% error rate — the compounded output quality reaching Wave 4 is roughly 0.85⁴ ≈ 52%. The Knowledge Bible, which is meant to be the authoritative master, may be only half-correct on facts that were introduced in Wave 1.

**Mathematical model (Benjamin framing):**
```
P(W1 good) = 0.85 (parallel, 2 agents, 1 may have a bad rate)
P(W2 good | W1 good) = 0.85 (reads W1, adds interpretation)
P(W3 good | W2 good) = 0.90 (simpler brief, less creative interpretation)
P(W4 good | W3 good) = 0.80 (compiles 4 sources — aggregation amplifies errors)
P(Bible fully correct) = 0.85 × 0.85 × 0.90 × 0.80 ≈ 0.52
```

That's a coin flip on the master document being correct when it's the only thing Gemini audits.

**Concrete fix:** Add a structured data extraction step after each wave where the orchestrator (not the subagent) reads the output and extracts 5-10 key facts into a `wave-N-facts.json`. These facts are diffed against PRICING-MASTER.json before the next wave launches. If any fact deviates >X%, hard stop + alert.

---

### 3. bypassPermissions Risk

**Failure mode:** `bypassPermissions` means a subagent can write to any path, delete files, overwrite git history, or make network calls without prompting. The specific risk here: a subagent building the Knowledge Bible may decide to "clean up" by deleting intermediate wave files it considers redundant. If the Gemini audit runs after git commit and finds an error, you've committed and potentially lost the intermediate wave outputs needed to debug.

**Secondary risk:** If a subagent hangs or enters a loop, it runs unconstrained. Without permission gates, the only circuit breaker is the turn budget — and if the subagent is burning turns on retries rather than productive work, the turn budget is consumed without output.

**Missing guardrails:**
- No write-path whitelist (subagents should only write to their designated output dir)
- No network call restriction (subagent could attempt external API calls)
- No file-deletion restriction (intermediate outputs are not protected)

**Concrete fix:** Instead of blanket `bypassPermissions`, define an allowed-paths allowlist per subagent in the prompt: "You may ONLY write to `output/wave-1/`. Any write outside this path is a critical error — stop and report." This is a prompt constraint, not a permission constraint, but it reduces the blast radius significantly.

---

### 4. Subagent Context Isolation — What They'll Miss

**Failure mode:** Each subagent starts with zero conversation history. What they won't have unless explicitly injected:
- The product's real pricing structure (€279/day commercial, €300 net/€400 list — the FAM pricing rule from MEMORY.md)
- The brand constraint: sub-brand is "Saimaa Lake Cruise by Arctic Cruises" — not just "Arctic Cruises"
- Route specifics: Night 1 Lappeenranta, Night 2 Sahanlahti, Night 3 Järvisydän
- The "200-pax ship = go big" rule (40-80 operators minimum)
- STF+Green Key journey by end 2027 — relevant to any sustainability section
- The wildlife USP constraint: "possible natural observation" NOT "see a seal"

If these are not in the subagent prompt, the agent will fill gaps with plausible-sounding defaults. The flyer will say "see Saimaa seals" and the PRD will show the wrong net rate.

**Concrete fix:** Write a `PRODUCT-BRIEF.md` (≤500 words, structured) that is injected verbatim into every subagent prompt. This is the single source of truth for product facts. The orchestrator writes this once from MEMORY.md + warm pack, then every subagent gets it prepended.

---

### 5. Wave 1 Parallel Race Conditions

**Failure mode:** Two subagents writing to `output/wave-1/` simultaneously. The actual risk depends on whether they write to distinct filenames. If both are instructed to write `wave-1-output.md` as a combined manifest, you get a write collision. More likely: they write distinct files (flyer.html, fam-invite.html) but both try to create or update a shared `wave-1/MANIFEST.json` simultaneously — last write wins, and one agent's manifest entry gets overwritten.

**Secondary risk:** If both agents read a shared template file at the same time and one modifies it in place (unlikely but possible with bypassPermissions), you get a torn read.

**Concrete fix:** Assign each Wave 1 subagent a distinct output subdirectory (`output/wave-1a/` and `output/wave-1b/`). Each writes its own MANIFEST.json. The orchestrator aggregates them after both complete. No shared write targets in parallel waves.

---

### 6. The MANIFEST.json Pattern — Reliability

**Failure mode:** MANIFEST.json as a gate check has two critical weaknesses:

1. **The subagent writes "complete" then crashes mid-write.** JSON is only valid when fully closed. A partial write (`{"status": "compl`) is not parseable. Your orchestrator will throw a JSON parse error or — worse — silently skip the gate check if error handling is permissive.

2. **"Complete" is self-reported.** The subagent decides it's done and writes complete. But "done" to the subagent means "I finished my turns" — not "the output is correct." A subagent that ran out of turn budget and wrote a half-finished document will still write `{"status": "complete"}` because it reached the end of its instruction set.

**Concrete fix:** Gate check must be structural, not self-reported. The orchestrator should:
1. Verify MANIFEST.json is valid parseable JSON
2. Verify the output file exists AND has size > minimum threshold (e.g., flyer.html > 5KB)
3. Verify that 3-5 required strings are present in the output (e.g., pricing figure, brand name, contact CTA)
4. Only then mark the wave as passed

Self-reported completion is always theater.

---

### 7. 20-Minute Time Budget Realism

**Failure mode:** 20 minutes for a full A4 HTML document from scratch is achievable for a simple template-fill but risky for a "commercial-grade" document that requires:
- Design decisions (layout, CSS, image placement)
- Content generation (headline, body copy, CTA, pricing)
- File writes and verification
- MANIFEST.json write

The real bottleneck is not generation speed — it's turn budget exhaustion from iterative refinement. If the subagent generates the HTML, reads it back, decides it needs improvement, and refines — that's 3-4 turns consumed on one document. With a 5-8 turn budget, you have 1-4 turns left for everything else (manifest, verification, error handling).

**Risk in autonomous mode:** A subagent that burns turns on quality refinement has fewer turns for error recovery. If the HTML write fails at turn 6, there are no turns left to retry.

**Concrete fix:** Give HTML subagents a strict instruction: "Generate once, write once, do not re-read or refine the output in this session. Quality iteration happens at orchestrator level, not within the subagent." This preserves turn budget for error recovery.

---

### 8. Judge Quality — Gemini on Bible Only

**Failure mode:** Gemini auditing only the Knowledge Bible misses the documents that operators actually receive. The B2B Flyer and FAM Invitation are the first-impression commercial materials — if those have wrong pricing, a broken CTA, or off-brand copy, Gemini won't catch it because it never sees them.

**Secondary flaw:** The Knowledge Bible is a compilation of Waves 1-3. If Gemini approves the Bible, it's approving a document that summarizes those waves — but the Bible may smooth over inconsistencies that exist in the source documents. The Bible says "net rate €300" but the FAM invitation says "€279/day all-inclusive" — the Bible is internally consistent, Gemini passes it, but the two documents contradict each other in the field.

**Concrete fix:** Run Gemini on a structured cross-document consistency check, not just the Bible. Extract key claims from each document (pricing, dates, contacts, brand name) into a comparison table and ask Gemini to flag contradictions across documents. This is faster and catches more than a single-document audit.

---

### 9. Wave 4 Complete Failure — Recovery Mode

**Failure mode:** Wave 4 fails completely (subagent crashes, turn budget exhausted, file write error). Current design: the git commit never fires, and the pipeline has no output artifact. All previous waves produced good documents but they are uncommitted and potentially at risk if the session dies.

**Why this is the worst failure mode:** The user invested the full pipeline cost (all 4 waves, Gemini audit call) and gets nothing committed. The intermediate files exist on disk but are not tracked. If the Claude Code session crashes after Wave 4 failure, the files may or may not survive.

**Concrete fix:** Progressive commit strategy:
- After Wave 1 passes gate check: `git commit -m "Wave 1 complete: flyer + FAM invite"`
- After Wave 2 passes gate check: `git commit -m "Wave 2 complete: Tour Operator PRD"`
- After Wave 3 passes gate check: `git commit -m "Wave 3 complete: Operations Brief"`
- Wave 4 failure → partial pipeline still committed, clearly labeled
- Add a `pipeline-status.json` at root tracking which waves are committed

This also enables resumption: if Wave 4 fails, restart from Wave 4 only.

---

### 10. Three Concrete Architectural Improvements

**Improvement 1: Centralized Data Contract (PRICING-MASTER.json + PRODUCT-BRIEF.md)**
Before any subagent fires, the orchestrator writes two files from source-of-truth inputs:
- `PRICING-MASTER.json`: all pricing tiers, net rates, list rates, FAM rates — structured, versioned
- `PRODUCT-BRIEF.md`: 500-word product facts (brand, route, dates, USPs, contacts)

All subagents receive PRODUCT-BRIEF.md prepended to their prompt. All subagents are prohibited from inventing pricing — they read from PRICING-MASTER.json only. This eliminates the #1 silent failure mode (pricing hallucination) entirely.

**Improvement 2: Structural Gate Checks (Replace Self-Reported MANIFEST)**
Replace `MANIFEST.json complete` with orchestrator-side structural validation:
```python
def wave_gate_check(output_path, required_strings, min_size_kb):
    assert os.path.getsize(output_path) > min_size_kb * 1024
    content = open(output_path).read()
    for s in required_strings:
        assert s in content, f"Required string missing: {s}"
    return True
```
Required strings per document are defined in the pipeline config before launch. Gate failure = hard stop + alert, not silent pass.

**Improvement 3: Progressive Commits + Wave-Isolated Output Dirs**
- Each wave writes to `output/wave-N/` (no shared write targets)
- Orchestrator commits after each wave passes gate check
- Wave 4 failure leaves Waves 1-3 committed and recoverable
- Add `pipeline-status.json` so a resumed run knows where to restart

These three changes together address: silent pricing failures (#1, #2), self-reported completion theater (#6), write collisions (#5), and unrecoverable total failure (#9).

---

## RISK CONSOLIDATION TABLE

| Risk | Severity (1-5) | Fix |
|------|---------------|-----|
| Pricing hallucination (no shared data contract) | 5 | PRICING-MASTER.json injected into all subagents |
| Error propagation through sequential chain (P≈0.52 for Bible) | 5 | Wave-facts extraction + diff gate between waves |
| Self-reported MANIFEST completion (theater) | 4 | Structural validation: file size + required strings |
| Subagent context isolation (missing product facts) | 4 | PRODUCT-BRIEF.md prepended to every subagent prompt |
| bypassPermissions unconstrained write paths | 4 | Allowed-paths prompt constraint per subagent |
| Wave 4 total failure = zero committed output | 4 | Progressive commits after each wave gate |
| Wave 1 parallel write collision (shared MANIFEST) | 3 | Wave-isolated output dirs (wave-1a/, wave-1b/) |
| Turn budget exhaustion on refinement loops | 3 | "Generate once, write once" instruction in HTML subagents |
| Gemini audits Bible only (misses cross-doc contradictions) | 3 | Cross-document claim extraction → Gemini consistency check |
| 20-min wall time for commercial-grade HTML | 2 | Scoped expectation: 1 generation pass, no in-agent refinement |

---

## SUMMARY VERDICT

The architecture is sound in its wave sequencing but has two critical gaps that will cause silent failures in production:

1. **No shared data contract.** Each subagent invents its own version of pricing from context. This is the #1 failure mode. Fix it before anything else.

2. **Self-reported completion is theater.** MANIFEST.json written by the subagent itself is not a gate check. It's the subagent telling you it's done, which is always true (it reached the end of its turns). Replace with structural validation in the orchestrator.

The progressive commit improvement is the cheapest fix with the highest recovery value — add it regardless of the other changes.

---

*Fallback analysis — manually paste `/tmp/grok-spar-arctic-orchestrator-20260415.txt` to Grok Expert for live web_search + code_execution augmented validation (Harper + Benjamin agent layers).*
