---
title: Pelco-D and Pelco-P
summary: Cautious developer orientation to legacy Pelco serial PTZ command families, variants, framing, gateways, and safe control.
page_type: protocol
domains: [video]
tags: [pelco-d, pelco-p, ptz, serial, legacy]
scope: global
content_status: maintained
technology_status: legacy
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: [Pelco-D, Pelco-P]
coverage_limit: No current official standalone normative byte-level Pelco-D/P specification was located; the sketches below are non-normative orientation and every implementation must use the exact official product/controller manual.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Pelco-D and Pelco-P

[Home](../../README.md) / [Protocols](../README.md) / [Interoperability and legacy](README.md) / Pelco-D and Pelco-P

Pelco-D and Pelco-P are legacy serial command families widely associated with analogue PTZ cameras, domes, matrix/controllers, encoders, and telemetry receivers. Pelco product manuals document support for both families, but a current official standalone wire specification was not available in the reviewed Pelco document centre.[^manual][^docs] Treat every byte table circulating elsewhere as a hypothesis until confirmed by the exact device manual or vendor support.

## Non-normative orientation

Common implementations are recognizable by these shapes:

```text
Pelco-D-like:  FF | address | command 1 | command 2 | data 1 | data 2 | checksum
Pelco-P-like:  A0 | address | data 1 | data 2 | data 3 | data 4 | AF | checksum
```

Often-described checksum conventions are an additive modulo-256 checksum for D-like frames and XOR for P-like frames. Address bases, checksum coverage, command-bit meaning, speed ranges, extended commands, response/acknowledgement, presets, auxiliaries, query support, and framing parameters vary. Do **not** implement or claim Pelco compatibility from the sketches alone.

## Capability record

For each endpoint pin product/firmware, protocol variant, physical interface, connector/pinout, baud/data/parity/stop bits, address interpretation, duplex, controller ownership, checksum, supported base and extended commands, speed encoding, preset range, response format, turnaround, and gateway behaviour. Capture vendor documentation with its revision.

Parse into typed operations rather than forwarding arbitrary bytes. Allowlist required pan/tilt/zoom/focus/iris/preset/auxiliary functions. Clamp values to the product's documented range. Ensure continuous-movement commands have an explicit stop, timeout/dead-man control, connection-loss policy, and observed state where available.

## Security and gateway boundary

These serial protocols generally provide no cryptographic authentication, confidentiality, replay protection, or per-operator authorization. Physical possession of the bus or gateway path may confer control. Put serial servers/encoders in an isolated zone, allow one approved command source, protect gateway management, and audit translated operator identity plus bounded raw command evidence.

A TLS-protected API to a Pelco gateway secures only the upstream hop. The serial segment remains a trust boundary, and controller arbitration must prevent two systems fighting for PTZ ownership.

## Safety and privacy

PTZ movement can expose private areas, defeat coverage, strike stops, reveal operator attention, or interfere with an investigation. Preset and auxiliary commands can be more consequential than directional moves. Start with passive configuration review; any environment validation approved by the system owner requires an unoccupied isolated bench, mechanical clearance, emergency power isolation, independent observation, and abort criteria.

## Primary sources

[^manual]: [Pelco — DX Series manual documenting Pelco-D/P support](https://media.pelco.com/DX%20Series%20Client%20Operation%20Configuration%20Manual%201-12.pdf)
[^docs]: [Pelco — document centre](https://www.pelco.com/docs)
- [Pelco — developer support](https://www.pelco.com/support/developer-support)
