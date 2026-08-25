---
title: "Safety impact checklist"
summary: "A high-impact decision boundary that separates observation from actuation and requires qualified approval for physical, life-safety, electrical, legal, and emergency consequences."
page_type: guide
domains:
  - cross-domain
tags:
  - safety
  - observation
  - actuation
  - life-safety
  - egress
  - checklist
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "IEC 62443-3-3:2013"
  - "NIST SP 800-82 Rev. 3"
coverage_limit: "Decision and escalation framework only; it supplies no life-safety, egress, fire, electrical, functional-safety, building-code, dispatch, labor, privacy, accessibility, or legal approval."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Safety impact checklist

[Home](../README.md) / [Reference](README.md) / Safety impact checklist

> **Mandatory boundary:** observation and actuation are separate authorities. Observation can still affect availability, privacy, or load; actuation can create physical consequences even when an API calls it “test,” “momentary,” “acknowledge,” “reset,” “maintenance,” or “configuration.”

This checklist does not authorize any action. Defer life-safety, egress, fire, emergency communications, lifts, gates, locks, electrical work, dispatch, legal/privacy, accessibility, and regulatory decisions to the system owner, qualified designers/engineers, monitoring/emergency stakeholders, legal/privacy professionals, and applicable authority having jurisdiction (AHJ).

## First classify the capability

### Observation

Observation reads or receives data without an intended state change:

- health/status, configuration inventory, capabilities, counters, time, and logs;
- alarm/access/device events and current state;
- live or recorded video/audio/metadata;
- passive serial/network observation using an approved non-intrusive method;
- read-only directory, credential, door, sensor, BMS, or OT values.

Observation is **not impact-free**. A query can overload a controller; a subscription can exhaust queues; a media session can consume bandwidth; discovery can cause storms; live audio/video can violate privacy; a passive electrical tap can change bus loading; an acknowledgement-looking read may consume server state. Apply authorization, minimization, query budgets, isolation, and stop conditions.

### Actuation

Actuation requests, enables, suppresses, or changes state or behavior, including:

- unlock, release, lock, lockdown, gate/barrier movement, lift-floor access, door schedule or anti-passback changes;
- relay/output/GPIO activation, supervised-input bypass, zone inhibit/isolate, alarm arm/disarm, acknowledge/silence/reset;
- intercom call, listen/talk, DTMF function, paging, recorded announcement, emergency message;
- PTZ movement, preset/tour, privacy-mask change, focus/IR/heater/output, recording/retention deletion or export release;
- controller/BMS/OT write, BACnet priority write, Modbus write, OPC UA method, KNX group write;
- credential issuance/revocation, access-level change, biometric enrollment/deletion, key/trust change;
- firmware/configuration import, reboot/reset, PoE cycle, service stop, failover trigger, time set;
- callback/subscription/configuration change that enables a later physical command.

An action is still actuation when its effect is indirect, delayed, scheduled, queued, retried, routed through a vendor cloud, or performed by changing policy rather than driving an output.

## Classification matrix

| Class | Description | Examples | Minimum disposition |
|---|---|---|---|
| O1 — bounded observation | Read-only and expected to have low load/privacy consequence | Bounded health read, synthetic offline trace parsing | Named owner, least privilege, limits, privacy review, evidence |
| O2 — consequential observation | Sensitive, high-volume, topology-revealing, or potentially disruptive | Live audio/video, broad discovery, controller walk, evidence export | Explicit written authority, minimization, capacity plan, isolation/monitoring, stop rule |
| A1 — controlled operational change | Intended state change with bounded, reversible operational effect in exact approved context | Noncritical lab configuration on isolated synthetic system | Change control, separate actuator identity, preconditions, witness/telemetry, rollback and unknown-outcome plan |
| A2 — high-impact actuation | Can affect people, egress, security posture, alarm/dispatch, physical movement, evidence, electrical load, or safety system | Unlock/lockdown, gate/lift, relay, alarm silence/reset, credential revocation, PoE restart of security device | Qualified system/safety/legal/AHJ approval as applicable; production-like isolation; independent stop authority; no autonomous repository execution |
| Prohibited/unsupported here | No safe authority/evidence path or inherently out of scope for this KB | Bypassing certified fire/egress controls, testing real dispatch, undocumented live writes | Do not proceed; escalate to responsible qualified authority |

