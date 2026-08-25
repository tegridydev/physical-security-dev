---
title: "Vendor API capability matrix"
summary: "A generic evidence contract for comparing vendor-owned APIs and SDKs without turning documentation labels into product capability claims."
page_type: reference
domains:
  - integration
  - cross-domain
tags:
  - vendor-apis
  - capability-matrix
  - evidence
  - sdk
  - selection
scope: global
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: "Comparison schema and evidence gates only; this page intentionally carries no vendor capability cells and makes no endpoint, entitlement, licence, region, compatibility, performance, security, or availability claim."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Vendor API capability matrix

[Home](../README.md) / [Reference](README.md) / Vendor API capability matrix

> This reference defines **how** to compare vendor APIs. It intentionally does not duplicate fast-changing vendor capability claims. Use the maintained [vendor API catalogue](../04-vendor-apis/README.md) and its [selection and capability matrix](../04-vendor-apis/selection-and-capability-matrix.md) for source-backed vendor rows, then open each vendor page and current official documentation.

## Why the matrix stays generic

A single check mark such as “events,” “video,” or “access control” hides the facts that decide compatibility:

- exact product family/build/firmware and API/SDK release;
- deployment model, region, tenant, licence, partner program, and feature entitlement;
- operation direction and authoritative system;
- resource granularity, security identity, scope, and role;
- delivery, pagination, rate, queue, retention, and reconciliation behavior;
- deprecation, support, distribution, and legal/licensing terms;
- whether an operation observes, configures, or physically actuates.

Therefore this page carries no vendor rows. A populated row belongs beside its official sources in `04-vendor-apis`, not as an uncited summary here.

## One row per exact surface

Do not create one row per marketing brand. Create a row only for an evidence-bounded surface:

```text
vendor / publisher:
product family and deployment:
API, SDK, plug-in framework, or protocol surface:
exact API/SDK/document version:
supported product/server/firmware window:
region/tenant/licence/partner prerequisites:
official reference and access date:
release/lifecycle source and access date:
canonical vendor page:
evidence grade and coverage limit:
```

If a public landing page establishes that a surface exists but the normative contract is gated, record that limitation. Do not reverse engineer a capability cell from marketing copy, UI screenshots, package names, forum posts, or an SDK class list.

## Comparison dimensions

### Deployment and authority

| Field | Values to record—not assume |
|---|---|
| Deployment | Device/edge, on-prem server, appliance, desktop client, mobile, private cloud, SaaS, hybrid |
| Authority | System of record for identity, configuration, event history, live state, media, credentials, physical command |
| Direction | Read, poll, subscribe, callback, provision, configure, command, plug-in/extension, media ingest/export |
| Boundary | Direct device, controller, VMS/PACS, gateway, broker, vendor cloud, customer cloud, partner service |
| Tenancy/region | Organization/site/tenant hierarchy, regional base URLs, sovereign/private editions, data residency |
| Availability dependency | LAN, server cluster, cloud control plane, vendor identity/licensing, mobile platform, partner service |

### Access and entitlement

| Field | Evidence question |
|---|---|
| Documentation access | Public, account-gated, partner-only, licensed install, NDA, package-local, unavailable |
| Development eligibility | Open registration, vendor approval, customer sponsorship, certification, commercial agreement |
| Runtime entitlement | Product edition, feature licence, subscription, per-device/channel/user entitlement |
| Distribution | May the SDK/runtime/plug-in be redistributed, and under which official terms? |
| Support | Supported integration program versus best-effort/public interface; escalation and end-of-support path |
| Environment | Sandbox/demo/non-production availability and whether it is behaviorally representative |

Access to documentation is not runtime entitlement. A customer login is not permission to redistribute a licensed SDK, and a downloaded SDK is not proof of compatibility with an installed product.

### Identity and security

| Dimension | Required evidence |
|---|---|
| Client enrollment | Registration, redirect/callback ownership, device/service identity bootstrap |
| Authentication | Exact OAuth flow/profile, mTLS/certificate, signed request, API token/key, session, local account, SDK mechanism |
| Authorization | Tenant/site/resource/action scope; read, event, media, configuration, credential, admin, physical command separated |
| Secret lifecycle | Creation, display, storage, rotation, overlap, revocation, expiry, compromise, operator offboarding |
| Transport | TLS versions/profile, certificate/hostname validation, proxy/gateway termination, private connectivity |
| Callback security | Registration authorization, destination validation, signature/mTLS, replay window, secret rotation, SSRF controls |
| Audit | Trusted principal, target/action, decision, request/result/correlation, admin/config changes, export/redaction |
| Limits | Body/message/decompression, pagination, connection, stream, subscription, rate, queue, export and tenant quotas |

### Capability classes

Use these only as **headings for evidence**, never yes/no marketing cells:

