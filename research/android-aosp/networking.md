# AOSP networking → ANARCHY

AOSP provides a useful case study in how a platform coordinates Wi-Fi, cellular, Ethernet, VPN, routing, DNS, sockets, connectivity state, and application-facing network policy.

## Research targets

- network interfaces and link state
- routing and network selection
- DNS resolution
- VPN and tunneling boundaries
- connectivity services
- per-application network policy
- network capability descriptions
- captive portal and validation mechanisms
- offline behavior

## ANARCHY translation

The strongest reusable idea is **capability-oriented network selection** rather than hard-coding one interface as the network.

A node can advertise capabilities such as:

```text
transport: ipv6 / ipv4 / overlay
latency: estimate
bandwidth: estimate
reachability: local / peer / global
trust: policy-derived
cost: policy-derived
availability: current estimate
```

A distributed routing layer can then select paths according to policy while retaining local autonomy.

## Research connection

Cross-reference this with ANARCHY work on mesh networking, Netsukuku, DNS, autonomous networks, I2P-style overlays, and distributed systems. AOSP is the endpoint/platform perspective; those projects provide the network/federation perspective.
