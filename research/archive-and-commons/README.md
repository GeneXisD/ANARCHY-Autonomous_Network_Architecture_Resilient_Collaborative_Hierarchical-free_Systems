# ANARCHY Archive, Commons, and Research-Lineage Layer

**Status:** Research corpus / project lineage
**Date:** 2026-09-07

## Purpose

ANARCHY research must preserve not only operating-system and networking prior art, but also the user's own research artifacts and the archival infrastructure used to discover, verify, preserve, and replay that prior art.

This layer connects four related bodies of work:

1. **ML-ANE / BNNS / Core ML research** — accelerator, model-runtime, and Apple-platform interoperability work.
2. **Wayback / web-archiving infrastructure** — preservation and replay of historical web evidence.
3. **InterPlanetary Wayback (ipwb)** — content-addressed, peer-to-peer preservation and replay of WARC records using IPFS.
4. **Decentralized Commons Treaty** — governance, stewardship, interoperability, preservation, and community-commons concepts.

The repositories are **research inputs and project lineage**, not claims that their existing code is automatically an ANARCHY dependency.

## 1. ML-ANE / BNNS / Core ML

The user's `GeneXisD/ml-ane-transformers` repository contains the ongoing Apple Neural Engine research. The repository work includes BNNS/Accelerate integration, DistilBERT/Core ML compatibility and diagnostics, and experiments concerning execution of transformer workloads through Apple's available machine-learning interfaces.

Relevant lineage:

```text
Transformer models
       |
       v
Core ML / model representation
       |
       +---- BNNS / Accelerate
       |
       +---- Apple Neural Engine
       |
       v
hardware-aware execution
       |
       v
portable ML service/interface research
```

ANARCHY relevance:

- hardware abstraction
- accelerator-aware execution
- model portability
- runtime capability discovery
- separation between model description and execution backend
- open tooling around otherwise platform-specific hardware

The ANARCHY corpus should reference the ML-ANE work as a concrete example of the same architectural principle used elsewhere: **preserve a portable description while adapting execution to the local substrate.**

Repository: `GeneXisD/ml-ane-transformers`

## 2. Wayback Machine / web preservation

The Wayback Machine is important to ANARCHY because a large portion of the historical evidence being reconstructed exists only on changing or disappearing websites.

The archival model should therefore distinguish:

```text
LIVE WEB
   |
   v
capture / WARC
   |
   v
archival index
   |
   v
historical replay
   |
   v
ANARCHY provenance record
```

A historical URL alone is not sufficient evidence. Whenever possible, preserve:

- original URL
- capture timestamp
- archive URL
- WARC identifier
- retrieval date
- content hash
- repository/revision identifier
- license/copyright information
- notes describing what was actually verified

This is particularly important for old Launchpad blueprints, Linux & C. material, dyne:bolic/Puredyne documentation, obsolete package repositories, and historical installation systems.

## 3. InterPlanetary Wayback (ipwb)

`GeneXisD/ipwb` is a direct project-lineage artifact for decentralized archival preservation.

The project describes **InterPlanetary Wayback** as a system for disseminating WARC contents into IPFS. Its indexer extracts WARC/HTTP headers and payloads, places content-addressed pieces into IPFS, and generates a CDXJ index containing references used for replay. Its replay component reconstructs archived resources from the decentralized storage layer.

The project README also documents client-side Service Worker rewriting through the Reconstructive library to prevent archival resource requests from leaking back to the live web.

The conceptual model is:

```text
             WARC
              |
              v
          ipwb indexer
              |
       +------+------+
       |             |
   HTTP headers   payloads
       |             |
       +------+------+
              |
              v
             IPFS
              |
        content hashes
              |
              v
            CDXJ
              |
              v
         ipwb replay
              |
              v
        historical web
```

ANARCHY relevance:

- content-addressed storage
- distributed replication
- persistent archives
- offline-capable historical evidence
- decentralized indexes
- replay rather than merely static storage
- separation of archival content from the mechanism used to retrieve it
- provenance that can survive changes to the original web

This is highly relevant to the ANARCHY concept of **resilient knowledge infrastructure**.

Repository: `GeneXisD/ipwb`

## 4. ODU Web Science and Digital Libraries lineage

