---
title: BACnet MS/TP
summary: Token passing, MAC addressing, serial timing, routing, failure handling, and safe commissioning for BACnet MS/TP.
page_type: protocol
domains: [bms]
tags: [bacnet, mstp, rs-485, token-passing, fieldbus]
scope: global
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: [ANSI/ASHRAE 135-2024 Clause 9]
coverage_limit: Normative state machines and electrical constraints require the licensed BACnet standard and current product manuals.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# BACnet MS/TP

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / [BACnet](bacnet-family.md) / MS/TP

BACnet Master-Slave/Token-Passing (MS/TP) is a BACnet data link normally carried on an EIA-485 multidrop bus. Master nodes pass a token to control transmission; slave-only nodes respond but do not hold the token. BACnet routers commonly bridge an MS/TP segment into BACnet/IP or BACnet/SC.[^stb]

## Three address spaces

Keep these separate in configuration and logs:

- the MS/TP MAC address on one serial segment;
- the BACnet network number assigned to that segment;
- the BACnet device instance at the application layer.

Duplicate MAC addresses corrupt token operation. Duplicate device instances create application ambiguity even when MACs differ. A router port must not reuse a network number already present elsewhere in the internetwork.

## Timing and token health

Correctness depends on baud, data format, bus wiring, turnaround, token timers, maximum master address, maximum frames per token, and implementation state-machine behaviour. Do not copy a generic serial profile without checking every node. A high `Max_Master` expands token search time; an incorrect low value makes higher-address masters unreachable.

Monitor token rotation time, retries, frame/CRC errors, silence, duplicate tokens, unexpected masters, router queueing, and device restart patterns. Rate-limit upstream polling so the router cannot saturate the serial segment. COV subscription traffic still consumes MS/TP bandwidth.

## Installation and diagnostics

Record topology, cable, segment length, baud, termination, bias, reference conductor/ground practice, isolation, MAC allocation, network number, router port, and power-domain boundaries. Use [serial transports](../infrastructure/serial-transports.md) for the distinction between protocol and electrical layer.

Passive observation should use an isolated, high-impedance interface. Adding a poorly configured USB adapter can change bias/termination or transmit unexpectedly. Active token or discovery tools require an isolated bench or explicit site authorization.

## Security boundary

MS/TP has no native per-frame confidentiality or cryptographic source authentication. Physical access, cabinet security, isolated routing, strict router ACLs, and application-level write controls are therefore material. BACnet/SC can secure the routed IP backbone but does not encrypt or authenticate an attached legacy MS/TP segment; the router is a security boundary.

## Primary sources

[^stb]: [ASHRAE BACnet Committee — BACnet MS/TP overview](https://bacnet.org/wp-content/uploads/sites/4/2022/06/STB-08-93.pdf)
- [ASHRAE BACnet Committee — standard status](https://bacnet.org/updates/)
- [ASHRAE BACnet Committee — obtaining the current standard](https://bacnet.org/buy/)
