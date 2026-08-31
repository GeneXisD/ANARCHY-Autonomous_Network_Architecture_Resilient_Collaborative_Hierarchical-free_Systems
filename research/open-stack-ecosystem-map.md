# ANARCHY Open Stack Ecosystem Map

**Status:** Research corpus / verified references
**Date:** 2026-08-31

## Purpose

This document consolidates the components identified so far in the ANARCHY investigation. It distinguishes established facts about third-party projects from hypotheses that still require artifact-level verification.

The goal is to study how an open, administrator-controlled computing environment can be assembled from interoperable projects rather than treating any single distribution or vendor as the whole system.

This is **not** a claim that these projects are ANARCHY components. They are classified as prior art, related technology, reference implementations, infrastructure, or research inputs.

---

## 1. The emerging architecture

```text
                         ANARCHY
                            |
          +-----------------+------------------+
          |                 |                  |
       RESEARCH          BUILD/OS          SERVICES
          |                 |                  |
   +------+-------+   +-----+------+      +----+-----+
   |              |   |            |      |          |
Unstructured   Launchpad Gentoo  Puredyne  XAMPP   self-hosted apps
   |              |      |          |        |          |
   |              |   Portage    dyne:bolic  |    WordPress/Joomla
   |              |      |          |        |    wiki/CMS/etc.
   +--------------+------+----------+--------+----------+
                          |
                          v
                  OPEN GNU/Linux STACK
                          |
                    DEVICE INTEROP
                          |
             +------------+------------+
             |                         |
       usbmuxd/libusbmuxd       libimobiledevice
             |                         |
             +------------+------------+
                          |
                          v
                   Apple-device
                  interoperability
```

This diagram is a research map, not an implementation dependency graph.

---

## 2. Gentoo — source-oriented system control

Gentoo is relevant because its model emphasizes user choice, source-based package construction, and administrator control. Gentoo documentation describes Portage as the package maintenance system and notes that source-based operation allows packages and the resulting system to be tuned; USE flags can add or remove functionality. cite-reference: https://wiki.gentoo.org/wiki/Handbook:ARM64/Installation/About

A 2026 Gentoo developer article describes Gentoo as a source-first distribution where the package manager handles source builds while giving the user control over build features and dependencies. cite-reference: https://blogs.gentoo.org/mgorny/2026/05/28/why-gentoo/

### ANARCHY relevance

Gentoo is a reference for:

- source-oriented distribution
- administrator control
- configurable package features
- transparent build configuration
- architecture portability
- reducing unnecessary components through build choices

It should not be treated as an ANARCHY base merely because it is source-oriented.

---

## 3. Puredyne and dyne:bolic — live systems and remasterable environments

The dynebolic project documents a development workflow in which dependencies are prepared, development root modules are obtained, the root system is built, and an ISO is generated. The current documentation explicitly describes `make deps`, `make setup`, `make system`, `make iso`, and `make qemu` as the quick-start workflow. cite-reference: https://dyne.org/docs/dynebolic/developers/

Historical dyne:bolic documentation also describes a modular system, development tools, live-CD customization, and creation of additional software modules. cite-reference: https://lab.dyne.org/DyneBolic2

Current dynebolic describes itself as a 100% free GNU+Linux live operating system and publishes its build system. It is currently based on Devuan and its public documentation emphasizes freedom, modularity, portability, and user-controlled production. cite-reference: https://dyne.org/dynebolic/about/

### ANARCHY relevance

These projects provide prior art for:

- live operating-system artifacts
- modular system construction
- reproducible-ish ISO generation workflows
- snapshot/remaster concepts
- portable environments
- building from an existing development environment

They are particularly relevant to the separate ANARCHY concepts of **live artifact**, **installation description**, and **target installation**.

---

## 4. Launchpad — more than a distribution host

Launchpad is relevant as a software-development and collaboration ecosystem associated historically with Ubuntu and many other free-software projects. The Bouillon Cube `live-install-generator` blueprint is being retained as historical evidence:

https://blueprints.launchpad.net/bouilloncube/+spec/live-install-generator

The exact implementation details of that old blueprint should be recovered from archived revisions/source before being stated as fact. The useful research question is how a live environment could participate in generating an installed system.

### ANARCHY relevance

Launchpad contributes historical prior art for:

- project planning
- blueprints/specifications
- bug tracking
- source development
- package/distribution relationships
- collaborative free-software development

It should not be reduced to "a distribution platform."

---

## 5. openSUSE One Click Install / YMP — declarative installation intent

The openSUSE One Click Install material is relevant because it represents installation intent separately from the software payload and execution mechanism.