`GeneXisD/oduwsdl.github.io` is preserved as part of the user's research lineage because it represents the Web Science and Digital Libraries research environment associated with the archival work.

The repository README identifies it as the home page for the Web Science and Digital Libraries Research Group. The broader lineage connects web archives, WARC processing, Memento/replay concepts, digital libraries, and preservation research.

Repository: `GeneXisD/oduwsdl.github.io`

## 5. Decentralized Commons Treaty

`GeneXisD/Decentralized-Commons-Treaty` provides a governance and commons layer complementary to the technical ANARCHY research.

Its README defines a decentralized-web social contract and identifies principles including:

- interoperability first
- interest-neutral stewardship
- people-governed decision making
- transparency
- forkability
- iterative evolution
- preservation of history

It also identifies technical standards concerning CIDs, naming, storage, and identity, and describes public records for signatories, governance, RFCs, and meeting notes.

ANARCHY relevance:

```text
technical infrastructure
        +
provenance / preservation
        +
community governance
        +
interoperability
        +
forkability
        |
        v
resilient decentralized commons
```

This should be treated as **governance prior art / project lineage**, not as a legal conclusion or as proof that a particular governance model is legally enforceable.

Repository: `GeneXisD/Decentralized-Commons-Treaty`

## 6. Combined ANARCHY interpretation

The four bodies of work fit into a broader research architecture:

```text
                  ANARCHY RESEARCH
                         |
       +-----------------+------------------+
       |                 |                  |
   COMPUTE            PRESERVE          GOVERN
       |                 |                  |
    ML-ANE              Wayback          Commons
    BNNS                WARC             Treaty
    Core ML             ipwb             RFCs
       |                 |                  |
       +-----------------+------------------+
                         |
                         v
             RESILIENT KNOWLEDGE FABRIC
                         |
             +-----------+-----------+
             |                       |
       execution substrate     historical substrate
             |                       |
       local hardware          archived evidence
             |                       |
             +-----------+-----------+
                         |
                         v
                  ANARCHY NODE
```

The important architectural distinction is:

> **Execution, preservation, and governance are separate layers that can interoperate without becoming one monolithic system.**

## 7. Provenance rule for ANARCHY

When a discovery comes from one of these projects or from an archived source, ANARCHY should record the chain of evidence rather than only the final conclusion.

Recommended record:

```text
source_project:
source_repository:
source_url:
archive_url:
artifact_type:
version_or_revision:
commit_or_release:
capture_timestamp:
content_hash:
license_or_rights:
verified_claims:
inferences:
open_questions:
anarchy_relevance:
```

Claims should be labeled as one of:

- **verified** — directly supported by the artifact
- **historical** — supported by dated archival evidence
- **derived** — an architectural interpretation of verified evidence
- **hypothesis** — plausible but requiring additional evidence
- **unresolved** — source or artifact has not yet been recovered

## 8. Relationship to existing ANARCHY research

This layer should cross-reference, rather than replace:

- `research/open-stack-ecosystem-map.md`
- `research/installation-and-distribution-model.md`
- `research/packaging/emerge-portage.md`
- `research/cygwin/rhcygwin.md`
- AOSP research
- Puredyne / dyne:bolic research
- Launchpad / Bouillon Cube research
- openSUSE / YMP research
- XAMPP research
- Linux & C. historical research
- terminal / PTY research

Together these establish a broader pattern:

```text
                  DESCRIPTION
                      |
        +-------------+-------------+
        |             |             |
     execution    installation   governance
        |             |             |
     ML/runtime    YMP/live       Treaty
        |          installers        |
        +-------------+-------------+
                      |
                   NODE STATE
                      |
                 provenance
                      |
                 WARC / IPFS
                      |
                 historical
                   replay
```

The resulting research direction is not simply a new Linux distribution. It is investigation into a **composable, administrator-controlled, resilient computing and knowledge architecture** in which software, installation intent, execution backends, archival evidence, and governance records remain independently addressable and verifiable.

## 9. Primary project references

- `GeneXisD/ml-ane-transformers`
- `GeneXisD/ipwb`
- `GeneXisD/oduwsdl.github.io`
- `GeneXisD/Decentralized-Commons-Treaty`

These repositories should be pinned by commit/release when a particular claim is incorporated into a formal ANARCHY specification.
