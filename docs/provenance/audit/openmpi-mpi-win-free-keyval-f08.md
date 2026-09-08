# Open MPI `MPI_Win_free_keyval_f08` provenance audit

## Artifact

- **Symbol:** `MPI_Win_free_keyval_f08`
- **Language:** Fortran 2008 (`! -*- f90 -*-`)
- **Likely component:** Open MPI Fortran 2008 bindings
- **Underlying C/Fortran bridge:** `ompi_win_free_keyval_f`
- **MPI domain:** One-sided communication / MPI Windows (RMA)
- **Function:** Releases an MPI window attribute keyval through the Open MPI Fortran binding.

## Provenance

The supplied source carries two explicit copyright notices:

- Copyright (c) 2010-2012 Cisco Systems, Inc.
- Copyright (c) 2009-2012 Los Alamos National Security, LLC.

The `$COPYRIGHT$` marker indicates that the complete applicable license/copyright boilerplate is expected to be supplied by the originating Open MPI source distribution/build system. The exact Open MPI release should therefore be determined from surrounding package metadata before assigning a precise version.

The `use :: mpi_f08, only : ompi_win_free_keyval_f` dependency is strong evidence that this is part of Open MPI's MPI-3-era Fortran 2008 binding layer rather than a standalone Fortran implementation.

## Technical classification

This is a **thin language-binding wrapper**, not an implementation of the MPI window/keyval mechanism itself. It:

1. accepts the Fortran `INTEGER` window keyval;
2. calls Open MPI's internal Fortran-compatible routine `ompi_win_free_keyval_f`;
3. copies the returned error status into the optional Fortran `ierror` argument.

There is no allocation, persistence, networking protocol, cryptographic primitive, credential handling, or key material in this source file.

## Cryptography/security classification

- **Cryptographic algorithm:** None.
- **Security keys:** None. `win_keyval` is an MPI attribute/keyval identifier, **not a cryptographic key**.
- **Authentication:** None.
- **Encryption:** None.
- **Integrity/signing:** None.

The term `keyval` must not be conflated with SSH/GPG/JOSE keys. In MPI, a keyval is an opaque/application-level identifier used for attributes associated with MPI objects.

## Dependencies / interfaces

- `mpi_f08` — Open MPI Fortran 2008 module.
- `ompi_win_free_keyval_f` — Open MPI internal binding entry point.
- MPI error/status conventions via the optional `ierror` argument.

## ANARCHY relevance

This artifact is relevant as **distributed-computing infrastructure provenance**. MPI RMA/window semantics can be useful when evaluating high-performance distributed coordination, memory/metadata exchange, and federated compute components in ANARCHY/RitualMesh.

However, this particular wrapper should remain classified as an interoperability/binding layer. It does not itself establish a decentralized networking protocol, consensus mechanism, security boundary, or cryptographic trust model.

## Preservation / modernization disposition

**Preserve as historical provenance; do not rewrite this wrapper merely to modernize it.**

For a future ANARCHY integration, identify the exact Open MPI release and audit the corresponding `mpi_f08` module, RMA implementation, build configuration, and license files before porting or replacing components. The wrapper is small and mechanically straightforward; compatibility is more likely to depend on the surrounding Open MPI ABI/API and Fortran module than on this routine itself.

## Corpus tags

`openmpi`, `mpi`, `fortran-2008`, `mpi_f08`, `rma`, `one-sided-communication`, `distributed-computing`, `language-binding`, `historical-provenance`, `no-cryptography`, `cisco`, `los-alamos-national-security`
