# Current Status

## Project authority

PECTEST GitHub is the durable project authority. PEC C1 is transport only.

## Active validation

- Task ID: `PECTEST-007`
- PECTEST Issue: `#37`
- Neutral planning baseline: `565fdea699b10def2914cac82a7e370585b6ad0c`
- Planning branch: `planner/PECTEST-007-establish-authority`
- Active task: `docs/tasks/active/PECTEST-007-pec-validation.md`

State: planning authority and active validation contract are being established from the neutral README-only baseline. Execution is forbidden until the active task is merged to `main`, a dedicated execution branch is created at the merged Start, and Planner durably records the exact Repository / Branch / Start / Task / Task-blob binding.

Checkpoint A is the only checkpoint that may be authorized by the initial PEC `CONTINUE`. Checkpoint B remains forbidden until independent Planner review accepts Checkpoint A and a later `CONTINUE` is sent for the unchanged binding.
