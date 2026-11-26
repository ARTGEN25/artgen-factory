# ARTGEN Factory — Agent Rules

## Workflow
1. Always run `git pull --rebase` before starting work.
2. Read ONLY `STATE.md` and `docs/INDEX.md` first. Then open only the matching spec/memory file.
3. Update `STATE.md` (and the relevant memory/spec file) and push after every task.

## Housekeeping
- After EVERY change: update `STATE.md` and `docs/INDEX.md`, then commit and push.
- `STATE.md` = what is true now; `docs/INDEX.md` = where to look next. Keep both short.

## Safety
- Keep Cloud Shell light: no heavy builds or large installs in `$HOME`.
- Never touch or print secrets (`.env`, keys, tokens, Script Properties); use GitHub secrets only.

## Execution
- Headless runs: max 3 fix attempts, then stop and report the blocker.
- Always use `actions/checkout@v7` and `actions/setup-python@v7` (Node 24 native).
