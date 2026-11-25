import json

import pytest

from apps.sys_digest.digest import format_digest


def test_format_digest_valid_payload():
    payload = {
        "name": "api-gateway",
        "status": "healthy",
        "uptime": "42d 3h",
        "metrics": {"cpu": "12%", "memory": "480 MB", "latency_p95": "85 ms"},
        "notes": ["Deployed v2.4.1", "Cache warmed"],
        "alerts": ["Disk usage above 80%"],
    }

    digest = format_digest(json.dumps(payload))

    assert "# System Status Digest" in digest
    assert "**Service:** api-gateway" in digest
    assert "**Status:** healthy" in digest
    assert "**Uptime:** 42d 3h" in digest
    assert "## Metrics" in digest
    assert "- **cpu:** 12%" in digest
    assert "- **latency_p95:** 85 ms" in digest
    assert "## Notes" in digest
    assert "- Deployed v2.4.1" in digest
    assert "## Alerts" in digest
    assert "- Disk usage above 80%" in digest


def test_format_digest_invalid_and_partial_input():
    digest = format_digest(json.dumps({"status": "degraded"}))

    assert "**Service:** unknown" in digest
    assert "**Status:** degraded" in digest
    assert "**Uptime:** unknown" in digest
    assert "## Metrics" not in digest
    assert "## Notes" not in digest
    assert "## Alerts" not in digest

    with pytest.raises(ValueError):
        format_digest("{not valid json")

    with pytest.raises(ValueError):
        format_digest(json.dumps(["not", "an", "object"]))
