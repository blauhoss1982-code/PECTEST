# PECTEST collaboration authority

PECTEST GitHub is the durable source of truth for this repository. Chat is for Planner reasoning/review, and PEC C1 is transport only.

## Roles

- **Planner / Owner-side coordinator** owns project understanding, Issues, planning branches/PRs, merged task contracts, exact execution binding, independent review, ACCEPT/REWORK/REPLAN decisions, execution merge, closeout, and next-step selection.
- **Executor** works only from a merged active task plus the exact Repository / Branch / Start / Task / Task-blob binding recorded by the Planner. Executor must not infer authority from chat or from PEC register contents.

## Execution rules

1. Detailed executable requirements live in a merged file under `docs/tasks/active/`.
2. A dedicated execution branch is bound to one exact Start commit and one exact task blob before dispatch.
3. Executor changes only paths authorized by the active task, runs its required tests, commits, pushes, and returns a compact receipt.
4. A checkpoint stop is mandatory. A later checkpoint may begin only after Planner independently reviews remote evidence and PEC transports a new `CONTINUE`.
5. Executor-reported PASS is evidence, never acceptance. Planner independently reads the remote branch/diff/files/report/tests before deciding.
6. Ordinary implementation defects remain on the same task/branch as `REWORK`. A product or contract direction change requires `REPLAN` and a new durable task revision through planning review.
7. Accepted execution is merged by normal PR. Closeout is a separate planning PR that archives the active task unchanged, updates durable status, and is followed by Issue closure. Only then may PEC transport `TERMINAL`.

## PEC boundary

PEC register mutations carry only explicit `CONTINUE` or `TERMINAL` transport disposition and correlation coordinates. They are not PECTEST project facts and never replace repository task/status/Issue evidence.
