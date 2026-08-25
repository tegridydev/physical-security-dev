---
title: Multicast, Discovery, and NAT
summary: Discovery scopes, multicast behaviour, NAT constraints, and secure onboarding of physical-security devices.
page_type: foundation
domains: [video, access-control, alarms, intercom, bms, ot]
tags: [multicast, discovery, nat, ws-discovery, mdns, igmp]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: [RFC 6762, RFC 6763, OASIS WS-Discovery 1.1]
coverage_limit: Product discovery behaviour and default enablement vary by firmware and configuration.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Multicast, discovery, and NAT

Discovery answers “what claims to be here?” It rarely proves device identity or authorization. Treat discovery output as untrusted candidate endpoints that must pass a separate enrollment and authentication process.

## Discovery families

| Mechanism | Typical use | Boundary behaviour |
|---|---|---|
| WS-Discovery | ONVIF and other SOAP device services | Uses multicast discovery plus unicast responses; normally local-scope unless proxied |
| Multicast DNS (mDNS) / DNS-SD | Local service names and attributes | Link-local multicast by design; reflectors widen trust/exposure |
| SSDP | UPnP discovery in some device ecosystems | Local multicast with device-provided URLs |
| Vendor broadcast/multicast | Initial IP assignment or device finder | Often unauthenticated and product specific |
| Directory/registry | Managed services, cloud enrollment, DNS | Routable but depends on registry trust and lifecycle |

[RFC 6762](https://www.rfc-editor.org/rfc/rfc6762) defines mDNS and [RFC 6763](https://www.rfc-editor.org/rfc/rfc6763) defines DNS-Based Service Discovery. The OASIS [WS-Discovery 1.1 specification](https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html) defines multicast discovery and managed discovery using a proxy.

## Secure enrollment pattern

```text
discover candidate
  -> constrain by expected network/physical location
  -> fetch minimum identity/capabilities
  -> authenticate or verify an out-of-band claim
  -> authorize enrollment
  -> assign stable inventory identity
  -> configure trust and rotate bootstrap secret
  -> disable unnecessary bootstrap services
```

Do not automatically trust a discovered endpoint, import its certificate without validation, or send it production credentials. Display-name, MAC prefix, serial claim, and source IP can all be spoofed or reassigned.

## Multicast media and events

IP multicast can efficiently deliver one stream to many receivers, but requires:

- a defined group/address scope and source model;
- Internet Group Management Protocol (IGMP) or Multicast Listener Discovery (MLD) behaviour at switches/routers;
- querier availability and snooping configuration;
- rate/capacity planning for flooding and failover;
- authorization and confidentiality design—group membership is not identity;
- monitoring for unwanted senders, joins, and replication.

Do not stretch multicast across zones solely to avoid a gateway. A controlled relay/proxy can enforce scope, identity, rate, and audit, but becomes a trust boundary.

## NAT traversal

NAT usually permits outbound sessions and complicates inbound reachability, embedded addresses, peer-to-peer media, and negotiated ports. WebRTC uses Interactive Connectivity Establishment (ICE), Session Traversal Utilities for NAT (STUN), and Traversal Using Relays around NAT (TURN) as an explicit framework; generic port forwarding is not an equivalent security design.

For cloud-connected devices, verify:

- which side initiates and how the peer is authenticated;
- destination allowlisting and DNS behaviour;
- reconnect/backoff and offline storage;
- relay/cloud access to media and metadata;
- token/certificate rotation;
- whether a cloud path creates reverse configuration or actuation authority.

## Diagnostics without scanning

Begin with managed switch multicast tables, DHCP/DNS logs, product discovery logs, device inventory, and an authorized passive capture at the relevant boundary. Discovery probes can trigger load or state on constrained devices; do not broadcast them outside an approved, isolated scope.

