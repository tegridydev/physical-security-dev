---
title: HR, Identity, and Visitor Integration
summary: Authoritative identity, lifecycle, entitlement, synchronization, privacy, and recovery patterns across HR, directories, PACS, and visitor systems.
page_type: system
domains: [identity, access-control, integration]
tags: [hr-integration, identity-governance, scim, visitors, joiner-mover-leaver]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [RFC 7643, RFC 7644, PSIA PLAI]
coverage_limit: Architecture and lifecycle semantics only; no employment decision, entitlement policy, identity proofing procedure, personal dataset, credential secret, or live provisioning operation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# HR, identity, and visitor integration

Employment, digital identity, physical identity, access entitlement, credential, visit, and presence are related but distinct. Integration should propagate approved lifecycle facts while each system retains authority for its own decisions and evidence.

## Authority map

| Concern | Typical authority | Important boundary |
|---|---|---|
| employment/engagement status and organizational attributes | HR/workforce source | status alone does not grant physical access |
| digital account/authentication | identity provider/directory | account disable and PACS revoke have different completion evidence |
| physical person/holder record | PACS/identity governance | mapped to a durable source identity, not email alone |
| access role/entitlement approval | approved access-governance process | policy owner and approver must be attributable |
| credential keys/status | credential/PACS ecosystem | HR must not receive secrets or cloning capability |
| visit, host, sponsor, validity | visitor system and approved policy | visit approval is not unrestricted site entitlement |
| door decision and telemetry | PACS controller/door | upstream provisioning success is not a door grant |

Create a field-level matrix for source, owner, purpose, validation, target, transform, conflict, maximum age, retention, and deletion. A “master system” label is too coarse.

## Durable identity and matching

Use a non-reassigned, durable source identifier plus authoritative provenance. Email, name, phone, employee number, credential number, and department can change or collide. Automatic matching on weak attributes can merge two people and create unauthorized access.

Represent person, employment/engagement, digital account, physical holder, role, entitlement, credential, visit, sponsor/host, and vehicle as separate entities with explicit relationships and validity intervals. Record confidence and review for any non-authoritative match.

## Lifecycle

```text
source change -> validated identity event -> policy/approval evaluation
 -> target provisioning request -> target result
 -> entitlement/credential state verification -> exception/reconciliation
```

Handle pre-hire/scheduled activation, join, internal move, additional role, temporary assignment, leave/suspension, return, termination, extension, rehire, contractor end, and corrected records. Define effective time and timezone, approval, dependency ordering, retry, duplicate, out-of-order, and rollback semantics.

For high-risk cessation, distinguish request generated, target accepted, holder disabled, controller updates distributed, offline-controller exposure, mobile credential revoked, and physical credential recovered. Report unresolved targets; never close the workflow because one API call returned success.

## Provisioning interfaces

[RFC 7643](https://www.rfc-editor.org/info/rfc7643) defines the SCIM core schema and [RFC 7644](https://www.rfc-editor.org/info/rfc7644) defines its HTTP-based protocol. SCIM does not define an organization's entitlement policy, physical credential security, controller distribution, or door semantics. Verify schema extensions, PATCH/replace/delete behavior, filtering, pagination, ETags/versioning, bulk operations, errors, and product-specific limits.

PSIA describes [PLAI](https://psialliance.org/all-about-plai/) as an interoperability approach for normalizing and sharing identities and access privileges across physical access-control systems. Use its [published specifications](https://psialliance.org/specifications-overview/) and product evidence for exact interoperability; do not infer conformance from generic API support.

## Visitor and temporary identity

Capture only necessary visitor, host, approval, purpose, validity, location, escort, training/terms, credential, vehicle, and visit outcome data. Enforce expiry in the authoritative access system, including controller/offline behavior. Separate preregistration, identity verification, arrival, credential issue, access activation, check-in/out, credential return, cancellation, no-show, and deletion.

Self-service kiosks, document capture, watchlist checks, biometrics, host notification, and cross-site reuse need separate necessity, security, privacy, accessibility, and error review. Avoid making a visitor's access or safety depend solely on personal email/SMS or a mobile application.

See [Visitor, identity, and elevator integration](../access-control/visitor-identity-and-elevator-integration.md).

## Security, privacy, and reconciliation

- Use separate, least-privilege read and write workloads; scope by tenant/site/object/attribute.
- Protect API tokens/keys and personal data; restrict bulk read/export and support access.
- Validate allowed attribute changes and prevent source data from assigning privileged roles directly.
- Retain raw source event/reference, transform/version, request/result, approver, and exception.
- Reconcile authoritative source, target database, controller distribution, and credential state on a controlled schedule.
- Detect orphan accounts, duplicate holders, expired visits, stale roles, future-dated anomalies, and failed revocations.
- Define lawful purpose, transparency, correction, minimization, retention, deletion, and cross-border/provider boundaries.

## Acceptance evidence

Use synthetic or expressly authorized test identities in an approved isolated process to cover the lifecycle matrix, duplicates, delayed/out-of-order changes, retry, partial target failure, source correction, termination, rehire, offline controller, privacy deletion, and recovery. Record source, integration, and downstream reconciliation evidence separately.

Return to [Integration platforms](README.md).
