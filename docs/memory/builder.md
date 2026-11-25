# Builder Memory

Concise bullet-point memory for implementation. Append, do not rewrite history.

## Environment
- GitHub Actions `ubuntu-latest`, Python 3.12, actions `@v7` (Node 24 native).
- Cloud Shell is control room only — no heavy builds here.

## Implemented
- **2026-11-25** — `.github/workflows/runner.yml` with `CMD` and `AGENT` modes + always-on webhook report.
- **2026-11-25** — Google Doc dispatch confirmed working (webhook `doPost` creates the Drive log doc).
- **2026-11-25** — `apps/sys_digest/`: `format_digest()` parses JSON status payloads into a Markdown digest; CLI via stdin or file path; 4 pytest tests passing.

## Gotchas
- Never interpolate user payload into `run:` directly; pass it via `env:`.
- Commit/push in `AGENT` mode only when `git status --porcelain` is non-empty.
- Never print `APPS_SCRIPT_URL` / `APPS_SCRIPT_TOKEN` / `GEMINI_API_KEY`.
- **Node 24 actions:** always `actions/checkout@v7` + `actions/setup-python@v7`; v4/v5 emit Node 20 deprecation warnings and annotations.
- **Git identity first in CI:** set `git config user.name/user.email` BEFORE running OpenCode. With `--auto` it may commit on its own; otherwise it fails with "Author identity unknown".
- **Apps Script redirects:** web app GETs return 302 to `script.googleusercontent.com`; use `curl -L` (or urllib, which follows redirects) or you get sign-in HTML instead of JSON.
- **Gemini free tier ~15 RPM** on `gemini-3.5-flash-lite`: bursts hit 429. Keep prompts small, add retry/backoff, or use the free DeepSeek model.
- **Keep memory current:** update `STATE.md` and `docs/INDEX.md` after every task, then commit/push; otherwise the next agent starts blind.
- Prefer an always-run `Commit AGENT changes` step (`if: always() && mode == 'AGENT'`) plus a `concurrency` group so failed agents still leave a clean, pushed tree.

## Run Outcomes
- **2026-11-25** — `45639839600`: AGENT + gemini, agent self-commit/push ✅, pytest 2 passed, webhook 200.
- **2026-11-25** — `45642221498`: fallback commit path ✅ (`artgen-bot: fallback-path-test`), webhook 200.
- **2026-11-25** — `45642426120`: free model `opencode/deepseek-v4.1-flash-free` ✅, fallback commit, webhook 200.
- **2026-11-25** — `45668112279`: hardening smoke (CMD) ✅ `HARDENING_OK`, webhook 200, 0 annotations.
- **2026-11-25** — form trigger: `form-smoke-test` DISPATCHED + success; wrong PIN → `UNAUTHORIZED_FORM` (no dispatch).
- **2026-11-25** — `notify-path-test`: doPost FAILED path ✅ row 10 + Drive log doc.
