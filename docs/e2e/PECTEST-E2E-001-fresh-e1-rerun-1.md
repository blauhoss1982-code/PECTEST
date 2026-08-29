# PECTEST-E2E-001 — fresh E1 rerun 1 addendum

## Purpose

This addendum defines the first fresh counted Executor-first rerun after accepted PEC Issue #595. It supplements `docs/e2e/PECTEST-E2E-001-autonomous-bidirectional-flow.md` and exists because the original E1 artifact was already created by the preserved failed transport run.

Tracking Issue: `#54`.

## Selected SUT baseline

Use PEC `main` at or after:

```text
c99ec983594d83aa7a7a51522df8874b15895271
```

This baseline includes accepted ISSUE-573 and ISSUE-595 plus Planner lifecycle status refresh. Do not use an older PEC commit for the counted rerun.

## Fresh-boundary rule

Do not reuse:

- the prior failed E1 PEC Project/run;
- prior request IDs or register sequence state as semantic authority;
- PECTEST-010 / Issue #56;
- its execution branch, frozen task, or task blob;
- the previous E1 artifact as the new counted workload.

Start with a new PEC Project/run and a clean isolated PEC runtime/worktree. PECTEST intentionally has no new merged active workload task at the beginning of the run.

## Unique E1-R1 workload

The new counted repository outcome is:

- root `e2e-executor-first-rerun-1.txt`;
- exact bytes `PECTEST_EXECUTOR_FIRST_E2E_RERUN_1_OK\n`;
- a Python standard-library `unittest` asserting those exact bytes;
- the normal short validation report required by the new inner frozen task.

`e2e-executor-first-rerun-1.txt` is absent at this authorization boundary. The inner Planner chooses the new normal PECTEST task identifier, Issue, task filename, report filename and exact execution branch.

## Exact E1-R1 initial semantic request

Use the canonical Executor-first PEC entry point and submit exactly this workload requirement to the inner Executor:

```text
PECTEST autonomous E2E fresh workload E1-R1 — Executor-first.

Desired repository outcome:
1. add root e2e-executor-first-rerun-1.txt with exact bytes:
   PECTEST_EXECUTOR_FIRST_E2E_RERUN_1_OK\n
2. add a Python standard-library unittest asserting those exact bytes;
3. add the normal short validation report required by the durable task.

PECTEST GitHub is durable project authority and PEC is transport/orchestration only.
Before editing, inspect AGENTS.md, docs/CURRENT_STATUS.md, docs/tasks/README.md and live GitHub state.
If there is no merged active task and exact execution binding authorizing this workload, DO NOT edit or invent authority. Use the normal PEC handoff to request Planner to establish a brand-new Issue / merged frozen task / exact binding, then continue only after durable authorization arrives.

Once authorized, execute the exact task, test, commit and push, return a compact receipt, and let Planner independently review, merge and separately close out. After the inner Issue is closed and no further Executor turn is authorized, Planner must select the exact TERMINAL response. Do not ask the Owner for ordinary decisions.
```

## Counted E1-R1 success

A counted PASS requires the complete automatic sequence:

```text
fresh Executor-first request
-> Executor detects missing durable authority and makes no workload edit
-> automatic Planner handoff
-> brand-new inner Issue
-> merged frozen task
-> exact execution Start/branch/task-blob binding
-> automatic Executor authorization
-> Executor implementation/test/commit/push
-> independent Planner review
-> execution merge
-> separate closeout
-> frozen task archived unchanged
-> inner Issue closed
-> Planner selects same-request TERMINAL
-> zero post-closeout no-op Executor progression
```

Manual semantic relay/copy-paste must remain `NO`. Possible-send / possible-Enter ambiguity remains strict no-replay.

## P1 continuation

If and only if E1-R1 reaches explicit TERMINAL, the Autonomous Validation Operator immediately begins a fresh independent P1 Planner-first run using the original P1 workload from the main validation plan (`e2e-planner-first.txt` / `PECTEST_PLANNER_FIRST_E2E_OK\n`) unless live PECTEST shows that artifact already exists, in which case the operator must stop before starting P1 and obtain a new durable P1 addendum rather than accidentally testing a no-op workload.

## Failure handling

Follow the main validation plan. Before restart/delete/recreate/retry, preserve bounded live evidence including local status/project APIs, Project identity, register/request coordinates, send certainty, process/source HEAD, relevant logs, and GitHub durable state. A mechanically proven product defect may be repaired only in an isolated PEC repair branch/worktree, followed by a completely fresh counted run.
