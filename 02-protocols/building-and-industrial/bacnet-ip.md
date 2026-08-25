---
title: BACnet/IP
summary: BVLL, broadcast management, routing, discovery, transaction handling, and defensive deployment for BACnet over IP.
page_type: protocol
domains: [bms, cross-domain]
tags: [bacnet-ip, bvll, bbmd, discovery, udp]
scope: global
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: [ANSI/ASHRAE 135-2024 Annex J]
coverage_limit: The licensed BACnet standard is required for normative BVLL and NPDU/APDU encoding and conformance work.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# BACnet/IP

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / [BACnet](bacnet-family.md) / BACnet/IP

BACnet/IP, defined by Annex J of the BACnet standard, carries BACnet network and application messages in a BACnet Virtual Link Layer (BVLL) over UDP/IP. Deployments commonly use UDP port 47808 (`0xBAC0`), but port, BACnet network number, subnet, and routing design must come from the project configuration.[^faq]

## Broadcast domains and BBMDs

BACnet discovery and some service patterns use broadcasts. IP routers do not normally forward subnet broadcasts. A BACnet Broadcast Management Device (BBMD) distributes BACnet broadcasts between configured IP subnets, while a Foreign Device can register with a BBMD for a bounded lifetime.

Treat the Broadcast Distribution Table and Foreign Device Table as controlled routing/security configuration:

- allow only expected peers and registration sources;
- avoid duplicate or circular BBMD meshes;
- monitor table changes, registration churn, and broadcast-rate anomalies;
- never solve reachability by exposing BACnet UDP to the public Internet;
- document NAT explicitly—addresses carried in BVLL control information and topology assumptions can make casual translation fail.

## Client state

BACnet confirmed services use invoke identifiers to correlate responses. Keep a bounded per-peer transaction table and distinguish SimpleACK, ComplexACK, Error, Reject, Abort, timeout, and transport loss. Segment handling, maximum APDU, windowing, retries, and concurrent invoke IDs must follow the peer's declared and observed limits.

Discovery results are untrusted input. Enforce maximum message and collection sizes; normalise neither object names nor vendor strings into identifiers; and detect a device instance appearing at an unexpected address. Do not let repeated I-Am traffic overwrite a trusted inventory binding without review.

## Security posture

Classic BACnet/IP does not give every message modern cryptographic peer authentication or confidentiality. Network isolation, strict routing, source/destination allowlists, BBMD governance, write authorization, and monitoring remain necessary. Where products support it, [BACnet Secure Connect](bacnet-secure-connect.md) provides a TLS-based data link; migration still requires object/service authorization and secure management planes.

Packet capture or active Who-Is can expose building topology and may load controllers. Validate discovery rate limits, routing boundaries, write controls, and recovery behaviour in an authorized environment before enabling them at a site.

## Primary sources

[^faq]: [ASHRAE BACnet Committee — BACnet FAQ](https://bacnet.org/faq/)
- [ASHRAE BACnet Committee — obtaining the current standard](https://bacnet.org/buy/)
- [ASHRAE BACnet Committee — developer aids](https://bacnet.org/developer-aids/)
