"""Local-only MCP server entry point for ANARCHY."""

from __future__ import annotations

import logging
from typing import Any

from mcp.server import MCPServer

from . import __version__
from .audit import audit_event
from .policy import require_allowed

logging.basicConfig(level=logging.INFO)
mcp = MCPServer("ANARCHY MCP Gateway")


@mcp.tool()
def gateway_status() -> dict[str, Any]:
    """Return the gateway's static operational and security posture."""
    try:
        require_allowed("gateway_status")
    except PermissionError:
        audit_event(
            tool="gateway_status",
            decision="deny",
            outcome="policy_denied",
        )
        raise

    result = {
        "name": "ANARCHY MCP Gateway",
        "version": __version__,
        "transport": "stdio",
        "mode": "read-only",
        "external_integrations": [],
        "network_listener": False,
        "write_tools_enabled": False,
        "status": "phase-1-foundation",
    }
    audit_event(
        tool="gateway_status",
        decision="allow",
        outcome="success",
    )
    return result


def main() -> None:
    """Start the local stdio MCP server."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
