# PECTEST-010 — E1 executor-first counted workload

## Status

Active after this file is merged to `main`. This task is executable only after Planner has also durably recorded and independently re-verified the exact execution binding for this unchanged task blob.

## Project authority

- Repository: `blauhoss1982-code/PECTEST`
- PECTEST Issue: `#56`
- Outer validation Issue: `#54`
- Durable task path: `docs/tasks/active/PECTEST-010-e1-executor-first.md`
- PECTEST GitHub is the durable project authority.
- PEC C1 is transport only. PEC metadata or chat text never substitutes for this merged task and its exact execution binding.

## Objective

Complete the E1 Executor-first counted workload by creating repository-root `e2e-executor-first.txt` with exact bytes:

`b"PECTEST_EXECUTOR_FIRST_E2E_OK\n"`

Also add one Python standard-library unittest that asserts those exact bytes and a short validation report recording the required execution evidence.

## Execution binding requirement

Before the Executor may change any file, Planner must:

1. merge this exact task to `main` through a planning PR;
2. create the dedicated execution branch at that planning merge commit;
3. durably record all five exact coordinates through a separate Planner-owned change:
   - Repository
   - Branch
   - Start
   - Task
   - Task-blob
4. independently re-read the remote branch and frozen task blob.

The Task-blob is the blob SHA of this exact merged file and freezes the executable contract. Executor must fail closed if any coordinate is absent or does not match remote repository state.

## Authorized implementation

Once the exact binding above is durably established and Planner issues PEC `CONTINUE` for that binding, perform only these changes on the bound execution branch:

1. Create repository-root `e2e-executor-first.txt` with exact bytes `b"PECTEST_EXECUTOR_FIRST_E2E_OK\n"`.
2. Create `tests/test_e2e_executor_first.py` using only the Python standard library. It must assert the exact bytes of repository-root `e2e-executor-first.txt`.
3. Create `docs/reports/PECTEST-010-e1-executor-first-validation.md` recording:
   - Task ID `PECTEST-010`;
   - Repository / Branch / Start / Task / Task-blob used;
   - exact expected bytes;
   - exact unittest command below;
   - exact standalone byte-verification command below;
   - PASS/FAIL for both commands;
   - final pushed execution HEAD.

Do not modify this active task or Planner-owned lifecycle records.

## Required verification

Run exactly:

```bash
python -m unittest discover -s tests -p 'test_*.py'
python -c "from pathlib import Path; p=Path('e2e-executor-first.txt'); assert p.read_bytes() == b'PECTEST_EXECUTOR_FIRST_E2E_OK\n', p.read_bytes()"
```

Before committing, remove generated transient artifacts such as `__pycache__` if any are untracked.

Then commit the bounded implementation on the exact execution branch, push it to origin, return a compact Executor receipt containing Task ID, branch, pushed HEAD SHA, report path, and PASS/FAIL for both commands, and stop for Planner review.

## Planner acceptance criteria

Planner may accept only after independently verifying from remote GitHub:

- unchanged Repository / Branch / Start / Task / Task-blob binding;
- execution branch descends from exact Start;
- `e2e-executor-first.txt` has exact bytes `b"PECTEST_EXECUTOR_FIRST_E2E_OK\n"`;
- `tests/test_e2e_executor_first.py` uses only Python standard library and asserts exact bytes;
- `docs/reports/PECTEST-010-e1-executor-first-validation.md` exists and truthfully records required evidence;
- branch diff is limited to the three task-required implementation/evidence files;
- required verification and available remote status evidence are consistent with PASS.

Executor PASS is evidence only and never constitutes Planner acceptance.

## Completion lifecycle

After acceptance, Planner owns all remaining actions:

1. open/review/merge the normal execution PR to `main`;
2. create a separate closeout branch/PR;
3. move this active task unchanged to `docs/tasks/completed/PECTEST-010-e1-executor-first.md` so the completed blob remains identical to the frozen Task-blob;
4. remove the active task path;
5. update `docs/CURRENT_STATUS.md` with accepted execution and closeout evidence and E1 terminal state;
6. merge the closeout PR;
7. close PECTEST Issue #56;
8. only after all durable lifecycle actions are complete may Planner select PEC `TERMINAL` for this inner task.
