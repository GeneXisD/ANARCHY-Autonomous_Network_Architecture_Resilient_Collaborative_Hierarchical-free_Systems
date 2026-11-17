# ANARCHY MCP Gateway — Phase 1

This package is the first executable gateway milestone. It intentionally exposes one harmless status tool and no external integrations.

## Requirements

- Python 3.11 or newer
- pip or uv

## Install

From this directory:

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux, macOS, or Cygwin:
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the tests

```bash
python -m pytest -q
```

## Run the MCP server

```bash
python -m anarchy_mcp_gateway.server
```

The server uses MCP stdio transport. It does not open a TCP port. Connect an MCP client to the Python module/entry point using that client's local stdio-server configuration.

For interactive development, the official MCP Inspector can launch the server:

```bash
mcp dev src/anarchy_mcp_gateway/server.py
```

## Initial tool

- `gateway_status`: reports the gateway name, version, transport posture, and read-only status.

No GitHub, database, Shopify, filesystem, shell, or network tools are registered in this phase. No credentials are required.

## Security posture

- stdio only
- read-only
- default-deny tool policy
- structured audit events
- no credentials
- no arbitrary code execution
- no remote listener

This is a development foundation, not a production deployment. See the architecture and threat-model documents in `../docs/integrations/mcp/`.
