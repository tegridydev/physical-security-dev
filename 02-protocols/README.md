---
title: Protocols
summary: Index of physical-security protocol families, transports, wire models, security properties, and implementation concerns.
page_type: index
domains: [cross-domain]
tags: [protocols, interoperability, navigation]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: Protocol-family navigation and cross-layer developer checklist; normative details remain in the linked standards and protocol pages.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Protocols

[Home](../README.md) / Protocols

This section treats a protocol as more than a port number or packet layout. Each reference separates the application semantics, message or object model, transport, discovery, identity, security, failure behaviour, conformance boundary, and physical consequence.

## Families

| Family | What it connects | Start here |
|---|---|---|
| Video and media | Cameras, encoders, recorders, VMS, analytics, intercom, and browser/cloud media | [Video and media](video-and-media/README.md) |
| Web and messaging | APIs, web services, event streams, brokers, and cloud integrations | [Web and messaging](web-and-messaging/README.md) |
| Access control | Readers, controllers, credentials, mobile devices, and field buses | [Access control](access-control/README.md) |
| Alarm monitoring | Premises transmitters, receivers, monitoring automation, and verification audio | [Alarm monitoring](alarm-monitoring/README.md) |
| Building and industrial | BMS, PLC, SCADA, gates, power systems, lifts, and field equipment | [Building and industrial](building-and-industrial/README.md) |
| Infrastructure | IP, discovery, time, administration, AAA, serial, wireless, power, and discrete I/O | [Infrastructure](infrastructure/README.md) |
| Interoperability and legacy | Cross-system models, identity synchronization, and legacy PTZ control | [Interoperability and legacy](interoperability-and-legacy/README.md) |

## Read protocol references in layers

```text
System outcome and safety state
            ↑
Application objects, events, and commands
            ↑
Session, transaction, retry, and discovery rules
            ↑
Security: identity, authorization, integrity, confidentiality
            ↑
Transport, network, data-link, and physical medium
```

A protocol at one layer does not inherit guarantees from a similarly named technology at another. TCP delivery is not application acknowledgement. TLS peer authentication is not command authorization. A valid checksum is not proof of an authorized sender. A successful API response is not proof that a lock, relay, camera, or alarm path reached the intended physical state.

## Developer checklist

Before implementing or selecting a protocol, establish:

1. The exact standard edition, profile, optional features, and vendor extensions at both endpoints.
2. Which endpoint is authoritative for identity, time, configuration, and physical state.
3. Message size, ordering, duplicate, retry, timeout, reconnect, and partial-failure behaviour.
4. How peers and users authenticate, how actions are authorized, and how keys or certificates rotate.
5. Whether the protocol protects confidentiality, integrity, freshness, and availability—or relies on a protected conduit.
6. Which actions are observational, configurational, or physically actuating.
7. What evidence is needed before claiming conformance or interoperability.

## Safety boundary

References in this section are explanatory. Do not send discovery, diagnostic, configuration, write, unlock, relay, reset, silence, acknowledge, or control traffic to a live system without authorization, an agreed change window, independent observation, and a recovery path. Keep fire, egress, duress, lockdown, lift, gate, and life-safety interfaces outside exploratory work.

See [verification and safety](../00-start-here/verification-and-safety.md), [secure protocol parsing](../06-security-and-assurance/secure-protocol-parsing.md), and [segmentation and conduits](../06-security-and-assurance/segmentation-and-conduits.md).
