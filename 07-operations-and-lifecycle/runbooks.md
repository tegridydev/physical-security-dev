---
title: "Operational runbooks"
summary: "Safe diagnostic decision trees for common physical-security protocol and dependency failures."
page_type: operations
domains:
  - operations
tags:
  - runbooks
  - troubleshooting
scope: global
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Operational runbooks

[Home](../README.md) / [Operations and lifecycle](README.md) / Operational runbooks

These runbooks structure evidence collection and escalation. Any live-site action requires the applicable product procedure, local authority, system-owner approval, and controlled change record.

## Universal first response

1. Establish human and physical safety, required coverage and local authority.
2. Define affected sites, devices, functions, users, time range and first observation.
3. Preserve clocks, logs, configuration, alert history and recent changes.
4. Identify the failing layer: power/physical, link, address/routing, trust/authentication, protocol/session, application/state, storage/data, or external dependency.
5. Prefer read-only evidence and narrow containment.
6. Record each action, expected result, observed environment result, and accountable operator.
7. Stop if an action could actuate equipment, suppress signaling, erase evidence, break egress, or expand impact.

## Device offline or stream loss

- Check whether monitoring distinguishes power/link/device/application/stream failure.
- Compare device, switch/PoE, routing/firewall, DNS/time, certificate/authentication, VMS and storage evidence.
- Determine whether only one media profile, codec, multicast group, recorder or client is affected.
- Check configuration/change/reboot history and edge recording continuity.
- Do not reboot before preserving volatile evidence when compromise is suspected.

## Clock drift or certificate failure

- Compare UTC, offset, monotonic sequence and time-source state across affected components.
- Identify recent NTP/DNS/firewall/certificate/trust-anchor changes.
- Determine whether invalid time is causing certificate/token rejection or misleading event order.
- Do not disable validation. Restore trustworthy time/trust through the approved recovery path.

## Storage pressure or evidence gap

- Separate recording failure, indexing failure, retention deletion, export failure and playback failure.
- Preserve capacity, write errors, stream arrival, database/index, failover and deletion audit.
- Reduce nonessential load only through approved policy; never conceal loss of required recording.

## Controller, reader, or alarm path failure

- Establish door/alarm local state and responsible safety authority.
- Separate reader/field bus, controller, host, network, identity, event receiver and monitoring automation layers.
- Review supervision, polling, sequence/CRC, power, termination and recent configuration.
- Never generate dispatchable tests or change lock/alarm behavior without the approved site procedure.

## Credential compromise

- Identify credential type, holder/device, sites/doors, issuance system, mobile/cloud tokens and observed use.
- Suspend narrowly, preserve events/video/identity audit, rotate related secrets if exposed, and issue replacement through the authoritative process.
- Search for duplicate/replay or anomalous use without publishing raw credential values broadly.

## Vendor-cloud outage

- Confirm supplier status through an independent channel and identify affected region/tenant/service.
- Determine retained local operation, cached authorization, queues, data loss risk and safe duration.
- Prevent reconnect storms or insecure fallback.
- Preserve queued-event reconciliation evidence and validate state after recovery.

## Local adaptation and validation

Convert each decision tree into a product- and version-specific local runbook with exact authority, evidence sources, stop conditions, recovery actions, and escalation contacts. Validate it in a representative controlled environment and retain the result as `partially-runtime-validated` or `runtime-validated` evidence under the repository verification policy.

## Related pages

- [Monitoring and health](monitoring-and-health.md)
- [Incident response and evidence](incident-response-and-evidence.md)
- [Defensive labs](../08-defensive-labs/README.md)
