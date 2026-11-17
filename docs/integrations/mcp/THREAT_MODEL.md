# ANARCHY MCP Gateway Threat Model

## Scope

This threat model covers the initial local, read-only MCP gateway and its GitHub, database, and Shopify adapters. It does not claim to secure the underlying ANARCHY network or third-party services.

## Assets

- GitHub source code, issues, pull requests, and repository metadata
- Database records and connection credentials
- Shopify catalog, inventory, order, and customer information
- API tokens, passwords, private keys, and OAuth credentials
- Tool policies, audit records, and configuration
- Integrity and availability of the gateway host

## Trust boundaries

1. MCP client to gateway
2. Gateway policy layer to each adapter
3. Adapter to upstream API or database
4. Tool output to the model/client
5. Local host process to user-controlled filesystem and environment

Each boundary requires explicit validation. Content returned by an upstream system is data, not trusted policy or executable instruction.

## Primary threats and controls

| Threat | Initial control |
|---|---|
| Prompt injection in repository, supplier, or database content | Treat all returned content as untrusted; never let content modify gateway policy |
| Excessive agent authority | Read-only tools and explicit tool allowlists |
| Credential theft | Runtime secret injection, least privilege, no secret logging |
| Confused-deputy / token passthrough | Separate upstream credentials; never forward client tokens |
| SQL injection or data exfiltration | Named parameterized queries, read-only database role, row and time limits |
| Excessive Shopify customer-data exposure | Exclude personal fields by default; field allowlists and redaction |
| Malicious or malformed tool arguments | Schema validation, bounds, allowlisted identifiers |
| Denial of service | Request timeouts, response-size limits, concurrency limits |
| Audit tampering | Append-only event format, hash-linked records, periodic externally stored checkpoints |
| Unauthorized remote access | No network listener in initial release |
| Unsafe future write operation | Separate write-capable service, explicit human approval, per-action authorization |

## Audit event minimum

Each event should record:

- UTC timestamp
- gateway version
- client identity, when available
- tool name
- adapter name
- allow/deny decision
- normalized resource identifier
- outcome and duration
- correlation identifier

Do not record secrets, full authorization headers, payment-card data, or unnecessary customer personal information.

A hash-linked log can make later alteration detectable when checkpoints are independently preserved. It is not, by itself, proof that the original event was truthful or that the log cannot be rewritten before checkpointing.

## Release gates

The first release is not ready until:

- tests prove that write tools are not registered;
- database access uses a read-only account;
- credentials are absent from source, logs, and test fixtures;
- invalid and oversized inputs are rejected;
- tool outputs are bounded and sensitive fields are redacted;
- audit events are emitted for allow and deny decisions;
- adapter failures fail closed;
- dependency versions are pinned and scanned.

## Future remote deployment

Before enabling Streamable HTTP or exposing the gateway beyond the local host, add:

- OAuth 2.1-compliant authorization where applicable;
- token audience validation;
- TLS;
- per-client scopes and revocation;
- request rate limits;
- network segmentation;
- security monitoring and incident response;
- explicit consent for each upstream connection.

The gateway must never accept a token intended for another service or pass an MCP client token through to an upstream API.
