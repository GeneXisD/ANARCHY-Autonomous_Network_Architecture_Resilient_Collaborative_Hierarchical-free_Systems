# GNOME Keyring / Subversion Authentication Provenance

## Artifact reviewed

- Component: Apache Subversion GNOME Keyring authentication provider
- Files reviewed: `gnome_keyring.c`, `version.c`
- Functional area: SVN authentication credential storage and SSL client-certificate passphrase storage
- Upstream ecosystem: Apache Subversion + GNOME Keyring
- License: Apache License 2.0 for the Subversion source files

## `gnome_keyring.c`

The source implements Subversion authentication providers backed by GNOME Keyring. It stores and retrieves:

1. SVN simple-authentication passwords.
2. SSL client-certificate passphrases.

The implementation uses synchronous GNOME Keyring APIs, including default-keyring discovery, lock-state checking, unlock operations, network-password lookup, and network-password storage. Subversion's APR pools are used for copied credential data.

### Security boundary

GNOME Keyring is the credential-protection layer in this artifact. The source does not itself define a cryptographic algorithm for protecting the stored passwords; it delegates credential storage to the GNOME Keyring service.

The code explicitly distinguishes interactive and non-interactive operation. A locked keyring can invoke an unlock prompt when interactive, while non-interactive operation returns `SVN_ERR_AUTHN_CREDS_UNAVAILABLE` rather than prompting.

The implementation also contains a documented race around checking whether the keyring is unlocked and subsequently using it. This is a historical implementation detail worth retaining in the audit because it can affect reliability/security analysis.

### Dependencies visible in source

- Apache Portable Runtime (`apr_pools`, `apr_strings`)
- GLib
- GNOME Keyring
- Apache Subversion authentication/config/error/hash/pool APIs
- Subversion private authentication APIs

### Credential flows

`password_get_gnome_keyring()` retrieves a network password using the SVN username and realm string. `password_set_gnome_keyring()` writes the password into the default GNOME Keyring.

The same credential callbacks are reused for SSL client-certificate passphrase caching. This makes the artifact relevant to the repository's credential-management/provenance model even though it is not itself a general-purpose cryptographic library.

### Historical compatibility behavior

The source tracks whether opening/accessing GNOME Keyring failed using the `gnome-keyring-opening-failed` parameter. Once access fails, the provider avoids repeatedly attempting the same operation and allows the authentication framework to try another provider.

`init_gnome_keyring()` also sets the application name to `Subversion` when none is configured and installs a GLib default log handler. The source comments that this suppresses stderr logging from libgnome-keyring and potentially other linked GLib users without a log domain. This is important historical behavior and should not be silently modernized without testing.

## `version.c`

`version.c` identifies the artifact as the `libsvn_auth_gnome_keyring` version component and returns the Subversion version structure through `SVN_VERSION_BODY`.

It carries the same Apache License 2.0 header as `gnome_keyring.c`.

## License/provenance classification

| Field | Finding |
|---|---|
| License | Apache License 2.0 |
| Copyright/licensor | Apache Software Foundation (ASF), subject to NOTICE and contributor agreements |
| Component | Apache Subversion GNOME Keyring authentication provider |
| External dependency | GNOME Keyring / GLib |
| Credential material | SVN passwords; SSL client-cert passphrases |
| Cryptographic primitive in this source | None directly specified |
| Protection mechanism | Delegated to GNOME Keyring |
| Authentication protocol context | SVN authentication; SSL client certificate passphrase handling |
| Configuration-sensitive | Yes |
| Historical status | Preserve as historical source until version/dependency lineage is established |

## ANARCHY / RitualMesh relevance

This artifact is significant as a **credential-provider pattern**, not as a cryptographic primitive. It demonstrates a layered architecture in which an application authentication subsystem delegates secret storage to a platform keyring while retaining a provider abstraction and fallback behavior.

For the ANARCHY/RitualMesh audit, classify this under:

- `credential-storage`
- `authentication-provider`
- `platform-keyring`
- `secret-management`
- `Apache-2.0`
- `Subversion`
- `GNOME-Keyring`
- `historical-compatibility`

It should not be treated as interchangeable with Git Credential Manager, GPG signing, SSH authentication, or JOSE/JWS/JWE. Those serve different security boundaries.

## Preservation decision

**Preserve / inventory; do not rewrite yet.** First establish the exact Subversion release and GNOME Keyring/GLib versions from surrounding corpus files and package metadata. Any modernization should be performed as a separate compatibility layer or controlled patch rather than altering the historical source in place.
