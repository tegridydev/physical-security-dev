---
title: Eagle Eye Video API
summary: Publicly documented Eagle Eye Networks Video API v3 authentication, camera, media, event, webhook, SSE, pagination, and account boundaries.
page_type: vendor-api
domains: [video, integration]
tags: [eagle-eye-networks, video-api, oauth, webhooks, sse]
scope: global with account and service-region differences
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: Public Eagle Eye developer documentation reviewed on 2026-08-25; exact account entitlements, service hosts, rate limits, media codecs, retention, device support, and endpoint schemas require the live v3 reference and authorized tenant.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Eagle Eye Video API

[Vendor APIs](../README.md) / [VMS and cloud video](README.md) / Eagle Eye Networks

Eagle Eye Networks publishes a **Video API v3** for cloud video integrations. The current documentation covers OAuth-based authorization, camera/resources, live and recorded media, events and alerts, Server-Sent Events (SSE), webhooks, and list pagination. V3 identity is materially different from older V2 API-key patterns; new work should follow the current v3 contract.

## Verified scope and access

| Area | Publicly documented contract | Access boundary |
|---|---|---|
| Developer application | Client registration and credentials through the developer programme | Account/approval and secret custody required |
| User-delegated authorization | OAuth 2.0 Authorization Code flow and user consent | Application acts only within granted customer/user authority |
| Service integration | A vendor-enabled machine-to-machine option can issue a non-rotating refresh token after a user completes authorization | This is not OAuth client credentials; eligibility, authorization, token custody, revocation, and scope remain account-controlled |
| Camera/resources | Enumerate authorized cameras and related resources | Customer account, permissions and pagination apply |
| Media | Live and recorded viewing modes with documented media/session workflows | Codec, time range, entitlement, concurrency and token lifetime apply |
| Events | Query/event model plus SSE and webhook subscription approaches | Delivery/replay behavior must be designed from the selected guide |

## Authentication and authorization

Use V3 OAuth; do not copy a V2 key example into a V3 application. For user-facing integrations, use Authorization Code with state validation and the exact registered redirect URI. Keep the client secret and token exchange in a confidential backend, not browser JavaScript or a mobile package. Store access/refresh credentials in an approved secret store and never log them.

The documented machine-to-machine path is still established through user authorization and, when enabled by Eagle Eye, returns a non-rotating refresh token for the service. It is not the OAuth client-credentials grant. Treat that refresh token as a long-lived high-value secret, define explicit revocation/offboarding, and do not describe it as automatic workload identity.

The account supplies region/service routing information. Do not hard-code a host copied from another customer or geography. Bind authorization to the customer account and validate that returned resources remain within the expected tenant.

Use the narrowest scopes/permissions and separate media playback/export from administration or camera control. User consent is not a substitute for the application’s own role and purpose checks.

## Cameras, pagination, and reconciliation

The camera-list reference documents pagination. Follow response links/cursors and the endpoint’s declared limit semantics rather than inventing page arithmetic. Treat identifiers as opaque. Cache only with an expiry and re-enumerate after authorization, site or camera changes.

No stable public global request-rate number was verified for this page. Obtain current limits from the developer account/reference and implement `429` and transient-error backoff without hiding sustained quota or authorization failures.

## Events, SSE, and webhooks

Choose SSE for a managed long-lived client connection and webhooks when Eagle Eye should deliver to a controlled HTTPS receiver. For either:

- establish event types and filters from the current schema;
- persist event ID, source time, ingest time, camera/account and correlation;
- expect reconnect and duplicate delivery unless the contract explicitly says otherwise;
- detect gaps and reconcile using query APIs within the documented retention window;
- authenticate webhook origin using the vendor-documented mechanism;
- acknowledge only after durable acceptance;
- bound payload, retries, queue depth and processing time.

Never infer “person present” or “alarm handled” solely from event delivery.

## Media boundary

Use the documented live/recorded media workflow and session lifetime. Do not construct media URLs, share session tokens, disable TLS validation or make a private stream publicly cacheable. Bound requested time ranges, concurrent sessions and local buffers. Preserve original evidence through the platform’s supported export path; a decoded frame or browser recording is not equivalent.

## Lifecycle and compatibility

Monitor the developer portal for V3 changes and V2 retirement guidance. Record client type, consent/scopes, account/region, API documentation revision, media mode and event-delivery contract. Treat mutable limits and hosts as configuration discovered from the authorized environment.

## Primary sources

- [Video API v3 getting started](https://developer.eagleeyenetworks.com/docs/getting-started) — current API generation and onboarding.
- [Using the API](https://developer.eagleeyenetworks.com/reference/using-the-api) — authentication and application-access model.
- [Event subscriptions](https://developer.eagleeyenetworks.com/docs/event-subscriptions) — SSE and webhook approaches.
- [Events, alerts, and notifications](https://developer.eagleeyenetworks.com/docs/events-alerts-notifications-introduction) — event-domain entry point.
- [Watch live video](https://developer.eagleeyenetworks.com/docs/watch-live-video) — documented media workflows.
- [List cameras](https://developer.eagleeyenetworks.com/reference/listcameras) — resource and pagination reference.

## Related pages

- [WebSocket, SSE, and webhooks](../../02-protocols/web-and-messaging/websocket-sse-and-webhooks.md)
- [Media streaming fundamentals](../../01-foundations/media-streaming-fundamentals.md)
- [Polling, subscriptions, and reconciliation](../../05-development-and-integration/patterns/polling-subscriptions-and-state-reconciliation.md)
