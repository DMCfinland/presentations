<!-- .github/copilot-instructions.md for Finland DMC Oy (concise, actionable) -->
# Quick instructions for AI coding agents

These notes help an AI agent be immediately productive in this repository. Focus on the mining-driven, text-first workflow used by the project.

- Project type: not a software build — this repository contains project configuration, mining reports and final text artifacts (see `finland-dmc-2.0/CLAUDE.md`).
- Primary workflow: "mine first, build after" — all final files in `project-files/` must be created from real mined data saved under `mining-outputs/` (see `MINING_PROTOCOL.md`).

- Key files you will read and update:
  - `finland-dmc-2.0/CLAUDE.md` — authoritative project rules and natural-language commands
  - `finland-dmc-2.0/MINING_PROTOCOL.md` — step-by-step mining session process and report format
  - `finland-dmc-2.0/ROADMAP.md` — progress tracker; commands like `status` and `mark [task] done` update this file

- Natural-language CLI used by humans/agents (examples):
  - `status` — display CURRENT STATUS block from `ROADMAP.md`
  - `show mining [N]` — list files in `mining-outputs/session-[N]-*/`
  - `build [project]` — assemble/update files in `project-files/[project]/` from mined data
  - `save checkpoint` / `show report` — used during mining sessions to produce copy/paste-ready reports

- Patterns & constraints to preserve:
  - Always keep raw mining reports intact in `mining-outputs/` (filename: `mining-report.md`).
  - When building, draft files and ask for approval before saving to `project-files/`.
  - One golden prompt / Custom_Instructions.txt per project; these must be drawn from actual mined examples (see templates like `templates/Best_Lines_Starter.txt`).

- Helpful file locations to reference in edits or suggestions:
  - `finland-dmc-2.0/mining-outputs/` (session folders)
  - `finland-dmc-2.0/project-files/` (final outputs)
  - `finland-dmc-2.0/templates/` (examples only — do NOT treat as final)

- When updating docs or ROADMAP.md:
  - Preserve existing session timestamps and completion notes.
  - Add new session entries using the `new session` convention in `CLAUDE.md`.

- Merge guidance: If `.github/copilot-instructions.md` already exists, merge conservatively — keep any custom rules already present and add or update the sections above. If unsure, open a PR and request a human review.

If any section is unclear or you need examples of mined data to proceed, ask for the specific `mining-outputs/session-[N]-*/mining-report.md` to inspect. Ready to update or expand this file with any specific details you want included.
