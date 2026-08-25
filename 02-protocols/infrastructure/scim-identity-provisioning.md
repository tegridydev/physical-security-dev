---
title: "SCIM identity provisioning and reconciliation"
summary: "Secure SCIM 2.0 lifecycle integration for users, groups, devices, cursor pagination, asynchronous events, reconciliation, and physical-security boundaries."
page_type: protocol
domains: [identity, integration, cross-domain]
tags:
  - scim
  - provisioning
  - identity-lifecycle
  - reconciliation
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "RFC 7643: System for Cross-domain Identity Management: Core Schema"
  - "RFC 7644: System for Cross-domain Identity Management: Protocol"
  - "RFC 9865: Cursor-Based Pagination of System of Cross-domain Identity Management (SCIM) Resources"
  - "RFC 9944: Device Schema Extensions to the System for Cross-Domain Identity Management (SCIM) Model"
  - "RFC 9967: System for Cross-Domain Identity Management (SCIM) Profile for Security Event Tokens (SETs)"
  - "RFC 8417: Security Event Token"
coverage_limit: "SCIM protocol and lifecycle architecture; product schemas, extension support, source-of-truth policy, physical credential issuance, access entitlements, and controller distribution remain deployment-specific."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# SCIM identity provisioning and reconciliation

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / SCIM identity provisioning

System for Cross-domain Identity Management (SCIM) 2.0 defines common schemas and an HTTP protocol for managing identity resources across domains. RFC 7643 defines the core schema; RFC 7644 defines discovery, retrieval, search, create, replace, patch, delete, bulk, filtering, sorting, and pagination behavior. [SCIM-SCHEMA] [SCIM-PROTOCOL]

SCIM is a lifecycle transport and schema framework. It does not authenticate an operator session, prove a person’s real-world identity, issue a physical credential, define door permissions, or confirm that a controller received a change.

## Roles and lifecycle boundary

| Role | Responsibility | Common failure to avoid |
|---|---|---|
| Authoritative source | Owns selected identity and lifecycle facts | Treating every source attribute as authoritative |
| SCIM client | Translates source changes into bounded protocol operations | Sending a mutable display value as the durable identity key |
| SCIM service provider | Exposes resources, schema, capabilities, and protocol behavior | Claiming support without implementing advertised PATCH/filter semantics |
| Target application | Maps provisioned resources to local accounts and roles | Turning an external group name directly into unrestricted administration |
| PACS/credential workflow | Approves identity, access profile, credential, and controller distribution | Treating HTTP success as physical-access revocation |

A robust integration tracks each stage independently:

```text
authoritative record changed
  -> SCIM request accepted
  -> target identity state committed
  -> target role/entitlement mapping reconciled
  -> approved PACS workflow updated
  -> credential/controller state distributed
  -> effective state verified from its authoritative source
```

## Discovery and schema contracts

SCIM provides discovery resources including `ServiceProviderConfig`, `ResourceTypes`, and `Schemas`. Cache them only for a controlled period and alert on incompatible change.

Record for every integration:

- base URL and tenant/environment binding;
- advertised and actually supported authentication profile;
- core and extension schema URNs plus revision/change policy;
- supported resources and endpoint paths;
- filter operators/attributes, sort behavior, and case sensitivity;
- pagination mode and maximum page size;
- PATCH, ETag/version, bulk, delete, and uniqueness semantics;
- rate, concurrency, payload, collection, and response limits;
- product-specific error and retry behavior.

The core `User` and `Group` resources are starting points, not permission models. Enterprise user, device, or vendor extensions must use stable schema URNs and document required/mutability/returned/uniqueness properties. Reject an unknown critical extension; preserve or ignore optional unknown attributes only under the agreed schema policy.

## Resource identity

SCIM separates several identifiers:

- `id` is the service provider’s stable resource identifier and should not be reassigned.
- `externalId` is a client-provided identifier intended to help correlate a resource across domains; its scope and uniqueness are client/service agreements.
- `userName`, display names, emails, employee numbers, and group names may change and may not be globally unique.
- `meta.version` can support conditional requests when the service provider implements versioning/ETags.

Use an explicit correlation table containing source system, source immutable ID, target tenant, SCIM resource type, target SCIM `id`, mapping version, and lifecycle state. Never merge two people or devices solely because a mutable human-readable attribute matches.

Define canonicalization before uniqueness checks. Case sensitivity, Unicode handling, whitespace, phone/email normalization, and multi-valued `type`/`primary` fields can otherwise create duplicates or update the wrong resource.

## Create, replace, patch, and delete

### Create

Before `POST`, choose a deterministic duplicate policy. A timed-out create can have succeeded. Search or reconcile by a scoped immutable `externalId`; do not blindly retry and create a second person, device, or account.

