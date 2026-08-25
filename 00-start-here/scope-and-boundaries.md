---
title: Scope and Boundaries
summary: Defines the subject, audience, exclusions, and jurisdictional limits of the knowledge base.
page_type: policy
domains: [cross-domain]
tags: [scope, safety, audience]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: Global technical guidance; local legal, licensing, electrical, fire, building, labour, and privacy obligations are not catalogued exhaustively.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Scope and boundaries

## In scope

This library covers software-development and integration knowledge for:

- network video, recording, analytics, metadata, and media transport;
- physical access control, readers, controllers, credentials, and identity exchange;
- intrusion, alarm transmission, monitoring, and verification interfaces;
- intercom, emergency communication, and associated real-time media;
- building automation and OT convergence where physical-security data or control crosses a boundary;
- supporting networking, discovery, messaging, identity, cryptography, time, serial, radio, and power technologies;
- secure design, defensive analysis, operations, lifecycle, and evidence handling;
- publicly documented vendor APIs, with exact product/version limits.

The intended reader is a developer, integrator, architect, defensive researcher, or technically minded operator working on systems they own or are explicitly authorized to assess.

## Out of scope

- Instructions to bypass access controls, clone live credentials, defeat alarms, evade detection, exploit production devices, jam radio, tamper with firmware, or create denial of service.
- Undocumented privileged vendor procedures, leaked SDK material, secret keys, production credentials, or private customer data.
- Site design sign-off, code compliance, emergency response policy, fire strategy, lock/egress specification, electrical design, or legal advice.
- A claim that any example is conformant, certified, interoperable, production ready, or suitable for a particular site.
- Product purchasing recommendations divorced from a current threat model, lifecycle commitment, and local supply/support context.

## Physical-effect boundary

Many “data” operations can change a physical state. A door-unlock API, relay write, PTZ movement, alarm inhibit, credential update, intercom call, BMS command, or PLC register write is an actuation path. Treat it as operational technology:

```text
software intent -> protocol request -> controller logic -> field output -> physical effect
```

Each arrow can transform, delay, reject, retry, duplicate, or partially apply the request. A successful HTTP response does not prove the safe physical outcome; a timeout does not prove the command was not applied.

This library therefore keeps examples involving locks, doors, gates, lifts, fire, alarms, emergency functions, lockdown, and relays conceptual or non-actuating. Site execution requires a named authority, isolation plan, affected-person coordination, independent observation, abort criteria, and recovery path.

## Jurisdiction and standards

Standards availability, privacy duties, biometric rules, surveillance notice, credential handling, retention, accessibility, emergency egress, fire interfaces, radio use, electrical installation, and trade licensing differ by jurisdiction and site classification. “Global” here means the technical concept is not written for one legal system; it does **not** mean the same deployment is lawful everywhere.

Before implementation, identify:

- the authority having jurisdiction and applicable adopted editions;
- contract, insurance, accreditation, and customer requirements;
- safety integrity and fail-safe/fail-secure decisions owned by qualified people;
- data-controller/processor roles, retention, disclosure, and subject-right processes;
- vendor support, warranty, certification, and conformance conditions.

## Research boundary

Defensive labs use synthetic/offline fixtures, loopback-only simulations, or user-controlled isolated equipment. Discovery or packet capture on a shared network is not assumed authorized. See [authorized and safe use](../10-sources-and-maintenance/authorized-and-safe-use.md).

