# ANARCHY Portable Compatibility Runtime

## Status

Research architecture / candidate specification.

This document extracts architectural patterns from compatibility systems such as Cygwin without making ANARCHY dependent on Cygwin.

## 1. Purpose

ANARCHY nodes may execute across different host operating systems, ABIs, filesystems, process models, character encodings, and runtime environments. The compatibility runtime provides a stable boundary between those host-specific mechanisms and the canonical ANARCHY runtime.

The design goal is portability through explicit adaptation rather than implicit host assumptions.

## 2. Boundary model

```text
+--------------------------------------------------+
|                    HOST ABI                     |
| Windows / Linux / macOS / BSD / other hosts     |
+-------------------------+------------------------+
                          |
                    HOST ADAPTER
                          |
+-------------------------v------------------------+
|              COMPATIBILITY RUNTIME              |
| environment | paths | process | IPC | locale   |
| libraries   | terminal | runtime policy         |
+-------------------------+------------------------+
                          |
                     NORMALIZATION
                          |
+-------------------------v------------------------+
|              CANONICAL RUNTIME                  |
| UTF-8 | canonical paths | process identity      |
| portable environment | portable interfaces      |
+-------------------------+------------------------+
                          |
+-------------------------v------------------------+
|              ANARCHY NODE SERVICES              |
| identity | discovery | transport | routing      |
| trust | coordination | data | provenance        |
+--------------------------------------------------+
```

## 3. Core principle

**Host representation is not the canonical application representation.**

A host adapter may translate between representations while preserving a canonical ANARCHY contract.

Examples:

- Windows paths may be exposed through a POSIX compatibility layer but represented canonically by ANARCHY as a normalized path object.
- Windows UTF-16 APIs may be bridged to a canonical UTF-8 application interface.
- Host environment variables may be imported into a POSIX-compatible environment and explicitly synchronized when required by the host API.
- Process-specific telemetry must not require multiple processes to share one mutable output artifact.

## 4. Environment ABI

The environment is treated as an interface boundary rather than an undifferentiated string map.

```text
HOST ENVIRONMENT
      |
      | import / translate
      v
COMPATIBILITY ENVIRONMENT
      |
      | normalize
      v
ANARCHY ENVIRONMENT
```

The implementation should define:

1. Which host variables are imported.
2. Which variables are translated.
3. Which variables are canonicalized.
4. Which values are host-only.
5. Whether synchronization back to the host is automatic or explicit.
6. How inherited environments are recorded for provenance and reproducibility.

## 5. Path ABI

Paths should be modeled as structured values at compatibility boundaries rather than relying on string substitution alone.

```text
HOST PATH
   |
   v
HOST ADAPTER
   |
   v
CANONICAL PATH
   |
   v
APPLICATION / NODE
```

A canonical path contract should define encoding, absolute/relative semantics, separator rules, normalization, case behavior, drive/volume semantics, symbolic-link behavior, and invalid-name handling.

## 6. Locale and encoding ABI

The canonical runtime should use an explicitly documented character encoding contract. UTF-8 is the default candidate for network and application interchange, while host adapters may use native encodings internally.

```text
APPLICATION / NETWORK
        |
      UTF-8
        |
COMPATIBILITY RUNTIME
        |
  host encoding/API
```

Locale selection and character encoding are related but distinct concerns. Language, territory, collation, character classification, and wire encoding must not be conflated.

## 7. Process ABI

The compatibility layer must define how a logical ANARCHY process maps onto host processes.

Required concepts include:

- process identity;
- parent/child relationships;
- environment inheritance;
- working-directory inheritance;
- standard streams;
- exit status;
- signals or equivalent termination events;
- resource limits;
- process-local configuration;
- process-local telemetry.

Fork-like process creation is a reference pattern, not a mandatory primitive. Hosts without `fork()` should implement equivalent lifecycle semantics through the host adapter where practical.

## 8. Process-isolated observability

Telemetry must be namespaced by node, process, execution, and artifact identity.

```text
NODE
 |
 +-- PROCESS A -- telemetry/A
 +-- PROCESS B -- telemetry/B
 +-- PROCESS C -- telemetry/C
 |
 +-----------> aggregation layer
```

A compatibility runtime must not assume that independently executing processes can safely write the same profiling or diagnostic artifact.

## 9. Runtime policy

Runtime compatibility options should be represented separately from locale and environment data.

Candidate policy domains:

- terminal behavior;
- process behavior;
- IPC behavior;
- filesystem compatibility;
- path conversion;
- diagnostic behavior;
- host interoperability;
- legacy compatibility.

Policy should be explicit, versioned, and inspectable.

## 10. Host adapters

The canonical runtime must not contain arbitrary host-specific conditionals when an adapter can isolate them.

Candidate adapters:

```text
compat/host/windows
compat/host/linux
compat/host/macos
compat/host/bsd
```

Cygwin is a **reference implementation / prior-art source**, not an ANARCHY dependency.

## 11. ANARCHY architecture mapping

The compatibility runtime supports the existing ANARCHY layers:

| ANARCHY layer | Compatibility contribution |
|---|---|
| Identity | host-independent process/node identity |
| Discovery | portable interface and endpoint representation |
| Transport | host-independent socket/interface abstraction |
| Routing | stable node/process addressing |
| Trust | reproducible runtime and artifact identity |
| Coordination | process and environment semantics |
| Data/content | canonical encoding and path semantics |
| Provenance | host/runtime/build metadata |
| Governance | explicit policy and capability boundaries |
| Application | stable portable APIs |

## 12. Reference sources

The following Cygwin documentation is used as architectural prior art:

- Cygwin environment variables: https://jhauga.github.io/cygwin-htdocs/cygwin-ug-net/using-cygwinenv.html
- Cygwin locale setup: https://jhauga.github.io/cygwin-htdocs/cygwin-ug-net/setup-locale.html
- Cygwin environment setup: https://jhauga.github.io/cygwin-htdocs/cygwin-ug-net/setup-env.html
- Cygwin gprof and fork behavior: https://jhauga.github.io/cygwin-htdocs/cygwin-ug-net/gprof.html#gprof-fork

These references document Cygwin behavior. They do not establish ownership, licensing, or authorship of ANARCHY.

## 13. Research questions

- What is the minimum canonical ABI required for every ANARCHY node?
- Which host-specific semantics cannot be normalized without information loss?
- How should path identity behave across case-sensitive and case-insensitive hosts?
- How should process identity survive migration between hosts?
- How should environment state be captured in reproducible builds and node provenance?
- Which capabilities must remain host-specific rather than being normalized?
- Can one compatibility contract support native execution, emulation, containers, and cross-toolchain builds?

## 14. Non-goals

This specification does not attempt to:

- reimplement Cygwin;
- declare third-party code to be ANARCHY code;
- make legal ownership claims from technical similarity;
- require a particular operating system;
- require `fork()` on every host;
- define a final ANARCHY ABI before implementation evidence exists.
