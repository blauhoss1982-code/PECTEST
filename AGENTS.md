# PECTEST Collaboration Authority

`blauhoss1982-code/PECTEST` is the durable source of truth for PECTEST project state, task contracts, execution evidence, and lifecycle decisions. Chat is coordination context. The PEC repository and its C1 register are transport only and never replace PECTEST project authority.

## Roles

- Planner / Owner-side coordinator owns project interpretation, Issues, planning branches and PRs, task contracts, exact execution binding, independent review, ACCEPT / REWORK / REPLAN decisions, execution merge, closeout, and selection of the next action.
- Executor implements only a merged active task on the exact bound execution branch. Executor tests, commits, pushes, and returns a compact receipt. Executor PASS is evidence, not acceptance.

## Durable task lifecycle

1. Detailed executable requirements live in a versioned file under `docs/tasks/active/` and must be merged to `main` through a normal planning PR before execution starts.
2. Before dispatch, Planner records an exact binding consisting of Repository / Branch / Start / Task / Task-blob.
3. Once bound, the Executor must use those coordinates and must not substitute chat text, PEC transport metadata, another repository, another branch, or another task revision.
4. Ordinary implementation defects stay on the same task and execution branch as REWORK. A product or contract direction change requires REPLAN.
5. Planner independently reads the remote branch, diff, required files, reports, and tests before ACCEPT.
6. Completed implementation is merged through an execution PR.
7. Closeout is a separate planning PR. It moves the active task unchanged to `docs/tasks/completed/`, updates `docs/CURRENT_STATUS.md`, and records lifecycle completion before the related PECTEST Issue is closed.

## PEC transport boundary

PEC C1 carries only explicit `CONTINUE` or `TERMINAL` transport dispositions. A PEC authority such as `issues/387` identifies transport authority in the PEC repository; it is not the PECTEST task authority. Detailed implementation instructions must not be duplicated into the PEC register.

For a checkpointed task, a later checkpoint is forbidden until Planner independently accepts the prior checkpoint and then sends a new PEC `CONTINUE` for the same durable PECTEST binding. `TERMINAL` is permitted only after all required PECTEST lifecycle actions are durably complete.
