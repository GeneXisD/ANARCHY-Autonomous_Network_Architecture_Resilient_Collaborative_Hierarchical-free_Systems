# ANARCHY One-Click Provisioning and Provenance

## Purpose

ANARCHY treats provisioning as a reproducible, auditable build/distribution problem rather than a collection of manual installation commands.

The model combines lessons from XAMPP, openSUSE One Click Install/YMP, Apache Ant/Tomcat, package ecosystems, crosstool-NG and software-license inventories.

## Architecture

```text
SOURCE
  ↓
COMPONENT INVENTORY
  ↓
LICENSE / NOTICE / COPYRIGHT
  ↓
DEPENDENCY GRAPH
  ↓
BUILD CONFIGURATION
  ↓
CROSS-TOOLCHAIN
  ↓
BUILD
  ↓
TEST
  ↓
SBOM
  ↓
HASH / SIGNATURE
  ↓
PACKAGE
  ↓
DECLARATIVE MANIFEST
  ↓
LOCAL REPOSITORY
  ↓
ONE-CLICK PROVISION
  ↓
VALIDATION
```

## Component record

Every third-party component should eventually have a machine-readable record containing:

- name;
- upstream project;
- repository URL;
- version/tag/commit;
- release date;
- license SPDX identifier or verified license text;
- copyright holders;
- notices;
- dependencies;
- local modifications;
- patch files;
- build toolchain;
- build configuration;
- source hash;
- artifact hash;
- redistribution status;
- trademark requirements;
- evidence source;
- evidence status.

## License principle

A distribution-level license does not erase the licenses of embedded components.

```text
ANARCHY LICENSE / PROJECT TERMS
             │
             ├── component A license
             ├── component B license
             ├── component C license
             └── component-specific notices
```

Copyright, open-source license, trademark, patent, and contractual permissions must be treated as separate fields.

## XAMPP precedent

XAMPP demonstrates a practical distribution model in which independently licensed components are assembled into an installable developer environment. Its build infrastructure is therefore useful as a precedent for ANARCHY's installer/package engineering.

Do not interpret XAMPP as granting a universal license to bundled software.

## openSUSE YMP precedent

The One Click Install model demonstrates declarative repository/package provisioning. ANARCHY can adapt the concept without copying openSUSE branding or implying endorsement.

## Ant/Tomcat precedent

Ant/Tomcat demonstrates explicit build configuration, dependency caching, normal versus release builds, testing, packaging and integrity/signing stages.

## Local repository model

RitualMesh can provide the local distribution/orchestration layer:

```text
ANARCHY build artifacts
        ↓
provenance database / manifests
        ↓
RitualMesh local repository
        ↓
127.0.0.1 services
        ↓
provisioning clients
```

The local repository is an orchestration mechanism, not a change to upstream ownership or licensing.

## Future automation

Recommended future artifacts:

- `manifests/anarchy-restore.yaml`
- `sbom/`
- `70-provenance/hashes/`
- `70-provenance/build-records/`
- `scripts/verify-provenance.sh`
- `scripts/generate-sbom.sh`
- `scripts/build-manifest.sh`
- `60-licensing/license-matrix/`

## Evidence statuses

Use:

- VERIFIED
- SUPPORTED
- UNVERIFIED
- HYPOTHESIS
- PROPOSED
- IMPLEMENTED
- BLOCKED

Never turn an unverified policy, license, relationship, or historical claim into a verified fact merely because it appears in a prior conversation.
