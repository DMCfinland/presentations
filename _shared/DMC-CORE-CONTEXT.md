# DMC-CORE-CONTEXT.md
# Canonical lean reference — inject via /read in any bridge prompt.
# No session-specific content. No project status. No open tasks.
# Last updated: 2026-03-19 (session 99)

## Company
- **Name:** Finland DMC Oy
- **Type:** B2B Destination Management Company
- **Regions:** Lapland + Lakeland (inbound Finnish travel for corporate groups)
- **Holding:** 1658 Holdings Oy (10 portfolio companies, Patrick Heiskanen CEO)

## Team
- **Staff:** 6 people — non-ML TypeScript developers
- **Languages:** Finnish, English, German (all three in production)
- **Developer profile:** TypeScript only. No ML infra. No Python. No model retraining.

## Technical Stack
- **Automation:** n8n (email ingestion, scheduled triggers, webhook routing)
- **Database:** Supabase (PostgreSQL — all CRM data, classifier tracking)
- **Frontend:** Next.js (Kanban board, internal dashboard)
- **Email API:** Microsoft Graph API (shared mailbox + Teams + SharePoint via M365 connector)
- **Mining tool:** claude.ai browser with M365 connector + Opus — NOT Claude Code

## Email Classifier
- **Volume:** 200–500 relevant emails/month
- **Label classes (8):** hot-lead, warm-lead, cold-lead, existing-partner,
  spam, operational, supplier-inquiry, media-press
- **Languages:** Finnish + English + German — all three must be handled
- **Starting state:** Zero labeled examples — building classifier from scratch
- **Routing logic:** TypeScript + Supabase queries — no ML model serving

## Mining Process
- Patrick mines email history in claude.ai browser (not API, not Claude Code)
- Pre-processing = manual step or Terminal script BEFORE pasting into claude.ai
- M365 connector searches: shared mailbox + Teams channels + SharePoint
- Output: "Second Brain" knowledge base (client intel, deal history, partner data)
- GDPR: No real email content, names, or company names in specs — synthetic only

## File Zones
- **Zone A (Workshop):** ~/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/
- **Zone B (Knowledge):** ~/OneDrive - 1658 Holdings/FinlandDMCOy/AI-Knowledge/

## CRM Classifier Architecture (stable — not session-specific)
- Email pre-processing runs BEFORE LLM classification (strips anchoring signals)
- Progressive autonomy: zero-overrides-in-N-days per subclass (no confidence scores)
- S3→S4 coupling: pre-processing changes input distribution → routing thresholds
  must branch on `de_anchored: boolean` flag in email metadata
- Any active session bridge files live in: ~/1658HoldingsOy-AIFiles/_drafts/

## Build Sequence
S3 (de-anchoring) → S4 (confidence routing) → **S5: deterministic post-processing layer**
→ Flywheel (regression testing, runs weekly after S5 is live)

## S5 Developer Spec (next build session)
File: `FinlandDMCOy-AIFiles/project-files/dmc-secondbrain-crm/REGRESSION-FLYWHEEL-SPEC.md`
- Section **"30 Core Invariants"** = the TypeScript rules the developer must implement
  as deterministic overrides AFTER LLM returns its label (not as prompt instructions)
- Section **"Invariant implementation note"** = which invariants need table lookups vs regex
- Section **"Supabase Schema"** = regression_golden_set + regression_run_log tables (build S5+)
- Section **"Weekly n8n Workflow"** = operational regression loop (build post-S5)
- Spec version: 1.1 (Grok-audited, CONDITIONAL GO — S99/S102)