Primary reference:

https://en.opensuse.org/openSUSE:One_Click_Install

Historical YMP material should be treated as openSUSE/YaST-specific prior art rather than as an ANARCHY format.

### ANARCHY architectural lesson

```text
INSTALL INTENT
      |
      v
MACHINE-READABLE DESCRIPTION
      |
 +----+---------+---------+
 |              |         |
apt           zypper   other backend
 |              |         |
 +--------------+---------+
                |
                v
          TARGET SYSTEM
```

The important idea is separation of **what should be installed** from **how a particular operating system performs the installation**.

---

## 6. Bouillon Cube `live-install-generator`

Reference:

https://blueprints.launchpad.net/bouilloncube/+spec/live-install-generator

Working classification:

- historical evidence
- prior art
- live-install research

Do not currently assert unverified implementation details. The recovered blueprint/source history should eventually be archived with revision identifiers and hashes.

---

## 7. Unstructured — heterogeneous artifact ingestion

The Unstructured open-source library is designed to ingest and preprocess diverse document formats and partition documents into semantic elements and metadata. Current documentation lists support for formats including PDF, HTML, XML, Markdown, reStructuredText, Word, PowerPoint, spreadsheets, images, and more. cite-reference: https://docs.unstructured.io/open-source/introduction/overview

### ANARCHY relevance

This makes Unstructured useful as a **research-corpus ingestion layer**:

```text
PDF / HTML / XML / DOCX / RST / MD / images
                    |
                    v
             Unstructured
                    |
                    v
        semantic document elements
                    |
                    v
        provenance-aware corpus
```

Important rule: extraction must not replace the original artifact. Preserve the original file, source URI, retrieval date, revision/version where known, and cryptographic hash.

---

## 8. Sphinx — documentation as a build artifact

Sphinx is a documentation generator that converts structured plain-text documentation into multiple output formats and supports cross-referencing and extensions. Current documentation supports reStructuredText and MyST Markdown and output formats including HTML, LaTeX/PDF, ePub, and Texinfo. cite-reference: https://www.sphinx-doc.org/en/master/

`sphinx-build` takes a source directory and output directory and uses project configuration such as `conf.py`; `sphinx-quickstart` can create the initial project structure. cite-reference: https://www.sphinx-doc.org/en/master/man/sphinx-build.html

### ANARCHY relevance

Sphinx can provide the publication/build layer for:

- specifications
- research notes
- API documentation
- architecture documents
- provenance documentation
- generated reference material

Combined with Unstructured:

```text
RAW ARTIFACTS
     |
     v
EXTRACTION / PARTITIONING
     |
     v
STRUCTURED RESEARCH RECORDS
     |
     v
RST / Markdown / MyST
     |
     v
Sphinx build
     |
     +--> HTML
     +--> PDF/LaTeX
     +--> ePub
     +--> other builders
```

---

## 9. XAMPP — assembled administrator/developer environment

XAMPP is not itself an operating system. Apache Friends describes it as an easy-to-install Apache distribution containing MariaDB, PHP, and Perl. Its published packages have also included tools and services such as phpMyAdmin, OpenSSL, a control panel, Webalizer, mail/FTP components, Tomcat, and platform-specific additional libraries and tools. cite-reference: https://www.apachefriends.org/download.html

The exact component set varies by XAMPP release and platform, so historical XAMPP artifacts must be versioned before making claims about what a particular setup contained.

### ANARCHY relevance

XAMPP demonstrates a useful composition pattern:

```text
independent open components
          |
          v
integrated administrator environment
          |
          v
local development / services
```

The broader research interest is the ability to assemble and administer a useful environment from independently available components. XAMPP itself is not the proposed ANARCHY stack.

---

## 10. Self-hosted application ecosystem

The XAMPP direction led to a broader category of self-hostable applications and publishing systems.

### WordPress

WordPress describes itself as open-source software, licensed under GPLv2 or later. Its official documentation emphasizes the ability to install, modify, and redistribute the software. cite-reference: https://wordpress.org/about/

### Joomla

Joomla documentation states that Joomla is a GPL project and that Joomla software is licensed under GPL version 2 or later. cite-reference: https://docs.joomla.org/Extensions_and_GPL/en

### MoinMoin

MoinMoin is a wiki engine with its own markup and linking model; its documentation demonstrates the wiki-name/linking system and page-based knowledge model. cite-reference: https://moinmo.in/WikiName

### ANARCHY relevance

These are examples of the **application/service layer** that can sit above an administrator-controlled GNU/Linux system:

