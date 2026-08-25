---
title: Hikvision ISAPI and HEOP
summary: Evidence-bounded map of Hikvision device HTTP integration through ISAPI and supported on-device applications through HEOP.
page_type: vendor-api
domains: [video, access-control, integration]
tags: [hikvision, isapi, heop, device-api, edge-applications]
scope: global with regional portal differences
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public Hikvision TPP and product material establishes ISAPI and HEOP; normative guides, packages, exact operations, versions, models, regions, licences, and compatibility are restricted or login-gated and are not reproduced.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Hikvision ISAPI and HEOP

[Vendor APIs](../README.md) / [Device and edge video](README.md) / Hikvision

**ISAPI** is Hikvision’s HTTP-based device integration protocol. **HEOP** is its embedded open-platform route for running supported third-party applications on eligible products. They solve different problems and their materials are controlled through the Hikvision Technology Partner Program (TPP).

## Verified surface map

| Surface | Verified public purpose | Evidence/access status |
|---|---|---|
| ISAPI | REST-style HTTP application-layer integration across Hikvision product families, including video and access-related products | TPP publicly describes the surface; the current developer guide is restricted and obtained after account approval/login |
| HEOP | Deploys supported third-party applications on compatible Hikvision hardware | Public landing page names HEOP 2.0; manager, SDK, guide, package and hardware qualification are TPP/account controlled |
| HikCentral OpenAPI | Platform-level integration for HikCentral products | Listed by TPP as a distinct integration surface |
| Device/network SDKs | Native SDK route for selected products and workflows | Distinct from ISAPI; package and compatibility must come from the partner portal |

Do not mix an ISAPI device integration, HikCentral OpenAPI integration, native SDK integration, and HEOP application in one generic “Hikvision API” assumption.

## Access status as of 2026-08-25

The TPP Getting Started Guide dated March 2025 identifies ISAPI, OTAP and HEOP developer material as restricted. Registration approval is described by the portal as normally taking one to three business days, but approval, contractual terms, export controls, region, programme level and access can vary. The official current package obtained through the approved account is the normative source.

The China open-platform site publishes additional method and security material. Treat it as regional official evidence, not as a replacement for the contracted global TPP guide or proof that the same product, firmware, operation or service is available elsewhere.

## Product and version record

Before implementation, obtain and retain:

- product family, model, hardware revision and firmware;
- region and distribution channel;
- ISAPI guide revision and feature/module chapter;
- device capability response required by that guide;
- HEOP generation, hardware eligibility, SDK/toolchain, package format and resource limits;
- HikCentral or SDK version if the integration is not direct-to-device;
- required feature licence and Technology Partner entitlement.

The label “HEOP 2.0” was present on the public TPP page on the verification date. This page does not claim that it is supported on a particular model or is the latest package delivered to every partner.

## Authentication and transport

Authentication modes, TLS behavior, certificate management, account roles and session rules must be taken from the exact current ISAPI/HEOP guide and target firmware. Public regional capability documentation demonstrates that supported network/security options vary. Therefore:

- require HTTPS where the target contract supports it and reject silent downgrade;
- validate device identity rather than accepting any self-signed certificate indefinitely;
- create a unique least-privileged integration user;
- disable anonymous or unused services;
- never embed device credentials in an HEOP package, mobile client, URL or log;
- rate-limit authentication failure and command retries;
- record the exact firmware behavior for password rotation and certificate replacement.

This page intentionally does not publish an authentication recipe or endpoint because the normative material is restricted and product-specific.

## Events, media, configuration, and commands

Treat each ISAPI module as an independent contract. Verify the documented capability and version before using event subscriptions, stream/profile configuration, searches, snapshots, PTZ, access-control objects, audio, alarm I/O, firmware, or user administration. Product families can reuse names without identical schemas or permissions.

For event ingestion, design for reconnect, duplicates, gaps, malformed XML/JSON, device reboot, clock correction and changed event types. For configuration or actuation, require explicit operator authorization and reconcile device state after timeout. An HTTP response cannot prove a door, relay, camera, recorder, alarm input or edge application reached the intended real-world state.

## HEOP application boundary

An HEOP application becomes part of the device trust boundary. Obtain the official guidance for signing, packaging, process isolation, privileges, supported APIs, storage, network access, update and uninstall. Pin the toolchain and hardware/firmware matrix. Bound CPU, memory, disk and log output, and provide rollback if an application affects video availability or device stability.

## Lifecycle and compatibility

Track TPP release notices, product firmware release notes, security advisories, application compatibility and restricted guide revisions. Do not preserve a partner SDK or guide outside its licence/contract terms.

## Primary sources

- [Hikvision TPP Integration Center](https://tpp.hikvision.com/tpp/IntegrationCenter) — official integration-surface catalogue.
- [About the Technology Partner Program](https://tpp.hikvision.com/tpp/AboutTPP/) — ISAPI public description.
- [TPP Getting Started Center](https://tpp.hikvision.com/tpp/GettingStartedCenter) and [Getting Started Guide](https://tpp.hikvision.com/pd/GettingStartedGuide.pdf) — registration and restricted-material status.
- [ISAPI and OTAP landing page](https://tpp.hikvision.com/download/ISAPI_OTAP) — official download route.
- [HEOP landing page](https://tpp.hikvision.com/tpp/HEOP) — HEOP 2.0 and manager access route.
- [Hikvision Open Platform](https://open.hikvision.com/osp) — official regional surface map; use only within its stated scope.

## Related pages

- [HTTP and REST](../../02-protocols/web-and-messaging/http-and-rest.md)
- [Threat boundaries](../../06-security-and-assurance/threat-modeling-and-trust-boundaries.md)
- [Firmware and supply chain](../../06-security-and-assurance/firmware-updates-and-supply-chain.md)
