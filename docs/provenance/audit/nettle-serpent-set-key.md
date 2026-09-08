# Nettle Serpent Key Schedule — Provenance Audit

## Classification

- **Component:** Nettle low-level cryptographic library
- **Source:** `serpent-set-key.c`
- **Primitive:** Serpent block cipher
- **Operation:** User-key padding, expansion, and generation of 33 Serpent subkeys
- **Authors / copyright:** Niels Möller (2011); Simon Josefsson (2010–2011); Free Software Foundation, Inc. (2003–2005)
- **License stated by source:** GNU Lesser General Public License, version 2.1 or later (LGPL-2.1-or-later)
- **Algorithm provenance:** Serpent reference implementation / public-domain Serpent specification material
- **Direct source lineage:** Derived from `cipher/serpent.c` in Libgcrypt v1.4.6. Nettle adaptation credited to Simon Josefsson, 2010-12-07, with final touches 2011-05-30.

## Cryptographic role

This is genuine cryptographic key-schedule code. Unlike a cache/lookup key such as Postfix `smtp_key_prefix()`, the `serpent_set_key()` function consumes a secret user key and derives the internal round subkeys used by the Serpent block cipher.

The implementation:

1. Pads the supplied key according to the Serpent specification.
2. Converts the padded key into eight 32-bit words.
3. Uses the Serpent key-schedule recurrence with the constant `PHI = 0x9E3779B9`.
4. Applies the Serpent S-box transformations.
5. Produces and stores 33 groups of four 32-bit subkeys in `ctx->keys`.

## Key handling

`serpent_key_pad()` accepts a key up to `SERPENT_MAX_KEY_SIZE` and applies the Serpent-specific padding rule. The source explicitly documents the example `aabbcc -> aabbcc0100...00`.

The key schedule uses a circular buffer of eight 32-bit words. `KS_RECURRENCE()` advances the schedule counter and rotates each generated word left by 11 bits. `KS()` performs four recurrence operations followed by an S-box transformation and stores one four-word subkey.

The complete loop generates 33 subkeys, matching Serpent's 32-round design plus the final subkey used by the cipher construction.

## S-box provenance

The eight S-box macro implementations are identified in the source as being copied from the optimized Serpent reference implementation contained in `floppy2`. The source attributes that material to Ross Anderson, Eli Biham, and Lars Knudsen, copyright 1998.

The source also quotes the Serpent project statement that Serpent is completely in the public domain and imposes no restrictions on its use. The optimized submission implementations were described as GPL in the historical submission package, despite some comments retaining older wording.

This creates an important provenance distinction:

```text
Serpent algorithm / reference material
  └── public-domain status stated by source

Serpent reference S-box implementation
  └── Ross Anderson / Eli Biham / Lars Knudsen

Libgcrypt cipher/serpent.c v1.4.6
  └── direct source ancestor of this Nettle adaptation

Nettle serpent-set-key.c
  └── LGPL-2.1-or-later implementation
```

## Dependencies / interfaces visible in source

- `serpent.h`
- `serpent-internal.h`
- Nettle `macros.h`
- `config.h` when configured
- fixed-width integer types (`uint32_t`, `uint8_t`)

No external random-number generator is used by the key schedule itself. The function derives deterministic subkeys from the supplied key.

## Security classification

- **Secret input:** yes — the caller-supplied Serpent key
- **Key generation:** no — this code does not generate entropy or create a random master key
- **Key derivation / expansion:** yes
- **Encryption/decryption primitive:** the file provides initialization/key scheduling; the round encryption/decryption operations are elsewhere
- **Hashing:** no
- **Authentication/MAC:** no
- **Encoding:** no
- **Randomness:** no

The source's `PHI` constant is an algorithmic key-schedule constant, not a secret.

## Historical compatibility significance

The explicit Libgcrypt v1.4.6 lineage makes this artifact particularly useful for the corpus's upstream dependency graph. It demonstrates that the historical software stack incorporates cryptographic code through multiple generations of upstream projects rather than representing a single Nettle-original implementation.

The license header should be preserved as provenance evidence. Any modernization should account separately for the Nettle LGPL terms, the Libgcrypt-derived implementation lineage, and the Serpent reference/S-box provenance.

## Relationship to other audited artifacts

```text
Postfix smtp_key_prefix()
  └── application/cache lookup identity
      └── NOT cryptographic key material

Nettle DSA dsa-keygen.c
  └── asymmetric keypair generation

Nettle Salsa20 salsa20-set-key.c
  └── symmetric stream-cipher state initialization

Nettle Serpent serpent-set-key.c
  └── symmetric block-cipher key expansion
```

## Audit status

**Status:** Historical cryptographic implementation; preserve for provenance and compatibility analysis. Do not infer that the presence of Serpent in the corpus means Serpent is currently deployed or should be selected as a new ANARCHY cryptographic primitive. Deployment/use must be established from call sites, configuration, package manifests, and the surrounding application.

**Exact bundled Nettle release:** not established from this source alone.
