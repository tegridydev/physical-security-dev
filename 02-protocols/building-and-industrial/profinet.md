---
title: PROFINET
summary: PROFINET roles, cyclic and acyclic communication, discovery, configuration, security classes, and safe deployment.
page_type: protocol
domains: [ot, cross-domain]
tags: [profinet, profinet-io, dcp, gsdml, industrial-ethernet]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [IEC 61158-5-10, IEC 61158-6-10, IEC 61784-2-3, IEC 61784-6-3, PROFINET V2.5]
coverage_limit: Normative protocol, security profile, certification, timing, and application-profile requirements are in PI/IEC documents and device GSDML files.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# PROFINET

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / PROFINET

PROFINET is PI's industrial Ethernet system. A typical PROFINET IO relationship has an IO Controller exchanging cyclic process data with IO Devices; IO Supervisors provide engineering/diagnostic functions. Acyclic records, alarms, configuration, neighbourhood discovery, and time-sensitive real-time profiles complement cyclic I/O.[^technology]

PI published the PROFINET V2.5 specification set in July 2026, including IEC 61158 service/protocol material, the IEC 61784-2-3 communication profile, and the IEC 61784-6-3 security profile.[^spec]

## Engineering identity

A project binds device name, IP configuration, station/slot/subslot/module structure, IO data layout, timing/update settings, alarm behaviour, and GSDML identity/version. Treat DCP discovery and name/IP assignment as commissioning operations, not routine unauthenticated inventory truth. An unexpected device with the expected IP is not automatically the engineered station.

LLDP neighbourhood, topology checks, diagnostics, and SNMP can assist operations, but each has its own trust and exposure. Protect engineering stations and controllers; a field-device web server or SNMP agent is not secured simply because the cyclic PROFINET channel is controlled.

## Real-time and state

Keep communication relationship state, cyclic data status, provider/consumer status, alarms, substitute values, application readiness, and physical process state separate. A healthy Ethernet link does not mean valid IO. Define stale thresholds and fail-safe/substitute behaviour in the controller and receiving security application.

Do not add SPAN taps, inline appliances, QoS changes, time-sync changes, or generic security inspection without validating latency, jitter, redundancy, and real-time class requirements. Network controls must preserve the engineered traffic model.

## Security profile

PROFINET conformance classes (such as A/B/C/E) describe functional/performance groupings and must not be confused with security classes. PI's security architecture defines security classes with increasing protections; exact mandatory behaviour depends on the applicable V2.5/IEC profile and product role.[^security]

Build defence in depth around zones/conduits, least-privilege controller/device relationships, authenticated engineering, signed/controlled configuration, device identity/certificate lifecycle where supported, secure-capable product profiles, event monitoring, and protected recovery. During migration, document every legacy endpoint and any secure gateway termination; a secure-capable controller cannot retroactively authenticate classic downstream peers.

## Safety boundary

PROFINET may carry motion, gate, lift, or process I/O. PROFINET/PROFIsafe and other functional-safety profiles have separate certified requirements; ordinary PROFINET data or network security does not create a safety channel. Validate DCP naming, controller relationships, cyclic I/O, alarms, fail-safe behaviour, and recovery on an isolated authorized bench.

## Primary sources

[^technology]: [PROFINET — technology description](https://www.profinet.com/profinet-explained/technology-description)
[^spec]: [PI — PROFINET V2.5 specification download](https://www.profibus.com/download/profinet-specification)
[^security]: [PROFINET — security architecture](https://www.profinet.com/profinet-explained/security)
- [PI — PROFINET security guideline](https://www.profibus.com/download/profinet-security-guideline)
