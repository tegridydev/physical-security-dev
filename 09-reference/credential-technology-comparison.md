---
title: "Credential technology comparison"
summary: "A lifecycle- and proof-oriented comparison of identifiers, cards, mobile credentials, biometrics, and reader-controller preservation."
page_type: reference
domains:
  - access-control
  - identity
tags:
  - credentials
  - smart-cards
  - mobile-credentials
  - biometrics
  - comparison
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "ISO/IEC 14443 series"
  - "ISO/IEC 7816 series"
  - "FIPS 201-3"
  - "Aliro 1.0"
  - "PKOC 2.0.1"
  - "SIA OSDP 2.2.2"
coverage_limit: "Technology-family comparison only; assurance depends on the exact credential application, keys, reader, controller transport, identity proofing, lifecycle, certification, site policy, and environment evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Credential technology comparison

[Home](../README.md) / [Reference](README.md) / Credential technology comparison

> A carrier or form factor is not an assurance level. “Card,” “NFC,” “BLE,” “phone,” and “biometric” describe media or factors; the actual proof, cryptographic profile, issuer, reader validation, controller path, and lifecycle determine assurance.

## The complete decision chain

| Layer | Required question |
|---|---|
| Subject | Whose access is being decided, and how was that identity proofed? |
| Credential instance | What unique governed object was issued, to which subject/device, by which issuer? |
| Presentation | What medium and radio/electrical channel carried the exchange? |
| Proof | Static value, shared-key challenge, public-key signature, biometric match, PIN, or combination? |
| Reader validation | Which freshness, target, algorithm, key/certificate, revocation, and anti-relay rules were checked? |
| Controller path | Is the proof preserved or reduced to a static number before the access decision? |
| Authorization | Which opening, schedule, mode, anti-passback, and policy apply now? |
| Actuation/confirmation | What commands the lock/gate, and what sensor proves the physical result? |

See [credentials and identity media](../01-foundations/credentials-and-identity-media.md), [credential formats and mobile credentials](../02-protocols/access-control/credential-formats-and-mobile-credentials.md), and [safety impact checklist](safety-impact-checklist.md).

## Technology-family comparison

| Family | What may be presented | Proof model to record | Principal limitations | Lifecycle and integration questions |
|---|---|---|---|---|
| Printed number / visual badge | Human-readable identifier, photo, markings | Human inspection and/or lookup; no cryptographic proof in the print itself | Copying, transcription, stale photo/data, subjective inspection | Issuance authority, visual validation procedure, expiration, loss, accessibility, privacy |
| Barcode / QR | Encoded static or signed data; sometimes a short-lived token | Exact payload and signature/freshness profile | A static image can be copied; camera/display path and offline clock affect policy | Token lifetime, audience/door binding, replay cache, revocation, screenshots, brightness/accessibility |
| PIN | Memorized secret | Knowledge factor verified by controller/service | Observation, sharing, guessing, coercion, lockout abuse | Retry/lockout policy, duress/legal handling, reset, accessibility, logging minimization |
| Magnetic stripe | Tracks containing identifiers/application data | Usually static data under a site/application format | Skimming/copying and wear; no general modern mutual authentication | Exact track format, reader interface, replacement, coexistence retirement plan |
| Identifier-only LF proximity deployment | Fixed transmitted identifier under a product/site format | Possession of a readable static identifier | Observation/emulation/cloning risk; technology name alone cannot prove security | Frequency/product/format, issuer range, duplicate detection, reader-controller transport, migration |
| HF/NFC UID-only use | Public/anti-collision identifier | Presence of identifier, not credential authentication | UID may be public, random, changeable, duplicated, or unsuitable as stable identity by technology/product | UID type/lifetime, normalization, collision handling, explicit prohibition on treating UID as strong proof |
| Contactless shared-key application | Challenge-response or secure messaging using symmetric keys | Exact application, algorithm, diversified key, freshness, reader authentication | Fleet/master-key exposure, weak/default keys, relay/downgrade, reader key custody | Key ceremony, diversification, HSM/SAM use, rotation, replacement, offline validation, certification |
| Contactless public-key application | Credential signature/certificate proof with reader challenge/profile | Certificate/key ownership, issuer chain, freshness, policy identifiers | PKI complexity, certificate/profile mismatch, reader trust-store lifecycle, relay if presence/range not protected | Issuance, non-exportable key, trust rollover, revocation/offline status, algorithm agility |
| PIV credential | Governed identifiers, certificates, keys, and authentication mechanisms | FIPS 201-3 and selected SP 800-73/116 mechanism/profile | PIV conformance and card validity do not automatically authorize a door | Agency trust, CHUID/PIV Auth/Card Auth choice, certificate/path/revocation, PACS risk model |
| Aliro 1.0 mobile access | Standardized access-control credential ecosystem/profile | Exact Aliro role, transport, credential, transaction, and certification | New ecosystem as of 2026; public announcement is not product support evidence | Role/certification, wallet/device security, BLE/NFC/UWB use, issuance/revocation, reader/controller support |
| PKOC 2.0.1 | Public-key open credential over defined NFC/BLE paths; OSDP binding is separately versioned | Exact Core/NFC/BLE version and proof/binding | Product/profile support must be verified; transport and controller link remain distinct | Issuer/trust model, key custody, offline/revocation, OSDP version, conformance evidence |
| Proprietary mobile credential | Vendor-specific app/wallet, BLE/NFC/UWB, cloud/on-prem services | Published vendor protocol and security evidence for exact product/version | Lock-in, opaque protocol, phone/app lifecycle, cloud dependency, radio relay/range claims | Tenant/issuer, device binding, restore/migration, offline behavior, telemetry/privacy, API/reader/controller matrix |
| Biometric verification/identification | Captured characteristic and comparison result/template reference | Sensor quality, liveness/presentation-attack detection, matcher, threshold, supervised policy | Probabilistic error, demographic/performance variation, presentation attacks, irrevocability/privacy | Consent/legal basis, enrollment, template protection, threshold/version, fallback, accessibility, deletion/export |
| Multi-factor / multi-credential policy | Two or more independent proofs | Explicit independence, sequencing, freshness, transaction/door binding | Two weak values on one compromised path may not be independent; usability can cause bypass | Factor recovery, degraded mode, anti-passback, timeout, operator override, evidence and accessibility |