### Replace

`PUT` is replacement under SCIM semantics. Define how omitted optional attributes are treated, which server-managed attributes remain, and whether the product applies non-standard merge behavior. A language object serialized with default empty arrays can unintentionally remove memberships or contact values.

### Patch

SCIM PATCH has its own operations, paths, filters, and multi-valued-attribute rules. Validate:

- `add`, `remove`, and `replace` support exactly as advertised;
- path grammar, schema prefixes, filter evaluation, and case sensitivity;
- missing path and no-match behavior;
- atomicity of the patch request;
- duplicate membership and multi-valued primary-value constraints;
- concurrent changes through `If-Match` where versioning is supported.

Do not build patch paths through raw string concatenation from untrusted attribute names or values.

### Delete and deactivate

Deletion, `active: false`, suspension, archival, and anonymization have different effects. Define the source-of-truth transition and downstream obligations. A target may retain audit evidence after deactivation or deletion; privacy and legal policy must govern retained identifiers.

For physical security, deactivating a SCIM user does not prove revocation of cards, mobile credentials, PINs, cached offline rights, visitor passes, active sessions, or controller state. Drive and verify those through the approved credential and PACS lifecycle.

## Groups, roles, and entitlements

SCIM Groups express membership; they do not establish what a local role may do.

- Map only allowlisted external groups to locally defined roles.
- Scope mapping by trusted source, tenant, site, and environment—not group display name alone.
- Define whether the source pushes membership, the target owns membership, or reconciliation merges selected fields.
- Bound group size, nesting depth, expansion work, and cycle handling.
- Detect truncated/over-limit group claims and partial membership pages.
- Keep operator administration, video export, credential management, unlock/override, and platform configuration as separate permissions.
- Version and audit the mapping policy independently of SCIM resource changes.

Use an approval workflow for physical-access profiles. An upstream group named `Building-A-Access` is input to policy, not self-authenticating authorization to a building.

## Pagination and complete enumeration

RFC 7644 defines index-based pagination using `startIndex` and `count`. A changing collection can shift while pages are read, causing duplicates or omissions. Always use stable tie-breakers where the product supports them and reconcile by immutable ID.

RFC 9865 adds cursor-based pagination for SCIM. [SCIM-CURSOR]

- Treat cursors as opaque, tenant- and query-bound, expiring server state.
- Do not parse, edit, log, or reuse a cursor with different filters/sort/attributes.
- Bound page size and total enumeration work.
- Detect cursor expiry and restart with a documented high-watermark/reconciliation strategy.
- Do not infer a consistent snapshot unless the service contract explicitly promises one.

Pagination completion establishes only what the service returned under that query. Compare it with the prior authoritative snapshot and investigate unexpected mass additions, removals, or omissions before applying high-impact changes.

## Bulk operations

SCIM bulk requests reduce round trips but increase blast radius. Check advertised `maxOperations` and `maxPayloadSize`, dependency handling through `bulkId`, error threshold, per-operation status, and whether the product provides any atomicity. Do not assume one HTTP response means every sub-operation committed.

Split changes into bounded batches, preserve per-resource correlation, stop on systemic schema/authentication failures, and reconcile the final target state. Protect against a malformed dependency graph, duplicate `bulkId`, excessive response body, and retry of an uncertain partially completed batch.

## Devices and modern extensions

RFC 9944 defines a SCIM schema for device resources, extending SCIM beyond users and groups. [SCIM-DEVICE]

Treat a provisioned device record as inventory/lifecycle information, not cryptographic device authentication. Enrollment, key generation, attestation, certificate issuance, secure boot, firmware state, network admission, and decommissioning require separate protocols and evidence. Map device identifiers only after establishing their issuer, uniqueness, replacement, and transfer rules.

Extension support is independently negotiable: a service implementing RFC 7643/7644 does not automatically implement cursor pagination, the device schema, events, or vendor extensions.

## Asynchronous events and reconciliation

RFC 9967 defines SCIM event delivery using Security Event Tokens (SETs); RFC 8417 defines the SET format and processing framework. [SCIM-EVENTS] [SET]

An event can reduce propagation delay, but it is not a substitute for reconciliation:

- validate SET issuer, audience, signature/algorithm, time, event type, token ID/replay, and delivery-channel authorization;
- bind the event to the correct SCIM tenant and resource service;
- cap token/event size and reject conflicting or duplicate security-critical members;
- store a durable event ID/high-watermark under a bounded retention policy;
- handle duplicate, delayed, out-of-order, missing, and unsupported events;
- fetch authoritative current resource state rather than trusting an event to contain a complete record;
- periodically enumerate/reconcile to repair missed delivery and local drift.

