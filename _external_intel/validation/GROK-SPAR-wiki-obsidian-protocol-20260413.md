---
source: grok-expert
date: 2026-04-13
topic: wiki-obsidian-session-protocol-redesign
status: ok
---

Thought for 56s

Consensus Round 1-2 MAD ratings (prod ops lens: concurrent multi-tab Claude sessions, Patrick’s real workflow, flaky networks, human overrides, filesystem realities as of April 2026):
KV1: 4
KV2: 5
KV3: 5
KV4: 4
KV5: 5

The proposal’s core bet — deferred cheap compilation into entity pages as living single source of truth — collapses under normal production conditions. Multiple 5s mean this is not a minor tweak; it is a structural ops failure waiting to happen.

Two (actually three) kill vectors the proposal did NOT list

Missed KV-A: No atomicity or transaction model in mcpvault v0.11.0 writes.
Deferred compilation runs a Haiku subagent that does multiple file opens/reads/writes (YAML frontmatter + full entity page synthesis across 8 sessions). Any interruption (token limit hit, network hiccup, subagent crash, or Claude Code tab reload) leaves the wiki in a half-updated state: some pages updated, others stale, frontmatter last_updated inconsistent. Karpathy’s own April 2026 pattern and every public mcpvault production fork explicitly call out that filesystem writes are not transactional. Patrick ends up trusting a wiki that is silently corrupted until the next manual audit.

Missed KV-B: Real-time Obsidian graph view + backlinks become dangerously misleading during hot/deferred cycle.
Patrick keeps Obsidian open side-by-side (exactly as Karpathy’s pattern intends). Hot session writes only a 2-line stub + wiki_delta pointer. Fresh session later recompiles. In between, graph view, embeds, and embedded queries show incomplete/outdated entity pages. He makes pricing or financing decisions on stale synthesis. Production adaptations of the Karpathy pattern (multi-agent Claude Code setups with 6+ parallel agents) all hit this: the “live IDE” advantage turns into live misinformation.

Missed KV-C: Bidirectional edit conflicts with no merge strategy.
Patrick (or any human) will edit entity pages directly in Obsidian while AI sessions are running. mcpvault has no built-in diff/merge logic for YAML frontmatter or section-level updates. Next compile overwrites or silently drops human changes. The proposal treats entity pages as “the context,” but never closes the human↔AI edit loop.

Specific fixes required for any 4-5 severity KV (non-negotiable for prod)
KV2 + Missed KV-A (concurrency + atomicity, both 5): Add a custom mcpvault tool (or wrapper script) that implements per-entity file locking via .lock sentinel files + atomic rename (write to entity.md.tmp then mv). For compilation step: read → modify → validate frontmatter → atomic write in a single MCP call. If lock contended >5s, abort session with explicit “concurrent edit detected — retry after 30s”. This is the exact pattern used in the production multi-agent Karpathy forks that actually scale beyond single-user.
KV3 (directory divergence, 5): Eliminate the two directories. Configure mcpvault to point Claude Code workspace directly at ~/vaults/1658/wiki/ (or use a bind mount/symlink so the Claude workspace folder is the Obsidian one). Single source of truth or it is guaranteed drift. The current “same files Patrick browses” claim is marketing — filesystem paths differ, therefore they are not the same files in ops reality.
KV5 + Missed KV-B (discipline + stale graph, both 5): Hard enforcement, not prompt discipline. Create a 1-line MCP preflight tool “check-wiki-delta” that every fresh session (and every hot session start) must call first. If wiki_delta exists, the agent is forced to run compile before any other tool or response. Add a 10-second Obsidian plugin notification or daily note banner: “Pending wiki compilation — graph may be stale.” Remove the option to skip.
KV4 (Haiku synthesis risk, 4): Hybrid step only. Haiku drafts the entity page update; a cheap Sonnet review pass (or even just a structured diff check) validates against the full 8-session history before write. Finnish real-estate financing (DSCR methodology, LTV thresholds, tonttirahoitus specifics) is exactly the domain where cheap models quietly drop edge cases.
Missed KV-C (bidirectional edits): On every entity page load in a session, mcpvault must return last-modified timestamp + a short git-style diff against AI’s last known version. Compilation becomes “merge” not “overwrite.” Add a simple 3-way merge rule for frontmatter only.
Honest overall rating

3/10 viability in production as proposed.
The cost math checks out directionally (Haiku + fresh 2K context is genuinely cheaper), and the Karpathy April 2026 pattern + mcpvault v0.11.0 are both real and battle-tested in single-user, low-concurrency setups. But the redesign ignores the exact failure modes that killed every naive “deferred wiki” implementation in multi-session, multi-tab, human-in-the-loop production environments we see right now: race conditions, partial writes, stale views, and human discipline collapse.

Without the atomicity, locking, single-directory, and mandatory preflight fixes above, this will produce diverging entity pages, corrupted frontmatter, and decisions made on outdated knowledge within the first two weeks of real concurrent use. The deferred protocol saves pennies while introducing dollar-level operational debt. Implement the fixes or revert to in-hot-session compilation with proper locking — the “pure pointer file” elegance is not worth the ops pain it creates.

100 sources