The table intentionally avoids universal “low/medium/high” ratings. The same medium can carry a static identifier or a strong cryptographic application, and the strongest credential can be downgraded to a replayable number at the reader-controller boundary.

## Identifiers that must not be collapsed

| Identifier | Allocation authority and lifetime |
|---|---|
| Subject/person ID | Identity-governance system; may outlive employments or sites |
| Credential record ID | PACS/issuer database object; lifecycle/audit key |
| Printed badge number | Human-facing and potentially reissued |
| Facility/company code and card number | Site format namespace; uniqueness is not global |
| Card UID/CSN | Chip/technology field with technology-specific stability and privacy rules |
| Application serial/account | Credential-application namespace |
| Certificate subject/SAN/key ID | PKI/profile namespace and validity period |
| Mobile device/app/wallet instance | Platform/vendor lifecycle; replacement/restore changes are expected |
| Biometric template ID | Biometric system record, not the biometric data itself |
| OSDP peripheral address | Reader bus address, not credential identity |

Store the namespace, original representation, allocation authority, encoding, and lifecycle with every value. Do not strip leading zeroes, infer a bit format from length alone, or silently map duplicates.

## Reader-controller preservation

| Reader output | Assurance preserved at controller? | Required note |
|---|---|---|
| Wiegand bits / Clock-and-Data | Generally only the emitted static value; link has no modern native protection | Document format, weak-link exposure, and migration |
| OSDP without Secure Channel | Richer supervised messages but no cryptographic link protection | Do not equate CRC with authenticity |
| OSDP Secure Channel | Protects the OSDP link when keys/state/fallback are correctly managed | Record whether cryptographic credential result/proof or only a number is conveyed |
| Vendor encrypted bus | Unknown until exact public/licensed specification and product evidence are reviewed | Do not infer from marketing term “encrypted” |
| Decision at reader | Reduces raw credential exposure but moves authorization/state/lifecycle to the edge | Define offline policy, update authenticity, audit, revocation, and tamper response |

OSDP protection begins and ends at its peers. It cannot repair a clonable credential, and a secure credential cannot repair a cleartext/emulatable reader-controller path. See [OSDP](../02-protocols/access-control/osdp.md) and [legacy reader interfaces](../02-protocols/access-control/legacy-reader-interfaces.md).

