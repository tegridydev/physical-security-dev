---
title: Modbus family
summary: Architecture, data model, transaction semantics, and safe integration patterns shared by Modbus transports.
page_type: protocol
domains: [bms, ot, cross-domain]
tags: [modbus, registers, coils, gateway, ot]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [Modbus Application Protocol V1.1b3]
coverage_limit: Covers the public application specification and transport relationships; device register maps and product limits are vendor-specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Modbus family

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / Modbus family

Modbus defines a compact application protocol above several transports. Its logical data areas are coils, discrete inputs, input registers, and holding registers. The standard defines protocol data units and function semantics; it does **not** define what register `40001` means for a particular panel, lift, meter, or controller.[^app]

## Layering

```text
device meaning and register map     vendor/product profile
function code + addresses + data    Modbus PDU
serial address + CRC                Modbus RTU ADU
or transaction/unit header          Modbus TCP ADU
or TLS-protected TCP                Modbus Security transport
```

Read [Modbus RTU](modbus-rtu.md), [Modbus TCP](modbus-tcp.md), and [Modbus Security](modbus-security.md) for transport-specific behaviour.

## Data-model traps

- Protocol addresses are zero-based fields. Human-facing documents often use `0xxxx`, `1xxxx`, `3xxxx`, or `4xxxx` reference notation. Store both the original notation and the on-wire address; never guess an offset.
- A register is 16 bits, but multi-register integers, floating-point values, text, byte order, word order, scaling, signedness, and sentinel values are profile-specific.
- Read/write access and function support are device-specific. An address responding to a read does not establish that writes are safe.
- Exception responses are protocol outcomes, not transport failures. Preserve the exception code and request correlation.
- A successful write response proves protocol acceptance, not physical completion or safe actuation.

## Adapter contract

For every point, record unit/slave identifier, function, zero-based address, width, encoding, scale, unit, access, poll interval, stale threshold, validity rules, write interlocks, and source document revision. Decode into a value plus quality and source timestamp. Retain an explicit `unknown` state.

Coalesce only adjacent reads with identical access semantics and within both the protocol limit and the device's documented maximum. A theoretically legal large request can still overrun a small gateway. Bound outstanding requests, randomise reconnect backoff, and prevent fleet-wide synchronized polling.

## Security and safety

Classic Modbus provides no cryptographic peer identity, confidentiality, or authorization. Treat network location and unit identifier as routing hints, not identity. Segment the path, allowlist exact peers and function codes, make write capability opt-in, and monitor new unit IDs, write functions, scan-like address patterns, and exception-rate changes. Prefer [Modbus Security](modbus-security.md) when all endpoints support it, while retaining application authorization and engineering controls.

Never use exploratory writes on production equipment. Reads can also cause load or interact with fragile gateways. Bench-test against a documented register map, then deploy with an asset-owner-approved poll budget and rollback plan.

## Primary sources

[^app]: [Modbus Organization — Modbus Application Protocol Specification V1.1b3](https://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf)
- [Modbus Organization — current specifications and implementation guides](https://www.modbus.org/modbus-specifications)
