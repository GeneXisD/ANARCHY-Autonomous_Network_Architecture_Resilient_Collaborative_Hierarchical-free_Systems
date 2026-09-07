# ANARCHY — 25-Year Technical Lineage

## Purpose

ANARCHY is not a collection of unrelated technologies. It is a research record assembled across a long period of experimentation with GNU/Linux, networking, live distributions, X11, software distribution, build systems, emulation, mobile platforms, device recovery, cross-compilation, archival systems, and decentralized infrastructure.

This document provides the narrative layer connecting those technical domains without asserting that independent upstream projects share ownership, authorship, sponsorship, or organizational control.

## Lineage model

```text
PERSONAL TECHNICAL EXPERIENCE
          ↓
OPERATING SYSTEMS + NETWORKING
          ↓
LIVE / PORTABLE ENVIRONMENTS
          ↓
X11 / GRAPHICS / HOST-GUEST SYSTEMS
          ↓
SOFTWARE DISTRIBUTION + BUILD SYSTEMS
          ↓
LICENSE + PROVENANCE ANALYSIS
          ↓
CROSS-COMPILATION + KERNEL ENGINEERING
          ↓
ANDROID / MOBILE / DEVICE TOOLING
          ↓
APPLE RESTORE RESEARCH
          ↓
REPRODUCIBLE PROVISIONING
          ↓
DISTRIBUTED ARCHIVAL / PERSISTENCE
          ↓
RitualMesh ORCHESTRATION
          ↓
ANARCHY
```

## Historical technology families

### GNU/Linux and portable systems

Dynebolic and Puredyne are preserved as historical portable/live GNU/Linux precedents. Their exact artifacts, versions, notices, and licenses must remain distinguishable from ANARCHY-original work.

### RHCygwin and X11

The RHCygwin/X-server material belongs to the historical systems layer. Directory inventories and binaries should be captured as observed artifacts, then compared technically with later host/guest graphics systems such as Android emulators. Similarity is evidence for investigation, not proof of common provenance.

### XAMPP and software distribution

XAMPP is treated as a precedent for assembling independently licensed components into a practical developer distribution and installer/build environment. The relevant lesson is the distribution engineering model, not ownership of the bundled projects.

### openSUSE/YMP

openSUSE One Click Install provides a declarative provisioning precedent: repositories, package selection, architecture/version handling, and installation actions can be represented as machine-readable metadata.

### Apache / PHP / Tomcat / Ant

The supplied Apache notices and PHP component inventories demonstrate why provenance must operate below the top-level project name. Apache modules and PHP extensions can incorporate separately authored libraries with their own notices and terms. Tomcat/Ant demonstrates explicit configuration, dependency acquisition, build, test, package, and release stages.

### crosstool-NG and Linux kernel/modules

crosstool-NG provides controlled cross-toolchain construction. ANARCHY uses this concept to make kernel and module builds reproducible and traceable rather than treating a toolchain as an invisible prerequisite.

### Android / AOSP / emulator research

Android and emulator work extends the host/guest, graphics, filesystem, build, and device-provisioning lineage. Qualcomm/EDL research is a related but distinct technical branch from Apple's restore ecosystem.

### Apple restore research

The current Apple objective is to reproduce the observable/open-source host-side architecture of restore tooling. The research boundary excludes Activation Lock bypass, FRP bypass, secure-boot bypass, proprietary signing circumvention, and unauthorized device access.

### Web archiving and distributed persistence

ipwb, CarbonDate, Dark and Stormy Archives/Puddles, IPFS/Kubo, and related WS-DL research establish the archival/provenance side of the ANARCHY corpus. These projects contribute prior art and technical models for content-addressed evidence, temporal provenance, and distributed persistence.

## The synthesis

ANARCHY's central proposition is that these layers can be connected through a common evidence and build model:

```text
HISTORICAL ARTIFACT
       ↓
IDENTITY / SOURCE
       ↓
REVISION + HASH
       ↓
LICENSE / NOTICE / TRADEMARK
       ↓
BUILD RECIPE
       ↓
REPRODUCIBLE ARTIFACT
       ↓
SBOM / PROVENANCE
       ↓
DECLARATIVE PROVISIONING
       ↓
LOCAL / DISTRIBUTED REPOSITORY
       ↓
DEPLOYMENT / RESTORE / TEST
       ↓
ARCHIVED RESULT
```

## Evidence discipline

The lineage is intentionally conservative:

- a historical artifact establishes that the artifact existed;
- a source repository establishes source lineage;
- a license establishes the rights it grants;
- a trademark policy establishes branding constraints;
- a technical similarity establishes a research lead;
- a direct document or transaction is required for a claim about sponsorship, ownership, or institutional control.

The repository should preserve uncertainty rather than convert it into fact.

## Why this matters to sponsors and grants

A sponsor does not need to understand every historical experiment. The lineage gives reviewers a way to see that the present architecture emerged from accumulated work across several engineering disciplines.

The public-facing narrative is therefore:

> **ANARCHY turns a long-running technical research record into a reproducible, provenance-aware, enterprise-ready open engineering framework for decentralized systems.**

The underlying evidence remains available for technical due diligence.
