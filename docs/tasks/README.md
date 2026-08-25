# Task Lifecycle

## Directories
- `docs/tasks/active/`: merged executable task contracts currently authorized for execution.
- `docs/tasks/completed/`: accepted tasks moved here unchanged during a separate closeout PR.

## Rules
1. A task becomes executable only after its active task file is merged to `main`.
2. Planner creates an Issue for lifecycle tracking and records exact execution binding there after merge.
3. Executor works only on the bound branch and only to the merged task contract.
4. Planner independently reviews remote repository evidence before deciding ACCEPT, REWORK, or REPLAN.
5. REWORK keeps the same task and branch when the contract is still correct.
6. REPLAN is required when product intent or the task contract must change; durable planning changes are merged before execution resumes.
7. Accepted execution is merged normally.
8. Closeout is a separate PR: move the active task byte-for-byte to completed, update `docs/CURRENT_STATUS.md`, merge, then close the Issue.
9. PEC `TERMINAL` is sent only after the durable closeout lifecycle is complete.
