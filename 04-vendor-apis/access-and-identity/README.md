---
title: Access and Identity APIs
summary: Catalogue of PACS APIs, mobile-credential services, identity provisioning surfaces, access-control SDKs, and event integrations.
page_type: index
domains: [access-control, identity, integration]
tags: [pacs-api, identity-api, mobile-credentials, access-sdk]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Capability and access-tier catalogue only; no page grants authority to issue credentials, change access, unlock doors, process biometrics, or bypass life-safety and privacy controls.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Access and identity APIs

[Vendor APIs](../README.md) / Access and identity

Access-control integrations cross multiple authorities: the identity source, PACS cardholder record, credential issuer, controller policy, reader transaction, lock/egress system, and audit trail. An API “success” proves only that the service accepted or completed its defined operation; it does not by itself prove a credential reached a handset, a controller received policy, a lock changed state, or a person passed through a door.

## Pages

- [HID Origo and Mobile Access](hid-origo-and-mobile-access.md)
- [Gallagher Command Centre integrations](gallagher-command-centre-integrations.md)
- [LenelS2 OnGuard, OpenAccess, and Elements](lenels2-onguard-openaccess-and-elements.md)
- [Johnson Controls C•CURE integrations](johnson-controls-ccure-integrations.md)
- [SALTO APIs](salto-apis.md)
- [Brivo API](brivo-api.md)
- [Suprema BioStar 2 API](suprema-biostar-2-api.md)
- [Kisi API](kisi-api.md)

## Separate these capabilities

| Capability | Required control |
|---|---|
| Identity/user synchronization | Authoritative-source rules, joiner/mover/leaver semantics, stable identifiers, conflict and deletion policy |
| Credential issue/revoke | Issuer authority, inventory/subscription, proof of possession, asynchronous delivery state, revocation recovery |
| Access assignment | Approval, effective interval, site/tenant scope, role separation, controller propagation and offline state |
| Events and occupancy | Duplicate/order/gap handling, privacy minimization, passage uncertainty, anti-passback semantics |
| Door/output/lockdown commands | Explicit high-impact privilege, preconditions, idempotency/uncertain outcome, local life-safety authority, immutable audit |
| Biometrics and photos | Lawful basis, consent where required, template/image minimization, retention, export/deletion, vendor and jurisdiction constraints |
| Mobile SDK | App signing, device integrity, keychain/keystore protection, lifecycle, offline behavior, reader proximity proof, accessibility |

## Safety boundary

Never exercise unlock, lockdown, elevator, output, alarm, anti-passback, or credential operations on a live site as exploratory testing. Door hardware, emergency egress, fire interfaces, and accessibility remain under qualified design and the authority having jurisdiction. Use a documented test tenant and physically isolated lab only under written authority from the integration and site owners.

See [PACS architecture](../../03-systems/access-control/pacs-architecture.md), [credential lifecycle](../../03-systems/access-control/credential-lifecycle.md), [mobile access](../../03-systems/access-control/mobile-access.md), [identity and authorization security](../../06-security-and-assurance/identity-authentication-and-authorization.md), and [privacy](../../06-security-and-assurance/privacy-and-sensitive-data.md).
