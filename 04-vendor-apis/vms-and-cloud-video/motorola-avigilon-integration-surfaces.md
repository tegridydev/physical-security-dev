---
title: Motorola Solutions and Avigilon Integration Surfaces
summary: Product-separated catalogue of Avigilon Unity, Avigilon Alta, and Motorola Solutions developer and interoperability routes using public official evidence.
page_type: vendor-api
domains: [video, access-control, integration]
tags: [motorola-solutions, avigilon, unity, alta, developer-program]
scope: global with product, region, programme, and licence differences
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public Motorola Solutions and Avigilon programme, product, release, and help material; detailed SDK/API contracts, endpoints, credentials, licences, compatibility, and partner entitlements are fragmented or gated and are not inferred.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Motorola Solutions and Avigilon integration surfaces

[Vendor APIs](../README.md) / [VMS and cloud video](README.md) / Motorola Solutions and Avigilon

The current portfolio spans multiple independently versioned platforms. **Unity Video**, **Unity Access**, **Alta Video**, **Alta Access**, and other Motorola Solutions command-center products do not share one universal “Avigilon API.” The official developer-program page and Avigilon documentation portal are the correct starting points, but much of the detailed developer contract is programme-, product- or licence-controlled.

## Verified product separation

| Product family | Publicly evidenced integration route | Evidence limit |
|---|---|---|
| Avigilon Unity Video | Web Endpoint API and interoperability/developer programme references | Detailed current API/SDK contract and licences were not verified publicly as one catalogue |
| Avigilon Unity Access | Product-specific REST/integration and licensed partner surfaces | Public product/release docs exist; older official integration blueprints prove a REST API licence for that exact workflow only |
| Avigilon Alta Video | Cloud video integrations documented in the Avigilon help portal | Tenant/region API contract and developer entitlement must be obtained for the intended integration |
| Avigilon Alta Access | Cloud access, identity and app integrations; formerly Openpath | Public administration/integration guides exist; a general current public developer API reference was not established in this review |
| Motorola Solutions developer programmes | Avigilon and command-center developer/interoperability routes | Programme acceptance, agreements, documentation and support are distinct by product |

## Current documentation observations

The Avigilon portal contained Unity Video 8.8 documentation and Unity Access 7.20 release material during the 2026-08-25 review. These observations do not establish that either is universally latest, licensed, or compatible with a given integration. The portal also retains older product documentation; always select the exact version label.

Alta Access documentation reflects the Openpath-to-Avigilon product transition. Record both legacy and current names only for traceability; use current product identifiers in new contracts. Alta cloud sign-in and feature availability can be region- and subscription-specific.

## Required evidence before design

Obtain a vendor/partner statement that identifies:

- exact Unity/Alta/Motorola product and edition;
- server/cloud release, region and tenant type;
- API/SDK/package name and version;
- development, test and production licence/entitlement;
- supported operations and event/media semantics;
- identity, token/certificate and permission model;
- rate, pagination, session and retention limits;
- compatibility, deprecation, support and security-advisory route.

Do not use a PDF for a named third-party integration as proof of a general-purpose endpoint. For example, an official 2023 integration blueprint referenced a Unity Access REST API licence and minimum product version for that blueprint; it does not authorize or define other workflows.

## Security and physical-safety boundary

Unity and Alta surfaces can span live/recorded video, evidence, alarms, identities, credentials, doors and physical commands. Create separate principals and authorization policies for each capability. Cloud credentials must be bound to the correct organization/region; on-premises credentials must remain inside the management conduit.

For Alta identity-provider integrations, current official guides document subscription-dependent sync intervals and read permissions for named providers. Those application-specific settings are not a general Alta developer authentication contract. Pin the exact integration guide and permissions.

Never retry door, lockdown, alarm acknowledgement, relay, PTZ or other command blindly after timeout. Query product state and audit records or require operator reconciliation. Preserve local life-safety authority and egress behavior independently of cloud/API availability.

## Events and media

Before relying on an event integration, establish subscription durability, resume cursor, ordering, duplicate/gap behavior, initial snapshot and retention. Before using media, establish live/playback/export distinctions, session lifetime, codec, authorization, watermark/integrity and redistribution rights. Product UI deep links are not media APIs or evidence exports.

## Lifecycle and product identity

`technology_status: mixed` reflects multiple current cloud/on-premises product lines, retained older documentation, renaming and separately versioned interfaces. Re-check branding, product ownership, support and replacement paths at every review.

## Primary sources

- [Motorola Solutions developer programmes](https://www.motorolasolutions.com/en_us/developers.html) — official programme entry point, including Avigilon.
- [Motorola Solutions interoperability programmes](https://www.motorolasolutions.com/en_us/products/command-center-software/public-safety-software/public-safety-software-integration/interoperability.html) — official partner/resource route.
- [Avigilon documentation portal](https://docs.avigilon.com/) — current versioned product documentation.
- [Unity Video 8.8 support and Web Endpoint API links](https://docs.avigilon.com/bundle/unity-video-occupancy-counting-8-8/page/more-info-and-support.htm) — product-specific evidence.
- [Unity Access 7.20 documentation results](https://docs.avigilon.com/search?labelkey=unity_access_version_unityaccess7.20) — versioned release/product evidence.
- [Alta Access Microsoft Entra integration](https://docs.avigilon.com/bundle/alta-access-integration-entra-id/page/integrations/microsoft-entra/microsoft-azure-ad-oauth-service-principal.htm) — example of product-, subscription- and permission-specific integration documentation.

## Related pages

- [Selection matrix](../selection-and-capability-matrix.md)
- [PACS architecture](../../03-systems/access-control/pacs-architecture.md)
- [Vulnerability management and disclosure](../../06-security-and-assurance/vulnerability-management-and-disclosure.md)
