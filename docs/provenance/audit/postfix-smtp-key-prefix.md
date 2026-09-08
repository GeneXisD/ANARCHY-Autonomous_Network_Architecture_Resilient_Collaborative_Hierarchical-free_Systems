# Postfix `smtp_key_prefix` — lookup-key context management

## Status

**Partial audit.** The supplied artifact is the Postfix `smtp_key_prefix()` implementation and its helper functions. It is **not the key-generation/keymaker implementation**. The keymaker or additional key-construction code has not yet been supplied.

## Component

- **Project:** Postfix
- **Subsystem:** SMTP lookup-key management
- **Artifact:** `smtp_key` / `smtp_key_prefix`
- **Primary function:** `smtp_key_prefix(VSTRING *buffer, const char *delim_na, SMTP_ITERATOR *iter, int flags)`
- **Author:** Wietse Venema
- **Affiliation stated in source:** IBM T.J. Watson Research
- **License stated in source:** Secure Mailer license must be distributed with the software

## What this code actually does

This implementation constructs a **lookup-key prefix** from selected SMTP context fields. It is designed to make shared cache/lookup-table context explicit and consistent so that unrelated contexts do not accidentally share cache entries.

Supported context flags include:

- `SMTP_KEY_FLAG_SERVICE` — global service name
- `SMTP_KEY_FLAG_SENDER` — envelope sender
- `SMTP_KEY_FLAG_REQ_NEXTHOP` — requested nexthop
- `SMTP_KEY_FLAG_NEXTHOP` — current/fallback nexthop
- `SMTP_KEY_FLAG_HOSTNAME` — current remote hostname
- `SMTP_KEY_FLAG_ADDR` — current remote address
- `SMTP_KEY_FLAG_PORT` — current remote port

The function resets the output buffer, appends selected fields in a defined order, terminates the resulting string, and returns the resulting text pointer.

## Encoding / delimiter handling

`delim_na` supplies a field delimiter and optional placeholder character. Fields containing delimiter characters are Base64-encoded before the delimiter is appended. Empty or unavailable fields receive the placeholder representation.

Relevant helpers:

- `smtp_key_append_na()` — emits the unavailable/inapplicable placeholder
- `smtp_key_append_str()` — serializes string-valued fields and Base64-encodes delimiter-containing values
- `smtp_key_append_uint()` — serializes numeric fields

The source comment also says Base64 encoding is used for content that needs **obfuscation**. This should not be interpreted as cryptographic confidentiality: Base64 is an encoding, not encryption.

## Important cryptographic distinction

This artifact contains **no key generation** and does not create cryptographic keypairs.

The word `key` here means an application/cache/lookup **key**, not a cryptographic key. The use of Base64 is serialization/encoding for safe field separation and possible obfuscation, not a cryptographic protection mechanism.

The actual keymaker/key-generation logic must be audited separately when supplied.

## Cache-isolation significance

The central security/reliability property is **context separation**. Postfix deliberately includes only the context selected by the caller, while documenting which context each flag represents. This is intended to prevent false cache sharing, where credentials or other destination/request-specific results could be reused under the wrong context.

For ANARCHY/RitualMesh provenance work, this is relevant as an example of explicit **cache-key domain separation**. It should not be conflated with cryptographic domain separation, although the architectural principle is related: distinct security or operational contexts should have unambiguous identifiers before state is shared.

## Dependencies visible in the supplied source

- Postfix `sys_defs.h`
- networking headers (`netinet/in.h`, `arpa/inet.h`)
- C string functions
- Postfix `msg.h`
- Postfix `vstring.h`
- Postfix `base64_code.h`
- Postfix `mail_params.h`
- Postfix `smtp.h`

`ntohs()` is used to canonicalize the network port into host byte order before serialization.

## Provenance / licensing observations

The source header identifies Wietse Venema and IBM T.J. Watson Research and states that the Secure Mailer license must accompany the software. Exact Postfix release/version cannot be established from this snippet alone and should not be guessed.

## Follow-up required

When the user supplies the actual **keymaker/key-generation** implementation, audit it separately and correlate it with this prefix layer. In particular, determine:

1. whether the resulting lookup key is hashed or otherwise transformed later;
2. whether any cryptographic primitive is involved after prefix construction;
3. whether credentials, TLS state, SASL state, DNS results, or other security-sensitive data are keyed by this namespace;
4. whether the complete key construction provides sufficient context separation;
5. the exact Postfix release/source lineage if surrounding files identify it.

## Classification

**Historical infrastructure / lookup-key serialization / cache-context separation.**

**Not yet a cryptographic-key-generation artifact.**
