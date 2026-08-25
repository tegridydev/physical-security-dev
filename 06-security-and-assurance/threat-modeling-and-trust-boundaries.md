---
title: "Threat modelling and trust boundaries"
summary: "A repeatable threat model for physical-security protocol integrations and cyber-physical effects."
page_type: security
domains:
  - cross-domain
tags:
  - threat-model
  - trust-boundary
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

# Threat modelling and trust boundaries

[Home](../README.md) / [Security and assurance](README.md) / Threat modelling

Physical-security software crosses cyber and physical boundaries. A useful model follows an event from sensor or credential through field bus, controller, server, integration, operator, cloud, and actuator, and asks what happens if each assertion is forged, delayed, duplicated, disclosed, or lost.

> A software command that changes a lock, gate, alarm, elevator, public-address system, or emergency workflow is a high-impact actuation. Model the physical and life-safety consequence, not only the API response.

## Model scope

Record the exact boundary before listing threats:

1. Assets: live and recorded media, credentials, biometric templates, keys, configurations, event history, audit records, device firmware, availability, and safe physical state.
2. Actors: subject, operator, administrator, installer, service account, device, integration, vendor support, cloud service, monitoring centre, and attacker.
3. Entry points: field wiring, serial bus, Ethernet, wireless, discovery, web/API endpoints, media streams, removable storage, update channel, mobile application, and support tunnel.
4. Trust dependencies: DNS, DHCP, NTP/PTP, PKI, identity provider, broker, directory, vendor cloud, gateway, hypervisor, and power.
5. Physical consequences: unauthorized entry, entrapment, missed alarm, false dispatch, loss of evidence, privacy intrusion, unsafe movement, or loss of situational awareness.

## Trust-boundary map

| Boundary | Typical crossing | Questions |
|---|---|---|
| Credential to reader | NFC, BLE, UWB, card data | Is the presented identifier cryptographically authenticated, fresh, and bound to the holder? |
| Reader to controller | OSDP, Wiegand, vendor bus | Are endpoints authenticated; can the link be observed, replayed, downgraded, or substituted? |
| Device to management | HTTPS, ONVIF, SNMP, vendor API | Which identity is verified, and which operations are authorized? |
| Event to broker/platform | MQTT, WebSocket, webhook, DC-09 | How are origin, ordering, duplication, retention, and replay handled? |
| Media to recorder/client | RTP, RTSP, WebRTC, vendor stream | Are confidentiality, integrity, source identity, and session authorization preserved? |
| IT to OT/security zone | API gateway, directory, SIEM, remote support | Is policy narrow, observable, revocable, and safe when a dependency fails? |
| Software to actuator | Output, door, PTZ, alarm, gate | Is there an independent safety interlock and auditable authorization? |

## Abuse-case catalogue

For every data flow, evaluate:

- spoofing a device, user, credential, event source, time source, or broker;
- altering configuration, media, metadata, event codes, authorization, or firmware;
- replaying credentials, commands, events, tokens, packets, or old configuration;
- suppressing or delaying alarms, heartbeats, logs, recordings, or certificate warnings;
- exhausting connections, storage, queues, CPU, bandwidth, address space, or operator attention;
- crossing tenants, sites, roles, zones, or customer boundaries;
- using read access to infer occupancy, habits, identity, location, or sensitive facility layout;
- converting an integration failure into unsafe fail-open, fail-closed, or inconsistent state.

## Required outputs

A useful threat model produces more than a diagram:

- asset and data classification;
- authoritative source for each state item;
- trust-boundary and data-flow diagram;
- abuse cases with preconditions and physical impact;
- preventive, detective, and recovery controls;
- explicit assumptions and unsupported security properties;
- safe degraded modes and manual recovery path;
- testable requirements and evidence source;
- owner and review trigger for each accepted risk.

## Developer checklist

- Model the message before the endpoint: fields, identity, freshness, size, ordering, and allowed state transition.
- Separate transport authentication from command authorization.
- Treat time and sequence counters as hostile inputs until validated.
- Include bootstrap, reset, recovery, downgrade, compatibility, and offline modes.
- Model a compromised but correctly authenticated device.
- Model stale caches and split-brain states between controller, server, cloud, and mobile client.
- Ensure error and audit paths do not disclose secrets or sensitive physical context.

## Sources

- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], OT topology, threats, risk, reliability and safety guidance, accessed 2026-08-25.
- **NIST-800-154** — [NIST SP 800-154 Initial Public Draft: Guide to Data-Centric System Threat Modeling][NIST-800-154], unfinished draft from 2016; NIST's 2025 planning note says it intends to finalize the publication, accessed 2026-08-25.

[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final
[NIST-800-154]: https://csrc.nist.gov/pubs/sp/800/154/ipd

## Related pages

- [Segmentation and conduits](segmentation-and-conduits.md)
- [API and event security](api-and-event-security.md)
- [Resilience, backup, and recovery](resilience-backup-and-recovery.md)
