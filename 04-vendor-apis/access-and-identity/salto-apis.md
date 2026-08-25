---
title: SALTO APIs
summary: Publicly documented SALTO KS, Nebula, and Space API surfaces with authentication, events, pagination, licence, rate-limit, platform, and SHIP boundaries.
page_type: vendor-api
domains: [access-control, identity, integration]
tags: [salto, salto-ks, nebula-api, space, ship]
scope: global with platform, region, licence, hardware, and partner differences
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [OpenID Connect 1.0]
coverage_limit: Public SALTO developer and support documentation reviewed on 2026-08-25; client credentials, production tenant, exact locks/firmware, platform editions, mobile/wallet eligibility, SHIP specification, and partner/licence entitlements require SALTO confirmation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# SALTO APIs

[Vendor APIs](../README.md) / [Access and identity](README.md) / SALTO

SALTO operates multiple integration platforms. **SALTO KS Connect API**, **KS Core API**, **SALTO Nebula API**, **SALTO Space Hospitality API**, and the licensed **SALTO Host Interface Protocol (SHIP)** are different contracts. Select by deployed platform and workflow; similar concepts such as users, locks and access groups do not imply schema or identifier compatibility.

## Verified surface map

| Surface | Deployment/transport | Publicly documented purpose | Access boundary |
|---|---|---|---|
| KS Connect API | SALTO KS cloud; REST/JSON | Third-party management of KS installations; broad parity with KS front-end operations | Client ID/secret from local SALTO business unit; site/user consent and permissions apply |
| KS Core API | KS cloud; OpenAPI REST | Core access objects under a separate versioned reference | Use only when SALTO provisions this surface; do not substitute for Connect API |
| Nebula API | SALTO cloud platform; HTTP/2 RPC with Protocol Buffers | Access-point, identity/access and event operations for supported Nebula-based products | Product/tenant/client entitlement and exact proto/API revision apply |
| Space Hospitality API | On-premises Space plus WalletHub cloud | Apple Wallet hotel guest key lifecycle | Space 6.10+ baseline, later versions for named features/limits, licences and compatible hardware documented |
| SHIP | Space on-premises proprietary protocol | Connects Space to security, BMS, CCTV and time/attendance systems | Licence-dependent; NDA required; specification supplied by SALTO/partner |

## KS authentication and integration types

The KS documentation says its identity provider implements OpenID Connect on OAuth 2.0 and documents interactive web/mobile and non-interactive backend integration types. Client ID and, where applicable, client secret are provisioned for the registered application and redirect/environment.

Follow the exact SALTO-supported flow for the client type. Keep confidential credentials in a backend or secure workload store, validate redirect state and issuer/audience, and protect refresh tokens. The public KS page describes a password-based backend flow; do not collect or retain a user password unless the currently approved SALTO integration contract explicitly requires that legacy-style flow. Ask SALTO whether a stronger workload flow is available for new production designs.

Authorization is site/user/role specific. Enumerate effective permissions instead of assuming a token can manage every site. Separate read/event access, user/access-group administration, lock configuration and unlock/control.

## Events, pagination, and schema

KS publishes an event-streaming guide. Establish connection renewal, filter, checkpoint/replay, duplicate/gap and authorization-change behavior from that guide before treating it as a durable feed. Maintain an authoritative reconciliation poll for identities, access groups and lock state.

The Connect API is described by an OpenAPI reference whose paths can carry different versions; its aggregate reference is labelled `v-latest`. Pin the version of every operation/schema used, rather than recording only “latest.” The Core API public reference was labelled v1.2 during review.

Nebula’s documentation explicitly covers pagination, filtering and event types. Its Protocol Buffer interface is the schema authority even when documentation renders responses as JSON for readability. Generate clients only from the vendor-supplied supported definitions and reject unknown oversized fields safely.

## Space Hospitality boundary

The public Space Hospitality guide documents a narrow workflow: Apple Wallet guest room keys. It explicitly excludes physical/staff keys from that API. As reviewed, prerequisites included Space 6.10 or later, 6.12+ for full named feature support, 6.14+ for increased rate-limit capacity, specific Space licences, compatible NFC hardware/firmware, an Ethernet NCoder, TLS and WalletHub credentials. Re-check every value with the live guide.

The documented capacity was 20 concurrent requests plus 10 queued; excess requests receive HTTP 429. This is a concurrency contract, not a per-minute quota. Implement bounded retry and make check-in/check-out/key invalidation idempotent or reconcilable. An API response does not prove a wallet provisioned or a lock received updated authorization.

## SHIP boundary

SHIP is proprietary, licensed and NDA-gated. Do not implement it from captured traffic or third-party summaries. Obtain the current specification, Space version support and licence. Segment its TCP service, restrict peer IPs, use the strongest supported transport/security options and do not expose it to the Internet. Treat SHIP control of access/BMS objects as high impact.

## Safety and lifecycle

For all SALTO platforms, record tenant/site, lock and firmware compatibility, online/offline behavior, credential propagation, time schedules, gateway state and audit provenance. Never blind-retry lock/unlock or key operations. Query access-point and credential state, and preserve local egress/life-safety authority.

## Primary sources

- [SALTO KS developer portal](https://developer.saltosystems.com/ks/) — official API-family catalogue.
- [KS Connect API](https://developer.saltosystems.com/ks/connect-api/) and [authentication](https://developer.saltosystems.com/ks/connect-api/authentication/) — purpose, client credentials and OIDC model.
- [KS integration types](https://developer.saltosystems.com/ks/connect-api/integration-types/) — registered client-flow distinctions.
- [KS API reference](https://developer.saltosystems.com/ks/connect-api/reference/) and [event guides](https://developer.saltosystems.com/ks/guides/) — versioned operations and streaming.
- [KS Core API reference](https://developer.saltosystems.com/ks/core-api/reference/) — separate core surface.
- [SALTO Nebula API](https://developer.saltosystems.com/nebula/api/) — HTTP/2/Protocol Buffer contract and reference structure.
- [Space Hospitality API](https://developer.saltosystems.com/space/hospitality-api/) — exact wallet, licence, hardware and capacity scope.
- [Space SHIP configuration](https://support.saltosystems.com/space/user-guide/operator/general-options/ship/) — proprietary, licensed and NDA boundary.

## Related pages

- [Mobile access](../../03-systems/access-control/mobile-access.md)
- [Credential formats and mobile credentials](../../02-protocols/access-control/credential-formats-and-mobile-credentials.md)
- [Retries, timeouts, and idempotency](../../05-development-and-integration/patterns/retries-timeouts-and-idempotency.md)
