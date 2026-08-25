---
title: PACS Architecture
summary: Authority, entities, decision flow, planes, availability, federation, and integration boundaries in physical access-control systems.
page_type: system
domains: [access-control, identity]
tags: [pacs, architecture, access-decisions, federation]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 60839-11-1:2013", ONVIF Profiles A C D]
coverage_limit: Generic architecture; access policy, door hardware, emergency behavior, privacy, and exact product capabilities require local authority and product verification.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# PACS architecture

A physical access-control system (PACS) manages identities/credentials, policies, controllers, access points, alarms, and audit. The central database is not always the real-time decision authority: field controllers commonly cache policy and continue locally during server/network loss.

## Components and authority

| Component | Usually authoritative for | Not proof of |
|---|---|---|
| HR/identity source | Person/work relationship attributes | Physical-access authorization |
| PACS service/database | Credential assignments, schedules, access levels/rules, logical topology | Controller received/current policy |
| Field controller/panel | Local cached decisions and door logic | Actual lock movement or passage |
| Reader/peripheral | Credential transaction and user feedback | Person identity or granted access |
| Door inputs/monitors | Contact/lock/RTE states as wired | Complete physical security condition |
| Operator/integration | Requests, overrides, workflow | Safe physical outcome |

## Decision flow

```text
presentation -> reader/card/mobile authentication -> controller lookup/policy
 -> grant/deny decision -> output/lock timing -> door/passage observations
 -> event/audit -> central reconciliation and response
```

Record each stage. Never collapse `valid credential`, `access granted`, `unlock commanded`, `door opened`, and `passage completed` into one event.

## System planes

- **Policy/identity:** people, credentials, groups/access levels, schedules, areas, anti-passback, risk/escort rules.
- **Control:** momentary unlock, lockdown/secure modes, output control, credential update, panel commands.
- **Observation:** access decisions, door/lock/RTE/tamper/power/communication state, occupancy estimates.
- **Management:** topology, firmware, users/roles, keys/certificates, time, backup, controller downloads.

Use distinct roles/accounts/interfaces. A reporting integration should not inherit unlock or firmware authority.

## Standards

[IEC 60839-11-1:2013](https://webstore.iec.ch/en/publication/3662) publicly scopes minimum functionality/performance/test requirements for electronic access-control systems and components, including logging and information control. ONVIF [Profile A](https://www.onvif.org/profiles/onvif-profile-a/) covers credentials, schedules, access rules, status, and events; Profile C covers basic door/events; Profile D addresses peripherals. Verify exact device/client roles, profile conformance, and conditional features.

## Availability and reconciliation

Define behavior when server, database, message bus, identity provider, network, time, license, WAN/cloud, or controller fails. Record:

- controller cache content/version/expiry and download acknowledgement;
- offline credential/policy behavior and locally queued event capacity;
- server/controller sequence or checkpoint and gap handling;
- configuration conflict authority after reconnect;
- alarm/door operation independent of enterprise services;
- recovery of certificates, time, keys, database, and controller firmware.

A central “successfully downloaded” state should be reconciled against controller version/status. Stale cached access can be both an availability feature and a revocation risk.

## Federation and multi-site

Use globally stable site/controller/access-point/credential identifiers and scope all authorization by tenant/site. Decide whether a central system is authoritative or a federation overlay. Prevent one site's integration credentials or automation rules from addressing another site by numeric-ID collision.

## Security/privacy

PACS data reveals identity, movement, schedule, employment, and sensitive-area access. Minimize exports; use opaque IDs; restrict reports; protect backups; define retention and subject processes. Audit policy/credential changes, overrides, break-glass, denied admin actions, controller downloads, and support access.

Return to [Access-control systems](README.md).
