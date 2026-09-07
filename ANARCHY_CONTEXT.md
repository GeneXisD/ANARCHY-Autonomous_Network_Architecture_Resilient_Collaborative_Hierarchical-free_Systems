# ANARCHY — Canonical Continuation Context

**Purpose:** This file is the canonical handoff/context document for continuing ANARCHY work across ChatGPT sessions, collaborators, agents, and tooling.

> **Continuation directive:** When beginning work on this repository, read `ANARCHY_CONTEXT.md` first. Treat it as the project-level source of truth for current architecture, terminology, research scope, evidence discipline, and unresolved items. Then inspect the relevant repository files before making changes.

## 1. Project identity

**Project:** ANARCHY — Autonomous Network Architecture for Resilient, Collaborative, Hierarchy-free Systems.

**Repository:** `GeneXisD/ANARCHY-Autonomous_Network_Architecture_Resilient_Collaborative_Hierarchical-free_Systems`

ANARCHY is a research and engineering framework for autonomous, resilient, collaborative, distributed and hierarchy-free systems. It combines networking, reproducible software construction, provenance, archival evidence, distributed persistence, provisioning, licensing analysis, knowledge transfer, and device-recovery/restore research.

The project is not limited to one executable. It is a corpus, architecture, build/provisioning model, provenance system, and experimental integration layer.

## 2. Primary system goal

A major current objective is to **replicate the observable/open-source host-side model of Apple restore** without attempting to defeat proprietary security controls.

Safe scope:

- device identification;
- legitimate firmware/image acquisition;
- IPSW/image extraction and inspection;
- partition/GPT handling;
- recovery/restore interfaces documented by open-source projects;
- filesystem/image construction where legitimately supported;
- kernel and module construction;
- reproducible toolchains;
- package/provisioning automation;
- integrity verification and provenance;
- post-restore validation;
- local orchestration/distribution through ANARCHY/RitualMesh.

Out of scope:

- Activation Lock bypass;
- FRP bypass;
- secure-boot bypass;
- proprietary signing circumvention;
- unauthorized device access;
- defeating device authorization mechanisms.

Conceptual restore pipeline:

```text
device identification
    ↓
firmware/image acquisition
    ↓
IPSW/image extraction
    ↓
partition/GPT handling
    ↓
boot/recovery interfaces
    ↓
filesystem/image construction
    ↓
kernel + modules
    ↓
integrity/signature verification where legitimately supported
    ↓
restore/flash
    ↓
post-restore validation
    ↓
ANARCHY/RitualMesh local distribution and orchestration
```

## 3. Core open-source Apple restore research

Primary components to investigate and integrate as appropriate:

- `usbmuxd`
- `libimobiledevice`
- `libimobiledevice-glue`
- `libirecovery`
- `idevicerestore`
- `libplist`
- `libtatsu` where relevant to current upstream workflows

These are host-side/open-source restore ecosystem components. They are not interchangeable with Android/Qualcomm EDL tooling.

## 4. ANARCHY's build/provisioning model

The central engineering idea is:

```text
SOURCE
  ↓
COMPONENT IDENTIFICATION
  ↓
LICENSE / COPYRIGHT / NOTICE EXTRACTION
  ↓
DEPENDENCY MANIFEST
  ↓
CROSS-TOOLCHAIN / BUILD ENVIRONMENT
  ↓
REPRODUCIBLE BUILD
  ↓
TEST / VALIDATE
  ↓
SBOM + PROVENANCE
  ↓
PACKAGE
  ↓
HASH / SIGNATURE
  ↓
LOCAL REPOSITORY
  ↓
ONE-CLICK / DECLARATIVE PROVISIONING
  ↓
DEPLOYMENT / RESTORE / TEST
```

Important distinction:

```text
BUILD ≠ RELEASE ≠ PROVISION ≠ DEPLOYMENT
```

ANARCHY should preserve those stages separately so that source provenance, build configuration, generated artifacts, signatures, and installation actions remain auditable.

## 5. XAMPP model

XAMPP is a key architectural precedent for ANARCHY because it demonstrates how independently licensed software can be assembled into a developer distribution and installer/build system.

Important principles:

