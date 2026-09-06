# ANARCHY

## Autonomous Network Architecture for Resilient, Collaborative, Hierarchy-free Systems

ANARCHY is a research and engineering framework exploring autonomous, networked, resilient, collaborative and hierarchy-free systems.

This repository preserves the technical research, standards, historical references, open-source projects, architectures, protocols, licensing information, software-provenance concepts, web-archival evidence, distributed persistence, and knowledge-transfer mechanisms relevant to ANARCHY.

> **Research discipline:** a reference included here is evidence about a technology, institution, publication, implementation, or historical relationship. It is not, by itself, evidence of a hidden relationship, ownership, sponsorship, or organizational control. Claims must be supported by primary sources where possible.

---

## Acronym

**A** — Autonomous  
**N** — Networked  
**A** — Architecture  
**R** — Resilient  
**C** — Collaborative  
**H** — Hierarchy-free  
**Y** — Systems

The acronym and terminology are research concepts and may evolve as the project develops.

---

## Core research question

How can software and network systems provide autonomy, resilience, collaboration and interoperability without requiring a permanent centralized hierarchy?

A related systems question is:

> How can research artifacts, software artifacts, archived evidence, identities, revisions, and knowledge-transfer events remain traceable as they move between people, repositories, institutions, networks, and organizations?

---

## Major research branches

- Autonomous systems
- Computer networking
- Distributed systems
- Mesh networking
- Peer-to-peer systems
- Internet architecture
- Web archiving
- Digital preservation
- Temporal provenance
- Collection-level analysis
- IPFS / content-addressed storage
- GNU/Linux
- Android/AOSP
- Open-source software
- Software licensing
- Software provenance
- Cryptographic identity
- Machine-readable identifiers
- Reproducible builds
- Distributed governance
- Trust systems
- Git and version control
- Knowledge transfer
- Technology transfer
- Research commercialization
- Patents and licensing
- Proof-of-Concept / Proof-of-Value workflows
- Incubation and spin-offs
- Technology-readiness progression

---

## Provenance model

ANARCHY research treats these as separate concepts:

```text
AUTHOR
  ↓
ARTIFACT
  ↓
REVISION
  ↓
HASH
  ↓
LICENSE
  ↓
DERIVATIVE
  ↓
DISTRIBUTION
  ↓
DEPLOYMENT
  ↓
OBSERVATION / TEST
  ↓
ARCHIVAL EVIDENCE
```

For research-transfer analysis, the model can be extended:

```text
RESEARCH
  ↓
RESULT / ARTIFACT
  ↓
PROTECTION OR OPEN RELEASE
  ↓
VALIDATION / PROOF OF VALUE
  ↓
LICENSE / PARTNERSHIP / INCUBATION
  ↓
SPIN-OFF / INDUSTRIAL APPLICATION
  ↓
DEPLOYMENT
  ↓
OBSERVABLE OUTPUT
```

Technical provenance does not by itself establish legal ownership. Likewise, technical similarity does not establish common authorship or control.

---

# Research evidence corpus

## 1. InterPlanetary Wayback (ipwb)

**Repository:** https://github.com/GeneXisD/ipwb  
**Upstream lineage:** https://github.com/oduwsdl/ipwb  
**Primary concept:** peer-to-peer permanence of web archives.

InterPlanetary Wayback (ipwb) integrates WARC web-archive records with IPFS. The documented design extracts HTTP headers and payloads from WARC records, places content into IPFS, creates a CDXJ index containing IPFS references, and reconstructs archived responses during replay.

The project history identifies development at the Archives Unleashed Web Archive Hackathon in Toronto in March 2016, followed by presentations including TPDL 2016, WADL 2016, IIPC WAC 2017, and the 2018 Decentralized Web Summit IPFS Lab Day.

Primary citation:

> Mat Kelly, Sawood Alam, Michael L. Nelson, and Michele C. Weigle. *InterPlanetary Wayback: Peer-To-Peer Permanence of Web Archives*. Proceedings of TPDL 2016, DOI: 10.1007/978-3-319-43997-6_35.

Evidence classification: **Prior art / reference implementation / provenance reference / distributed archival technology**.

Repository evidence is preserved in `ipwb` and its README.

---

## 2. CarbonDate

**Repository:** https://github.com/GeneXisD/CarbonDate  
**Project:** http://carbondate.cs.odu.edu  
**Primary paper:** https://arxiv.org/abs/1304.5213

