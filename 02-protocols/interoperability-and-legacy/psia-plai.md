---
title: PSIA Physical-Logical Access Interoperability
summary: PLAI identity and privilege synchronization, adapters, authoritative-source rules, lifecycle controls, privacy, and conformance evidence.
page_type: protocol
domains: [identity, access-control, cross-domain]
tags: [psia, plai, pacs, identity-synchronization, ldap, provisioning]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [PSIA Area Control including PLAI v3.1, LDAP v3]
coverage_limit: Published PSIA overview and v3.1 baseline were reviewed; the current Integrators Kit, schemas, conformance tools, and product-specific adapters are required for implementation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# PSIA Physical-Logical Access Interoperability

[Home](../../README.md) / [Protocols](../README.md) / [Interoperability and legacy](README.md) / [PSIA](psia.md) / PLAI

Physical-Logical Access Interoperability (PLAI) normalizes and synchronizes identity, credential, role, and access information between an authoritative logical/HR source and disparate physical access-control systems (PACS). PSIA describes PLAI as using the LDAP v3 interface and lists Area Control including PLAI v3.1, released 7 August 2019, in its current downloads.[^plai][^legacy]

```text
authoritative HR/IAM/directory
            │ lifecycle and roles
            ▼
       PLAI agent/model
       ┌────┴─────────┐
       ▼              ▼
 PACS adapter A   PACS adapter B   ... biometric/visitor integrations
```

The architecture must name one authority for each attribute and decision. “Single source” cannot remain a slogan: record whether HR owns legal identity/employment, IAM owns role, a PACS owns card format/number, a local site owns access level, and a biometric system owns templates.

## Synchronization contract

For every entity and field define stable identifier, source, schema/version, normalization, create/update/disable/delete semantics, effective/expiry time, precedence, conflict handling, retry, idempotency, tombstone retention, acknowledgement, reconciliation interval, and audit. Do not use name or email as the immutable person key.

High-impact cases require explicit state machines:

- pre-hire and future-dated activation;
- transfer between sites/roles and overlapping entitlements;
- termination/emergency revocation when one PACS is offline;
- lost/replaced/shared credentials and duplicate credential detection;
- leave/suspension and time-bounded visitor/contractor access;
- rename, rehire, merger of duplicate identities, and deletion/privacy requests;
- adapter backlog, partial fan-out, poison record, retry exhaustion, and later reconciliation.

Never represent “could not update PACS B” as global success. Return a per-target result and expose age/backlog. Revocation workflows should fail closed for new grants, use an approved emergency path, and alert until every target is reconciled.

## Security and privacy

Authenticate every agent, adapter, directory, and PACS with unique service identity; encrypt transport and validate peer identity. Authorize minimum LDAP base/attributes and minimum PACS operations. Separate provisioning, reconciliation/read, revocation, and administration roles. Protect queues, exports, backups, logs, schema maps, and dead-letter records as sensitive identity data.

Biometric templates and location/presence data need purpose limitation, data minimization, jurisdictional retention/consent controls, and vendor-specific protection. Avoid moving raw biometrics when a scoped reference or protected template meets the purpose. Do not use physical presence as silent authentication for unrelated logical access without policy, user notice, freshness, anti-tailgating limitations, and an independent recovery path.

## Conformance evidence

PSIA provides an Integrators Kit and test-tool packet. Its product page explicitly says PSIA does not conduct conformance testing; vendors run the test and submit self-declarations/results.[^conformance] Verify the exact vendor product, version, PLAI version, declaration date, tested group/event set, known exceptions, and your own cross-vendor lifecycle cases.

Validate directory, PLAI agent, PACS adapter, conformance, reconciliation, and identity-lifecycle behaviour with synthetic identities in an isolated authorized environment.

## Primary sources

[^plai]: [PSIA — All About PLAI](https://psialliance.org/all-about-plai/)
[^legacy]: [PSIA — Area Control including PLAI v3.1 download listing](https://psialliance.org/legacy-specs/)
[^conformance]: [PSIA — PLAI conformant products and self-declaration model](https://psialliance.org/conforming-products/plai-conformant/)
- [PSIA — specification family overview](https://psialliance.org/specifications-overview/)
- [RFC Editor — RFC 4511, LDAP v3](https://www.rfc-editor.org/info/rfc4511/)
