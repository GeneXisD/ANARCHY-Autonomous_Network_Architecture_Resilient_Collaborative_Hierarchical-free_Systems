# FEC Open-Source Provenance Research

## Purpose

This document records primary-source evidence relevant to ANARCHY's software-provenance, public-domain, open-source, government-reuse, interoperability, and commercialization research.

The Federal Election Commission (FEC) is treated here as a documented government reference model. Inclusion does not imply that the FEC, GSA/18F, or any other institution endorses ANARCHY or is connected to ANARCHY.

## 1. FEC Open Source Policy

The FEC Open Source Policy establishes a provenance distinction between software created by FEC staff/contractors and existing open-source software that FEC staff modify. FEC-created source code is treated as public-domain work by default, subject to the policy's exceptions. Existing OSS modified by FEC personnel can constitute a joint work, with the original OSS license continuing to apply to the applicable portion.

The policy also addresses rights, legal restrictions, security considerations, release review, contribution, procurement, reuse, and open-source development practices.

Primary source:
- https://github.com/fecgov/FEC/blob/master/OPEN-SOURCE-POLICY.md

## 2. CC0 implementation

The FEC policy identifies CC0 as the mechanism used to permanently waive copyright and related rights worldwide for covered FEC-created software. CC0 does not eliminate unrelated patent, trademark, privacy, publicity, or statutory restrictions.

Primary source:
- https://creativecommons.org/publicdomain/zero/1.0/

FEC repository license evidence:
- https://github.com/fecgov/FEC/blob/master/LICENSE.md

## 3. Mixed-provenance repositories

FEC repositories explicitly describe a mixture of:

1. open-source works that are not in the public domain; and
2. open-source work created by the U.S. government that is in the public domain.

The repository-level license therefore must not be interpreted as changing the license of every third-party component. Component-level provenance and license notices remain authoritative for those components.

Primary sources:
- https://github.com/fecgov/openFEC/blob/master/LICENSE.md
- https://github.com/fecgov/fec-cms/blob/master/LICENSE.md
- https://github.com/fecgov/fecfile-web-api/blob/master/license.md

## 4. Contributions

FEC contribution guidance brings external contributions into the project's licensing framework. The contribution process is therefore part of provenance governance, not merely a social-code-of-conduct matter.

Primary source:
- https://github.com/fecgov/openFEC/blob/master/CONTRIBUTING.md

## 5. OpenFEC and API ecosystem

The FEC's software ecosystem includes openFEC, FEC CMS, FEC infrastructure, FECFile components, validation, regulations-related projects, and other repositories. The openFEC package metadata identifies CC0-1.0 as its package license.

Primary sources:
- https://github.com/fecgov
- https://github.com/fecgov/openFEC

## 6. FEC + 18F/GSA modernization

FEC public materials document collaboration with 18F/GSA around modernization of FEC.gov and its API/open-development approach. The FEC's 2016 e-filing study describes open source as a means of enabling commercial software vendors to integrate with FEC systems and cites the broader government-open-source rationale that private-sector businesses can build around government-developed code.

Primary sources:
- https://www.fec.gov/updates/fec-hosts-public-forum-on-website-improvement/
- https://www.fec.gov/about/reports-about-fec/agency-operations/e-filing-study-2016/recommendation-3-help-those-who-help-filers/
- https://www.fec.gov/about/reports-about-fec/agency-operations/e-filing-study-2016/how-move-forward-software-development-workflow-technical-road-map/

## 7. FECFile modernization

In 2024 the FEC announced an $8.8 million Technology Modernization Fund award for modernization of FECFile. FEC public materials describe the resulting web-oriented work as open source and state that vendors and state agencies can use it to develop their own systems. Later FEC budget material refers to the program as FECfile+ and describes continued deployment/development.

Primary sources:
- https://www.fec.gov/updates/fec-receives-88-million-award-to-modernize-agencys-electronic-filing-system/
- https://www.fec.gov/resources/cms-content/documents/fy27-fec-congressional-budget-justification.pdf

## 8. Copyright is not the same as statutory data-use restrictions

FEC software rights and FEC campaign-finance data restrictions must be analyzed separately. A public-domain or CC0 software release does not itself waive statutory restrictions governing particular categories of FEC data.

Primary source:
- https://www.fec.gov/legal-resources/court-cases/fec-v-political-contributions-data/

## 9. Evidence model derived from the FEC record

```text
AUTHOR / GOVERNMENT / CONTRACTOR
             |
             v
        SOFTWARE ARTIFACT
             |
             v
       PROVENANCE REVIEW
             |
      +------+-------+----------------+
      |              |                |
   ORIGINAL        EXISTING OSS     UNKNOWN
   GOVERNMENT      / MODIFIED       / NEEDS REVIEW
      |              |                |
      v              v                v
 PUBLIC DOMAIN    ORIGINAL LICENSE   HOLD / RESEARCH
      |
      v
    CC0
      |
      v
WORLDWIDE REUSE
      |
      +-------------------+
      |                   |
      v                   v
 OUTSIDE DEVELOPERS    COMMERCIAL VENDORS
      |                   |
      +---------+---------+
                v
       NEW SOFTWARE / SERVICES
```

This is a research abstraction derived from documented FEC practices. It is not a claim that every FEC project follows every step identically.

## 10. ANARCHY application

ANARCHY should adopt the same separation of concerns:

- authorship/provenance;
- copyright status;
- third-party license obligations;
- public-domain/CC0 status;
- statutory or contractual restrictions;
- contribution terms;
- security/release review;
- redistribution rights;
- commercialization pathways.

No component should be classified as ANARCHY-original merely because it has been copied, modified, or integrated.

## Evidence classification

**Institutional evidence; licensing evidence; provenance reference; government open-source model; commercialization/interoperability reference.**
