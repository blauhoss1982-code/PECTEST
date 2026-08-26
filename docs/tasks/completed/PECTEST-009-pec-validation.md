# PECTEST-009 — Two-checkpoint PEC collaboration validation

## Status

Active after this file is merged to `main`. This task is executable only when Planner has also durably recorded an exact execution binding for this unchanged task blob.

## Project authority

- Repository: `blauhoss1982-code/PECTEST`
- PECTEST Issue: `#47`
- Durable task path: `docs/tasks/active/PECTEST-009-pec-validation.md`
- PECTEST GitHub is the durable project authority.
- PEC C1 is transport only and may carry only the Planner-selected `CONTINUE | TERMINAL` disposition. PEC metadata is never a substitute for this task or the exact PECTEST execution binding.

## Objective

Validate one real Planner↔Executor lifecycle using two gated checkpoints on one frozen task and one dedicated execution branch. The final repository-root file must be exactly:

```text
PEC_VALIDATION_FIRST_OK
PEC_VALIDATION_SECOND_OK
```

The final bytes must be exactly `b"PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n"`.

## Execution binding requirement

Before the Executor may change any file, Planner must merge this task to `main`, create a dedicated execution branch at the resulting merged task commit, and durably record all five exact coordinates:

- Repository
- Branch
- Start
- Task
- Task-blob

The Task-blob is the blob SHA of this exact merged file and freezes the executable contract. Executor must fail closed if any coordinate is missing or does not match the remote repository state.

## General executor rules

1. Work only in the bound repository and bound execution branch, beginning from the exact bound Start.
2. Do not modify this active task.
3. Do not modify Planner-owned lifecycle records except files explicitly required below.
4. Ordinary implementation mistakes remain on this same task/branch as `REWORK`; do not create a new branch or reinterpret the contract.
5. A compact Executor receipt is evidence only. Planner independently reviews remote branch state, diff, required files, report, tests, and status before any acceptance decision.
6. Stop at every Planner gate. Never infer authorization for a later checkpoint from this task alone.

## Checkpoint A — first-line creation

Authorization: the initial PEC `CONTINUE` for the exact binding authorizes Checkpoint A only.

Required change:

- Create repository-root `pec-validation.txt`.
- Its bytes must be exactly `b"PEC_VALIDATION_FIRST_OK\n"`.
- It must contain one line only: `PEC_VALIDATION_FIRST_OK`.
- Do not create the Checkpoint B report or test file yet.

Required verification before commit:

```bash
python -c "from pathlib import Path; p=Path('pec-validation.txt'); assert p.read_bytes() == b'PEC_VALIDATION_FIRST_OK\n', p.read_bytes()"
```

Then:

- commit the Checkpoint A change on the bound execution branch;
- push that branch to origin;
- return a compact receipt containing at least Task ID, checkpoint `A`, remote branch, pushed HEAD SHA, and PASS/FAIL for the required verification;
- stop and wait for Planner review.

Checkpoint B is forbidden until Planner independently reviews the remote Checkpoint A evidence, accepts it, and sends a later PEC `CONTINUE` for the same unchanged Repository / Branch / Start / Task / Task-blob binding.

## Checkpoint B — second line, test, and report

Authorization: only a later Planner-selected PEC `CONTINUE` after accepted Checkpoint A authorizes Checkpoint B.

Required changes:

1. Preserve the first line of `pec-validation.txt` unchanged and append exactly one second line `PEC_VALIDATION_SECOND_OK` with a trailing newline. Final bytes must be exactly:

   `b"PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n"`

2. Create `tests/test_pec_validation.py` using only the Python standard library. It must assert the exact final bytes of repository-root `pec-validation.txt`.

3. Create `docs/reports/PECTEST-009-validation.md`. The report must record:
   - Task ID `PECTEST-009`;
   - that Checkpoint A was completed before Checkpoint B;
   - the Checkpoint A commit SHA;
   - the final exact expected bytes;
   - the exact test command used for Checkpoint B;
   - the exact standalone byte-verification command used for Checkpoint B;
   - PASS/FAIL for both required Checkpoint B commands.

Required Checkpoint B commands:

```bash
python -m unittest discover -s tests -p 'test_*.py'
python -c "from pathlib import Path; p=Path('pec-validation.txt'); assert p.read_bytes() == b'PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n', p.read_bytes()"
```

Then:

- commit all Checkpoint B changes on the same bound execution branch;
- push that branch to origin;
- return a compact receipt containing at least Task ID, checkpoint `B`, remote branch, pushed HEAD SHA, report path, and PASS/FAIL for both required commands;
- stop and wait for Planner review.

## Planner acceptance criteria

Planner may accept Checkpoint A only after independently verifying the remote bound branch, exact `pec-validation.txt` bytes, branch ancestry from Start, diff scope, and available commit/status evidence.

Planner may accept Checkpoint B only after independently verifying all of the following from the remote repository:

- same bound Repository / Branch / Start / Task / Task-blob;
- Checkpoint A remains in branch ancestry;
- `pec-validation.txt` exact final bytes are `b"PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n"`;
- `tests/test_pec_validation.py` exists and uses only Python standard library to enforce exact bytes;
- `docs/reports/PECTEST-009-validation.md` exists and truthfully records the required evidence;
- branch diff is limited to task-required implementation/evidence changes;
- required tests/verification and available remote status evidence are consistent with PASS.

Executor PASS alone never constitutes Planner acceptance.

## Completion lifecycle

After accepted Checkpoint B, Planner owns all remaining actions:

1. Open/review/merge the normal execution PR into `main`.
2. Create a separate planning closeout branch/PR.
3. Move this active task unchanged to `docs/tasks/completed/PECTEST-009-pec-validation.md` so the completed blob remains identical to the frozen Task-blob.
4. Remove the active task path.
5. Update `docs/CURRENT_STATUS.md` with accepted execution and closeout evidence.
6. Merge the closeout PR.
7. Close PECTEST Issue #47.
8. Only after those durable lifecycle actions are complete may Planner return PEC `TERMINAL`.
