# PECTEST Collaboration Authority

`blauhoss1982-code/PECTEST` is the durable source of truth for PECTEST project state, task contracts, execution evidence, and lifecycle decisions. This Planner conversation is working context. The PEC repository and C1 register are transport only and never replace PECTEST project authority.

## Roles

- Planner / Owner-side coordinator owns project interpretation, Issues, planning branches and PRs, versioned task contracts, exact execution binding, independent review, `ACCEPT | REWORK | REPLAN`, execution PR/merge, closeout, and next-step selection.
- Executor implements only a merged active task on the exact bound execution branch. Executor tests, commits, pushes, returns a compact receipt, and stops at required review gates. Executor PASS is evidence, not Planner acceptance.

## Durable lifecycle

1. Detailed executable requirements live under `docs/tasks/active/` and must be merged to `main` through a normal planning PR before execution begins.
2. After task merge, Planner records the exact Repository / Branch / Start / Task / Task-blob binding. The Task-blob freezes the executable contract.
3. Executor must use only those durable coordinates. Chat text, PEC transport metadata, another branch, or another task revision cannot substitute for them.
4. Ordinary implementation defects stay on the same task/branch as `REWORK`. Product or contract direction changes require `REPLAN` through Planner-owned durable changes.
5. Planner independently reads remote branch state, diff, required files, report, tests, and available CI/status evidence before accepting a checkpoint or implementation.
6. Accepted implementation merges through a normal execution PR controlled by Planner.
7. Closeout is a separate planning PR that moves the active task unchanged to `docs/tasks/completed/`, updates `docs/CURRENT_STATUS.md`, and records completion before the related PECTEST Issue is closed.

## PEC transport boundary

PEC C1 carries only explicit `CONTINUE | TERMINAL` transport dispositions. PEC authority identifiers belong to the transport repository; they are not PECTEST task authority. Detailed implementation instructions stay in the merged PECTEST task.

For checkpointed work, a later checkpoint is forbidden until Planner independently accepts the prior checkpoint and then sends a new PEC `CONTINUE` for the same durable PECTEST binding. `TERMINAL` is permitted only after all required PECTEST lifecycle actions are durably complete.