Classification follows consequence, not HTTP method, SDK function name, UI label, protocol, or duration.

## Observation checklist

- [ ] Read-only capability and credential are technically separate from write/admin/actuation
- [ ] Query/stream/subscription scope is the minimum resource, fields, resolution, duration, and rate
- [ ] Endpoint supports the requested load and bounded pagination/batch size
- [ ] Discovery/multicast/serial attachment cannot create storms, transmit unexpectedly, or alter electrical behavior
- [ ] Live/recorded video, audio, access, location, biometric, credential, and topology data have purpose/access/retention approval
- [ ] Logs and evidence redact secrets and unnecessary personal/security-sensitive fields
- [ ] Absence, stale state, unknown quality, clock error, and data gaps remain explicit
- [ ] Observation is not used as implicit authorization for a later command
- [ ] Stop on load increase, control latency, device instability, privacy scope breach, or unexpected state change

## Actuation preconditions

Do not expose or issue an actuation unless every applicable item has named evidence and approval:

- [ ] Exact target asset, physical location, controlled function/load, product/firmware, and current operating mode positively identified
- [ ] Requester, operator, service, device, and approving authority authenticated and separately authorized for this specific action/target/time
- [ ] Current authoritative state, freshness/quality, dependencies, interlocks, occupancy/human presence, and environmental preconditions verified by approved system logic
- [ ] Consequence analysis covers expected, duplicate, late, reordered, replayed, partial, failed, and unknown outcomes
- [ ] Retry policy is operation-specific; no blind retry after an ambiguous mutating result
- [ ] Competing controllers, BACnet priorities, schedules, anti-passback, emergency modes, local overrides, and manual controls understood
- [ ] Fail-safe/fail-secure terminology is defined for the exact opening/system and code context—not assumed from a label
- [ ] Positive physical completion evidence comes from the authoritative sensor/controller/process, not transport success alone
- [ ] Rollback/recovery is physically possible, authorized, time-bounded, and does not create a worse hazard
- [ ] Independent monitoring, human stop authority, communications, incident response, and audit are active

For any A2 capability, use an isolated owner-controlled setup with no live egress, dispatch, fire/life-safety, public, production, or connected hazardous load unless the responsible qualified authorities explicitly own a controlled commissioning/acceptance procedure. Such a procedure is site-, product-, jurisdiction-, and authority-specific and falls outside this global reference.

## Command lifecycle to preserve

| Milestone | Meaning |
|---|---|
| Authorized | Policy allowed the named principal to request the exact action |
| Submitted | Client sent or durably queued a request |
| Transport accepted | Peer/proxy acknowledged protocol receipt |
| Application accepted | Target service accepted syntax and current preconditions |
| Commanded | Controller attempted the output/state transition |
| Physically observed | Authoritative sensor/process reported a resulting state |
| Operator acknowledged | Human/workflow recognized the condition |
| Restored/reconciled | System returned to intended stable state and checked for divergence |

Never collapse these into one `success` flag. A timeout can leave outcome unknown; a `2xx`, SOAP response, MQTT acknowledgement, OSDP reply, BACnet SimpleACK, Modbus response, or gRPC `OK` does not by itself prove safe physical completion.

## High-impact domains and mandatory deferral

| Domain | Defer to and require |
|---|---|
| Doors, locks, egress, lockdown | Access-control owner, life-safety/egress designer, security operations, fire/code/AHJ authorities as applicable |
| Gates, barriers, turnstiles, lifts | Equipment manufacturer, qualified controls/safety engineer, site owner, accessibility/code/AHJ stakeholders |
| Fire, smoke control, emergency communications | Certified system owner/provider, fire engineer/service, emergency stakeholders, AHJ; never bridge around listed/certified behavior |
| Intrusion, duress, hold-up, medical, panic, dispatch | Monitoring center, response authority, subscriber/site owner, regulator/insurer as applicable; synthetic non-dispatch routes only for development |
| Electrical, PoE, relays, GPIO, batteries, mains | Manufacturer, qualified electrical designer/installer, applicable electrical/fire code and AHJ |
| Video/audio/biometrics/access history | Privacy/legal, workforce/union where applicable, security owner, evidence custodian, accessibility stakeholders |
| BMS/OT writes | Process/building owner, controls engineer, safety/environmental owner, change authority; preserve certified/local controllers |

