---
title: Physical-Security Systems
summary: System-level architecture, authority, data/control planes, failure modes, and integration boundaries across physical security.
page_type: index
domains: [video, access-control, alarms, intercom, bms, ot, identity, cross-domain]
tags: [systems, architecture, navigation, integration]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [IEC 62676 series, "IEC 60839-11-1:2013", IEC 62642 series, IEC 62820 series]
coverage_limit: System architecture and integration guidance; product behavior, site design, legal duties, and authority approvals require separate verification.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Physical-security systems

This section turns protocol knowledge into system models. Each page identifies which component is authoritative, separates observation from control and management, and makes ambiguous or degraded physical outcomes visible.

## Domains

- [Video surveillance](video-surveillance/README.md): cameras, video management, recording, analytics, PTZ, evidence, and health.
- [Access control](access-control/README.md): PACS, panels/readers/doors, locks and egress, pedestrian portals and turnstiles, credentials, biometrics, mobile access, offline policy, visitors, and lifts.
- [Intrusion and monitoring](intrusion-monitoring/README.md): panels, zones, sensors, communicators, receivers, supervision, verification, panic/duress, and fire boundaries.
- [Intercom and emergency communications](intercom-and-emergency-communications/README.md): call stations, media/routing, door control, emergency phones, public address, and mass notification.
- [Perimeter and detection](perimeter-and-detection/README.md): layered perimeter design, ANPR/LPR, radar, fence/buried sensors, gates, barriers, and vehicles.
- [Integration platforms](integration-platforms/README.md): PSIM/command platforms, BMS/SCADA, SIEM/SOAR, identity/HR/visitor, cloud/mobile, and multi-tenancy.

## Shared system model

```text
people / vehicles / environment
  -> sensors, readers, cameras, call stations, physical I/O
  -> controllers, panels, edge compute, recorders
  -> management platforms and integration gateways
  -> enterprise/cloud data, identity, response, and operator workflows
```

For every arrow document:

- actors, ownership, direction, protocol/profile/version, and trust boundary;
- entity IDs, event/state/command meaning, source and receive times, and provenance;
- authenticated user/device/workload, resource/site/tenant authorization, and audit;
- timeout, retry, sequence, duplicate, loss, offline, and reconciliation behavior;
- sensitive data, retention, disclosure, and physical consequence;
- supported versions, conformance evidence, lifecycle, and recovery.

## Four planes

| Plane | Examples | Rule |
|---|---|---|
| Observation | video, door state, alarms, health | Preserve provenance, quality, time, loss, and privacy |
| Control | unlock, PTZ, alarm acknowledge, gate command | Least authority, independent confirmation, safe ambiguity |
| Management | configuration, firmware, users, certificates | Separate privileged identity, change control, recovery |
| Bootstrap/discovery | enrollment, DHCP/DNS, discovery, key setup | Candidate discovery is not authenticated trust |

No protocol success response proves a safe physical outcome. See [physical-security system architecture](../01-foundations/physical-security-system-architecture.md), [events/state/commands/time](../01-foundations/events-state-commands-and-time.md), and [verification and safety](../00-start-here/verification-and-safety.md).

## Standards boundary

Official standards establish minimum/system/profile requirements, but adopted editions and local obligations differ. IEC catalogue summaries used here include [IEC 62676-1-1:2013](https://webstore.iec.ch/en/publication/7347) for video-surveillance system requirements, [IEC 60839-11-1:2013](https://webstore.iec.ch/en/publication/3662) for electronic access control, [IEC 62642-1:2010](https://webstore.iec.ch/en/publication/7298) for intrusion/hold-up systems, and current [IEC 62820-1-1:2026](https://webstore.iec.ch/en/publication/68745) for building intercoms. Normative texts are paywalled and this library does not reconstruct them.
