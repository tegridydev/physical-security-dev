---
title: LenelS2 OnGuard, OpenAccess, and Elements
summary: Evidence-bounded map of OnGuard OpenAccess web services, licensed OAAP integrations, OnGuard Cloud, and the distinct Elements cloud platform.
page_type: vendor-api
domains: [access-control, identity, integration]
tags: [lenels2, onguard, openaccess, elements, oaap]
scope: global with product, version, deployment, and licence differences
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public LenelS2 product, data-sheet, partner-certification, cloud, and portal material; current OpenAccess contract, API packages, auth, endpoint schemas, licences, DataConduIT status, and any Elements developer API are not publicly verified here.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# LenelS2 OnGuard, OpenAccess, and Elements

[Vendor APIs](../README.md) / [Access and identity](README.md) / LenelS2

LenelS2’s integration story spans the on-premises **OnGuard** platform, **OnGuard Cloud**, the **OpenAccess Web Services** API family, legacy/other data interfaces, and the distinct **Elements** SaaS platform. Do not infer that an OnGuard OpenAccess integration can call Elements or that the Elements OnGuard Connector is a general public API.

## Verified surface map

| Surface | Public evidence | Boundary |
|---|---|---|
| OnGuard OpenAccess Web Services | OnGuard product and data sheets identify RESTful/web-service integration; OnGuard 7.5 material described parity work with DataConduIT | Full current contract and samples are delivered through LenelS2 Connect/installed product and licences |
| OpenAccess event bridge | Official partner pages show REST plus SignalR event-bridge use for named certified integrations | Delivery behavior on one partner page is not universal; use the target OpenAccess guide |
| OAAP/technology-partner interfaces | Certified integrations list exact OnGuard releases, partner versions and API licence part numbers | Certification applies only to the listed combination and does not certify partner cybersecurity |
| OnGuard Cloud | Single-tenant cloud deployment with web/OpenAccess integration options in official brochure | Cloud network, region, edition, licence and support contract apply |
| Elements | Cloud access/video platform with continuous delivery and an Elements–OnGuard Connector | No general current public Elements developer API contract was established in this review |

## OnGuard contract

The OnGuard 8.3 data sheet observed during review lists continuing OpenAccess Web Services API updates. It is fixed evidence for that release, not a current-version claim. Record OnGuard server/enterprise version, OpenAccess component build, database/topology, API licence, service identity, event-bridge version and every target entity class.

Public OAAP partner pages demonstrate that LenelS2 issues integration-specific API licence part numbers and certifies named product/version combinations. Use that matrix for the selected partner interface. Do not treat “factory certified” as a blanket security, functionality or future-compatibility warranty; LenelS2 explicitly limits the certification statement on those pages.

DataConduIT appears in older OnGuard material as a comparison/legacy integration surface. Obtain the current lifecycle and migration guidance before maintaining or replacing it. Do not start new database or COM-based integration based on historical familiarity when OpenAccess is the supported route.

## Elements boundary

Official Elements material establishes a cloud access/video product, continuous delivery and the Elements OnGuard Connector for hybrid deployments. Public material does not establish a customer-general Elements API reference with authentication, schemas, limits and lifecycle. Therefore this catalogue makes no endpoint, SDK or access claim for Elements. Obtain written LenelS2 evidence for any proposed Elements integration.

Continuous delivery means capability and behavior can change without an on-premises upgrade event. Record tenant, release/change-notice channel, region, subscription and connector version, and maintain contract tests within the integration owner's release process.

## Authentication, events, and commands

Use the exact versioned OpenAccess guide for identity/authentication, TLS, operator permissions, token/session lifetime and event subscription. Do not copy ports, file paths or auth from old knowledge-base articles into a new design.

Separate cardholder/credential management, configuration reads, event monitoring, alarm acknowledgement and command/control. OnGuard APIs can expose doors, readers, panels, alarms, photos and credentials through authorized integrations. Apply least privilege, data minimization and immutable audit.

For event bridges, establish whether subscriptions are transient or durable, initial-state behavior, filters, gap recovery and backpressure. One official partner page says its integration supports transient hardware-event subscriptions only; that statement belongs to that integration, not every OpenAccess consumer.

For door/output commands, never blind-retry. Query authoritative state/journal and preserve local egress and life-safety authority.

## Primary sources

- [OnGuard product page](https://www.lenels2.com/en/security-products/onguard/) — current public platform/open-integration positioning.
- [OnGuard 8.3 data sheet](https://www.lenels2.com/en/media/OnGuard_8_3_Datasheet_10012024_tcm841-239894.pdf) — fixed release evidence for OpenAccess updates and platform security features.
- [OnGuard Cloud brochure](https://www.lenels2.com/en/media/OnGuard_Cloud_Brochure_040325_tcm841-230960.pdf) — single-tenant cloud and OpenAccess architecture evidence.
- [LenelS2 login and portal routes](https://www.lenels2.com/en/log-in/) — gated technical documentation/support boundary.
- [OAAP partner example with version/licence matrix](https://www.lenels2.com/en/security-solutions/third-party-integration/oaap-partners/resolver-command-center/) — certification and integration-specific licence evidence.
- [OpenAccess REST/event-bridge partner example](https://www.lenels2.com/en/security-solutions/third-party-integration/oaap-partners/qognify-qvms-sei-plugin/) — transient subscription evidence limited to that product.
- [Elements data sheet](https://www.lenels2.com/en/media/Elements_Datasheet_04182024_tcm841-203784.pdf) and [cloud-solutions page](https://www.lenels2.com/en/security-solutions/cloud-based-solutions/) — Elements/connector boundary.

## Related pages

- [Credential lifecycle](../../03-systems/access-control/credential-lifecycle.md)
- [Event normalization and schema evolution](../../05-development-and-integration/patterns/event-normalization-and-schema-evolution.md)
- [Change, firmware, and patching](../../07-operations-and-lifecycle/change-firmware-and-patching.md)
