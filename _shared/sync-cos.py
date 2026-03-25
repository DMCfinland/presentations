#!/usr/bin/env python3
"""
sync-cos.py — Synkronoi CURRENT-STATUS.md → weekly-context.md (CoS-botin System B)

Käyttö:
    python3 ~/1658HoldingsOy-AIFiles/_shared/sync-cos.py

Mitä tekee:
    1. Lukee CURRENT-STATUS.md:n Current State -taulukon
    2. Suodattaa arkaluontoiset termit (GDPR)
    3. Kirjoittaa TILA-osion weekly-context.md:ään
    4. Avaa tiedoston TextEditissä tarkistettavaksi ennen liittämistä

Huom: Älä poista tai muuta suodatinlistaa ilman harkintaa (GDPR).
"""

import re
import subprocess
from pathlib import Path
from datetime import date

# --- POLUT ---
BASE = Path.home() / "1658HoldingsOy-AIFiles"
SOURCE = BASE / "CURRENT-STATUS.md"
TARGET = BASE / "_drafts" / "weekly-context.md"

# --- GDPR-SUODATIN ---
# Lisää tähän termit jotka eivät saa mennä System B:hen
REDACT = [
    "AHI",
    "Frendy",
    "Roope Flinkilä",
    "Northern Lights Village",
]

def redact(text: str) -> str:
    for term in REDACT:
        text = re.sub(re.escape(term), "[kontakti]", text, flags=re.IGNORECASE)
    return text

def extract_current_state(source_text: str) -> dict:
    """Parsii Current State -taulukon rivit."""
    fields = {}
    # Etsi taulukon rivit: | **Field** | Value |
    pattern = re.compile(r"\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|")
    for match in pattern.finditer(source_text):
        key = match.group(1).strip()
        val = match.group(2).strip()
        # Muunna <br> rivinvaihdoiksi
        val = val.replace("<br>", "\n    ")
        fields[key] = val
    return fields

def build_tila_block(fields: dict) -> str:
    phase = fields.get("Current Phase", "[ei saatavilla]")
    next_tasks = fields.get("Next 3 Tasks", "[ei saatavilla]")
    blockers = fields.get("Blockers", "[ei saatavilla]")

    # Suodatus
    phase = redact(phase)
    next_tasks = redact(next_tasks)
    blockers = redact(blockers)

    today = date.today().strftime("%Y-%m-%d")

    return f"""## TILA (kopioitu CURRENT-STATUS.md:stä — {today})

**Current Phase:**
{phase}

**Next 3 Tasks:**
    {next_tasks}

**Aktiiviset blockerit:**
{blockers}"""

def update_weekly_context(tila_block: str):
    """Korvaa TILA-osion weekly-context.md:ssä."""
    content = TARGET.read_text(encoding="utf-8")

    # Etsi ja korvaa ## TILA ... ## VIIKON KOKOUKSET välinen osio
    pattern = re.compile(
        r"(## TILA \(kopioi CURRENT-STATUS\.md:stä\).*?)(## VIIKON KOKOUKSET)",
        re.DOTALL
    )

    new_content = pattern.sub(
        tila_block + "\n\n---\n\n## VIIKON KOKOUKSET",
        content
    )

    if new_content == content:
        # Fallback: korvaa koko TILA-blokki joustavammin
        pattern2 = re.compile(r"## TILA.*?(?=\n---|\n## VIIKON)", re.DOTALL)
        new_content = pattern2.sub(tila_block + "\n", content)

    TARGET.write_text(new_content, encoding="utf-8")

def main():
    print("🔄 sync-cos: luetaan CURRENT-STATUS.md...")

    if not SOURCE.exists():
        print(f"❌ Tiedostoa ei löydy: {SOURCE}")
        return

    source_text = SOURCE.read_text(encoding="utf-8")
    fields = extract_current_state(source_text)

    if not fields:
        print("❌ Current State -taulukkoa ei löydetty. Tarkista CURRENT-STATUS.md rakenne.")
        return

    print(f"✅ Löydettiin {len(fields)} kenttää.")

    tila_block = build_tila_block(fields)

    print("\n--- ESIKATSELU (kirjoitetaan weekly-context.md:ään) ---")
    print(tila_block)
    print("--- ESIKATSELU LOPPUU ---\n")

    confirm = input("Kirjoitetaanko weekly-context.md:ään? [y/n]: ").strip().lower()
    if confirm != "y":
        print("Peruttu.")
        return

    update_weekly_context(tila_block)
    print(f"✅ weekly-context.md päivitetty: {TARGET}")

    # Avaa TextEditissä tarkistettavaksi
    subprocess.run(["open", "-a", "TextEdit", str(TARGET)])
    print("📝 Avattu TextEditissä — tarkista ennen kuin liität CoS-bottiin.")

if __name__ == "__main__":
    main()
