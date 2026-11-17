from __future__ import annotations

import json
import logging

from anarchy_mcp_gateway.audit import audit_event


def test_audit_event_is_structured_and_minimal(caplog) -> None:
    with caplog.at_level(logging.INFO, logger="anarchy_mcp_gateway.audit"):
        event = audit_event(
            tool="gateway_status",
            decision="allow",
            outcome="success",
        )

    assert event["component"] == "anarchy-mcp-gateway"
    assert event["tool"] == "gateway_status"
    assert event["decision"] == "allow"
    assert "access_token" not in event
    assert "password" not in event

    logged = json.loads(caplog.records[-1].message)
    assert logged == event
