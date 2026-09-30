# ANARCHY Licensing and Evidence Status

This document prevents research notes from being mistaken for verified legal permissions.

## Verified/established research inputs

### XAMPP

The XAMPP project documents itself as a compilation/distribution of free software and states that individual contained products retain their own licenses. XAMPP's build/distribution infrastructure is relevant as an engineering precedent.

### PHP component inventory

The supplied PHP license inventory demonstrates that one software distribution may contain numerous independently licensed components and special notices. ANARCHY therefore requires component-level provenance.

### Apache Ant/Tomcat build material

The supplied build documentation demonstrates explicit dependency configuration, build targets, testing, packaging and release/integrity stages.

### openSUSE One Click Install/YMP

The public specification demonstrates declarative repository/package installation. Trademark permissions remain separate from the software licenses.

### Oracle StorageTek SL150 licensing disclosure

**Status: COMPARATIVE PRIMARY-SOURCE EVIDENCE**

The repository preserves the supplied `Licensing Information.pdf` from the Oracle StorageTek SL150 licensing documentation. The document identifies/reproduces multiple third-party notices and licenses associated with software included/distributed with the product.

This is evidence for the **existence of historical component-level licensing disclosure inside a larger product**, not evidence that Oracle owns those components or that their licenses apply to ANARCHY.

Provenance record:

`docs/provenance/oracle-storagetek-sl150-licensing.md`

Preserved artifact metadata:

- Path: `Licensing Information.pdf`
- Git blob SHA-1: `24550bee55d4364c2813fe3a27edbb1fec4eb4dc`
- Size: `1,250,130` bytes

The Git blob SHA-1 is not a SHA-256 file digest. A cryptographic digest should be generated from the actual PDF bytes during a controlled archival pass.

### mediocre-go-lib

**Status: SUPPORTED artifact identity; historical Git/license/module metadata VERIFIED**

A provenance record has been added at:

`docs/provenance/mediocre-go-lib.md`

The record documents the historical GitHub repository, explicit 2023 tombstone/migration, v2 Go module metadata, historical MIT license and copyright notice, selected commit lineage, dependency state at the final substantive GitHub snapshot, and the current-source verification gap.

Historical source evidence:

- Repository: `github.com/mediocregopher/mediocre-go-lib`
- Last substantive GitHub commit: `47c8c5b8504f02617f225f9850d5b250708326d9`
- Tombstone: `41a84f123a49c1ee0c309f19d9d90d5dc46854d6`
- v2 module: `github.com/mediocregopher/mediocre-go-lib/v2`
- Go version: `1.15`
- Historical license: MIT
- Historical copyright notice: Brian Picciano, 2018
- External Go module requirements at the inspected snapshot: none declared
- Current-source byte equivalence with `code.betamike.com`: not yet verified

This artifact is recorded as a **historical upstream component**, not as ANARCHY-originated code.

## Unverified / awaiting primary evidence

### DC219 Open Source Software Policy

**Status: UNVERIFIED**

The actual policy document has not been located in the available Library evidence. Existing license inventories are not sufficient proof of DC219 applicability.

Required next evidence:

- exact policy document;
- revision/date;
- issuing organization;
- scope;
- covered components/artifacts;
- clauses concerning modification;
- clauses concerning redistribution;
- clauses concerning relicensing;
- clauses concerning trademarks/branding;
- clauses concerning Android/AOSP or other named projects.

### Linux&C Vol. 39

**Status: UNVERIFIED**

The exact magazine issue/artifact has not yet been recovered into the current evidence set. Do not invent its contents.

### FunkyMios

**Status: UNVERIFIED**

The project has been identified by the user as an iDevice one-click installation/provisioning component, but exact upstream source, version, license and behavior still need to be captured.

## Legal/provenance rule

```
OPEN-SOURCE LICENSE
       ≠
TRADEMARK LICENSE
       ≠
PATENT LICENSE
       ≠
CONTRACTUAL PERMISSION
       ≠
CORPORATE POLICY
```

A component can be legally modifiable under its copyright license while still requiring separate trademark analysis. A corporate OSS policy can impose internal process requirements without changing the upstream license. A third-party inventory can list a license without proving that an organization owns or controls the component.

## Required ANARCHY matrix

| Artifact | Upstream | License | Modification | Redistribution | Trademark | Policy evidence | Status |
|---|---|---|---|---|---|---|---|
| XAMPP build model | ApacheFriends | component-specific | possible | component-specific | Apache/XAMPP marks separate | public project docs | SUPPORTED |
| openSUSE-derived environment | openSUSE | component-specific | possible | component-specific | separate openSUSE trademark rules | public trademark docs | SUPPORTED |
| Linux kernel/modules | Linux upstream | GPL obligations | possible | GPL obligations | N/A | policy TBD | SUPPORTED |
| Apple restore tools | upstream projects | project-specific | possible | project-specific | Apple marks separate | policy TBD | PROPOSED |
| Oracle StorageTek SL150 disclosure | Oracle product + named third-party components | component-specific | component-specific | component-specific | separate | Oracle disclosure | COMPARATIVE |
| mediocre-go-lib | mediocregopher / code.betamike.com | MIT (historical GitHub evidence) | TBD | historical license permits subject to terms | separate | project evidence | SUPPORTED |
| FunkyMios | TBD | TBD | TBD | TBD | TBD | TBD | UNVERIFIED |
| Linux&C Vol.39 | publication | publication copyright | TBD | TBD | N/A | TBD | UNVERIFIED |
| DC219 policy | TBD | policy document | TBD | TBD | TBD | actual text required | UNVERIFIED |

## Rule for future commits

If a new document changes a licensing conclusion, preserve the original evidence and update this matrix with a citation, revision date and evidence status. Never delete uncertainty merely to make the repository appear more complete.
