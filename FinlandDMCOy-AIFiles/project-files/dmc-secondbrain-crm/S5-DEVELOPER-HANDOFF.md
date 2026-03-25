# S5 Developer Handoff — DMC CRM Email Classifier: Deterministic Post-Processing Layer

**For:** TypeScript developer (Supabase + n8n stack)
**Date:** 2026-03-20
**Reads before building:** This file first, then `REGRESSION-FLYWHEEL-SPEC.md`

---

## What you are building in S5

The email classifier uses Claude (LLM) to label incoming emails into 8 classes.
The LLM is unreliable in one specific way: its reasoning can correctly identify a
booking reference number, a known partner domain, or a Finnish-language sender —
and still output the wrong label. This is not a prompt problem. It is structural
(see: chain-of-thought faithfulness research, `llm-reasoning-action-divergence.md`).

S5 builds a **TypeScript post-processing layer** that runs AFTER the LLM returns
its label and OVERRIDES it when a deterministic rule applies. This layer is what
makes the classifier trustworthy enough to route emails autonomously.

---

## Dependency chain

```
S3: Anti-anchoring pre-processing
  → strips headers, quoted threads, booking references from raw_email
  → outputs: { stripped_body: string, de_anchored: boolean, booking_ref: string | null }

S4: Confidence routing
  → threshold logic branches on de_anchored flag
  → outputs: { label: string, confidence_score: number }

S5 (YOU ARE HERE): Deterministic post-processing
  → reads S3 output signals + partners table + S4 label
  → applies 30 invariant rules
  → outputs: { final_label: string, override_fired: boolean, override_rule: string | null }

Flywheel (post-S5): Weekly regression test suite
  → validates S5 override layer works correctly
  → 30 core test cases + up to 20 long-tail cases
  → Supabase schema + n8n weekly workflow (see REGRESSION-FLYWHEEL-SPEC.md)
```

---

## What to implement

Open `REGRESSION-FLYWHEEL-SPEC.md` and read:

1. **Section "30 Core Invariants"** — these are the rules. Each is a TypeScript condition.
2. **Section "Invariant implementation note"** (at the bottom of that section) — tells you
   which invariants require: (a) partners table lookup, (b) booking reference regex,
   (c) language detection, (d) confidence score check. These are deterministic signals —
   implement them as TypeScript checks, NOT as prompt instructions.

### Input contract (from S3 + S4)
```typescript
interface ClassifierInput {
  stripped_body: string;        // from S3
  de_anchored: boolean;         // from S3
  booking_ref: string | null;   // from S3 regex
  sender_domain: string;        // parsed from email headers before S3
  detected_language: 'fi' | 'en' | 'de' | 'unknown';  // from S3
}

interface LLMOutput {
  label: EmailLabel;
  confidence_score: number;     // 0.0–1.0
}
```

### Output contract (from S5)
```typescript
interface ClassifierOutput {
  final_label: EmailLabel;
  override_fired: boolean;
  override_rule: string | null;  // e.g. 'invariant_18' — for logging/debugging
  confidence_score: number;      // passed through from LLM, unchanged
}

type EmailLabel =
  | 'hot-lead' | 'warm-lead' | 'cold-lead'
  | 'existing-partner' | 'spam' | 'operational'
  | 'supplier-inquiry' | 'media-press';
```

---

## Priority order for implementation

Build invariants in this order (highest error-cost first):

1. **Booking reference override** (invariants 18, 19, 20) — FIN-YYYY-NNN regex
2. **Known partner override** (invariants 3, 12, 13) — partners table lookup
3. **Finnish language override** (invariant 27) — language detection
4. **Hot-lead confidence gate** (invariant 30) — routes to human review if < 0.85
5. **Spam domain gate** (invariants 2, 6) — domain suffix allow/block list
6. Remaining invariants — implement as enum of label-pair rules

---

## Regression testing (post-S5)

Once S5 is live, the flywheel activates. The Supabase schema and n8n workflow are
fully spec'd in `REGRESSION-FLYWHEEL-SPEC.md`. Do not build the flywheel before S5
is stable — the 30 invariants are the test cases, so the layer must exist first.

---

## Known limitations (from Grok audit — not blocking S5)

- **Stale deterministic layer risk:** Partners table and booking reference regex will
  evolve. When either changes, re-run regression immediately (use `trigger_source = 'version_change'`
  in run log). The weekly Monday schedule alone is insufficient after a schema change.
- **Statistical thinness:** With 200-500 emails/month across 8 classes, rare subclasses
  (media-press, supplier-inquiry) may have < 10 examples in year 1. The invariant-based
  approach handles this — rules don't require examples to fire.
- **80-case cap:** Research suggests 50-200+ cases for robust regression. The 80-case cap
  is a maintenance budget constraint, not an accuracy target. When the team grows or
  maintenance budget increases, raise the cap before the long-tail ratio.

---

*Handoff created S102 (2026-03-20). Next: Patrick activates S5 session with this file + REGRESSION-FLYWHEEL-SPEC.md as source documents.*
