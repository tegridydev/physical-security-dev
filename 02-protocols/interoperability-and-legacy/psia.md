---
title: PSIA specification family
summary: Status, layering, shared models, security baseline, conformance language, and integration guidance for PSIA specifications.
page_type: protocol
domains: [cross-domain, video, identity]
tags: [psia, service-model, cmem, csec, area-control, interoperability]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [PSIA Service Model v3.0, PSIA CSEC v2.0 R1, PSIA CMEM v3.1 Rev 0.4, PSIA Area Control including PLAI v3.1]
coverage_limit: PSIA publishes specifications rather than accredited standards; exact downloadable documents, schemas, product declarations, and errata are required for implementation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# PSIA specification family

[Home](../../README.md) / [Protocols](../README.md) / [Interoperability and legacy](README.md) / PSIA

The Physical Security Interoperability Alliance (PSIA) publishes complementary system and domain specifications for exchanging security data. PSIA itself distinguishes its specifications from standards formally accredited by ANSI, IEC, ISO, or similar bodies.[^faq] Use “implements PSIA specification/version/profile” rather than an unsupported generic “PSIA standard compliant” claim.

## Family and status

| Layer/specification | PSIA-listed edition | Role/status |
|---|---|---|
| Common Security Model (CSEC) | v2.0 R1, posted 2015-04-18 | Network/session security, key/certificate and permission model shared by PSIA nodes |
| Service Model | v3.0 | Shared service framework/reference work |
| Common Metadata & Event Model (CMEM) | v3.1 Rev 0.4, posted 2016-05-12 | Shared metadata and event vocabulary/reference work |
| Area Control including PLAI | v3.1, released 2019-08-07 | Access/intrusion integration and PLAI profile |
| IP Media Device | 1.1 package / older 1.0 registrations | Legacy, no active development |
| Recording and Content Management | 1.1a (r0.6b) | Legacy video recording/search/content integration |
| Video Analytics | v1.0 | Legacy analytics discovery and output |

The editions and legacy labels above are taken from PSIA's current overview, FAQ, and legacy download page.[^overview][^legacy] PSIA says present organizational focus is access control and credential management, through PLAI and secure-credential work.[^org]

## Integration method

1. Select the exact functional specification and all referenced system specifications.
2. Obtain the official documents, XML schemas/examples, errata, and conformance materials.
3. Build a product capability matrix: version, services, resources/events, optional fields, authentication, transport, limits, extensions, and declared conformance.
4. Validate XML with hardened parsers: prohibit external entities and network resolution; bound document size, depth, lists, strings, and decompression.
5. Preserve namespace/version and unknown extensions. Do not erase a value simply because an older peer cannot represent it.
6. Model delivery, application acceptance, persistence, rule processing, and physical action as separate results.

CMEM supplies common vocabulary but does not make two vendors' operational meanings identical. Map identity, device/location hierarchy, event type, severity, state transition, timestamps, acknowledgement, clear/restore, media references, and extension fields explicitly.

## Security and conformance

CSEC remains part of the family but its posted edition predates current TLS guidance. Apply its required PSIA semantics together with the exact product profile and current [TLS/PKI baseline](../infrastructure/tls-pki-and-secure-transport.md); do not silently rewrite the specification or claim conformance to a newer transport profile that the product lacks.

PSIA's PLAI listing states that PSIA does not itself test products: members conduct the conformance test and submit a self-declaration and results.[^conformance] Record the declaring vendor, exact product/version, profile/version, declaration/certificate date, and test evidence. A listing is useful evidence, not proof of project-specific interoperability or security.

## Safety boundary

PSIA events can trigger cross-system rules, credential revocation, barrier movement, recording, or alarm workflows. Prevent loops with origin/correlation and idempotency, constrain automation by authoritative event quality, require human approval for high-impact actions, and keep safe-egress/life-safety logic in its approved path. Validate endpoint, schema, retry, duplicate, and authorization behaviour against the selected implementation.

## Primary sources

[^overview]: [PSIA — specifications overview](https://psialliance.org/specifications-overview/)
[^legacy]: [PSIA — specification downloads and listed editions](https://psialliance.org/legacy-specs/)
[^faq]: [PSIA — frequently asked questions](https://psialliance.org/about/faqs/)
[^org]: [PSIA — organization and current working groups](https://psialliance.org/about/organization/)
[^conformance]: [PSIA — PLAI conformant products and disclaimer](https://psialliance.org/conforming-products/plai-conformant/)
