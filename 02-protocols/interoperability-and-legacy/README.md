---
title: Interoperability and legacy protocols
summary: Index to cross-vendor PSIA models and legacy camera-control protocols that require strict edition and product scoping.
page_type: index
domains: [cross-domain, video, identity]
tags: [interoperability, legacy, psia, plai, pelco, visca]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [PSIA specifications, Pelco-D, Pelco-P, Sony VISCA]
coverage_limit: Family-level integration guidance; exact product manuals, schemas, profiles, firmware, and conformance records are required.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Interoperability and legacy protocols

[Home](../../README.md) / [Protocols](../README.md) / Interoperability and legacy

These technologies remain important when maintaining installed estates or joining systems from different eras. “Open,” “standard,” “compatible,” and “supports protocol X” are not interchangeable claims. Pin the edition, profile/subset, product, firmware, transport, security mode, extensions, and evidence.

| Reference | Current posture | Use |
|---|---|---|
| [PSIA specifications](psia.md) | Mixed: current access/credential work plus legacy video specifications | Shared service, security, metadata/event, area-control models |
| [PSIA PLAI](psia-plai.md) | Active PSIA focus; Area Control including PLAI v3.1 is the published baseline listed by PSIA | Synchronize identity, credentials, roles, and privileges across PACS/logical systems |
| [Pelco-D and Pelco-P](pelco-d-and-p.md) | Legacy, variant-prone | Serial PTZ and auxiliary camera commands |
| [Sony VISCA](visca.md) | Active in supported cameras; serial and IP forms differ | Camera command, inquiry, PTZ and preset control |

## Adapter rule

Keep a capability matrix for every endpoint. Unknown fields and commands must round-trip or fail explicitly, never default to a privileged state. Separate protocol receipt, acceptance, completion, observed device state, and operator outcome. Make command paths opt-in and read-only by default.

Legacy transports frequently lack encryption, authenticated identity, replay protection, or granular authorization. Put them behind a hardened gateway, isolate the segment, allowlist exact controllers and operations, protect management, and audit the translated identity. Do not label the downstream side “secure” merely because the upstream API uses TLS.

## Primary sources

- [PSIA — specifications overview](https://psialliance.org/specifications-overview/)
- [PSIA — legacy specifications and editions](https://psialliance.org/legacy-specs/)
- [Pelco — document centre](https://www.pelco.com/docs)
- [Sony — VISCA Command List for BRC/SRG cameras](https://pro.sony/support/res/manuals/E042/3230148ee903c204b912cca5c2c3f5aa/E0421001M.pdf)