```text
GNU/Linux
   |
   +-- web server
   +-- database
   +-- scripting/runtime
   +-- wiki
   +-- CMS
   +-- publishing
   +-- collaboration
   +-- APIs/services
```

They should remain separate from the lower-level device, OS, and installation layers.

---

## 11. libimobiledevice / libusbmuxd / usbmuxd — open Apple-device interoperability

libimobiledevice describes itself as a cross-platform FOSS library for communicating with iOS devices natively. Its project ecosystem includes `libusbmuxd` and `usbmuxd`. cite-reference: https://libimobiledevice.org/

`usbmuxd` is a socket daemon that multiplexes connections over USB to iOS devices; its documentation states that higher-level layers are handled by libimobiledevice. cite-reference: https://cgit.libimobiledevice.org/usbmuxd.git/tree/docs/usbmuxd.8

The project README describes usbmuxd as an open-source implementation of the proprietary usbmuxd daemon and identifies Linux, macOS, Windows, and Android as tested platforms. cite-reference: https://cgit.libimobiledevice.org/usbmuxd.git/tree/README.md

### ANARCHY relevance

This is a concrete interoperability layer:

```text
Apple device
     |
     v
USB transport
     |
     v
usbmuxd / libusbmuxd
     |
     v
libimobiledevice
     |
     v
open applications / tools
```

This is one of the strongest technically grounded parts of the long-term open-device research direction because these projects provide actual public implementations rather than merely an architectural idea.

---

## 12. Cygnus Solutions — historical business model for free software

Cygnus Solutions is important as historical evidence that free/open-source software development, maintenance, engineering, and support can form a commercial enterprise.

Red Hat's November 15, 1999 announcement described its agreement to acquire Cygnus in a transaction valued at $674 million and characterized the combined company as focused on open-source technology, information, services, and support. cite-reference: https://www.redhat.com/en/about/press-releases/press-cygnusacquisition

### ANARCHY relevance

Cygnus is **business-model prior art**, not proof that ANARCHY itself will be commercially successful.

The relevant lesson is:

```text
free/open software
      |
      +-- engineering
      +-- maintenance
      +-- ports
      +-- tooling
      +-- support
      +-- services
      |
      v
commercial sustainability
```

---

## 13. Cygwin / Red Hat Cygwin investigation — NOT YET ESTABLISHED

Two Cygwin-related setups are being preserved for comparison. Source files are currently available for one setup but not the other.

The user's working hypothesis is that an important difference may involve components that appear **"licenseless" and "headless."**

This terminology is currently a **research hypothesis**, not an established fact.

Required evidence before making the claim:

- exact version/release
- package manifests
- source tree
- copyright notices
- COPYING/LICENSE/NOTICE files
- build specifications
- binary metadata
- dependency metadata
- runtime behavior
- comparison between the two setups

The absence of a visible license file must not automatically be interpreted as the absence of copyright or a license. The artifact-level provenance investigation will determine what is actually present.

---

## 14. Apple / GNU/Linux objective — precise formulation

The long-term direction discussed in this research is to reduce dependence on proprietary platform-controlled components by developing and using open implementations, standards, interoperability layers, build systems, and administrator-controlled infrastructure wherever legally and technically possible.

The objective is **not** to claim ownership of third-party projects or reproduce proprietary source code.

A defensible formulation is:

> **Build an open, inspectable, reproducible, administrator-controlled computing stack that can interoperate with proprietary hardware and protocols through legitimate open interfaces and independent implementations.**

This allows Apple hardware/device interoperability to be a target without making proprietary Apple implementation details a prerequisite for ANARCHY.

---

## 15. Current research layers

The corpus now has a clearer separation of layers:

```text
LAYER 0 — PROVENANCE / KNOWLEDGE
    Unstructured
    Sphinx
    RDF / structured metadata
    source archives

LAYER 1 — PROJECT / DEVELOPMENT
    Launchpad
    Git
    issue tracking
    specifications / blueprints

LAYER 2 — BUILD / SYSTEM CONSTRUCTION
    GNU toolchain
    Gentoo / Portage
    Puredyne
    dyne:bolic

LAYER 3 — INSTALLATION / DISTRIBUTION
    live-install-generator
    YMP / One Click Install prior art
    live ISO generation
    package repositories
    installation descriptors

LAYER 4 — ADMINISTRATOR SERVICES
    XAMPP-style assembled stacks
    Apache
    databases
    PHP/Perl/etc.
    self-hosted CMS/wiki applications

LAYER 5 — DEVICE INTEROPERABILITY
    usbmuxd
    libusbmuxd
    libimobiledevice
    related open device tooling

LAYER 6 — ANARCHY
    autonomous
    resilient
    collaborative
    hierarchy-free composition
```