- XAMPP is a compilation/distribution of free software, not a single-license grant covering every bundled component.
- The XAMPP compilation has its own licensing terms while contained products retain their own licenses.
- Individual component licenses, copyrights, notices, and trademarks must be tracked separately.
- XAMPP's build/installer infrastructure is more relevant to ANARCHY than merely the Apache/PHP/MariaDB stack.
- XAMPP historically integrated one-click application packaging, including WordPress and other applications, demonstrating an application-provisioning model.
- The public `ApacheFriends/xampp-build` repository is relevant as a build/distribution engineering reference.

ANARCHY interpretation:

```text
upstream sources
      ↓
component builds
      ↓
licensed artifact set
      ↓
installer/package metadata
      ↓
local ANARCHY repository
      ↓
one-click provisioning
```

Do not describe this as making all software "free" in the legal sense. The correct model is **no separate XAMPP distribution fee from XAMPP's perspective plus independent component licensing obligations**.

## 6. One-click provisioning model

openSUSE One Click Install/YMP is a second major precedent.

The important concept is declarative provisioning:

```text
manifest
  ↓
repository definitions
  ↓
package selection
  ↓
architecture/version handling
  ↓
user confirmation
  ↓
repository/package installation
```

ANARCHY should eventually have a machine-readable manifest format for complete environments and restore toolchains.

Candidate artifact:

`manifests/anarchy-restore.yaml`

Candidate provisioning areas:

- openSUSE/YMP model;
- XAMPP-style installer/build model;
- WordPress/application packaging;
- Kubernetes/open-source orchestration tools;
- iDevice restore tools;
- local repository services;
- RitualMesh distribution.

## 7. Tomcat/Ant build model

The Apache Ant/Tomcat build material supplied during research is an important build-system precedent.

It demonstrates:

```text
SOURCE
  ↓
BUILD CONFIGURATION
  ↓
DEPENDENCY CACHE / ACQUISITION
  ↓
ANT BUILD
  ↓
TEST / VALIDATE
  ↓
PACKAGE
  ↓
SIGN / VERIFY
  ↓
DISTRIBUTE
```

Important lessons for ANARCHY:

- configuration belongs outside source where practical;
- dependency caches should be explicit;
- normal builds and release builds should be distinct;
- tests and source validation are first-class stages;
- generated artifacts should have deterministic provenance;
- release artifacts should be integrity-verifiable;
- builds should not require root privileges.

## 8. PHP/component license inventory model

A PHP third-party component inventory was analyzed as a model for license/provenance tracking. The relevant lesson is that a distribution can contain many components with different compatible licenses and additional notices.

Examples encountered include:

- PCRE2 — BSD-style with PCRE2 exception;
- libmagic/fileinfo;
- libmbfl;
- libgd;
- libzip-derived code;
- libarchive-derived tar code;
- libbcmath;
- OpenLDAP-derived data-generation code;
- various BSD-style, MIT-style, Apache-style and public-domain components.

ANARCHY must therefore track licenses at the **component level**, not only at the top-level distribution level.

Preferred model:

```yaml
artifact:
  name: anarchy-runtime
  version: 0.1
components:
  - name: component
    source: upstream
    version: version
    license: SPDX-ID-or-verified-text
    notices: path
    modifications: path-or-none
    upstream_commit: hash
    build_record: path
```

## 9. crosstool-NG and Linux kernel/module layer

crosstool-NG is a core build-system component for constructing reproducible cross-toolchains.

Current ANARCHY objective:

- use crosstool-NG for controlled cross-compilation;
- build the Linux kernel and required modules from traceable source;
- maintain explicit patches;
- record toolchain configuration and versions;
- produce build records and hashes;
- connect resulting modules to the restore/provisioning pipeline.

The phrase **"patch the kernel modules with crosstool-NG"** should be interpreted technically as building/rebuilding modules with an explicitly controlled cross-toolchain and applying source patches as required. crosstool-NG itself is a toolchain constructor, not a generic binary patcher.

## 10. Distributions and environments

Important environments in the ANARCHY corpus:

- Dynebolic
- Puredyne
- openSUSE
- Ubuntu 14.04 for legacy/federated-node work
- GNU/Linux source/build environments
- macOS/Apple Silicon and Intel development hosts
- Android/AOSP environments

Dynebolic/Puredyne are relevant as historical portable/live GNU/Linux environment precedents. Preserve their original identity and provenance; debranding/rebranding is a separate legal/trademark task.

## 11. openSUSE debranding/rebranding

openSUSE trademark rules must be treated separately from open-source copyright licenses.

General ANARCHY rule:

