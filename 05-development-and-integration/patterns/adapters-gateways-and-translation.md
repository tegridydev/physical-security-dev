---
title: "Adapters, gateways, and protocol translation"
summary: "Keep transport, vendor variation, security boundaries, and domain semantics separate."
page_type: development
domains:
  - development
tags:
  - adapter
  - gateway
  - protocol-translation
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-82 Rev. 3"
coverage_limit: "Protocol-neutral gateway architecture; exact translation semantics, security properties, capabilities, and failure behavior come from selected standards and product profiles."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Adapters, gateways, and protocol translation

[Home](../../README.md) / [Development](../README.md) / [Patterns](README.md) / Adapters and gateways

An adapter translates one implementation into a stable internal interface. A gateway additionally terminates trust, identity, sessions, policy, and failure behavior between zones. Transparent forwarding is not automatically simpler or safer.

## Layered design

| Layer | Owns | Must not own |
|---|---|---|
| Transport | Connection, TLS, serial/network framing, deadlines | Door/alarm/media business meaning |
| Protocol codec | Message framing, parsing, serialization, version rules | Vendor-independent authorization policy |
| Session/state | Negotiation, sequence, subscriptions, retry and reconnect | UI-specific representations |
| Vendor adapter | Product capability and version quirks | Canonical cross-system state |
| Domain service | Cameras, doors, alarms, credentials, events and commands | Raw wire values without provenance |
| Policy/audit | Identity, authorization, side-effect gating, evidence | Silent fallback or protocol guessing |

## Canonical capability model

Represent capabilities explicitly: supported, unsupported, conditionally supported, unknown, disabled by policy, or unavailable in current state. Do not infer a capability from the presence of an endpoint alone. Bind observations to model, firmware, profile/API revision and configuration.

## Translation rules

- Preserve original source, identifiers, times, sequence, quality, units and raw status reference.
- Map only meanings supported by both sides; expose lossy translation as a first-class limitation.
- Never invent success when a downstream protocol has only delivery acknowledgement.
- Normalize identifiers without discarding the vendor/native value needed for diagnostics.
- Separate unknown from false, closed, inactive or healthy.
- Define round-trip behavior before supporting configuration writes.

## Gateway security

Terminate and independently authenticate both sides. Apply per-direction, per-operation authorization and schema/size validation. A secure upstream protocol does not make an unauthenticated downstream bus secure; document the trust breakpoint and compensating controls.

## Failure behavior

Define startup discovery, partial inventory, downstream outage, upstream outage, stale cache, split-brain, duplicate messages, upgrade/version mismatch, queue overflow, clock loss and gateway restart. Physical actuation must default to simulation in documentation examples.

## Sources

- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], zones, conduits and OT gateway context, accessed 2026-08-25.

[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## Related pages

- [Event normalization and schema evolution](event-normalization-and-schema-evolution.md)
- [Segmentation and conduits](../../06-security-and-assurance/segmentation-and-conduits.md)
