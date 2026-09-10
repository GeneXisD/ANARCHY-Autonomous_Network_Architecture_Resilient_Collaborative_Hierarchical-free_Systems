# Open-Source Institutional Map

## Scope

This document records the defensible relationships among FEC, Creative Commons/CC0, UC Berkeley, MIT, Oracle, and the Cygwin/RH Cygwin lineage as they relate to ANARCHY's research questions.

A listed institution is evidence of a model or documented activity. It is not evidence of sponsorship, ownership, hidden coordination, or common authorship.

## Core map

```text
                         OPEN SOFTWARE / KNOWLEDGE
                                  |
             +--------------------+--------------------+
             |                    |                    |
             v                    v                    v
          GOVERNMENT          ACADEMIA             INDUSTRY
             |                    |                    |
            FEC            +------+-------+          Oracle
             |             |              |            |
             |          Berkeley         MIT           |
             |             |              |            |
             |         OSS startups   OSS education    |
             |         + spinouts     + entrepreneurship|
             |             |              |             |
             +-------------+--------------+-------------+
                           |
                           v
                  OPEN-SOURCE ECOSYSTEM
                           |
                +----------+----------+
                |                     |
                v                     v
          COPYRIGHT LICENSES      PUBLIC DOMAIN
          GPL/MIT/Apache/etc.          |
                                      CC0
                           |
                           v
                    REUSE / REDISTRIBUTION
                           |
                           v
                 VENDORS / DEVELOPERS
                           |
                           v
                COMMERCIAL APPLICATIONS
```

## FEC

The FEC provides the strongest government-side reference in this corpus. Its Open Source Policy addresses public-domain government work, modified third-party OSS, rights review, release, contributions, procurement, and reuse. FEC public materials also document an open-source/API modernization approach and a path toward software that can be reused by vendors and state agencies.

Primary sources:
- https://github.com/fecgov/FEC/blob/master/OPEN-SOURCE-POLICY.md
- https://github.com/fecgov/openFEC
- https://www.fec.gov/about/reports-about-fec/agency-operations/e-filing-study-2016/recommendation-3-help-those-who-help-filers/
- https://www.fec.gov/updates/fec-receives-88-million-award-to-modernize-agencys-electronic-filing-system/

## Creative Commons / CC0

CC0 is the rights-dedication layer. It is not equivalent to every software license and does not erase unrelated rights or statutory restrictions.

Primary source:
- https://creativecommons.org/publicdomain/zero/1.0/

## UC Berkeley

Berkeley documents both entrepreneurship support and a dedicated Open Source Software Startup Program (OS3). OS3 explicitly addresses open-source licensing and commercialization/spin-out conditions and is therefore a direct academic OSS-to-startup reference.

Primary sources:
- https://www.berkeley.edu/entrepreneurship/
- https://ipira.berkeley.edu/open-source-software-startup-program
- https://haas.berkeley.edu/entrepreneurship-program/
- https://step.berkeley.edu/program-details

## MIT

MIT's Martin Trust Center documents entrepreneurship education, advising, accelerators, and ecosystem support. MIT News also documents an Open-Source Entrepreneurship course teaching students to initiate and manage open-source projects, consult users/mentors, and develop promotional/business plans.

Primary sources:
- https://entrepreneurship.mit.edu/
- https://entrepreneurship.mit.edu/news/open-source-entrepreneurship/
- https://sandbox.mit.edu/

## Oracle

Oracle documents a long-running commitment to open source and maintains a large open-source/third-party component ecosystem. Oracle Enterprise Manager documentation historically and currently documents Cygwin as a Windows management-agent prerequisite/tooling layer, including path mappings for Cygwin utilities. Oracle's source-code pages also document mechanisms for obtaining source for third-party OSS distributed with Oracle products.

Primary sources:
- https://www.oracle.com/a/otn/docs/oracles-commitment-to-open-source.pdf
- https://www.oracle.com/downloads/opensource/software-components-source-code.html
- https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/24.1/embsc/installing-cygwin.html
- https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/embsc/installing-cygwin-starting-ssh-daemon-overview.html
- https://www.oracle.com/database/technologies/related/berkeleydb/berkeleydb-licensing.html

## Berkeley DB connection

Berkeley DB provides a concrete technology lineage between Berkeley-originated software and Oracle stewardship. Oracle's current licensing material describes Berkeley DB's dual licensing model: an OSI-certified open-source license and a commercial license. This should be treated as a technology/provenance connection, not as evidence that UC Berkeley controls Oracle.

Primary source:
- https://www.oracle.com/database/technologies/related/berkeleydb/berkeleydb-licensing.html

## Cygwin / RH Cygwin

Cygwin is a separate historical/open-source technology lineage. Oracle documentation provides direct evidence that Cygwin was integrated into Oracle Enterprise Manager Windows provisioning workflows. The exact historical Red Hat/Cygnus Cygwin version used by a particular Oracle release must be established from the corresponding Oracle installation media/documentation before asserting an exact version relationship.

Primary sources:
- https://cygwin.com/licensing.html
- https://cygwin.com/doc/preview/faq/faq.html
- https://docs.oracle.com/cd/B13789_01/server.101/q20201/cygwin.html

## Challenge mechanisms

Oracle's historical $1 million database benchmark challenge is a corporate competitive/marketing challenge. It should be kept separate from public-sector or academic challenge-fund programs. The available 1999 contemporary reporting describes a specific Oracle/Microsoft benchmark dispute; do not generalize its terms without citing the source.

Reference:
- https://www.itprotoday.com/oracle-cloud-infrastructure/microsoft-meets-oracle-1-million-challenge

## What the map does NOT establish

This corpus does not establish a single hidden chain connecting FEC, Berkeley, MIT, Oracle, Cygwin, or Red Hat. It establishes distinct, documented mechanisms that can be compared:

1. government open-source release and reuse;
2. public-domain/CC0 dedication;
3. academic OSS commercialization;
4. entrepreneurship education;
5. enterprise OSS stewardship/integration;
6. historical POSIX/Windows interoperability tooling;
7. competitive challenge mechanisms.

Future provenance claims require primary-source evidence for the specific relationship being claimed.