```text
OPEN-SOURCE LICENSE
        ≠
TRADEMARK PERMISSION
        ≠
COPYRIGHT OWNERSHIP
        ≠
BRAND/LOGO RIGHTS
```

If an openSUSE-derived distribution is modified and openSUSE marks must be removed under the applicable trademark rules, ANARCHY branding should be introduced explicitly rather than implying endorsement.

Keep a `trademark-audit` record for each branded artifact.

## 12. FunkyMios / iDevice provisioning

The user identifies FunkyMios as a one-click iDevice installation/provisioning component and wants it treated as a first-class iDevice provisioning node in ANARCHY.

**Verification status:** exact source/artifact and license still need to be captured in the corpus. Do not invent its license, authorship, or capabilities. Once supplied, add it under:

`10-provisioning/iDevices/funkymios/`

and record:

- upstream URL;
- version/commit;
- license;
- dependencies;
- installer behavior;
- supported devices;
- hashes;
- modifications;
- redistribution status;
- trademark considerations.

## 13. XAMPP / WordPress / Kubernetes application layer

ANARCHY is interested in the pattern demonstrated by packaged applications around XAMPP and the broader open-source ecosystem:

```text
application source
      ↓
application build
      ↓
packaging
      ↓
manifest
      ↓
local repository
      ↓
one-click installation
```

WordPress and Kubernetes are examples of independently governed open-source projects that may be provisioned by an ANARCHY environment. Their own licenses, trademarks, release processes, and dependencies remain authoritative.

## 14. Linux&C Vol. 39

The user identified **Linux&C Vol. 39 (Italian Linux magazine)** as an important research artifact.

**Verification status:** the exact issue/file has not yet been recovered into the current Library evidence set.

Do not fabricate its contents. When the exact issue is supplied, create:

`docs/research/linuxc-vol39.md`

with bibliographic metadata, table of contents, relevant technical sections, citations, and license/copyright constraints.

## 15. DC219 Open Source Software Policy

The user identifies a **DC219 Open Source Software Policy** as an important policy document, including claims about permitted handling of open-source components and Android-related licensing/rebranding.

**Critical evidence status:** the actual DC219 policy document has not yet been located in the current Library evidence available to the project.

Therefore:

- do not state that DC219 authorizes a particular relicensing action unless the actual policy says so;
- do not treat a generic OSS inventory as proof of DC219 applicability;
- do not infer trademark rights from an OSS license;
- once the actual document is supplied, preserve it as evidence and extract exact clauses into a controlled policy matrix.

Recommended future file:

`docs/licensing/dc219-policy-analysis.md`

## 16. Existing Library evidence

Known relevant Library artifacts include:

1. `3a921a83-9167-4f9a-80d1-6a9608ee20ee.txt` — large third-party software/license inventory containing many JARs and licenses including Apache, BSD, Bouncy Castle, CC0, CDDL, Eclipse/EPL, LGPL, MIT, Mozilla/MPL and others.
2. `f898404a-6047-4412-ada7-12c4fb50da94.pdf` — OSS notice/privacy-style document with numerous third-party components and licenses.
3. Several `.ini` files — primarily Cygwin package metadata, not DC219.
4. `pip(2).log` — Python package/build log material.
5. `ArminMedosch.pdf` — unrelated historical/RIXC material.

These artifacts should be treated as separate evidence classes. A license inventory is not automatically a corporate policy.

## 17. Provenance and evidence rules

Every ANARCHY research claim should distinguish:

- direct primary evidence;
- secondary evidence;
- historical evidence;
- technical similarity;
- hypothesis.

Required provenance fields where possible:

```text
artifact
upstream
repository
commit/tag
release date
access date
sha256
license
copyright holder
modifications
patches
build environment
dependencies
redistribution obligations
trademark obligations
source citation
confidence/status
```

Core evidence chain:

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
BUILD
  ↓
PACKAGE
  ↓
DISTRIBUTION
  ↓
DEPLOYMENT
  ↓
OBSERVATION / TEST
  ↓
