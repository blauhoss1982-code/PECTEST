# Current Status

## Project authority

PECTEST GitHub is the durable project authority. PEC C1 is transport only.

## Active validation lifecycle

- Task ID: `PECTEST-006`
- PECTEST Issue: `#33`
- Neutral planning baseline: `8778b6ebad28a525be651d32d806cc85713b382e`
- Active task path: `docs/tasks/active/PECTEST-006-pec-validation.md`

State: planning authority and active task are being established through a normal planning PR.

Execution is **not authorized** until the active task is merged to `main`, a dedicated execution branch is created from the exact merged planning commit, and Planner durably records the exact Repository / Branch / Start / Task / Task-blob binding.

Checkpoint B is additionally forbidden until Checkpoint A has been independently reviewed and accepted by Planner and a later PEC `CONTINUE` is sent for that unchanged binding.
