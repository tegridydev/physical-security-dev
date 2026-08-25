---
title: Brivo Access API
summary: Publicly documented Brivo Access API onboarding, OAuth, API-key, user, credential, site, door, event, and high-impact command boundaries.
page_type: vendor-api
domains: [access-control, identity, integration]
tags: [brivo, brivo-access, oauth, cloud-access, developer-portal]
scope: global with account, application, edition, and customer differences
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "RFC 6749: OAuth 2.0"
coverage_limit: Public Brivo Access documentation and programme material reviewed on 2026-08-25; customer editions, production approval, service-to-service flow, quotas, endpoint schemas, devices, credentials, and feature licences require the developer portal and authorized account.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Brivo Access API

[Vendor APIs](../README.md) / [Access and identity](README.md) / Brivo

Brivo now publishes separate Access and Video developer documentation. This page covers the **Brivo Access API**—sites, users, credentials, groups, doors, events and associated access-control operations—not the Brivo/Eagle Eye video API.

## Verified scope and access

| Element | Publicly documented model | Boundary |
|---|---|---|
| Documentation | Public Access API reference, auth guides and endpoint material | Documentation host is not the runtime API |
| Developer portal | Registers applications and requests production API keys | Portal approval and application/customer configuration required |
| Three-legged application | OAuth 2.0 Authorization Code plus Brivo application credentials/API key | Customer administrator/user authorizes access; exact redirect URI registered per app |
| Service integration | Alternative server-to-server flow available by contacting API support | Do not invent or repurpose a password flow; obtain the approved contract |
| Brivo Access edition | API integrations depend on commercial edition/add-on | Product sheet observed API integrations as an add-on in Standard and included in higher editions; re-check at purchase time |

The official documentation router generated 2026-08-05 says all documentation files are public and clearly separates Access from Video. Follow only the Access branch for access-control work.

## Authentication and application design

Brivo’s official Access integration guidance uses an API key plus OAuth client credentials and the Authorization Code flow for customer-delegated access. Protect all confidential material in a backend. Validate state, exact redirect URI and TLS; never expose client secret or API key in a browser bundle or mobile binary.

The official example-prompt page explicitly labels its local Vite/loopback patterns as development harnesses, not production architecture. It warns about localhost proxy relay, browser token theft, development-only HTTP redirects, missing server-side revocation and sensitive raw errors. A production application should use a hardened backend, secure HTTP-only sessions, per-request authorization and HTTPS redirects.

Create a distinct application/API key per integration and customer model as Brivo requires. Use a dedicated service administrator/role where the current programme guide permits, so audit and permissions are not tied to a person who may leave. Rotate secrets and revoke unused applications.

## Domain and state model

Keep these workflows independent:

- user/person creation and authoritative identity matching;
- physical and mobile credential issue, invitation, assignment and revoke;
- group/access assignment and schedule/effective-time policy;
- site, panel, reader and door inventory/status;
- access events and audit retrieval;
- unlock and emergency-scenario operations.

Cache lookup data only with revision/expiry. Use stable IDs rather than names for groups, formats, sites or doors. Validate bulk input completely before mutation and design compensation for a partial user/credential/group transaction.

An invitation or credential-created response does not prove mobile delivery or controller propagation. An unlock response does not prove lock state or passage. Preserve controller/door event evidence and reconcile.

## Pagination, limits, and events

Use the current Access reference’s endpoint-specific pagination and filters. A numeric global rate limit was not independently established from the reviewed public overview, so this page makes none. Implement bounded concurrency, `429`/transient backoff and customer-visible quota diagnostics, then record the quota supplied by Brivo for the application.

For events, store stable event ID, site/door, subject identifier, source and ingest time, and pagination/checkpoint state. Minimize names, e-mail, card values and other personal data. Reconcile gaps rather than treating a polling window as complete by assumption.

## High-impact safety boundary

Door unlock and emergency-scenario operations need independent explicit privileges, allowlisted targets, operator confirmation, reason, idempotency/uncertain-outcome behavior and immutable audit. Never expose them through a generic proxy or execute them as part of API exploration. Preserve fire/egress and local controller authority.

## Primary sources

- [Brivo API Documentation and Resources](https://apidocs.brivo.com/) — official Access/Video separation and portal routes.
- [Brivo documentation router](https://apidocs.brivo.com/llms.txt) — generated public documentation map and runtime-host warning.
- [Official Access development prompts and production warnings](https://apidocs.brivo.com/prompts/access.html) — auth/application requirements and explicit dev-harness limitations.
- [Brivo Technology Partner programme overview](https://resources.brivo.com/wp-content/uploads/securepdfs/2024/08/technology-partner-program-overview.pdf) — OAuth and API-key integration guidance; confirm current terms.
- [Brivo Access editions](https://resources.brivo.com/sales-sheets/brivo-access-editions-sale-sheet) — mutable API-integration commercial boundary.

## Related pages

- [Credential lifecycle](../../03-systems/access-control/credential-lifecycle.md)
- [Secrets, certificates, and configuration](../../05-development-and-integration/patterns/secrets-certificates-and-configuration.md)
- [API and event security](../../06-security-and-assurance/api-and-event-security.md)
