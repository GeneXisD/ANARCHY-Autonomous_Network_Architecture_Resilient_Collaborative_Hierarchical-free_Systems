# phpMyAdmin Copyright and Third-Party License Notice — Evidence Record

## Identification

This record preserves the copyright and licensing notice supplied for the phpMyAdmin artifact corpus. The notice identifies copyright coverage for:

- Tobias Ratschiller, 1998-2000;
- Marc Delisle, 2001-2018;
- Olivier Müller;
- Robin Johnson;
- Alexander M. Turek;
- Michal Čihař;
- Garvin Hicking;
- Michael Keck;
- Sebastian Mendel;
- and additional contributors referenced by the project's credits.

The notice states that the program is free software and may be redistributed and/or modified under the GNU General Public License as published by the Free Software Foundation. It also states the standard warranty disclaimer and directs recipients to the GNU GPL text.

## Third-party licensing topology

The supplied notice explicitly distinguishes the phpMyAdmin program license from third-party components.

It states that phpMyAdmin includes third-party libraries under their respective licenses. It specifically identifies jQuery files under `js/vendor/jquery/` as available under MIT and GPL licensing, with copies of the relevant notices in the repository. It also states that the download kit contains Composer libraries whose licensing information is located in the `vendor/` directory.

This is significant for ANARCHY because it provides direct evidence of a component-level licensing model inside a larger software distribution:

```text
phpMyAdmin program
       |
       +--> project copyright / GPL terms
       |
       +--> bundled jQuery files
       |       +--> MIT
       |       +--> GPL
       |
       +--> Composer libraries
               +--> component-specific notices
```

## Provenance status

**Status: SUPPORTED**

The supplied notice is internally coherent with the phpMyAdmin licensing model already represented in the ANARCHY evidence corpus. It should be retained as evidence rather than treated as a standalone legal opinion.

The exact byte-level origin of the supplied notice has not yet been hash-matched to a particular phpMyAdmin release/tag. The copyright years and contributor list also indicate that this notice belongs to a historical project state and should not automatically be applied to every phpMyAdmin release.

## Legal interpretation boundary

This record does not determine ownership of any individual contribution, patent rights, trademark rights, or contractual permissions. It records what the supplied notice says about copyright and software licensing.

In particular:

```text
COPYRIGHT NOTICE
      !=
COMPLETE COPYRIGHT CHAIN OF TITLE
      !=
TRADEMARK PERMISSION
      !=
PATENT LICENSE
      !=
CORPORATE OSS POLICY
```

The notice's reference to GPL permissions should therefore be analyzed together with the exact source files, third-party notices, release metadata and applicable version of the GPL.

## ANARCHY relevance

The most important architectural evidence is not the GPL text itself but the explicit separation of:

1. project-level copyright and license;
2. third-party component licenses;
3. bundled license notices;
4. distribution-kit dependency licensing.

This supports ANARCHY's requirement for component-level SBOM and provenance records rather than a single aggregate license label for an entire distribution.

## Reproducibility target

To upgrade this evidence from SUPPORTED to VERIFIED, record:

- exact phpMyAdmin release/tag;
- exact source-file path containing the notice;
- upstream Git/blob identifier;
- SHA-256 of the supplied file and upstream file;
- release archive SHA-256 and/or signature verification;
- complete third-party notice inventory for that release;
- relationship between the notice and the source files to which it applies;
- any local modifications in the historical copy supplied to ANARCHY.

## Evidence status

**Current: SUPPORTED**

**Upgrade path:** SUPPORTED -> VERIFIED when the supplied notice is hash-matched to an identified upstream release/blob.

## Relationship to advisory-rules evidence

This notice should be cross-referenced with `evidence/phpmyadmin-advisory-rules.md`. The two artifacts establish complementary evidence:

- the advisory rules demonstrate a declarative operational-analysis mechanism;
- the copyright notice demonstrates project-level and component-level licensing boundaries.

Neither artifact alone establishes that phpMyAdmin is a direct ancestor, dependency, or source of ANARCHY. The appropriate current relationship is **historical/technical precedent and licensing/provenance evidence**.
