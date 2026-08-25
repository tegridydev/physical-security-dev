---
title: "Access-control protocols and credentials"
summary: "Index for reader-controller links, contactless/smart-card interfaces, radio transports, and credential data models."
page_type: index
domains: [access-control, identity]
tags:
  - osdp
  - wiegand
  - smart-card
  - nfc
  - ble
  - uwb
scope: global
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: "Navigation, layer separation, and defensive defaults only; no credential, reader, controller, door, radio, key, or conformance behavior is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Access-control protocols and credentials

[Knowledge base](../../README.md) / Access-control protocols and credentials

This section separates four concepts that are often conflated: the reader-to-controller interface, the credential-to-reader radio/contact interface, the credential's application/data model, and the authorization decision made by the access-control system.

## Reading map

| Module | Coverage |
|---|---|
| [OSDP](osdp.md) | SIA OSDP 2.2.2, RS-485 topology, ACU/PD exchanges, Secure Channel, deployment, migration, and defensive diagnostics |
| [Legacy reader interfaces](legacy-reader-interfaces.md) | Wiegand signaling and bit formats, Clock-and-Data, limitations, compensating controls, and migration |
| [Contactless and smart-card standards](contactless-and-smart-card-standards.md) | ISO/IEC 14443, ISO/IEC 15693, ISO/IEC 7816, APDUs, applications, and secure messaging boundaries |
| [NFC, BLE, and UWB](nfc-ble-and-uwb.md) | Discovery, transport, ranging, version status, radio threat model, and access-system use |
| [Credential formats and mobile credentials](credential-formats-and-mobile-credentials.md) | Identifier layouts, smart credentials, public-key/mobile designs, lifecycle, privacy, and authorization mapping |

## System model

```text
person/device
    │ presents or proves possession
credential / secure element / mobile wallet
    │ contact, NFC, BLE, or UWB
reader or lock
    │ OSDP, legacy interface, IP, or vendor link
access-control unit / decision service
    │ events, policy, identity and audit APIs
management and identity systems
```

Security can be lost at any hop. A cryptographically strong credential sent as an unprotected static number over a legacy reader link has a weaker end-to-end result. Conversely, OSDP Secure Channel cannot repair a clonable upstream credential or an authorization policy that accepts stale identities.

## Engineering defaults

- Prefer OSDP Secure Channel on a supervised, segmented bus; use unsecured mode only for controlled initialization when required.
- Prefer credentials that perform challenge-response or signed proof over exposed, replayable identifiers.
- Treat a UID, CSN, serial number, facility code, card number, phone identifier, BLE address, or UWB range result as an input—not as authorization by itself.
- Bind proof to the intended reader/session and freshness context; reject replays and stale lifecycle state.
- Keep credential keys out of readers where a secure element or managed cryptographic boundary can hold them.
- Design issuance, activation, suspension, revocation, replacement, expiry, recovery, and audit before enrollment begins.
- Preserve life-safety egress and local code requirements independently from cyber controls.

## Safety and examples

This is a defensive developer reference. It does not provide credential-cloning, bypass, key-extraction, or unauthorized-entry procedures. Synthetic bit layouts and APDUs are for parser and data-model understanding only. Use implementation and validation techniques only on equipment you own or are explicitly authorized to test.

`V1` on this index is a manual documentation review. Child protocol pages use `V2` where claims were checked against official standards and program documentation. Product certification and site acceptance require the relevant standards body, manufacturer, laboratory, and local authority processes.