“Global” documentation cannot decide these jurisdiction- and system-specific duties.

## Unsafe automation patterns

- Event normalization directly emits an unlock, lockdown, dispatch, silence, reset, or relay command.
- A generic retry library repeats a mutation after timeout.
- Health failure automatically power-cycles a device with no state/cooldown/consequence gate.
- A discovered address is trusted and immediately configured or controlled.
- A video analytic alone makes an irreversible/high-impact access or response decision.
- An MQTT retained message or stale cache is interpreted as fresh physical state.
- A credential/radio UID, RSSI, or raw UWB range is treated as sufficient authentication.
- A gateway maps unknown vendor alarm codes to the nearest high-priority standard meaning.
- A monitoring integration acknowledges/silences upstream merely because downstream storage succeeded.
- A “fail-open” software fallback is used to solve an availability problem without certified system authority.

## Stop conditions

Stop work and preserve evidence if:

- the target, connected load, physical effect, current state, or authority is ambiguous;
- production credentials, real subscriber/dispatch routes, real people, or live emergency systems appear in an intended lab path;
- a supposedly read-only tool changes configuration/state or creates material load;
- an action returns timeout/unknown outcome and safe physical state cannot be independently confirmed;
- interlocks, local controls, schedules, emergency override, or competing controller behavior differs from the approved model;
- certificate/identity, firmware, topology, wiring, power, or code status differs from the approved record;
- monitoring, communication, stop authority, rollback, or audit becomes unavailable;
- any person reports unsafe, inaccessible, coercive, privacy-invasive, or unexpected behavior.

## Review record

```text
capability and exact target:
classification: O1 | O2 | A1 | A2 | prohibited/unsupported
intended and worst credible physical effect:
data/privacy effect:
owner and approving authorities:
standard/product/configuration evidence:
isolation proof:
preconditions and interlocks:
authoritative completion evidence:
unknown-outcome and retry rule:
rollback/recovery and stop authority:
legal/AHJ/electrical/life-safety decisions (external references only):
environment-validation record and owner:
residual risk acceptance and expiry:
```

## Related pages

- [Integration readiness checklist](integration-readiness-checklist.md)
- [Events, state, commands, and time](../01-foundations/events-state-commands-and-time.md)
- [Dry contacts and supervised circuits](../01-foundations/dry-contacts-and-supervised-circuits.md)
- [PTZ and device I/O](../03-systems/video-surveillance/ptz-and-device-io.md)
- [Access-control system](../03-systems/access-control/README.md)
- [Authorized and safe use](../10-sources-and-maintenance/authorized-and-safe-use.md)

## Sources

- **NIST-OT** — [NIST SP 800-82 Rev. 3: Guide to Operational Technology Security][NIST-OT], NIST, September 2023; used for OT safety/reliability/security boundary context, not as site approval.
- **IEC62443** — [IEC 62443-3-3:2013, System security requirements and security levels][IEC62443], IEC; applicability and current amendments must be checked for the project.
- **SIA-OSDP-CHECK** — [Implementing OSDP Access Control? Follow This Simple Checklist][SIA-OSDP-CHECK], Security Industry Association, 10 February 2026.
- **ONVIF** — [ONVIF Network Interface Specifications][ONVIF], ONVIF, accessed 2026-08-25; capability semantics require exact service/profile/product evidence.

[NIST-OT]: https://csrc.nist.gov/pubs/sp/800/82/r3/final
[IEC62443]: https://webstore.iec.ch/en/publication/7033
[SIA-OSDP-CHECK]: https://www.securityindustry.org/2026/02/10/implementing-osdp-access-control-follow-this-simple-checklist/
[ONVIF]: https://www.onvif.org/profiles-specifications-new/
