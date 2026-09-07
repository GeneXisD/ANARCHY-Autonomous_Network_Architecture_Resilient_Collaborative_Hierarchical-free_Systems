# AOSP HAL, Treble, and modular updates

## Hardware abstraction

AOSP's HAL model is useful because it separates framework expectations from hardware-specific implementations. For ANARCHY, a similar boundary can expose node capabilities without exposing the implementation behind them.

Examples of capability classes to investigate:

- storage
- networking
- sensors
- compute accelerators
- display/audio
- cryptographic hardware
- location/time

## Treble

Project Treble is important as prior art for **stable interface boundaries between independently evolving layers**. ANARCHY should investigate the same property at a distributed boundary: a peer should be able to upgrade or replace an implementation without requiring every other peer to rebuild simultaneously.

## Project Mainline

Mainline is relevant to the idea of updating selected system components independently of the full platform image. For ANARCHY, this suggests independently versioned, signed, content-addressed service components with explicit compatibility metadata.

## ANARCHY questions

- What is the smallest stable capability contract?
- Can implementations be selected dynamically from multiple peers?
- Can a failed implementation be rolled back locally?
- Can a component be replicated without sharing mutable global state?
- Can compatibility be proven from manifests rather than assumed?

## Key principle

**Separate interfaces from implementations, and separate component lifecycle from node lifecycle.**