ARCHIVAL EVIDENCE
```

## 18. ANARCHY research corpus already established

Existing major research branches include:

- InterPlanetary Wayback / ipwb;
- CarbonDate;
- Dark and Stormy Archives Puddles;
- IPFS/Kubo setup automation;
- WS-DL web-archiving research;
- University of Turin knowledge-transfer research;
- UNI-FIND knowledge/provenance model;
- patents and spin-off/incubation mechanisms;
- open-source licensing and provenance;
- GNU/Linux and distribution engineering;
- Android/AOSP;
- Apple restore tooling;
- cross-compilation;
- reproducible builds;
- distributed persistence;
- technology transfer and commercialization.

## 19. RitualMesh relationship

RitualMesh is the intended decentralized/local orchestration and distribution layer around ANARCHY research and artifacts.

Conceptual relationship:

```text
                    ANARCHY
                       │
            research/build/provenance
                       │
                       ▼
                  RitualMesh
                       │
          local distribution/orchestration
                       │
                    127.0.0.1
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
    repositories               restore/build
    artifacts                  services
```

RitualMesh should not silently become the legal owner of upstream artifacts. It is an orchestration/distribution concept; upstream licenses remain authoritative.

## 20. Proposed repository structure

```text
ANARCHY/
├── ANARCHY_CONTEXT.md
├── README.md
├── 00-research/
│   ├── Linux&C-Vol39/
│   ├── Dynebolic/
│   ├── Puredyne/
│   ├── openSUSE/
│   ├── XAMPP/
│   └── FunkyMios/
├── 10-provisioning/
│   ├── openSUSE-YMP/
│   ├── xampp/
│   ├── applications/
│   └── iDevices/
├── 20-restore/
│   ├── libimobiledevice/
│   ├── libirecovery/
│   ├── idevicerestore/
│   ├── IPSW/
│   └── device-manifests/
├── 30-build/
│   ├── crosstool-ng/
│   ├── linux-kernel/
│   ├── kernel-modules/
│   └── patches/
├── 40-distributions/
│   ├── dynebolic/
│   ├── puredyne/
│   └── opensuse-anarchy/
├── 50-branding/
│   ├── debrand-opensuse/
│   ├── anarchy-branding/
│   └── trademark-audit/
├── 60-licensing/
│   ├── dc219/
│   ├── SPDX/
│   ├── third-party/
│   └── license-matrix/
├── 70-provenance/
│   ├── hashes/
│   ├── SBOM/
│   ├── source-manifests/
│   └── build-records/
└── docs/
    ├── architecture/
    ├── provenance/
    ├── licensing/
    ├── branding/
    └── research/
```

This is a target architecture, not a claim that every directory currently exists.

## 21. Canonical continuation instruction

When a future session starts, the user can say:

> **"Open ANARCHY_CONTEXT.md and continue from the canonical ANARCHY context."**

The agent should then:

1. read `ANARCHY_CONTEXT.md`;
2. inspect the current repository state;
3. identify what is already implemented versus proposed;
4. preserve evidence-status distinctions;
5. continue from the last repository state rather than asking the user to repeat the architecture;
6. update this context file when a durable architectural decision changes;
7. never convert an unverified claim into established fact.

## 22. Current unresolved evidence queue

- [ ] Recover and analyze the actual DC219 policy document.
- [ ] Recover the exact Linux&C Vol. 39 artifact.
- [ ] Capture the exact FunkyMios upstream/source/license.
- [ ] Inventory existing ANARCHY files against the target structure.
- [ ] Add complete Apple restore component provenance.
- [ ] Add crosstool-NG/toolchain manifests.
- [ ] Add kernel/module build manifests and patch records.
- [ ] Build the component-level SPDX/license matrix.
- [ ] Add SBOM generation and verification tooling.
- [ ] Add machine-readable restore/provisioning manifest.
- [ ] Add source/hash/build-record automation.
- [ ] Audit openSUSE-derived branding separately from software licenses.

## 23. Change-control rule

Do not silently rewrite project history. Prefer feature/topic branches and pull requests for substantial changes. Keep `main` stable. GitHub recommends branches and pull requests for isolated development and protected important branches. See the official GitHub repository and branch-protection guidance.

## 24. Status vocabulary

Use these exact labels when practical:

- **VERIFIED** — directly supported by a primary source or inspected artifact.
- **SUPPORTED** — supported by credible evidence but not yet fully primary-source verified.
- **UNVERIFIED** — asserted or suspected but not yet established.
- **HYPOTHESIS** — analytical possibility requiring evidence.
- **PROPOSED** — architecture/design not yet implemented.
- **IMPLEMENTED** — present in the repository and tested/inspected.
- **BLOCKED** — cannot proceed without a missing artifact, permission, or technical dependency.

Last baseline: **2026-09-07**.
