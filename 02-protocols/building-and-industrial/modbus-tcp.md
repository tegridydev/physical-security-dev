---
title: Modbus TCP
summary: MBAP framing, request correlation, gateway semantics, failure handling, and secure deployment guidance for classic Modbus TCP.
page_type: protocol
domains: [bms, ot]
tags: [modbus-tcp, mbap, tcp, gateway, port-502]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [Modbus Application Protocol V1.1b3, Modbus Messaging on TCP/IP Implementation Guide V1.0b]
coverage_limit: Does not define vendor register maps or claim interoperability with any product.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Modbus TCP

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / [Modbus](modbus-family.md) / TCP

Modbus TCP carries each PDU behind a seven-octet Modbus Application Protocol header (MBAP) over TCP, conventionally on port 502.[^tcp]

```text
transaction ID | protocol ID | length | unit ID | function + data
     2               2           2         1        variable
```

The transaction identifier correlates requests and responses. Protocol identifier is zero for Modbus. Length counts the following bytes, including unit identifier. The unit identifier is especially important when an IP endpoint fronts a downstream serial bus; it is not a cryptographic identity.

## Stream parser requirements

TCP preserves order, not message boundaries. A parser must accept a partial MBAP header, a partial body, or multiple ADUs in one receive operation. Before allocation, validate protocol identifier and a locally configured maximum length. Consume exactly one declared ADU, and do not accept trailing bytes as part of it.

Maintain a bounded table of outstanding transaction IDs. Reject unexpected or duplicate IDs, and define behaviour for wraparound, late replies, reconnects, and a peer that reuses identifiers. Do not retry a timed-out write blindly: the operation may have reached the server even if its response was lost.

## Gateway semantics

A unit ID commonly selects a device behind a bridge. Document whether the server ignores it, requires a fixed value, or routes it. Limit parallel requests to what the endpoint and downstream bus actually support. A reconnect must not replay old write queues automatically.

Keep these outcomes distinct: TCP connect failure, TCP close/reset, framing error, timeout, Modbus exception, successful protocol response, and observed physical state. Only a subsequent authoritative read or device-specific completion event can support a state-change claim.

## Security

Classic port 502 traffic has no built-in confidentiality or peer authentication. Use [Modbus Security](modbus-security.md) where supported. Otherwise place the endpoint behind strict conduits, block public exposure, allowlist client/server pairs and functions, and protect the controller's management plane independently. A generic TLS tunnel can protect a path but is not automatically conformant to the Modbus Security protocol or its authorization model.

## Primary sources

[^tcp]: [Modbus Organization — Modbus Messaging on TCP/IP Implementation Guide V1.0b](https://www.modbus.org/docs/Modbus_Messaging_Implementation_Guide_V1_0b.pdf)
- [Modbus Organization — Modbus Application Protocol Specification V1.1b3](https://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf)
- [Modbus Organization — specifications](https://www.modbus.org/modbus-specifications)
