---
title: Ademco Contact ID and SIA DC-05
summary: Developer reference for the fixed-format DTMF alarm reporting protocol standardized by SIA.
page_type: protocol
domains: [alarms]
tags: [sia, dc-05, contact-id, dtmf, legacy]
scope: global
content_status: maintained
technology_status: legacy
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: [SIA DC-05-2016-DCS Ademco]
coverage_limit: Public SIA catalog material was reviewed; exact tones, timing, checksum, event codes, and handshakes require the purchased normative standard.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Ademco Contact ID and SIA DC-05

[Home](../../README.md) / [Protocols](../README.md) / [Alarm monitoring](README.md) / Contact ID

Ademco Contact ID is a fixed-format alarm reporting protocol that uses DTMF tones between an alarm communicator and central-station receiver. SIA's catalog lists **DC-05-2016-DCS Ademco** and states that the standard covers handshake timing, data structure, error detection, and event codes.[^sia-dc05]

## Message semantics

A Contact ID integration commonly needs to retain these conceptual fields:

```text
subscriber account
message type
event qualifier: new event / restore / status
event code
partition or area
zone, user, or device reference
transmission check result
```

The exact symbol positions, tone timing, handshake and kissoff behaviour, checksum calculation, and code tables are normative. Implement them only from the licensed standard and the receiver/panel documentation. Do not copy a field layout from an arbitrary web table: numerous products describe proprietary prefixes, relaxed timing, or receiver-specific mappings while still using “Contact ID” as a marketing label.

## Receiver pipeline

```text
panel event
   ↓
communicator encodes DTMF
   ↓
receiver handshake → message → validation → kissoff
   ↓
receiver-to-automation mapping, often DC-07 or vendor API
```

A kissoff confirms the receiver's protocol state, not that monitoring automation stored or acted on the event. Keep telephony/audio detection, Contact ID parsing, receiver acknowledgement, automation delivery, and operator handling as separate audit milestones.

## Implementation controls

- Model the account, event code, qualifier, partition, and zone/user as typed identifiers; retain leading zeroes.
- Treat restore and new-event qualifiers as materially different events. Never infer restore from silence.
- Bound repeated-handshake and redial behaviour to prevent storms while still meeting the panel and receiver's supervised-delivery requirements.
- Preserve unknown event codes and vendor extensions without assigning a misleading generic meaning.
- Record the receiver's measured timing and signal-quality diagnostics separately from semantic validation.
- Make duplicate delivery idempotent downstream: telephony retry and receiver failover can produce equivalent reports.

## Security model

Contact ID has no modern confidentiality, cryptographic sender authentication, command authorization, or replay protection. DTMF checks and checksums address transmission errors, not malicious forgery. Subscriber account knowledge must not be treated as a secret authenticator.

Keep analogue/VoIP gateways, receivers, and automation interfaces segmented; protect receiver management; constrain account routing; alert on impossible source/account combinations and repeated invalid reports; and prefer a modern authenticated alarm-transport profile when both endpoints and regulatory context support it.

VoIP conversion can alter timing, tone quality, compression, echo cancellation, and packet-loss behaviour. A call completing is not evidence that Contact ID was decoded correctly. Validate the exact panel, communicator, carrier/gateway, codec configuration, receiver, and firmware under the user's controlled process.

## Safety boundary

Never place a test call to a production receiver or use a real subscriber account. Even malformed or replayed tones can be interpreted as a valid alarm. Synthetic receiver testing remains the user's responsibility and must be isolated from dispatch automation.

## Primary source

[^sia-dc05]: Security Industry Association store, [SIA DC-05-2016-DCS Ademco](https://mysia.securityindustry.org/ProductCatalog/Product.aspx?ID=16370), reviewed 2026-08-25. See also SIA's [standards index](https://www.securityindustry.org/industry-standards/at-a-glance-guide-to-sia-standards/).
