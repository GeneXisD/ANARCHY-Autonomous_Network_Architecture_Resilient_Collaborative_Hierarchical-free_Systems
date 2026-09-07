# Apache HTTP Server Subcomponent License Topology

## Purpose

This document records the licensing/provenance pattern visible in the Apache HTTP Server license and third-party notices supplied for ANARCHY research. It is intended as an engineering/provenance reference, not as legal advice.

## Key finding

An Apache-2.0 top-level project can contain separately licensed third-party components. The correct ANARCHY model is therefore **component-level provenance**, not a single-license assumption.

Apache-2.0 itself permits reproduction, modification, derivative works, sublicensing and distribution subject to its conditions. In particular, redistribution requires providing the license, marking modified files, preserving applicable notices, and carrying forward NOTICE attributions where a NOTICE file applies. Apache-2.0 does **not** grant the licensor's trademarks. See the Apache Software Foundation's current licensing guidance and license text. 

## Components identified in the supplied Apache HTTP Server notice material

| Component / area | Identified licensing basis | Key obligation / issue |
|---|---|---|
| Apache HTTP Server core | Apache License 2.0 | Preserve required notices; mark modified files; include applicable NOTICE material; trademark rights are separate. |
| `mod_mime_magic` | Cisco contribution + Ian F. Darwin `file`-derived terms | Preserve origin/credit; altered versions must be marked; retain notice. |
| `mod_imagemap` polygon code | Eric Haines copyright | Preserve applicable copyright/attribution terms. |
| `server/util_md5.c` | NCSA/University of Illinois + Carnegie Mellon + Bellcore-derived notices | Preserve copyright/permission notices and attribution restrictions. |
| `util_pcre.c`, `ap_regex.h` | University of Cambridge BSD-style terms | Source and binary notice requirements; no endorsement without permission. |
| APR MD5 material | RSA Data Security notice | Preserve identification and derivation notices. |
| APR MD5 crypt material | FreeBSD Beer-Ware license | Retain the license notice. |
| APR-util MD4 material | RSA Data Security notice | Preserve identification/derivation and notice requirements. |
| ZeusBench test code | Zeus Technology permissive terms | Copyright notice must remain. |
| PCRE | BSD-style PCRE license | Preserve notices/disclaimer; endorsement restrictions apply. |
| OpenSSL / SSLeay-era material | OpenSSL + original SSLeay terms in the supplied historical material | Preserve required notices/acknowledgements; branding/name restrictions and historical license text must be treated carefully for the exact version. |
| zlib | zlib license | Preserve notice; altered source must be marked; origin must not be misrepresented. |
| Lua | MIT | Preserve copyright and permission notice. |
| libxml2 | MIT | Preserve copyright and permission notice. |
| nghttp2 | MIT | Preserve copyright and permission notice. |
| Brotli | MIT | Preserve copyright and permission notice. |
| curl | MIT-style | Preserve copyright/permission notice; no endorsement implication. |
| Jansson | MIT | Preserve copyright and permission notice. |

## Why this matters to ANARCHY

This is directly relevant to the ANARCHY distribution/provisioning model:

```text
upstream project
      |
      +-- top-level license
      |
      +-- embedded component A --> license + notice
      |
      +-- embedded component B --> license + notice
      |
      +-- embedded component C --> license + notice
      |
      +-- trademarks --> separate analysis
      |
      v
ANARCHY artifact
      |
      +-- LICENSE bundle
      +-- NOTICE bundle
      +-- component manifest / SBOM
      +-- modification records
      +-- provenance hashes
      +-- branding/trademark audit
```

The important conclusion is that **Apache-2.0 compatibility does not erase the obligations of separately licensed embedded code**. ANARCHY should preserve each component's original notice and license requirements in the generated distribution.

## Apache-2.0 modification rule

For an Apache-2.0 component, ANARCHY can make and distribute modifications, but modified files need prominent notices indicating that changes were made. A derivative distribution may also add its own copyright statement and additional terms for the modifications/derivative work as a whole, provided the underlying Apache-2.0 conditions remain satisfied.

This is particularly important for debranding/rebranding work: **copyright/license permissions and trademark permissions are separate questions**. Apache-2.0 section 6 does not grant permission to use the licensor's trademarks except for the limited descriptive/NOTICE circumstances stated in the license.

## ANARCHY implementation requirement

Every packaged component should eventually have a record resembling:

```yaml
component:
  name: example
  upstream: example-project
  version: verified-version
  license: SPDX-ID-or-verified-text
  copyright: path/to/copyright-record
  license_files:
    - LICENSE
  notice_files:
    - NOTICE
  source_revision: verified-commit-or-release
  modifications:
    status: none|modified
    record: path/to/patch-or-changelog
  trademarks:
    status: separate-audit-required
  redistribution:
    status: verified|review-required
```

## Evidence status

- **Source text:** supplied in ANARCHY research conversation; exact originating Apache HTTP Server release should be recorded when known.
- **License interpretation:** cross-checked against current Apache Software Foundation guidance.
- **Exact version mapping:** not yet established from the supplied text alone.
- **Historical OpenSSL/SSLeay terms:** must be evaluated against the exact OpenSSL release before using them as the license record for a current component.

## Official references

- Apache Software Foundation licensing overview: https://www.apache.org/free/
- Apache Software Foundation policies: https://www.apache.org/foundation/policies/
- Apache License 2.0 reference: https://www.apache.org/licenses/LICENSE-2.0

These references should be used as authoritative navigation points; the exact upstream release's own LICENSE/NOTICE files remain the primary provenance evidence for a particular ANARCHY dependency.
