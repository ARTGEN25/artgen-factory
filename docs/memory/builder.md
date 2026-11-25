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
- (none yet)
