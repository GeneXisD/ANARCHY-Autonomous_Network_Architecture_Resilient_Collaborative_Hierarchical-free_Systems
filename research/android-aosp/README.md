# Android / AOSP Research

AOSP = Android Open Source Project.

ANARCHY should treat AOSP as a **reference architecture**, not as a code dependency or as a decentralized system in itself. The useful question is how AOSP decomposes a large operating environment into interfaces, services, security boundaries, hardware abstractions, update domains, and build/provenance layers that can be reinterpreted for a resilient, collaborative, hierarchical-free architecture.

## Research tracks

- System architecture and layer boundaries
- Linux kernel / Android Common Kernel
- boot and `init`
- Binder IPC and service discovery
- system services and service managers
- ART and application/runtime isolation
- HAL and hardware abstraction
- Treble / stable vendor interfaces
- Project Mainline / modular system components
- SELinux / mandatory access control
- permissions, identities, capabilities, and sandboxing
- networking and connectivity services
- package/update mechanisms and rollback concepts
- Soong / Blueprint / build graph
- repo/Git/Gerrit and multi-repository source management
- reproducible builds, manifests, provenance, and supply-chain integrity
- licensing and component boundaries

## ANARCHY relevance

AOSP is especially valuable as a study of **federated complexity inside a single platform**. ANARCHY can borrow the architectural patterns while changing the authority model:

| AOSP concept | ANARCHY research question |
|---|---|
| Binder IPC | Can service-to-service messaging work across autonomous nodes? |
| `init` | Can node-local orchestration be declarative without a central controller? |
| HAL | Can hardware capabilities be exposed as portable, discoverable interfaces? |
| Treble | Can stable interfaces let independently maintained node components interoperate? |
| Mainline | Can critical services be updated independently without rebuilding the whole system? |
| SELinux | Can policy be distributed and locally enforceable while preserving interoperability? |
| Package/update system | Can updates be content-addressed, signed, replicated, and rollback-safe? |
| repo/Git/Gerrit | Can a distributed source federation preserve provenance without one mandatory forge? |
| Soong/Blueprint | Can dependency graphs become portable build descriptions across nodes? |

## Files

- `architecture.md` — AOSP layer model and ANARCHY translation.
- `ipc-services.md` — Binder, service boundaries, discovery, and distributed analogues.
- `boot-init.md` — boot, `init`, property/configuration flow, and node orchestration implications.
- `hal-treble-mainline.md` — hardware abstraction, Treble, and modular system updates.
- `security-identity.md` — SELinux, UID/package identity, permissions, sandboxing, and policy implications.
- `build-provenance.md` — repo, manifests, Soong/Blueprint, Git/Gerrit, reproducibility, and provenance.
- `networking.md` — Android networking architecture and implications for autonomous nodes.

## Primary sources

- https://source.android.com/
- https://source.android.com/docs/core/architecture
- https://source.android.com/docs/core/architecture/kernel
- https://android.googlesource.com/

## Evidence rule

Do not copy the AOSP source tree into ANARCHY. Record architectural observations, links, version/date, relevant source paths, and licensing/provenance information. When a design claim depends on a particular Android release, record the release/branch explicitly.
