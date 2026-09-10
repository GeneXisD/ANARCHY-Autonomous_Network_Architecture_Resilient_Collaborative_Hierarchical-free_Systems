# ANARCHY Software Provenance Framework

## Purpose

This framework separates authorship, technical lineage, licensing, public-domain status, contribution history, and commercialization rights.

## Classification

### ANARCHY-original

Work authored specifically for ANARCHY by its project contributors and not copied from an existing work.

### Third-party open source

Software originating outside ANARCHY and distributed under an identified open-source license. Preserve the original license and attribution requirements.

### Modified open source

An existing open-source work modified or incorporated by ANARCHY. Record the upstream repository, version/commit, original license, and modifications. Do not classify the upstream work as ANARCHY-original.

### Public domain / CC0

Material for which public-domain status or a CC0 dedication can be established from a primary source. Preserve the evidence supporting that classification.

### Unknown / pending review

Any component whose origin, license, or redistribution status cannot yet be established. Do not ship or relicense it as ANARCHY-original until reviewed.

## Required component record

Every material third-party or externally sourced component should have:

- component name;
- origin/author/owner;
- upstream repository or publication;
- exact version, tag, release, or commit where available;
- license or public-domain basis;
- copyright notice;
- modifications made by ANARCHY;
- redistribution conditions;
- patent/trademark considerations when relevant;
- evidence URL;
- evidence access date;
- confidence/classification.

## Evidence chain

```text
SOURCE
  ↓
AUTHOR / OWNER
  ↓
ARTIFACT
  ↓
VERSION / COMMIT / HASH
  ↓
LICENSE / RIGHTS STATUS
  ↓
MODIFICATION HISTORY
  ↓
DISTRIBUTION
  ↓
DEPLOYMENT
  ↓
OBSERVABLE RESULT
```

## Legal separation

Do not collapse these into one field:

```text
copyright status
software license
patent rights
trademark rights
privacy/publicity rights
statutory restrictions
contractual restrictions
security/release restrictions
```

CC0 can address copyright and related rights to the extent legally possible, but does not automatically waive unrelated rights or statutory restrictions.

## Government-originated software

The FEC provides a useful documented model: government-created software can be treated as public-domain work, while existing OSS modified by government personnel may retain third-party licensing/provenance requirements. See `docs/research/FEC_OPEN_SOURCE_PROVENANCE.md`.

## Contributions

Contribution terms must be explicit before accepting external code. A contribution should have a known copyright/licensing destination and must not silently change the licensing status of third-party code.

## Commercialization

A component's commercial usability must be determined from its actual license and applicable restrictions. Open source does not mean ownerless, and public domain does not mean that every unrelated legal restriction disappears.

The ANARCHY commercialization path is:

```text
ORIGINAL / VALIDATED ARTIFACT
          ↓
PROVENANCE + RIGHTS REVIEW
          ↓
REPRODUCIBLE VALIDATION
          ↓
OPEN RELEASE OR PROTECTED RELEASE
          ↓
LICENSE / PARTNERSHIP / INCUBATION
          ↓
SERVICE / PRODUCT / SPIN-OFF / INDUSTRIAL USE
```

## Research discipline

A technical similarity is not proof of common authorship. A hyperlink is not proof of sponsorship. A shared dependency is not proof of organizational control. A repository license is not proof that every file has the same provenance.

Primary evidence should be preferred over secondary commentary. When uncertainty remains, record it explicitly rather than converting a hypothesis into a fact.
