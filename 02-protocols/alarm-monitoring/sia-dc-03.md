---
title: SIA DC-03 alarm event format
summary: Developer reference for the open-ended SIA digital communicator-to-receiver event format.
page_type: protocol
domains: [alarms]
tags: [sia, dc-03, alarm-format, receiver]
scope: global
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: [SIA DC-03-2017]
coverage_limit: Public SIA scope was reviewed; timing, frequencies, field grammar, checks, and event codes require the purchased normative standard.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# SIA DC-03 alarm event format

[Home](../../README.md) / [Protocols](../README.md) / [Alarm monitoring](README.md) / DC-03

SIA DC-03, commonly called the **SIA Format**, specifies digital communication between alarm transmitters and receivers. SIA's public page lists **DC-03-2017** and describes an open-ended block format with variable-length account and data sections, multi-block expansion, transmission rules, interpretation, and interoperability objectives.[^sia-dc03]

## Scope

DC-03 is an event-content and transmission format, not a modern secure network transport. It historically fits communicator-to-receiver paths and can also appear as payload content carried by IP alarm reporting products. When a product says “SIA,” determine whether it means DC-03 content, DC-09 IP transport, a vendor's subset, or merely a SIA event-code vocabulary.

```text
event source
   │  account + event blocks + protocol checks
   ▼
communicator ───────────────> receiver
```

## Developer data model

Do not map a received event directly to a free-form string. Preserve at least:

- protocol and edition;
- raw bounded message or protected evidence reference;
- account and receiver route as separate identifiers;
- event code and qualifier/condition;
- area/partition and zone/user/device references when present;
- occurrence time, receive time, and whether the timestamp came from the premises or receiver;
- block ordering and continuation state;
- integrity/check result, receiver response, and parser warnings;
- vendor extension namespace and original value.

Normalize into a canonical event only after retaining the source semantics. Unknown codes are valid evidence; they are not permission to invent a nearest known meaning.

## Parser requirements

- Bound the total message, block count, account length, field count, and numeric conversions before allocating storage.
- Implement the purchased edition's exact timing, framing, character, error-detection, and acknowledgement rules. Community summaries are insufficient for conformance.
- Treat incomplete multi-block messages as incomplete. Never emit a fully qualified alarm from a prefix unless the site's policy explicitly defines a safe degraded mapping.
- Preserve leading zeroes and identifiers as strings where the standard treats them as identifiers.
- Make duplicate and retransmission handling idempotent at the receiver/automation boundary.
- Reject malformed data deterministically and record a sanitized reason; never feed raw control characters into logs or operator displays.

## Security properties

DC-03's historical communication model does not itself provide modern peer authentication, authorization, confidentiality, or replay protection. Error detection protects transmission integrity against some accidental corruption; it is not a cryptographic authenticity check.

Use a protected, authenticated conduit where DC-03 is carried over IP, isolate receiver interfaces, authorize each account-to-source relationship, and detect duplicates, impossible sequences, and event-rate anomalies. If DC-03 content is transported in DC-09, apply [DC-09 security and retry controls](sia-dc-09.md) as well; do not assume the inner format becomes secure by association.

## Interoperability questions

Record supported DC-03 edition, event-code set, optional fields, maximum lengths, multi-block support, character/timing mode, receiver replies, restoration semantics, time-zone rules, and vendor extensions. The SIA public description explicitly expects manufacturer-to-manufacturer resolution for incompatibilities and provides a standards-subcommittee interpretation path.[^sia-dc03]

## Safety boundary

Use synthetic events on a non-dispatch receiver route. Parser tests must not dial or transmit to a production receiver. Panic, duress, hold-up, fire, medical, and restore events require monitoring-centre approval even in a nominal test account because automation rules may span accounts or receivers.

## Primary source

[^sia-dc03]: Security Industry Association, [DC-03-2017 — DCS SIA Format Standard](https://www.securityindustry.org/industry-standards/dc-03-2017/), reviewed 2026-08-25.
