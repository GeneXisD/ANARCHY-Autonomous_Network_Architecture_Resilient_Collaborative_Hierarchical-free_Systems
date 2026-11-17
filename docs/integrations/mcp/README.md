# ANARCHY MCP Gateway

## Purpose

The ANARCHY MCP Gateway is an interoperability boundary between MCP-capable AI clients and explicitly authorized ANARCHY services. It is an adapter layer, not the ANARCHY network itself.

ANARCHY must remain operable if MCP, any AI provider, GitHub, Shopify, or a cloud provider becomes unavailable. MCP is one supported interface among multiple possible interfaces.

## Initial operating mode

The first implementation is local-only and read-only:

- MCP transport: standard input/output (stdio)
- Runtime: Python
- GitHub: repository metadata and file inspection only
- Database: explicitly configured read-only connection and approved query templates only
- Shopify: catalog, inventory, and order visibility only, after a merchant-authorized API connection exists
- Audit: structured event records with secret redaction
- Writes: disabled
- Payment operations: out of scope
- Public network listener: disabled

No credentials are committed to this repository. Secrets are supplied at runtime through an approved secret store or environment injection and must never be included in logs or tool results.

## Logical architecture

```text
MCP CLIENTS
  ChatGPT / Copilot / Codex / other authorized clients
                 |
                 | MCP (local stdio first)
                 v
       ANARCHY MCP GATEWAY
       - tool allowlist
       - policy enforcement
       - input validation
       - output filtering
       - audit events
                 |
       +---------+----------+
       |         |          |
       v         v          v
    GitHub    Database   Shopify
    adapter   adapter    adapter
       |         |          |
       v         v          v
  GitHub API  Read-only   Shopify Admin
              DB role    GraphQL API

       ANARCHY identity, trust, provenance,
       service discovery and resilience remain
       independent core services.
```

## Security invariants

1. Default deny: a capability is unavailable unless explicitly allowlisted.
2. Read-only first: the initial release exposes no mutation tools.
3. Least privilege: each adapter uses a dedicated credential with minimum required access.
4. Credential separation: an MCP client credential is never forwarded as an upstream GitHub, database, or Shopify credential.
5. Validate every input and bound result size, execution time, and query cost.
6. Treat repository text, database content, supplier data, and tool output as untrusted data, not instructions.
7. Do not log access tokens, passwords, private keys, customer payment data, or full secret-bearing request headers.
8. Require human approval and a separate authorization path before any future write capability.
9. Keep the gateway local until authentication, authorization, TLS, rate limits, and operational monitoring are implemented for remote access.
10. MCP is replaceable; no core ANARCHY identity or network function may depend exclusively on MCP.

## Planned tool surface

### GitHub (read-only)

- `github_repo_metadata`
- `github_list_branches`
- `github_read_file`
- `github_list_recent_commits`

### Database (read-only)

- `database_list_allowed_datasets`
- `database_describe_dataset`
- `database_run_approved_query`

The database adapter must not expose unrestricted SQL execution in the initial release. Queries are named, parameterized, bounded, and reviewed.

### Shopify (read-only)

- `shopify_list_products`
- `shopify_get_product`
- `shopify_inventory_snapshot`
- `shopify_order_status`

Order tools must return only fields necessary for the requested operational task. Customer personal data is excluded by default.

## Implementation status

This document establishes the architecture and security baseline. It does not claim that a gateway, adapter, credential, or live connection has already been deployed.

See [Implementation Plan](IMPLEMENTATION_PLAN.md) and [Threat Model](THREAT_MODEL.md).
