# ClearingHouse / CRSH — ANARCHY Research Lineage

**Status:** Project architecture / research reference
**Date:** 2026-09-07

## Purpose

ClearingHouse (CRSH) is part of the broader RitualMesh → ANARCHY research lineage. It represents the **clearing, netting, accounting, and federated coordination layer** rather than the underlying transport or operating system.

The purpose of preserving this work in ANARCHY is to keep distinct:

- decentralized network transport,
- federation/order routing,
- clearing and replicated state,
- token/accounting records,
- and eventual external settlement interfaces.

This is an architectural research record, not a claim that ANARCHY is a financial institution, payment system, or replacement for regulated settlement infrastructure.

## 1. Relationship to RitualMesh

```text
                         RITUALMESH
                              |
                     decentralized mesh
                              |
                              v
                    federation / broker node
                              |
                    +---------+---------+
                    |                   |
              validation            routing
                    |                   |
                    +---------+---------+
                              |
                              v
                         CRSH / CLEARING
                              |
                 replicated clearing state
                              |
                 +------------+------------+
                 |                         |
          token/accounting          netting records
                 |                         |
                 +------------+------------+
                              |
                              v
                    external settlement
                    adapters / interfaces
```

The important boundary is that **clearing is not the same thing as transport**. A mesh can carry messages without being the authority for the application state those messages represent.

## 2. Ubuntu 14.04 / Trusty reference node

The earlier RitualMesh design used an Ubuntu 14.04 (Trusty) environment as a historical/reference runtime for a federated node.

Its modeled role was a broker/order-routing layer capable of receiving signed records, validating signatures, matching or routing orders/messages, calculating applicable fees according to system rules, forwarding clearing records to CRSH, and maintaining replicated node history.

Ubuntu 14.04 is therefore an **implementation/reference environment**, not the protocol itself and not a requirement that future ANARCHY nodes run that release.

The security model should be based on cryptographic identity and verifiable replicated state, not on the age or branding of the underlying Linux distribution.

## 3. Clearing state

CRSH was investigated as the decentralized clearing/netting ledger and experimental token/accounting layer.

```text
TRANSACTION / ORDER
        |
        v
 validation
        |
        v
 matching / netting
        |
        v
 clearing record
        |
        +----> replicated ledger/history
        |
        +----> token/accounting state
        |
        v
 settlement interface
```

This separation allows the network substrate to remain independent of the application-specific state machine operating above it.

## 4. Token and accounting model

The ClearingHouse research includes an experimental token/accounting concept. In ANARCHY documentation this should be described as a **research ledger/accounting layer** unless a specific implementation and legal/regulatory model establishes otherwise.

A useful abstract state model is:

```text
identity
   |
   +--> account
           |
           +--> balance/state
           |
           +--> signed transactions
           |
           +--> clearing obligations
           |
           +--> settlement status
```

The ledger should distinguish between authorization, transaction submission, clearing, net obligation, final settlement, and historical audit/provenance.

## 5. Why this belongs in ANARCHY

ClearingHouse contributes an example of **application state distributed over resilient infrastructure**.

```text
                 APPLICATION STATE
                        |
                 ClearingHouse/CRSH
                        |
              state machine / records
                        |
             cryptographic identity
                        |
                 federation layer
                        |
                  mesh transport
                        |
              heterogeneous OS nodes
```

This parallels other ANARCHY research:

- AOSP separates services and IPC from hardware implementation.
- Portage separates package intent/dependency metadata from build execution.
- openSUSE YMP separates installation intent from the installer backend.
- Cygwin separates a compatibility interface from the Windows substrate.
- ipwb separates archival indexes/replay from content-addressed storage.
- ML-ANE work separates model/runtime intent from accelerator-specific execution.
- ClearingHouse separates application/economic state from the network carrying it.

## 6. Provenance and auditability

Clearing records should be treated as provenance-bearing objects.

Recommended fields include:

```text
record_id
previous_record / dependency references
originating_node
identity / public-key reference
timestamp
operation type
input references
resulting state transition
signature
protocol/version
content hash
replication status
settlement status
```

The exact schema remains an implementation question. The principle is that a node should be able to demonstrate what state transition occurred, who authorized it, which prior state it depended on, and how the record was replicated.

## 7. Relationship to archival infrastructure

The ClearingHouse layer connects naturally to the Wayback/ipwb research already preserved in ANARCHY.

```text
ClearingHouse records
        |
        v
canonical export / WARC / structured archive
        |
        v
content-addressed preservation
        |
        v
IPFS / archival replicas
        |
        v
historical replay + provenance
```

Historical protocol records, node manifests, software releases, and governance decisions can themselves become archival artifacts. This provides an archival history independent of the availability of a particular web server or Git repository.

## 8. Governance boundary

ClearingHouse should remain technically distinct from the Decentralized Commons Treaty governance layer.

```text
GOVERNANCE
  Treaty / RFCs / community process
                 |
                 v
PROTOCOL RULES
                 |
                 v
CLEARING STATE
  CRSH state machine / records
                 |
                 v
NETWORK
  RitualMesh / federated nodes
                 |
                 v
SUBSTRATE
  Linux / hardware / transport
```

A governance document can specify rules without itself being the ledger. Likewise, a ledger can record state without becoming the governance process that determines future protocol rules.

## 9. Research cautions

Do not state that ClearingHouse provides legal finality, regulated settlement, banking functionality, or guaranteed monetary value without independent evidence establishing those claims.

Do not conflate:

- token issuance with settlement,
- clearing with payment finality,
- federation with decentralization,
- replicated records with legal records,
- or cryptographic validity with legal validity.

## 10. ANARCHY architectural lesson

The strongest reusable idea from the ClearingHouse work is separation of **transport, federation, application state, and settlement**.

```text
        WHAT IS SENT?
             |
          transport
             |
        WHO ROUTES IT?
             |
         federation
             |
        WHAT STATE CHANGES?
             |
       application ledger
             |
        WHAT IS OWED?
             |
           clearing
             |
        WHAT IS FINAL?
             |
          settlement
```

That layered model belongs beside ANARCHY's installation, packaging, device-interoperability, archival, and ML-runtime research.

## 11. Status

This document records the ClearingHouse concept as part of the user's RitualMesh/ANARCHY research lineage. Specific protocol schemas, source implementations, cryptographic formats, and settlement integrations should be added only when the corresponding artifacts are recovered and verified.