## Offline and failure questions

- What time source and maximum clock error govern validity?
- Which revocations, schedule changes, key changes, and threat-list updates are unavailable offline?
- How old may cached authorization be, and which openings are excluded from cache?
- Does a phone restore or card replacement clone, invalidate, or reissue the credential?
- What happens after reader, controller, mobile, secure-element, or PKI reset?
- Can a stale credential be accepted during network partition, and how is that event marked?
- How are duplicate identifiers, rollback, counter loss, and transaction replay detected?
- Does degraded mode change from cryptographic proof to UID/static identifier? It should never do so silently.
- What safe alternative exists for disability, dead battery, lost device, damaged card, or failed biometric?

## Privacy and human factors

Credential systems reveal identity, location, routine, and sometimes biometric or device data. Minimize collection; separate operational access logs from analytics; protect issuer mappings; define retention/export/correction; and provide accessible alternatives. Do not log raw keys, PINs, biometric samples/templates, challenge material, wallet tokens, or full certificate/private data.

Biometric deployment requires jurisdiction-specific legal, labor, consent, equality, retention, and incident analysis. This page provides no legal conclusion. Mobile radios and wallets require regional/platform/product review and must not use RSSI or raw range as sole identity proof.

## Selection and evidence checklist

- [ ] Exact medium, application/profile, revision, role, and certification recorded
- [ ] Identity proofing and credential issuance authority documented
- [ ] Static identifiers distinguished from cryptographic authentication
- [ ] Challenge, target, reader, freshness, transaction, and optional ranging binding specified
- [ ] Key/certificate/trust lifecycle and hardware custody documented
- [ ] Loss, restore, replacement, revocation, expiry, offline, and clock policy tested by owner
- [ ] Reader-controller hop preserves intended proof and blocks silent downgrade
- [ ] Door authorization, lock actuation, and physical confirmation remain separate decisions
- [ ] Privacy, accessibility, coercion, help-desk, and alternate path reviewed
- [ ] Exact product support, versions, and behavior are backed by product declarations and environment evidence

## Sources

- **SIA-GUIDE** — [Corporate Credential Design Guide][SIA-GUIDE], Security Industry Association, March 2026.
- **ISO14443** — [ISO/IEC 14443-1:2018][ISO14443], ISO, current series entry reviewed 2026-08-25.
- **ISO7816** — [ISO/IEC 7816-4:2020][ISO7816], ISO, confirmed 2025.
- **FIPS201** — [FIPS 201-3: Personal Identity Verification][FIPS201], NIST, January 2022.
- **PIV-PACS** — [NIST SP 800-116 Rev. 1: Guidelines for the Use of PIV Credentials in Facility Access][PIV-PACS], NIST, June 2018.
- **ALIRO** — [Introducing Aliro 1.0][ALIRO], Connectivity Standards Alliance, 26 February 2026.
- **PKOC** — [Secure Credential Interoperability and PKOC][PKOC], Physical Security Interoperability Alliance, Core/NFC/BLE 2.0.1 status dated 13 August 2026.
- **OSDP** — [Open Supervised Device Protocol][OSDP], Security Industry Association, OSDP 2.2.2 status reviewed 2026-08-25.
- **NIST-BIO** — [Digital Identity Guidelines: Authentication and Authenticator Management, biometric requirements][NIST-BIO], NIST SP 800-63B-4, July 2025.

[SIA-GUIDE]: https://www.securityindustry.org/wp-content/uploads/2026/03/SIA_CorporateCredentialDesignGuide.pdf
[ISO14443]: https://www.iso.org/standard/73596.html
[ISO7816]: https://www.iso.org/standard/77180.html
[FIPS201]: https://csrc.nist.gov/pubs/fips/201-3/final
[PIV-PACS]: https://csrc.nist.gov/pubs/sp/800/116/r1/final
[ALIRO]: https://csa-iot.org/newsroom/introducing-aliro-1-0-a-unified-standard-to-transform-the-access-control-ecosystem/
[PKOC]: https://psialliance.org/securecredentials/
[OSDP]: https://www.securityindustry.org/industry-standards/open-supervised-device-protocol/
[NIST-BIO]: https://pages.nist.gov/800-63-4/sp800-63b.html#biometrics
