# Oracle StorageTek SL150 Licensing Evidence Record

**Evidence status:** Comparative / primary-document evidence

**License-matrix status:** NOT PROMOTED TO A LICENSE DETERMINATION

## Preserved artifact

The repository contains the supplied archival document at:

`/Licensing Information.pdf`

Repository object metadata observed during intake:

- Git path: `Licensing Information.pdf`
- Git blob SHA-1: `24550bee55d4364c2813fe3a27edbb1fec4eb4dc`
- Stored size: `1,250,130` bytes
- Document subject: Oracle StorageTek SL150 Modular Tape Library Licensing Information

**Important:** the Git blob SHA above is an object identifier, not a SHA-256 digest of the PDF. A cryptographic file digest should be generated from the downloaded PDF bytes during a controlled archival/hash pass.

## Primary-source identification

The document is an Oracle StorageTek SL150 Licensing Information manual. It contains Oracle Technology Notices and Licenses and reproduces third-party license/notice material for software identified as included or distributed with the product.

The associated Oracle Linux/Oracle VM component-list resource supplied for this research is:

- Oracle Linux and Oracle VM License Information / Component List: https://oss.oracle.com/linux/legal/oracle-list.html#License_information_on_distribution

The StorageTek SL150 licensing document is a product-specific disclosure. The Oracle Linux component-list resource is a separate distribution-level licensing resource. They must not be conflated.

## What this document directly establishes

Based on the preserved document text:

1. Oracle identifies third-party software as potentially included/distributed with the StorageTek SL150 product.
2. The document reproduces or identifies individual third-party notices and license texts.
3. The listed components do not share one universal third-party license. The document contains multiple licensing regimes, including Apache, BSD-style, W3C, Mesa/XFree86/SGI-related, and other terms.
4. The document therefore provides a concrete historical example of **component-level licensing inside a larger product/distribution disclosure**.
5. The presence of a component in an Oracle product does **not**, by itself, establish Oracle ownership of that component.

## What this document does NOT establish

This artifact does not, by itself, establish:

- that DC219 was authored by Oracle, IBM, Huawei, or any other organization;
- that DC219 has the same legal terms as Oracle's notices;
- that XAMPP or the Delphi XAMPP Control Panel is licensed under any Oracle license;
- that any particular third-party component originated with Oracle;
- that any listed third-party license applies to ANARCHY or RitualMesh;
- that an umbrella product/distribution license automatically applies to every contained component;
- that a license identifier such as an SPDX expression can be assigned without checking the exact license text and applicable version.

## Licensing architecture demonstrated

```text
Oracle product / distribution disclosure
                 |
                 +-- Oracle material
                 |
                 +-- Third-party component A
                 |       +-- copyright / attribution
                 |       +-- license A
                 |       +-- conditions A
                 |
                 +-- Third-party component B
                 |       +-- copyright / attribution
                 |       +-- license B
                 |       +-- conditions B
                 |
                 +-- Third-party component C
                         +-- copyright / attribution
                         +-- license C
                         +-- conditions C
```

This is useful **comparative evidence** for ANARCHY's provenance model because it demonstrates why product-level and component-level licensing facts must remain separate records.

## Specific caution: warranty language

Warranty/disclaimer vocabulary must not be used as a license-identification shortcut. Phrases concerning warranties, merchantability, fitness for a particular purpose, or "AS IS" treatment occur in multiple independent licensing regimes.

The operative license determination must instead be tied to the complete applicable license/notice text and the identified component/provenance relationship.

## Specific caution: mixed-license documents

The reproduced third-party material includes materially different terms. In particular, the Mesa/SGI-related material must not be normalized to MIT/BSD merely because portions of Mesa use permissive licensing language. Its historical license text contains additional provisions that require independent analysis.

Likewise, W3C software notices and W3C document notices should remain distinct records rather than being collapsed into a generic "W3C license" label.

## Provenance graph interpretation

```text
StorageTek SL150
       |
       | Oracle disclosure says included/distributed
       v
Third-party component
       |
       +--> named copyright holder(s)
       +--> upstream/project identity
       +--> exact license/notice text
       +--> component-specific conditions
       +--> redistribution/attribution requirements
```

The arrow from product to component is a **distribution/disclosure relationship**, not an ownership relationship.

## Relationship to ANARCHY evidence policy

This artifact belongs in the evidence/research layer. It should remain separate from the ANARCHY license matrix until an independent provenance question requires a specific component/license determination.

The repository's evidence discipline is:

```text
Observed in product notice
        !=
Owned by distributor
        !=
Licensed by distributor
        !=
Applicable to ANARCHY
        !=
Applicable to DC219
```

## Follow-up research targets

1. Preserve the complete PDF without modification.
2. Generate and record SHA-256/SHA-512 from the actual PDF bytes.
3. Record PDF metadata and page count from the archival artifact.
4. Verify the official Oracle source URL and document revision/date.
5. For each third-party component of interest, obtain the upstream license from the relevant primary project/source repository.
6. Compare exact historical license text rather than relying on license names.
7. Only promote a component to the ANARCHY license matrix when the component identity, provenance, applicable license, and evidence source are sufficiently established.

## Evidence classification

**Classification:** `COMPARATIVE-PRIMARY-SOURCE`

**Confidence:** High for the narrow proposition that the supplied Oracle licensing document is a historical product-level disclosure containing component-specific third-party notices/licenses; insufficient for any unrelated ownership, authorship, DC219, XAMPP, Huawei, IBM, or ANARCHY provenance claim.

**Disposition:** Preserve; do not use as a standalone license grant or provenance determination.
