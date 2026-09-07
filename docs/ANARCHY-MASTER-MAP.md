# ANARCHY — Master Architecture Map

## One project, multiple layers

```text
                         ANARCHY
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
       ▼                    ▼                    ▼
   25-YEAR              ENGINEERING          EVIDENCE
   CORPUS                PLATFORM             SYSTEM
       │                    │                    │
       │              ┌─────┼─────┐             │
       │              │     │     │             │
       ▼              ▼     ▼     ▼             ▼
 Dynebolic         Build  Restore Provision  Provenance
 Puredyne          Linux  Apple   YMP/XAMPP   SPDX/SBOM
 RHCygwin          Kernel iDevice Local repo  Hashes
 X11               crosstool Android RitualMesh Notices
 XAMPP             Ant     tooling 127.0.0.1  Evidence
 openSUSE          toolchains
 Linux&C            packaging
 Apache/PHP
 Tomcat
```

## Build plane

```text
SOURCE
  ↓
TOOLCHAIN
  ↓
KERNEL / MODULES / APPLICATIONS
  ↓
TEST
  ↓
ARTIFACT
  ↓
HASH
  ↓
SBOM + PROVENANCE
```

## Provisioning plane

```text
ANARCHY MANIFEST
       ↓
REPOSITORIES
       ↓
PACKAGES / ARTIFACTS
       ↓
DEPENDENCY RESOLUTION
       ↓
INSTALL / CONFIGURE
       ↓
VALIDATE
```

## Restore plane

```text
DEVICE IDENTIFICATION
       ↓
LEGITIMATE IMAGE ACQUISITION
       ↓
IMAGE / IPSW INSPECTION
       ↓
PARTITION / FILESYSTEM HANDLING
       ↓
OPEN RESTORE TOOLING
       ↓
KERNEL / MODULE BUILD WHERE APPLICABLE
       ↓
INTEGRITY VERIFICATION
       ↓
RESTORE
       ↓
POST-RESTORE VALIDATION
```

## Distribution plane

```text
VERIFIED ARTIFACT
      +
PROVENANCE METADATA
      +
LICENSE METADATA
      +
SBOM
      +
NOTICE DATA
          ↓
   LOCAL REPOSITORY
          ↓
       RitualMesh
          ↓
 DISTRIBUTED / PEER NODES
```

Decentralization changes the transport and persistence model; it does not erase upstream licensing obligations.

## Governance plane

```text
EVIDENCE
  ↓
TECHNICAL DECISION
  ↓
LICENSE DECISION
  ↓
SECURITY DECISION
  ↓
RELEASE DECISION
  ↓
DISTRIBUTION DECISION
```

Every decision should be traceable to evidence or explicitly marked as a proposal/hypothesis.

## Historical-to-future bridge

The 25-year record is the input corpus. The ANARCHY engineering platform is the transformation layer. RitualMesh is the decentralized orchestration/distribution layer.

```text
HISTORY
  ↓
EVIDENCE
  ↓
REPRODUCIBILITY
  ↓
ENGINEERING
  ↓
PROVISIONING
  ↓
DISTRIBUTION
  ↓
DEPLOYMENT
  ↓
NEW EVIDENCE
  └──────────────→ HISTORY
```

This feedback loop is the core of the project.
