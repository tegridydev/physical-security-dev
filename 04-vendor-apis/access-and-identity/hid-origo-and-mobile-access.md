---
title: HID Origo and Mobile Access APIs
summary: Publicly documented HID Origo identity, digital-credential, event, authentication, rate-limit, and Mobile Access lifecycle surfaces.
page_type: vendor-api
domains: [access-control, identity, integration]
tags: [hid, origo, mobile-access, digital-credentials, scim]
scope: global with organization, subscription, platform, and partner differences
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "RFC 6749: OAuth 2.0"
  - "RFC 7643 and RFC 7644: SCIM 2.0"
coverage_limit: Public HID Origo documentation reviewed on 2026-08-25; partner enrolment, subscriptions, part numbers, wallet/app eligibility, mobile SDK packages, organization environments, exact schemas, and tenant credentials require HID confirmation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# HID Origo and Mobile Access APIs

[Vendor APIs](../README.md) / [Access and identity](README.md) / HID

HID Origo is a cloud platform with several APIs, not a single “Mobile Access endpoint.” Current public documentation includes the Mobile Identities 2.2 family, newer User and Credential Management 3.x services, Events and Callbacks, and Identity Positioning. The **HID Mobile Access SDK** is a separate mobile-app component used to provision and use supported credentials; its package and platform contract are partner-controlled.

## Verified surface map

| Surface | Documented purpose | Important boundary |
|---|---|---|
| Mobile Identities API 2.2 | User, device/credential-container, invitation and Mobile ID lifecycle | Current public 2.x contract; callback registration moved to Events and Callbacks; some partner-environment functions differ |
| User Management API 3.x | SCIM-oriented user management for newer Origo services | Limited SCIM 2 support; public docs say these users currently work with Credential Management, not Mobile Identities 2.x |
| Credential Management API 3.x | Pass, pass-template, pass-design, credential-container and credential lifecycle | Platform support differs among Apple Wallet, Google Wallet, Identity Positioning and app-based Seos workflows |
| Events and Callbacks | Asynchronous state-change delivery | Delivery is not proof that a device has retrieved or applied an issue/revoke instruction |
| Mobile Access SDK | Embeds supported mobile-credential functionality in an application | SDK agreement, platform package, app identity and reader/credential compatibility required |
| Identity Positioning | Occupancy/utilization/proximity and site/floor/zone data | Separate privacy, lawful-basis, consent and subscription boundary |

The documentation is publicly readable, but states that its intended audience is developers enrolled in HID’s Technology Partner Program. Application identifiers and environment access are provided through HID Partner Services.

## Version and lifecycle evidence

The Mobile Identities page identified 2.2 and 2.1 as supported and 2.0 as deprecated with a retirement date in 2024. It also recorded 2.2 updates in April and July 2026. On 2026-08-25, the Credential Management page showed a 3.4.1 release line. These are separate API generations; do not upgrade by changing only a path or media type.

Credential Management 3.x describes a `Pass` abstraction and states which credential platforms are supported by each release. For example, public 3.4.x notes distinguish wallet, Identity Positioning and app-based Seos support and list known limitations. Treat every “future support” statement as non-available until a later released contract says otherwise.

## Authentication and authorization

The official authentication page states that Origo endpoints use OAuth 2.0 bearer access tokens issued for **System Accounts** created by an Organization Administrator. It documents password-based and certificate-based authentication, a one-hour token lifetime, application identifiers and data-security considerations.

For production machine integration:

- prefer the documented certificate-based system-account path where available;
- bind the system account and Application-ID to one integration and organization;
- store private keys/passwords in a managed secret or HSM-backed service;
- validate TLS and identity-provider hosts;
- cache access tokens only for their bounded lifetime and prevent renewal stampedes;
- rotate credentials before expiry and audit every administrator/system-account change;
- never put an issuance token, invitation code, access token, mobile credential identifier or user photo in general logs.

An OAuth token authenticates the integration; application and organization authorization still govern which users, templates, part numbers and credentials it may manage.

## Identity and credential state

Model API acceptance, credential issuance initiated, handset/app retrieval, credential active, revoke initiated, handset retrieval of revocation, and revoked as distinct states. A phone can be offline. Deleting a user or container can initiate downstream credential revocation, but the resulting physical-access risk depends on controller/reader synchronization and offline policy outside Origo.

Use immutable enterprise identifiers and do not join solely on mutable e-mail address. The 3.x User Management docs explicitly say its user objects are not currently interchangeable with Mobile Identities users. Build an adapter per API generation and document migration/dual-run semantics.

Events/callbacks must be authenticated using HID’s current contract, deduplicated, durably queued and correlated to the initiating request. Reconcile by reading authoritative API state after gaps or delivery failure. Never treat callback order as business order without a documented sequence contract.

## Documented limits as observed

The official Usage Limits page says limits can change and applies them by organization ID unless specified. On 2026-08-25 it listed:

| Service | Documented requests/window |
|---|---:|
| Mobile Identities API 2.2 | 300 per 5 minutes |
| Authentication service | 50 per 5 minutes |
| Events and Callbacks | 300 per 5 minutes |
| User Management API 3.x | 5,000 per 5 minutes |
| Credential Management API 3.x | 5,000 per 5 minutes |
| Identity Positioning API | 5,000 per 5 minutes |
| Identity Positioning authentication | 150 per 5 minutes |

The page documents HTTP 403 on limit exceed, rather than the more common 429. Treat that behavior as vendor-specific and re-check before coding. Centralize budgets across workers and preserve capacity for revocation and recovery.

Mobile Identities 2.2 documented a maximum search page size of 25 in July 2026. Credential Management 3.4.0.2 clarified zero-indexed pages and page sizes from 1 to 1,000 with a default of 20. Do not share a pagination helper across these APIs without per-service configuration.

## Safety and privacy

Credential issue/revoke is high impact. Require approval, target organization, credential template/part number, effective interval, reason and audit correlation. Protect photos, phone/device identifiers, wallet details, card numbers, occupancy and proximity as sensitive personal/security data. Define deletion, retention, data residency, subject-right and support-log handling before production.

## Primary sources

- [HID Origo API documentation](https://doc.origo.hidglobal.com/api/) — official API-family and partner-audience catalogue.
- [Authentication and authorization](https://doc.origo.hidglobal.com/api/authentication/) — OAuth, system-account and token contract.
- [Mobile Identities 2.2](https://doc.origo.hidglobal.com/api/mobile-identities/) — architecture, lifecycle, version and known limitations.
- [User Management](https://doc.origo.hidglobal.com/api/user-management/) — limited SCIM and cross-API user boundary.
- [Credential Management](https://doc.origo.hidglobal.com/api/credential-management/) — 3.x release, pass and platform scope.
- [Usage limits](https://doc.origo.hidglobal.com/api/usage-limits/) — mutable per-service quotas.
- [HID Mobile Access API 2.2 specification PDF](https://doc.origo.hidglobal.com/api/assets/pdf/ma-api-2.2.pdf) — fixed versioned contract.

## Related pages

- [Credential lifecycle](../../03-systems/access-control/credential-lifecycle.md)
- [Mobile access](../../03-systems/access-control/mobile-access.md)
- [Privacy and sensitive data](../../06-security-and-assurance/privacy-and-sensitive-data.md)
