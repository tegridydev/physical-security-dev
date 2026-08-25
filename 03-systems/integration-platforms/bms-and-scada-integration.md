---
title: BMS and SCADA Integration
summary: Safety-conscious observation and control boundaries between security platforms and building-management or industrial-control systems.
page_type: system
domains: [bms, ot, integration, building-industrial]
tags: [bms, scada, ot, building-automation, cross-domain-integration]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [NIST SP 800-82 Rev. 3]
coverage_limit: Defensive architecture only; no register/object writes, live commands, controller logic, safety function, process setting, commissioning procedure, or site-specific cause-and-effect.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# BMS and SCADA integration

Building-management and industrial-control systems affect real processes: HVAC, power, water, smoke control, lifts, machinery, environmental conditions, and other services. Security integration should default to constrained, observable exchange. A common dashboard never becomes engineering or safety authority by presentation alone.

## Boundary architecture

```text
native controller/process <-> native supervisory system and approved safety logic
              |
        bounded gateway/DMZ or broker
              |
     read-only events/state/trends -> security correlation
     separately approved semantic request <- constrained workflow
```

Prefer native, supported integration interfaces and a broker/gateway over direct controller access. Keep management and control networks separated according to risk and necessary flows. Avoid dual-homed general-purpose hosts that bypass the boundary design.

## Authority map

| Information/action | Authority |
|---|---|
| process value and quality | field/controller/native supervisory path |
| safety interlock and protective action | approved native safety/control design |
| engineering units, scaling, alarms, limits | native engineering configuration |
| security event/case | source security system and operations workflow |
| cross-domain correlation | integration platform, clearly marked derived |
| command or set-point change | separately authorized control workflow; never inferred from dashboard access |

Security staff visibility does not imply permission or competence to operate plant. OT staff visibility of a security event does not grant access-control, alarm-reset, or surveillance authority.

## Point and event semantics

For every exchanged point retain native object/address reference, human meaning, source, units, scale, range, enumerations, read/write capability, quality/status, sample/update mode, source time, receive time, maximum age, deadband, alarm semantics, and mapping version.

Distinguish commanded value, controller-accepted value, feedback/process value, alarm state, acknowledgement, inhibit/override, maintenance, and communication failure. A successful protocol response or write acknowledgement does not prove plant movement or desired physical outcome.

When mapping BACnet, Modbus, OPC UA, KNX, DNP3, or other protocols, use their own security and semantic limits. See [Building and industrial protocols](../../02-protocols/building-and-industrial/README.md). Protocol normalization must not discard native quality, type, units, or security context.

## Approved use patterns

Lower-risk examples include receiving equipment fault, environmental, power, or room-condition observations for correlation; publishing a constrained security status to an authorized native consumer; and associating incidents with approved trend data.

Higher-risk patterns requiring explicit engineering, safety, and operational approval include changing set-points or modes, suppressing alarms, starting/stopping equipment, smoke-control interaction, lift commands, door/gate release, power switching, and automated cross-domain cause-and-effect. This page provides no implementation procedure for them.

## Cybersecurity and resilience

- Inventory assets, firmware/software, protocols, data flows, owners, remote access, and unsupported dependencies.
- Authenticate users and workloads; restrict service identities to exact objects/operations.
- Make read-only technically enforced where only observation is intended.
- Use controlled remote access with approval, monitoring, time bounds, and revocation.
- Protect engineering configuration, logic, backups, keys/certificates, and update paths.
- Monitor gateway health, stale points, rejected/unauthorized requests, configuration drift, time error, and unexpected write capability.
- Design for safe native operation if the security platform, gateway, identity service, WAN/cloud, or time source fails.

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) describes OT security while recognizing performance, reliability, and safety requirements; its scope includes building automation and physical access systems. Apply it with the site's engineering and safety obligations.

## Change and validation boundary

Maintain a signed-off data-flow and point list; owner for every mapping; approved direction; configuration/version evidence; rollback; maintenance window; and post-change review. Validate in an authorized environment and coordinated site process, including stale data, loss, partial failure, recovery, and native fallback.

Keep exploratory validation disconnected from live controllers, plant, fire/smoke control, lifts, locks, gates, relays, and safety functions. Coordinate any physical acceptance activity through the site change and safety process.

## Questions before connection

- Is the business purpose achievable with one-way/read-only data?
- Which system is authoritative for each value and decision?
- Are units, quality, source time, stale state, and override visible end to end?
- What common dependencies or new remote paths does the gateway create?
- Can either side continue safely and securely when the integration is wrong or unavailable?
- Who approves, observes, reverses, and investigates every privileged change?

See [Integration platforms](README.md) and [Gates, barriers, and vehicle access](../perimeter-and-detection/gates-barriers-and-vehicle-access.md).
