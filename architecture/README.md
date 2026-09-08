# ANARCHY Architecture

Candidate architecture layers:

1. Identity
2. Discovery
3. Transport
4. Routing
5. Trust
6. Coordination
7. Data/content
8. Provenance
9. Governance
10. Application

## Cross-cutting portability layer

ANARCHY also defines a candidate **Portable Compatibility Runtime** that separates host-specific ABI behavior from the canonical ANARCHY runtime.

```text
Host ABI
   |
Host Adapter
   |
Compatibility Runtime
   |-- environment
   |-- paths
   |-- process semantics
   |-- IPC
   |-- locale / encoding
   |-- runtime policy
   `-- observability
   |
Canonical ANARCHY Runtime
   |
ANARCHY node services
```

This layer is informed by compatibility-system prior art, including Cygwin, but does not make Cygwin an ANARCHY dependency.

See [`compatibility-runtime.md`](compatibility-runtime.md).

## Research questions

- How do autonomous nodes discover each other?
- How does routing work without a mandatory central controller?
- How does the system behave during network partitions?
- How are identities established?
- How is authority delegated?
- How is authority revoked?
- How are conflicting states resolved?
- How is provenance preserved across migrations?
- How are software licenses represented?
- How can independent implementations interoperate?
- What host ABI differences must be normalized for independent implementations to interoperate?
- What is the minimum canonical runtime contract shared across operating systems?