CarbonDate estimates the creation date of web resources using web archives and other evidence sources. Its documented modules include publication dates, archives, search results, social media, backlinks, and last-modified information.

This establishes a distinct temporal-provenance layer:

```text
WEB RESOURCE
    ↓
MULTIPLE OBSERVATIONS
    ↓
ARCHIVAL / EXTERNAL EVIDENCE
    ↓
EARLIEST / ESTIMATED APPEARANCE
    ↓
TEMPORAL PROVENANCE
```

Primary citation:

> Hany M. SalahEldeen and Michael L. Nelson. *Carbon Dating The Web: Estimating the Age of Web Resources*. arXiv:1304.5213, 2013.

Evidence classification: **Prior art / temporal provenance / archival evidence**.

---

## 3. Dark and Stormy Archives Puddles

**Repository:** https://github.com/GeneXisD/dsa-puddles

The repository describes the Dark and Stormy Archives Project as an attempt to generate meaningful “stories” or summaries of web-archive collections containing tens or hundreds of thousands of archived pages (mementos). The goal is to make collections differentiable without requiring manual review of every archived document.

This contributes a collection-level interpretation layer:

```text
MEMENTOS / ARCHIVE COLLECTION
          ↓
     LARGE CORPUS
          ↓
      ANALYSIS
          ↓
    SUMMARY / STORY
          ↓
 COLLECTION-LEVEL MEANING
```

Evidence classification: **Historical evidence / collection-analysis prior art / digital-preservation research**.

---

## 4. IPFS / Kubo setup automation

**Repository:** https://github.com/GeneXisD/setup-ipfs  
**Upstream implementation lineage:** https://github.com/oduwsdl/setup-ipfs  
**Kubo:** https://github.com/ipfs/kubo

The setup action installs and initializes Kubo/IPFS in GitHub Actions environments. Its documented outputs include a resolved IPFS version, download URL, peer identity, and a content reference for the initialized Welcome object.

This is important to ANARCHY because it connects distributed persistence with reproducible automation and machine-readable peer/content identifiers.

Evidence classification: **Compatible technology / reference implementation / reproducible infrastructure / identity and provenance reference**.

---

## 5. Web Science and Digital Libraries (WS-DL) research ecosystem

**Institutional site:** https://oduwsdl.github.io/

The WS-DL research group at Old Dominion University describes research spanning web archiving, web science, digital libraries, digital preservation, information retrieval, social media, data mining, visualization, machine learning, graph neural networks, NLP, scholarly data, HCI, and web-archiving forensics.

The site also documents support from organizations including NSF, NEH, IMLS, NASA, DoD, DOE, ED, IIPC, Protocol Labs, and the Andrew W. Mellon Foundation. These acknowledgments document institutional funding/support relationships; they do **not** by themselves establish that every WS-DL project was funded by every listed organization or that a particular project had a government/intelligence purpose.

The ANARCHY corpus should therefore distinguish:

1. documented institutional support;
2. documented project funding;
3. documented authorship or collaboration;
4. inferred technical similarity.

Only the first three are positive provenance evidence. Similarity is a hypothesis requiring additional evidence.

Evidence classification: **Institutional context / historical evidence / research ecosystem**.

---

# Knowledge-transfer and commercialization layer

## 6. University of Turin (UniTo) — Knowledge Transfer

**Official knowledge-transfer portal:** https://en.unito.it/research/knowledge-transfer

UniTo explicitly describes knowledge transfer as the exploitation and commercialization of research results by transferring innovations to industry. The university identifies two major mechanisms: patent filing followed by licensing, and support for industrial commercialization of ideas developed within academia.

The documented institutional pipeline includes:

```text
ACADEMIC RESEARCH
       ↓
INVENTION / RESEARCH RESULT
       ↓
PATENT / IP PROTECTION
       ↓
EVALUATION
       ↓
PROOF OF VALUE / VALIDATION
       ↓
LICENSING / INDUSTRIAL PARTNER
       ↓
2i3T INCUBATION
       ↓
SPIN-OFF / START-UP
       ↓
MARKET / INDUSTRIAL APPLICATION
```

This is an explicit institutional process, not an inference.

### UniTo patents

https://en.unito.it/research/knowledge-transfer/patents

