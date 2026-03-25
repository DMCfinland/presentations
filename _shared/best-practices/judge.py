#!/usr/bin/env python3
"""
Mistral Large 3 — Automated Judge for PWJ Loop
Source: _shared/best-practices/mistral-judge-system-prompt.md (v2 Hardened)
Usage: python3 judge.py criteria.txt worker_doc.txt
Key: Stored in macOS Keychain as service=MISTRAL_API_KEY, account=mistral
Exit: 0 = GO, 1 = NO-GO, 2 = Judge error (parse fail / network / auth)
"""

import json
import subprocess
import sys
import requests

MODEL = "mistral-large-latest"
URL = "https://api.mistral.ai/v1/chat/completions"
REQUEST_TIMEOUT = 60  # seconds

SYSTEM_PROMPT = """
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
"""


def _get_api_key():
    """Read Mistral API key directly from macOS Keychain — never via env var."""
    result = subprocess.run(
        ["security", "find-generic-password", "-s", "MISTRAL_API_KEY", "-a", "mistral", "-w"],
        capture_output=True, text=True, check=True, timeout=10
    )
    key = result.stdout.strip()
    # Clear subprocess result from memory
    del result
    return key


def _strip_markdown_fences(text: str) -> str:
    """Remove ```json ... ``` wrappers Mistral sometimes adds despite json_object mode."""
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        # Drop first line (```json or ```) and last line (```)
        inner = lines[1:] if lines[-1].strip() == "```" else lines[1:]
        if inner and inner[-1].strip() == "```":
            inner = inner[:-1]
        text = "\n".join(inner).strip()
    return text


def run_judge(criteria: str, worker_output: str) -> dict:
    api_key = _get_api_key()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    user_content = f"""### ACCEPTANCE CRITERIA:
{criteria}

### WORKER DOCUMENT:
{worker_output}
"""

    payload = {
        "model": MODEL,
        "temperature": 0.0,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content}
        ]
    }

    try:
        response = requests.post(URL, headers=headers, json=payload, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    finally:
        # Clear key from local scope regardless of HTTP outcome
        del api_key
        del headers

    raw = response.json()['choices'][0]['message']['content']

    # Strip trailing GO/NO-GO line if present before JSON parsing
    lines = raw.strip().split('\n')
    verdict_line = ""
    if lines[-1].strip() in ("GO", "NO-GO"):
        verdict_line = lines[-1].strip()
        raw = '\n'.join(lines[:-1])

    # Handle markdown fences Mistral may add despite json_object mode
    raw = _strip_markdown_fences(raw)

    # Wrap json_object response (single dict) in a list if needed
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Judge returned unparseable output. Raw (first 500 chars):\n{raw[:500]}"
        ) from e

    # Mistral json_object mode returns a dict; unwrap if needed
    if isinstance(parsed, dict):
        result = parsed.get("criteria", parsed.get("results", [parsed]))
    else:
        result = parsed

    # Derive verdict from data if not in response
    if not verdict_line:
        all_pass = all(c.get("pass_fail") == "PASS" for c in result)
        scores = [c.get("skepticism_score", 0) for c in result]
        avg_score = sum(scores) / len(scores) if scores else 0
        verdict_line = "GO" if all_pass and avg_score >= 7 else "NO-GO"

    return {"criteria_results": result, "verdict": verdict_line}


def print_summary(judgment: dict):
    results = judgment["criteria_results"]
    verdict = judgment["verdict"]

    failures = [c for c in results if c.get("pass_fail") == "FAIL"]
    scores = [c.get("skepticism_score", 0) for c in results]
    avg_score = round(sum(scores) / len(scores), 1) if scores else 0

    print(f"\n{'='*60}")
    print(f"VERDICT: {verdict}  |  Failures: {len(failures)}/{len(results)}  |  Avg skepticism: {avg_score}/10")
    print('='*60)

    for c in results:
        status = c.get("pass_fail", "?")
        cid = c.get("criterion_id", "?")
        score = c.get("skepticism_score", "?")
        print(f"  [{status}] {cid}  (score: {score}/10)")
        if status == "FAIL":
            print(f"    → {c.get('reasoning', '')}")
            flags = c.get("red_flags_triggered", [])
            if flags:
                print(f"    → Red flags: {', '.join(flags)}")

    print()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 judge.py criteria.txt worker_doc.txt")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as c_file, open(sys.argv[2], "r") as w_file:
            judgment = run_judge(c_file.read(), w_file.read())
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Keychain read failed — {e}", file=sys.stderr)
        sys.exit(2)
    except requests.exceptions.Timeout:
        print(f"ERROR: Mistral API timeout ({REQUEST_TIMEOUT}s)", file=sys.stderr)
        sys.exit(2)
    except requests.exceptions.HTTPError as e:
        print(f"ERROR: Mistral API HTTP error — {e.response.status_code} {e.response.text[:200]}", file=sys.stderr)
        sys.exit(2)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)

    print(json.dumps(judgment, indent=2))
    print_summary(judgment)

    # Exit code: 0 = GO, 1 = NO-GO, 2 = Judge error (caught above)
    sys.exit(0 if judgment["verdict"] == "GO" else 1)
