# Task Lifecycle

PECTEST task contracts are durable, versioned project authority.

- `docs/tasks/active/` contains merged executable tasks that may be bound to execution branches.
- `docs/tasks/completed/` contains closed tasks moved from active without changing their contents.
- A task must be merged before an execution binding is created.
- The binding records Repository / Branch / Start / Task / Task-blob. The Task-blob freezes the executable contract used by the Executor.
- After binding, ordinary implementation fixes are REWORK on the same task and branch. Contract changes require REPLAN and a new reviewed planning change before further execution.
- Executor receipts are compact evidence only. Planner independently reviews remote state before accepting a checkpoint or merging implementation.
- Closeout is performed separately from implementation and archives the active task unchanged.
