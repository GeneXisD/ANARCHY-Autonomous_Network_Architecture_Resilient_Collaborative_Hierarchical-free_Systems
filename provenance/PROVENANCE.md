# ANARCHY Software Provenance Framework

## Purpose

This framework separates authorship, technical lineage, licensing, public-domain status, contribution history, and commercialization rights.

ANARCHY maintains provenance as a **chain of evidence**, not as a claim that every related technology, institution, repository, or historical artifact belongs to ANARCHY.

## Project-origin statement

**Project:** ANARCHY — Autonomous Network Architecture for Resilient, Collaborative, Hierarchy-free Systems  
**Project author / steward:** Victor Jose Corral  
**Project identity:** GeneXisD  
**Project repository:** `GeneXisD/ANARCHY-Autonomous_Network_Architecture_Resilient_Collaborative_Hierarchical-free_Systems`  
**Repository origin:** GitHub  
**Current primary branch:** `main`  
**Provenance record status:** Living record; updated as evidence is discovered, verified, or corrected.

This statement records the project's claimed authorship and stewardship. It does **not** by itself create, transfer, or prove any particular legal intellectual-property right. Copyright, patent, trademark, contract, employment, government, and other legal questions must be evaluated under the applicable law and the actual evidence.

## Personal dedication and motivation

The author records ANARCHY as a long-term engineering and research journey undertaken with the goal of building useful, lawful, durable technical work and creating a meaningful legacy for his son, **Ian Patrick Corral**, born June 4, 2000, in Las Vegas, Nevada.

This dedication is part of the project's historical narrative and motivation. It is not presented as evidence that the son authored, owns, endorsed, or participated in any particular technical artifact.

## Provenance boundary

ANARCHY distinguishes four different questions:

1. **Who created or contributed the artifact?**
2. **Where did the technical material originate?**
3. **What rights govern the material?**
4. **How did the artifact enter the ANARCHY research corpus?**

A source can answer one question without answering the others.

For example, a third-party Apache-licensed file may be valid research evidence and may be redistributed under its license while remaining third-party work. A technical idea inspired by prior art may influence ANARCHY without becoming evidence of common authorship.

## Classification

### ANARCHY-original

Work authored specifically for ANARCHY by its project contributors and not copied from an existing work.

### Third-party open source

Software originating outside ANARCHY and distributed under an identified open-source license. Preserve the original license and attribution requirements.

### Modified open source

An existing open-source work modified or incorporated by ANARCHY. Record the upstream repository, version/commit, original license, and modifications. Do not classify the upstream work as ANARCHY-original.

### Public domain / CC0

Material for which public-domain status or a CC0 dedication can be established from a primary source. Preserve the evidence supporting that classification.

### Historical / archival evidence

Material preserved because it establishes that an artifact, implementation, publication, configuration, or technical practice existed at a particular time. Historical evidence is not automatically ANARCHY-original.

### User-supplied evidence

Material supplied by the project author for provenance analysis. Record what was supplied, the date received, and what can and cannot be independently established from it.

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

## Project-history chain

The ANARCHY project history should also preserve the evolution of the author's work as a sequence of independently verifiable artifacts:

```text
PERSONAL RESEARCH / OBSERVATION
          ↓
IDEA / QUESTION
          ↓
EXPERIMENT
          ↓
SOURCE COLLECTION
          ↓
LOCAL ARTIFACT
          ↓
GIT REVISION
          ↓
COMMIT / HASH
          ↓
PUBLIC OR PRIVATE REPOSITORY
          ↓
TEST / VALIDATION
          ↓
DOCUMENTED RESULT
          ↓
RELEASE / LICENSE / TECHNOLOGY TRANSFER
```

The existence of an entry in this chain establishes an evidence point only to the extent supported by the underlying record.

## Authorship and contribution policy

The project prefers an **individual-authorship / author-of-origin** record when the evidence supports that characterization. Company affiliation, employment, collaboration, institutional association, or use of third-party infrastructure must not automatically replace the documented origin of an individual contribution.

At the same time, this repository must not claim sole authorship over third-party code, standards, papers, datasets, libraries, or other works merely because they appear in the research corpus.

External contributions should identify:

- contributor;
- contribution date;
- affected artifact;
- commit or revision;
- applicable license/CLA or other contribution terms;
- upstream origin where applicable;
- whether the contribution is original, derivative, or third-party material.

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
employment/commissioning terms
```

CC0 can address copyright and related rights to the extent legally possible, but does not automatically waive unrelated rights or statutory restrictions.

## Government-originated software

The FEC provides a useful documented model: government-created software can be treated as public-domain work, while existing OSS modified by government personnel may retain third-party licensing/provenance requirements. See `docs/research/FEC_OPEN_SOURCE_PROVENANCE.md`.

Government references in the ANARCHY corpus must therefore be classified according to evidence. Mention of a government agency, standard, publication, grant, or technology does not establish government authorship, sponsorship, procurement, control, or endorsement of ANARCHY.

## Configuration and deployment artifacts

Configuration files are provenance-bearing artifacts even when they contain little executable code. For example, a Tomcat `context.xml` carrying an Apache License 2.0 header should be recorded as a configuration artifact with its licensing/header information preserved. The file may demonstrate Tomcat application-context behavior, but it does not by itself establish authentication, authorization, ownership, or an ANARCHY authorization-agent implementation.

For such artifacts preserve:

- exact file path when known;
- source distribution/repository when known;
- complete license header;
- relevant version/release;
- hash where available;
- local modifications;
- deployment context;
- date observed;
- evidence source;
- classification.

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

## Evidence standards

Evidence should be ranked approximately as follows:

**Tier 1 — Primary technical record**

- Git commit;
- signed release;
- repository history;
- original source file;
- build artifact with reproducible hash;
- official standard/specification;
- official institutional record.

**Tier 2 — Direct contemporaneous evidence**

- dated documentation;
- archived official page;
- conference publication;
- contemporaneous project announcement;
- recorded presentation.

**Tier 3 — Secondary evidence**

- later summaries;
- news coverage;
- third-party documentation;
- community discussion.

**Tier 4 — Hypothesis / interpretation**

- technical similarity;
- pattern matching;
- inferred relationship;
- unverified attribution.

Tier 4 material must remain explicitly labeled as hypothesis and must not be converted into factual provenance merely through repetition.

## Research discipline

A technical similarity is not proof of common authorship. A hyperlink is not proof of sponsorship. A shared dependency is not proof of organizational control. A repository license is not proof that every file has the same provenance.

Primary evidence should be preferred over secondary commentary. When uncertainty remains, record it explicitly rather than converting a hypothesis into a fact.

## Maintenance rule

Every substantive provenance update should itself become a Git revision. Where possible, preserve the previous record rather than silently rewriting history. Corrections should state what changed and why.

Recommended commit pattern:

```text
provenance: record <artifact/event> and evidence
```

The Git history is therefore part of the provenance system rather than merely a transport mechanism for source code.
