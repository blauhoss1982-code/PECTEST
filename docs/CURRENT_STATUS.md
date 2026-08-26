# Current Status

## Project authority

PECTEST GitHub is the durable project authority. PEC C1 is transport only.

## PECTEST-008 lifecycle

- Task ID: `PECTEST-008`
- PECTEST Issue: `#41`
- Neutral planning baseline: `833f98d5dafb160bdb0239768c4068acd407a896`
- Planning authority branch: `planner/PECTEST-008-establish-authority`
- Active task candidate: `docs/tasks/active/PECTEST-008-pec-validation.md`

State: planning authority and executable active task are being established through a normal planning PR. Execution is forbidden until the active task is merged to `main`, the dedicated execution branch is created at the exact merged Start, and Planner durably records and independently verifies the exact Repository / Branch / Start / Task / Task-blob binding.

The initial PEC `CONTINUE` may authorize Checkpoint A only after that binding is fully established. Checkpoint B remains forbidden until Planner independently reviews and accepts Checkpoint A and a later PEC `CONTINUE` is sent for the unchanged binding.
