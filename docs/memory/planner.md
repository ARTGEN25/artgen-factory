# Planner Memory

Concise bullets only. Keep this file <= 35 lines.

## Inputs
- Specs live in `docs/specs/` (legacy imports may use `01_PLANS_DOCS/`).
- Keep prompts under 55,000 chars (Apps Script/DocumentApp trim limit).

## Defaults
- Default to HOLD unless the task is explicitly tagged `[AUTO]`.
- Every code change must include pytest tests before it is considered done.

## Flow
- Read `STATE.md` + `docs/INDEX.md` first, then only the matching spec/memory file.
- Update `STATE.md` after every task and push.

## Next
- Phase 2/3 Orchestrator v3 integration.
