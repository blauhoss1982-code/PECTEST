# PECTEST Collaboration Authority

## Durable authority
PECTEST GitHub repository state is the durable source of truth for this project. Chat is Planner working context. The PEC register is transport only and must not be treated as PECTEST project authority.

## Roles
- Planner / Owner-side coordinator: understands the project, creates Issues, plans and merges planning PRs, authors versioned active task contracts, establishes exact execution bindings, independently reviews remote evidence, decides ACCEPT / REWORK / REPLAN, merges execution, performs closeout, and selects next work.
- Executor: executes only the merged active task on the exact bound execution branch, runs required tests, commits, pushes, and returns compact receipts. Executor PASS is evidence, never acceptance.

## Task authority
Detailed executable requirements live in `docs/tasks/active/` and must be merged to `main` before execution starts. Executor instructions through PEC remain compact and point to durable repository coordinates.

## Execution binding
Before Executor starts, Planner must record an exact binding containing Repository, Branch, Start commit, Task path, and Task blob SHA in the task Issue. The task blob SHA is recorded outside the task file because a blob cannot contain its own SHA without becoming a different blob.

## Review and lifecycle
- Planner independently reads the remote execution branch, diff, required report, and tests before any disposition.
- Ordinary implementation defects stay on the same task and execution branch as REWORK.
- Product or contract direction changes require REPLAN through durable planning changes.
- Execution merge happens only after task acceptance.
- Closeout uses a separate PR that moves the active task unchanged to `docs/tasks/completed/`, updates `docs/CURRENT_STATUS.md`, and is merged before the Issue is closed and PEC TERMINAL is sent.

## PEC transport
Use PEC only for explicit `CONTINUE` or `TERMINAL` transport dispositions. Routine relay, correlation, retry, and approval work belongs to the Planner/Executor workflow and must not be delegated to the Owner.
