# Opus Research Prompt: API Key Security for Non-Developer CEO on macOS

**Purpose:** Get Opus to research and recommend the safest, simplest API key management approach for Patrick's specific situation.
**Send to:** claude.ai with Opus, or Batch API (~$0.50-1)
**Output:** Concrete setup instructions to paste into terminal

---

## Prompt

You are an expert in API key security and macOS system administration. Your task is to research and recommend the BEST and SAFEST way to manage API keys for a non-developer CEO who uses Claude Code (CLI) and Python scripts on macOS.

### Context

**User profile:**
- CEO of a holding company (10 companies, ~50 employees)
- Works on macOS (Darwin 24.6.0, Apple Silicon)
- Uses Claude Code CLI tool daily (needs ANTHROPIC_API_KEY available in terminal)
- Runs Python scripts that call Anthropic Batch API (needs key in `os.environ`)
- Non-developer — needs simple, reliable approach that doesn't break
- Files are in a Git repository — keys must NEVER be committed
- Multiple projects may need different API keys in the future
- Also needs to store other API keys eventually (OpenAI, Google, etc.)

**Current problem:**
- API key was set temporarily in a previous terminal session
- Session ended, key is gone
- No `.env` file exists
- Cannot retrieve Batch API results without the key
- Existing SECURITY.md in project has basic advice but no macOS-specific recommendation

**Requirements:**
1. Key must persist across terminal sessions (survives restart)
2. Key must be available to both Claude Code CLI and Python scripts
3. Key must NEVER end up in Git (even by accident)
4. Setup must be simple enough for a non-developer to maintain
5. Must support adding more API keys later
6. Should work with zsh (macOS default shell)
7. Ideally uses macOS-native security features (Keychain, etc.)

### Research Questions

Please research and answer ALL of the following:

1. **macOS Keychain approach:**
   - Can API keys be stored in macOS Keychain and retrieved in terminal?
   - Exact commands to store and retrieve
   - How to auto-export to environment variables on shell startup
   - Pros/cons vs. other approaches

2. **~/.zshrc export approach:**
   - Is `export ANTHROPIC_API_KEY="sk-..."` in ~/.zshrc safe enough?
   - What are the actual risks? (file permissions, backup exposure, etc.)
   - How to secure ~/.zshrc file permissions

3. **Dedicated secrets file approach:**
   - Create `~/.secrets` or `~/.api-keys` file, source from ~/.zshrc
   - Better isolation than putting keys directly in .zshrc?
   - Standard pattern for this?

4. **1Password CLI approach:**
   - Does Patrick already use 1Password? (assume he might)
   - How does `op run` work for injecting secrets?
   - Is this overkill for a solo developer?

5. **direnv approach:**
   - Per-project `.envrc` files with direnv
   - Automatic loading/unloading of keys per directory
   - Good for multiple projects with different keys?

6. **Python-specific: python-dotenv approach:**
   - Project-level `.env` files loaded by scripts
   - Works alongside any of the above
   - Standard `.gitignore` pattern

### Deliverables

Please provide:

1. **Ranked recommendation** (best → acceptable) with reasoning
2. **Step-by-step setup instructions** for the #1 recommendation — exact terminal commands, copy-paste ready
3. **Verification commands** to confirm it works
4. **Fallback option** if #1 is too complex
5. **Multi-key management** — how to organize when we have 3-5 different API keys
6. **Git safety checklist** — prevent accidental commits of key files
7. **Recovery procedure** — what to do if a key is compromised

Format: Write the setup guide as a markdown file ready to save as `_shared/best-practices/api-key-management.md`. Include exact commands — no placeholders except the actual key value.

### Anti-laziness instructions
- Write the FULL setup guide directly. Do NOT say "you should research..." or "consider looking into..."
- Include ACTUAL terminal commands, not descriptions of commands
- Test your reasoning: would a non-developer be able to follow this without Googling?
- If you're unsure about a macOS-specific detail, say so explicitly rather than guessing
