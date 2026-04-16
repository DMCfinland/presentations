# Riikka S200 Bridge Spar — Gemini Cross-Validation
Gap report:

### Confirmed Decisions (no new findings)
Most of the stated decisions appear sound in principle, particularly the general design for dashboard rendering, retry mechanisms, graceful error handling, use of `python-telegram-bot`'s `JobQueue`, the "draft only" rule for the bot, the consolidated Haiku call for scoring, Pydantic/Instructor usage, and the overall hard gates and sequencing. The scoring weights sum to 1.0, and the logic for "Cold leads CAN reach 100" and "1st degree (1.5x) needs base>=67 to hit 100" is mathematically consistent with a multiplicative warmth factor, assuming an underlying dimension scoring scale (see missing constraints).

### Questionable Decisions

*   **[Lucas, Harper] Track B — Telegram Bot: `launchd plist` deployment strategy for Windows user.**
    *   **Questionable Decision:** The bridge specifies `launchd plist` for bot deployment. `launchd` is a macOS-specific service management framework. The target user (Riikka) uses a Windows laptop.
    *   **Impact:** This is a fundamental platform mismatch. The proposed deployment mechanism for the bot is entirely incompatible with the user's operating system. It will fail to deploy or run the bot on Riikka's machine, making Track B non-functional from the outset.
*   **[Lucas] Track A — Dashboard: `HTML < 2MB, truncate pipeline to 20 active contacts`**
    *   **Questionable Decision:** Hard-coding a limit of 20 active contacts for the dashboard.
    *   **Impact:** While a 2MB HTML target is reasonable for local rendering, an arbitrary limit of 20 active contacts might be too restrictive for a senior executive managing many leads. This could be a significant usability gap and frustrate the non-technical user if they need to see more contacts and the system hides them without clear explanation or an option to override. This prioritizes a technical constraint (HTML size) over potential user workflow needs without explicit validation.
*   **[Harper] Track B — Telegram Bot: Reliance on `JobQueue.run_daily()` for critical tasks with `launchd KeepAlive`.**
    *   **Questionable Decision:** The `Stale draft cleanup at 09:00 daily` and `healthchecks.io silent ping` rely on the internal `JobQueue` scheduling within the bot process. `launchd KeepAlive=true` ensures the *process* restarts if it crashes, but it does *not* persist the internal state of the `JobQueue`.
    *   **Impact:** If the bot process crashes and restarts *after* its scheduled `run_daily()` time (e.g., crashes at 08:30, restarts at 09:10), the `09:00` stale draft cleanup or silent ping job will be missed for that day. This can lead to stale drafts persisting longer than intended and potentially missed health pings.

### Missing Constraints

*   **[Lucas] Interface Contract: Explicit `pipeline.yaml` schema definition.**
    *   **Missing Constraint:** `pipeline.yaml` is a central, shared data store. Track A (Dashboard) reads it, and Track B (Telegram Bot) writes to it. The bridge document provides no explicit schema or data contract for this YAML file.
    *   **Impact:** Without a defined schema, there is a high risk of integration issues during S201. Track A might expect fields or structures that Track B doesn't provide, or vice-versa, leading to parsing errors, data inconsistencies, or unexpected behavior even with file locking. This is a critical interface gap.
*   **[Benjamin] Scorer v4: Scale of individual dimension scores from Haiku LLM.**
    *   **Missing Constraint:** The bridge defines weights for the 6 dimensions but does not specify the numerical scale that the Haiku LLM will output for each dimension (e.g., 1-5, 0-100).
    *   **Impact:** While the overall math for weights and warmth factor holds true, the base assumption that `base_score` (sum of weighted dimensions) can reach 100 (which is necessary for "Cold leads CAN reach 100") implies that individual dimension scores from Haiku must implicitly also be scaled to contribute to a sum of 100. This unstated assumption is crucial for the scoring model's output to be in the desired 0-100 range.
*   **[Lucas, Harper] Track B — Telegram Bot: Windows deployment strategy.**
    *   **Missing Constraint:** Given the `launchd` error, a robust, equivalent Windows-native solution for ensuring the bot runs automatically, continuously, and restarts on failure (e.g., using Windows Task Scheduler with a script, a systemd-like service wrapper for Windows, or NSSM) is entirely absent.
    *   **Impact:** Without a defined Windows deployment strategy, Track B cannot be deployed or tested effectively on Riikka's machine, completely blocking its path to production.
*   **[Lucas] File Locking: Specific cross-platform implementation.**
    *   **Missing Constraint:** The bridge mentions "Read-side filelock on pipeline.yaml" and "All pipeline writes via PipelineTracker + filelock only". While critical, it doesn't specify the chosen file locking mechanism.
    *   **Impact:** File locking behavior can vary across operating systems. For a Windows user, relying on a Python library that transparently handles Windows-native file locking (e.g., `portalocker` or `filelock`) is crucial. Assuming a generic `flock`-like behavior without specifying the library risks potential cross-platform compatibility issues or non-functional locking on Windows.

### Sequencing Risks

*   **[Lucas, Harper] Critical Path Blocker: Incorrect platform for bot deployment.**
    *   The `launchd plist` assumption for a Windows user is the single most critical, immediate build risk. It directly blocks the completion of S200B (Telegram Bot build) and thus any "live test" or integration into S201. This needs to be resolved before any code for bot deployment can be generated or tested.
*   **[Lucas] Integration Risk: Undefined `pipeline.yaml` schema.**
    *   While S200A and S200B builds are parallel, their resulting runtime components critically depend on `pipeline.yaml`. Without a defined schema, S201 (integration + smoke tests) is highly likely to encounter data parsing errors and inconsistencies between the dashboard and bot, requiring significant rework.
*   **[Lucas] Misleading Independence Claim:**
    *   The statement "S200A, S200B, S200C run in PARALLEL (independent, no shared state during build)" is misleading in the context of *runtime artifacts*. While the *build process itself* might be independent, the resulting components (Dashboard, Bot, Scorer) absolutely share state (`pipeline.yaml`) and have implicit data dependencies (Scorer relying on `pipeline history`). This mischaracterization could lead to underestimating the complexity of S201.

### Verdict

The most immediate and critical error is the **platform mismatch for the Telegram bot's deployment (`launchd` on Windows)**. This will completely block Track B's live testing and S201 integration. Resolving this with a robust Windows-native service management solution is paramount.

The biggest **interface contract gap** is the lack of an explicit `pipeline.yaml` schema, which is a significant risk for data consistency and integration bugs in S201 between the Dashboard and the Bot.

The one **assumption that, if wrong, makes the 4-week shadow mode timeline meaningless** is the implicit assumption that the `pipeline history` will be sufficiently rich and accurately populated (likely by the newly built bot) to provide meaningful input for Scorer v4's shadow mode testing and comparison against v3. If Track B's deployment or functionality is delayed or flawed (due to the `launchd` issue or other bugs), the data used for shadow mode will be unreliable, rendering the comparison period ineffective for evaluating v4.
