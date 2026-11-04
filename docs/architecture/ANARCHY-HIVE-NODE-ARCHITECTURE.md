# ANARCHY Hive — Six-Node Architecture

**Status:** PROPOSED — architecture specification; deployment not yet verified  
**Baseline date:** 2026-11-03

## 1. Purpose

The ANARCHY Hive is a cooperative environment of independent physical computers. Each node has its own operating system, cryptographic identity, local AI agent, capabilities, permissions, logs, and recovery path. The agents coordinate work and share authorized project knowledge so the environment behaves as one cooperative system without becoming one monolithic process or depending on one permanent master.

**Design rule: independent nodes, cooperative intelligence, verifiable work.**

This document records the intended architecture from the current planning discussion. It does not claim that the network, agents, security controls, or external integrations have already been installed or tested.

## 2. Physical node inventory

| Node | Intended role | Known assignment | Verification still required |
|---|---|---|---|
| Dell OptiPlex | Legacy/native build node | Slackware and Emerde | Installed release, CPU architecture, storage layout, network services, build status |
| Newer Windows laptop | Primary development workstation | Windows, Visual Studio 2026 Community, XAMPP | Git/Chocolatey installation, XAMPP service state, exact hardware and build paths |
| Older MacBook | Legacy Linux node | Ubuntu 14.04 | Intel/PowerPC/other architecture, exact Ubuntu image, packages, available RAM/storage |
| MacBook M4 | Modern Apple node | macOS and XAMPP development | Installed versions, local service configuration, AI runtime capability |
| Additional MacBook | Additional test/build node | Not assigned yet | Model, CPU architecture, OS, storage, role |
| Older iMac | Additional test/storage node | Not assigned yet | Model, CPU architecture, OS, storage, role |

Use neutral node IDs such as NODE-01 through NODE-06 until the hardware is inventoried. Do not publish personal hostnames, serial numbers, private IP addresses, MAC addresses, credentials, or precise physical location in the public repository.

## 3. Per-node AI agent

Each node is intended to run a separate agent instance. The implementation may use different local models or runtimes depending on hardware capability; no model, vendor, or minimum hardware requirement is selected yet.

Every agent should have:

- a unique node and agent identity;
- a dedicated cryptographic key pair, stored outside the repository;
- a declared capability manifest (OS, architecture, tools, build targets, available resources);
- local working memory and logs;
- explicit read/write/execute permissions;
- a task inbox and outbound message interface;
- a versioned configuration and reproducible installation record;
- an offline mode for local work when other nodes are unavailable.

A node agent is not automatically trusted to execute every task. High-impact actions require policy checks, human approval, or independent verification.

### Cooperative behavior

Agents may:

1. publish availability and capabilities;
2. request or accept bounded tasks;
3. delegate work to another authorized agent;
4. exchange signed task results and evidence references;
5. independently verify another node's output;
6. synchronize only authorized project knowledge;
7. continue local work during network partition;
8. reconcile task state after reconnection.

Shared memory is not unrestricted filesystem replication. Private files, credentials, local chat history, and personal data remain local unless explicitly approved for transfer.

## 4. Coordination and task ledger

The Hive requires a durable task ledger with at least:

- task ID and parent task ID;
- requesting agent and assigned agent;
- task description and acceptance criteria;
- status and timestamps;
- lease/claim expiry where applicable;
- input artifact hashes;
- output artifact hashes;
- test results and evidence references;
- permission/approval record;
- retry and failure history.

The coordinator is a replaceable service role, not an owner of the network. Use leases or another documented coordination mechanism so a node failure does not permanently strand work. Conflict resolution and offline reconciliation must be tested before claiming multi-master operation.

## 5. XAMPP management plane

XAMPP is the initial local application and management foundation because it provides a practical Apache/PHP/MariaDB development environment.

Proposed responsibilities:

- node registry and capability inventory;
- human-facing Control Center;
- task and build-block dashboard;
- API endpoints for node agents;
- build records and evidence links;
- project configuration and role administration;
- status history and audit views.

XAMPP is not required to host every workload. Native compilers, build tools, AI inference runtimes, SSH services, cryptographic agents, message workers, and node daemons should run as separate native processes when appropriate. A PHP web interface must not become a privileged remote shell.

Initial service boundaries:

