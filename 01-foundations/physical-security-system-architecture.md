---
title: Physical-Security System Architecture
summary: Actors, planes, boundaries, and common deployment patterns across video, access, alarms, intercom, BMS, and OT.
page_type: foundation
domains: [video, access-control, alarms, intercom, bms, ot]
tags: [architecture, systems, trust-boundaries, data-flow]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [NIST SP 800-82 Rev. 3]
coverage_limit: Generic reference architecture; actual authority and safety boundaries are site-specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Physical-security system architecture

A useful architecture separates **field effects**, **control decisions**, **observation/data**, and **administration**. Products may combine those planes, but the security review should not.

## Reference topology

```text
People / vehicles / environment
            |
Field devices and circuits
  cameras | readers | locks | sensors | intercoms | relays
            |
Controllers and edge compute
  access panels | NVR/edge storage | alarm panels | PLC/BAS controllers
            |
Site platforms and gateways
  VMS | PACS | receiver | intercom server | protocol gateway | broker
            |
Enterprise and cloud services
  identity | SIEM | PSIM | analytics | case management | VSaaS | BMS/SCADA
            |
Operators, maintainers, APIs, and automation
```

Every vertical line may contain multiple networks, suppliers, credentials, protocols, and administrative owners. A cloud connection initiated from a device still crosses a trust boundary even when no inbound port is exposed.

## Four planes

| Plane | Examples | Design concern |
|---|---|---|
| Physical/control | lock output, alarm inhibit, PTZ, relay, credential update | Safety, least authority, confirmation, manual override |
| Observation/data | video, door state, alarms, health, audit | Provenance, time, privacy, loss and duplication |
| Management | configuration, firmware, users, certificates, time sources | Strong identity, separate roles, change control, recovery |
| Discovery/bootstrap | DHCP, DNS, WS-Discovery, mDNS, enrollment | Initial trust, spoofing, unintended exposure, secure defaults |

Do not give an integration management authority merely because it needs observations. Use distinct accounts, endpoints, ACLs, certificates, and network paths where the product permits.

## Sources of authority

For each entity or property, name the authoritative writer:

- identity source governs a person's lifecycle attributes;
- PACS governs access rights and access decisions;
- access controller governs local door logic and cached decisions;
- door contact reports a sensed position, not the lock state;
- VMS governs recording policy and logical camera mapping;
- camera or trusted time service may originate capture time;
- monitoring procedure, not merely a receiver message, governs alarm response.

Two sources can both be valid but represent different things. “Door unlocked,” “lock relay energized,” “request to exit active,” and “door open” must not collapse into a single Boolean.

## Common patterns

### On-premises control, enterprise observation

Controllers continue local operation during upstream loss; gateways export events northbound. This can limit blast radius, but requires replay/catch-up, sequence tracking, local storage bounds, and health signalling.

### Cloud-managed edge

Devices initiate authenticated outbound sessions for configuration, events, and media. Review tenant isolation, device enrollment, token/certificate rotation, offline behaviour, regional storage, support access, and cloud dependency.

### Cross-domain broker

A gateway normalizes events from VMS/PACS/alarm/BMS into a shared bus. Treat it as a high-value policy enforcement point. It should not automatically create a reverse command route; use separate topics/interfaces and authorization.

### Federated platforms

Multiple sites or products retain local authority while a central platform offers a unified view. Stable global identifiers, site scoping, version compatibility, clock quality, and partial-failure visibility are essential.

## Availability and safety

Define what continues when DNS, identity, cloud, WAN, broker, database, time, or certificates fail. Local emergency and life-safety behaviour must not depend on a convenience integration unless the complete system has been engineered and approved for that dependency.

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) includes physical access control and building automation in operational technology and frames controls around performance, reliability, and safety. Use that lens for any path capable of physical effect.

