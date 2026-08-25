---
title: Architecture and Layering
summary: A practical layered model for classifying physical-security interfaces without confusing media, transports, protocols, profiles, and APIs.
page_type: foundation
domains: [cross-domain]
tags: [architecture, layers, protocols, integration]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: [ISO/IEC 7498-1, RFC 1122]
coverage_limit: Explanatory model; individual specifications remain authoritative about their own layering.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Architecture and layering

Layering prevents category mistakes. It does not mean every physical-security product cleanly implements the seven-layer Open Systems Interconnection (OSI) model; it gives a disciplined way to ask which component owns a behaviour.

## Working model

```text
Business and safety policy
  identity lifecycle | alarm handling | privacy | response | retention
Application semantics
  ONVIF | OSDP | SIA formats | Modbus | BACnet | OPC UA | vendor APIs
Messaging, session, and media control
  HTTP | MQTT | WebSocket | SIP | RTSP | SDP
Security context
  TLS | DTLS | SRTP | protocol secure modes | application authorization
Transport and network
  TCP | UDP | IP | routing | multicast | QoS
Link, electrical, and radio
  Ethernet | Wi-Fi | RS-485 | serial | BLE | NFC | Wiegand signalling
Physical effect
  sensor | reader | lock | relay | camera | loudspeaker | gate | indicator
```

“Security context” cuts across layers: TLS protects a transport connection; OSDP Secure Channel protects protocol messages; application roles constrain operations; physical enclosure protects keys and wiring. None substitutes for the others.

## Classify before selecting

For each interface, record:

| Question | Example answer |
|---|---|
| What is the medium/link? | Ethernet, RS-485 bus, BLE radio |
| What carries packets/messages? | IPv6/UDP, TCP, serial frames |
| What protects the path? | TLS 1.3 with mutual authentication, or no cryptographic protection |
| What defines application meaning? | ONVIF event topic, OSDP command/reply, vendor JSON schema |
| What profile/options apply? | ONVIF Profile T feature set; MQTT 5 session policy |
| What physical result is possible? | View stream, change configuration, energize output |
| Who authorizes it? | Device role, PACS policy, broker ACL, controller logic |

This exposes statements that are too vague. “The camera supports HTTPS” says nothing about which API is available, certificate validation, client identity, authorization, media protection, or downgrade behaviour. “RS-485 support” says nothing about baud rate, frame format, addressing, bus bias, or application protocol.

## Encapsulation is not equivalence

An application may be remapped without preserving every property:

```text
OSDP event -> gateway -> MQTT publication -> cloud webhook
```

The gateway must decide how to map device address, sequence, timestamp, priority, acknowledgement, retry, duplicate detection, and authorization. A transport bridge moves bytes; a protocol gateway terminates state machines; a semantic adapter changes meaning. Name the actual role.

## Profiles and products

A specification often offers too many choices for predictable interoperability. A profile selects mandatory and optional capabilities, roles, and sometimes conformance tests. A product can implement multiple profiles and native APIs. Record all four separately:

```text
product/version -> protocol edition -> role -> profile/options
```

Do not infer support from a logo or family name. Verify the exact product/firmware in the publisher's conformance database or declaration.

## Where failures live

- Link failure: loss, noise, collision, power, association.
- Network failure: addressing, routing, MTU, multicast, NAT, path asymmetry.
- Transport/session failure: timeout, reset, stalled connection, renegotiation.
- Application failure: rejected operation, unsupported feature, schema mismatch.
- Semantic failure: valid message with wrong identity, unit, time, or state meaning.
- Physical failure: accepted command but jammed door, disconnected relay, obscured lens.

Diagnose from lower layers upward but validate the intended outcome end to end.

## Sources

- [ISO/IEC 7498-1:1994 — Basic Reference Model: The Basic Model](https://www.iso.org/standard/20269.html) (ISO catalogue; normative text is paywalled)
- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122)
- [RFC 8200 — Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200)

