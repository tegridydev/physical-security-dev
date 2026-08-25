---
title: Suprema BioStar 2 API
summary: Publicly documented BioStar 2 New Local API, session authentication, version, pagination, biometric, event, device, and separate SDK/TA boundaries.
page_type: vendor-api
domains: [access-control, identity, integration]
tags: [suprema, biostar-2, local-api, biometrics, device-sdk]
scope: global with server, version, licence, device, and firmware differences
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public Suprema API collection and support documentation reviewed on 2026-08-25; exact BioStar build, licence, device/firmware compatibility, session settings, rate limits, endpoint schemas, old Local API, Device SDK, and TA API behavior require the target installation contract.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Suprema BioStar 2 API

[Vendor APIs](../README.md) / [Access and identity](README.md) / Suprema

The current **BioStar 2 New Local API** is a JSON/HTTPS service integrated into BioStar 2. It is distinct from the older separately installed Local API server, the native **BioStar 2 Device SDK**, and the separate Time and Attendance (TA) API. Choose the authority plane deliberately: the BioStar server API manages platform state; the Device SDK talks at a lower device-integration layer.

## Verified surface map

| Surface | Publicly documented purpose | Version/access boundary |
|---|---|---|
| BioStar 2 New Local API | Users, access groups/levels, credentials, devices, doors, elevators, schedules, events, audits, zones and administration | Integrated from BioStar 2.7.10 onward; exact features evolve by server version |
| Offline/local Swagger | Reads bundled New Local API description without a running server connection | Available from BioStar 2.8.14 according to support page; does not execute or prove behavior |
| Old Local API server | Earlier separately installed API server | Separate version/licence compatibility; do not mix paths or auth with New Local API |
| BioStar 2 Device SDK | Direct supported device integration | Native SDK package, device/firmware matrix and language/runtime contract apply |
| BioStar 2 TA API | Time-and-attendance service and Swagger | Added with BioStar 2.8.13; separate service/port/schema from access-control API |

## Version and lifecycle evidence

The public API collection showed **v2.9.12 revisions dated 2026-03-11** and earlier per-release change notes during the 2026-08-25 review. This proves documentation changes tied to that BioStar line; it does not mean every installation runs 2.9.12 or that all documented operations work on older builds/devices.

The collection flags a compatibility change from BioStar 2.9.9: trailing slashes are no longer accepted for API URLs. This illustrates why integrations must pin and review seemingly small parsing changes. Maintain a per-release contract and do not normalize URLs in a way that defeats documented behavior.

## Authentication and transport

The official overview requires HTTPS. The login operation returns a `bs-session-id` used for later authorization. Use a dedicated least-privileged BioStar operator, protect its password and session in memory/secret storage, and never log either. Validate the BioStar server certificate under the site PKI instead of accepting a permanent exception.

Session expiry, concurrency, revocation and failover behavior must be verified on the target version. Re-authenticate safely without replaying a high-impact mutation. If a server/UI account uses broad biometric or door privileges, do not reuse it as the API service identity.

## Pagination and data contract

The public collection shows more than one collection pattern: some operations use `offset`/`limit`, some use page/limit, and search bodies carry their own conditions/order/total fields. Build endpoint-specific pagination adapters. Do not assume page origin or a universal maximum.

Treat identifiers, counts, dates, device fields, event data and binary/photo/biometric content as untrusted. Validate bounds before allocation. Record server/API build and device firmware with every compatibility workaround.

A public global request-rate limit was not verified. Bound concurrency conservatively, handle throttling/service-unavailable responses and obtain site/vendor limits before bulk enrollment or event backfill.

## Events, devices, and biometrics

The API includes event search and device-log workflows. Distinguish device-resident logs from server-stored events; deletion or synchronization has different evidence impact. Preserve immutable exported evidence before any retention/destructive operation and authorize those operations separately.

User records can contain cards, faces, fingerprints, photos and other sensitive attributes depending on configuration. Minimize collection, encrypt storage/transit, restrict export, define retention/deletion and avoid logging templates/images. Check lawful basis and jurisdiction before biometric processing.

Device, door, quick-action, alarm-clear, firmware and user-export/delete operations are high impact. Never test wildcards or bulk operations on production. Reconcile server and device state after timeout; a server response does not prove all devices synchronized.

## Primary sources

- [BioStar 2 API collection](https://bs2api.biostar2.com/) — official current API overview, revisions, auth and operation catalogue.
- [Using the BioStar 2 New Local API](https://support.supremainc.com/en/support/solutions/articles/24000047041--biostar-2-api-how-to-use-and-start-biostar-2-new-local-api) — integrated-server and session model.
- [BioStar 2 API login](https://support.supremainc.com/en/support/solutions/articles/24000072553--biostar-2-api-how-to-login-) — session authorization guidance.
- [Offline Swagger support](https://support.supremainc.com/en/support/solutions/articles/24000073868--biostar-2-api-how-to-use-local-swagger-new-local-api-) — version and non-runtime documentation boundary.
- [BioStar 2 TA API introduction](https://support.supremainc.com/en/support/solutions/articles/24000073529) — separate TA surface.
- [SDK and API starter guide](https://support.supremainc.com/en/support/solutions/articles/24000005839--biostar-2-sdk-sdk-and-api-starter-s-guide) — old API and Device SDK distinction; verify current packages.

## Related pages

- [Biometrics](../../03-systems/access-control/biometrics.md)
- [Secure protocol parsing](../../06-security-and-assurance/secure-protocol-parsing.md)
- [Incident response and evidence](../../07-operations-and-lifecycle/incident-response-and-evidence.md)
