---
title: EtherNet/IP and CIP
summary: CIP objects, EtherNet/IP explicit and implicit messaging, connection state, multicast, CIP Security, and safe integration.
page_type: protocol
domains: [ot, cross-domain]
tags: [ethernet-ip, cip, odva, implicit-io, cip-security]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [ODVA CIP Networks Library Volume 1, EtherNet/IP Volume 2 v1.36, CIP Security Volume 8 v1.21]
coverage_limit: The licensed ODVA specifications, device EDS, profiles, and conformance declarations are required for wire implementation and product interoperability.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# EtherNet/IP and CIP

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / EtherNet/IP and CIP

EtherNet/IP adapts the Common Industrial Protocol (CIP) to Ethernet and IP. CIP provides an object model, services, connections, device profiles, and network-independent application semantics. “EtherNet/IP” is the ODVA technology name; it is not a generic abbreviation for any Ethernet protocol.[^overview]

## Messaging modes

| Mode | Typical use | Transport characteristic |
|---|---|---|
| Explicit messaging | configuration, attributes, diagnostics, connection setup | request/response, commonly TCP via encapsulation |
| Implicit I/O | time-sensitive producer/consumer data under an established CIP connection | commonly UDP, cyclic or change-of-state, may use multicast |

ODVA's overview identifies TCP/UDP port 44818 for EtherNet/IP encapsulation and UDP 2222 for I/O traffic.[^overview] Ports alone are not sufficient policy: constrain expected originator/target, direction, connection identifiers, multicast groups, assembly instances, requested packet interval (RPI), and service/class/instance/attribute paths.

## Developer contract

Pin the device profile and EDS revision, vendor/device/product identifiers, firmware, supported CIP services, class/instance/attribute paths, assembly layouts, byte/bit ordering, configuration data, connection type, RPI, timeout multiplier, owner type, and run/idle behaviour. Reject identity mismatch instead of downloading a “close enough” assembly map.

Keep TCP/encapsulation session, CIP connection, I/O validity, sequence/state, device fault, and physical process state distinct. After a reconnect, do not reuse stale connection identifiers or replay queued commands. Define what happens when multicast joins fail, an exclusive owner already exists, electronic keying fails, I/O times out, or configuration ownership changes.

## CIP Security

CIP Security is specified in Volume 8. ODVA describes TLS for TCP traffic, DTLS for UDP traffic, X.509 certificates or pre-shared keys, and security profiles for authenticating endpoints and protecting messages.[^security] The current specification page lists EtherNet/IP Volume 2 v1.36 and CIP Security Volume 8 v1.21.[^specs]

- Prefer unique certificate identities and least-privilege profile/role configuration; constrain PSKs to products/use cases that require them and avoid fleet-wide reuse.
- Protect provisioning and trust-list management as separate control planes.
- Plan renewal, time, revocation, algorithm/profile negotiation, and secure/non-secure coexistence explicitly.
- A secure gateway or proxy terminates protection; identify the cleartext downstream boundary.
- Transport protection does not make arbitrary CIP services or I/O outputs safe or authorized.

## Safety boundary

Discovery, configuration writes, Forward Open, implicit I/O ownership, reset services, and output assemblies can change live equipment. CIP Safety has separate certified semantics and is not implied by EtherNet/IP or CIP Security. Work from a vendor-approved offline profile and use an isolated bench for connection, multicast, recovery, and output validation.

## Primary sources

[^overview]: [ODVA — EtherNet/IP Technology Overview, PUB00138R8](https://www.odva.org/publication_download/ethernet-ip-technology-overview/)
[^security]: [ODVA — CIP Security](https://www.odva.org/technology-standards/distinct-cip-services/cip-security/)
[^specs]: [ODVA — current specification editions](https://www.odva.org/subscriptions-services/specifications/)
- [ODVA — Common Industrial Protocol](https://www.odva.org/technology-standards/key-technologies/common-industrial-protocol-cip/)
- [ODVA — CIP Security at a glance](https://www.odva.org/publication_download/cip-security-at-a-glance-pub-319/)
