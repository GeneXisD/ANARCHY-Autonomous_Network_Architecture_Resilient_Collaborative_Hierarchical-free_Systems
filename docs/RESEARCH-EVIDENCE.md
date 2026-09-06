# ANARCHY Research Evidence Record

**Status:** Living research document  
**Purpose:** Preserve source-backed findings, relationships, and uncertainty without collapsing evidence into unsupported conclusions.

## 2026-09-06 — Web archival + distributed persistence + knowledge transfer

### A. Web archival and temporal provenance

#### InterPlanetary Wayback (ipwb)
- GeneXisD repository: https://github.com/GeneXisD/ipwb
- Upstream: https://github.com/oduwsdl/ipwb
- Concept: WARC records are decomposed into archival content and represented through IPFS; CDXJ metadata records IPFS references; replay reconstructs archived responses.
- Documented history includes a 2016 Archives Unleashed hackathon origin and later presentations including TPDL, WADL, IIPC WAC, and Decentralized Web Summit/IPFS Lab Day.
- Primary publication DOI: https://doi.org/10.1007/978-3-319-43997-6_35
- Classification: prior art; reference implementation; distributed archival technology.

#### CarbonDate
- GeneXisD repository: https://github.com/GeneXisD/CarbonDate
- Project: http://carbondate.cs.odu.edu
- Paper: https://arxiv.org/abs/1304.5213
- Concept: estimate the creation/first appearance of web resources from archives and other observations.
- Classification: temporal provenance; archival evidence; prior art.

#### Dark and Stormy Archives Puddles
- GeneXisD repository: https://github.com/GeneXisD/dsa-puddles
- Concept: generate meaningful summaries/stories of very large web-archive collections so that collections can be differentiated without manually reviewing every memento.
- Classification: collection-level analysis; digital-preservation prior art; historical evidence.

### B. Distributed infrastructure

#### setup-ipfs
- GeneXisD repository: https://github.com/GeneXisD/setup-ipfs
- Upstream lineage: https://github.com/oduwsdl/setup-ipfs
- Kubo: https://github.com/ipfs/kubo
- Concept: GitHub Actions automation for installing and initializing IPFS/Kubo across runner platforms.
- Documented outputs include resolved version, download URL, peer ID, and a content reference for the initialized Welcome object.
- Classification: reproducible infrastructure; distributed identity; compatible technology; provenance reference.

### C. Institutional research ecosystem

#### WS-DL
- Institutional site: https://oduwsdl.github.io/
- The site documents research in web archiving, web science, digital libraries, digital preservation, information retrieval, social media, machine learning, graph methods, NLP, scholarly data, HCI, and web-archiving forensics.
- The site also lists institutional support from NSF, NEH, IMLS, NASA, DoD, DOE, ED, IIPC, Protocol Labs, and the Mellon Foundation.
- Classification: institutional context and historical evidence.
- Important limitation: a funding/support acknowledgment does not establish that every project was funded by every listed organization or that a project had a hidden/government purpose.

### D. University of Turin knowledge-transfer architecture

#### Knowledge Transfer
- Official page: https://en.unito.it/research/knowledge-transfer
- UniTo explicitly states that it promotes exploitation and commercialization of research results by transferring innovations to industry.
- The page identifies patent filing/licensing and support for industrial commercialization as major mechanisms.
- Classification: institutional evidence; knowledge-transfer model.

#### Patents
- Official page: https://en.unito.it/research/knowledge-transfer/patents
- UniTo states that its Knowledge Transfer Office evaluates industrial implementation potential, establishes NDAs, identifies exploitation opportunities, and works with inventors to identify companies interested in patent exploitation.
- Classification: institutional IP-transfer evidence.

#### Data analysis and computer science patents
- Official page: https://en.unito.it/research/knowledge-transfer/patents/data-analysis-and-computer-science
- Listed examples include detection of moving space objects in telescope fields and text categorization/analytics using statistical machine learning.
- Classification: institutional technology portfolio evidence.

#### Spin-offs
- Official page: https://en.unito.it/research/knowledge-transfer/spin-companies
- UniTo defines spin-offs as companies created to commercially exploit university research results and describes committee, Academic Senate, and Administrative Board approval processes.
- Listed software/AI-oriented examples include AEQUA TECH, DATABLOOM, Deeplomacy, DITRA SOFTWARE, METRO-POLIS, SENSE-MAKING, and S.CA.LA.
- Classification: institutional commercialization evidence.

#### 2i3T
- Official page: https://en.unito.it/research/knowledge-transfer/2i3t-incubator
- UniTo describes 2i3T as a bridge between academic research and industry, including scouting, business plans, pre-incubation, company creation, post-creation support, mentoring, and investor/partner connections.
- Classification: institutional incubation and technology-transfer evidence.

#### Third Mission
- Official page: https://en.unito.it/research/third-mission
- UniTo describes Third Mission as knowledge and university activity extending into social, cultural, and economic development and interaction with industry and society.
- Classification: institutional context.

#### UNI-FIND
- Official page: https://en.unito.it/research/ri-projects-and-outputs/uni-find-unito-space-research-innovation-and-third-mission
- UniTo describes UNI-FIND as an integrated, continuously updated interface connecting people, research activities, scientific production, groups, departments, laboratories, public engagement, technology transfer, patenting, and entrepreneurship.
- Classification: institutional knowledge-layer/interface reference.

## Evidence graph

```text
WEB RESOURCE
    │
    ├── CarbonDate ──► temporal provenance
    │
    ├── WARC ──► ipwb ──► IPFS/Kubo ──► replay
    │                         │
    │                         └── setup-ipfs ──► reproducible CI
    │
    └── archive collection ──► DSA Puddles ──► collection-level story

RESEARCH / KNOWLEDGE
    │
    ├── UNI-FIND ──► people / projects / outputs / groups / patents
    │
    ├── patent/IP protection
    │       ↓
    ├── validation / Proof of Value
    │       ↓
    ├── licensing / industrial partner
    │       ↓
    ├── 2i3T incubation
    │       ↓
    └── spin-off / start-up / market application
```

## What is directly established

1. Web archival research can use distributed content addressing and IPFS for preservation/replay.
2. Web resources can be temporally estimated from multiple archival and external observations.
3. Large archival collections can be summarized at collection level.
4. IPFS/Kubo can be provisioned reproducibly in CI workflows and can expose machine-readable peer/content references.
5. WS-DL publicly documents a research ecosystem spanning web archiving, digital libraries, preservation, data analysis, and related fields.
6. UniTo publicly documents an institutional pipeline connecting research, IP protection, validation, licensing, incubation, spin-offs, and industrial/social application.
7. UniTo publicly documents a research/innovation knowledge interface (UNI-FIND) connecting people, research outputs, groups, patents, technology transfer, and entrepreneurship.

## What remains a hypothesis

The above evidence does **not** establish that all projects are one program, one organization, or one control structure. It establishes documented technologies, institutions, processes, and relationships. Any stronger relationship requires additional primary evidence such as:

- explicit collaboration agreements;
- shared authorship or personnel;
- grant or contract records;
- patent ownership or licensing records;
- corporate ownership records;
- shared infrastructure or accounts;
- dependency or import relationships;
- explicit project acknowledgments;
- dated correspondence or meeting records;
- reproducible technical lineage.

## Research rule

**Evidence first. Interpretation second.**

Technical resemblance is useful for generating hypotheses, but provenance claims should be promoted only when supported by direct documentary evidence.