- web UI: presentation and human approval;
- API: authenticated requests and response validation;
- database: task metadata, node registry, status history;
- worker: bounded job execution under a dedicated unprivileged account;
- artifact store: content-addressed outputs with hashes and rights metadata;
- secrets: OS-protected secret storage, never source-controlled.

## 6. Network and security planes

### Initial trusted transport

Begin with a known local network and authenticated SSH or mutually authenticated TLS. Establish node identity, key rotation, firewall rules, least privilege, and audit logging before adding anonymity or overlay routing.

### Hyphanet / Freenet

Hyphanet (the continuation of the original Freenet project) Darknet mode is a candidate friend-to-friend overlay for explicitly trusted peers. The trust graph and peer enrollment must be intentional. Darknet participation does not automatically authenticate every application request or protect every local service.

### Tor

Tor is a separate privacy-routing layer for explicitly selected outbound traffic. It is not the default transport for every internal node-to-node operation. Define which processes may use Tor, how DNS is handled, and what happens when Tor is unavailable.

**Do not assume Hyphanet automatically routes through Tor.** If a particular application path is intended to traverse both, design and test that path explicitly. Avoid accidental clearnet fallback and verify DNS, IPv4/IPv6, and connection-leak behavior.

### Security baseline

- unique per-node identity and key;
- mutually authenticated connections for control traffic;
- least-privilege service accounts;
- signed task messages and verifiable artifacts;
- secrets kept out of Git and public status records;
- explicit human approval for destructive or privileged operations;
- encrypted backups and tested recovery;
- firewall segmentation between management, build, and external-access paths;
- tamper-evident audit events;
- documented threat model and incident procedure.

Do not describe the environment as military-grade or certified until a defined standard, independent assessment, and test evidence support that claim.


## 7.1 Lockheed Martin Software Factory — reference model

The two Lockheed Martin references supplied for this project describe a **software-factory operating model**, not simply a list of open-source utilities:

