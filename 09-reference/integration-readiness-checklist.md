---
title: "Integration readiness checklist"
summary: "A gate-based evidence checklist for taking a physical-security integration from bounded intent through environment validation and maintainable operations."
page_type: guide
domains:
  - integration
  - cross-domain
tags:
  - integration-readiness
  - acceptance
  - evidence
  - checklist
  - change-control
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: "Process and evidence gates only; it does not approve a product, architecture, production change, safety case, electrical design, legal position, or environment-acceptance result."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Integration readiness checklist

[Home](../README.md) / [Reference](README.md) / Integration readiness checklist

Use this checklist at design review, before an isolated evaluation, before production change, and at acceptance. A checked box needs an evidence reference and named owner; the checklist alone is not acceptance evidence.

## Readiness record

```text
integration ID:
decision/change ID:
business and security owner:
system/data owners:
implementer and independent reviewer:
environments in scope:
target products and exact firmware/software:
protocol/API editions and roles:
observation-only or actuation-capable:
safety classification:
evidence folder/register:
planned validation window and owner:
production approval authority:
rollback owner and stop authority:
```

## Evidence strength

| Label | Meaning |
|---|---|
| `D` | Design assumption or proposed requirement—not verified |
| `S` | Official standard/profile evidence for exact edition |
| `P` | Official product/API documentation for exact product/version |
| `C` | Approved configuration/inventory evidence |
| `E` | Environment observation with date, owner, versions, configuration, input, result, and artifacts |
| `A` | Named owner/authority acceptance of stated evidence and residual risk |

Most production gates need several evidence types. A product claim (`P`) does not substitute for site configuration (`C`) or environment evidence (`E`); environment validation cannot rewrite normative semantics (`S`). Apply the evidence rules in the [verification policy](../10-sources-and-maintenance/verification-policy.md).

## Gate 0 — authority, consequence, and scope

- [ ] Integration purpose, owner, users, assets, sites, tenants, and out-of-scope systems named
- [ ] Read, subscribe, create, update, delete, configure, administer, and actuate capabilities separated
- [ ] Observation and actuation classified using the [safety impact checklist](safety-impact-checklist.md)
- [ ] Doors/locks, gates, lifts, relays, alarms, fire/emergency, dispatch, audio, PTZ, power cycle, and firmware effects identified
- [ ] Privacy/sensitive data includes video, audio, location, access history, credentials, biometrics, device identifiers, and topology
- [ ] Applicable organizational policy, contract, regulator, jurisdiction, labor/privacy, retention, accessibility, and AHJ review assigned to qualified owners
- [ ] Written authority exists for every environment, account, device, network, dataset, and validation activity
- [ ] Explicit stop conditions, emergency contact, maintenance window, rollback, and decision authority recorded

**Stop:** no technical readiness claim is possible while ownership, legal authority, safety consequence, or environment scope is unknown.

## Gate 1 — exact systems, roles, and topology

- [ ] Source of authority identified for identity, configuration, current state, event history, command completion, and evidence
- [ ] Products, licenses, firmware/software, modules, cloud region/tenant, and support lifecycle inventoried
- [ ] Client/server, producer/consumer, controller/peripheral, publisher/subscriber, proxy/gateway, and admin roles explicit
- [ ] Trust boundaries and every decrypt/re-encrypt, protocol translation, queue, cache, database, and export boundary diagrammed
- [ ] IPv4/IPv6, VLAN/zone, routing, NAT, proxy, DNS, time, discovery/multicast, serial/radio, and management paths recorded
- [ ] Normal, degraded, offline, failover, recovery, and replacement topologies recorded
- [ ] Shared dependencies and failure domains include identity, PKI, DNS, time, broker, storage, cloud, license, update, and remote support

Use [physical-security system architecture](../01-foundations/physical-security-system-architecture.md), [protocol layer and role matrix](protocol-layer-and-role-matrix.md), and [system protocol matrix](system-protocol-matrix.md).

## Gate 2 — standards, products, and capability evidence

- [ ] Exact standard/specification title, edition/date, amendments, errata, namespace, and lifecycle status pinned
- [ ] Profile/add-on/companion specification and required versus conditional features mapped
- [ ] Official product documentation and conformance/certification listing match exact model, firmware, role, feature, and region
- [ ] API base/version, schema/WSDL/proto/MIB, SDK/runtime support window, and deprecation policy pinned
- [ ] Capability discovery treated as an untrusted product claim until reconciled with configuration and official evidence
- [ ] Defaults, optional modes, fallback, proprietary extensions, undocumented behavior, and license dependencies recorded
- [ ] Standards/profile changes monitored through the [status register](standards-and-profile-status.md)

