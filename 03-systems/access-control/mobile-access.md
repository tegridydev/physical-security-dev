---
title: Mobile Access Systems
summary: Provisioning, device binding, BLE/NFC/UWB presentation, reader decisions, phone lifecycle, privacy, offline use, and recovery.
page_type: system
domains: [access-control, identity]
tags: [mobile-credentials, ble, nfc, uwb, smartphones]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [Bluetooth Core Specification, NFC Forum Specifications, ONVIF Profile D]
coverage_limit: Architecture only; no vendor credential provisioning, radio capture/replay, wallet key, or product-security claim.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Mobile access systems

[Home](../../README.md) / [Access-control systems](README.md) / Mobile access

A mobile credential spans identity service, issuer/cloud, mobile OS/app/wallet, secure key storage, device/account recovery, radio presentation, reader/controller, and PACS authorization. “Uses BLE/NFC/UWB” describes transport/ranging, not the credential security protocol.

## Lifecycle

```text
identity + sponsor approval -> invitation/enrollment -> device/account binding
 -> credential/key provisioning -> reader presentation/ranging
 -> controller authorization -> renew/suspend/revoke -> device replacement/exit
```

Use a scoped opaque mobile-credential ID and bind subject, device/application instance, issuer, tenant/site, assurance, validity, and key/version. Avoid exposing stable radio/device identifiers in PACS or analytics.

## Presentation modes

- **NFC:** intentional close presentation/card emulation; application/card security is separate from radio distance.
- **BLE:** advertisement/connection/GATT or vendor protocol; pairing is not necessarily used or sufficient for access authentication.
- **UWB:** may provide more precise ranging, commonly combined with another discovery/credential channel; complete secure-ranging and fallback design matters.
- **QR/barcode/link:** camera/optical presentation can be convenient but requires freshness, signature, audience/site scope, and screenshot/forwarding controls.

Bluetooth SIG [adopted specifications](https://www.bluetooth.com/specifications/specs/) and NFC Forum [specifications](https://nfc-forum.org/build/specifications/) are the authoritative technology roots. Verify exact core/profile/application/release and product qualification; a phone supporting a core version does not prove credential behavior.

## Security model

- Generate/retain non-exportable keys in secure platform storage where supported; bind tokens to app/device/reader/session and prevent bearer reuse.
- Authenticate issuer, reader/controller, and mobile client; protect against replay, relay, downgrade, rogue reader, cloned app, rooted/compromised device, account takeover, and notification-link theft.
- Use short-lived enrollment/recovery artifacts, out-of-band approval, and server/PACS reconciliation.
- Define online/offline validation, revocation latency, clock requirements, and stale credential behavior.
- Avoid unlocking solely from RSSI or “phone nearby.” Separate authenticated credential, measured distance/uncertainty, user intent, and PACS policy.

## Privacy and usability

Radio scanning can track device presence. Rotate identifiers where supported, limit telemetry, do not use access scans for unrelated analytics, and explain permissions/background behavior. Provide accessible alternatives for dead battery, device loss, OS incompatibility, no smartphone, shared devices, and emergency egress.

## Reader and API integration

ONVIF Profile D includes mobile access peripherals in its public scope, but vendor credential protocols and wallets often remain proprietary. Treat the issuer/cloud as a critical dependency and document data residency, support access, tenant exit, credential export/non-portability, and reader firmware lifecycle.

## Recovery and decommission

Lost/replaced phone processes should revoke the old credential/device, invalidate pending invitations, re-proof the claimant, issue a new binding, reconcile offline controllers/readers, and alert on later use. At tenant/service exit revoke signing/issuer trust, remove integrations/keys, export required lifecycle audit, and confirm deletion.

## Related pages

- [Credential lifecycle](credential-lifecycle.md)
- [Credential formats and mobile credentials](../../02-protocols/access-control/credential-formats-and-mobile-credentials.md)
- [NFC, Bluetooth Low Energy, and UWB](../../02-protocols/access-control/nfc-ble-and-uwb.md)
- [Contactless and smart-card standards](../../02-protocols/access-control/contactless-and-smart-card-standards.md)
