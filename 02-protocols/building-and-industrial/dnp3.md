---
title: DNP3
summary: DNP3 master/outstation data, event classes, time, unsolicited operation, Secure Authentication, and defensive integration.
page_type: protocol
domains: [ot, cross-domain]
tags: [dnp3, ieee-1815, telecontrol, secure-authentication, scada]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [IEEE 1815-2012]
coverage_limit: IEEE 1815 is normative and licensed; implementation subsets, device profiles, and current DNP Users Group technical documents are required for interoperability.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# DNP3

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / DNP3

DNP3 is a telecontrol protocol used between control centres, substations, outstations, gateways, and intelligent devices. It separates data-link, pseudo-transport, and application functions and supports static values, timestamped events, unsolicited responses, time synchronization, file transfer, and controls.[^overview]

**IEEE 1815-2012** remains the last published DNP3 edition, but IEEE now places it in the administratively inactive category because it passed the ten-year lifecycle without a completed revision. The superseding **P1815** project is an Active PAR/draft, not a published standard.[^ieee] This combination is why the page uses `technology_status: mixed`: the protocol remains deployed and a revision is active, while the published edition is administratively inactive. Do not present the draft or DNP Users Group next-generation security work as an approved replacement.

## Data contract

DNP3 points are typed by object/variation and index, not by a universal name. Record group/variation, index, class assignment, flags/quality, engineering conversion, event/deadband behaviour, timestamp provenance, static variation, event variation, and control authority. Preserve device flags and `online`, restart, communication-lost, remote-forced, local-forced, over-range, and reference-error semantics rather than flattening to a value.

Class 0 is an integrity/static poll convention; Classes 1–3 organize events. A robust master must plan integrity polls, event polls, buffer overflow recovery, restart indication, duplicate events, unsolicited enable/confirm, and stale data. Application confirmation is distinct from link acknowledgement and from physical operation.

For controls, model select-before-operate versus direct-operate, control code, count/on/off timing, status, timeout, and subsequent authoritative state. Never retry a non-idempotent control without knowing whether the outstation acted.

## Time and transport

DNP3 may run over serial or IP. Record link addresses independently from IP/serial addressing and enforce expected master/outstation roles. Time synchronization and device event timestamps require explicit accuracy, clock-quality, UTC/local handling, and correction policy; receipt time is not event time.

## Security

DNP3 Secure Authentication version 5 is included in IEEE 1815-2012 and authenticates critical operations at the application layer.[^sav5] It is not generic transport confidentiality. Confirm exact device support, user/key model, update-key lifecycle, challenge mode, protected operations, failure behaviour, and conformance subset. Segment and allowlist paths, protect engineering interfaces, authenticate remote access, and monitor restarts, time changes, unsolicited enablement, control attempts, authentication failures, and point-map/configuration changes.

The DNP Users Group describes ongoing work on DNP3-SA and a next-generation DNP3 Security Layer/Authenticated Messaging Protocol.[^cyber] Track it as development work until a published applicable edition and product support exist.

## Safety boundary

DNP3 controls can switch real equipment and affect utilities or site resilience. Use read-only, rate-bounded observation first; controls, time changes, cold/warm restarts, file transfer, or unsolicited reconfiguration require a separately approved, non-production acceptance process with independent safety observation.

## Primary sources

[^overview]: [DNP Users Group — overview of DNP3](https://www.dnp.org/About/Overview-of-DNP3-Protocol)
[^ieee]: [IEEE Standards Association — IEEE 1815-2012 status](https://standards.ieee.org/ieee/1815/6177/)
[^sav5]: [DNP Users Group — Secure Authentication version 5 overview](https://www.dnp.org/LinkClick.aspx?fileticket=XmRjAM35VxU%3D&forcedownload=true&mid=447&portalid=0&tabid=66)
[^cyber]: [DNP Users Group — cybersecurity program](https://www.dnp.org/Cybersecurity-Program)
- [DNP Users Group — protocol features](https://www.dnp.org/About/Features-of-DNP3)
- [DNP Users Group — testing policy](https://www.dnp.org/Products/Testing-Policy)
