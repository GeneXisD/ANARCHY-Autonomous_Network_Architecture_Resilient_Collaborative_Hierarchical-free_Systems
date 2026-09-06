# ANARCHY Evidence Matrix

This matrix is intentionally conservative. “Direct” means the source explicitly documents the relationship. “Context” means the source establishes an institutional or technical environment. “Hypothesis” means the relationship requires additional evidence.

| ID | Subject | Claim | Evidence level | Primary source |
|---|---|---|---|---|
| E001 | ipwb | WARC archival content can be disseminated into IPFS and replayed through a CDXJ/IPFS index | Direct | https://github.com/oduwsdl/ipwb |
| E002 | ipwb | Project history includes 2016 Archives Unleashed development and later archival/decentralized-web presentations | Direct | https://github.com/oduwsdl/ipwb |
| E003 | CarbonDate | Web resource creation/appearance dates can be estimated from archives and other evidence sources | Direct | https://github.com/oduwsdl/CarbonDate |
| E004 | CarbonDate | The work has a documented 2013 research publication | Direct | https://arxiv.org/abs/1304.5213 |
| E005 | DSA Puddles | Large web-archive collections can be summarized into meaningful “stories” | Direct | https://github.com/GeneXisD/dsa-puddles |
| E006 | setup-ipfs | IPFS/Kubo can be installed and initialized through GitHub Actions | Direct | https://github.com/oduwsdl/setup-ipfs |
| E007 | setup-ipfs | Initialization exposes peer and content references as workflow outputs | Direct | https://github.com/oduwsdl/setup-ipfs |
| E008 | WS-DL | ODU WS-DL researches web archiving, digital libraries, preservation, data analysis, ML, graph methods, NLP and related areas | Direct | https://oduwsdl.github.io/ |
| E009 | WS-DL | The public site lists institutional support from multiple public/nonprofit organizations | Direct | https://oduwsdl.github.io/ |
| E010 | UniTo | UniTo has an explicit knowledge-transfer system for research exploitation/commercialization | Direct | https://en.unito.it/research/knowledge-transfer |
| E011 | UniTo patents | UniTo evaluates inventions, may establish NDAs, and seeks licensing/exploitation opportunities | Direct | https://en.unito.it/research/knowledge-transfer/patents |
| E012 | UniTo data/CS | UniTo's patent portfolio includes data-analysis/computer-science technologies | Direct | https://en.unito.it/research/knowledge-transfer/patents/data-analysis-and-computer-science |
| E013 | UniTo spin-offs | UniTo has a formal process for granting spin-off status to research-commercialization companies | Direct | https://en.unito.it/research/knowledge-transfer/spin-companies |
| E014 | UniTo 2i3T | 2i3T acts as a bridge between university research and industry through scouting, business planning, incubation and support | Direct | https://en.unito.it/research/knowledge-transfer/2i3t-incubator |
| E015 | UniTo Third Mission | UniTo explicitly frames university activity as extending into social, cultural and economic development | Direct | https://en.unito.it/research/third-mission |
| E016 | UNI-FIND | UniTo provides an integrated interface connecting people, research, outputs, groups, patents, technology transfer and entrepreneurship | Direct | https://en.unito.it/research/ri-projects-and-outputs/uni-find-unito-space-research-innovation-and-third-mission |
| E017 | GeneXisD corpus | The same GitHub organization contains repositories representing archival, provenance, IPFS and collection-analysis artifacts | Direct | https://github.com/GeneXisD |
| E018 | Cross-project lineage | Shared authorship/upstream links should be tested by commit history, dependency data, citations and explicit acknowledgments | Method | Git histories and primary project documentation |
| E019 | Unified organization | All listed projects constitute one organization or hidden program | Not established | Requires contracts, grants, personnel, ownership, collaboration or equivalent primary evidence |
| E020 | Government/intelligence purpose | A listed institution/funder implies a hidden government or intelligence purpose for a project | Not established | Requires project-specific primary evidence |

## Recommended next evidence passes

1. Compare `GeneXisD` repository histories against upstream repositories and record exact fork/copy/derivative dates.
2. Extract author and maintainer names from the repositories and papers.
3. Build a person-to-project matrix using primary institutional biographies and publications.
4. Search patents and licensing databases for exact project names, authors, inventors, and assignees.
5. Search grant databases for project-specific awards rather than relying on institution-wide acknowledgments.
6. Identify explicit cross-links in READMEs, papers, acknowledgments, dependency manifests, CI workflows, and commit messages.
7. Preserve commit SHA, source URL, date, and interpretation for every high-value relationship.
