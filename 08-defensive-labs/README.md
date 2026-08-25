---
title: "Defensive labs"
summary: "Offline and simulated exercises for protocol interpretation, validation planning, hardening review, and incident reasoning."
page_type: index
domains:
  - defensive-labs
tags:
  - labs
  - defensive
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Defensive labs

[Home](../README.md) / Defensive labs

These labs are bounded research procedures based on synthetic fixtures, offline artefacts, calculations, or loopback simulation. They teach interpretation and evidence planning without requiring an operational system.

> Lab scope is limited to synthetic or sanitized offline artefacts, calculations, table-tops, simulated topologies, and local loopback simulation. External networks, operational systems, physical devices, real credentials, dispatchable alarms, and physical actuation are excluded.

## Lab classes

| Class | Meaning |
|---|---|
| Offline fixture | Embedded synthetic text/bytes; preferred |
| Calculation | Synthetic inputs evaluated with documented units, assumptions, and uncertainty |
| Tabletop | A paper scenario used to reason about roles, decisions, evidence, and recovery |
| Loopback simulation | Synthetic local components bound exclusively to operating-system loopback, with no route to an external network or device |
| Simulated topology | Invented components and flows documented without a network or device |

Physical hardware, field buses, devices, real brokers, monitoring receivers, service endpoints, and external networks are not lab classes. Use the separate commissioning and acceptance process for them.

## Labs

- [Authorization, topology, and safety](authorization-topology-and-safety.md)
- [Offline packet and trace reading](offline-packet-and-trace-reading.md)
- [TLS certificate-chain review](tls-certificate-chain-review.md)
- [ONVIF discovery and media-flow reasoning](onvif-discovery-and-media-flow.md)
- [RTSP/RTP/SDP trace analysis](rtsp-rtp-sdp-trace-analysis.md)
- [MQTT TLS and ACL review](mqtt-tls-and-acl-review.md)
- [WebSocket event-flow review](websocket-event-flow-review.md)
- [OSDP and Wiegand offline decoding](osdp-and-wiegand-offline-decoding.md)
- [SIA DC-09 validation planning](sia-dc09-validation-planning.md)
- [Modbus and BACnet interpretation](modbus-and-bacnet-interpretation.md)
- [Time drift and event correlation](time-drift-and-event-correlation.md)
- [SNMP and syslog health correlation](snmp-and-syslog-health-correlation.md)
- [Video bandwidth and storage calculation](video-bandwidth-and-storage-calculation.md)
- [Camera and controller hardening review](camera-and-controller-hardening-review.md)
- [Certificate rotation and restore tabletop](certificate-rotation-and-restore-tabletop.md)
- [Incident-response tabletop](incident-response-tabletop.md)

## Prohibited lab actions

- Internet or production scanning; brute force; password lists; credential harvesting.
- Card/credential cloning, live replay, bypass, evasion or jamming.
- Denial of service, exploit delivery, undocumented privileged APIs or firmware tampering.
- Unlocking/locking doors, moving gates/elevators, disarming/silencing alarms, energizing relays or generating monitoring-centre dispatch.
- Capturing or using traffic, media, credentials or personal data belonging to others.
- Connecting to physical devices, field wiring, real brokers, monitoring receivers, service endpoints, or any non-loopback network.

Owner-authorized physical acceptance is a separate activity governed by the [environment validation checklist](../10-sources-and-maintenance/manual-qa-checklist.md), manufacturer instructions, site change control, and the responsible safety or operations authority. It is not a defensive lab.

## Related pages

- [Reference examples](../05-development-and-integration/examples/README.md)
- [Security and assurance](../06-security-and-assurance/README.md)
- [Environment validation checklist](../10-sources-and-maintenance/manual-qa-checklist.md)
