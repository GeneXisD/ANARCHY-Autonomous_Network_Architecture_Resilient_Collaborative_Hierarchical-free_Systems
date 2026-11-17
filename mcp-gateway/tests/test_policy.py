from __future__ import annotations

import pytest

from anarchy_mcp_gateway.policy import (
    ALLOWED_TOOLS,
    ToolDeniedError,
    require_allowed,
)


def test_status_tool_is_explicitly_allowlisted() -> None:
    assert ALLOWED_TOOLS == frozenset({"gateway_status"})
    require_allowed("gateway_status")


@pytest.mark.parametrize(
    "tool_name",
    [
        "github_write_file",
        "database_execute_sql",
        "shopify_refund_order",
        "run_shell_command",
        "../gateway_status",
        "",
    ],
)
def test_unlisted_tools_are_denied(tool_name: str) -> None:
    with pytest.raises(ToolDeniedError):
        require_allowed(tool_name)
