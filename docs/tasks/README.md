# Task lifecycle

Executable work is governed by versioned Markdown contracts.

## Directories

- `docs/tasks/active/`: merged tasks currently authorized for execution when paired with an exact Planner binding.
- `docs/tasks/completed/`: immutable task contracts moved here during closeout after accepted execution is merged.

## Rules

1. A task becomes executable only after its planning PR is merged to `main`.
2. Planner then records exact `Repository / Branch / Start / Task / Task-blob` coordinates. The blob SHA freezes the executable contract for that binding.
3. Executor must execute only the bound task blob on the bound branch; chat and PEC transport do not extend scope.
4. Checkpoint receipts are evidence. Planner independently verifies remote commits, diff, file bytes, report, and tests before acceptance.
5. Implementation defects use REWORK on the same task/branch. Contract or product-direction changes use REPLAN through a new planning revision.
6. After accepted execution merges, a separate closeout PR moves the active task to `completed/` without changing its contents and updates `docs/CURRENT_STATUS.md`; the linked Issue is then closed.
