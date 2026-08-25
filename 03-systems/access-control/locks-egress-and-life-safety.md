---
title: Locks, Egress, and Life-Safety Boundaries
summary: Separating security locking, free egress, emergency release, fire interfaces, machinery, overrides, and software authority.
page_type: system
domains: [access-control, alarms]
tags: [locks, egress, life-safety, fire-boundary, emergency-release]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 60839-11-1:2013"]
coverage_limit: Boundary model only; no fail-safe/fail-secure selection, wiring, release sequence, code interpretation, or live actuation guidance.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Locks, egress, and life-safety boundaries

Security and life safety can require different behavior from the same opening. “Fail safe” and “fail secure” are hazard conclusions for a specific door and failure—not universal lock properties or synonyms for unlocked/locked.

## Separate functions

- entry authorization and security locking;
- required egress and accessibility;
- fire/emergency release or stair re-entry where applicable;
- lockdown/security emergency policy;
- mechanical key/manual override;
- powered-door/gate machinery safety;
- monitoring of door, latch/lock, power, and release circuits;
- operator and emergency-service procedure.

One software integration must not arbitrate these functions casually.

## Authority hierarchy

The authority having jurisdiction, adopted building/fire/egress/electrical/accessibility rules, approved fire strategy, door hardware schedule, and qualified designers determine required behavior. PACS logic implements only its approved part. A convenience API, VMS rule, BMS sequence, or cloud workflow cannot override independent required safety functions.

[IEC 60839-11-1:2013](https://webstore.iec.ch/en/publication/3662) addresses electronic access-control system/component scope, but local adopted codes and product listings govern openings. Generic release wiring or timing is unsafe; use the approved site design, listed product instructions, and applicable authority requirements.

## Boundary design

```text
PACS authorization -> security-control input
approved emergency/fire interface -> independently engineered release function
local egress hardware -> direct required egress path
monitor contacts -> observation only unless approved logic says otherwise
```

Document which system owns each output, the electrical normal/degraded states, priority, latching/reset, supervision, manual override, and evidence. Avoid undocumented parallel relays that make the effective logic impossible to prove.

## Software/integration rules

- Expose named operations such as an approved temporary access request, not unrestricted raw output control.
- Scope by site/door/action; require strong operator/workload identity and current authorization.
- For high-impact bulk/lockdown operations, use separate permission, target preview, reason, confirmation, dual control where required, and abort/recovery.
- Do not retry an indeterminate actuation blindly.
- Never infer safe physical state from response, lock-output bit, or door contact alone.
- Keep enterprise/cloud/analytics availability outside independent required egress/emergency paths.

## Degraded states

The approved design must cover loss of mains/battery/PoE, controller/server/network/time/identity, broken/shorted wiring, fire input fault, stuck relay, jammed hardware, door propping, mechanical override, and simultaneous emergencies. Monitor the layers without creating unsafe automatic correction.

## Change and testing

Any firmware, rule, integration, wiring, lock, door, fire-interface, or emergency-procedure change can alter the approved system. Physical acceptance testing requires written site authority, affected-person coordination, responsible fire/safety/security personnel, independent observation, emergency/egress preservation, abort criteria, manual override, and restoration evidence.

Return to [Access-control systems](README.md).
