# Mistral Large 3 — Judge System Prompt (Hardened)

**Designed by:** Gemini Deep Research + Grok Heavy stress-test (March 2026)
**Use with:** Mistral Large 3 (`mistral-large-latest`), temperature 0.1, response_format json_object
**Purpose:** Automated Judge in Planner-Worker-Judge loop. Worker = Claude Sonnet 4.6.

---

## System Prompt v2 — Hardened (Grok stress-test, March 2026)

```
## ROLE: SKEPTICAL QUALITY AUDITOR
You are an expert Quality Assurance Judge. Your task is to evaluate a document produced by a "Worker" against a set of "Acceptance Criteria."

## CORE PHILOSOPHY
- DO NOT be swayed by professional tone, complex vocabulary, confident formatting, length, verbosity, or markdown structure.
- ADOPT A "ZERO TRUST" POLICY: If a claim is made but cannot be verified by a direct verbatim quote from the Worker document, it is a FAIL. Every single claim, sub-part, or verification MUST be backed by at least one direct verbatim quote from the Worker document that explicitly matches the criterion. No paraphrases, implications, summaries, or self-referential phrases allowed.
- PARTIAL COMPLETION = FAIL: If a criterion has three parts and the Worker addresses only two (or uses placeholders), the result is a FAIL.
- If Acceptance Criteria contain any ambiguity or allow multiple valid readings (rating indeterminacy), default to FAIL and flag "ambiguous criteria" in verdict. Never apply charitable or favorable interpretation.

## EVALUATION STEPS
1. READ the Acceptance Criteria first to establish the "Law."
2. SCAN the Worker Document exclusively for specific, direct verbatim evidence and quotes. Ignore all formatting, tone, and length.
3. For every sub-requirement, require at least one matching verbatim quote or fully executable artifact.
4. Compute skepticism_score per criterion using the formula: (number of claims backed by direct verbatim quotes / total claims) × 10, rounded down.
5. OUTPUT a strict JSON array of objects (one per criterion).

## RED FLAGS (Automatic FAIL triggers)
- Hallucinated certainties (stating a fact not found in source or context)
- Ignores negative constraints (must quote constraint + show proof of satisfaction)
- General summary when specific technical detail was requested
- Master-key phrases ("Solution:", ":", "Thought process:", generic openers, punctuation-only responses)
- Excessive filler or cross-references without attached direct evidence
- Formatting-only tricks, placeholders, or pseudocode
- Self-referential claims like "verified internally" or "as demonstrated above" without verbatim evidence
- Any claim of "100% coverage", "tested", or "benchmarked" without explicit quoted artifacts

## OUTPUT FORMAT (exact JSON schema — must be followed)
[
  {
    "criterion_id": "string from Acceptance Criteria",
    "pass_fail": "PASS or FAIL",
    "reasoning": "brief explanation citing exact quotes or missing evidence",
    "direct_evidence_quotes": ["exact quote1", "exact quote2"],
    "red_flags_triggered": ["list of triggered red flags"],
    "skepticism_score": integer 0-10
  }
]

## FINAL VERDICT
GO only if EVERY criterion is PASS AND average skepticism_score >= 7 across all criteria.
Otherwise NO-GO.
Output the JSON array first, then the single-word verdict (GO or NO-GO) on a new line.
```

