# AOSP IPC and services

## Binder as a reference pattern

Android uses Binder as a central IPC mechanism for communication between processes and framework/system services. For ANARCHY, the interesting abstraction is **typed service communication across trust and lifecycle boundaries**, not Binder itself.

## Questions for ANARCHY

- Can local IPC and remote peer messaging share a common service model?
- Can service endpoints be discovered without a permanent central registry?
- Can service identity be cryptographically bound to a key rather than a machine address?
- Can requests carry capability constraints and provenance?
- How are timeouts, retries, replay protection, and duplicate requests handled?
- How can a service migrate from one node to another?
- What happens when two peers provide incompatible implementations?

## Proposed ANARCHY abstraction

```text
service identity
   + capability declaration
   + protocol/version
   + endpoint(s)
   + trust/provenance metadata
   + health/liveness
   + policy constraints
```

A local transport may be Unix sockets, shared memory, Binder-like IPC, or another mechanism. A remote transport may be QUIC, TCP, mesh routing, or an ANARCHY-specific transport. The protocol contract should be independent of the transport.

## Important distinction

Binder should be documented as **prior art**. ANARCHY should not assume that a single system-wide service manager or privileged broker is available across the federation.