- [Lockheed Martin: Software Factory continues to expand company-wide software development capabilities (2020)](https://www.lockheedmartin.com/en-us/news/features/2020/lockheed-martin-software-factory-continues-expand-company-accelerates-software-development-capabilities.html)
- [Lockheed Martin: Software Factory](https://www.lockheedmartin.com/en-us/capabilities/digital-transformation/software-factory.html)

ANARCHY should study this model for its engineering workflow: standardized development environments, repeatable build pipelines, automation, integration and test practices, reusable tooling, and a path from developer work to validated software delivery. The 2020 article is historical context; the current capability page should be rechecked before making claims about current products, scale, or implementation details.

### ANARCHY adaptation

The ANARCHY implementation is its own independently built software factory, centered initially on the XAMPP management plane and the six-node physical lab. Its planned factory stages are:

1. **Intake:** create a build-block/task record, identify owner and target node, define acceptance criteria.
2. **Source control:** identify repository, branch, commit, authorship, and applicable license.
3. **Environment qualification:** verify OS, CPU architecture, compiler/toolchain, dependencies, and build configuration on the selected physical node.
4. **Automated build:** execute a repeatable, logged build with pinned inputs where feasible.
5. **Continuous integration:** run formatting, static analysis, unit/integration tests, and platform-specific checks.
6. **Security and provenance:** generate an SBOM, record dependency licenses, scan artifacts, preserve hashes and build logs, and sign outputs where the key-management design is ready.
7. **Independent verification:** a second node or reviewer checks the artifact and evidence rather than trusting the producing node alone.
8. **Release authorization:** a human-approved gate checks test results, rights, notices, security findings, and distribution permissions.
9. **Deployment and feedback:** deploy only to an authorized target, record the version, and feed failures back into a tracked build block.

### Candidate capability map

| Software-factory capability | ANARCHY implementation direction |
|---|---|
| Standardized engineering workflow | BUILD_STATUS.md, build-block issue template, and build-block workflow |
| Multi-platform development | Windows/Visual Studio, OptiPlex/Slackware-Emerde, Ubuntu 14.04 legacy node, and macOS nodes |
| Build automation | Native per-platform scripts and reproducible build definitions |
| CI and automated testing | Repository CI plus node-specific test runners; select tooling after compatibility review |
| Shared engineering services | XAMPP-based project dashboard, task ledger, artifact index, and API |
| Security and supply-chain controls | SBOM, dependency/license inventory, hashes, provenance, signed artifacts, and access controls |
| Distributed engineering | Per-node AI agents, task delegation, independent verification, and offline-capable work queues |
| Release governance | Human approval and explicit licensing/security acceptance gates |

These are ANARCHY design targets, not claims that Lockheed Martin software, processes, source code, or proprietary systems are available to or adopted by ANARCHY. No affiliation, endorsement, partnership, or license is implied. Each candidate tool must be evaluated from its authoritative upstream source, exact version, license, dependency chain, and supported platforms before inclusion.

## 7. External technology and validation boundaries

| Reference | Intended use in ANARCHY | Boundary |
|---|---|---|
| IBM | Evaluate agent orchestration, governance, and interoperability patterns; assess MCP/A2A and relevant IBM offerings | No partnership, purchase, or mandatory cloud dependency is implied |
| Broadcom | Production capability reference for infrastructure, automation, and API management | ANARCHY intends to implement its own services; no Broadcom source, product license, or endorsement is assumed |
| Oracle LiveLabs | External workshop and cloud validation where the selected workshop permits the test | Follow workshop terms; use sanitized test data; preserve source and evidence outside temporary lab resources |
| Lockheed Martin-linked OSS projects | Evaluate relevant open-source build, SBOM, testing, and engineering tools | Verify exact upstream, release, license, dependencies, platform support, and redistribution rights before adoption |
| Hyphanet and Tor | Candidate trust overlay and separate privacy-routing layer | Distinct protocols and trust boundaries; neither substitutes for endpoint security |

Every candidate dependency requires a component record and rights review before production inclusion.

## 8. Build and verification workflow

    SOURCE + DECLARED LICENSE
          |
          v
    SOURCE REVISION + HASH
          |
          v
    NODE CAPABILITY CHECK
          |
          v
    BUILD BLOCK / TASK CLAIM
          |
          v
    REPRODUCIBLE BUILD
          |
          v
    INDEPENDENT TEST / REVIEW
          |
          v
    SBOM + PROVENANCE + NOTICES
          |
          v
    SIGNED ARTIFACT + RELEASE DECISION
          |
          v
    LOCAL REPOSITORY / AUTHORIZED DISTRIBUTION

Build, test, package, release, provision, and deploy are separate states. A successful compilation is not automatically a release or permission to redistribute.

## 9. Implementation milestones

| Milestone | Exit criteria | State |
|---|---|---|
| H0 — Inventory | Six machines identified by model, CPU architecture, OS, storage, network role | PROPOSED |
| H1 — Laptop foundation | Visual Studio, Git, XAMPP verified; source checkout and build paths documented | NOT STARTED |
| H2 — Native build node | OptiPlex Slackware/Emerde state inventoried; one reproducible test build | NOT STARTED |
| H3 — Legacy node | Ubuntu 14.04 architecture and supported toolchain documented; compatibility test | NOT STARTED |
| H4 — Node identity | Key provisioning, mutual authentication, rotation, revocation tested | NOT STARTED |
| H5 — First two agents | Two independent agents exchange tasks and signed results; one can operate offline | NOT STARTED |
| H6 — Six-node expansion | All nodes enrolled with capability manifests and access controls | NOT STARTED |
| H7 — Overlay security | Hyphanet/Tor routes explicitly designed, isolated, and leak-tested | NOT STARTED |
| H8 — External validation | Approved Oracle LiveLabs workshop test completed; evidence retained locally | NOT STARTED |

## 10. Acceptance tests

Do not mark a milestone complete until evidence demonstrates:

- a node can be identified and revoked;
- unauthorized nodes cannot claim tasks;
- agents can exchange a task and verify its result;
- a node can continue local work during disconnection;
- the task ledger reconciles after reconnection;
- secrets do not appear in logs, Git, or public status;
- artifact hashes and build records match;
- a failed coordinator does not destroy the task history;
- external routing follows the declared policy without unintended fallback;
- recovery from a lost node or corrupted local state is demonstrated.

## 11. References and status

This document is an ANARCHY design specification. Product names and external organizations are references for evaluation, not claims of sponsorship, partnership, certification, or endorsement. Exact upstream documentation and license evidence must be attached before a dependency is approved.

Related documents:
- BUILD_STATUS.md
- docs/workflow/BUILD-BLOCK-WORKFLOW.md
- docs/licensing/ANARCHY-LICENSE-GOVERNANCE.md
- docs/ANARCHY-MASTER-MAP.md
