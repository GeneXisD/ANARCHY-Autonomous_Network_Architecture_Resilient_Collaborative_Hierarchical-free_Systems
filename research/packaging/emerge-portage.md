# Gentoo emerge / Portage → ANARCHY

## Why this matters

The `emerge` command is the high-level command-line interface to Gentoo's Portage system. Portage resolves dependencies and can work with source and binary packages; its repository model is based on package metadata/ebuilds rather than a monolithic distribution image.

Primary references:

- https://dev.gentoo.org/~zmedico/portage/doc/man/emerge.1.html
- https://devmanual.gentoo.org/general-concepts/emerge-and-ebuild/index.html
- https://github.com/gentoo/portage

## Concepts worth importing into ANARCHY research

### 1. Dependency graphs

Treat software as a graph of explicit dependencies instead of a fixed image. This is directly relevant to independently replaceable ANARCHY services.

### 2. Declarative package metadata

An ebuild describes how a package is obtained, built, installed, and related to dependencies. ANARCHY can study this as a model for declarative component recipes.

### 3. Source and binary distribution

Portage can build from source and use binary packages. ANARCHY can use the same conceptual split:

```text
source recipe → reproducible build → signed artifact
                              ↘
                         binary distribution
```

### 4. Profiles / configuration

Gentoo's configuration and USE-flag model demonstrates how the same package graph can produce different system capabilities. ANARCHY should investigate capability profiles that do not require one universal node image.

### 5. World / explicit intent

Portage distinguishes explicitly selected software from dependencies. ANARCHY can use a similar distinction between:

- operator intent;
- node-required services;
- transitive dependencies;
- opportunistic peer services.

### 6. Repository federation

Additional repositories and binary hosts are especially relevant to ANARCHY's decentralized distribution model.

## ANARCHY design questions

- Can package metadata be content-addressed?
- Can multiple independent repositories advertise compatible components?
- Can dependency resolution tolerate unavailable repositories?
- Can a node choose among multiple providers for the same capability?
- Can a signed package be verified without contacting the original repository?
- Can updates be staged, replicated, and rolled back locally?
- Can dependency conflicts be represented as explicit graph conflicts rather than hidden failures?

## Relationship to the current ANARCHY work

This belongs beside AOSP, GNU, Cygwin, Puredyne/dyne:bolic, openSUSE, and other distribution/build ecosystems. Together they provide prior art for **componentized operating environments, source federation, build metadata, and decentralized distribution**.
