---
title: Johnson Controls C•CURE Integrations
summary: Evidence-bounded catalogue of C•CURE 9000 SDK, web-service, Connected Partner, victor, and licensed product-integration surfaces.
page_type: vendor-api
domains: [access-control, alarms, integration]
tags: [johnson-controls, software-house, ccure-9000, connected-partner, sdk]
scope: global with product, version, package, and licence differences
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public Johnson Controls and Software House product/integration documentation establishes SDK and web-service routes; current developer contracts, methods, authentication, package versions, licences, compatibility, and partner-only material are excluded.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Johnson Controls C•CURE integrations

[Vendor APIs](../README.md) / [Access and identity](README.md) / Johnson Controls C•CURE

C•CURE 9000 integrations are delivered through a full platform SDK, selected web-service APIs, product-specific drivers and the Software House Connected Partner programme. Public Johnson Controls documentation is rich for named integrations but does not expose one current general developer reference. Use each public artefact to establish a surface, then obtain the exact supported package and licence.

## Verified surface map

| Surface | Public evidence | Boundary |
|---|---|---|
| C•CURE 9000 SDK | Official product/accessibility documents describe a full SDK exposing platform objects | Current package, runtime, object model, auth, redistribution and licence require Connected Partner/vendor access |
| Web-service API | Software House Connected material names web-service APIs; victor integration uses a victor Web Service API with C•CURE operator/client connections | Do not generalize the victor-specific topology to all integrations |
| Connected Partner kits/drivers | Named integrations ship with release notes, compatibility table and C•CURE licence option | Every driver is versioned and licensed independently |
| victor C•CURE integration | Synchronizes/operates C•CURE objects through the documented victor integration | victor and C•CURE builds, Web Service client connections and driver licence apply |
| BACnet/BMS integration | Maps supported BMS/C•CURE objects using a licensed BACnet/IP integration | Separate protocol/driver trust boundary; not the general C•CURE SDK |
| C•CURE Cloud | Single-tenant hosted C•CURE offering | Cloud deployment does not imply an Internet-public API or unchanged network/auth contract |

## Compatibility is the unit of support

Official C•CURE integration release notes publish a matrix containing C•CURE version, partner product/version, driver version, licence option, redundancy certification, operating system and database context. Require an equivalent matrix for every integration. A driver that works on a standalone server may not be enterprise/redundancy certified.

The Johnson Controls third-party software page listed C•CURE 9000 3.20 artefacts during review, while many public integration guides target 3.00 or older. Do not label 3.20 as the correct target or load an older integration into it without a support statement.

## Authentication and privilege

Use the exact SDK/Web Service/driver guide for operator identity, client connections, TLS, certificate, service account and permission configuration. Public victor documentation shows that one integration requires a C•CURE operator and sufficient licensed client connections; this is a planning example, not a universal count.

Separate personnel/credential administration, device/configuration reads, alarms/events, acknowledgement, door/output commands, intrusion arm/disarm and BMS control. The Connected ecosystem includes emergency and automation workflows, so an integration service must receive only its named object classes and actions.

## State, events, and high-impact commands

Establish initial object state, journal/event subscription behavior, filters, reconnection and failover semantics. Preserve C•CURE object identity, event time, ingest time and source. Reconcile after service/driver restart and enterprise failover.

Never treat a database row or SDK object update as proof that controllers received configuration. Never blind-retry unlock, lockdown, arm/disarm, alarm silence or output commands after timeout. Query current platform/controller state and journal or require operator resolution.

Do not access C•CURE database tables directly unless a current vendor integration contract explicitly authorizes and specifies it. Public product integrations that connect to a database are not a general extension pattern.

## Lifecycle and compatibility

Track C•CURE, SDK/web-service, partner driver, victor/IQ, operating system/database, controller firmware and licence together. Obtain current hardening and upgrade guides and rehearse rollback.

## Primary sources

- [Software House product/options page](https://www.swhouse.com/Products/web-mobile-apps) — current C•CURE 9000, Cloud and Connected Partner positioning.
- [Johnson Controls C•CURE third-party software information](https://www.johnsoncontrols.com/legal/digital/third-party-software-information) — dated product artefact inventory.
- [C•CURE 9000 SDK evidence](https://docs.johnsoncontrols.com/softwarehouse/api/khub/documents/YF2w33Yr4tdcnePS54aCzA/content) — official statement that platform objects are available through a full SDK.
- [victor C•CURE integration guide](https://docs.johnsoncontrols.com/americandynamics/api/khub/documents/J_GcvIrg0Na3qxyYfE9yRg/content) — product-specific Web Service, operator, client and licence boundary.
- [C•CURE 3.00 integration compatibility example](https://docs.johnsoncontrols.com/softwarehouse/r/Software-House/en-US/DSC-integration-for-C-CURE-9000-v3.0-Release-Notes/A/3.00/Compatibility-information) — official driver compatibility matrix pattern.
- [C•CURE BMS integration overview](https://docs.johnsoncontrols.com/softwarehouse/r/Software-House/en-US/Building-Management-System-Integration-Software-for-C-CURE-9000-v3.00-User-Guide/A/3.00/Integration-software-overview) — licensed product-specific BACnet boundary.

## Related pages

- [PACS architecture](../../03-systems/access-control/pacs-architecture.md)
- [BACnet/IP](../../02-protocols/building-and-industrial/bacnet-ip.md)
- [Threat modeling and trust boundaries](../../06-security-and-assurance/threat-modeling-and-trust-boundaries.md)
