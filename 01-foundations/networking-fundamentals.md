---
title: Networking Fundamentals
summary: Network concepts most relevant to cameras, controllers, VMS, PACS, alarm, intercom, BMS, and OT integrations.
page_type: foundation
domains: [cross-domain]
tags: [networking, ethernet, ip, tcp, udp, qos]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: [RFC 8200, RFC 9293, RFC 768]
coverage_limit: Engineering primer, not a substitute for network design and packet-level specifications.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Networking fundamentals

Physical-security traffic combines bursty events, management operations, time-sensitive voice/video, discovery multicast, firmware transfer, and sometimes control. Design for their different properties rather than placing all “security devices” into one undifferentiated network.

## Layered path

```text
application message
  -> optional TLS/DTLS/security framing
  -> TCP stream or UDP datagrams
  -> IPv4/IPv6 packets
  -> Ethernet/Wi-Fi/VPN/link
  -> switches, routers, firewalls, NAT, WAN
```

Capture both endpoints, direction, DNS name, address family, transport, port, connection initiator, authentication, expected rate/size, and failure behaviour in an interface inventory.

## TCP and UDP

TCP is a reliable ordered **byte stream**, standardized by [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293). Applications still need message framing, deadlines, cancellation, keepalive/health semantics, reconnect, and protection against stalled peers. A successful write only means bytes entered the local stack.

UDP, specified by [RFC 768](https://www.rfc-editor.org/rfc/rfc768), preserves datagram boundaries but does not guarantee delivery, order, duplicate suppression, congestion handling, or peer identity. It is common for discovery, multicast, RTP, and constrained/field protocols. The application or enclosing protocol must provide required reliability and security.

## MTU and fragmentation

Paths have a maximum transmission unit (MTU). Tunnels, VPNs, IPv6, and WAN services can reduce effective payload size. Fragment loss can discard a whole datagram; middleboxes may mishandle fragments. Prefer protocol-defined packetization and path-MTU-aware libraries over arbitrary large UDP messages. Never assume a payload that worked on one LAN works across a routed or tunneled path.

## Bandwidth is not enough

For video and voice, plan:

- average and peak bitrate, including I-frame bursts;
- simultaneous live views, recording streams, playback, export, and analytics;
- packet loss, jitter, latency, and retransmission effects;
- multicast replication points and receiver joins;
- storage/WAN catch-up after outage;
- encrypted tunnel and protocol overhead;
- failure of one link or recorder.

Quality of Service (QoS) markings do not create capacity. Trust and remarking policy must be consistent end to end, and control/management traffic must not be starved by video.

## Address family and naming

Support IPv4 and IPv6 intentionally. [RFC 8200](https://www.rfc-editor.org/rfc/rfc8200) defines IPv6; IPv6 link-local addresses, neighbor discovery, multicast, extension headers, and firewall policy differ from IPv4. Avoid disabling IPv6 while leaving it unmonitored.

Use DNS names for services where certificates, migration, or redundancy require stable naming, but design for DNS outage and cache behaviour. Device identity must not equal IP address.

## Network controls

- Default-deny inter-zone policy based on documented flows.
- Separate observation, control, management, and guest/user paths where practical.
- Restrict device egress to named services and required destinations.
- Protect and monitor DHCP, DNS, time, certificate, update, and identity dependencies.
- Use network access control as one signal, not proof the endpoint is trustworthy.
- Preserve an out-of-band recovery path for critical controllers and gateways.

See [IP addressing, routing, and ports](ip-addressing-routing-and-ports.md), [multicast, discovery, and NAT](multicast-discovery-and-nat.md), and [trust boundaries](trust-boundaries-and-segmentation.md).
