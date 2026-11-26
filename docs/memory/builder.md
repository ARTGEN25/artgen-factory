# Builder Memory

Concise bullets only. Keep this file <= 35 lines.

## Implemented
- **2026-11-25** — `apps/sys_digest/`: JSON status digest to Markdown; CLI via stdin/file; 4 pytest tests passing.
- **2026-11-25** — `runner.yml`: CMD + AGENT modes, always-on webhook report, concurrency + always-run commit.
- **2026-11-26** — Re-verified `apps/sys_digest/` digest + CLI unchanged; 2 pytest tests passing (run in `/tmp/opencode/venv`).

## CI
- Always use `actions/checkout@v7` + `actions/setup-python@v7` (Node 24 native).
- Set `git config user.name/user.email` BEFORE a headless `opencode run`; `--auto` may commit itself.

## Apps Script
- `/exec` POST returns a 302 redirect; follow redirects, never force POST on the redirect target.
- Validate the token server-side; never log secrets.

## Models
- Prefer `google/gemini-3.5-flash-lite` to protect the 15 RPM free-tier quota.
- Free fallback: `opencode/deepseek-v4.1-flash-free` (verified end-to-end).

## Hygiene
- Update `STATE.md` after every task; commit and push `main`.
- Never commit secrets; use GitHub secrets only.
