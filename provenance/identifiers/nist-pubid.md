# NIST Machine-Readable PubID

## Grammar

<publisher>.<series>.<report-num>[<part>][<edition>][-<update>][.<stage>][.<translation>]

## Example

`NIST.HB.150-1e2021-upd3.ipd.spa`

Conceptual components:

- publisher
- series
- report number
- part
- edition
- update
- stage
- translation

## ANARCHY relevance

NIST PubID demonstrates a structured machine-readable identifier capable of
encoding publication identity and version metadata.

ANARCHY research should compare this model with:

- DOI
- SPDX
- PURL
- Git object IDs
- Git commit IDs
- IPFS CIDs
- UUID
- URI/URN

The goal is to determine which identifier mechanisms are useful for
software, network artifacts and provenance.
