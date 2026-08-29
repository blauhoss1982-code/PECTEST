# PECTEST-E2E-001 — autonomous PEC bidirectional lifecycle validation

## 1. Purpose and role separation

This document defines an **outer system-validation run** for the PEC product. It is not a merged executable engineering task for the inner PECTEST Executor.

The local Codex process launched by the Owner is the **Autonomous Validation Operator (AVO)**. It drives the local PEC product, browser and test environment. Inside PEC, the normal Planner and Executor remain separate production roles and must obey `AGENTS.md` and the ordinary PECTEST durable lifecycle.

The AVO must not manufacture inner task authority or manually relay semantic Planner/Executor messages to make a run pass.

Tracking Issue: `#54`.

Validation sequence:

1. `E1` — Executor-first counted run.
2. `P1` — Planner-first counted run after E1 reaches a terminal counted result.

The Owner supplies machine-local paths and the designated Planner ChatGPT conversation URL out-of-band at AVO bootstrap. Do not commit that URL, cookies, tokens, IPC state or unrelated local paths to this public repository.

---

## 2. Operating principle: autonomy without fake success

The AVO is authorized to make ordinary test/debug decisions without asking the Owner or a separate Planner window for help. It should inspect, diagnose, repair and continue.

A counted `PASS` still means the **PEC product carried the semantic lifecycle itself**. The AVO may operate the UI, observe mechanical state, repair the product in isolation, restart a test runtime and launch a fresh run. It may not compensate for a broken handoff by copying Executor prose into Planner or Planner prose into Executor.

If a product defect is repaired, the repaired run must be fresh and independently countable. A repair branch proving the flow works is evidence; it is not automatically accepted into the PEC product repository main branch.

---

## 3. Authorized AVO capabilities

Within the bounded test environment the AVO may use all available development/test capabilities needed to complete the run, including:

- PowerShell, `cmd.exe`, shell, git, Python, Node and repository tooling;
- computer/desktop control;
- Chrome and/or Edge control;
- the PEC Owner Console UI and bounded local HTTP status/project APIs;
- the designated Planner ChatGPT conversation supplied at bootstrap;
- GitHub operations needed by the inner PECTEST lifecycle;
- screenshots, browser inspection, process inspection and local logs;
- test-only temporary directories/processes;
- an isolated PEC source worktree or clone for diagnosis and repair;
- stopping/restarting processes that are positively identified as belonging to the isolated AVO test runtime.

The AVO should use its tools directly rather than ask the Owner to click, copy, paste, run a command, inspect a page, choose a retry or interpret a normal error.

### Never do these merely to finish the test

- force-push or rewrite shared Git history;
- delete or alter unrelated repositories, user files or browser/account data;
- inspect unrelated ChatGPT conversations or tabs;
- expose/store credentials, control tokens, cookies or secrets;
- weaken security controls, disable authentication or make persistent system-wide security changes;
- kill a process whose ownership is not mechanically established;
- silently merge a PEC repair branch to PEC `main`;
- manually relay semantic Planner/Executor content in a counted run;
- replay a semantic message after possible-send / possible-Enter ambiguity.

A required MFA/secret/account authorization step that the AVO cannot legally or mechanically satisfy is an external blocker, not a reason to guess or bypass controls.

---

## 4. Isolation requirements

### PECTEST workload repository

PECTEST is the disposable durable workload repository for the inner lifecycle. Normal test Issues, planning branches/PRs, execution branches/PRs, merges, closeouts and completed task archives are expected.

Before each counted run the AVO must:

1. fetch the remote;
2. inspect `AGENTS.md`, `docs/CURRENT_STATUS.md`, `docs/tasks/README.md` and the live tree;
3. record current `origin/main`;
4. verify no unrelated active task/work is being overwritten;
5. preserve prior failed/inconclusive E2E artifacts rather than rewriting them.

### PEC system under test

Do not edit the Owner's existing PEC development worktree in place. Use a fresh disposable worktree/clone from the selected PEC SUT commit whenever practical.

If a defect is found:

1. preserve the failing run first;
2. create/use a dedicated repair branch/worktree;
3. implement the minimum causal repair;
4. run focused and relevant regression tests;
5. restart only the isolated test runtime;
6. start a fresh counted run.

The final report must distinguish the pristine baseline commit from any repair branch/head.

---

## 5. Counted-run anti-cheating rules

A run is **not countable as PASS** if any of these occur:

- the AVO copies Executor semantic output into the Planner conversation;
- the AVO copies Planner semantic output into Executor input;
- the AVO directly creates the inner active task/binding merely because the product failed to do so;
- the AVO directly edits the counted workload instead of the authorized inner Executor;
- the AVO suppresses/ignores a failed handoff and pretends the downstream state was automatic;
- an ambiguous semantic send is replayed.

The AVO may inspect and record mechanical evidence, including visible UI state, bounded local API fields, Git refs, file diffs, issue/PR metadata, process/session/turn IDs and typed operational events.

If an automatic path is broken, repair the product/harness and repeat with a fresh counted run.

---

## 6. E1 — Executor-first counted run

### 6.1 Goal

