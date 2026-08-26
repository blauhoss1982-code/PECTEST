# Current Status

## Project authority

PECTEST GitHub is the durable project authority. PEC C1 is transport only.

## Active validation

- Task ID: `PECTEST-003`
- Issue: `#14`
- Planning baseline: `8d31ceb43e8ff5703c6433140274671003438320`
- Planning authority PR: `#15` (merged)
- Active task: `docs/tasks/active/PECTEST-003-pec-validation.md`
- Task-blob: `17aace65f4811ecc70713ffef48e7eab901e2d2f`
- State: Checkpoint A authorized for dispatch only after the exact execution binding below is independently reverified.

## Exact execution binding

- Repository: `blauhoss1982-code/PECTEST`
- Branch: `executor/PECTEST-003-pec-validation`
- Start: `6cbdc07304cc53e4f210e5540c4baf21209a1620`
- Task: `docs/tasks/active/PECTEST-003-pec-validation.md`
- Task-blob: `17aace65f4811ecc70713ffef48e7eab901e2d2f`

The execution branch was created exactly from Start after the active task was merged. Executor must use this binding unchanged. The initial PEC `CONTINUE` authorizes Checkpoint A only. Checkpoint B is forbidden until Planner independently accepts Checkpoint A and sends a later PEC `CONTINUE` for this same binding.
