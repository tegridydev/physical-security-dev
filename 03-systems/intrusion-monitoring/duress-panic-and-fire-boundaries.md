---
title: Duress, Panic, and Fire System Boundaries
summary: High-consequence authority, presentation, integration, and failure boundaries for hold-up, duress, panic, fire, and evacuation-related events.
page_type: system
domains: [alarms, access-control, intercom, building-industrial, operations]
tags: [duress, panic, hold-up, fire-boundary, emergency-response]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 62642-1:2010", "ISO 7240-19:2007"]
coverage_limit: Integration boundary only; no activation, concealment, reset, release, evacuation, emergency-services, or jurisdiction-specific life-safety procedure.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Duress, panic, and fire system boundaries

Hold-up, duress, panic, fire, and evacuation events can look similar in a common user interface while carrying very different activation, disclosure, routing, reset, and regulatory requirements. Normalize for correlation only; preserve the native class and authority.

## Authority boundary

```text
approved initiating system -> native control/indication -> approved transmission
                         \-> read-only integration event -> correlation/presentation

common platform: observe, associate, display, audit
native safety/security system: detect, supervise, decide, control, reset
authorized responder/AHJ: response and operational authority
```

An integration platform must not become the hidden sole path for a required alarm, evacuation warning, door release, or emergency response unless the complete design is expressly assessed and approved for that role. Convenience integrations never override the certified/native system or the authority having jurisdiction.

## Preserve event meaning

Maintain separate types for intrusion, hold-up/duress, panic/assistance, fire alarm, fire fault, supervisory condition, evacuation message, medical/welfare request, tamper, test, and restore. Retain source, native code, location, activation time, receive time, presentation time, acknowledgement layer, confidentiality class, and response policy version.

For silent or covert events, restrict names, maps, notifications, audio, device indicators, and audit access according to the approved threat model. Do not add UI confirmation, audible feedback, or broad mobile push notifications without safety review.

## Fire and evacuation boundary

Fire detection/alarm, smoke control, evacuation sound, lifts, door release, and building controls have jurisdiction-specific cause-and-effect, survivability, monitoring, inspection, and approval requirements. A security platform may consume approved read-only indications, but should present source authority and stale/failed integration clearly.

Never infer that `alarm restored`, `panel reset`, or `integration acknowledged` means a building is safe or evacuation can end. Do not combine fire and security silence/reset controls behind one generic action.

[ISO 7240-19:2007](https://www.iso.org/standard/42979.html), confirmed by ISO in 2025, covers design, installation, commissioning, and service of sound systems for emergency purposes; local adoption and rules still control. The broader fire design must be handled by competent, authorized practitioners.

## Access-control interaction

Emergency unlocking, egress, muster, lockdown, and shelter-in-place can conflict. The approved life-safety and security cause-and-effect matrix must state command authority, hardwired/native dependencies, fail state, manual override, restoration, and audit behavior for each opening. A head-end map or occupancy estimate is not a certified evacuation count.

See [Locks, egress, and life safety](../access-control/locks-egress-and-life-safety.md) and [Emergency phones, mass notification, and PA](../intercom-and-emergency-communications/emergency-phones-mass-notification-and-pa.md).

## Integration acceptance evidence

- approved event taxonomy and confidentiality classification;
- native-versus-integrated indication and acknowledgement semantics;
- end-to-end latency, ordering, duplicate, loss, and recovery behavior;
- clear degraded state if source, network, middleware, or client fails;
- role-restricted viewing, notification, acknowledgement, and export;
- coordinated test plan that protects live emergency response;
- approval owner, local obligations, and change-control boundary.

Coordinate all acceptance tests with the system owner, monitoring organization, emergency stakeholders, and applicable authority so test events cannot produce an unintended response.

## Source baseline

[IEC 62642-1:2010](https://webstore.iec.ch/en/publication/7298) includes intrusion and hold-up alarm systems within its scope. It does not turn a general integration platform into a fire or emergency authority. Obtain applicable local codes, approved design documentation, and normative standards before implementation.

Return to [Intrusion and monitoring systems](README.md).
