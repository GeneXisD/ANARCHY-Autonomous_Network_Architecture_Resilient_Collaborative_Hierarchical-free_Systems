# ANARCHY — License and Open Distribution Governance

## Purpose

ANARCHY must remain legally intelligible as it grows. The project therefore treats open-source licensing, copyright, patents, trademarks, contractual permissions, and internal policy as distinct evidence classes.

## Core rule

```text
UPSTREAM LICENSES REMAIN AUTHORITATIVE
                    ↓
ANARCHY ADDS INTEGRATION + PROVENANCE
                    ↓
ANARCHY DISTRIBUTES ONLY WITH APPLICABLE RIGHTS
```

ANARCHY does not presume that integrating an upstream project permits relicensing that project.

## Open-by-design model

The desired architecture is **open where the governing rights permit openness**.

This means:

- upstream source remains under its upstream license;
- ANARCHY-original code receives an explicitly selected project license;
- modifications are identified and attributed;
- required notices are preserved;
- source-availability obligations are fulfilled where applicable;
- trademark restrictions remain visible;
- proprietary or restricted material is not silently converted into open-source material;
- missing rights block release rather than being guessed away.

## License closure

"License closure" means that the release process has resolved the rights status of every material component sufficiently to make a distribution decision.

It does **not** mean changing every component to one license.

```text
IDENTIFY
   ↓
CLASSIFY
   ↓
VERIFY LICENSE
   ↓
VERIFY NOTICES
   ↓
CHECK MODIFICATION RIGHTS
   ↓
CHECK REDISTRIBUTION TERMS
   ↓
CHECK SOURCE OBLIGATIONS
   ↓
CHECK TRADEMARKS / PATENTS / CONTRACTS
   ↓
RECORD DECISION
   ↓
RELEASE OR BLOCK
```

## Component record

Each released component should eventually have a record containing:

```yaml
component:
  name:
  upstream:
  version:
  revision:
  source_hash:
  license:
  license_evidence:
  copyright:
  notices:
  modifications:
  patches:
  trademark_notes:
  patent_notes:
  redistribution:
  source_offer_or_source_location:
  sbom_reference:
  build_record:
  evidence_status:
```

## SPDX

ANARCHY should use SPDX identifiers and SPDX-compatible metadata where they accurately represent the governing terms. SPDX is intended to communicate licensing and related software supply-chain information in machine-readable form.

SPDX metadata complements, rather than replaces, the actual license and copyright notices required by upstream projects.

## Decentralized distribution

A decentralized network does not erase licensing obligations. Every node that obtains, stores, serves, modifies, or redistributes an artifact must be able to identify the artifact's provenance and applicable rights.

The ANARCHY/RitualMesh model should therefore distribute metadata together with artifacts:

```text
ARTIFACT
  +
SOURCE ID
  +
VERSION
  +
HASH
  +
LICENSE ID
  +
NOTICE REFERENCES
  +
SBOM
  +
PROVENANCE
  +
RELEASE RECORD
```

Content addressing provides integrity and identity; it does not itself grant copyright or redistribution rights.

## Treaty / international compliance language

ANARCHY should not claim blanket "treaty compliance" merely because it uses open-source licenses. International obligations can arise from copyright, patent, trademark, trade, export-control, privacy, sanctions, procurement, contract, and other legal regimes depending on the jurisdiction and transaction.

The defensible engineering objective is therefore:

> **Maintain machine-readable provenance and rights evidence so jurisdiction-specific legal review can be performed without reconstructing the technical history from scratch.**

## Evidence classes

| Status | Release meaning |
|---|---|
| VERIFIED | Primary evidence inspected |
| SUPPORTED | Authoritative upstream documentation supports conclusion |
| OBSERVED | Directly observed in supplied artifact |
| PROPOSED | Future architecture |
| UNVERIFIED | Evidence missing |
| BLOCKED | Release should not proceed until issue is resolved |

## Required future controls

- SPDX license identifiers;
- SPDX SBOM or equivalent machine-readable inventory;
- NOTICE aggregation where required;
- source and patch manifests;
- cryptographic artifact hashes;
- reproducible build records where practical;
- trademark audit;
- contributor/license records;
- release checklist;
- exception register;
- evidence archive.


## Creator rights, Creative Commons, and separate license domains

This section records the project's current **rights-policy intent**. It is not a substitute for a signed license, legal review, or a verified chain of title. Do not add a blanket repository license until the rights holder, scope, and exact license text have been approved.

### ANARCHY-original material: reserved-rights intent

The creator's stated requirements for original ANARCHY material are:

- preserve authorship and attribution;
- no CC0 dedication or blanket waiver;
- commercial exploitation requires separate written permission;
- distribution of derivative/adapted works requires permission;
- retain a verifiable record of the author, source, revision, publication, and permission granted.

Working rights statement:

> Open participation does not eliminate ownership. Distributed access does not eliminate accountability. Shared knowledge does not eliminate the rights of its creators.

Until a specific license is approved for a specific work, mark its rights status **UNRESOLVED / RIGHTS RESERVED — verify ownership and permissions before redistribution**. Do not imply that this statement overrides licenses already granted by upstream authors or third parties.

### Creative Commons distinctions

- **CC BY** requires attribution and permits commercial use and adaptations under its terms.
- **CC BY-SA** requires attribution and ShareAlike for distributed adaptations; it permits commercial use. Preserve the exact version attached to the source work.
- **CC BY-NC** restricts commercial use but permits adaptations under its terms.
- **CC BY-NC-ND** permits noncommercial sharing of unchanged material with attribution and does not permit distributing adapted material under the license. It does not prohibit private creation of adaptations. Therefore it is not a complete substitute if the creator intends to prohibit even private derivative creation without permission.
- **CC0** is not approved for ANARCHY-original material under the current creator instruction.

CC licenses are standardized public licenses, not a custom permission system. If a work requires a stricter or differently scoped permission rule, use a separately drafted rights-reserved notice or written license reviewed for that work. Do not describe CC BY-NC-ND as an OSI-approved open-source software license.

### Historical licenses and migration

The corpus contains references to CC BY-SA 1.0, 2.0, and 3.0 and GNU FDL 1.2. Preserve the exact license/version, copyright notices, attribution, source, and modification history that accompanied each historical work. Do not silently upgrade, replace, or migrate a work to a newer Creative Commons version.

A GFDL-to-Creative-Commons migration is conditional on the exact work, version, notices, eligibility, and license terms. It is never a blanket repository-wide conversion. Record the original license, any additional license, migration basis, and permission evidence separately.

### Separate rights domains

| Material | Required treatment |
|---|---|
| Original ANARCHY documentation and research text | Work-specific copyright and approved documentation license/permission notice |
| Original software/code | Separate software license; do not apply a Creative Commons license by default |
| Hardware designs, schematics, PCB files and physical devices | Separate hardware/design license and physical-product rights review |
| Third-party source and binaries | Exact upstream license, version, notices and obligations |
| Trademarks, names and logos | Separate trademark/brand permission; an open-source license is not trademark permission |
| Historical archived works | Preserve original authorship, source and exact historical license |

### Rights gate for every release

Before publication or distribution, record: (1) author/rightsholder evidence, (2) exact work and version, (3) selected license or written permission, (4) attribution and notices, (5) commercial-use status, (6) adaptation/derivative status, (7) third-party components, and (8) trademark status. If any material right is unknown, mark the affected component **BLOCKED** rather than assuming permission.

This section preserves the creator's stated intent; final license selection and enforceability should be reviewed by qualified counsel before a production release.
