# Current Status

## Project authority

PECTEST GitHub is the durable project authority. PEC C1 is transport only.

## Active validation

- Task ID: `PECTEST-004`
- Issue: `#20`
- Planning baseline: `738a1e6f97cb049444412579b0067196ba077f3f`
- Planning authority PR: `#21` (merged)
- Active task: `docs/tasks/active/PECTEST-004-pec-validation.md`
- Task-blob: `778debd7545e444e63979ab6cd2894447822adb1`

## Exact execution binding

- Repository: `blauhoss1982-code/PECTEST`
- Branch: `executor/PECTEST-004-pec-validation`
- Start: `92e05ffe51e09257cdc2084d7f0c43017a4ca66f`
- Task: `docs/tasks/active/PECTEST-004-pec-validation.md`
- Task-blob: `778debd7545e444e63979ab6cd2894447822adb1`

State: exact execution binding established; Checkpoint A has not yet been dispatched. Executor must execute only the merged Task-blob on the exact bound branch from Start.

Checkpoint A is the first executable checkpoint. Checkpoint B is forbidden until Planner independently accepts Checkpoint A and sends a later PEC `CONTINUE` for this same exact binding.
