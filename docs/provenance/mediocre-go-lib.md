# mediocre-go-lib — Provenance Record

**Status:** SUPPORTED artifact identity; historical Git/license/module metadata VERIFIED; current-source byte equivalence UNVERIFIED.

## Artifact identity

- Project: `mediocre-go-lib`
- Historical repository: `github.com/mediocregopher/mediocre-go-lib`
- Maintainer/author identity observed in repository history: Brian Picciano / `mediocregopher`
- Current source location announced by the historical repository: `code.betamike.com/mediocregopher/mediocre-go-lib`
- Go v2 module: `github.com/mediocregopher/mediocre-go-lib/v2`

## Repository migration

The GitHub repository was created in January 2018 and was subsequently migrated away from GitHub. The final GitHub commit is an explicit `TOMBSTONE` commit dated 2023-12-26:

```
41a84f123a49c1ee0c309f19d9d90d5dc46854d6
TOMBSTONE
```

The preceding substantive source commit is:

```
47c8c5b8504f02617f225f9850d5b250708326d9
mlog: Make default message handler human readable
2023-09-10
```

The tombstone README identifies `code.betamike.com/mediocregopher/mediocre-go-lib` as the moved project location.

## Go module metadata

At commit `47c8c5b8504f02617f225f9850d5b250708326d9`, `go.mod` contained:

```go
module github.com/mediocregopher/mediocre-go-lib/v2

go 1.15
```

No third-party module requirements were declared in that `go.mod`, and the corresponding `go.sum` was empty.

Documented v2 release evidence includes `v2.0.0-beta.2`.

## Historical license

At the last substantive GitHub source state, the repository contained a `LICENSE` file declaring:

```
MIT License

Copyright (c) 2018 Brian Picciano
```

The complete MIT notice was present in the repository before the tombstone migration commit. The GitHub repository's current tombstone state should therefore not be used to infer that the historical source lacked a license.

**License status:** MIT — VERIFIED historical repository evidence.

**Copyright notice:** Brian Picciano, 2018.

This record does not independently determine the licensing status of any later source revision hosted at the migrated location.

## Commit lineage

Selected historical commits establish the evolution of the project:

- `0e64f16f032d90be698c3eef7619f80d7d95172` — 2019-07-16 — initial `mredis` implementation.
- `df01ccffcb75501687044e60d2184a4307a206d6` — 2019-07-30 — thread-safe random implementation.
- `3e2713a85086bbf66133276904d4502ce15cda57` — 2021-02-07 — removal of `mcmp` and subsequent refactoring.
- `360d41e2b8f6e8f8ef9b09190f11dc3692d51774` — 2021-04-09 — `merr` refactor and removal of most earlier components.
- `ba9bc6c46cc3ce935245f01365dfcee7b1643f27` — 2021-04-10 — `merr`/`mlog` error handling refactor.
- `cbeee71cb1eed198da98d34a44cc2ab74f022f40` — 2022-05-06 — `mlog` fatal-error API change.
- `ec5e2441c6ddfb847233470fe9bd30ce08306ade` — 2022-11-13 — `mlog` `WithMaxLevel`.
- `07f3889a705b3283c3e1d4999c827fc50f731b15` — 2022-11-13 — `mlog` `MaxLevel`.
- `47c8c5b8504f02617f225f9850d5b250708326d9` — 2023-09-10 — human-readable default `mlog` handler.
- `41a84f123a49c1ee0c309f19d9d90d5dc46854d6` — 2023-12-26 — repository tombstone/migration.

The history shows that the pre-v2 library was substantially broader than the final documented v2 package set. Historical package names such as `mredis`, `mdb`, `msql`, `mpubsub`, `mnet`, `mrun`, and `mcmp` should not automatically be treated as part of the final v2 API.

## v2 package relevance

The documented v2 package set includes:

- `mctx` — context annotations.
- `merr` — structured errors, attributes, stack information and multi-errors.
- `miter` — iterator abstractions.
- `mlog` — logging.

For ANARCHY research, `mctx`, `merr`, and `mlog` are particularly relevant as a historical example of contextual metadata, structured error information, and logging being carried through application execution.

This is an architectural similarity only. It is not evidence that mediocre-go-lib derives from ANARCHY or that ANARCHY derives from mediocre-go-lib.

## Dependency status

**At the inspected final substantive GitHub v2 snapshot:**

- External Go module requirements: none declared.
- `go.sum`: empty.
- Go language version: 1.15.
- Standard-library usage: present.

Historical consumers of the older module may contain additional dependencies, but those consumer dependencies are not evidence that the final v2 library itself declared those modules.

## Evidence classification

| Claim | Status |
|---|---|
| Historical GitHub repository identity | VERIFIED |
| Historical author/copyright notice | VERIFIED |
| Historical MIT license | VERIFIED |
| v2 module path | VERIFIED |
| Go version `1.15` | VERIFIED |
| Empty `go.sum` at inspected snapshot | VERIFIED |
| Explicit GitHub tombstone | VERIFIED |
| Migration destination named by project | VERIFIED |
| Historical commit lineage | VERIFIED |
| Current `code.betamike.com` repository identity | SUPPORTED |
| Byte-for-byte equivalence between current source and GitHub snapshot | UNVERIFIED |
| Current-host license state | UNVERIFIED |
| Current-host dependency state | UNVERIFIED |

## ANARCHY integration note

This artifact is suitable for ANARCHY's provenance corpus as a **historical upstream component record**.

Do not copy or vendor the source merely from this metadata record. If ANARCHY later incorporates source code from the project, record:

1. exact upstream URL;
2. exact revision/tag;
3. source archive or Git object identifiers;
4. SHA-256 of the captured source;
5. license and copyright files;
6. modifications made by ANARCHY;
7. resulting build artifact and build environment;
8. redistribution/trademark considerations.

## Primary source references

- Historical repository: https://github.com/mediocregopher/mediocre-go-lib
- Last substantive source commit: https://github.com/mediocregopher/mediocre-go-lib/commit/47c8c5b8504f02617f225f9850d5b250708326d9
- Tombstone commit: https://github.com/mediocregopher/mediocre-go-lib/commit/41a84f123a49c1ee0c309f19d9d90d5dc46854d6
- Historical LICENSE: https://github.com/mediocregopher/mediocre-go-lib/blob/47c8c5b8504f02617f225f9850d5b250708326d9/LICENSE
- Go module documentation: https://pkg.go.dev/github.com/mediocregopher/mediocre-go-lib/v2
- Current source location announced by the project: https://code.betamike.com/mediocregopher/mediocre-go-lib

## Verification limitation

This record was created from accessible GitHub repository metadata, Git history, repository files, and public Go package documentation. The current source repository at `code.betamike.com` has not yet been independently cloned and compared against the historical Git object tree. Therefore this record intentionally does **not** claim byte-level equivalence.
