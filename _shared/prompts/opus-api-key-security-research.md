# Opus Research Prompt: API Key Security Best Practices (2026)

## Context

I'm the CEO of 1658 Holdings Oy, managing AI workflows across 10 portfolio companies (~50 employees). I use multiple AI services (Anthropic, OpenAI, Perplexity, etc.) and need a secure, practical API key management strategy.

**Current Setup:**
- Mac (macOS Sonoma/Sequoia)
- Claude Code CLI for local development
- Anthropic Batch API for cost optimization
- Multiple API keys: Anthropic, OpenAI, Perplexity, potentially others
- Two-zone architecture: Zone A (local Git repo) + Zone B (OneDrive → SharePoint)
- Multiple projects across different company folders
- Some scripts need API access (batch status checks, automated workflows)

**Current Problem:**
- API keys are NOT persisted properly
- Using temporary `export ANTHROPIC_API_KEY="..."` in each terminal session
- No clear strategy for multiple keys across multiple projects
- Need to balance security with convenience (don't want to enter password every time)
- Team members will eventually need access to some keys (e.g., for SEO tools)

**Key Requirements:**
1. **Security:** Keys should NEVER be committed to Git or exposed in plain text unnecessarily
2. **Convenience:** Shouldn't require password entry for every API call
3. **Multi-project:** Some keys are global (Anthropic), others are project-specific (customer API keys)
4. **Team-ready:** Future-proof for when employees need access to certain keys (but not all)
5. **Automation-friendly:** Scripts and batch jobs need to access keys programmatically
6. **Auditable:** Should be able to track which keys are used where

---

## Research Questions

### 1. Modern API Key Management Landscape (2026)

What are the current industry-standard approaches for API key management in 2026?

- **Developer tools:** 1Password CLI, Bitwarden CLI, macOS Keychain, direnv, envchain, etc.
- **Enterprise solutions:** HashiCorp Vault, AWS Secrets Manager, Azure Key Vault
- **Best practices:** What changed since 2024? Any new standards or tools?
- **AI-specific considerations:** Do AI API keys (Anthropic, OpenAI) have unique security requirements?

### 2. macOS-Specific Solutions

For a Mac-native workflow, what are the BEST options ranked by security + convenience?

- **macOS Keychain:** Native, secure, but how to integrate with CLI workflows?
- **1Password CLI:** We already use 1Password family plan - is this the killer solution?
- **Bitwarden CLI:** Open-source alternative
- **direnv + .env:** Simple but secure enough?
- **Comparison matrix:** Security, convenience, team access, automation support

### 3. Project-Level vs. Global Keys

What's the best architecture for managing keys across multiple projects?

- **Global keys:** Anthropic API key used across all projects - where should it live?
- **Project-specific keys:** Customer API keys, project-specific credentials
- **Environment isolation:** How to prevent cross-project key leakage?
- **Pattern recommendation:** Should I use different approaches for different key types?

### 4. Team Access Model

We're a 50-person company with 10 business units. Eventually, some employees will need API access.

- **Access levels:** How to grant SEO manager access to SEO tools but NOT Anthropic key?
- **Shared secrets:** Best way to share keys with specific team members?
- **Rotation strategy:** How often should keys be rotated? How to automate rotation?
- **Audit trail:** How to track who used which key when?

### 5. Git Safety

How to ensure keys NEVER leak into version control?

- **.gitignore patterns:** What should be in global vs. project .gitignore?
- **Pre-commit hooks:** Should I use git-secrets or similar tools?
- **Secret scanning:** GitHub secret scanning, Anthropic's key revocation - how to leverage?
- **Accident recovery:** If I accidentally commit a key, what's the recovery playbook?

### 6. Automation & Scripts

I use batch API scripts, cron jobs, and automated workflows. Keys need to be accessible programmatically.

- **Non-interactive access:** How to authenticate scripts without manual password entry?
- **Batch API use case:** Best way to handle long-running batch jobs that need API access?
- **Cron jobs:** If I schedule a nightly batch job, how does it get the key?
- **Error handling:** What if key retrieval fails? How to log/alert without exposing the key?

### 7. OneDrive/SharePoint Integration

Zone B syncs to OneDrive/SharePoint for M365 search. Keys MUST NOT sync to cloud.

- **Exclusion patterns:** How to ensure .env files never sync to OneDrive?
- **Zone A vs. Zone B:** Should keys ONLY ever live in Zone A (local Git)?
- **Verification:** How to audit that no keys have leaked to SharePoint?

### 8. Cost-Benefit Analysis

Don't over-engineer. What's the right level of security for a 50-person company?

- **Threat model:** What are the realistic risks? (Laptop theft, Git leak, shoulder surfing, malware)
- **ROI:** Is enterprise Vault worth it, or is 1Password CLI + good practices enough?
- **Complexity vs. security:** Where's the sweet spot for our company size and use case?

---

## Deliverable Format

Please provide:

### 1. Executive Summary (1 page)
- Recommended solution for 1658 Holdings
- Why this approach (security + convenience + cost)
- Migration path from current state

### 2. Architecture Diagram (text/ASCII)
- How keys are stored
- How they're accessed (CLI, scripts, team members)
- Access control model

### 3. Implementation Guide (step-by-step)
- Exact commands to set up the system
- How to store first key (Anthropic API key)
- How to retrieve in different contexts (terminal, script, cron)
- How to add project-specific keys
- How to grant team member access

### 4. Best Practices Checklist
- What to ALWAYS do
- What to NEVER do
- Audit checklist (quarterly key hygiene review)

### 5. Migration Plan
- Step 1: Set up key management system
- Step 2: Migrate existing keys
- Step 3: Update scripts to use new system
- Step 4: Verify no keys in Git history or OneDrive
- Step 5: Team rollout plan

### 6. Troubleshooting Guide
- "I can't access the key in my script" → solution
- "I accidentally committed a key" → recovery playbook
- "Key retrieval is too slow" → optimization
- "Team member needs access to specific key" → delegation procedure

### 7. Future-Proofing
- When to upgrade to enterprise Vault
- Key rotation schedule
- Annual security review checklist

---

## Quality Standards

- **Actionable:** I should be able to implement this TODAY
- **Specific:** No vague advice like "use a password manager" - tell me WHICH one and HOW
- **2026-current:** Focus on modern tools and practices, not outdated 2020 advice
- **Opinionated:** Don't give me 10 options - recommend THE BEST solution for my context
- **Trade-offs explicit:** If convenience sacrifices security, SAY SO clearly
- **Cost-conscious:** Don't recommend $50k/year enterprise solutions for a 50-person company

---

## Output File Name

Save the research output as: `_shared/best-practices/api-key-security-2026.md`

This will become the canonical reference for API key management across all 10 companies in the portfolio.

---

## Budget

This is a foundational security topic that affects all projects. Use Opus. Take your time. Be thorough.

Estimated cost: $3-8 for a comprehensive 10,000-20,000 word research document.

**This is worth it.** Getting API key security wrong could cost us far more than $8.
