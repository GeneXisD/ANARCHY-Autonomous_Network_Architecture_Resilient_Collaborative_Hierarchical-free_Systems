# RH Cygwin / XAMPP Software Provenance Audit

**Status:** Living audit — update as corpus artifacts are reviewed.

## Scope

This record captures historical software, source-code provenance, licensing, dependencies, cryptographic relevance, compatibility behavior, and architectural observations identified while auditing the RH Cygwin/XAMPP text corpus.

The corpus was collected recursively from the XAMPP tree and contains **232 source `.txt` files**, plus a generated manifest. The RH Cygwin environment is preserved as a historical environment and is **not to be blindly upgraded or replaced during provenance analysis**.

## Evidence-handling rule

A license name alone is insufficient for provenance. Where source files are available, retain the actual source/header evidence and map it to the component, upstream project, copyright statements, dependencies, and derivative relationships.

Historical presence does not imply current security suitability. A cryptographic algorithm, dependency, or compatibility mechanism must be classified according to its actual purpose and context.

---

## 1. EggAccelerators — `eggaccelerators.c`

### Identification

- **Component:** EggAccelerators
- **Subsystem:** GTK/GDK keyboard accelerator parsing and virtual/concrete modifier mapping
- **Language:** C
- **Ecosystem:** GNOME / GTK / GDK / X11
- **Copyright:** Red Hat, Inc. (2002); Tim Janik (1998, 2001)
- **Developers:** Havoc Pennington; Tim Janik
- **License:** GNU Library General Public License, version 2 or later
- **Provisional SPDX classification:** `LGPL-2.0-or-later`

### Function

The implementation parses accelerator expressions such as `<Control>a`, `<Shift><Alt>F1`, and `<Release>z`, then translates between virtual modifier concepts and concrete X11 modifier bits.

It uses GDK/GTK together with X11 facilities including `XKeysymToKeycode()`, `XGetModifierMapping()`, and `XFreeModifiermap()`.

The code accounts for virtual modifiers including Alt, Meta, Hyper, Super, Num Lock, Scroll Lock, and Mode Switch, and contains compatibility handling for GTK key-symbol behavior.

### Security/crypto classification

- Cryptography: none
- Authentication: none
- Credential storage: none
- Security primitive: none
- Keyboard/input translation: yes
- X11 compatibility: yes

The word “key” in this component refers to keyboard keys, not cryptographic keys.

### Provenance significance

The source is historical compatibility infrastructure demonstrating a boundary between platform-specific X11 representation and an application-level accelerator representation. It is useful architectural prior art for compatibility-layer design, but it is not a candidate security component for direct reuse in ANARCHY/RitualMesh.

---

## 2. BIND — `bind.keys`

### Identification

- **Component:** BIND 9
- **Artifact:** `bind.keys`
- **Subsystem:** DNSSEC trust-anchor configuration
- **Origin:** ISC/BIND
- **Artifact date:** January 2011 revision evidence
- **Status:** Historical

### Function

The file defines public DNSSEC trust anchors, including the root zone (`.`) and the historical ISC DLV (`dlv.isc.org`) entry.

The root trust anchor uses DNSSEC algorithm 8 (RSA/SHA-256). The historical DLV entry uses algorithm 5 (RSA/SHA-1).

These are **public trust anchors**, not private keys.

### Configuration significance

The trust-anchor file is configuration-dependent. Its presence does not by itself establish that DNSSEC validation or DNSSEC lookaside validation was active; the BIND configuration determines whether the relevant mechanisms were enabled.

The embedded comments identify the file as a historical snapshot and indicate that trust-anchor information should be kept current.

### Security/crypto classification

- Cryptographic material: public trust anchors
- Private key material: none
- Function: DNSSEC trust establishment
- Historical SHA-1 use: trust-anchor/signature algorithm context, not password hashing

This artifact must not be treated as current DNSSEC trust state without checking the corresponding BIND configuration and release lineage.

---

## 3. Squid — `store_key_md5`

### Identification

- **Component:** Squid Web Proxy Cache
- **Subsystem:** Storage Manager / cache-key implementation
- **Artifact:** `store_key_md5` implementation
- **Author identified in source:** Duane Wessels
- **Copyright identified in source:** Regents of the University of California, 2001
- **License identified in source:** GPL v2
- **Upstream:** Squid Web Proxy Cache

### Function

The code implements deterministic cache-key handling through the Squid storage manager, including operations such as `storeKeyText`, `storeKeyScan`, `storeKeyHashCmp`, `storeKeyHashHash`, `storeKeyPrivate`, and `storeKeyPublic`.

### Security/crypto classification

MD5 is present, but in this artifact it is used for **cache-key/digest purposes**, not as a password hash, digital signature, certificate algorithm, or authentication primitive.

Therefore the correct audit classification is:

`MD5 → deterministic cache/storage keying → non-security use`

This should not be reported as equivalent to using MD5 for password authentication or cryptographic signatures.

### Provenance follow-up

For exact version and complete licensing lineage, correlate this source with Squid `COPYRIGHT`, `CREDITS`, contributor information, and the enclosing release/version metadata.

---

## 4. GNOME/MATE desktop infrastructure — `gsp-keyfile.c`

### Identification