---

## 16. What is established vs. what remains research

### Established enough to record

- Gentoo provides a source-oriented, highly configurable GNU/Linux model.
- dyne:bolic provides live, modular, free-software system/build prior art.
- Launchpad provides project/development infrastructure beyond merely hosting a distribution.
- The Bouillon Cube `live-install-generator` blueprint exists as historical Launchpad evidence.
- openSUSE One Click Install/YMP provides installation-recipe prior art.
- Unstructured provides open-source document ingestion/partitioning capabilities.
- Sphinx provides a documentation build system with multiple output builders and cross-referencing.
- XAMPP assembles multiple server/development components into an administrator-oriented environment.
- WordPress, Joomla, and wiki software demonstrate higher-level self-hostable applications.
- libimobiledevice/usbmuxd/libusbmuxd provide open-source Apple-device interoperability components.
- Cygnus provides historical evidence of commercial services around open software.

### Still requiring evidence

- The exact implementation of the historical Bouillon Cube blueprint.
- The exact relationship between Puredyne artifacts and particular dyne:bolic generations.
- The full historical YMP implementation and how much of it can be generalized.
- The two Cygwin setups and the "licenseless/headless" hypothesis.
- The exact role intended by "FunkyMios" and its relationship to openSUSE.
- Any claim that a specific Apple component can be replaced without additional hardware/firmware constraints.
- Any patent/trademark/copyright conclusion about ANARCHY or third-party projects.

---

## 17. Research discipline

For every external artifact, preserve:

```text
NAME
ORIGINAL AUTHOR / PROJECT
ORIGINAL URL
REPOSITORY URL
VERSION / RELEASE
REVISION / COMMIT
RETRIEVAL DATE
CONTENT HASH
LICENSE
COPYRIGHT NOTICES
DEPENDENCIES
MODIFICATIONS
DERIVATIVE STATUS
ANARCHY CLASSIFICATION
```

The ANARCHY project should distinguish:

- Foundation
- Related technology
- Prior art
- Compatible technology
- Reference implementation
- Standard/specification
- License reference
- Provenance reference
- Historical evidence
- ANARCHY-original work

No third-party project becomes ANARCHY-original merely because ANARCHY integrates with, studies, forks, wraps, or reimplements an interface to it.

---

## 18. Working thesis

The strongest common thread across the current corpus is not a particular distribution.

It is **composability under administrator control**.

```text
knowledge
   +
source
   +
build
   +
installation
   +
services
   +
networking
   +
device interoperability
   +
provenance
   =
open computing system
```

ANARCHY can therefore be investigated as a **composition architecture**, rather than as a monolithic replacement operating system.

The long-term question is whether these independently controlled layers can be combined into a resilient system whose users and operators retain meaningful control over their software, data, build process, network relationships, and device interoperability.

---

## References

- Launchpad — Bouillon Cube live-install-generator: https://blueprints.launchpad.net/bouilloncube/+spec/live-install-generator
- openSUSE — One Click Install: https://en.opensuse.org/openSUSE:One_Click_Install
- dynebolic developer documentation: https://dyne.org/docs/dynebolic/developers/
- dynebolic project/about: https://dyne.org/dynebolic/about/
- dynebolic historical DyneBolic2 development notes: https://lab.dyne.org/DyneBolic2
- Gentoo Handbook: https://wiki.gentoo.org/wiki/Handbook:ARM64/Installation/About
- Unstructured open-source overview: https://docs.unstructured.io/open-source/introduction/overview
- Unstructured supported file types: https://docs.unstructured.io/open-source/introduction/supported-file-types
- Sphinx documentation: https://www.sphinx-doc.org/en/master/
- Sphinx build: https://www.sphinx-doc.org/en/master/man/sphinx-build.html
- Apache Friends XAMPP: https://www.apachefriends.org/download.html
- WordPress: https://wordpress.org/about/
- Joomla GPL documentation: https://docs.joomla.org/Extensions_and_GPL/en
- MoinMoin: https://moinmo.in/
- libimobiledevice: https://libimobiledevice.org/
- usbmuxd documentation: https://cgit.libimobiledevice.org/usbmuxd.git/tree/docs/usbmuxd.8
- usbmuxd source: https://cgit.libimobiledevice.org/usbmuxd.git/
- Red Hat / Cygnus merger announcement: https://www.redhat.com/en/about/press-releases/press-cygnusacquisition
