# phpMyAdmin Advisory Rules — Evidence Record

## Identification

The supplied artifact is a phpMyAdmin advisory-rules definition file using the legacy `advisory_rules_generic.txt` rule language consumed by phpMyAdmin's `Advisor.php` parser.

The artifact contains rules for MySQL/MariaDB operational analysis including:

- server uptime and query volume;
- slow-query logging and query rates;
- MySQL release/version checks;
- source/distribution detection and Percona detection;
- 32-bit/64-bit architecture checks;
- query-cache behavior;
- sort, join and table-scan rates;
- temporary-table behavior;
- MyISAM key/index caching;
- open files and table-cache pressure;
- table locks;
- thread cache and connection behavior;
- aborted connections/clients;
- InnoDB configuration and log sizing;
- MyISAM concurrent inserts.

## Provenance assessment

**Status: SUPPORTED**

The supplied text is independently corroborated as the phpMyAdmin `libraries/advisory_rules_generic.txt` artifact family. Debian's packaged phpMyAdmin 5.0.4 source tree contains `libraries/advisory_rules_generic.txt`, and its generated translation catalog identifies the same rule names, formulas and source-file line references. The rule set also appears in phpMyAdmin 5.0.x-era distribution archives.

The exact version of the supplied text is **not yet cryptographically matched to a specific release artifact**. Do not label the supplied copy as an exact 5.0.4 release file until its SHA-256 or repository blob hash is compared with the corresponding upstream release source.

## Historical significance

This artifact is relevant to the ANARCHY lineage because it is an example of an older, declarative, data-driven operational-analysis system embedded in a web/database administration stack.

The rules separate:

1. an observed server variable or status counter;
2. a calculated metric;
3. a threshold/test;
4. a human-readable problem statement;
5. an operational recommendation; and
6. a formatted justification containing the calculated result.

This is directly relevant to ANARCHY's evidence/provenance architecture because it demonstrates a historical pattern of turning machine-observable state into deterministic diagnostic assertions without hard-coding every recommendation into procedural application logic.

The sequential `fired('rule name')` mechanism is particularly significant: rule evaluation has explicit ordering and dependency semantics. That provides a historical precedent for documenting rule-engine behavior, evidence state transitions and reproducible diagnostics.

## Architectural placement

Primary ANARCHY areas:

- `40-distributions` / historical web-stack and database tooling lineage;
- `70-provenance` / evidence and deterministic diagnostic rules;
- licensing/SBOM corpus for PHP/web/database distributions;
- enterprise readiness / operational observability.

Relationship to the existing lineage:

```text
PHP / Apache / MySQL web stack
        |
        v
   phpMyAdmin
        |
        v
Declarative advisory rules
        |
        +--> observed server state
        +--> deterministic calculations
        +--> threshold evaluation
        +--> operator recommendation
        |
        v
ANARCHY evidence/provenance model
        |
        v
reproducible diagnostics / enterprise observability
```

This is a **technical precedent**, not evidence that phpMyAdmin was an ancestor, dependency, or direct source of ANARCHY. Any stronger historical connection requires additional evidence.

## Licensing / copyright

The phpMyAdmin project is GPL-2.0 licensed. phpMyAdmin's 5.0.4 documentation states that the program may be redistributed and modified under the GNU General Public License version 2, while third-party libraries retain their respective licenses.

This evidence record does **not** make a relicensing or ownership determination for the supplied artifact. The exact upstream copyright headers and release-specific source should be preserved before redistribution of the actual source file.

## Reproducibility target

For a future closure pass, obtain the corresponding upstream release source and record:

- phpMyAdmin release/tag;
- exact path: `libraries/advisory_rules_generic.txt`;
- upstream Git/blob identifier;
- SHA-256 of the source file;
- release archive SHA-256 and/or PGP verification;
- exact license/copyright metadata;
- relationship to `libraries/classes/Advisor.php`;
- any local modifications in the historical artifact supplied to ANARCHY.

## Evidence status

**Current: SUPPORTED**

**Upgrade path:** SUPPORTED -> VERIFIED when the supplied artifact is hash-matched to an upstream release/blob.

## External corroboration

- phpMyAdmin 5.0.4 release archive and release date: https://www.phpmyadmin.net/files/5.0.4/
- Debian phpMyAdmin 5.0.4 source package contains `libraries/advisory_rules_generic.txt`.
- phpMyAdmin 5.0.4 documentation records GPLv2 licensing and separate third-party licenses.

These external references establish the artifact family and licensing context; they do not by themselves prove that the user's supplied copy is byte-identical to a particular release.