- **Artifact:** `gsp-keyfile.c`
- **Function:** GKeyFile extensions / desktop-session keyfile handling
- **Copyright:** Novell, Inc., 2008–2009
- **Author identified:** Vincent Untz
- **License:** GPL v2
- **Lineage:** explicitly based on `panel-keyfile.c` from `mate-panel`
- **Primary dependency:** GLib

### Function

The source extends GLib key-file handling for desktop-session configuration. It contains a documented compatibility workaround referencing GLib bug `#309224`.

### Security/crypto classification

- Cryptography: none
- Authentication: none
- Credential storage: none
- Configuration/keyfile handling: yes

### Provenance significance

The explicit statement that the source is based on `panel-keyfile.c` is a direct derivative-lineage clue. Preserve this relationship in the provenance graph rather than reducing the record to “GPLv2”.

---

## 5. Apache Subversion — `libsvn_auth_gnome_keyring/gnome_keyring.c`

### Identification

- **Component:** Apache Subversion
- **Library:** `libsvn_auth_gnome_keyring`
- **Artifact:** `gnome_keyring.c`
- **License:** Apache License 2.0
- **Upstream:** Apache Software Foundation / Subversion
- **Dependencies:** APR, GLib, GNOME Keyring, Subversion authentication/configuration APIs

### Function

This is a credential-provider integration between Subversion and GNOME Keyring.

It implements two major credential paths:

1. **SVN simple credentials** — retrieval and storage of network passwords.
2. **SSL client certificate passphrases** — retrieval and storage of passphrases associated with TLS client-certificate authentication.

The source uses GNOME Keyring operations such as `gnome_keyring_find_network_password_sync()` and `gnome_keyring_set_network_password_sync()` rather than implementing its own cryptographic storage primitive.

### Credential architecture

```text
Subversion
    |
    v
Authentication provider
    |
    +-- SVN network password
    |
    +-- TLS client-certificate passphrase
    |
    v
GNOME Keyring
    |
    v
Protected secret storage
```

### Interactive/non-interactive behavior

Interactive execution can invoke an unlock callback and request the keyring password. Non-interactive execution reports credentials as unavailable when the keyring remains locked.

The source explicitly documents a race between checking that a keyring is unlocked and subsequently using it. This is an implementation limitation to preserve in the historical record.

### Security/crypto classification

- Credential handling: **high relevance**
- Secret storage integration: **high relevance**
- TLS client authentication: **high relevance**
- Direct cryptographic primitive implementation: none
- Key management: delegated to GNOME Keyring

The actual certificate/private-key cryptography is not implemented by this file.

### Architectural relevance to ANARCHY/RitualMesh

This provides useful prior art for a pluggable credential-provider architecture with:

- external secret-store delegation;
- interactive versus non-interactive policy;
- provider failure-state propagation;
- separate credential classes;
- TLS client-authentication support.

It should be treated as architectural prior art, not copied into a modern security boundary without a current dependency/security review.

---

## 6. Apache Subversion — `libsvn_auth_gnome_keyring/version.c`

### Identification

- **Component:** `libsvn_auth_gnome_keyring`
- **Artifact:** `version.c`
- **License:** Apache License 2.0
- **Version API:** `svn_auth_gnome_keyring_version()`
- **Version mechanism:** `SVN_VERSION_BODY`

The source exposes the component's version structure through Subversion's shared version infrastructure. It does not contain the actual version number itself.

### Provenance significance

The standardized Apache header references:

- the Apache Software Foundation;
- contributor license agreements;
- the distributed `NOTICE` file;
- Apache License 2.0.

This is important evidence that the audit must track **NOTICE and contributor-license provenance in addition to the SPDX license identifier**.

---

# Cross-component provenance map

```text
Historical RH Cygwin / XAMPP corpus
          |
          +-------------------+-------------------+------------------+
          |                   |                   |                  |
          v                   v                   v                  v
      GNOME/GTK             BIND                 Squid           Apache SVN
          |                   |                   |                  |
    eggaccelerators.c     bind.keys         store_key_md5      gnome_keyring.c
          |                   |                   |                  |
       X11/GDK            DNSSEC             cache keys       GNOME Keyring
          |                   |                   |                  |
       LGPL-2+          public anchors          GPL-2            Apache-2.0
                                                                      |
                                                                      v
                                                                 version.c
```

These are **separate upstream lineages**. Their coexistence in the historical environment does not establish common ownership or a single development program.

# License/provenance inventory rule

For each newly discovered source artifact, record:

1. component/project;
2. exact artifact path/name;
3. upstream origin;
4. version/date clues;
5. copyright holders;
6. authors/contributors named in the source;
7. declared license;
8. NOTICE or additional attribution obligations;
9. derivative/based-on statements;
10. dependencies;
11. cryptographic algorithms and their actual purpose;
12. authentication/credential relevance;
13. configuration versus executable/source role;
14. historical compatibility workarounds;
15. current/historical status;
16. evidence confidence;
17. ANARCHY/RitualMesh architectural relevance.

## Preservation principle

The historical RH Cygwin environment and its source corpus are evidence artifacts. Modernization decisions should be made **after** provenance capture, not before. A modern replacement may be appropriate for deployment while the historical implementation remains preserved for reproducibility and lineage analysis.
