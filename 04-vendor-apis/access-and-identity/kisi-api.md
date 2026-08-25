---
title: Kisi API and Mobile SDKs
summary: Publicly documented Kisi JSON API, API-key, rate-limit, deprecation, webhook, user-attribution, and mobile SDK integration boundaries.
page_type: vendor-api
domains: [access-control, identity, integration]
tags: [kisi, cloud-access, api-key, webhooks, mobile-sdk]
scope: global with organization, plan, sandbox, SDK, and hardware differences
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public Kisi product and OpenAPI documentation reviewed on 2026-08-25; organization plans, sandbox/production approval, mobile SDK partner ID, exact hardware/firmware, endpoint schemas, custom quotas, and marketplace terms require Kisi confirmation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Kisi API and mobile SDKs

[Vendor APIs](../README.md) / [Access and identity](README.md) / Kisi

Kisi publishes a JSON/HTTPS API for organizations, users, locks, access rights, events and unlock workflows, plus webhooks and mobile SDKs for embedded access. The REST API can support user provisioning and cloud unlocks; the iOS/Android SDKs add supported proximity/tap behavior and require separate partner access and hardware.

## Verified surface map

| Surface | Publicly documented purpose | Access boundary |
|---|---|---|
| Kisi API | Organization, user, place, lock, access, event and command resources | Public OpenAPI reference; organization account/API key and permissions required |
| Webhooks | Real-time event delivery to an integration | Receiver authenticity, retry and reconciliation must follow current guide |
| Mobile SDK for iOS/Android | Embeds Tap to Unlock, in-app unlock and MotionSense workflows | Partner ID/SDK access, provisioned users and compatible controller/reader required |
| Marketplace application | Admin-configured integration inside Kisi dashboard | Partner approval and marketplace quality/security requirements |
| Sandbox and hardware dev kit | Authorized development environment | Requested through integration-partner onboarding; not production entitlement |

## Authentication and key lifecycle

Most API calls use a Kisi API key/login secret in the documented authorization scheme over HTTPS. Organization owners or administrators can create keys. The current guide recommends a separate API key for each integration instance and says:

- a user can hold up to 40 API keys, after which older keys expire;
- keys expire after six months of inactivity by default unless created under the documented non-expiring option;
- organization-owner creation can avoid an administrator departure invalidating the integration.

A non-expiring secret increases risk; prefer bounded lifecycle and rotation unless an approved operational requirement says otherwise. Keep keys in a backend secret store, never in browser/mobile source, and include the integration-identification/contact headers required of partners. Revoke on decommission or compromise.

## User attribution and identity

An administrator key used directly for every unlock can attribute events to the administrator rather than the actual person. Kisi documents user provisioning and user-specific login/secret patterns for applications that require individual audit. Apply them only through the current guide and protect every user secret like a credential.

Use stable user identifiers and explicit organization/place scope. Define joiner/mover/leaver behavior, group/access changes, schedule timezone and credential revocation. Do not create “managed” users or non-expiring device logins without retention and deletion policy.

## Limits, versioning, and deprecation

As documented on 2026-08-25, authenticated requests are limited to **5 requests per second per user** and unauthenticated requests to **5 per second per IP**, with lower custom limits on selected endpoints. Limits are mutable. Serialize/bound work per user, add exponential backoff for HTTP 429 and read each endpoint’s custom rule.

Kisi says the API is not path/versioned and aims for backward-compatible change. The OpenAPI document’s `1.0.0` label is a specification-document version, not evidence of a `/v1` lifecycle. When incompatibility is necessary, Kisi documents `Deprecation` and `Sunset` response headers. Capture and alert on both headers and subscribe to the developer newsletter.

Use endpoint-specific pagination/filter fields from the OpenAPI schema. Do not assume all collections fit a response or share one cursor/offset model.

## Webhooks and events

Authenticate webhook delivery using the current Kisi mechanism, validate freshness, deduplicate, enqueue durably before acknowledgement and reconcile after gaps. Preserve event ID, source time, ingest time, organization/place/lock and attributed user while minimizing names and credential material.

An unlock event, lock output state, door-contact state and confirmed passage are different facts. The API cannot replace supervised door hardware or local life-safety logic.

## Mobile SDK boundary

Kisi documents Tap to Unlock using BLE on iOS or NFC on Android, in-app cloud unlock, and MotionSense for supported hardware. The SDK handles proximity proof/reader interaction; the host app remains responsible for user lifecycle, UI, secure credential storage, authorization and privacy.

Request a partner ID and follow the supplied testing protocol. Pin SDK, mobile OS, controller/reader, firmware and network/offline behavior. Never reverse-engineer proximity advertisements or extract user secrets from the SDK.

## High-impact safety boundary

Door/elevator lockdown and unlock are high impact. Allowlist targets, require explicit application authorization, record requester/reason, and handle timeout as uncertain. Do not expose a generic “call any Kisi endpoint” proxy.

## Primary sources

- [Kisi API overview](https://docs.kisi.io/platform/apis/) — capability, rate-limit and versioning policy.
- [Kisi OpenAPI reference](https://api.kisi.io/docs) — public operation, error, custom-limit and deprecation contract.
- [How to integrate Kisi](https://docs.kisi.io/platform/integrate_kisi/) and [getting started](https://docs.kisi.io/platform/integrate_kisi/getting_started/) — sandbox, keys, hardware and SDK access.
- [Generate an API key](https://docs.kisi.io/dashboard/account/generate_api_key/) — administrator, key-count and inactivity lifecycle.
- [Integration methods](https://docs.kisi.io/platform/integrate_kisi/integration_methods/) — user provisioning, user-attributed unlock, SDK and marketplace boundaries.
- [Mobile SDK integration process](https://docs.kisi.io/platform/sdks/integration_process/) — platform/hardware and partner-ID requirements.

## Related pages

- [Locks, egress, and life safety](../../03-systems/access-control/locks-egress-and-life-safety.md)
- [Mobile access](../../03-systems/access-control/mobile-access.md)
- [Certificate and account lifecycle](../../07-operations-and-lifecycle/certificate-and-account-lifecycle.md)
