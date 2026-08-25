---
title: "Synthetic Modbus/TCP read-response interpretation"
summary: "A bounded walkthrough of a synthetic Modbus/TCP read response with security and semantic limits."
page_type: development
domains:
  - building-industrial
tags:
  - modbus
  - binary
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-executed
safety_level: safety-relevant
standards:
  - "MODBUS Application Protocol V1.1b3"
coverage_limit: "Synthetic read-response interpretation only; device register maps, product behavior, interoperability, and operational authorization are outside this page's scope."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Synthetic Modbus/TCP read-response interpretation

[Home](../../README.md) / [Development](../README.md) / [Examples](README.md) / Modbus read response

Input: offline synthetic bytes  
Side effects: none; no network address or write function is provided

## Synthetic bytes

~~~text
00 2A  00 00  00 07  01  03  04  00 64  00 C8
-----  -----  -----  --  --  --  -----  -----
 TID    PID   length UID FC count reg0   reg1
~~~

Interpretation under the Modbus Application Protocol:

- transaction identifier: 0x002A, matched to the originating request;
- protocol identifier: zero for Modbus;
- length: remaining unit identifier plus PDU bytes;
- unit identifier: 0x01;
- function: 0x03, read holding registers response;
- byte count: four;
- two big-endian 16-bit register words: 100 and 200.

## What the bytes do not tell you

Register semantics, signedness, scaling, word order for multi-register values, freshness, engineering unit, authorization and safe meaning are device-model specific. A value of 100 must not be treated as gate position, voltage, alarm state or command result without the exact vendor register map and version.

Classic Modbus/TCP does not authenticate the peer or protect integrity/confidentiality. Modbus Security is a distinct TLS/X.509-based profile using port 802; product support must be confirmed [MODBUS-SPECS]. A read-only example is not permission to scan or query an operational PLC/controller.

## Defensive parser checks

- exact minimum and declared lengths;
- transaction and unit identifier context;
- expected function or exception response;
- byte count consistent with payload and requested quantity;
- bounded register count and offset arithmetic;
- device-specific type/word order only after the frame is valid;
- timeout, duplicate and mismatched response handling.

## Sources

- **MODBUS-SPECS** — [Modbus specifications and implementation guides][MODBUS-SPECS], V1.1b3 and Modbus Security overview, accessed 2026-08-25.

[MODBUS-SPECS]: https://www.modbus.org/modbus-specifications

## Related pages

- [Modbus/TCP](../../02-protocols/building-and-industrial/modbus-tcp.md)
- [Secure protocol parsing](../../06-security-and-assurance/secure-protocol-parsing.md)
