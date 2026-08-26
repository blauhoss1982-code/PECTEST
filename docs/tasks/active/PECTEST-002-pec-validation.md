# PECTEST-002 — two-checkpoint PEC collaboration validation

## Objective

Validate the production-style Planner↔Executor lifecycle with PECTEST as durable authority and PEC C1 as transport only.

Linked Issue: `#9`.

## Execution authority

This task is executable only after it is merged to `main` and the Planner records an exact binding containing all five coordinates:

- Repository
- Branch
- Start commit SHA
- Task path: `docs/tasks/active/PECTEST-002-pec-validation.md`
- Task-blob SHA for this merged file

Executor must work only on that bound repository/branch from that Start and must execute exactly this task blob. Chat or PEC register text cannot add requirements.

## Authorized implementation paths

During execution, Executor may create or modify only:

- `pec-validation.txt`
- `docs/reports/PECTEST-002-validation-report.md` (Checkpoint B only)

Do not modify this task, `AGENTS.md`, `docs/CURRENT_STATUS.md`, `docs/tasks/README.md`, README, or any other path on the execution branch.

## Checkpoint A — first-line proof

1. Create repository-root `pec-validation.txt`.
2. Its UTF-8 bytes must be exactly `PEC_VALIDATION_FIRST_OK\n` — one content line, LF newline, no BOM, no spaces, and no additional bytes.
3. Run the Checkpoint A test below.
4. Commit and push to the exact bound execution branch.
5. Return a compact receipt containing: task id, checkpoint `A`, branch, commit SHA, push status, and test result.
6. **STOP.** Do not begin Checkpoint B until the Planner independently reviews the remote evidence and PEC delivers a later `CONTINUE` for the same task/binding.

Checkpoint A required test:

```sh
python -c "from pathlib import Path; assert Path('pec-validation.txt').read_bytes() == b'PEC_VALIDATION_FIRST_OK\\n'"
```

Checkpoint A acceptance evidence is the remote branch commit/diff/file bytes read independently by Planner. Executor PASS alone is not acceptance.

## Checkpoint B — second-line proof and report

Checkpoint B is forbidden until a post-review PEC `CONTINUE` is received.

1. Preserve the first line of `pec-validation.txt` unchanged.
2. Append exactly one second content line: `PEC_VALIDATION_SECOND_OK`.
3. Final UTF-8 bytes must be exactly `PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n` — LF newlines, no BOM, no spaces, and no additional bytes.
4. Create `docs/reports/PECTEST-002-validation-report.md` containing:
   - the exact Repository / Branch / Start / Task / Task-blob binding used;
   - Checkpoint A commit SHA and its test result;
   - Checkpoint B commit SHA (or, if the report is committed together with B, the explicit note `Checkpoint B commit: this commit`) and its test result;
   - the exact final expected bytes/text for `pec-validation.txt`;
   - confirmation that only task-authorized implementation paths changed relative to Start.
5. Run all Checkpoint B tests below.
6. Commit and push to the same bound execution branch.
7. Return a compact receipt containing: task id, checkpoint `B`, branch, commit SHA, push status, both test results, and report path.
8. Stop for Planner review. Do not merge or perform closeout.

Checkpoint B required tests:

```sh
python -c "from pathlib import Path; assert Path('pec-validation.txt').read_bytes() == b'PEC_VALIDATION_FIRST_OK\\nPEC_VALIDATION_SECOND_OK\\n'"
git diff --check
```

## Planner review and decisions

For each checkpoint, Planner must independently inspect the PECTEST remote branch, compare it with the exact Start/binding, read relevant file bytes/content, and verify report/tests as applicable.

- `ACCEPT`: evidence satisfies this merged contract.
- `REWORK`: ordinary implementation/test/report defect; keep the same task and execution branch and issue compact corrective transport.
- `REPLAN`: contract/product direction must change; stop execution and revise durable planning authority through a planning PR before further work.

Acceptance of A authorizes only a later PEC `CONTINUE` for B. Acceptance of B authorizes Planner to open/review/merge the execution PR.

## Completion and closeout

After Checkpoint B is independently accepted:

1. Planner opens and normally merges the execution PR into `main`.
2. Planner uses a separate closeout planning branch/PR to move this file **unchanged** from `docs/tasks/active/` to `docs/tasks/completed/` and update `docs/CURRENT_STATUS.md` to completed/no active execution.
3. Planner merges the closeout PR and closes Issue `#9` as completed.
4. Only after those durable lifecycle actions are complete may PEC transport `TERMINAL`.

## Final required file

At completion, `pec-validation.txt` must contain exactly:

```text
PEC_VALIDATION_FIRST_OK
PEC_VALIDATION_SECOND_OK
```