**Stop:** “supports ONVIF/OSDP/REST/MQTT/BACnet/SDK” without version, role, security mode, and exact product evidence is not an integration contract.

## Gate 3 — data and semantic contract

- [ ] Resource identities and namespaces stable; display names, addresses, tokens, UIDs, and business IDs not collapsed
- [ ] Field types, units, scale, precision, enum/code tables, null/unknown, default, limits, character encoding, and time semantics defined
- [ ] Source payload retained or referenced safely enough to diagnose mapping changes
- [ ] Event, current state, command, acknowledgement, acceptance, completion, and alarm/operator lifecycle are separate records
- [ ] Source occurrence, device observation, receive, ingest, normalization, persistence, and operator times preserved with clock quality
- [ ] Duplicate, ordering, sequence reset, restart, replay, gap, reconciliation, and stale-state behavior defined
- [ ] Schema/version compatibility, unknown fields/enums, migration, rollback, and consumer support window defined
- [ ] Mapping is loss-aware and uses the [event normalization field guide](event-normalization-field-guide.md)

## Gate 4 — security and privacy

- [ ] Threat model covers external, adjacent-network, malicious/compromised authorized client, device replacement, supply chain, operator error, and dependency failure
- [ ] Server/device/application/user/service/credential identities separated and bound to expected site/tenant/resource
- [ ] TLS/security profile, certificate/key validation, bootstrap, rotation, revocation, expiry, backup, recovery, and compromise response owned
- [ ] Least privilege applies per object/action/topic/stream/door/site; observation and actuation identities are separate
- [ ] Secrets never appear in examples, source, URLs, logs, exports, crash dumps, packet captures, or support bundles
- [ ] Input/message/decompressed body/XML depth/field/string/array/connection/rate/queue/export limits defined before allocation/use
- [ ] SSRF, redirect, callback registration, discovery URL, archive/path, injection, parser differential, and unsafe deserialization controls reviewed
- [ ] Logs/audit protect integrity and privacy; correlation identifiers cannot impersonate trusted identity
- [ ] Data minimization, purpose, access, retention, export, deletion, subject/worker rights, and incident handling approved by qualified owners

Use [protocol security comparison](protocol-security-comparison.md) and [security and assurance](../06-security-and-assurance/README.md).

## Gate 5 — reliability and failure semantics

- [ ] Connect, handshake, header, body/idle, transaction, total, and shutdown deadlines defined with monotonic time
- [ ] Retry matrix is operation-specific; mutation unknown-outcome and idempotency/deduplication are explicit
- [ ] Backoff, jitter, retry budget, circuit breaking, load shedding, queue/disk bounds, and poison-message policy defined
- [ ] Subscription/session lease, renewal, reconnect, resume/replay, checkpoint, and full reconciliation behavior defined
- [ ] Backpressure propagates without silent loss or unsafe fail-open; loss/gap counters are observable
- [ ] Failover does not duplicate actuation, reuse stale authorization, split authority, or hide data gaps
- [ ] Restart/restore/clock step/certificate expiry/dependency outage/partial connectivity behavior modeled
- [ ] Transport success never represented as physical completion; authoritative feedback and timeout/unknown states exist

Use [retries, timeouts, and idempotency](../05-development-and-integration/patterns/retries-timeouts-and-idempotency.md) and [reconnect, backpressure, and queues](../05-development-and-integration/patterns/reconnect-backpressure-and-queues.md).

## Gate 6 — capacity and physical infrastructure

- [ ] Normal, peak, burst, restart, failover, backlog, replay, export, and recovery workloads quantified
- [ ] Connections, subscriptions, sessions, messages, bytes, packet rate, bandwidth, CPU/memory, queues, storage, and rate limits budgeted
- [ ] Media model uses measured mean/peak and [bandwidth/storage units](media-bandwidth-and-storage.md)
- [ ] Multicast/discovery scope, response count, IGMP/MLD, reflectors/proxies, and storm behavior designed
- [ ] Cabling, power, distance, temperature, grounding, surge, UPS, and degraded power reviewed under [physical-layer caveats](cabling-power-and-distance-caveats.md)
- [ ] Service limits and quotas protect small embedded endpoints and shared tenants
- [ ] Capacity acceptance includes fill level, failure/rebuild state, and operational headroom—not headline throughput

