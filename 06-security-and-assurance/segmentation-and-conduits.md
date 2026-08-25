---
title: "Segmentation and conduits"
summary: "Network and application boundaries for cameras, controllers, management services, integrations, and operators."
page_type: security
domains:
  - infrastructure
  - building-industrial
tags:
  - segmentation
  - firewall
  - zones
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards:
  - "NIST SP 800-82 Rev. 3"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Segmentation and conduits

[Home](../README.md) / [Security and assurance](README.md) / Segmentation and conduits

Segmentation limits which identities and flows can reach a component; it does not repair an insecure protocol. A VLAN is an addressing and broadcast boundary, not a complete security policy. Enforce conduits with routed policy, firewalls, application gateways, host controls, and monitored identities.

## Recommended zones

| Zone | Typical contents | Default policy |
|---|---|---|
| Field/device | Cameras, readers, panels, sensors, intercoms | Initiate only explicitly required flows; no general Internet or user access |
| Management | VMS, PACS, alarm servers, configuration services | Reach devices on documented management/media/event ports only |
| Integration | Brokers, gateways, API adapters, PSIM connectors | Terminate and normalize cross-system traffic; no implicit transit |
| Identity and trust | Directory, IdP, RADIUS, CA, time | Only named consumers and protocols; protect administration separately |
| Operator | Workstations and consoles | Application access, not direct device administration by default |
| Security operations | Logging, monitoring, update and backup services | Prefer one-way collection where practical; tightly control response paths |
| Vendor support | Bastion or just-in-time support path | Disabled by default, approved, time-bound, recorded, and revocable |
| Safety-regulated | Fire, egress, elevator or other regulated functions | Separate authority and change control; integration must not replace certified functions |

## Flow specification

Document each permitted flow as a tuple:

| Field | Example meaning |
|---|---|
| Source identity and zone | Recording server service identity in management zone |
| Destination identity and zone | Exact camera inventory group in device zone |
| Protocol and secure mode | HTTPS with validated server certificate; RTP mode recorded separately |
| Ports/direction | Explicit fixed or negotiated range, including return behavior |
| Purpose | Configuration, events, media, health, or time |
| Authorization | Required device/API role and permitted object scope |
| Availability need | Continuous, commissioning-only, scheduled, or break-glass |
| Logging | Connection, authentication, command and denial evidence |
| Owner/review | Named system role and change trigger |

Do not approve a broad any-to-any rule merely because a vendor publishes a long port list. Trace actual topology, optional features, active/passive connection direction, multicast groups, discovery scope, NAT, and failover peers.

## Discovery and multicast

Broadcast and multicast discovery can cross intended boundaries through relays, proxies, or misconfigured routing. Constrain WS-Discovery, mDNS, SSDP, vendor discovery, IGMP, and multicast routing to defined commissioning or media domains. Prefer inventory-driven unicast after commissioning where the product permits it.

## Failure behavior

- Decide what happens when a firewall, gateway, DNS, NTP, IdP, CA, broker, or cloud path is unavailable.
- Avoid automatic plaintext fallback or silent certificate bypass.
- Rate-limit reconnect storms and preserve bounded queues.
- Keep local safety behavior independent of nonessential remote services.
- Monitor denied flows, but suppress neither repeated authentication failure nor loss of expected heartbeats.

## Review checklist

- Every route maps to a documented system data flow.
- Management and user traffic are distinct from media and device events.
- Administrative interfaces are not exposed to general client networks.
- Outbound device connectivity is allowlisted by destination identity and purpose.
- IPv6, secondary interfaces, Wi-Fi, cellular, VPNs and vendor tunnels are included.
- Temporary commissioning rules have expiry and removal evidence.
- Firewall policy and application authorization are both validated in a representative environment before deployment.

## Sources

- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], network architecture and segmentation guidance for OT, accessed 2026-08-25.
- **CISA-DEFENSE** — [CISA Recommended Practice: Improving Industrial Control Systems Cybersecurity with Defense-in-Depth Strategies][CISA-DEFENSE], accessed 2026-08-25.

[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final
[CISA-DEFENSE]: https://www.cisa.gov/resources-tools/resources/improving-industrial-control-systems-cybersecurity-defense-depth-strategies

## Related pages

- [Remote access](remote-access.md)
- [Identity, authentication, and authorization](identity-authentication-and-authorization.md)
- [Infrastructure protocols](../02-protocols/infrastructure/README.md)
