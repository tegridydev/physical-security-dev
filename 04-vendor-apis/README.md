---
title: Vendor APIs and SDKs
summary: Decision-oriented catalogue of supported vendor integration surfaces for physical-security devices, VMS and cloud video, access control, identity, and intercom.
page_type: index
domains: [integration, cross-domain]
tags: [vendor-apis, sdk, integration, catalogue]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: Public official documentation and clearly identified partner or licensed surfaces as reviewed on 2026-08-25; this is not a compatibility, certification, entitlement, or current-version guarantee.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Vendor APIs and SDKs

[Home](../README.md) / Vendor APIs and SDKs

This catalogue answers the first integration question: **which vendor-owned surface is authoritative for the product and job in front of you?** It separates public APIs from login-gated references, partner SDKs, licensed server interfaces, on-device application frameworks, and open-standard interfaces. It does not turn a marketing claim such as “open API” into an endpoint, entitlement, or compatibility claim.

## Start here

- [Selection and capability matrix](selection-and-capability-matrix.md) — compare deployment, access tier, capabilities, and evidence quality.
- [Device and edge video](device-and-edge-video/README.md) — camera, intercom, edge-application, device-management, and native SDK surfaces.
- [VMS and cloud video](vms-and-cloud-video/README.md) — server, client, plug-in, media, cloud, and event integrations.
- [Access and identity](access-and-identity/README.md) — PACS, mobile credentials, cloud access, identity lifecycle, door, and biometric surfaces.

## How to use a vendor page

1. Match the exact product family, deployment model, and integration direction.
2. Confirm whether the normative material is public, account-gated, partner-only, licensed, or delivered with an installed product.
3. Pin product, firmware/server, API/SDK, operating-system/runtime, region, tenant, and licence assumptions.
4. Obtain the current vendor compatibility and lifecycle statement before designing against a surface.
5. Separate read, event, configuration, credential, media, and physical-command privileges.
6. Build recovery for duplicate, delayed, missing, reordered, and partially applied operations.
7. Validate integrations in an owner-approved non-production environment before any live deployment.

## Evidence grades in this section

| Grade | Meaning here |
|---|---|
| `V2` | Multiple official sources were cross-checked, including a reference plus release, lifecycle, product, or access source where available. |
| `V1` | An official public landing page or product artefact establishes the surface, but the normative guide, package, entitlement, compatibility matrix, or current details are gated or incomplete. |
| `V0` | Reserved for an unverified inventory claim; no maintained vendor page in this release relies on guessed technical details. |

The grade describes source quality, not vendor certification or deployment compatibility. Environment evidence must identify the exact account, entitlement, product build, configuration, and controlled test scope. See [verification and safety](../00-start-here/verification-and-safety.md) and the [verification policy](../10-sources-and-maintenance/verification-policy.md).

## Integration boundaries

- A vendor API is not automatically enabled on every model or edition.
- A public reference does not grant a tenant, licence, developer account, export right, media entitlement, or command privilege.
- An SDK package version and the product it targets can have independent release lifecycles.
- Cloud regions, sovereign environments, and government editions can use different identities, hosts, features, and data-residency terms.
- ONVIF, SIP, BACnet, OSDP, and other standards-based support must be confirmed through the exact product declaration or conformance record; it is distinct from a vendor-native API.
- “Unlock”, “override”, “arm/disarm”, “output”, “firmware”, “credential”, “biometric”, “audio”, and evidence-export operations are high-impact even when the transport is ordinary HTTPS.

## Shared engineering guidance

Use these pages with:

- [Physical-security system architecture](../01-foundations/physical-security-system-architecture.md)
- [Identity, authentication, and authorization](../01-foundations/identity-authentication-and-authorization.md)
- [Events, state, commands, and time](../01-foundations/events-state-commands-and-time.md)
- [Interoperability, conformance, and profiles](../01-foundations/interoperability-conformance-and-profiles.md)
- [Development and integration patterns](../05-development-and-integration/README.md)
- [API and event security](../06-security-and-assurance/api-and-event-security.md)
- [Privacy and sensitive data](../06-security-and-assurance/privacy-and-sensitive-data.md)
- [Asset and configuration inventory](../07-operations-and-lifecycle/asset-and-configuration-inventory.md)

## Maintenance rule

Vendor claims in this section expire quickly. Re-check public-versus-gated access, release status, identity flow, licences, regions, limits, deprecations, and compatibility at least every 90 days and before procurement or implementation. A dated version on a page is an observed documentation fact, not a claim that the version remains latest.
