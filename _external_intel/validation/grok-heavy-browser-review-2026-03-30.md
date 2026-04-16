# Grok Heavy — Browser Automation Code Review
**Date:** 2026-03-30
**Source:** Grok Heavy 4-agent (self-analysis of own UI)
**Skill reviewed:** grok-heavy-browser/main.py v1.0

---

## Key Findings

### Dead selectors (v1.0 was using these — all broken):
- `div[data-message-id]` → REMOVED from production DOM months ago
- `textarea` (generic) → works today but fragile

### Correct selectors (from Grok's own DOM knowledge):
- Input: `textarea[data-testid="chat-input"]`
- Send: `button[data-testid="send-button"]`
- Model picker: `button[data-testid="model-selector"]`
- Stop button: `button[aria-label="Stop generating"]` or `button[data-testid="stop-button"]`
- Response container: `div[data-testid="grok-response"][role="listitem"]`

### Heavy mode NOT auto-activated:
Must click `button[data-testid="model-selector"]` → select "Grok 4 Heavy"
No URL param, no keyboard shortcut.

### Timing:
- Heavy 4-agent: 5–20 min (median ~12 min complex tasks)
- 3-min timeout = always fails on real Heavy prompts
- Correct: 5 min for first token + stability polling loop

### Streaming completion detection:
- Reliable: poll stability of last response + stop button disappearance
- Useless: networkidle (SSE stays open), fixed sleep

### Architecture:
Sync blocking = unacceptable for 10-15 min runs.
Recommended: async Playwright + write result to JSON file.

---

## Stability polling function (from Grok):
```python
def wait_for_heavy_completion(page, stability_seconds=4):
    stop_btn = page.locator('button[aria-label="Stop generating"]')
    last_text = ""
    while True:
        if stop_btn.count() == 0:
            time.sleep(stability_seconds)
            current_text = page.locator('div[data-testid="grok-response"]').last.inner_text().strip()
            if current_text == last_text:
                return
            last_text = current_text
        time.sleep(1)
```
