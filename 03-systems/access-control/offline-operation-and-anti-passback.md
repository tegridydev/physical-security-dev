---
title: Offline Operation and Anti-Passback
summary: Controller autonomy, cached policy, queued events, reconciliation, occupancy uncertainty, anti-passback modes, overrides, and recovery.
page_type: system
domains: [access-control]
tags: [offline, anti-passback, occupancy, controllers, reconciliation]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 60839-11-1:2013"]
coverage_limit: Semantic and resilience model; no site access, evacuation, occupancy, lockdown, or egress policy recommendation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Offline operation and anti-passback

Controllers often continue access decisions during server/WAN outage using cached credentials, schedules, and rules. That preserves availability but delays revocation and fragments global state. Design the tradeoff explicitly.

## Offline contract

For each controller/device define:

- cached entities/rules, capacity, version, download acknowledgement, and expiry;
- local clock/timezone/schedule behavior and time-loss handling;
- credentials/actions permitted or denied while isolated;
- local alarm/door logic and operator/manual functions;
- queued event count/bytes/age, overflow policy, sequence/session epoch;
- server command behavior during uncertain connectivity;
- reconnect authority and reconciliation.

Do not describe “offline capable” without these limits. A locally granted event may arrive centrally after an account was revoked; preserve source decision time and policy version.

## Anti-passback (APB)

APB uses entry/exit events to restrict repeated or directionally inconsistent credential use. Variants include hard deny, soft violation/event, timed APB, local-area, and global/federated APB. Define scope and authority.

APB state is an estimate, not proven occupancy. It can be wrong due to tailgating, missed presentation, manual/mechanical entry, door held open, emergency release, controller isolation, duplicate credential, reader direction error, event loss, or reset.

Never use APB/occupancy estimates as the sole source for evacuation accountability or life-safety decisions.

## State model

Track subject/credential separately and include area, direction, event/source, source time, controller epoch/sequence, policy/APB version, confidence/quality, and exception/override. `unknown` and `conflicted` are valid states.

When sites/controllers partition, global APB may be unavailable. Choose documented policy: local-only enforcement, soft violation, deny selected areas, or another risk-approved mode. Do not let stale central state silently override newer controller events.

## Reconciliation

```text
authenticate new session -> compare controller/config epoch
 -> retrieve ordered buffered events -> detect gaps/duplicates/resets
 -> merge by source authority -> surface conflicts/uncertainty
 -> re-download approved policy -> confirm -> resume global rules
```

Event receipt order is not occurrence order. Preserve corrections as appended facts rather than rewriting historical grants/denials.

## Overrides and reset

APB forgive/reset, emergency mode, bulk area reset, manual credential move, and cached-policy override are privileged operations. Require exact scope, reason, strong identity, audit, preview/confirmation for bulk action, and independent review where risk requires. An emergency reset should not erase the evidence explaining later inconsistencies.

## Acceptance scenarios

Environment acceptance should cover server/WAN/time loss, controller reboot, buffer full, revocation while offline, daylight-saving boundary, conflicting area events, duplicate/reordered events, global APB partition, reconnect, policy version mismatch, and emergency/manual entry. Preserve egress and site safety throughout testing and restoration.

## Source boundary

[IEC 60839-11-1:2013](https://webstore.iec.ch/en/publication/3662) provides the electronic access-control system context. Its public catalogue scope does not define a particular product's offline cache, anti-passback, distribution, or reconciliation behavior; verify those against exact product documentation and the approved site design.

Return to [Access-control systems](README.md).
