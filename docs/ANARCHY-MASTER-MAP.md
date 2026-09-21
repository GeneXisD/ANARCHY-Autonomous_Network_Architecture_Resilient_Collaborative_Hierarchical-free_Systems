# ANARCHY — Master Architecture Map

## One project, multiple layers

```text
                         ANARCHY
                            │
       ┌────────────────────┼──────────────────────────────┐
       │                    │                              │
       ▼                    ▼                              ▼
   25-YEAR              ENGINEERING                    EVIDENCE
   CORPUS                PLATFORM                       SYSTEM
       │                    │                              │
       │              ┌─────┼─────┐                        │
       │              │     │     │                        │
       ▼              ▼     ▼     ▼                        ▼
 Dynebolic         Build  Restore Provision             Provenance
 Puredyne          Linux  Apple   YMP/XAMPP              SPDX/SBOM
 RHCygwin          Kernel iDevice Local repo             Hashes
 X11               crosstool Android RitualMesh          Notices
 XAMPP             tooling  tooling 127.0.0.1            Evidence
 openSUSE          Ant     packaging
 Linux&C            toolchains
 Apache/PHP
 Tomcat
       │
       ▼
  NETWORK RESILIENCE PLANE
       │
       ├── Netsukuku / P2P Layer-3 research
       ├── QSPN routing concepts
       ├── Physical / local mesh
       ├── OpenWrt / embedded nodes
       ├── Internet gateway when available
       └── Independent local/regional operation
```

## Network resilience plane

ANARCHY treats decentralized networking as an **additional communications and distribution layer**, not as a claim that the conventional Internet must be replaced.

Netsukuku is an important historical technical predecessor. Its published QSPN document describes the goal as a physical, scalable, distributed and decentralized mesh network, designed to run on low-resource devices such as access points, embedded systems and older computers. It explicitly describes a network capable of operating separately from conventional Internet infrastructure. The current Netsukuku source page identifies C, Python and Vala implementations and states that the Vala implementation can run on OpenWrt routers.

Source:
- https://netsukuku.freaknet.org/sourcecode.html
- https://netsukuku.freaknet.org/doc/main_doc/qspn.pdf

### Architectural relationship

```text
                    CONVENTIONAL INTERNET
               ┌───────────────────────────┐
               │ ISP / BGP / DNS / Cloud   │
               │ Telecom / Data Centers    │
               └─────────────┬─────────────┘
                             │
                      Internet Gateway
                             │
               ┌─────────────▼─────────────┐
               │       ANARCHY OVERLAY      │
               │ routing / identity /      │
               │ discovery / distribution  │
               └─────────────┬─────────────┘
                             │
                  ┌──────────▼──────────┐
                  │   PHYSICAL MESH     │
                  │ Wi-Fi / Ethernet /  │
                  │ OpenWrt / embedded  │
                  │ legacy computers     │
                  └─────┬─────┬─────┬───┘
                        │     │     │
                      NODE  NODE  NODE
                        │     │     │
                    LOCAL / REGIONAL
                    PEER CONNECTIVITY
```

### Design principle

**Internet availability and mesh availability are complementary states.**

```text
                 ┌──────────────────────┐
                 │     ANARCHY NODE      │
                 └──────────┬───────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
       Conventional path             Mesh path
       ISP / Internet                Peer / local
              │                           │
              └─────────────┬─────────────┘
                            ▼
                    Service / Artifact
                    / Identity / Route
```

When upstream Internet connectivity exists, nodes can use it. When an upstream path is unavailable, the architecture can preserve local or regional communications and distribution through participating peers, subject to physical connectivity, node availability, routing convergence, and the capabilities of the deployed protocols.

This is a **resilience architecture**, not a guarantee of nationwide connectivity.

## Netsukuku technical lineage

The Netsukuku QSPN paper describes a routing-discovery system based on tracer packets and hierarchical grouping. It also documents mechanisms for handling changed, new and broken links through Extended Tracer Packets. These concepts are relevant to ANARCHY as historical research and as candidate design patterns; they should not be represented as proof that an ANARCHY deployment has already achieved the theoretical scale described in the paper.

