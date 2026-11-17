"""Structured audit events; never pass secrets or raw request payloads here."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from typing import Any

_LOGGER = logging.getLogger("anarchy_mcp_gateway.audit")


def audit_event(
    *,
    tool: str,
    decision: str,
    outcome: str,
    principal: str = "local_process",
) -> dict[str, Any]:
    """Emit a minimal event without arguments, credentials, or customer data."""
    event: dict[str, Any] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "component": "anarchy-mcp-gateway",
        "version": "0.1.0",
        "principal": principal,
        "tool": tool,
        "decision": decision,
        "outcome": outcome,
    }
    _LOGGER.info("%s", json.dumps(event, sort_keys=True))
    return event
