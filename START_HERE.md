# ANARCHY — START HERE

## Current project state

ANARCHY is now being organized as a **25-year technical research record plus an enterprise-ready, reproducible, provenance-aware engineering platform**. The project connects historical GNU/Linux and networking work with modern build, licensing, provisioning, archival, distributed persistence, and legitimate device-restore research.

## For a new ChatGPT/agent session

Read these files in this order:

1. `ANARCHY_CONTEXT.md` — canonical project context and continuation directive.
2. `docs/ANARCHY-MASTER-MAP.md` — how the historical, engineering, evidence, provisioning, restore, and RitualMesh layers fit together.
3. `docs/architecture/ANARCHY-25-YEAR-LINEAGE.md` — historical and technical lineage.
4. `docs/architecture/ANARCHY-APPLE-RESTORE.md` — current Apple restore architecture and security boundary.
5. `docs/ANARCHY-ENTERPRISE-READINESS.md` — sponsor, enterprise, reproducibility, and funding framework.
6. `docs/provenance/one-click-provisioning.md` — build, package, provenance and one-click provisioning model.
7. `docs/licensing/ANARCHY-LICENSE-GOVERNANCE.md` — open distribution, license closure, SPDX/SBOM, and decentralized compliance model.
8. `docs/licensing/evidence-status.md` — what is verified versus still awaiting primary evidence.
9. `README.md` — broader research corpus and project history.

### Continuation phrase

Use:

> **Open `ANARCHY_CONTEXT.md`, then the ANARCHY Master Map, and continue from the current canonical project state.**

The assistant/agent should inspect the current repository state and continue from what is implemented, proposed, verified, blocked, or unresolved. Do not make the user restate the architecture.

## Evidence rule

The repository deliberately records unresolved items such as the actual DC219 policy, Linux&C Vol. 39 and exact FunkyMios source. Those items must remain marked **UNVERIFIED** until their primary artifacts are inspected.

## Enterprise rule

> **Close the engineering loop, not the upstream licenses.**

ANARCHY tracks upstream licenses, notices, trademarks, provenance, modifications, and redistribution requirements separately. Open distribution is a rights-aware engineering process, not a blanket relicensing claim.

## Working rule

Substantial changes should use a topic branch and pull request. Keep `main` stable. Branches and pull requests provide an isolated review path for important changes.
