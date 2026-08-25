---
title: IP transport and segmentation
summary: Ethernet, IPv4/IPv6, TCP/UDP, multicast, VLAN, NAT, MTU, QoS, and zone/conduit guidance for physical-security systems.
page_type: reference
domains: [networking, cross-domain]
tags: [ethernet, ipv4, ipv6, tcp, udp, vlan, segmentation]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [IEEE 802.3-2022, IEEE 802.1Q-2022, RFC 8200, RFC 9293, RFC 768]
coverage_limit: Design baseline, not a site addressing plan, firewall rule set, or performance validation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# IP transport and segmentation

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / IP transport and segmentation

Ethernet and IP provide reachability, not application interoperability or trust. IEEE 802.3 defines Ethernet layers; IEEE 802.1Q covers bridges and VLANs. IPv6 is standardized in RFC 8200, TCP in RFC 9293, and UDP in RFC 768.[^ethernet][^ipv6][^tcp][^udp]

## Layer contract

| Layer | Record explicitly | Common false inference |
|---|---|---|
| Ethernet | link speed/duplex, VLAN, MTU, PoE, redundancy, multicast treatment | same VLAN means trusted |
| IP | v4/v6 addresses, prefix, routes, gateways, fragmentation policy, NAT | IP address is device identity |
| Transport | TCP/UDP, local/remote ports, connection direction, keepalive, timeout | TCP ACK means application completed |
| Application | protocol edition/profile, framing, correlation, authorization | TLS alone makes commands safe |

TCP is a byte stream: parsers must handle partial and coalesced messages, bound lengths, and implement application correlation. UDP preserves datagram boundaries but not delivery, ordering, uniqueness, or path-MTU success; application retry and duplicate rules are essential. Neither transport authenticates a peer.

## IPv4 and IPv6

Maintain policy parity. An IPv4-only firewall rule does not constrain IPv6, and link-local IPv6 may remain active even when no global address was planned. Inventory all addresses, extension-header policy, multicast dependencies, neighbour-discovery exposure, DNS records, default routes, and management binding. Do not disable IPv6 casually when the product or secure protocol uses it; constrain and monitor it deliberately.

NAT is not an authorization control. It can break protocols that advertise embedded addresses, use multicast/broadcast, accept inbound callbacks, or bind security identity to an endpoint name. Prefer routed, policy-controlled zones and protocol-aware configuration over undocumented address translation.

## Segmentation pattern

Create zones from consequence and administration—not vendor alone: endpoints, controllers/servers, management, monitoring, identity/time, operator clients, and third-party/remote service. Define conduits as exact source, destination, direction, protocol, port, initiating role, rate, and maintenance window. Default-deny unused east-west and management access; log policy changes and denials at a sustainable rate.

VLANs provide logical separation inside a bridge domain but require routed enforcement to become a security boundary. QoS, multicast snooping/queriers, redundancy, and security inspection must preserve alarm latency, media bandwidth, and industrial real-time requirements. Validate failover and congestion on an isolated representative design.

## Failure and observation

Instrument link transitions, address/route change, duplicate address, neighbour/ARP churn, connection failure, RTT/loss, retransmission, UDP sequence gaps, MTU/fragmentation failure, multicast membership, firewall deny, and application health separately. A ping response is neither application health nor identity proof.

Validate segmentation, failover, congestion, MTU, multicast, and packet-filter behaviour against the authorized target network and recovery plan.

## Primary sources

[^ethernet]: [IEEE Standards Association — IEEE 802.3-2022](https://standards.ieee.org/ieee/802.3/10422/)
[^ipv6]: [RFC Editor — RFC 8200, IPv6](https://www.rfc-editor.org/info/rfc8200/)
[^tcp]: [RFC Editor — RFC 9293, TCP](https://www.rfc-editor.org/info/rfc9293/)
[^udp]: [RFC Editor — RFC 768, UDP](https://www.rfc-editor.org/info/rfc768/)
- [IEEE Standards Association — IEEE 802.1Q-2022](https://standards.ieee.org/standard/802_1Q-2022.html)
