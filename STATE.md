# ARTGEN Factory — State

- **Status:** active — hardening + cross-checks done
- **Last updated:** 2026-11-25
- **Current task:** none
- **AGENT default model:** `opencode/deepseek-v4.1-flash-free` (free, verified)
- **Verified paths:**
  - agent self-commit + push (`a779133`)
  - workflow fallback commit + push (`965c26f`, `1093fd4`)
  - free-model capability (`apps/free_model_check/note.txt`)
  - form trigger end-to-end: valid submit `DISPATCHED`, wrong PIN `UNAUTHORIZED_FORM`
  - webhook `doPost`: row + Drive log doc created (`notify-path-test`, row 10)
  - hardening: `concurrency` + always-run AGENT commit step (`262804d`)
- **Known gaps:**
  - Task/Calendar/Mail delivery not independently verified (try/catch hides errors).
  - `Runs_Log` timestamps appear ~8h behind GitHub UTC (check spreadsheet timezone).
- **Next step:** none