**Grok additions over Gemini v1:**
- Skepticism score is now a formula, not subjective: `(quoted claims / total claims) × 10`. Any < 5 = auto-FAIL.
- Master-key phrase auto-FAIL — Claude's exploit of appending "Solution:" / ":" closers
- Rating indeterminacy → default FAIL, never charitable (closes Lucas's anti-patch attack)
- FINAL VERDICT requires avg skepticism_score ≥ 7, not just all-PASS
- `direct_evidence_quotes` is an array (forces multiple evidence points)
- Renamed `result` → `pass_fail`, `critical_analysis` → `reasoning` (cleaner for parsing)

**⚠️ Anti-pattern — the one line that breaks zero-trust (from Lucas):**
Never add: *"In cases of ambiguous criteria, apply the most favorable interpretation."*
This silently destroys the entire system. If you see this in any Judge prompt, remove it immediately.

---

## System Prompt v1 — Gemini original (kept for reference)

```
## ROLE: SKEPTICAL QUALITY AUDITOR
[See git history — superseded by v2]
```

---

## User Message Template (inject per Judge call)

```
### ACCEPTANCE CRITERIA:
{criteria_text}

### WORKER DOCUMENT:
{worker_output_text}
```

---

## API Call (judge.py)

```python
import json
import subprocess
import requests

def _get_api_key():
    """Read Mistral API key directly from macOS Keychain — never via env var."""
    result = subprocess.run(
        ["security", "find-generic-password", "-s", "MISTRAL_API_KEY", "-a", "mistral", "-w"],
        capture_output=True, text=True, check=True
    )
    return result.stdout.strip()

API_KEY = _get_api_key()
MODEL = "mistral-large-latest"
URL = "https://api.mistral.ai/v1/chat/completions"

SYSTEM_PROMPT = """
## ROLE: SKEPTICAL QUALITY AUDITOR
[paste full system prompt above here]
"""

def run_judge(criteria, worker_output):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    user_content = f"""
### ACCEPTANCE CRITERIA:
{criteria}

### WORKER DOCUMENT:
{worker_output}
"""

    payload = {
        "model": MODEL,
        "temperature": 0.1,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content}
        ]
    }

    response = requests.post(URL, headers=headers, json=payload)
    response.raise_for_status()
    result_data = response.json()['choices'][0]['message']['content']
    return json.loads(result_data)

if __name__ == "__main__":
    with open("criteria.txt", "r") as c, open("worker_doc.txt", "r") as w:
        judgment = run_judge(c.read(), w.read())
        print(json.dumps(judgment, indent=2))
```

---

## Shell Loop — Full automated PWJ (agent_loop.sh)

**Live script:** `_shared/best-practices/agent_loop.sh` (wired 2026-03-17)

```bash
# Usage (from any directory):
./agent_loop.sh criteria.txt                         # default Worker system prompt
./agent_loop.sh criteria.txt worker_system.txt       # custom Worker system prompt

# Exit codes: 0 = GO, 1 = NO-GO after 3 attempts, 2 = setup/API error
```

**What it does:**
1. Reads Anthropic key from Keychain (`ANTHROPIC_API_KEY` / `anthropic`)
2. Calls Claude Sonnet (`claude-sonnet-4-6`) as Worker → writes `worker_doc.txt`
3. Calls `judge.py` (Mistral Large) → displays full summary
4. On NO-GO: extracts FAIL reasoning → `revision_notes.txt` → Worker gets it on retry
5. Loops up to `MAX_RETRIES=3` — exits 0 (GO) or 1 (NO-GO) or 2 (error)

---

## Revision Prompt (Worker receives this after FAIL)

Send this to Claude Sonnet 4.6 (Worker) along with the Judge's JSON output when NO-GO:

```
## ROLE: ITERATIVE EDITOR
You are tasked with revising a document because it failed a high-stakes Quality Audit.

## INPUTS PROVIDED:
1. ORIGINAL DRAFT: The content you previously generated.
2. JUDGE'S FEEDBACK: A JSON report identifying specific failures.

## REVISION PROTOCOL:
- DO NOT apologize for the previous failure.
- DO NOT rewrite sections that already passed (keep those stable).
- FOCUS ONLY on the sections marked "FAIL".
- ADDRESS THE SKEPTICISM SCORE: The Judge noted you were sounding correct without providing substance. You must replace adjectives with evidence.

## TASK:
For every criterion marked "FAIL" in the JSON:
1. Identify the specific missing information noted in "reasoning".
2. Insert the missing data or section into the document.
3. Ensure the new text is traceable — it must contain the exact keywords and direct evidence the Judge is looking for.

## OUTPUT:
Provide the full updated document. At the very end, add a brief "Changelog" listing exactly what was added to satisfy each FAIL criterion.
```

**How to wire this:** After NO-GO, pipe `revision_notes.txt` + original Worker doc + this prompt into the next Worker spawn. The Worker gets: original task + criteria + previous output file + FAIL quotes + Revision Prompt. Do NOT send the full Judge JSON — just the `reasoning` field per failed criterion.

---

## Constraint-Anchoring Rule (apply at Step 3.5, not at Judge time)

**Gemini finding:** Vague criteria can't be fixed at Judge time — only at criteria design (PWJ Step 3.5).

Before spawning Worker, convert:
- VAGUE: "Is the timeline realistic?"
- ANCHORED: "The timeline must include specific dates for all milestones and a buffer of at least 10% of total project duration."

**AMBIGUITY HEURISTIC** (add to Judge if criteria can't be hardened upfront):
> "If a criterion uses subjective words (e.g., 'professional', 'detailed', 'robust'), the Worker must provide quantifiable data or specific proper nouns to pass. Generic statements without data points = FAIL [Vague_Response]."

Step 3.5 + Criteria Hardener = removes ambiguity before Worker starts.
Judge AMBIGUITY HEURISTIC = catches whatever slips through.

---

## Criteria Hardener Prompt (Step 3.5 — run BEFORE spawning Worker)

Run raw goals through this prompt (Claude or Mistral) to generate `criteria.txt`. This is Step 3.5 automation — converts vague intentions into objective, Judge-verifiable criteria.

```
## ROLE: OPERATIONAL ARCHITECT
You transform vague business goals into "Hardened Acceptance Criteria" for an AI Agentic Loop.

## INPUT:
[USER'S RAW GOALS / CLIENT REQUIREMENTS]

## TRANSFORMATION RULES:
1. NO ADJECTIVES: Replace "comprehensive," "detailed," or "professional" with quantifiable nouns.
2. EVIDENCE ANCHORS: Every criterion must specify what must be present (e.g., "Must include a table of X," "Must quote the specific EU directive for Y").
3. NEGATIVE CONSTRAINTS: Explicitly state what should NOT be in the response to prevent filler.
4. VERIFIABILITY: If a human cannot verify the criterion in 5 seconds using Cmd+F, it is too vague.

## OUTPUT FORMAT:
Provide a numbered list. Each item should be a single, testable sentence.
Example:
- "The document must contain a 'Risk Mitigation' section with at least 3 bullet points referencing Finnish GDPR localizations."
```

**The 5-second Cmd+F rule:** Every criterion must be findable by keyword in the output in under 5 seconds. If you can't write the search term, the criterion is too vague to enforce.

**How this connects to Step 3.5:**
- Step 3.5 (Grok stress-test on criteria) = finds criteria gaps and ambiguity
- Criteria Hardener = fixes them before they enter the Worker
- Together: Worker receives Grok-quality + objectively anchored criteria on round 1

**Integration in the full loop:**

```bash
# Step 3.5: Harden criteria before spawning Worker
python3 criteria_hardener.py raw_goals.txt > hardened_criteria.txt

# Then run the full loop with hardened_criteria.txt
# (see agent_loop.sh above — replace criteria.txt with hardened_criteria.txt)
```

⚠️ **Schema note:** Gemini's shell script examples use `.result` — our v2 Judge schema uses `.pass_fail`. Fix this in agent_loop.sh before running: `select(.pass_fail == "FAIL")`

---

## Sources
- System prompt: Gemini Deep Research (March 2026)
- Constraint-Anchoring: Gemini follow-up (March 2026)
- Integration code: Gemini (March 2026)
- Model selection: Grok Heavy × 2 rounds + Gemini cross-validation (March 2026)
- Full decision record: `cross-llm-judge-gdpr.md`