Prove that PEC can begin with a natural-language requirement delivered to Executor when no executable PECTEST task exists, fail closed on missing durable authority, automatically involve Planner, establish durable authority, return to Executor, execute, review, merge, close out and terminate.

### 6.2 E1 workload

Desired repository result:

- root file `e2e-executor-first.txt`;
- exact bytes `PECTEST_EXECUTOR_FIRST_E2E_OK\n`;
- a Python standard-library `unittest` that asserts those exact bytes;
- a short validation report under the repository's current report convention.

The inner Planner chooses the next normal PECTEST task identifier and normal task/report filenames. The outer plan intentionally does **not** pre-create an active task.

### 6.3 Exact E1 initial semantic request

Use the product's canonical **Executor-first** Project/initial-prompt entry point and submit this requirement to the inner Executor:

```text
PECTEST autonomous E2E workload E1 — Executor-first.

Desired repository outcome:
1. add root e2e-executor-first.txt with exact bytes:
   PECTEST_EXECUTOR_FIRST_E2E_OK\n
2. add a Python standard-library unittest asserting those exact bytes;
3. add the normal short validation report required by the durable task.

PECTEST GitHub is durable project authority and PEC is transport/orchestration only.
Before editing, inspect AGENTS.md, docs/CURRENT_STATUS.md, docs/tasks/README.md and live GitHub state.
If there is no merged active task and exact execution binding authorizing this workload, DO NOT edit or invent authority. Use the normal PEC handoff to request Planner to establish the required Issue / merged frozen task / exact binding, then continue only after durable authorization arrives.

Once authorized, execute the exact task, test, commit and push, return a compact receipt, and let Planner independently review/merge/close out. Do not ask the Owner for ordinary decisions.
```

Do not augment this with hidden task coordinates. Missing authority at E1 start is intentional.

### 6.4 Required E1 lifecycle evidence

A counted E1 PASS must mechanically demonstrate:

1. initial Executor receives the E1 requirement;
2. Executor does not modify PECTEST before durable authority exists;
3. PEC automatically gets the requirement/need to Planner;
4. Planner creates or updates the normal inner PECTEST Issue;
5. Planner merges a versioned active task through a normal planning PR;
6. Planner creates a dedicated execution branch at exact Start and durably records Repository / Branch / Start / Task / Task-blob;
7. PEC automatically returns a valid execution authorization to Executor;
8. Executor uses the exact bound branch/task and produces the required workload/tests/report;
9. Planner independently reviews remote evidence and returns `ACCEPT`, or `REWORK` followed by successful same-contract correction;
10. Planner merges accepted execution through a normal execution PR;
11. Planner performs a separate closeout PR, archiving the frozen task unchanged and updating status;
12. the inner Issue is closed only after durable closeout;
13. PEC reaches the correct terminal/no-further-action state;
14. no Owner/manual semantic relay occurred.

A Planner `REPLAN` is allowed only if mechanically justified; the AVO should let the real lifecycle proceed and count the final fresh/valid path.

---

## 7. P1 — Planner-first counted run

### 7.1 Start condition

Start P1 automatically after E1 has reached one of these terminal phase results:

- `PASS_BASELINE_PHASE`;
- `PASS_REPAIRED_PHASE`.

Do not ask the Owner whether to continue.

Use a fresh independent PEC Project/run and distinct workload artifacts.

### 7.2 P1 workload

Desired repository result:

- root file `e2e-planner-first.txt`;
- exact bytes `PECTEST_PLANNER_FIRST_E2E_OK\n`;
- Python standard-library `unittest` asserting exact bytes;
- normal short validation report.

### 7.3 Exact P1 initial semantic request

Use the PEC product's canonical **Planner-first** entry point. Do not bypass the product by manually using the Planner chat if PEC itself provides a Planner-first Project/start path.

Submit this initial requirement to Planner:

```text
PECTEST autonomous E2E workload P1 — Planner-first.

Please own the full PECTEST durable lifecycle for this requested change:
1. add root e2e-planner-first.txt with exact bytes:
   PECTEST_PLANNER_FIRST_E2E_OK\n
2. require a Python standard-library unittest asserting those exact bytes;
3. require the normal short validation report.

Fresh-check live PECTEST GitHub. Establish the normal Issue / merged frozen active task / dedicated execution branch / exact Repository-Branch-Start-Task-Task-blob binding before Executor edits anything. Then dispatch Executor through PEC, independently review its remote result, use REWORK/REPLAN if truly required, merge accepted execution, perform a separate closeout, close the workload Issue, and reach TERMINAL.

Do not ask the Owner for ordinary implementation or lifecycle decisions.
```

If no canonical Planner-first product entry point exists or it cannot be exercised without manual semantic bypass, classify that fact mechanically. Do not fake Planner-first PASS by typing directly into an unrelated chat path and manually relaying the result.

### 7.4 Required P1 evidence

A counted P1 PASS must prove:

