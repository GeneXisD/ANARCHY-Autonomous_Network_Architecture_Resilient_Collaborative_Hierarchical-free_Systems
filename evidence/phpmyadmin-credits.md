# phpMyAdmin Credits and Historical Lineage — Evidence Record

## Identification

This record preserves the supplied phpMyAdmin `credits` documentation as historical provenance evidence.

The supplied text is corroborated by the official phpMyAdmin 4.9.9 documentation, whose Credits page contains the same chronological contributor history and the same `Original Credits of Version 2.1.0` section. The documentation identifies Tobias Ratschiller as creator of phpMyAdmin, records Marc Delisle's early multilingual work and SQL analyzer contributions, and records later contributors responsible for authentication, database maintenance, configuration, export/import, query history, tracking, replication, testing, security assessment and other subsystems. citeturn0search1turn0search5

The official documentation also preserves the original 2.1.0 statement that phpMyAdmin was based conceptually on Peter Kuppelwieser's MySQL-Webadmin, while explicitly stating that its source code was not used. That distinction is important: the upstream project itself separates conceptual influence from copied source. citeturn0search1

## What this evidence establishes

The credits document is more than a list of names. It is a historical map of subsystem provenance.

Examples include:

- **Project origin:** Tobias Ratschiller — creation and early maintenance.
- **Internationalization and SQL analysis:** Marc Delisle.
- **SourceForge/CVS consolidation and language infrastructure:** Olivier Müller.
- **Authentication and database/network policy:** Robin Johnson, including IP Allow/Deny and DB-based configuration work.
- **Export and distribution features:** Armel Fauveau and other contributors.
- **Database compatibility and privileges:** Alexander M. Turek.
- **Query history, transformations, comments and relational/PDF features:** Garvin Hicking.
- **Cookie authentication:** Piotr Roszatycki and Dan Wilson.
- **Tracking:** Alexander Rutkowski.
- **Replication support:** Tomáš Srnka.
- **Automated testing:** multiple Google Summer of Code contributors.
- **Security assessment:** Emanuel Bronshtein.
- **Modern JavaScript/build tooling and templating:** Maurício Meneghini Fauth and later contributors.

These are useful provenance signals because the configuration corpus supplied alongside this evidence contains many of the same subsystem categories: authentication, allow/deny policy, configuration storage, bookmarks, export/import, query history, tracking, testing/debugging, and security controls.

## Important historical lineage boundary

The original credits explicitly describe phpMyAdmin as conceptually based on MySQL-Webadmin while also stating that phpMyAdmin did not use its source code. This is a strong example of why ANARCHY must distinguish:

```text
conceptual influence
      !=
source-code ancestry
      !=
dependency
      !=
authorship
      !=
license inheritance
```

ANARCHY should apply the same standard to its own historical corpus. A technical similarity or conceptual predecessor is not sufficient evidence of copied implementation or direct dependency.

## Relationship to the configuration and advisory evidence

The credits document provides a third dimension to the existing phpMyAdmin evidence set:

```text
phpMyAdmin credits
      |
      +--> contributor/subsystem provenance
      |
      +--> historical project lineage
      |
      +--> conceptual-influence disclosures
      |
      v
configuration documentation
      |
      +--> policy
      +--> identity
      +--> state
      +--> trust boundaries
      +--> audit/history
      |
      v
advisory rules
      |
      +--> observed state
      +--> deterministic tests
      +--> findings
      +--> recommendations
      |
      v
ANARCHY evidence / provenance model
```

Together, these artifacts provide a useful historical precedent for treating a complex software system as a collection of identifiable subsystems with distinct provenance, configuration, operational behavior and licensing boundaries.

This remains a **technical/historical precedent**, not evidence that phpMyAdmin is a direct ancestor, dependency, or source of ANARCHY.

## Licensing and attribution boundary

Credits are attribution/provenance evidence. They do not, by themselves, establish:

- ownership of every contribution;
- a complete chain of title;
- patent rights;
- trademark permissions;
- contractual permissions;
- the license applicable to every historical file;
- or permission to reuse individual contributions outside the applicable project license.

The separate phpMyAdmin copyright/third-party notice remains the appropriate evidence for the project-level GPL and component-level licensing topology. See `evidence/phpmyadmin-copyright.md`.

## Provenance status

**Status: SUPPORTED**

The supplied credits are strongly corroborated by official phpMyAdmin documentation, including the 4.9.9 documentation set. citeturn0search1turn0search5

The exact supplied file has not yet been byte-for-byte hash matched to a specific upstream release archive or Git blob. Therefore this record does not claim VERIFIED byte-level provenance for the local artifact.

## Reproducibility target

To upgrade this evidence from SUPPORTED to VERIFIED, record:

- exact phpMyAdmin release/tag;
- exact upstream documentation source path;
- upstream Git/blob identifier where available;
- SHA-256 of the supplied file;
- SHA-256 of the matched upstream file;
- release archive SHA-256 and/or signature verification;
- any local formatting or textual modifications.

## ANARCHY relevance

This evidence strengthens three ANARCHY requirements:

1. **Subsystem provenance:** historical credits can identify who contributed major functional areas without converting attribution into unsupported ownership claims.
2. **Evidence lineage:** upstream projects themselves may document conceptual influence separately from source-code reuse; ANARCHY should preserve that distinction.
3. **Enterprise SBOM/provenance:** component and subsystem records should remain traceable to source, version, license and historical evidence rather than relying on an aggregate project label.

**Current relationship:** historical/technical precedent and provenance evidence.
