---
title: Start Here
summary: Orientation and safe-use guide for Physical Security Dev Notes.
page_type: index
domains: [cross-domain]
tags: [navigation, onboarding, safety]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: Navigation and usage policy only.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Start here

Physical-security integrations cross disciplines that use the same words differently. A camera, door controller, BMS gateway, message broker, and cloud API may all expose an “event,” yet differ on delivery, ordering, acknowledgement, retention, identity, and time. These pages establish the shared vocabulary and evidence rules needed before protocol detail.

## Reading order

1. [How to use this knowledge base](how-to-use-this-knowledge-base.md)
2. [Scope and boundaries](scope-and-boundaries.md)
3. [Verification and safety](verification-and-safety.md)
4. [Glossary and conventions](glossary-and-conventions.md)
5. Choose a route in [learning paths](learning-paths.md)
6. Read the [protocol landscape](../physical-security-protocol-landscape.md), then the relevant foundation and protocol pages

## What this library optimizes for

- **Correct classification:** electrical interface, data link, transport, media format, application protocol, profile, API, and product are kept distinct.
- **Integration decisions:** pages call out actors, trust boundaries, state models, failure semantics, version scope, and migration concerns.
- **Defensible claims:** facts that can change are dated and sourced close to the claim.
- **Safe failure:** advice accounts for physical effects, degraded modes, and independent life-safety functions.
- **Maintainability:** one canonical page per topic, controlled metadata, relative links, explicit gaps, and scheduled review.

## Useful shortcuts

| Need | Go to |
|---|---|
| Understand where a protocol sits | [Architecture and layering](../01-foundations/architecture-and-layering.md) |
| Design an event integration | [Events, state, commands, and time](../01-foundations/events-state-commands-and-time.md) |
| Reason about authentication | [Identity, authentication, and authorization](../01-foundations/identity-authentication-and-authorization.md) |
| Understand certificates | [TLS, PKI, and certificates](../01-foundations/tls-pki-and-certificates.md) |
| Review physical interfaces | [Serial and field interfaces](../01-foundations/serial-and-field-interfaces.md) |
| Check evidence quality | [Source policy](../10-sources-and-maintenance/source-policy.md) |
| Add a page consistently | [Templates](../10-sources-and-maintenance/templates/README.md) |

Return to the [root index](../README.md).
