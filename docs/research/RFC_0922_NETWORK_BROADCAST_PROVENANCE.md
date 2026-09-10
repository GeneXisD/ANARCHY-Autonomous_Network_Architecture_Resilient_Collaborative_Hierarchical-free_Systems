# RFC 922 — Network Broadcast and Subnet Architecture Reference

## Purpose

This document records RFC 922 as a historical technical reference for ANARCHY's work on autonomous network discovery, distributed subnet communication, gateway behavior, and resilient collaborative networking.

## Primary source

- **RFC:** RFC 922
- **Title:** *Broadcasting Internet Datagrams in the Presence of Subnets*
- **Author:** Jeffrey Mogul
- **Date:** October 1984
- **Publisher:** RFC Editor / Internet Engineering Task Force
- **Evidence:** https://www.rfc-editor.org/info/rfc922/
- **Document:** https://www.rfc-editor.org/rfc/rfc922

## Technical relevance to ANARCHY

RFC 922 describes how Internet datagram broadcasts can operate when a logical IP network is divided into multiple physical networks or subnets connected by gateways. It addresses propagation of broadcast datagrams across subnet boundaries while limiting unnecessary duplication and forwarding loops.

The document is relevant to ANARCHY as **architectural lineage and technical evidence**, not as a claim that ANARCHY implements RFC 922 or that RFC 922 authors contributed to ANARCHY.

Relevant concepts include:

- logical IP networks spanning multiple physical networks;
- subnet-aware broadcast behavior;
- gateways forwarding broadcast information between subnetworks;
- Reverse Path Forwarding as a mechanism for controlling broadcast propagation;
- network discovery and service-oriented uses of broadcast communication.

## Relationship to ANARCHY discovery architecture

ANARCHY's autonomous/distributed networking research can use the following conceptual distinction:

```text
CLASSIC IP BROADCAST / RFC 922
            ↓
 discover hosts/services across subnet boundaries
            ↓
 gateway-aware propagation
            ↓
 topology and duplicate-control mechanisms

ANARCHY RESEARCH DIRECTION
            ↓
 autonomous peer/service discovery
            ↓
 distributed network participation
            ↓
 resilient collaborative routing/coordination
            ↓
 mesh and heterogeneous-node deployment
```

RFC 922 should therefore be treated as a historical precursor/reference for the **network discovery and gateway coordination layer**, while ANARCHY's mesh, autonomous routing, resilience, governance, and application-layer mechanisms remain distinct research and implementation work.

## Related RFC lineage

RFC 922 belongs to the early Internet work surrounding subnetting and broadcast behavior. Its references and surrounding standards provide a useful historical chain for studying how IP networks evolved from single physical networks toward interconnected subnetworks.

For ANARCHY provenance purposes, related RFCs should be recorded independently rather than treating a family of RFCs as a single source or license.

## Rights and provenance

RFC 922 is an external standards document and is **not ANARCHY-original**. This entry establishes technical provenance only. It does not transfer copyright, patent, trademark, or other rights to ANARCHY and does not establish sponsorship, endorsement, affiliation, or shared authorship.

Any text, diagrams, code, or other material reproduced from the RFC must be handled according to the RFC Editor/IETF rights and permissions applicable to that material. ANARCHY should prefer citation and technical paraphrase over copying source text.

## Classification

**Classification:** Third-party technical reference / standards lineage

**ANARCHY modification:** None to the RFC itself.

**ANARCHY use:** Architectural research, provenance documentation, historical network-design reference.

**Commercialization significance:** The RFC may inform independently authored ANARCHY implementations, but its existence does not by itself determine the licensing or commercial rights of ANARCHY code.
