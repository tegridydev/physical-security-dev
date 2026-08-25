---
title: Physical Access-Control Systems
summary: Architecture and navigation for PACS, controllers, doors, credentials, biometrics, mobile access, offline policy, visitors, and lift integration.
page_type: index
domains: [access-control, identity]
tags: [pacs, doors, credentials, readers, access-control]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 60839-11-1:2013", "IEC 60839-11-5:2020", ONVIF Profiles A C D]
coverage_limit: Architecture only; lock/egress/fire/lift design and legal access decisions require the authority having jurisdiction and qualified professionals.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Physical access-control systems

Physical access control spans identity governance, credential issuance, local controller decisions, door hardware, life-safety behavior, and audit. Treat each as a separate authority.

## Pages

- [PACS architecture](pacs-architecture.md)
- [Panels, readers, and door I/O](panels-readers-and-door-io.md)
- [Locks, egress, and life safety](locks-egress-and-life-safety.md)
- [Credential lifecycle](credential-lifecycle.md)
- [Biometrics](biometrics.md)
- [Mobile access](mobile-access.md)
- [Pedestrian portals, turnstiles, and interlocked doors](pedestrian-portals-turnstiles-and-interlocked-doors.md)
- [Offline operation and anti-passback](offline-operation-and-anti-passback.md)
- [Visitor, identity, and elevator integration](visitor-identity-and-elevator-integration.md)

## Decision chain

```text
person -> identity/account -> credential -> reader transaction
       -> controller/PACS policy -> lock/turnstile/lift request
       -> sensed door/passage state -> immutable audit/event lifecycle
```

An access-granted decision, unlock output, door-contact change, and confirmed passage are different facts. Preserve uncertainty.

## Source baseline

[IEC 60839-11-1:2013](https://webstore.iec.ch/en/publication/3662) establishes public scope for electronic access-control system/component functionality, performance, logging, identification, and information control. [IEC 60839-11-5:2020](https://webstore.iec.ch/en/publication/33414) specifies OSDP between access-control units and peripherals. ONVIF [Profiles A, C, and D](https://www.onvif.org/profiles/) address access configuration, basic door/events, and peripherals respectively; verify exact product conformance and conditional features.

Return to [Systems](../README.md).
