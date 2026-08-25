# PECTEST-001 — Two-checkpoint PEC collaboration validation

## Goal
Validate the real Planner↔Executor lifecycle using PECTEST as durable project authority and PEC only as transport.

## Authority
- Issue: `#1`
- This merged active task file is the executable contract.
- Executor may act only on the exact Repository / Branch / Start / Task / Task-blob binding recorded by Planner in Issue #1.
- No work may start from chat-only requirements.

## Scope
Executor performs exactly two checkpoints on one bound execution branch. Checkpoint B is forbidden until Planner independently accepts Checkpoint A and sends PEC `CONTINUE`.

## Checkpoint A
1. On the bound execution branch, create repository-root file `pec-validation.txt`.
2. Its complete bytes must be exactly:
   `PEC_VALIDATION_FIRST_OK\n`
   This means one content line, LF terminated, with no BOM, spaces, blank lines, or additional text.
3. Do not create or modify any other repository file at Checkpoint A.
4. Run the Checkpoint A test below.
5. Commit with a clear task/checkpoint message and push the bound branch.
6. Return a compact receipt containing: task, checkpoint=A, repository, branch, bound start SHA, resulting HEAD SHA, commit SHA, test result, and push result.
7. STOP. Do not begin Checkpoint B until Planner sends PEC `CONTINUE` after independent review.

### Checkpoint A required test
Run from repository root:

```bash
python -c "from pathlib import Path; assert Path('pec-validation.txt').read_bytes() == b'PEC_VALIDATION_FIRST_OK\\n'"
```

PASS requires exit code 0.

## Checkpoint B
Checkpoint B is authorized only by Planner PEC `CONTINUE` after Checkpoint A acceptance.

1. Continue on the same bound execution branch from the accepted Checkpoint A HEAD.
2. Preserve the first line unchanged and append exactly one second line so the complete bytes become:
   `PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n`
3. Create `docs/reports/PECTEST-001-validation-report.md`.
4. The report must record:
   - Repository, branch, bound Start SHA, active Task path, and bound Task blob SHA.
   - The accepted Checkpoint A HEAD SHA supplied by the existing branch history / receipt context.
   - The exact Checkpoint A and Checkpoint B test commands used and PASS results.
   - The final expected bytes of `pec-validation.txt`.
   - The files changed by the task.
5. Do not modify the active task, `AGENTS.md`, `docs/CURRENT_STATUS.md`, or unrelated files.
6. Run both required Checkpoint B tests below.
7. Commit and push the bound branch.
8. Return a compact receipt containing: task, checkpoint=B, repository, branch, bound start SHA, resulting HEAD SHA, commit SHA, both test results, report path, and push result.
9. STOP for Planner independent review.

### Checkpoint B required tests
Exact content:

```bash
python -c "from pathlib import Path; assert Path('pec-validation.txt').read_bytes() == b'PEC_VALIDATION_FIRST_OK\\nPEC_VALIDATION_SECOND_OK\\n'"
```

Report existence:

```bash
python -c "from pathlib import Path; p=Path('docs/reports/PECTEST-001-validation-report.md'); assert p.is_file() and p.read_text(encoding='utf-8').strip()"
```

Both commands must exit 0.

## Planner review contract
Planner must independently inspect remote branch state, compare against the bound Start SHA, read `pec-validation.txt`, read the report when applicable, and verify required tests/evidence before any disposition.

### Checkpoint A acceptance
- Remote branch contains exactly the intended A change relative to Start: new root `pec-validation.txt` only.
- File bytes are exactly `PEC_VALIDATION_FIRST_OK\n`.
- Required A test is evidenced as PASS.
- Branch is pushed and receipt coordinates match remote state.

If accepted, Planner sends PEC `CONTINUE` for Checkpoint B on the same task/branch. Otherwise ordinary implementation defects are `REWORK` on the same task/branch.

### Checkpoint B acceptance
- Final `pec-validation.txt` bytes are exactly `PEC_VALIDATION_FIRST_OK\nPEC_VALIDATION_SECOND_OK\n`.
- First line is unchanged from accepted A.
- `docs/reports/PECTEST-001-validation-report.md` exists and contains all required report fields.
- Both required B tests are evidenced as PASS.
- Remote diff contains only task-authorized implementation/report changes.
- Receipt coordinates match remote state.

If accepted, Planner merges the execution PR, then performs a separate closeout PR. Ordinary implementation defects remain `REWORK`; only a product/contract direction change is `REPLAN`.

## Closeout contract
After execution merge, Planner must on a separate closeout branch/PR:
1. Move this active task file unchanged to `docs/tasks/completed/PECTEST-001-pec-validation.md`.
2. Update `docs/CURRENT_STATUS.md` to record completion and no active execution.
3. Merge the closeout PR.
4. Close Issue #1 as completed.
5. Only after those durable actions, send PEC `TERMINAL`.

## Final invariant
At accepted completion, repository-root `pec-validation.txt` must be exactly two lines:

```text
PEC_VALIDATION_FIRST_OK
PEC_VALIDATION_SECOND_OK
```
