# Nettle `dsa-keygen.c` provenance audit

## Artifact

- **Component:** Nettle low-level cryptographic library
- **Source file:** `dsa-keygen.c`
- **Function:** `dsa_generate_keypair`
- **Purpose:** generation of DSA public/private keypairs
- **Copyright:** Niels Möller, 2002
- **License stated in source:** GNU Lesser General Public License (LGPL), version 2.1 or later
- **Primary dependency:** GNU MP (`mpz_t` and modular arithmetic)

## Cryptographic role

This is genuine cryptographic key-generation code, unlike the MPI `win_keyval` artifact where the word “key” refers to an attribute identifier. It constructs DSA parameters and generates a private/public keypair.

The implementation accepts `q_bits` of 160 or 256 and checks the corresponding minimum `p` size. The source comment identifies the FIPS 186-3 parameter sets as `(1024,160)`, `(2048,224)`, `(2048,256)`, and `(3072,256)`, while noting that this implementation uses only `q` sizes of 160 or 256 bits.

The implementation:

1. Generates a prime `q` using Nettle's random-prime facilities.
2. Generates an auxiliary prime `p0`.
3. Constructs a DSA `p` using a Pocklington-prime generation routine.
4. Searches for a generator `g` by modular exponentiation.
5. Generates private exponent `x` from randomness in the range `1 .. q-1`.
6. Computes public value `y = g^x mod p`.

## Security/provenance observations

- The security of the generated keypair depends on the supplied `nettle_random_func` random source and the integrity of the underlying big-number and prime-generation routines.
- The code itself does not implement a standalone entropy source; randomness is injected through the Nettle callback interface.
- DSA is a historical public-key signature algorithm. This artifact should therefore be preserved as **historical cryptographic provenance**, not automatically selected as a new ANARCHY signing primitive.
- The source explicitly references FIPS 186-3-era parameterization. The exact Nettle release containing this file is not established from the supplied snippet alone and must not be guessed.
- No private key material is embedded in the source.

## Dependency/provenance graph

```text
Nettle
  └── dsa-keygen.c
       ├── dsa.h
       ├── bignum.h
       ├── nettle-internal.h
       └── GNU MP (mpz_t / modular arithmetic)
```

## ANARCHY relevance

This artifact belongs in the cryptographic provenance layer of ANARCHY because it demonstrates an upstream implementation of asymmetric key generation and the historical evolution of DSA support. It is particularly useful when separating:

- historical cryptographic algorithms from current cryptographic policy;
- key-generation code from credential-storage code;
- entropy/randomness interfaces from the cryptographic primitive itself;
- source provenance from the eventual application-level signing protocol.

For modernization work, retain this artifact for lineage and compatibility analysis. Do not treat the presence of DSA support as a recommendation to deploy DSA in new protocol designs.

## Audit status

**Classification:** Historical cryptographic implementation / asymmetric key generation  
**Crypto:** DSA  
**License:** LGPL-2.1-or-later as stated by the source header  
**Status:** Preserve for provenance; modernization candidate if exposed as a new signing primitive  
**Version certainty:** Exact upstream release not established from supplied source alone
