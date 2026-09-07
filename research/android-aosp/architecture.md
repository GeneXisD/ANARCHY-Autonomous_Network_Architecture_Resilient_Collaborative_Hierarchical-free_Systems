# AOSP architecture → ANARCHY

## Why this belongs in ANARCHY

AOSP demonstrates how a very large operating platform can be decomposed into layers with explicit interfaces. ANARCHY can study those boundaries while replacing centralized ownership assumptions with autonomous nodes and federated coordination.

## Layers worth modeling

1. Bootloader / firmware boundary
2. Linux kernel / Android Common Kernel
3. Hardware abstraction and vendor interfaces
4. Native userspace and libraries
5. Android Runtime (ART)
6. Binder IPC
7. system services / framework
8. application framework and apps
9. update, package, and configuration domains

## ANARCHY translation

The key architectural primitive is not the Android application. It is the **interface boundary**. A node should be able to replace an implementation while preserving a declared protocol, capability contract, identity model, and provenance record.

A useful ANARCHY node model is:

```text
hardware
   ↓
local kernel / drivers
   ↓
capability adapters (HAL-like)
   ↓
local services
   ↓
node IPC / message fabric
   ↓
application + distributed services
   ↓
peer discovery / federation
```

Unlike AOSP, the upper layers should not require a single global authority. A peer may disappear, fork, migrate, or be replaced without destroying the rest of the network.

## Research questions

- Which interfaces are genuinely stable versus implementation-specific?
- Which services can become independently replicated actors?
- What state must remain local?
- What state can be replicated or eventually consistent?
- How should capability advertisement work?
- How can a node reject incompatible or untrusted peers locally?
- What is the minimum common protocol needed for heterogeneous nodes?