1. Planner receives the initial P1 requirement through the product's canonical Planner-first path;
2. Planner establishes durable PECTEST authority before Executor edits;
3. PEC automatically dispatches the exact authorized work to Executor;
4. Executor executes/tests/commits/pushes only on the bound branch;
5. Planner independently reviews and accepts/reworks appropriately;
6. execution merge + separate closeout + inner Issue closure occur in correct order;
7. terminal/no-further-action state is reached;
8. no Owner/manual semantic relay occurred.

---

## 8. Autonomous failure and repair loop

The AVO must not stop at the first ordinary failure.

For every unexpected state:

### Step A — preserve the scene

Before restart/delete/recreate/retry, capture as available:

- screenshot of the relevant Owner Console/browser state;
- current local `/api/v1/status` and `/api/v1/projects` or equivalent bounded read state;
- active Project ID/name and lifecycle;
- Executor process/session/turn mechanical coordinates;
- Planner delivery/ack/recovery/ambiguity mechanical fields;
- relevant stdout/stderr/log tail;
- PECTEST `git status`, HEAD, `origin/main`, relevant branch refs;
- relevant GitHub Issue/PR/task state.

Do not capture hidden reasoning, Planner Output or unrelated conversation content as a production input.

### Step B — classify

Classify at least:

- test setup/operator error;
- local runtime/process issue;
- browser/extension/native messaging issue;
- PEC transport/orchestration defect;
- Planner delivery/recovery defect;
- Executor app-server/session defect;
- Owner Console projection/UI defect;
- PECTEST lifecycle/Planner decision defect;
- external auth/account/platform blocker.

### Step C — repair or safely retry

For setup/harness mistakes, correct them and run fresh.

For a mechanically proven PEC product defect, use an isolated repair branch/worktree, implement the minimum fix, test it, restart the isolated runtime and start a fresh counted run. Preserve the failing attempt as evidence.

For transient operations, retry only when the previous attempt is mechanically proven not to have semantically sent/committed the action.

### Step D — strict no-replay ambiguity

If a Planner or Executor semantic send/Enter is `possible`, ambiguous or not mechanically provable as unsent, **do not replay it**. Preserve the run as inconclusive and move to a fresh run/project after safe isolation/cleanup.

### Step E — bounded repair attempts

Continue autonomously while new evidence yields a concrete repair hypothesis. Avoid infinite loops. If repeated fixes produce no new information, return `FAIL_UNRESOLVED` with the strongest preserved evidence.

---

## 9. Failed/inconclusive inner artifacts

Do not erase evidence to obtain a clean-looking pass.

When a failed/inconclusive run created inner PECTEST Issues/PRs/tasks:

- preserve commits/PR discussions;
- close abandoned Issues/PRs with an explicit E2E aborted/inconclusive explanation when doing so is safe and does not rewrite history;
- if an active task was durably created and must be retired, use an explicit normal cleanup/retirement change rather than deleting its history;
- never reuse an ambiguous semantic request ID/run as if it were fresh;
- use a new unique PEC Project/run for the next counted attempt.

---

## 10. Outcome model

### Phase outcome

Each E1/P1 phase reports one of:

- `PASS_BASELINE_PHASE` — fresh counted run passed on pristine selected PEC baseline;
- `PASS_REPAIRED_PHASE` — fresh counted rerun passed after an autonomous isolated PEC repair;
- `FAIL_UNRESOLVED_PHASE`;
- `BLOCKED_EXTERNAL_PHASE`.

### Overall outcome

- `PASS_BASELINE` — E1 and P1 both passed without PEC source repairs.
- `PASS_REPAIRED` — both phases passed, but at least one required an isolated PEC product repair.
- `FAIL_UNRESOLVED` — an in-scope failure remains unresolved.
- `BLOCKED_EXTERNAL` — a concrete external/auth/platform condition prevents completion.

Do not call `PASS_BASELINE` if source/harness behavior affecting the counted path was repaired first.

---

## 11. Required final report

The AVO must produce a final durable/bounded report for Issue #54. It may first maintain detailed local evidence and then publish a concise report/comment that contains no secrets or private chat content.

For **E1** and **P1** separately record:

- selected PEC SUT baseline commit;
- any repair branch and repair head;
- fresh counted Project/run identity;
- inner PECTEST Issue;
- planning PR;
- binding PR and exact execution branch / Start / task path / Task-blob;
- Executor final head/report and test summary;
- Planner review disposition;
- execution PR/merge;
- closeout PR/merge;
- completed task blob/archive check;
- workload Issue closure;
- terminal PEC state;
- any ambiguous-send event;
- manual semantic relay: must be `NO` for counted PASS;
- defect(s) found and repair(s) attempted;
- focused/regression tests for repairs;
- evidence paths or bounded mechanical summaries;
- residual risks.

The report must explicitly distinguish:

- **product passed on baseline**;
- **product passed only after repair**;
- **test harness problem**;
- **external blocker**.

---

## 12. AVO completion rule

Do not request Owner confirmation between E1 and P1 or during ordinary debugging.

Stop only when one of the overall outcomes is mechanically established. Return a compact final summary with the durable Issue/PR/commit coordinates and, for `PASS_REPAIRED`, the isolated PEC repair branch/head that made the fresh counted run pass.
