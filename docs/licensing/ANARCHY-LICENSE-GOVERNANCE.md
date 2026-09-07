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
