---
title: "IEC 60839 alarm-transmission systems and IP messaging"
summary: "Developer reference for IEC 60839 alarm-transmission roles, system and transceiver requirements, IP message boundaries, and comparison with SIA DC-09."
page_type: protocol
domains: [alarms, networking]
tags:
  - iec-60839
  - alarm-transmission
  - alarm-receiving-centre
  - ip-messaging
  - supervised-path
scope: global
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "IEC 60839-5-1:2014"
  - "IEC 60839-5-2:2016"
  - "IEC 60839-5-3:2016"
  - "IEC TS 60839-7-8:2019"
coverage_limit: "Public IEC catalogue scope and system architecture only; licensed normative text, amendments, regional adoptions, conformity schemes, product profiles, and alarm-receiving-centre requirements are needed for implementation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# IEC 60839 alarm-transmission systems and IP messaging

[Alarm-monitoring protocols](README.md) / IEC 60839 alarm transmission

The IEC 60839-5 series addresses alarm-transmission systems between supervised premises and an alarm receiving centre. IEC TS 60839-7-8:2019 addresses a common message protocol for alarm transmission using Internet Protocol. The publications divide system performance, premises equipment, receiving-centre equipment, and protocol concerns; support for one part must not be represented as conformity to the entire path.

## Publication map

Status and scope below follow the IEC catalogue as reviewed **2026-08-25**.

| Publication | Scope in the family | Integration consequence |
|---|---|---|
| IEC 60839-5-1:2014 | General requirements for alarm-transmission systems | Evaluate the end-to-end path and declared performance, not only a packet format |
| IEC 60839-5-2:2016 | Requirements for the supervised premises transceiver (SPT) | Record the exact premises product role and conformity evidence |
| IEC 60839-5-3:2016 | Requirements for the receiving-centre transceiver (RCT) | Record the receiver role separately from monitoring automation |
| IEC TS 60839-7-8:2019 | Common alarm-transmission message protocol using IP | A Technical Specification has a different publication status from an International Standard; verify adoption, product profile, and current stability before specifying it |

The complete texts are paid IEC publications. Catalogue abstracts establish scope and lifecycle context, but not field encodings, timing values, classification criteria, conformance tests, or security mechanisms. Use licensed copies for engineering decisions.

## Roles and boundaries

```text
protected premises                                  alarm receiving centre

alarm system -> supervised premises transceiver -> transmission network
                                                        │
                                                        ▼
monitoring automation <- receiving-centre interface <- RCT
```

Important terms include:

- **alarm transmission system (ATS):** the system that conveys alarm information across the defined path;
- **supervised premises transceiver (SPT):** the premises-side transmission equipment;
- **receiving-centre transceiver (RCT):** the receiving-centre-side transmission equipment;
- **alarm transmission path:** the defined connection through the transmission system/network;
- **alarm receiving centre (ARC):** the organization/facility that receives and handles alarm information;
- **monitoring automation:** downstream software that presents, correlates, persists, and routes received events.

A communicator, gateway, receiver, and monitoring application may be sold as one product stack but remain different assurance boundaries. Network reachability, RCT receipt, protocol acceptance, automation ingestion, operator presentation, and response must be modelled separately.

## System view before message view

An alarm-transmission design should define:

- protected-premises and receiving-centre endpoints;
- single or diverse paths and their independence assumptions;
- transmission-network ownership and service boundaries;
- supervision, fault detection, reporting, restoration, and escalation;
- availability, transmission time, and other declared performance criteria;
- power, backup, clock, buffering, and behavior during extended outage;
- substitution, replay, redirection, tampering, and denial-of-service controls;
- commissioning, maintenance, change, and conformity evidence.

Do not infer system performance from nominal bandwidth, a successful connection, or one delivered test message. The declared classification and evidence must follow the exact IEC edition, regional adoption, product certificates, and installed design.

## IP message boundary

IEC TS 60839-7-8 belongs at the application-message layer. IP, TCP, UDP, TLS, mobile, or fixed networks provide lower-layer services according to the chosen profile; they do not supply alarm-event meaning or end-to-end outcome.

A defensive implementation record should identify:

- exact publication, regional profile, and vendor interoperability profile;
- transport and connection lifecycle;
- sender, receiver, account/object, message, and sequence identity;
- event vocabulary and how initial, repeat, update, fault, and restore are represented;
- application acknowledgement and negative-result semantics;
- timeout, retry, duplicate, delayed, reordered, and buffered-message behavior;
- maximum encoded and decoded lengths, field constraints, and parser rejection rules;
- security mode, peer authentication, confidentiality/integrity, replay protection, and key lifecycle;
- failover route and reconciliation when paths or receivers change.

Transport acceptance is not an alarm-protocol acknowledgement. Protocol acknowledgement is not automation persistence. Automation persistence is not operator handling or emergency response.

## Relationship to SIA DC-09

