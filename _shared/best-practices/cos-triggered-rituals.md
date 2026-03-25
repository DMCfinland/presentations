---
name: AI Rituals as Triggered Skills — Not Auto-Fire
description: Maintenance rituals in AI systems should be triggered by user request, not automatic at every session start. Auto-fire creates friction; triggered skills preserve value.
type: feedback
---

When designing AI assistant behaviors that involve "check-in" or "maintenance" routines, make them triggered skills — not automatic session openers.

**Anti-pattern:** Every session starts with "It's Monday, let me ask you 3 questions about last week." → User feels interrogated → stops opening the bot.

**Pattern:** Routine fires ONLY when user triggers it ("maanantai", "viikkobrief", "päivitä konteksti"). Normal session start: pick up where left off, no ceremony.

**Why:** Time-poor executives (Finnish culture especially) are anti-bureaucracy. Rituals that fight daily workflow instead of embedding in it die within 2 weeks (Gemini + Grok both confirmed). The ritual's VALUE doesn't change — just the trigger moves from automatic to on-demand.

**How to apply:**
- Any CoS bot / thinking partner system prompt
- Design the ritual in full, then add: "triggers ONLY when user writes [keyword]"
- Keywords should be natural language, not commands ("maanantai" not "/monday")
- Keep 2-3 keywords max per ritual — more is never remembered

**Applies to:** Weekly briefing, context sync check, ROI check-in, memory audit, any maintenance behavior.

**Source:** Session 115 (2026-03-25) — Patrick's instinct confirmed by Grok Round 4