The UniTo Knowledge Transfer Office states that it evaluates inventions for industrial implementation, can establish NDAs, identifies exploitation opportunities, and works with inventors to identify potentially interested companies for patent exploitation contracts.

UniTo also groups patent information into areas including **Data analysis and computer science**, environment, medical imaging, nervous-system diseases, new materials, and others.

The Data Analysis and Computer Science portfolio includes, among other entries:

- detection of space objects moving in a telescope field of view;
- text categorization and analytics using storage, analysis, statistical machine learning, and classification.

Reference: https://en.unito.it/research/knowledge-transfer/patents/data-analysis-and-computer-science

### UniTo spin-offs

https://en.unito.it/research/knowledge-transfer/spin-companies

UniTo defines spin-off companies as stock corporations or limited-liability companies formed to commercially exploit research results obtained at the university and granted official spin-off status. The university describes an evaluation process involving a Spin-off Committee, business plans, commercial potential, Academic Senate review, and final Administrative Board approval.

The current list includes multiple software/AI-oriented entities, including:

- AEQUA TECH
- DATABLOOM
- Deeplomacy
- DITRA SOFTWARE
- METRO-POLIS
- SENSE-MAKING
- Strategic CApabilities LAb (S.CA.LA.)

The presence of a company in UniTo's list establishes its listing/status in that institutional page. It does **not** establish a relationship to ANARCHY or to any other project without additional evidence.

### 2i3T Incubator

https://en.unito.it/research/knowledge-transfer/2i3t-incubator

UniTo describes 2i3T as its business incubator and technology-transfer bridge between university research and the industrial ecosystem. The documented process includes scouting research ideas, developing business plans, pre-incubation, company formation, post-creation support, market development, mentoring, management training, and connections to investors and business partners.

Evidence classification: **Institutional technology-transfer model / commercialization prior art / organizational process reference**.

---

## 7. UniTo Third Mission

**Official page:** https://en.unito.it/research/third-mission

UniTo describes its “Third Mission” as extending beyond teaching and research toward social, cultural, and economic development, including interaction among university, industry, and society.

This provides the broader institutional context in which knowledge transfer, patents, incubation, open science, museums/archives, and public engagement are organized.

Evidence classification: **Institutional context / research-to-society framework**.

---

## 8. UNI-FIND: research, innovation and Third Mission knowledge graph/interface

**Official page:** https://en.unito.it/research/ri-projects-and-outputs/uni-find-unito-space-research-innovation-and-third-mission

UniTo describes UNI-FIND as a single, integrated and continuously updated interface for university know-how. It connects people, research activities, scientific production, research groups, departments, laboratories, and public-engagement activities, while promoting technology transfer, patenting, entrepreneurship, and external relationships.

For ANARCHY, this is particularly relevant as an example of a machine-navigable institutional knowledge layer connecting:

```text
PEOPLE
  ↕
RESEARCH GROUPS
  ↕
PROJECTS / OUTPUTS
  ↕
PATENTS / KNOW-HOW
  ↕
TECHNOLOGY TRANSFER
  ↕
ENTREPRENEURSHIP / EXTERNAL STAKEHOLDERS
```

Evidence classification: **Knowledge-graph/interface reference / institutional provenance / technology-transfer infrastructure**.

---

# Integrated evidence model

The current corpus supports a defensible layered model:

```text
                    RESEARCH / KNOWLEDGE
                             │
             ┌───────────────┼────────────────┐
             │               │                │
             ▼               ▼                ▼
       TEMPORAL          ARCHIVAL         INSTITUTIONAL
       PROVENANCE        PRESERVATION     KNOWLEDGE
             │               │                │
        CarbonDate          ipwb           UNI-FIND
             │               │                │
             └───────────────┼────────────────┘
                             ▼
                    EVIDENCE / CORPUS
                             │
                             ▼
                    COLLECTION ANALYSIS
                             │
                       DSA / Puddles
                             │
                             ▼
                  DISTRIBUTED PERSISTENCE
                             │
                         IPFS / Kubo
                             │
                     setup-ipfs automation
                             │
                             ▼
                  REPRODUCIBLE SYSTEMS
                             │
                             ▼
                   VALIDATION / TESTING
                             │
                             ▼
                  KNOWLEDGE TRANSFER
                             │
             ┌───────────────┼────────────────┐
             │               │                │
          PATENTS          PoV/PoC          LICENSES
             │               │                │
             └───────────────┼────────────────┘
                             ▼
                       2i3T / INCUBATION
                             │
                             ▼
                    SPIN-OFF / START-UP
                             │
                             ▼
                    INDUSTRIAL / SOCIAL USE
```

