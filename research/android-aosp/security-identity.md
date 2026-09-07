# AOSP security, identity, and policy

AOSP is useful to ANARCHY because it combines multiple security boundaries: Linux credentials, application identities, permissions, sandboxing, SELinux mandatory access control, and cryptographic trust anchors.

## Research areas

- Linux UID/GID and process isolation
- Android package/application identity
- permission model
- SELinux domains and policy
- keystore / hardware-backed key concepts
- sandboxing
- service permissions and IPC authorization
- verified boot and integrity chains
- update signing and rollback protection

## ANARCHY translation

ANARCHY should distinguish at least four identities:

1. **Node identity** — cryptographic identity of a participating machine/node.
2. **Service identity** — identity of an independently replaceable service.
3. **Human/application identity** — identity of the actor requesting an operation.
4. **Artifact identity** — hash/signature identity of software, data, or configuration.

This prevents the common mistake of treating 'the computer' as the only security principal.

## Policy model

A distributed policy system should support:

- local enforcement;
- explicit capability grants;
- least privilege;
- delegation with expiration/scope;
- offline operation;
- auditable provenance;
- conflict detection rather than silent policy replacement.

A peer should never need to ask a global authority whether it is allowed to enforce its own local safety policy.
