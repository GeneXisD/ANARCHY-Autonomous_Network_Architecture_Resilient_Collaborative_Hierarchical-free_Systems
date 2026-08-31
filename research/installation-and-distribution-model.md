# ANARCHY Installation & Distribution Model

**Status:** Research / prior-art synthesis  
**Date:** 2026-08-31

## Purpose

This document records a line of investigation developed while studying historical GNU/Linux live systems, Puredyne, dyne:bolic, Bouillon Cube, and openSUSE installation technologies.

The goal is **not** to claim that any of these projects are ANARCHY components. They are recorded as prior art, reference implementations, and architectural evidence from which an ANARCHY installation/distribution model can be studied.

The ANARCHY repository explicitly distinguishes third-party references from ANARCHY-original work. This document follows that distinction.

## Architectural question

How can a live, distributed, heterogeneous GNU/Linux environment describe and reproduce an installation without making the installer itself the only source of truth?

A useful working model is:

```text
             LIVE / EXISTING SYSTEM
                       |
                       | inspect / describe
                       v
              INSTALL GENERATOR
                       |
                       v
            INSTALLATION DESCRIPTION
                       |
             +---------+---------+
             |                   |
       repositories          packages/patterns
             |                   |
             +---------+---------+
                       |
                       v
                INSTALL BACKEND
                       |
              +--------+--------+
              |                 |
           target FS        boot/config
              |                 |
              +--------+--------+
                       |
                       v
                 REPRODUCED OS
```

The important architectural separation is between **description** and **execution**.

An installation description can potentially be translated to different package managers or installation backends, while the backend remains responsible for the platform-specific mechanics.

## 1. Bouillon Cube: `live-install-generator`

Historical reference:

https://blueprints.launchpad.net/bouilloncube/+spec/live-install-generator

The Launchpad blueprint is being treated here as historical prior art concerning a **live-install generator**: an approach in which a running/live environment and its configuration can be used as the basis for generating or performing an installation.

Launchpad access to the original blueprint may be restricted today, so claims about its exact implementation should be verified against archived source, project revisions, or recovered package/source artifacts before being treated as implementation facts.

### Research significance

The key architectural idea worth preserving is the transition:

```text
live environment
      |
      v
installation generator
      |
      v
target installation
```

This is particularly relevant to the historical Puredyne/dyne:bolic investigation because those systems demonstrate that a distribution can be assembled as a live environment rather than beginning with a conventional installed system.

## 2. openSUSE One Click Install

Primary reference:

https://en.opensuse.org/openSUSE:One_Click_Install

The openSUSE One Click Install model provides another useful abstraction: an installation action can be represented by a machine-readable instruction/recipe rather than embedding the software itself in the launcher.

The historical YMP (YaST Meta Package) approach describes repositories and packages to install and allows installation instructions to be interpreted by an installation handler.

The resulting conceptual pipeline is:

```text
             YMP / installation recipe
                       |
          +------------+------------+
          |                         |
      repositories              packages
          |                         |
          +------------+------------+
                       |
                       v
                YaST / zypper
                       |
                       v
                  installed OS
```

This suggests a general design principle:

> **Keep the installation intent separate from the mechanism that executes the installation.**

That principle is potentially more important to ANARCHY than the historical YMP format itself.

## 3. Cross-distribution interpretation

A particularly useful property of a declarative installation description is that it can act as an intermediate representation.

```text
                 INSTALL INTENT
                      |
                      v
             MACHINE-READABLE IR
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
      apt           zypper       custom backend
        |             |             |
        +-------------+-------------+
                      |
                      v
                TARGET SYSTEM
```

The installation description does not need to dictate one package manager.

Instead, an implementation can translate the same intent into platform-specific operations.

Potential fields include:

- repository identifiers
- package identifiers
- package groups/patterns
- architecture constraints
- release/distribution constraints
- configuration requirements
- filesystem requirements
- boot requirements
- cryptographic hashes
- signatures/provenance
- licensing metadata
- dependency information
- optional capabilities/features

## 4. Connection to Puredyne and dyne:bolic research

The current historical investigation has exposed several different layers that should not be collapsed into one system:

```text
SOURCE / PACKAGE CORPUS
        |
        v
DISTRIBUTION ASSEMBLY
        |
        v
LIVE FILESYSTEM
        |
        +----> LIVE BOOT
        |
        +----> INSTALL GENERATION
        |
        v
TARGET FILESYSTEM
        |
        v
BOOT + CONFIGURATION
```

