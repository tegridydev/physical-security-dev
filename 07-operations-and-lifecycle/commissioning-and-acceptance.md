---
title: "Commissioning and acceptance"
summary: "A controlled, evidence-led transition from delivered components to an accepted physical-security integration."
page_type: operations
domains:
  - operations
tags:
  - commissioning
  - acceptance
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-82 Rev. 3"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Commissioning and acceptance

[Home](../README.md) / [Operations and lifecycle](README.md) / Commissioning and acceptance

Commissioning proves that the installed, configured and integrated system matches the versioned design and behaves predictably in normal, denied, degraded and recovery scenarios.

> Commissioning authority comes from the system owner and applicable local authority. High-impact and regulated functions also require manufacturer procedures, qualified personnel, local approvals, and an isolated or controlled acceptance window.

## Commissioning sequence

1. Verify asset identity, provenance, hardware, firmware, licences and physical installation records.
2. Establish isolated ownership and remove defaults using the [secure onboarding](../06-security-and-assurance/secure-commissioning-and-onboarding.md) state model.
3. Apply and record approved protocol, network, identity, certificate, time, logging, storage and update baselines.
4. Confirm only designed flows and roles are enabled.
5. Validate each integration with synthetic or non-actuating cases first.
6. Validate authorization denials, malformed input handling, timeouts, retries, duplicate/replay behavior and safe failure.
7. Validate failover, offline operation, queue/storage limits, reconnection and state reconciliation.
8. Validate monitoring, audit correlation, backup and recovery.
9. Resolve deviations or document explicit accepted limitations.
10. Capture the system-owner-approved acceptance record and handover material.

## Protocol acceptance record

For every interface record client/server/device roles, standard/API revision, optional features, secure mode, certificate identities, accounts/roles, addresses/ports, discovery, timeouts, retries, event ordering, scale, error cases, evidence location, exact validation endpoints, and observed environment result.

## Safety separation

Validate software integration without bypassing independent hardware interlocks or certified local control. Do not generate dispatchable monitoring events, unlock occupied-site doors, move gates/elevators, alter fire interfaces, silence alarms, or energize outputs as a generic documentation test. Use manufacturer-approved simulated/test modes and site procedures.

## Handover package

- as-built architecture, inventories and schedules;
- configuration and approved deviation records;
- credential, certificate and key custody without secret disclosure;
- support and escalation contacts;
- update, backup, restore and decommissioning procedures;
- monitoring and runbooks;
- environment-validation scope, results, approval, and limitations;
- outstanding defects, risks and review dates.

## Sources

- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], lifecycle, architecture, testing and safety considerations, accessed 2026-08-25.

[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## Related pages

- [Site survey and design records](site-survey-and-design-records.md)
- [Asset and configuration inventory](asset-and-configuration-inventory.md)
- [Defensive labs](../08-defensive-labs/README.md)
