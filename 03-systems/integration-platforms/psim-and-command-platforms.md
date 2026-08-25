---
title: PSIM and Command Platforms
summary: Authority, adapter, canonical-state, workflow, command, audit, and failure architecture for physical-security integration platforms.
page_type: system
domains: [integration, operations, cross-domain]
tags: [psim, command-platforms, event-correlation, operator-workflows]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [NIST SP 800-207]
coverage_limit: Platform-neutral architecture only; no vendor feature assertion, live command, playbook, response authority, or product interoperability claim.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# PSIM and command platforms

Physical security information management and command platforms combine events, state, maps, procedures, video, identity, cases, and sometimes control. Their useful role is correlation and governed workflow. Their principal risk is becoming a broad, opaque control plane with stale or over-normalized data.

## Reference architecture

```text
source system
 -> source-specific adapter and constrained identity
 -> immutable raw event/state observation
 -> canonical mapping with provenance and quality
 -> correlation/rules and workflow
 -> operator decision or explicitly approved automation
 -> target-specific adapter and constrained command
 -> native acknowledgement/telemetry
 -> case and audit record
```

Keep ingestion and control identities separate. Split by tenant, site, security domain, and capability so compromise of a display or one adapter does not create universal actuation.

## Source authority and canonical model

For every object and field, document the authoritative source, mapping owner, refresh mode, maximum age, conflict rule, and behavior when the source is unavailable. Preserve native identifiers, event codes, timestamps, sequence, quality, raw payload or reference, adapter/parser version, and received time.

Canonical categories help operators, but never erase source meaning. `alarm`, `acknowledged`, `restore`, `door open`, `device offline`, and `case closed` mean different things across systems. Maintain a mapping table and expose uncertainty or unsupported state.

Use separate objects for:

- current reported state and the time/quality of that report;
- immutable source event;
- derived correlation/incident;
- operator task and acknowledgement;
- case disposition/closure;
- command request, target acceptance, physical telemetry, and outcome.

## Correlation and workflow

Rules should be versioned, attributable, testable against representative historical/synthetic records, explainable to an operator, and reversible. Store contributing and contradicting events. Missing telemetry must be `unknown`, not a negative condition.

Workflows can guide verification, escalation, evidence capture, communications, and handover, but must show policy version, required/optional steps, authority, deadline, exception reason, and incomplete dependencies. Avoid forcing operators to enter a false answer merely to advance a case.

Maps and dashboards need source time, state age, live/recorded status, and failure overlays. A green aggregate must not hide an unavailable adapter, stale site, bypassed zone, lost recording, or disabled rule.

## Command boundary

Use semantic operations such as a constrained access request, camera preset request, or alarm acknowledgement—not raw relay, register, shell, or unrestricted vendor calls. For every command define:

- authorized roles, target scope, prerequisites, reason, confirmation, and expiry;
- idempotency/replay/duplicate behavior, timeout, cancellation, and queueing;
- native system policy and safety checks that remain authoritative;
- returned protocol result versus observed physical state;
- dual authorization or break-glass where consequence warrants;
- complete audit and reconciliation after partial failure.

Do not create generic cross-domain automation such as “alarm implies unlock/gate cycle/lift action.” Physical effects require an approved cause-and-effect and safety boundary.

## Security architecture

- Strong workforce/workload identity and least-privilege adapters; no shared global service account.
- Explicit authorization at each request, independent of network location.
- Segmented management, ingestion, media, command, and third-party connections.
- Protected secrets/keys, certificate rotation, supported patching, dependency inventory, and recovery.
- Tenant/site isolation for data, search, caches, exports, rules, notifications, and support access.
- Audit of identity, configuration, mapping, rule, workflow, view/search, export, and command activity.
- Egress controls and allowlisted integration destinations; integrations are supply-chain boundaries.

NIST [SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) rejects implicit trust based solely on network location and frames authentication and authorization as per-resource decisions. Apply that principle to adapters and command requests; it is not a product certification.

## Resilience and exit

Document adapter, broker, database, search, identity provider, mapping service, rules engine, client, WAN/cloud, time, licence, and source-system failures. State what continues natively, what becomes stale, what queues, what is lost, and how recovery avoids duplicates or silent gaps.

The native security systems should retain their approved essential operation if the integration layer fails. Maintain tested configuration, mapping, workflow, audit, case, and evidence export; document migration and vendor/service termination so the platform does not become the sole undocumented memory of operations.

## Acceptance evidence

- complete source/target inventory, authorities, service identities, scopes, and dependency graph;
- field-by-field mapping with unknown/stale/conflict behavior;
- representative ordering, duplicate, loss, reconnect, failover, and clock cases;
- role/tenant isolation and privileged-action evidence;
- command request through physical telemetry without inferred success;
- native operation during platform failure and reconciled recovery;
- privacy, retention, audit integrity, evidence export, backup, restore, and exit.

See [Integration platforms](README.md), [SIEM, SOAR, and case management](siem-soar-and-case-management.md), and [BMS and SCADA integration](bms-and-scada-integration.md).