Puredyne and dyne:bolic are valuable historical reference points because they demonstrate distribution designs where the live environment itself is a first-class artifact.

The Bouillon Cube `live-install-generator` reference is useful for studying how that live artifact can become an installed system.

The openSUSE One Click Install model is useful for studying how installation intent can be represented separately from the installer implementation.

Together, these references suggest a broader ANARCHY research direction:

```text
        DISTRIBUTION ARTIFACT
                 |
        +--------+--------+
        |                 |
       LIVE          INSTALL DESCRIPTION
        |                 |
        |                 v
        |          INSTALL BACKENDS
        |          /      |       \
        |        apt    zypper    other
        |          \      |       /
        +-----------+-----+------+
                    |
                    v
              TARGET SYSTEM
```

## 5. ANARCHY interpretation

This research does **not** propose copying YMP, YaST, Puredyne, dyne:bolic, or Bouillon Cube.

Instead, it identifies an architectural pattern that may be suitable for ANARCHY:

### Installation intent

A node should be able to describe what it requires without necessarily prescribing one centralized installation mechanism.

### Translation

A local installation agent should translate that intent into the mechanisms available on the node.

### Provenance

The resulting installation should retain provenance describing where the requested artifacts came from, which revisions were selected, and which licenses apply.

### Reproducibility

The installation description should be capable of being recorded, hashed, signed, archived, and replayed.

### Resilience

Repository and package sources should not necessarily depend on a single permanent server. Multiple equivalent sources can satisfy the same content requirement when their provenance and integrity can be verified.

### Heterogeneity

Different nodes may use different operating systems, architectures, package managers, or boot mechanisms while still participating in the same higher-level installation-description model.

## 6. Proposed ANARCHY abstraction

A future ANARCHY installation descriptor could conceptually look like:

```yaml
schema: anarchy.install/v0
identity:
  name: example-node
  architecture: amd64
sources:
  - id: primary
    type: repository
    uri: <repository-uri>
requirements:
  packages:
    - example-package
  capabilities:
    - networking
    - mesh
constraints:
  filesystem: linux
provenance:
  source_revision: <revision>
  content_hash: <hash>
  license: <SPDX-expression>
execution:
  backend: auto
```

This is intentionally a **conceptual research schema**, not an implementation specification.

The important property is that `requirements`, `sources`, `provenance`, and `execution` remain separable.

## 7. Relationship to ANARCHY provenance

The repository's existing provenance model is:

```text
AUTHOR
    ↓
ARTIFACT
    ↓
REVISION
    ↓
HASH
    ↓
LICENSE
    ↓
DERIVATIVE
    ↓
DISTRIBUTION
```

Installation descriptors fit naturally into this chain because an installation is itself a distribution event derived from identified artifacts.

A mature implementation could therefore record:

```text
installation descriptor
        |
        +--> source repository
        +--> package/artifact
        +--> exact revision
        +--> content hash
        +--> license metadata
        +--> local transformation
        +--> installation result
```

This provides a path toward auditable, reproducible installation without requiring every node to run identical software.

## 8. References

1. **Launchpad — Bouillon Cube `live-install-generator` blueprint**  
   https://blueprints.launchpad.net/bouilloncube/+spec/live-install-generator

2. **openSUSE Wiki — One Click Install**  
   https://en.opensuse.org/openSUSE:One_Click_Install

3. **openSUSE — One Click Install presentation / historical material**  
   https://en.opensuse.org/images/b/b0/OneClickInstallFosdemTalk.pdf

4. **ANARCHY repository**  
   https://github.com/GeneXisD/ANARCHY-Autonomous_Network_Architecture_Resilient_Collaborative_Hierarchical-free_Systems

## Classification

| Reference | ANARCHY classification |
|---|---|
| Bouillon Cube `live-install-generator` | Historical evidence / prior art |
| openSUSE One Click Install | Prior art / reference implementation |
| YMP concept | Related technology / prior art |
| Puredyne | Historical evidence / reference implementation |
| dyne:bolic | Historical evidence / reference implementation |
| Proposed ANARCHY installation descriptor | ANARCHY research concept |

## Research note

The central hypothesis emerging from this work is:

> **A resilient distribution architecture should treat the operating-system image, installation intent, execution backend, and provenance record as distinct but composable artifacts.**

That separation may allow an installation model to move between live systems, installed systems, package ecosystems, architectures, and autonomous network nodes without requiring one monolithic installer to control the entire process.