[SIA DC-09](sia-dc-09.md) also carries protected-premises alarm events to a central-station receiver over IP networks. The two references are not aliases.

| Question | IEC 60839 family | SIA DC-09 |
|---|---|---|
| Standards body | IEC | Security Industry Association / ANSI-approved SIA edition |
| System scope | IEC 60839-5 parts address ATS, SPT, and RCT requirements | DC-09 primarily specifies an IP event-reporting interface |
| Common IP message publication | IEC TS 60839-7-8:2019 | ANSI/SIA DC-09-2026 |
| Conformity claim | Must name applicable IEC parts, editions, regional adoption, product/system evidence | Must name DC-09 edition, payload profile, transport, receiver, and conformity evidence |

Some products or gateways may implement both. That does not imply field-level equivalence, bidirectional lossless conversion, or shared certification. For a gateway, publish an explicit mapping of account identity, event/restore semantics, timestamps, acknowledgements, retry state, encryption/security context, and every unsupported value.

## Reliability and duplicate handling

Alarm paths retry because loss and uncertain outcomes are expected. Preserve enough state to distinguish:

- a retransmission of the same application message;
- a repeated occurrence reported with a new identity;
- a late message buffered during outage;
- a restore paired to an earlier condition;
- the same event received through a diverse path;
- receiver failover followed by replay or state reconciliation.

Deduplication must not discard a genuine repeated alarm, and duplicate delivery must not create duplicate dispatch or operator action. Keep the bounded original evidence or a protected evidence reference, parsing result, receiver result, correlation, route, and timestamps according to privacy and retention policy.

## Security architecture

- Authenticate each SPT/RCT or gateway identity and bind it to permitted accounts, sites, paths, and message types.
- Do not use source IP, caller/network identity, or a syntactically valid account field as sole authorization.
- Use the exact approved security profile; reject silent downgrade and shared default credentials.
- Give every device/customer or suitably small security domain independently revocable keys or credentials where the normative profile permits.
- Protect provisioning, receiver routing, account mapping, key rotation, certificate trust, firmware, time, and remote management more strongly than ordinary read access.
- Segment event listeners from receiver management and monitoring-automation administration.
- Enforce connection, authentication, message, decoded-size, retry, and event-rate limits per authenticated source and tenant.
- Alert on path substitution, repeated integrity/decryption failure, sequence anomalies, unexpected payload type, clock discontinuity, route change, and prolonged supervision loss.

Encryption protects content only within its defined endpoints and key model. It does not prove that the event belongs to the claimed account, that automation handled it correctly, or that a response occurred.

## Failure and degraded states

Design evidence should address loss of primary/secondary network, DNS or addressing dependency, power/backup, SPT, RCT, automation, database, time source, certificate/credential service, and operator interface. Define:

- which events are buffered, their maximum count/age/bytes, and overflow behavior;
- failover ordering, backoff, route authorization, and split-brain prevention;
- supervision fault and restoration reporting;
- whether old alarms are replayed and how operators see their original occurrence time;
- how planned maintenance differs from an unplanned path failure;
- reconciliation after receiver or automation recovery.

Never generate a synthetic restore simply to clear a stale condition after outage.

## Verification and procurement evidence

Require evidence for:

- applicable IEC parts/editions, regional adoptions, product certificates, and declared system classification;
- SPT, RCT, network/path, automation, and service-provider ownership;
- exact message and transport profile, including optional features and maximums;
- normal, duplicate, delayed, reordered, malformed, unsupported, and over-limit message handling;
- acknowledgement, timeout, retry, buffer, diverse-path, failover, and recovery semantics;
- peer/account authorization, cryptographic profile, provisioning, rotation, revocation, and downgrade resistance;
- monitoring of path health, security anomalies, time quality, and receiver/automation handoff;
- explicit distinction among path availability, protocol acceptance, automation persistence, operator handling, and response.

Protocol fixtures should use synthetic accounts and an isolated receiver/automation environment with no dispatch connection. Operational alarm-path acceptance requires written authority from the premises and monitoring organizations, controlled change, responsible operators, abort/restoration criteria, and retained evidence.

## Primary sources

- IEC, [IEC 60839-5-1:2014](https://webstore.iec.ch/en/publication/3664), alarm-transmission systems general requirements.
- IEC, [IEC 60839-5-2:2016](https://webstore.iec.ch/en/publication/24120), supervised-premises transceiver requirements.
- IEC, [IEC 60839-5-3:2016](https://webstore.iec.ch/en/publication/24121), receiving-centre transceiver requirements.
- IEC, [IEC TS 60839-7-8:2019](https://webstore.iec.ch/en/publication/27073), common alarm-transmission protocol using IP.

Related SIA material: [SIA DC-09 IP event reporting](sia-dc-09.md), [SIA DC-07 receiver-to-automation](sia-dc-07.md), and [Contact ID / SIA DC-05](contact-id-sia-dc-05.md).
