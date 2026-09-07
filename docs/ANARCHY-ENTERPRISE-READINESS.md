# ANARCHY — Enterprise Readiness Framework

## Purpose

ANARCHY is being organized as an enterprise-ready, open research and engineering program without collapsing the distinct identities, licenses, trademarks, provenance, and governance of the projects from which its corpus is assembled.

The objective is to make the project understandable to sponsors, grant reviewers, engineering partners, auditors, and open-source contributors while preserving the underlying 25-year technical history as evidence rather than obscuring it.

## Operating principle

> **Close the engineering loop, not the upstream licenses.**

ANARCHY may integrate, rebuild, document, provision, test, and distribute artifacts subject to their governing terms. It does not automatically acquire ownership of upstream works, change upstream licenses, or acquire trademark rights merely by incorporating a component.

## Enterprise lifecycle

```text
RESEARCH
  ↓
SOURCE IDENTIFICATION
  ↓
PROVENANCE + LICENSE AUDIT
  ↓
DEPENDENCY / SBOM RECORD
  ↓
CONTROLLED BUILD
  ↓
TEST + VALIDATION
  ↓
ARTIFACT HASHING
  ↓
RELEASE RECORD
  ↓
DECLARATIVE PROVISIONING
  ↓
DEPLOYMENT / RESTORE
  ↓
OBSERVATION + FEEDBACK
  ↓
ARCHIVAL EVIDENCE
```

## Enterprise controls

### 1. Source control

Every incorporated source should identify, where available:

- upstream project;
- repository or publication;
- release/tag/commit;
- acquisition date;
- cryptographic hash;
- local modifications;
- patch set;
- build environment.

### 2. License control

License status is recorded at component level. A top-level distribution license is never treated as a substitute for component notices or obligations.

### 3. Trademark control

Copyright, open-source licensing, patents, trademarks, logos, endorsement, and branding are tracked as separate rights questions.

### 4. Release control

A successful build is not automatically a release. Release records should identify the exact source, dependencies, configuration, tests, hashes, notices, and distribution terms.

### 5. Security control

The repository should progressively adopt appropriate secret scanning, dependency/security alerts, code scanning, and responsible disclosure practices. GitHub recommends these controls as part of repository security hygiene. citeturn0search0

### 6. Auditability

Material decisions should be represented by durable repository artifacts rather than relying on undocumented conversation history.

## Enterprise evidence classes

| Class | Meaning |
|---|---|
| VERIFIED | Supported by inspected primary evidence |
| SUPPORTED | Strongly supported by authoritative upstream documentation |
| OBSERVED | Directly observed in a supplied artifact |
| REPRODUCED | Independently built/tested by ANARCHY work |
| PROPOSED | Architecture or future implementation |
| UNVERIFIED | Evidence still required |
| HYPOTHESIS | Plausible interpretation requiring further evidence |
| BLOCKED | Cannot proceed until a missing dependency/right/artifact is resolved |

## Sponsor-facing value proposition

ANARCHY combines:

- long-term historical technical research;
- reproducible software construction;
- open-source provenance and licensing analysis;
- distributed persistence and archival research;
- declarative provisioning;
- Linux and cross-toolchain engineering;
- device restore/recovery research within legitimate security boundaries;
- decentralized orchestration through RitualMesh;
- an evidence-first research methodology.

The repository is therefore both a technical corpus and a reproducibility framework.

## Funding work packages

### WP1 — Historical corpus

Recover, hash, classify, and preserve the 25-year technical record.

### WP2 — Provenance and licensing

Build component-level license, notice, trademark, source, and modification records.

### WP3 — Reproducible build infrastructure

Integrate controlled toolchains, kernel/module builds, dependency records, SBOM generation, and artifact verification.

### WP4 — Provisioning infrastructure

Implement the ANARCHY manifest and local repository model inspired by XAMPP-style packaging and openSUSE/YMP declarative provisioning.

### WP5 — Restore research

Implement the observable/open-source host-side restore workflow using legitimate device and firmware inputs without bypassing proprietary security controls.

### WP6 — Decentralized distribution

Connect reproducible artifacts and metadata to RitualMesh/local distribution and future peer-to-peer persistence mechanisms.

### WP7 — Demonstration and technology transfer

Produce reproducible demonstrations, technical reports, sponsor-ready milestones, and open research outputs.

## Enterprise readiness definition

ANARCHY is enterprise-ready when an independent reviewer can answer, for a released artifact:

1. What is it?
2. Where did every material component come from?
3. Which version was used?
4. What license governs each component?
5. What notices and attribution are required?
6. What modifications were made?
7. How was it built?
8. What was tested?
9. What exact artifact was released?
10. What rights and restrictions apply to redistribution?
11. Which trademarks are present?
12. What evidence supports every material claim?

That is the standard ANARCHY should build toward.
