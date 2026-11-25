"""Render a JSON system status payload as a readable digest."""

import json
import sys
from typing import Any, Dict, List

UNKNOWN = "unknown"


def _text(value: Any) -> str:
    """Return a non-empty display string for a scalar value."""
    if value is None:
        return UNKNOWN
    text = str(value).strip()
    return text or UNKNOWN


def _items(value: Any) -> List[str]:
    """Normalize a notes/alerts value into a list of display strings."""
    if value is None:
        return []
    if isinstance(value, dict):
        return [f"{key}: {_text(item)}" for key, item in value.items()]
    if isinstance(value, (list, tuple)):
        return [_text(item) for item in value if _text(item) != UNKNOWN]
    text = _text(value)
    return [] if text == UNKNOWN else [text]


def _first(payload: Dict[str, Any], *keys: str) -> Any:
    """Return the first present, non-empty value for the given keys."""
    for key in keys:
        if key in payload and payload[key] not in (None, "", {}):
            return payload[key]
    return None


def _metrics(payload: Dict[str, Any]) -> List[str]:
    """Flatten a metrics mapping into ``key: value`` lines."""
    raw = payload.get("metrics")
    if isinstance(raw, dict):
        return [
            f"- **{_text(key)}:** {_text(value)}"
            for key, value in raw.items()
            if value is not None
        ]
    return _items(raw)


def format_digest(raw_json: str) -> str:
    """Parse ``raw_json`` and return a Markdown status digest.

    Raises:
        ValueError: if the input is not valid JSON or not a JSON object.
    """
    try:
        payload = json.loads(raw_json)
    except (TypeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Invalid JSON input: {exc}") from exc

    if not isinstance(payload, dict):
        raise ValueError("Status payload must be a JSON object")

    lines = [
        "# System Status Digest",
        "",
        f"**Service:** {_text(_first(payload, 'service', 'name'))}",
        f"**Status:** {_text(_first(payload, 'status', 'state'))}",
        f"**Uptime:** {_text(_first(payload, 'uptime', 'uptime_pct'))}",
    ]

    metrics = _metrics(payload)
    if metrics:
        lines += ["", "## Metrics", *metrics]

    notes = _items(_first(payload, "notes", "note"))
    if notes:
        lines += ["", "## Notes", *[f"- {note}" for note in notes]]

    alerts = _items(_first(payload, "alerts", "alert"))
    if alerts:
        lines += ["", "## Alerts", *[f"- {alert}" for alert in alerts]]

    return "\n".join(lines) + "\n"


def main(argv: List[str] = None) -> int:
    """CLI entrypoint: read JSON from a file path argument or stdin."""
    args = sys.argv[1:] if argv is None else argv
    if len(args) > 1:
        print("usage: python -m apps.sys_digest.digest [status.json]", file=sys.stderr)
        return 2

    try:
        if args:
            with open(args[0], encoding="utf-8") as handle:
                raw_json = handle.read()
        else:
            raw_json = sys.stdin.read()
        print(format_digest(raw_json), end="")
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
