# ANARCHY Disclosure Record — MIT TLO Model

**Record type:** Institutional disclosure/protection model
**Record date:** 2026-09-10
**Project:** ANARCHY — Autonomous Network Architecture Resilient Collaborative Hierarchical-free Systems
**Enterprise context:** ANARCHY Systems
**Status:** Reference model / internal disclosure record

## Purpose

This record adopts the documented MIT Technology Licensing Office (TLO) disclosure model as a structural reference for ANARCHY's own invention, software, provenance, protection, and commercialization records.

It is **not** an MIT disclosure, filing, submission, endorsement, affiliation, or assignment. ANARCHY Systems has no resulting claim to MIT ownership or MIT sponsorship merely because MIT TLO materials are used as a reference.

## Primary source

MIT Technology Licensing Office, **Submit Disclosure**:
https://tlo.mit.edu/researchers-mit-community/protect/submit-disclosure

MIT Technology Licensing Office, **Software & Open Source Protection**:
https://tlo.mit.edu/researchers-mit-community/protect/software-open-source-protection

## Disclosure fields adopted for ANARCHY

The MIT TLO model identifies a detailed description of the development, funding/sponsorship information, other funding sources, conception date, public-disclosure date, and inventor/creator or submitter information as relevant disclosure data. ANARCHY therefore treats these as first-class provenance fields when applicable.

```text
DEVELOPMENT / INVENTION
        ↓
CREATOR / AUTHOR / INVENTOR
        ↓
CONCEPTION DATE
        ↓
PUBLIC DISCLOSURE DATE
        ↓
FUNDING / SPONSORSHIP
        ↓
THIRD-PARTY / OPEN-SOURCE COMPONENTS
        ↓
COPYRIGHT / LICENSE / PATENT REVIEW
        ↓
PROTECTION DECISION
        ↓
OPEN RELEASE / PROTECTED RELEASE
        ↓
COMMERCIALIZATION
```

## Software-specific treatment

MIT TLO states that software may involve separate disclosure treatment for the patentable process or algorithm and for the copyrightable software code, and that the inventors of the process or algorithm need not be identical to the authors of the code.

ANARCHY adopts that distinction without asserting that any particular ANARCHY artifact is patentable or that a disclosure itself establishes ownership.

```text
PROCESS / ALGORITHM
        ↕
SOFTWARE CODE

INVENTOR(S) may differ from AUTHOR(S)
```

## Open-source release gate

The MIT TLO material identifies disclosure, sponsorship review, and identification of third-party/open-source code and licenses as part of its own open-source release process. ANARCHY uses the same *discipline* as a release-review model:

1. identify original and third-party material;
2. record licenses and rights status;
3. identify sponsorship or contractual constraints when applicable;
4. record disclosure/protection status;
5. determine whether open release, protected release, licensing, service, product, or other commercialization is appropriate.

This complements `provenance/PROVENANCE.md` and `provenance/components.csv`.

## Public-disclosure caution

MIT TLO advises that public disclosure can affect patent-protection opportunities and specifically calls for recording the date of public disclosure. ANARCHY therefore records public disclosures as evidence events rather than assuming that publication creates or destroys any particular legal right.

For any potentially patentable matter, legal counsel or the appropriate IP professional should determine the effect of publication, filing, inventorship, ownership, and applicable jurisdiction.

## Non-affiliation statement

References to MIT, MIT TLO, Research@MIT, MIT licensing practices, or MIT open-source guidance in this repository are historical or methodological references only. They do not establish collaboration, sponsorship, employment, student status, institutional ownership, endorsement, or affiliation.

## Evidence discipline

The source itself distinguishes software licensing/protection, disclosure, and commercialization. ANARCHY likewise keeps the following separate:

- authorship;
- inventorship;
- copyright ownership;
- software license;
- patent status;
- enterprise/organization identity;
- third-party provenance;
- sponsorship or contractual obligations;
- public disclosure events;
- commercialization decisions.

## Source access date

2026-09-10
