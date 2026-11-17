"""Small default-deny policy boundary for the initial gateway."""

from __future__ import annotations

ALLOWED_TOOLS = frozenset({"gateway_status"})


class ToolDeniedError(PermissionError):
    """Raised when a tool is not explicitly allowed."""


def require_allowed(tool_name: str) -> None:
    """Allow only explicitly registered Phase 1 tools."""
    if tool_name not in ALLOWED_TOOLS:
        raise ToolDeniedError(f"Tool is not allowlisted: {tool_name}")
