# ANARCHY MCP Gateway Implementation Plan

## Phase 0 — Architecture and threat model

Status: documented on the foundation branch.

- Define MCP as an adapter interface, not the ANARCHY network core.
- Establish local-only, read-only defaults.
- Define trust boundaries, credential handling, audit requirements, and release gates.

## Phase 1 — Minimal Python MCP server

Deliverables:

- Python package with a pinned MCP SDK dependency.
- Local stdio transport only.
- Health/version resource or tool.
- Central policy module and explicit tool registry.
- Structured, redacted audit events.
- Unit tests for policy enforcement and input validation.
- No external credentials required for the first smoke test.

Acceptance criteria:

- An MCP client can discover and invoke the harmless health tool.
- No network listener is opened.
- No write-capable tool is registered.
- Invalid arguments are rejected.
- Audit records contain no secrets.

## Phase 2 — GitHub read-only adapter

Deliverables:

- Read repository metadata.
- List branches.
- Read selected text files.
- List recent commits.
- Dedicated least-privilege GitHub credential supplied at runtime.

Acceptance criteria:

- Read operations work against an explicitly configured repository allowlist.
- Private repositories are inaccessible unless explicitly authorized.
- No issue, PR, workflow, file-write, or repository-admin mutation tool is exposed.

## Phase 3 — Database read-only adapter

Deliverables:

- Support one explicitly configured database engine initially.
- Use a dedicated read-only database principal.
- Expose schema inspection only for allowlisted datasets.
- Execute named, parameterized query templates; do not expose arbitrary SQL.

Acceptance criteria:

- Attempts to mutate data fail at the database permission layer.
- Query duration, row count, and output size are bounded.
- Sensitive columns are excluded unless separately approved.

## Phase 4 — Shopify read-only adapter

Deliverables:

- Use a merchant-authorized Shopify Admin API connection.
- Read product/catalog information.
- Read inventory snapshots.
- Read limited order status fields.
- Exclude customer personal data by default.

Acceptance criteria:

- Required API scopes are documented and minimized.
- No product, inventory, order, refund, payment, theme, or settings mutation tools are exposed.
- Access is tested against a development/test store before production.

## Phase 5 — ANARCHY identity and policy integration

- Map authenticated principals to ANARCHY identities.
- Add capability-based authorization.
- Bind audit records to identity and policy decisions.
- Add service discovery without making MCP the only discovery mechanism.
- Define offline and degraded operation behavior.

## Phase 6 — Controlled write capabilities (separate review)

No write capability is enabled by default. Each proposed write tool requires:

1. A documented business or infrastructure need.
2. A dedicated permission and narrow scope.
3. A dry-run or preview mode.
4. Explicit human approval at execution time.
5. Idempotency and replay protection where applicable.
6. Audit event and rollback/recovery plan.
7. Tests proving unauthorized principals cannot invoke it.

Financial operations, payouts, refunds, and destructive infrastructure operations require separate security and business approval.

## First implementation decision

Start with Phase 1 and a no-credential smoke test. Then add adapters one at a time. Do not connect production GitHub, database, or Shopify credentials until the local gateway passes its Phase 1 tests.
