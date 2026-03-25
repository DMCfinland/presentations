# Supersedes Field on New Patterns
<!-- source: knowledge-management-research-2026.md Section 5 | session: 70 -->
<!-- created: 2026-03-12 | confidence: 0.7 | tier: B -->

**What:** When writing a new BP pattern that updates or replaces old guidance, explicitly note which older pattern it supersedes — in both the new file and the old file.

**Why:** Without explicit supersession tracking, contradictory patterns coexist in the system. Old guidance stays active ("slow-motion context poisoning"). The Opus contradiction scan catches this periodically, but per-write tracking prevents accumulation between reviews. Stale guidance being actively used is worse than a missing pattern.

**When to apply:** Any time a new pattern changes a previous recommendation. Triggers: "we used to do X but now we do Y," model capability changes (Sonnet now beats Opus on X), tooling changes, approach reversals.

**How:**
- In the NEW pattern file header: add `supersedes: [old-pattern-filename]`
- In the OLD pattern file: add comment at top `# SUPERSEDED by [new-filename] as of session-N — read [new-filename] instead`
- In `_index.yaml`: add `supersedes: [old-filename]` field to new entry; mark old entry with `status: superseded`

**Example:** If a new pattern "sonnet-beats-opus-on-financial-analysis" is created, it should note `supersedes: any-older-guidance-recommending-opus-for-financial-work`.
