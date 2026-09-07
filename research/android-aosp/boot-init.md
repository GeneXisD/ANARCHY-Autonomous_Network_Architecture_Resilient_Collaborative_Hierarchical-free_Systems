# AOSP boot and init

Android's early userspace and `init` are useful prior art for ANARCHY's node lifecycle model.

## Research targets

- bootloader → kernel → first userspace transition
- first-stage and second-stage initialization
- declarative service definitions
- filesystem setup and mounts
- property/configuration propagation
- service classes and lifecycle
- restart behavior
- triggers and dependency ordering
- recovery and failure handling

## ANARCHY interpretation

A node should have a small, deterministic bootstrap layer that can:

1. establish local identity;
2. verify its boot/configuration state;
3. mount or discover required local resources;
4. start minimum trusted services;
5. discover peers;
6. advertise capabilities;
7. reconcile desired state with locally available services.

The important departure from conventional centralized orchestration is that the node must remain useful when peer discovery fails. Bootstrap should therefore have a **local-first failure domain**.

## Design principle

Borrow the idea of declarative lifecycle and dependency ordering, but avoid making a global controller a prerequisite for boot or continued operation.
