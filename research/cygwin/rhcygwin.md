# RH/Cygwin historical research

## Scope note

This file records the **Red Hat / Cygnus / Cygwin lineage** and the historical packaging/tooling evidence relevant to ANARCHY. The exact term `rhcygwin` should be treated as a research label until a specific artifact, archive, or repository bearing that exact name is identified.

## Why Cygwin belongs in ANARCHY

Cygwin is a strong example of an operating-environment compatibility layer: a shared DLL supplies substantial POSIX API functionality on Windows, while a large collection of GNU/Open Source tools runs above it. The official project describes it as a collection of GNU/Open Source tools plus `cygwin1.dll`, rather than as a Linux binary compatibility layer.

Primary references:

- https://cygwin.com/
- https://cygwin.com/docs.html
- https://www.cygwin.com/doc/preview/cygwin-ug-net/using.html

## Historical lineage

Cygwin began at Cygnus Solutions in 1995. Cygnus later merged with Red Hat. Early Cygwin development deliberately used a shared compatibility layer rather than rewriting every Unix/GNU application directly against Win32. This is an important architectural precedent for ANARCHY: **adapt the boundary once, then reuse a broad ecosystem above it**.

## The `rh` / Red Hat-era packaging clue

Historical Cygwin developer-list material documents an `rh` Perl script that transformed `setup.ini` metadata into categorized output. This is useful evidence for the evolution of Cygwin's package metadata and distribution tooling.

Reference:

- https://cygwin.com/pipermail/cygwin-developers/2001-September/004491.html

Do not equate this historical `rh` script with a proven component called `rhcygwin`; keep the names separate until primary evidence establishes the connection.

## ANARCHY relevance

### Compatibility boundary

Cygwin demonstrates a compatibility-layer pattern:

```text
existing application ecosystem
            ↓
      POSIX API boundary
            ↓
       cygwin1.dll
            ↓
       Win32 substrate
```

ANARCHY can generalize this into:

```text
portable service/application
            ↓
     ANARCHY capability API
            ↓
       node adapter
            ↓
local OS / hardware / network substrate
```

### Ecosystem preservation

A stable compatibility interface can let a large body of software survive across a changing substrate. This supports ANARCHY's goal of heterogeneous nodes rather than one mandatory operating system.

### Packaging and mirrors

Cygwin's setup/package metadata, mirrors, package repositories, and contributor model are relevant prior art for distributed software distribution.

### Windows interoperability

Cygwin's POSIX/Win32 path mapping, process model, permissions, networking, and `/proc` exposure are useful case studies for cross-substrate interoperability. See the Cygwin User's Guide for detailed behavior.

## ANARCHY research questions

- What minimum API surface makes an adapter useful?
- Can one service protocol span Linux, Android, Windows/Cygwin, BSD, and embedded systems?
- Which semantics must be preserved exactly and which can be translated?
- Can compatibility adapters be independently maintained by different node operators?
- How should package metadata identify the substrate and ABI requirements?
- Can repositories and mirrors fail independently without making the whole system unavailable?

## Evidence classification

- **Established:** Cygwin is a POSIX-oriented compatibility environment for Windows.
- **Established:** Cygwin originated at Cygnus Solutions and later became part of the Red Hat lineage.
- **Established:** historical Cygwin tooling included package metadata generation/categorization workflows.
- **Unresolved:** the exact identity and provenance of any artifact specifically named `rhcygwin`.

If a local/archive artifact named `rhcygwin` is found, add its filename, source URL, checksum, date, license, and relationship to this historical chain here rather than silently treating the name as equivalent to Cygwin.