| Class | Minimum detail before comparison |
|---|---|
| Inventory/discovery | Resource types, stable IDs, pagination, filters, consistency, deleted/tombstone behavior |
| Health/status | Poll/event source, freshness, quality, counters, restart/failover semantics |
| Events/alarms | Types/schema, ordering, duplicate/replay, delivery/ack, retention/replay, gap reconciliation |
| Live media | Codec/transport, session authorization, concurrency, latency, audio, PTZ/control separation |
| Recorded media/export | Search/index semantics, time/clock, watermark/signature, export job, retention/legal hold, evidence custody |
| Configuration | Resource/version model, validation, optimistic concurrency, transaction/apply/restart/rollback |
| Identity/credential | Subject/credential namespaces, issuance/revocation, keys/mobile/biometric handling, offline propagation |
| Door/output/device control | Exact command/preconditions, idempotency, unknown outcome, authoritative physical feedback, audit |
| Plug-in/edge app | Trust/sandbox, signing, package lifecycle, permissions, resource limits, compatibility/crash isolation |
| Administration/update | Accounts/roles, certificate/trust, firmware, backup/restore, restart; normally separate high-impact surface |

For any physical-control class, attach the [safety impact checklist](safety-impact-checklist.md). “Unlock available” without preconditions, exact authorization, completion feedback, timeout behavior, and qualified owner approval is not a useful capability claim.

## Evidence states for a cell

| State | Meaning |
|---|---|
| `not researched` | No official evidence reviewed; do not infer absent or present |
| `not publicly established` | Official public material reviewed but does not establish the capability; gated material may exist |
| `documented` | Official exact-version reference defines the capability/class within stated limits |
| `entitlement required` | Official evidence says licence/account/partner/feature access is required |
| `deprecated` | Official lifecycle source deprecates/withdraws the surface or operation, with date/replacement where stated |
| `configuration evidenced` | Approved site configuration shows it is enabled for exact scope; this is not behavior or interoperability evidence |
| `environment validated` | A scoped record identifies exact versions, configuration, cases, observations, limitations, date, and responsible owner |
| `unsupported for exact scope` | Official compatibility/support evidence explicitly excludes the exact product/version/role—not merely absent docs |

Never encode unknown as `no`. Never promote a vendor documentation claim to `environment validated`. A product can support an API family while omitting a method, model, event, role, or security mode.

## Suggested populated table contract

The canonical vendor section may use several tables rather than one extremely wide table. Each row should be reducible to:

| Column | Required content |
|---|---|
| Surface | Vendor, product/deployment, API/SDK/framework, exact version |
| Evidence | Official reference(s), release/lifecycle source, access date, evidence grade |
| Prerequisites | Product/firmware, region/tenant, licence, partner/account, runtime/OS |
| Authority/direction | System of record and read/event/configure/command/extension direction |
| Capability statement | Narrow source-supported statement with limitations—not a check mark alone |
| Security | Authentication, authorization scope, TLS/callback, secret lifecycle boundary |
| Reliability | Pagination/rate, event delivery/replay, retry/idempotency, reconnect/reconciliation |
| Safety/privacy | Sensitive data and any high-impact operations; qualified approval boundary |
| Validation | Linked environment evidence, cases, results, limitations, date, and owner; otherwise `not established` |
| Review | Last verified, next review, deprecation/security-advisory triggers |

## Shortlisting questions

- [ ] Does the surface exist for the exact installed deployment, build, model, licence, region, and role?
- [ ] Is its normative contract accessible under acceptable terms for development, deployment, and maintenance?
- [ ] Is it authoritative for the desired data/action, or a cache/proxy with weaker semantics?
- [ ] Can observation, configuration, administration, credential, media, and physical command privileges be separated?
- [ ] Are stable IDs, schema/version, pagination, event replay, reconciliation, and deletion semantics documented?
- [ ] Are timeout/retry/duplicate/unknown-outcome rules safe for every mutating operation?
- [ ] Are quotas, concurrency, retention, export, and failure/recovery limits available and owner-testable?
- [ ] Are certificates/secrets/tokens/callbacks manageable throughout deployment and offboarding?
- [ ] Are release notes, deprecation notices, security advisories, compatibility matrices, and support paths durable?
- [ ] Is a standards-based surface preferable or required, and is the exact product/profile registered/certified?
- [ ] Can the integration team validate it with synthetic data in an isolated authorized environment without physical consequence?

## Related pages

- [Vendor API catalogue](../04-vendor-apis/README.md)
- [Vendor API selection and capability matrix](../04-vendor-apis/selection-and-capability-matrix.md)
- [Integration readiness checklist](integration-readiness-checklist.md)
- [API and event security](../06-security-and-assurance/api-and-event-security.md)
- [Retries, timeouts, and idempotency](../05-development-and-integration/patterns/retries-timeouts-and-idempotency.md)
- [Polling, subscriptions, and state reconciliation](../05-development-and-integration/patterns/polling-subscriptions-and-state-reconciliation.md)
- [Vendor API page template](../10-sources-and-maintenance/templates/vendor-api-page-template.md)