Important documented limitations include the original assumption that nodes are relatively stationary and that network-wide route updates can take several minutes. The paper notes that mobility can instead be addressed by combining Netsukuku with other mesh protocols designed for mobile nodes.

### Historical lineage

```text
Freaknet / Dyne ecosystem
          │
          ├── Netsukuku
          │      ├── P2P Layer-3 routing
          │      ├── QSPN
          │      ├── distributed route discovery
          │      └── mesh-network research
          │
          └── Dyne:bolic / free-software ecosystem
                 │
                 ├── bootable computing environments
                 ├── decentralized / community tooling
                 └── reproducible distribution research
                                │
                                ▼
                            ANARCHY
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
          Networking        Computing        Distribution
          Netsukuku           AOSP          Dyne / PureDyne
          mesh routing      toolchains       repositories
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ▼
                    Decentralized Commons
```

The lineage is historical and technical. It does **not** imply that the original projects endorse ANARCHY or that their implementations can be reused without checking their respective licenses and provenance.

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
          ↓
   MESH TRANSPORT WHEN
   UPSTREAM IS UNAVAILABLE
```

Decentralization changes the transport and persistence model; it does not erase upstream licensing obligations.

## Resilience model

The project should distinguish five different properties:

1. **Internet independence** — whether a function can continue without an upstream ISP path.
2. **Local survivability** — whether participating nodes can continue communicating inside a local mesh.
3. **Regional survivability** — whether multiple local meshes can remain connected through surviving peers.
4. **Artifact persistence** — whether software, documentation and provenance remain available from replicated nodes.
5. **Recovery interoperability** — whether conventional Internet connectivity can be restored and reintegrated without destroying the decentralized layer.

```text
                    FAILURE / DISRUPTION
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
       Internet path lost          Individual node lost
             │                           │
             ▼                           ▼
       Mesh path remains           Route recalculation
             │                           │
             └─────────────┬─────────────┘
                           ▼
                 LOCAL / REGIONAL SERVICE
                           │
                           ▼
                  RECONNECT WHEN READY
```

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

## Security and resilience boundary

ANARCHY should not describe decentralization as automatically secure.

A mesh can reduce dependence on centralized infrastructure while introducing or preserving other risks, including:

- compromised nodes;
- malicious routing information;
- identity spoofing;
- partitioned networks;
- RF interference;
- physical node loss;
- stale route information;
- supply-chain compromise;
- malicious or corrupted artifacts.

Therefore the network layer must remain paired with **cryptographic identity, authenticated routing where supported, artifact signatures, hashes, provenance, revocation, and evidence preservation**.

The architectural rule is:

> **Redundancy of transport is not the same thing as trustworthiness of content.**

## Historical-to-future bridge

The 25-year record is the input corpus. The ANARCHY engineering platform is the transformation layer. RitualMesh is the decentralized orchestration/distribution layer. Netsukuku provides an important historical reference for the independent routing layer.

```text
HISTORY
  ↓
EVIDENCE
  ↓
REPRODUCIBILITY
  ↓
ENGINEERING
  ↓
NETWORK RESILIENCE
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

## Evidence status

The Netsukuku material cited here is **historical primary-source evidence about the Netsukuku project and its documented design**, not evidence that ANARCHY has already implemented or validated Netsukuku.

Current ANARCHY status should therefore distinguish:

- **Confirmed:** Netsukuku has published implementations and technical documentation.
- **Confirmed:** The QSPN documentation describes decentralized physical mesh routing.
- **Confirmed:** The Vala implementation is documented as running on OpenWrt.
- **Proposed:** Netsukuku-derived concepts can inform ANARCHY's network-resilience layer.
- **Unvalidated:** Nationwide or continental ANARCHY mesh deployment.
- **Unvalidated:** Security properties of a modern ANARCHY/Netsukuku-derived implementation.
- **Required:** Modern hardware, RF, routing, identity, security and recovery testing before making deployment-scale claims.

This distinction preserves the project's provenance while allowing historical work to become a foundation for new engineering.