Receipt or acknowledgement of a SET proves only an event-channel step. It does not prove the SCIM mutation, mapped role, physical credential, or controller state is effective.

## Authentication, authorization, and transport

RFC 7644 requires TLS and describes bearer-token and other authentication considerations, but deployments must define a current HTTP/OAuth profile. [SCIM-PROTOCOL]

- Validate HTTPS endpoint identity; pin allowed hosts and redirect behavior.
- Use a dedicated client/workload identity with short-lived, audience-bound credentials where supported.
- Separate read/search, create/update, group membership, bulk, device, event, and administrative permissions.
- Enforce tenant and resource-type authorization server-side; filters are not access controls.
- Do not place credentials or personal attributes in URLs or verbose error logs.
- Rotate credentials and keys with overlap and rollback; monitor stale credentials.
- Apply per-client and per-tenant rate, concurrency, enumeration, export, and mutation limits.

## Reliability and loop prevention

- Use connect, TLS, response-header, body-idle, and total operation deadlines.
- Retry bounded reads under policy; retry mutations only with correlation, conditional requests, and uncertainty handling.
- Classify `429`/`Retry-After`, authentication, authorization, schema, conflict, server, and transport failures separately.
- Prevent bidirectional connectors from echoing the same update indefinitely. Record source, source revision, mapping version, and last writer.
- Quarantine poison records rather than blocking the whole lifecycle queue.
- Alert on backlog age, not just queue length; a small queue can contain an old high-impact leaver event.

## Privacy, audit, and evidence

Minimize attributes to the target purpose. Identity records may contain employment, contact, organization, location, manager, device, and access-related data. Define field-level ownership, retention, regional transfer, support access, export, correction, and deletion policy.

Audit authenticated client, source/target tenant, resource type and stable IDs, operation, changed attribute names rather than secret values, prior/new lifecycle state, mapping version, conditional version, request/event correlation, result, and downstream reconciliation outcome. Keep bearer tokens and unnecessary full user/device records out of logs.

## Review checklist

- [ ] ServiceProviderConfig, ResourceTypes, Schemas, extensions, limits, and product deviations recorded
- [ ] Immutable source-to-target correlation used; mutable names never used as the sole identity key
- [ ] Attribute ownership, canonicalization, uniqueness, mutability, returned behavior, and privacy defined
- [ ] POST timeout/duplicate, PUT omission, PATCH path/filter, DELETE/deactivate, and concurrency semantics validated in a controlled environment under system-owner approval
- [ ] Group-to-role mapping allowlisted, scoped, versioned, and separated from physical entitlements
- [ ] Index or cursor pagination handles change, expiry, duplication, omission, and bounded enumeration
- [ ] Bulk partial completion tracked per operation and reconciled
- [ ] Events authenticated, replay-protected, treated as hints to authoritative state, and backed by reconciliation
- [ ] Device records kept separate from device authentication and attestation
- [ ] SCIM state kept separate from credentials, controller distribution, and effective physical access
- [ ] Authentication, tenant authorization, rate limits, loop prevention, quarantine, audit, and privacy enforced

## Sources

- **SCIM-SCHEMA** — [RFC 7643: System for Cross-domain Identity Management: Core Schema][SCIM-SCHEMA], IETF, September 2015.
- **SCIM-PROTOCOL** — [RFC 7644: System for Cross-domain Identity Management: Protocol][SCIM-PROTOCOL], IETF, September 2015.
- **SCIM-CURSOR** — [RFC 9865: Cursor-Based Pagination of System of Cross-domain Identity Management (SCIM) Resources][SCIM-CURSOR], IETF, October 2025.
- **SCIM-DEVICE** — [RFC 9944: Device Schema Extensions to the System for Cross-Domain Identity Management (SCIM) Model][SCIM-DEVICE], IETF, May 2026.
- **SCIM-EVENTS** — [RFC 9967: System for Cross-Domain Identity Management (SCIM) Profile for Security Event Tokens (SETs)][SCIM-EVENTS], IETF, May 2026.
- **SET** — [RFC 8417: Security Event Token (SET)][SET], IETF, July 2018.

[SCIM-SCHEMA]: https://www.rfc-editor.org/info/rfc7643/
[SCIM-PROTOCOL]: https://www.rfc-editor.org/info/rfc7644/
[SCIM-CURSOR]: https://www.rfc-editor.org/info/rfc9865/
[SCIM-DEVICE]: https://www.rfc-editor.org/info/rfc9944/
[SCIM-EVENTS]: https://www.rfc-editor.org/info/rfc9967/
[SET]: https://www.rfc-editor.org/info/rfc8417/
