---
title: CAN, CANopen, and SAE J1939
summary: Layer boundaries, identifiers, state machines, data models, diagnostics, and security constraints across CAN-based ecosystems.
page_type: protocol
domains: [ot, cross-domain]
tags: [can, can-fd, canopen, j1939, fieldbus]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [ISO 11898-1, ISO 11898-2, CiA 301 v4.2.0, SAE J1939]
coverage_limit: The page distinguishes families but does not reproduce licensed ISO, CiA, or SAE bit-level specifications, profiles, or parameter assignments.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# CAN, CANopen, and SAE J1939

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / CAN ecosystems

Controller Area Network (CAN) is a data-link/physical-layer family. CANopen and SAE J1939 are different higher-layer ecosystems using CAN. Sharing a CAN controller or connector does not make their identifiers, bit rate, addressing, transport, device model, or diagnostics interoperable.[^higher]

## CAN layer

CAN arbitrates using the message identifier: numerically dominant identifiers gain bus access, so an identifier carries priority and message meaning—not a trustworthy sender identity. Classical CAN and CAN FD differ in frame capabilities. CANopen CC uses CAN Classical; CANopen FD uses CAN FD.[^lower]

Record ISO 11898 variant, Classical/FD, nominal and data-phase bit rates, 11/29-bit identifiers, sample-point/timing assumptions, termination, topology, transceiver voltage, isolation, connector pinout, and bus load. Error detection and fault confinement improve link reliability but do not provide cryptographic authenticity, confidentiality, freshness, or authorization.

## CANopen

CANopen uses an object dictionary as the device's structured interface. CiA 301 defines the classic application/communication profile; CiA lists version 4.2.0, with CANopen FD defined separately by CiA 1301.[^cia]

Key mechanisms include:

- Network Management (NMT) states and commands;
- heartbeat/error control and boot-up indication;
- Process Data Objects (PDOs) for configured process data;
- Service Data Objects (SDOs) for object-dictionary access;
- emergency messages (EMCY), synchronization, and time distribution.

An integration must pin the device/communication profile, EDS/DCF revision, node ID, object index/subindex, data type, PDO mapping, transmission type, heartbeat, NMT ownership, and save/restore behaviour. SDO success does not establish that a value was persistently stored or physically applied.

## SAE J1939

J1939 commonly uses 29-bit CAN identifiers and defines Parameter Group Numbers (PGNs), Suspect Parameter Numbers (SPNs), source addresses, address claim, network management, diagnostics, and multi-packet transport. The SAE top-level and Digital Annex are revisioned separately; the Digital Annex is the living assignment source for PGNs/SPNs, not the top-level prose standard alone.[^j1939][^da]

Bind values to exact PGN/SPN definitions and revision, scaling, offset, range, `not available`/error encodings, repetition rate, source address and claimed NAME. Source addresses can change through address claim and are not cryptographic identities. J1939-21 and J1939-22 cover different data-link capabilities; confirm Classical CAN versus CAN FD profile before decoding transport sessions.[^j193922]

## Security and safety

Passive access can reveal operational state; active injection, diagnostic sessions, NMT commands, address claim, or high-priority traffic can disrupt a bus and move machinery. Use an isolated, listen-only interface on an approved bench. Enforce bus-side gateways with identifier/rate/direction policy, authenticate higher-level remote access, and detect new identifiers, address-claim conflict, error storms, bus-off, impossible rates, diagnostic/control traffic, and changed device profiles.

Validate exact electrical characteristics, arbitration behaviour, decoder limits, error recovery, and product profiles on an isolated listen-only or otherwise approved bench.

## Primary sources

[^higher]: [CAN in Automation — standardized higher-layer protocols](https://can-cia.org/can-knowledge/standardized-higher-layer-protocols)
[^lower]: [CAN in Automation — CANopen lower layers](https://www.can-cia.org/can-knowledge/canopen-lower-layers)
[^cia]: [CAN in Automation — technical documents](https://www.can-cia.org/cia-groups/technical-documents)
[^j1939]: [SAE International — J1939 top-level document](https://saemobilus.sae.org/standards/j1939_202306-serial-control-communications-heavy-duty-vehicle-network-top-level-document)
[^da]: [SAE International — J1939 Digital Annex](https://saemobilus.sae.org/standards/j1939da_202506-j1939-digital-annex)
[^j193922]: [SAE International — J1939-22 FD data-link layer](https://saemobilus.sae.org/standards/j1939-22_202103-fd-data-link-layer)
- [CAN in Automation — CANopen overview](https://www.can-cia.org/can-knowledge/canopen)