This diagram is a **research model**, not a claim that all listed projects are one organization or one hidden program.

---

# Evidence taxonomy

Every future ANARCHY reference should be tagged with one or more of:

- **Foundation** — conceptual or technical foundation.
- **Related technology** — relevant but not required by ANARCHY.
- **Prior art** — predates or informs an ANARCHY design.
- **Compatible technology** — could interoperate with ANARCHY.
- **Reference implementation** — concrete implementation demonstrating a concept.
- **Standard/specification** — formal standard or protocol.
- **License reference** — licensing/legal information.
- **Provenance reference** — establishes authorship, revision, lineage, identity, or origin.
- **Historical evidence** — establishes that something existed at a particular time.
- **Institutional evidence** — official organizational documentation.
- **Knowledge-transfer evidence** — documented research-to-industry mechanism.
- **ANARCHY-original work** — work created specifically for ANARCHY.
- **Hypothesis** — plausible connection requiring additional evidence.

Do not promote a **hypothesis** to a factual provenance claim without a primary source.

---

# Evidence-chain methodology

When investigating a suspected relationship, prefer this sequence:

1. Identify the artifact.
2. Identify its original author/owner.
3. Capture repository URL and commit history.
4. Record dates and hashes.
5. Identify cited papers, standards, licenses, and upstream repositories.
6. Follow explicit hyperlinks and dependency references.
7. Identify institutional affiliations from primary sources.
8. Check patents, grants, contracts, licensing, or company records where relevant.
9. Separate direct evidence from technical similarity.
10. Record uncertainty and alternative explanations.
11. Preserve the source URL and access date.
12. Prefer reproducible evidence over interpretation.

---

# Key primary-source links

## ANARCHY / GeneXisD

- https://github.com/GeneXisD/ANARCHY-Autonomous_Network_Architecture_Resilient_Collaborative_Hierarchical-free_Systems
- https://github.com/GeneXisD/ipwb
- https://github.com/GeneXisD/CarbonDate
- https://github.com/GeneXisD/setup-ipfs
- https://github.com/GeneXisD/dsa-puddles
- https://github.com/GeneXisD/oduwsdl.github.io

## WS-DL / web archival lineage

- https://oduwsdl.github.io/
- https://github.com/oduwsdl/ipwb
- https://github.com/oduwsdl/setup-ipfs
- https://github.com/ipfs/kubo
- https://ipfs.tech/
- https://www.w3.org/TR/WARC/
- https://arxiv.org/abs/1304.5213

## University of Turin

- https://en.unito.it/research/knowledge-transfer
- https://en.unito.it/research/knowledge-transfer/patents
- https://en.unito.it/research/knowledge-transfer/patents/data-analysis-and-computer-science
- https://en.unito.it/research/knowledge-transfer/spin-companies
- https://en.unito.it/research/knowledge-transfer/2i3t-incubator
- https://en.unito.it/research/third-mission
- https://en.unito.it/research/ri-projects-and-outputs/uni-find-unito-space-research-innovation-and-third-mission

---

# Current research interpretation

The strongest evidence currently supports a **convergent architecture of ideas** around:

- preserving web evidence;
- determining when resources appeared;
- representing large archive collections;
- reconstructing archived content;
- using content-addressed distributed storage;
- reproducibly initializing distributed infrastructure;
- maintaining machine-readable identity and references;
- connecting research outputs to institutional knowledge systems;
- validating research for practical value;
- protecting or licensing inventions;
- incubating research-derived companies;
- and transferring validated knowledge into external use.

The corpus does **not** currently prove that these separate projects constitute a single organization, covert program, or unified control structure. Establishing such a claim would require direct documentary evidence such as contracts, grant records, authorship, corporate ownership, explicit collaboration agreements, shared personnel, or other primary-source links.

That distinction is part of the ANARCHY methodology: **follow the evidence chain, preserve the provenance, and mark inference as inference.**

---

## Repository status

This repository is the research corpus and development foundation for ANARCHY. New findings should be added as dated, source-backed records rather than replacing earlier evidence with conclusions.
