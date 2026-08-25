---
title: Verkada Command APIs
summary: Publicly documented Verkada Command API key, short-lived token, region, permission, pagination, rate-limit, webhook, video, and access-control boundaries.
page_type: vendor-api
domains: [video, access-control, integration]
tags: [verkada, command, cloud-api, webhooks, access-api]
scope: global with service-region and product-subscription differences
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public Verkada API documentation and policy reviewed on 2026-08-25; product subscriptions, organization permissions, critical-endpoint approval, region hosts, adjusted quotas, feature availability, and endpoint schemas require the authorized tenant.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Verkada Command APIs

[Vendor APIs](../README.md) / [VMS and cloud video](README.md) / Verkada

Verkada publishes APIs across Command product families, including camera and access-control capabilities. The identity pattern starts with an organization-managed top-level API key with explicit product and critical-endpoint permissions, then uses short-lived API tokens for most calls. Service regions are a first-class boundary.

## Verified contract

| Area | Publicly documented behavior | Design consequence |
|---|---|---|
| Top-level API key | Organization administrator creates a key and assigns product/critical permissions | Store only in a confidential backend; review and rotate as a root integration secret |
| API token | Generated from the key; documented 30-minute lifetime and no refresh | Cache only briefly, renew safely, prevent stampede and never log |
| Service region | Credentials and service hosts are region-bound across documented commercial/government regions | Discover/configure the correct region; never fall back across regions |
| Pagination | Common pagination guidance plus endpoint-specific fields | Follow returned token/link contract, not guessed offsets |
| Rate limit | As observed 2026-08-25, 300 requests/minute globally per organization; vendor may adjust | Centralize quota across workers and treat the number as mutable configuration |
| Webhooks | Product-specific camera notification and access-event webhook models | Authenticate, deduplicate, queue durably and reconcile |

## Authentication and secret handling

Create one key per integration/purpose rather than sharing an administrator’s general key. Enable only the required product APIs and critical endpoints. A token inherits its key’s permission, so short lifetime reduces exposure time but does not compensate for overbroad authority.

- Keep the top-level key and token exchange server-side.
- Bind region and organization identifiers in configuration and audit.
- Validate TLS and reject redirects to unexpected hosts.
- Rotate keys with overlapping deployment only according to the documented lifecycle.
- Redact keys, tokens, media URLs, webhook secrets and sensitive IDs from traces.
- Treat a token-generation failure as an identity incident, not a reason to fall back to another organization key.

Some streaming interfaces can use different authentication. Follow the exact streaming reference; do not attach an ordinary API token to an undocumented URL.

## Limits and pagination

The public rate-limit page said 300 requests per minute globally per organization on the verification date and notes that Verkada can adjust limits. Coordinate all replicas against that shared budget, reserve capacity for recovery/critical workflows and add jitter. On `429`, honor the current documented retry guidance; the reviewed page advised waiting at least five seconds rather than immediate retries.

Use endpoint-specific pagination and persist a cursor only for its documented lifetime. Avoid unbounded organization-wide scans. For synchronization, checkpoint only after durable processing and periodically reconcile authoritative collections.

## Video, events, and access control

Treat live video, archives, thumbnails, analytics/notifications and access events as different data classes. Media session links and tokens are sensitive and should not enter analytics or general logs. Follow platform export/evidence procedures for evidentiary use.

Access APIs can expose identities, credentials, doors and commands depending on permission. Unlock and other critical operations require a separate high-impact policy: named requester, purpose, target, precondition, explicit confirmation, idempotency/uncertain-outcome handling, and immutable audit. Never use exploratory calls on production doors.

For webhooks, validate the vendor-documented authenticity mechanism, timestamp/freshness and schema. Deduplicate by stable delivery/event identifier, acknowledge after durable enqueue and reconcile when delivery fails. Do not assume webhook receipt proves physical passage or operator action.

## Region, policy, and lifecycle

The service-region reference identifies commercial regions including Australia and Europe and a GovCloud environment. Credentials are not portable between regions. Confirm product API support, organization placement, data residency, egress and legal terms for the selected region.

The API Use Policy governs permitted use independently of technical access. Monitor the API change log, limits, permissions and policy before each deployment. Date mutable claims in design records.

## Primary sources

- [Verkada API quick start](https://apidocs.verkada.com/reference/quick-start-guide) — key, permissions, token and HTTPS model.
- [Get API token](https://apidocs.verkada.com/reference/postloginapikeyviewv2) — 30-minute token/no-refresh contract.
- [Service regions](https://apidocs.verkada.com/reference/service-regions) — region and credential boundary.
- [Rate limiting](https://apidocs.verkada.com/reference/ratelimiting) — mutable organization quota and retry behavior.
- [Pagination](https://apidocs.verkada.com/reference/pagination) — common collection contract.
- [Access API overview](https://apidocs.verkada.com/reference/access-api-101) and [access-event webhooks](https://apidocs.verkada.com/reference/access-events-webhooks) — access-control boundary.
- [Camera notification webhook object](https://apidocs.verkada.com/reference/notification-webhook-object-1) — video notification evidence.
- [Verkada API Use Policy](https://docs.verkada.com/docs/API-Use-Policy.pdf) — use constraints.

## Related pages

- [Credentials and identity media](../../01-foundations/credentials-and-identity-media.md)
- [Retries, timeouts, and idempotency](../../05-development-and-integration/patterns/retries-timeouts-and-idempotency.md)
- [Privacy and sensitive data](../../06-security-and-assurance/privacy-and-sensitive-data.md)
