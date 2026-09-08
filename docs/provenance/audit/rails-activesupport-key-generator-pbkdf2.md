# Rails ActiveSupport `KeyGenerator` — PBKDF2 Audit

## Classification

- **Component:** Ruby on Rails ActiveSupport
- **Artifact:** `lib/active_support/key_generator.rb` (represented in the supplied RDoc output)
- **Class:** `ActiveSupport::KeyGenerator`
- **Role:** Cryptographic key derivation interface
- **Underlying primitive:** PBKDF2 via OpenSSL
- **License/provenance:** Not present in the supplied RDoc fragment; must be established from the corresponding Rails source/package metadata before making a licensing conclusion
- **Exact Rails version:** Not established from the supplied fragment

## What this artifact is

This is a genuine cryptographic key-derivation abstraction, not a cache-key formatter or a cipher key-schedule.

The supplied documentation describes `KeyGenerator` as a wrapper around OpenSSL's PBKDF2 implementation. Its purpose is to derive multiple keys from a single application secret while keeping those derived keys separated by application purpose/context.

Conceptually:

```text
                    application secret
                           │
                           ▼
              ActiveSupport::KeyGenerator
                           │
                           ▼
                    PBKDF2 / OpenSSL
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          purpose A     purpose B     purpose C
          derived key   derived key   derived key
```

## Security significance

The most important architectural statement in the supplied documentation is that one secure secret can be used as the root secret while avoiding reuse of the same raw secret in incompatible contexts.

That is a **key-separation / domain-separation design objective**. The resulting derived keys can be used for different purposes without treating the application's master secret itself as the direct key for every operation.

The artifact therefore belongs in ANARCHY's cryptographic architecture inventory under **KDF / key derivation**, rather than under symmetric encryption, asymmetric signing, or credential storage.

## PBKDF2 relationship

PBKDF2 is a password-based key derivation construction. In this artifact, the actual cryptographic implementation is delegated to OpenSSL rather than implemented inside `KeyGenerator` itself.

Therefore the dependency chain visible from the supplied material is:

```text
Rails ActiveSupport
  └── ActiveSupport::KeyGenerator
       └── OpenSSL PBKDF2
```

The supplied fragment does **not** provide enough information to determine the exact digest/hash, iteration count, output-length policy, salt construction, or Rails release. Those values should be recovered from the actual source file and versioned Rails package before recording implementation-specific parameters.

## Important distinction from previously audited "key" artifacts

```text
Postfix smtp_key_prefix()
  └── cache / lookup identity

Open MPI win_keyval
  └── MPI attribute identifier

Nettle DSA dsa-keygen.c
  └── asymmetric keypair generation

Nettle Salsa20 set_key
  └── symmetric stream-cipher state initialization

Nettle Serpent set_key
  └── symmetric block-cipher key expansion

Rails ActiveSupport::KeyGenerator
  └── cryptographic key derivation (PBKDF2)
```

This distinction is important for automated corpus classification: the word `key` alone is insufficient to identify cryptographic material or cryptographic operations.

## Provenance evidence in supplied artifact

The RDoc serialization explicitly identifies:

- `ActiveSupport::KeyGenerator`
- source path `lib/active_support/key_generator.rb`
- method `generate_key`
- dependency on OpenSSL's PBKDF2 implementation
- purpose-oriented derivation of multiple keys from a common secret

The binary-looking prefix in the supplied text is RDoc serialized/encoded structure rather than evidence of encrypted key material. No secret, salt, derived key, password, or private key is present in the supplied fragment.

## Audit status

**Status:** Confirmed cryptographic KDF abstraction; historical source fragment requires version/source-package correlation before exact parameter and license conclusions are made.

**Do not infer from this fragment alone:**

- the exact PBKDF2 digest
- iteration count
- salt format
- derived-key length
- Rails release
- whether this specific installation actively uses the class

Those should be established from surrounding source, call sites, gem/package metadata, and the original Rails documentation/source bundle.
