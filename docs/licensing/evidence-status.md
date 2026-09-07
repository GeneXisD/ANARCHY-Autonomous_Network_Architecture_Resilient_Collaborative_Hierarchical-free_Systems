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

## Newly integrated evidence

### phpMyAdmin advisory rules

**Status: SUPPORTED**

The supplied artifact is a legacy phpMyAdmin `libraries/advisory_rules_generic.txt` rule-set definition consumed by `Advisor.php`. Its structure separates observed database/server state, calculations, tests, issue descriptions, recommendations and formatted justifications. Independent source evidence corroborates the same artifact family in phpMyAdmin 5.0.x, including Debian's phpMyAdmin 5.0.4 source package.

This is relevant to ANARCHY as a historical precedent for declarative diagnostics and evidence-driven operational analysis. It is not currently treated as proof of direct ANARCHY ancestry, dependency, or authorship.

The exact supplied copy is not yet hash-matched to a specific upstream release. Preserve the distinction between **SUPPORTED artifact identity** and **VERIFIED byte-level provenance**.

Evidence record: `evidence/phpmyadmin-advisory-rules.md`

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

```text
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
| PHP component inventory | PHP ecosystem | component-specific | component-specific | component-specific | separate | supplied inventory | SUPPORTED |
| phpMyAdmin advisory rules | phpMyAdmin | GPL-2.0 context; exact file metadata pending | possible under applicable GPL terms | possible under applicable GPL terms | phpMyAdmin marks separate | public release/source evidence | SUPPORTED |
| openSUSE-derived environment | openSUSE | component-specific | possible | component-specific | separate openSUSE trademark rules | public trademark docs | SUPPORTED |
| Linux kernel/modules | Linux upstream | GPL obligations | possible | GPL obligations | N/A | policy TBD | SUPPORTED |
| Apple restore tools | upstream projects | project-specific | possible | project-specific | Apple marks separate | policy TBD | PROPOSED |
| FunkyMios | TBD | TBD | TBD | TBD | TBD | TBD | UNVERIFIED |
| Linux&C Vol.39 | publication | publication copyright | TBD | TBD | N/A | TBD | UNVERIFIED |
| DC219 policy | TBD | policy document | TBD | TBD | TBD | actual text required | UNVERIFIED |

## Rule for future commits

If a new document changes a licensing conclusion, preserve the original evidence and update this matrix with a citation, revision date and evidence status. Never delete uncertainty merely to make the repository appear more complete.
