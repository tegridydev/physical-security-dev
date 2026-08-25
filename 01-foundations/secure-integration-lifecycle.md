---
title: Secure Integration Lifecycle
summary: A decision and assurance lifecycle from use case and threat model through retirement.
page_type: foundation
domains: [cross-domain]
tags: [lifecycle, secure-development, threat-model, supply-chain]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [NIST SP 800-218, NIST IR 8259 Rev. 1]
coverage_limit: Framework-level guidance; project governance, regulation, and safety assurance remain local.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Secure integration lifecycle

Security is not a commissioning hardening step. The interface contract, failure model, support lifecycle, and recovery design determine much of the eventual risk.

## 1. Frame the outcome

Define users, sites, systems, data, physical effects, safety/privacy obligations, service levels, and explicit exclusions. Identify authoritative sources and who owns each decision. Separate observation from actuation and administration.

## 2. Inventory and research

Record exact products, hardware/firmware/software, protocols/editions/profiles/options, SDK/library versions, certificates/keys, licenses, cloud regions, dependencies, support/end-of-life, conformance evidence, and advisories. Public documentation gaps remain gaps; do not fill them with guessed endpoints.

NIST [IR 8259 Rev. 1](https://csrc.nist.gov/pubs/ir/8259/r1/final) (final April 2026) describes foundational cybersecurity activities IoT product manufacturers should perform before sale. Its lifecycle and customer-information framing is also useful when evaluating long-lived security devices.

## 3. Model threats and failures

Diagram actors, data/control paths, trust boundaries, and physical consequences. Consider spoofing, tampering, disclosure, replay, over-privilege, tenant/site confusion, unsafe actuation, privacy misuse, supply-chain compromise, outage, stale state, ambiguous retry, and loss of recovery capability.

## 4. Define contracts

Specify interface role, protocol/version, identity/authentication, authorization, schema/semantics, timestamp/provenance, delivery/order, bounds/rates, timeouts/retries/idempotency, degraded state, observability, privacy/retention, versioning, and decommissioning. Write acceptance evidence before implementation.

## 5. Build securely

Apply NIST [SP 800-218, Secure Software Development Framework 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) while tracking the published [SSDF work](https://csrc.nist.gov/projects/ssdf/publications), which lists version 1.2 as draft at this baseline. Pin and inventory dependencies; validate untrusted input; protect secrets; use least-privilege identities; keep secure defaults; make unsafe operations explicit; and provide diagnostic signals without leaking sensitive data.

## 6. Verify in layers

Perform static review, schema/parser negative cases, protocol state/error cases, authorization denials, certificate and clock lifecycle, reconnect/sequence gaps, bounded-load/backpressure, upgrade/rollback, backup/restore, and integration-owner-controlled isolated interoperability tests. Physical actuation needs a separate safety gate and independent observation. Assign `V3` only to the exact claims supported by accepted environment-validation evidence.

## 7. Commission deliberately

Change defaults and unique bootstrap secrets; enroll identities/certificates; restrict flows and egress; set trusted time; apply supported firmware; disable unused services; establish inventory/configuration baseline; verify logs/alerts; document recovery; and capture approvals. Preserve local safety functions and a manual/out-of-band path.

## 8. Operate and change

Monitor availability, freshness, time, certificates, keys/tokens, queues, denied operations, storage, power, version drift, and advisories. Reassess trust and semantic mappings after product, firmware, network, identity, cloud, or organizational change—not only after code changes.

## 9. Retire

Revoke device/workload/user credentials; remove trust anchors, DNS, routes, broker ACLs, webhooks, cloud tenancy, and support access; export/retain required evidence; securely erase secrets and personal data according to capability/policy; update inventory; and verify no orphaned automation still targets the asset.

## Exit criteria

An integration is maintainable when another authorized engineer can identify every dependency and authority, understand failure/physical effects, rotate credentials, upgrade or roll back, diagnose a gap, recover from outage, and retire the path without relying on undocumented knowledge.
