# New Opus Follow-Up Questions (Q7-Q12)

**Context:** The Opus claude.ai Project conversation is still open. Files are deleted so queries are cheap (~$0.50 each). Opus retains its conversation history including all Q1-Q6 answers. It has deep recall of ~30 videos and partial recall of ~50.

**Strategy:** Extract maximum remaining value from the 30 videos Opus DID read deeply. Don't ask it to recall what it didn't read — ask it to go deeper on what it knows.

---

## Q7: Named Frameworks & Vocabulary Extraction

> From the ~30 videos you deeply engaged with, list every specific NAMED FRAMEWORK, COINED TERM, or MEMORABLE PHRASE you encountered. Not patterns you inferred — the actual vocabulary and concepts as Nate (or the video creator) named them. For each, give the term, a one-sentence definition, and which video it came from.
>
> Examples of what I mean: "Ferrari failure mode," "heap-not-hierarchy," "four knobs of reliability," "intelligence-resistant problems."
>
> I want the raw vocabulary list. This becomes my search index.

**Why:** These exact terms become tags and `key_concepts` in our routing index. We can't extract them from videos Opus didn't read, but we get 30 videos' worth of precise terminology for free.

---

## Q8: Anti-Patterns and Warnings

> From what you read, what specific WARNINGS, ANTI-PATTERNS, or "things NOT to do" did the videos highlight? I find anti-patterns are often more actionable than positive advice. Include:
> - The anti-pattern name or description
> - Why it fails
> - What to do instead
> - Which video it came from (if you remember)

**Why:** Anti-patterns are the highest-ROI content for a CEO. "Don't do X" prevents $50K mistakes. These go into a standalone reference doc.

---

## Q9: If I Could Only Keep 10 Videos

> If I could only keep 10 videos as permanent reference documents from the ones you actually read, which 10 would you recommend? For each, give:
> - The video (as best you can identify it)
> - The ONE question it answers better than any other source
> - Why it's irreplaceable (not just "good" — what would I lose without it?)

**Why:** Creates an immediate "greatest hits" shortlist. These 10 get priority human review and become the test set for validating our digest quality.

---

## Q10: Sonnet Compression Prompt Design

> I'm about to process all 195 video analyses through Sonnet to create 1.5KB compressed digests. Based on the ~30 videos you deeply read:
>
> 1. What FILLER PATTERNS did you notice that are safe to remove? (e.g., repeated intros, generic conclusions, timestamp padding)
> 2. What CONTENT PATTERNS must be preserved? (e.g., specific frameworks, named concepts, quantified claims, contrarian insights)
> 3. What gets LOST in compression that shouldn't? What would you warn the compression prompt about?
> 4. Draft me a 200-word compression prompt instruction that a less capable model (Sonnet) could follow faithfully.

**Why:** Opus read 30 of these files at full fidelity. It knows what the raw content looks like and what matters. This directly produces the Step 2 compression prompt.

---

## Q11: Cross-Video Connections

> From the videos you deeply read, what CONNECTIONS BETWEEN VIDEOS did you notice? Cases where Video A's framework explains Video B's observation, or where two videos contradict each other, or where combining insights from multiple videos produces something neither says alone.
>
> List as many as you can. Format: "Video A + Video B → Combined insight"

**Why:** Cross-references are the hardest thing to build computationally. Opus saw 30 videos in the same context window — it may have spotted connections that file-by-file processing will miss. These become seed data for our `related_videos` field.

---

## Q12: Your Internal Experience (Meta-Learning)

> You gave incredibly honest self-assessment in Q5-Q6. I want to document this as a reusable best practice for future expensive sessions. Can you tell me:
>
> 1. At what point in processing the file did you "know" you couldn't read it all? Was there a moment of recognition?
> 2. When you were extrapolating vs. recalling, were you aware of the difference in real-time?
> 3. What signals should I watch for in future large-context responses that indicate the model is extrapolating rather than recalling?
> 4. If you could redesign how I submitted the 195 videos, what format/structure would have given you the best chance of faithful processing?
>
> This isn't criticism — it's engineering. Your honest answer here becomes a template for every future expensive query across 10 companies.

**Why:** This creates the definitive "how to work with large context" guide, written by the model that experienced the failure. Reusable across all portfolio companies.

---

## Sending Instructions

1. Copy each question into the Opus claude.ai Project conversation one at a time
2. Wait for full response before sending next question
3. Save responses back here as q7 through q12 files
4. Total estimated cost: ~$3-6 for all 6 questions (conversation history only, no files)
5. **Do this before closing the conversation window** — once closed, this context is gone forever