## Gate 7 — implementation and static review

- [ ] Protocol parser is incremental/bounded and validates framing, length, type, integrity, state, and semantics in the correct order
- [ ] Safe integer conversion, endian/sign/overflow, Unicode, duplicate key/field, path/URI, and allocation behavior reviewed
- [ ] Generated code/compiler/SDK/runtime versions pinned; dependency and artifact provenance recorded
- [ ] Configuration schema, secrets injection, environment separation, safe defaults, and fail-closed behavior reviewed
- [ ] Read-only and mutating clients are separate modules/credentials; examples cannot accidentally target production
- [ ] Logs/metrics/traces identify layer and failure without exposing sensitive content
- [ ] Independent static review records assumptions, unresolved findings, and evidence references
- [ ] Any environment-specific claim links to a scoped evidence record; see the [code example index](code-example-index.md)

## Gate 8 — isolated environment-validation plan

The responsible integration owner plans, authorizes, supervises, and records environment validation using the [runtime validation template](../10-sources-and-maintenance/templates/runtime-validation-record-template.md).

- [ ] Synthetic/non-production accounts, identities, addresses, media, credentials, events, and endpoints only
- [ ] No dispatch, emergency service, production notification, egress/lock, relay/load, fire/life-safety, or live control path
- [ ] Exact test environment, versions, topology, configuration hash, time source, input, expected result, observed result, and artifacts recorded
- [ ] Positive, malformed, boundary, duplicate, replay, loss, reorder, timeout, restart, dependency outage, certificate rotation/expiry, and recovery cases planned
- [ ] Interoperability covers each product/firmware/role pairing—not only a mock or SDK
- [ ] Security negative tests include wrong identity/role/resource, expired/revoked trust, downgrade, oversized input, and rate/queue limits
- [ ] Safety observer, stop authority, isolation proof, and rollback/witness defined where any physical effect could exist
- [ ] Failed and ambiguous results preserved; no environment-validation claim published without evidence

## Gate 9 — operations and lifecycle

- [ ] Named service owner, runbook, escalation, supplier/support path, and after-hours responsibility
- [ ] Health model distinguishes network, transport, protocol, authentication, authorization, data freshness, physical subsystem, and dependency health
- [ ] Alerts have owner, threshold, suppression/deduplication, diagnostic evidence, and safe response
- [ ] Backup/restore includes configuration, keys/trust, schemas/mappings, queues/checkpoints, audit, and restore verification
- [ ] Certificate/key/token/account/credential rotation and emergency recovery rehearsed by owner
- [ ] Firmware/API/standard/dependency advisories, end-of-life, deprecation, and compatibility review scheduled
- [ ] Change/rollback/migration preserve old/new schema and credential overlap only for a bounded period
- [ ] Decommission revokes trust/accounts/tokens, removes flows/discovery/DNS, sanitizes data, and retains required evidence

Use [operations and lifecycle](../07-operations-and-lifecycle/README.md) and the [review register](../10-sources-and-maintenance/review-register.md).

## Final acceptance record

| Decision | Required entry |
|---|---|
| Accepted scope | Exact versions, sites, roles, actions, data classes, and exclusions |
| Evidence | `S/P/C/E/A` references, dates, owner, immutable artifact/hash where used |
| Open limitations | Unassessed cases, vendor claims, scale/failure gaps, regional/legal unknowns |
| Residual risk | Consequence, likelihood rationale, compensating controls, accepting authority, expiry |
| Production guardrails | Least privilege, feature flags, rate limits, canary, monitoring, stop/rollback |
| Review triggers | Firmware/API/standard/security advisory, topology, key, policy, incident, owner change |
| Outcome | `not ready`, `ready for isolated validation`, or `accepted by named authority for exact scope` |

This page never assigns an “accepted” outcome. That decision belongs to the authorized owners and qualified safety/legal/electrical authorities for the exact system.

## Related governance

- [Authorized and safe use](../10-sources-and-maintenance/authorized-and-safe-use.md)
- [Source policy](../10-sources-and-maintenance/source-policy.md)
- [Environment validation checklist](../10-sources-and-maintenance/manual-qa-checklist.md)
- [Secure integration lifecycle](../01-foundations/secure-integration-lifecycle.md)
- [Vendor API capability matrix](vendor-api-capability-matrix.md)
