---
title: Serial and Field Interfaces
summary: Electrical layer, framing, topology, termination, supervision, isolation, and safe gateways for RS-232, RS-485, Wiegand, and field buses.
page_type: foundation
domains: [access-control, alarms, intercom, bms, ot, video]
tags: [serial, rs-232, rs-485, fieldbus, wiring]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [TIA-232, TIA-485]
coverage_limit: Conceptual engineering guidance; exact electrical values, cable, topology, and installation rules must come from applicable standards and product manuals.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Serial and field interfaces

“Serial” describes bit transfer, not an application protocol. An integration is only defined when electrical interface, connector/pinout, topology, baud/timing, frame format, addressing, error handling, and application semantics all match.

## RS-232 and RS-485

- TIA-232-family interfaces are commonly point to point and single ended. Product connectors and voltage/interface implementations vary; never infer pinout from a connector shell.
- TIA-485-family interfaces use differential signalling and support multipoint buses. Products label lines `A/B`, `+/-`, or other conventions inconsistently; verify against both manuals and measure only under an approved procedure.
- Neither interface supplies application framing, device discovery, encryption, or authorization. OSDP, Modbus RTU, BACnet MS/TP, Pelco telemetry, and vendor protocols add their own rules.

The TIA standards are normative and generally paywalled; the [TIA standards catalogue](https://tiaonline.org/what-we-do/standards/) is the official access point. This page deliberately does not reproduce electrical limits.

## Bus design record

Document:

```text
interface standard and transceiver type
connector and verified pinout
cable type, shield/drain, reference/common, and grounding scheme
topology, total length, stubs, nodes, and isolation boundaries
termination and bias/fail-safe arrangement
baud, data bits, parity, stop bits, and turn-around timing
protocol edition, address allocation, and secure mode
power source, current budget, voltage drop, and fault protection
```

Termination belongs at the electrically defined ends, not automatically every device. Biasing must be coordinated so multiple devices do not fight. Ground potential differences, surge/lightning exposure, induced noise, and shared power faults can damage interfaces or create intermittent framing errors; use qualified electrical design and isolation.

## Direction and collision

Two-wire half-duplex buses require controlled transmitter enable and turnaround. The application protocol may define controller polling, token passing, contention, or reply delays. A serial-to-IP converter that tunnels bytes does not fix collision, addressing, or timing and may introduce variable latency or reconnect boundary issues.

## Supervision and security

Physical reachability of a bus can expose credentials, events, or commands when the application protocol lacks cryptographic protection. Enclosures, cable routes, tamper detection, line supervision, restricted commissioning, and network gateway policy are part of security.

Where an authenticated/encrypted protocol mode exists—such as OSDP Secure Channel—use it with managed keys. Do not describe a private cable route as encryption.

## Safe diagnostics

Start with configuration and device counters. Passive observation using isolated, appropriate equipment is less disruptive than injecting frames, but still requires authorization and electrical competence. Never attach an unknown ground/reference or termination to a live fire, door, gate, lift, alarm, or safety-related circuit without approved drawings and responsible personnel.

## Gateway requirements

A gateway must bound serial frames and timing, validate addresses/functions, authenticate the IP side, rate-limit requests, serialize concurrent operations, expose bus health, preserve provenance, and define behaviour when a TCP session retries after an indeterminate serial outcome.

