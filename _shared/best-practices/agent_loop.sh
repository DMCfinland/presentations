#!/bin/bash
# Full automated PWJ loop: Worker (Claude Sonnet) → Judge (Mistral) → retry
# Usage: ./agent_loop.sh criteria.txt [worker_system_prompt.txt]
# Requires: judge.py in same dir, jq, macOS Keychain entries for both API keys
# Exit: 0 = GO, 1 = NO-GO after max retries, 2 = setup/API error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JUDGE_SCRIPT="$SCRIPT_DIR/judge.py"
MAX_RETRIES=3
RETRY_COUNT=0
PASSED=false

CRITERIA_FILE="${1:-criteria.txt}"
WORKER_SYSTEM_FILE="${2:-}"

# --- Validation ---
if [ ! -f "$CRITERIA_FILE" ]; then
    echo "ERROR: criteria file not found: $CRITERIA_FILE" >&2
    exit 2
fi

if [ ! -f "$JUDGE_SCRIPT" ]; then
    echo "ERROR: judge.py not found at $JUDGE_SCRIPT" >&2
    exit 2
fi

if ! command -v jq &>/dev/null; then
    echo "ERROR: jq not installed — run: brew install jq" >&2
    exit 2
fi

# --- Read Anthropic key from Keychain ---
ANTHROPIC_KEY=$(security find-generic-password -s "ANTHROPIC_API_KEY" -a "anthropic" -w 2>/dev/null)
if [ -z "$ANTHROPIC_KEY" ]; then
    echo "ERROR: ANTHROPIC_API_KEY not found in Keychain" >&2
    exit 2
fi

# --- Worker system prompt ---
WORKER_SYSTEM="You are a skilled technical writer and analyst. Produce a document that satisfies ALL of the acceptance criteria provided. Be specific, cite evidence, and be complete. Write markdown directly — no scripts, no code unless the criteria explicitly require it."
if [ -n "$WORKER_SYSTEM_FILE" ] && [ -f "$WORKER_SYSTEM_FILE" ]; then
    WORKER_SYSTEM=$(cat "$WORKER_SYSTEM_FILE")
fi

# --- Main loop ---
while [ $RETRY_COUNT -lt $MAX_RETRIES ] && [ "$PASSED" = false ]; do
    echo ""
    echo "=== PWJ Attempt $((RETRY_COUNT + 1)) of $MAX_RETRIES ==="

    # Build user message — include revision notes on retries
    CRITERIA=$(cat "$CRITERIA_FILE")
    if [ -f "revision_notes.txt" ] && [ $RETRY_COUNT -gt 0 ]; then
        REVISION=$(cat revision_notes.txt)
        USER_MSG="ACCEPTANCE CRITERIA:
$CRITERIA

REVISION NOTES (your previous attempt failed — fix these specific issues):
$REVISION"
    else
        USER_MSG="ACCEPTANCE CRITERIA:
$CRITERIA"
    fi

    # --- Call Claude Sonnet as Worker ---
    echo "[Worker] Calling Claude Sonnet..."
    WORKER_JSON=$(jq -n \
        --arg sys "$WORKER_SYSTEM" \
        --arg msg "$USER_MSG" \
        '{
            model: "claude-sonnet-4-6",
            max_tokens: 8096,
            system: $sys,
            messages: [{role: "user", content: $msg}]
        }')

    WORKER_RESPONSE=$(curl -sf https://api.anthropic.com/v1/messages \
        -H "x-api-key: $ANTHROPIC_KEY" \
        -H "anthropic-version: 2023-06-01" \
        -H "content-type: application/json" \
        -d "$WORKER_JSON")

    CURL_EXIT=$?
    if [ $CURL_EXIT -ne 0 ]; then
        echo "ERROR: Claude API call failed (curl exit $CURL_EXIT)" >&2
        unset ANTHROPIC_KEY
        exit 2
    fi

    API_ERROR=$(echo "$WORKER_RESPONSE" | jq -r '.error.message // empty' 2>/dev/null)
    if [ -n "$API_ERROR" ]; then
        echo "ERROR: Claude API error — $API_ERROR" >&2
        unset ANTHROPIC_KEY
        exit 2
    fi

    echo "$WORKER_RESPONSE" | jq -r '.content[0].text' > worker_doc.txt
    echo "[Worker] Done — $(wc -l < worker_doc.txt | tr -d ' ') lines → worker_doc.txt"

    # --- Run Mistral Judge ---
    echo "[Judge] Calling Mistral Large..."
    python3 "$JUDGE_SCRIPT" "$CRITERIA_FILE" worker_doc.txt > /tmp/pwj_judge_output.txt 2>&1
    JUDGE_EXIT=$?
    cat /tmp/pwj_judge_output.txt

    if [ $JUDGE_EXIT -eq 0 ]; then
        PASSED=true

    elif [ $JUDGE_EXIT -eq 1 ]; then
        RETRY_COUNT=$((RETRY_COUNT + 1))
        if [ $RETRY_COUNT -lt $MAX_RETRIES ]; then
            # Extract FAIL reasoning to revision_notes.txt
            python3 -c '
import json
content = open("/tmp/pwj_judge_output.txt").read()
sep_idx = content.find("\n" + "="*60)
json_str = content[:sep_idx].strip() if sep_idx >= 0 else content.strip()
try:
    data = json.loads(json_str)
    results = data.get("criteria_results", data if isinstance(data, list) else [data])
    fails = [c for c in results if c.get("pass_fail") == "FAIL"]
    notes = []
    for f in fails:
        notes.append("CRITERION: " + str(f.get("criterion_id", "?")))
        notes.append("REASON: " + str(f.get("reasoning", "")))
        flags = f.get("red_flags_triggered", [])
        if flags:
            notes.append("RED FLAGS: " + ", ".join(flags))
        notes.append("")
    print("\n".join(notes))
except Exception as e:
    print("Could not parse judge output: " + str(e))
' > revision_notes.txt
            echo "[Loop] Revision notes → revision_notes.txt — retrying..."
        fi

    else
        echo "ERROR: Judge returned error (exit $JUDGE_EXIT) — check output above" >&2
        unset ANTHROPIC_KEY
        exit 2
    fi
done

unset ANTHROPIC_KEY

echo ""
if [ "$PASSED" = true ]; then
    echo "=== PWJ COMPLETE: GO — final output in worker_doc.txt ==="
    exit 0
else
    echo "=== PWJ COMPLETE: NO-GO after $MAX_RETRIES attempts — see revision_notes.txt ==="
    exit 1
fi
