# Planner Memory

Concise bullet-point memory for planning. Append, do not rewrite history.

## Goals
- Keep runs small, cheap, and restartable (`STATE.md` is the source of truth).

## Decisions
- **2026-11-25** — Repo initialized with docs-first structure (`STATE.md`, `docs/INDEX.md`, specs, memory).
- **2026-11-25** — Default AGENT model: `opencode/deepseek-v4.1-flash-free` (free, verified end-to-end); `google/gemini-3.5-flash-lite` as fallback (free tier ~15 RPM).
- **2026-11-25** — Node 24 native actions only: `actions/checkout@v7` + `actions/setup-python@v7`.
- **2026-11-25** — Keep `STATE.md` + `docs/INDEX.md` as the only entrypoint; update them every task so phone/headless runs stay restartable.

## Open Questions
- Fix `Runs_Log` timestamps (spreadsheet timezone is PST; should be Asia/Kolkata).
- Migrate legacy 4-column rows into `Runs_Log` or archive the old tab.
- Tighten GitHub token to fine-grained `Actions: write` on `artgen-factory` only.

## Next
- Add `action=health` (property presence only, never values).
- Add retry/backoff around OpenCode runs.
