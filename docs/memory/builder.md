# Builder Memory

Concise bullet-point memory for implementation. Append, do not rewrite history.

## Environment
- GitHub Actions `ubuntu-latest`, Python 3.12, actions `@v7` (Node 24 native).
- Cloud Shell is control room only — no heavy builds here.

## Implemented
- **2026-11-25** — `.github/workflows/runner.yml` with `CMD` and `AGENT` modes + always-on webhook report.

## Gotchas
- Never interpolate user payload into `run:` directly; pass it via `env:`.
- Commit/push in `AGENT` mode only when `git status --porcelain` is non-empty.
- Never print `APPS_SCRIPT_URL` / `APPS_SCRIPT_TOKEN` / `GEMINI_API_KEY`.

## Run Outcomes
- **2026-11-25** — `45639839600`: AGENT + gemini, agent self-commit/push ✅, pytest 2 passed, webhook 200.
- **2026-11-25** — `45642221498`: fallback commit path ✅ (`artgen-bot: fallback-path-test`), webhook 200.
- **2026-11-25** — `45642426120`: free model `opencode/deepseek-v4.1-flash-free` ✅, fallback commit, webhook 200.
