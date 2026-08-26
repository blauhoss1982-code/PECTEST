# PECTEST-003 — Two-checkpoint PEC Collaboration Validation

## Identity

- Task ID: `PECTEST-003`
- PECTEST Issue: `#14`
- Status: active
- Project authority: `blauhoss1982-code/PECTEST`
- Transport: PEC C1, transport only

## Objective

Validate one real Planner↔Executor lifecycle with two gated checkpoints on one exact execution binding. The final repository-root file `pec-validation.txt` must contain exactly the two required validation lines, and Checkpoint B must not begin until Planner independently accepts Checkpoint A and sends a later PEC `CONTINUE`.

## Binding rule

Execution may begin only after this task is merged to `main` and Planner records the exact binding:

- Repository
- Branch
- Start
- Task
- Task-blob

Executor must execute this exact merged Task-blob on that exact branch. Chat text and PEC register metadata do not replace or revise this contract.

## Checkpoint A — first line only

Authorization: the initial PEC `CONTINUE` for the exact binding authorizes **Checkpoint A only**.

Required change:

1. Create repository-root `pec-validation.txt` as UTF-8 without BOM using LF newline convention.
2. Its exact bytes after Checkpoint A must be:
   `PEC_VALIDATION_FIRST_OK\n`
3. Do not add the second validation line yet.
4. Do not create the Checkpoint B report or test file yet.

Required verification before commit:

`python -c "from pathlib import Path; b=Path('pec-validation.txt').read_bytes(); assert b == b'PEC_VALIDATION_FIRST_OK\\n', b; print('PASS checkpoint-a exact bytes')"`

Then commit and push the bound execution branch. Return a compact receipt containing Task ID, checkpoint `A`, branch, bound Start, resulting HEAD/commit, verification result, and push result. Stop and wait for Planner review. Executor PASS does not authorize Checkpoint B.

## Checkpoint A Planner gate

Planner independently checks the remote execution branch, commit/diff, and exact `pec-validation.txt` bytes. If implementation is defective but the contract is still correct, Planner chooses REWORK on the same task/branch. If accepted, Planner sends a new PEC `CONTINUE` for the same binding; only that later `CONTINUE` authorizes Checkpoint B.

## Checkpoint B — second line, test, report

Authorization: only a post-acceptance PEC `CONTINUE` for the same binding authorizes Checkpoint B.

Required changes:

1. Preserve the first line unchanged and append exactly one second line.
2. Final `pec-validation.txt` exact bytes must be:
   `PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n`
3. Add `tests/test_pec_validation.py` using only the Python standard library. It must read repository-root `pec-validation.txt` as bytes, fail unless the bytes exactly equal the final required bytes above, and print a concise PASS message on success.
4. Add `docs/reports/PECTEST-003-validation-report.md` containing:
   - Task ID and checkpoint `B`;
   - bound Repository / Branch / Start / Task / Task-blob coordinates supplied by the durable project state;
   - statement that Checkpoint A's first line was preserved unchanged;
   - the exact verification commands run for Checkpoint B;
   - PASS/FAIL results observed before commit.

Required verification before commit:

`python tests/test_pec_validation.py`

and

`python -c "from pathlib import Path; b=Path('pec-validation.txt').read_bytes(); assert b == b'PEC_VALIDATION_FIRST_OK\\nPEC_VALIDATION_SECOND_OK\\n', b; print('PASS checkpoint-b exact bytes')"`

Both commands must pass. Then commit and push the same bound execution branch and return a compact receipt containing Task ID, checkpoint `B`, branch, bound Start, resulting HEAD/commit, both test results, report path, and push result.

## Planner completion gate

After Checkpoint B receipt, Planner independently reviews the remote branch, diff, final file bytes, report, test source, and available test/CI evidence. If accepted:

1. merge the implementation through a normal execution PR;
2. create a separate closeout planning branch/PR;
3. move this active task **unchanged** from `docs/tasks/active/PECTEST-003-pec-validation.md` to `docs/tasks/completed/PECTEST-003-pec-validation.md`;
4. update `docs/CURRENT_STATUS.md` with completed lifecycle evidence;
5. merge the closeout PR;
6. close PECTEST Issue #14;
7. only then send PEC `TERMINAL`.

## Final invariant

At task completion, repository-root `pec-validation.txt` must be exactly:

```text
PEC_VALIDATION_FIRST_OK
PEC_VALIDATION_SECOND_OK
```

No additional lines, whitespace, BOM, or alternate line endings are permitted.
