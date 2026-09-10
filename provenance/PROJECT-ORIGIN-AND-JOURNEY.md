# ANARCHY — Project Origin and Long-Term Journey

**Status:** Living provenance record  
**Project steward / claimed author:** Victor Jose Corral  
**Project identity:** GeneXisD  
**Repository:** `GeneXisD/ANARCHY-Autonomous_Network_Architecture_Resilient_Collaborative_Hierarchical-free_Systems`

## Purpose of this record

This document records the human and technical origin of the ANARCHY project alongside the repository's machine-verifiable history.

It intentionally separates **personal motivation**, **authorship claims**, **technical evidence**, and **legal rights**. A personal statement can explain why a project exists without proving ownership of every technology referenced by that project.

## Origin

ANARCHY grew from a long-running effort to understand how computers, operating systems, networking, distributed systems, archives, software repositories, and open-source technologies can be combined into systems that remain resilient, collaborative, interoperable, and less dependent on a permanent centralized hierarchy.

The project is organized around the question:

> How can technical systems preserve autonomy, resilience, collaboration, interoperability, and traceability while remaining accountable to verifiable evidence?

The project treats the repository itself as part of the answer: ideas become artifacts; artifacts become revisions; revisions receive hashes; sources and licenses are recorded; experiments are documented; and later readers can distinguish original work from prior art and third-party technology.

## Personal motivation and dedication

The author records this work as a lifelong technical journey and as a legacy project motivated in significant part by his son, **Ian Patrick Corral**, born June 4, 2000, in Las Vegas, Nevada.

The dedication expresses the personal reason for preserving the work. It is not a claim that Ian authored, owns, endorsed, or participated in any specific technical artifact unless a separate record establishes such a contribution.

## Authorship boundary

The ANARCHY repository may contain or reference:

- original research and engineering by the project author;
- original project documentation;
- experiments and prototypes;
- third-party open-source software;
- standards and specifications;
- academic publications;
- historical artifacts;
- archived evidence;
- institutional documentation;
- compatibility references;
- derivative or modified works;
- hypotheses requiring further verification.

These categories must remain separate.

**ANARCHY does not claim ownership merely because an external artifact is documented here.**

Likewise, documenting a technical relationship does not establish sponsorship, employment, institutional control, common authorship, or legal ownership.

## Technical journey

The project corpus reflects a progression through multiple layers of computing and networking research, including:

```text
OPERATING SYSTEMS
      ↓
SOFTWARE / SOURCE CODE
      ↓
VERSION CONTROL
      ↓
NETWORKING
      ↓
DISTRIBUTED SYSTEMS
      ↓
MESH / PEER-TO-PEER SYSTEMS
      ↓
ARCHIVING / DIGITAL PRESERVATION
      ↓
CONTENT-ADDRESSABLE STORAGE
      ↓
IDENTITY / TRUST / PROVENANCE
      ↓
REPRODUCIBLE VALIDATION
      ↓
KNOWLEDGE TRANSFER
      ↓
COMMERCIALIZATION / DEPLOYMENT
```

The repository's research areas and linked projects are evidence of this technical exploration. Each external project remains separately attributable to its documented authors and license.

## Provenance as infrastructure

The central insight behind the provenance work is that **traceability should survive movement**.

An artifact may move:

```text
AUTHOR
  → LOCAL MACHINE
  → GIT REPOSITORY
  → FORK
  → PATCH
  → DISTRIBUTION
  → DEPLOYMENT
  → ARCHIVE
  → DERIVATIVE
  → NEW REPOSITORY
```

The provenance record should make those transitions visible without pretending that every transition has the same legal meaning.

## Repository evidence

The strongest evidence for ANARCHY's technical development is its own Git history, including commits, branches, files, revisions, and release records. Those records should be preserved rather than replaced by a retrospective narrative.

The repository currently maintains multiple provenance-oriented records under `provenance/`, `docs/provenance/`, `docs/research/`, `research/provenance/`, and `evidence/software-provenance/`.

These records include software provenance, historical migration research, open-source licensing research, network-provenance studies, configuration audits, and source bundles.

## Current provenance architecture

```text
                 ANARCHY PROJECT
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       AUTHOR       ARTIFACT      SOURCE
          │            │            │
          └────────────┼────────────┘
                       ▼
                  REVISION
                       │
                       ▼
                     HASH
                       │
                       ▼
               LICENSE / RIGHTS
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
         VALIDATION          DERIVATIVE
             │                   │
             └─────────┬─────────┘
                       ▼
                  DISTRIBUTION
                       │
                       ▼
                    USE
                       │
                       ▼
                  OBSERVATION
                       │
                       ▼
                    ARCHIVE
```

## Historical evidence policy

When a new artifact is discovered, the project should record:

1. what the artifact is;
2. where it was found;
3. who is identified as its author or owner;
4. its original repository/publication when available;
5. version, release, commit, or hash;
6. license and copyright notices;
7. relevant dates;
8. any modifications made for ANARCHY;
9. evidence supporting the record;
10. unresolved uncertainty.

## The Apache/Tomcat configuration evidence class

A configuration artifact supplied for current provenance work contains the Apache License 2.0 header and a Tomcat `<Context>` element with a watched `WEB-INF/web.xml` resource plus commented session-persistence and Comet-related configuration examples.

This artifact is classified as **third-party configuration/reference evidence unless an independent source establishes a different origin**.

Its contents demonstrate Tomcat context configuration concepts. They do not, by themselves, prove an authorization system, ownership relationship, sponsorship relationship, or authorship by ANARCHY.

The exact source path, upstream release, commit, and hash should be added when those facts are recovered from the original distribution.

## What this record does not claim

This document does not claim that:

- every referenced technology was invented by ANARCHY;
- every related organization collaborated with ANARCHY;
- technical similarity proves common authorship;
- historical proximity proves causation;
- government or institutional references prove sponsorship;
- a license grants patent or trademark rights automatically;
- open-source software is ownerless;
- an archive record proves the legal status of an artifact;
- a personal dedication creates an intellectual-property transfer.

## Future preservation

Future updates should append evidence rather than erase inconvenient history. Corrections should identify the earlier statement, the new evidence, and the reason for the correction.

Where possible, each major milestone should have:

```text
DATE
AUTHOR
ARTIFACT
REPOSITORY
COMMIT / HASH
LICENSE
TEST RESULT
EVIDENCE
NOTES / UNCERTAINTY
```

That structure is intended to make the project understandable years later by someone who was not present for its creation.

## Long-term objective

The objective is not merely to preserve source code. It is to preserve the **chain by which knowledge became source code**, including experiments, failed approaches, successful implementations, external references, legal boundaries, and reproducible evidence.

That is the provenance standard ANARCHY should continue to build toward.
