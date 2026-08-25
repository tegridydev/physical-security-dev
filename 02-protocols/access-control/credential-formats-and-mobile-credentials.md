---
title: "Credential formats, smart credentials, and mobile credentials"
summary: "Developer reference for credential namespaces, bit layouts, cryptographic credential models, Aliro, PKOC, PIV, mobile lifecycle, privacy, and end-to-end PACS authorization."
page_type: protocol
domains: [access-control, identity]
tags: [credential-formats, mobile-credentials, aliro, pkoc, piv, smart-cards]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "SIA AC-01-1996.10: 26-BIT Wiegand Reader Interface"
  - "Aliro 1.0 (February 2026)"
  - "PKOC Core, NFC, and BLE 2.0.1 (August 2026)"
  - "FIPS 201-3 and NIST SP 800-73-5 (reference profile)"
coverage_limit: "Credential data-model and lifecycle guidance only; no identity proofing, key ceremony, wallet/mobile OS, card, reader, credential issuance, cryptographic exchange, PACS decision, door, certification, or vendor interoperability is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Credential formats, smart credentials, and mobile credentials

[Access-control protocols](README.md) / Credential formats and mobile credentials

A physical-access credential is not just a card number. It is a governed binding among a subject, authenticator/key or identifier, issuer, lifecycle state, presentation protocol, reader validation result, and PACS authorization record. Treat each binding and namespace explicitly.

## Keep these identifiers separate

| Identifier | What it names | Security caveat |
|---|---|---|
| Printed badge number | Human help-desk/display reference | Often photographed or guessable; not an authenticator |
| Technology UID/CSN/serial | Chip/object selected by a reader | Observable and sometimes random/reused/emulatable; not proof of a secure application |
| Wiegand facility/card fields | Reader-controller output fields | Static, small collision domain, cleartext on legacy link |
| Application credential ID | Identifier inside a credential scheme | May be public/opaque; authenticity depends on protocol proof |
| Public key / derived identifier | Cryptographic credential namespace | Must prove possession and bind key to issuer/registration policy |
| PACS credential-record ID | Internal lifecycle/database record | Must be tenant-scoped and never accepted directly as on-air proof |
| Subject/person ID | Human or service identity account | Requires governed proofing, joins, privacy, and lifecycle |
| Device/wallet instance ID | Mobile endpoint or secure container | Device identity is not automatically person identity |

Never collapse these into one database integer. Preserve the original scheme, version, issuer/allocation authority, binary value and display rendering separately.

## Credential assurance chain

```text
identity proofing and sponsorship
        -> credential issuance / key binding
        -> credential-holder or device activation
        -> fresh reader–credential authentication
        -> protected reader–controller result
        -> current PACS policy and lifecycle decision
        -> bounded door command
        -> physical sensor confirmation and audit
```

Each arrow is a trust boundary. Strong asymmetric authentication cannot repair weak identity proofing, a compromised reader, unprotected Wiegand output, stale authorization, or unsafe door hardware.

## Static identifier formats

### Common 26-bit Wiegand

SIA AC-01-1996.10 defines a 26-bit reader-interface format commonly represented as:

```text
leading parity | 8-bit facility code | 16-bit card number | trailing parity
```

This yields a small allocation space and duplicate facility/card pairs across independent issuers. Parity provides transmission error detection, not authenticity. See [Legacy reader interfaces](legacy-reader-interfaces.md) for the exact conceptual field layout and offline-only parser fixture. [SIA-WIEGAND]

### Other bit layouts

Longer Wiegand-style formats are frequently vendor, customer, or program profiles. “37-bit” does not identify a unique layout. A format registry should record:

```text
format_id and version
bit_length
field name, offset, width, signedness and byte/bit order
parity/check coverage and expected rule
issuer/allocation authority and collision domain
display conversion and leading-zero policy
allowed credential technologies/readers/panels
status: issue / accept-only / retired
migration and overlap dates
```

Reject unknown length/layout instead of guessing. Do not silently truncate a public key hash, mobile credential identifier, smart-card application ID, or large card number into a legacy field without recording the collision and replay downgrade.

## Smart credential models

### Identifier-only or memory credentials

The reader retrieves a static UID or stored value. This is easy to integrate but usually clonable/replayable unless a separate trusted mechanism authenticates the object. Password-protected memory is not automatically challenge-response authentication.

### Symmetric-key credentials

The credential and verifier prove possession of shared/diversified secrets through fresh challenge-response and may establish secure messaging. Secure design requires:

- unique or diversified per-credential/application keys;
- protected issuer master keys in HSM/SAM or equivalent boundary;
- strong randomness and transaction counters/nonces;
- reader authentication when the scheme supports it;
- algorithm/key-version agility and downgrade refusal;
- batch compromise, rotation, replacement, and revocation procedures.

A global key copied into all cards and readers creates systemic compromise risk.

### Public-key credentials

The credential holds a non-exportable private key and proves possession by signing or authenticated key agreement. The verifier registers a public key/derived identifier or validates a certificate/attestation chain. This reduces shared-secret distribution but still requires trust-anchor, registration, algorithm, revocation, reader-authentication, privacy, and lifecycle design.

## Current open mobile credential standards

Status below is verified as at **2026-08-25**.

| Scheme/profile | Current status | Developer boundary |
|---|---|---|
| Aliro | **1.0**, released 2026-02-26 | CSA communication and credential standard using asymmetric cryptography across NFC, BLE, and BLE+UWB access flows, with certification |
| PKOC | **Core 2.0.1**, NFC 2.0.1, BLE 2.0.1, approved 2026-08-13 | PSIA transport-independent public-key credential plus NFC and BLE profiles |
| PKOC over OSDP | **1.63**, approved 2024-03-22 | Separate reader-to-panel binding; PSIA notes it has not yet been reissued under the 2.0.1 Core structure |
| PIV | FIPS 201-3; SP 800-73-5 final in 2024; SP 800-116 Rev. 1 final in 2018 | US federal governed reference profile over ISO/IEC smart-card interfaces; not a universal commercial mobile credential standard |

[ALIRO] [PKOC] [FIPS201] [PIV-INTERFACE] [PIV-PACS]

### Aliro 1.0

The Connectivity Standards Alliance released Aliro 1.0 in February 2026 as a mobile credential and communication standard for commercial, educational, hospitality, and residential access. Its public release material says it uses asymmetric cryptography and supports:

- NFC tap-to-access;
- BLE user-initiated longer-range access;
- BLE plus UWB hands-free authentication/ranging;
- offline-capable installation scenarios;
- mobile wallet ecosystems and a certification/test program.

Represent Aliro conformance only for a certified product's exact transport/features. The Alliance describes expanded secure key sharing as future work beyond the initial foundation, so do not assume Aliro 1.0 implements every sharing/delegation use case. [ALIRO]

### PKOC 2.0.1

PSIA's Secure Credential Interoperability page identifies the following approved releases:

- **Core 2.0.1:** transport-independent credential model, ECDSA using NIST P-256, key encodings, PKOC Credential and Derived Identifier, PKOC-CVC attestation, registration, and trust-anchor provisioning.
- **NFC Transport Profile 2.0.1:** ISO/IEC 14443 application/APDU binding and defined card profiles/modes; supersedes NFC Card 1.1 while retaining the stated compatibility path.
- **BLE Transport Profile 2.0.1:** GATT/TLV/fragmentation binding, including an ECDHE flow with forward secrecy and AES-CCM protection plus a simpler profile-defined flow; reader signing keys/certificates support its validated trust model.
- **PKOC over OSDP 1.63:** conveys credential data from PD/reader to panel and assumes an OSDP Secure Channel with a unique paired key.

The Core alone has no wire format and a transport profile is incomplete without the Core. Record both. PKOC avoids a conventional certificate-issuing PKI for basic credential enrollment, but its 2.0.1 validated modes include profile-specific attestation/certification structures; implement the exact trust model rather than relying on a slogan. [PKOC] [PKOC-OSDP]

### PIV as a governed reference profile

FIPS 201-3 specifies the US federal Personal Identity Verification system. NIST SP 800-73-5 defines current PIV card application interfaces/data models, and SP 800-116 Rev. 1 defines risk-based use in facility access. It demonstrates how ISO/IEC 14443/7816 transport, identifiers/data objects, PKI authentication mechanisms, lifecycle, and PACS policy can be constrained into an interoperable program. It is not automatically appropriate or compliant outside its scope. [FIPS201] [PIV-INTERFACE] [PIV-PACS]

A readable CHUID, FASC-N, UUID, or card identifier is not equivalent to successful PKI card authentication. Use the authentication mechanism selected by the governing risk profile and validate certificate/current status as required.

## Mobile credential lifecycle

### Enrollment and issuance

1. Authenticate the administrator/issuer and prove/sponsor the subject under a recorded policy.
2. Identify the wallet/device/secure-container capabilities and compliance state.
3. Generate the private key inside the intended non-exportable security boundary when the scheme requires it.
4. Bind/register the public credential to issuer, subject, device instance, tenant, validity, allowed transports and policy.
5. Deliver provisioning material through an authenticated protected channel with replay/expiry controls.
6. Confirm activation and record only safe key references/fingerprints—not private keys or recovery secrets.
7. Notify the subject and expose a way to report loss or unexpected issuance.

Issuance authorization must be separate from ordinary PACS administration. Bulk issuance, reissuance, and help-desk recovery deserve stronger controls and dual approval under higher-risk policy.

### Presentation and decision

1. Discover or select the intended reader using the profile.
2. Authenticate reader and credential and bind a fresh transcript.
3. Perform user/device activation or verification where policy requires it.
4. For hands-free flows, bind UWB or Bluetooth Channel Sounding evidence to the authenticated session.
5. Send a protected result to the controller/decision service.
6. Look up current credential and subject status plus door/time/context policy.
7. Issue a unique, expiring command and separately observe door/lock state.

Biometric unlock of a phone/secure element can be a local activation factor. Do not export the biometric template to the PACS unless a separate biometric system and privacy basis requires it. Platform attestation can describe device/app state; it is not the user's identity or door authorization.

### Suspension, revocation, expiry, and replacement

- Make suspension fast and reversible; make revocation explicit and audited.
- Revoke/disable all affected wallet/device instances after device loss or subject termination.
- Define offline-reader policy validity and maximum revocation lag.
- Expire short-lived transport/session credentials independently of employment/subject lifecycle.
- Handle phone restore, secure-element reset, OS migration, device trade-in, number change, and multi-device enrollment as new binding events.
- Never reuse a revoked key or silently transfer a non-exportable key by treating a backup identifier as equivalent.
- Keep historical event referential integrity after deleting/minimizing active personal data.

## Safe credential-record shape

**Target:** Schema discussion only.

**Inputs:** Documentation identifiers; no public/private key, token, phone identifier, or real person.

**Side effects:** None.

```json
{
  "credential_record_id": "cr_demo_001",
  "tenant_id": "tenant_demo",
  "subject_id": "person_demo_001",
  "scheme": "aliro-1.0",
  "scheme_credential_id": "opaque-demo-reference",
  "device_binding_id": "device-binding-demo-001",
  "status": "active",
  "valid_from": "2026-08-25T00:00:00Z",
  "valid_until": "2026-09-25T00:00:00Z",
  "allowed_transports": ["nfc"],
  "revision": 7
}
```

The application must enforce allowed enum values, UTC/time uncertainty, tenant-scoped uniqueness, immutable scheme/issuer binding, revision preconditions, authorized transitions, and sensitive-field minimization. Real cryptographic material belongs in the selected secure-key/trust system, not this record shape.

## Offline access

Offline readers improve resilience but delay revocation and policy updates. Define:

- signed policy/credential cache source and version;
- trusted clock and behavior when time is uncertain;
- maximum offline duration and credential validity;
- deny/allow list freshness and storage protection;
- anti-passback/event sequence reconciliation;
- event buffer capacity and authenticated upload;
- safe behavior on rollback, corruption, full storage, and expired policy;
- emergency and accessibility rules independent of network availability.

“Works offline” must never mean indefinite acceptance of a static identifier.

## Reader-to-controller downgrade

Preserve the credential assurance result across the reader-controller boundary:

- Prefer OSDP Secure Channel with unique per-PD keys.
- Convey scheme/version, verified credential reference/result, transaction context, and reader identity as the profile allows.
- Do not output only a static Wiegand number after a secure smart/mobile exchange unless the downgrade is explicitly accepted, collision-managed, and scheduled for removal.
- Protect IP reader/controller APIs with mutual identity, authorization, replay controls, and audit.
- Keep unlock/relay actuation on the secure side.

## Privacy and human factors

- Minimize stable identifiers in RF advertisements, logs, analytics, badges, and screenshots.
- Separate the printed badge display need from machine credential values.
- Give users clear tap/hands-free intent, success, denial, and device-loss reporting paths.
- Avoid exposing access level, employee number, office, signature, date of birth, or unnecessary branding/QR data on a badge.
- Make credentials accessible to users with mobility, dexterity, vision, hearing, and cognitive differences; provide governed alternatives.
- Define controller/processor roles, retention, cross-site correlation, export, correction, and deletion under applicable privacy rules.

SIA's 2026 Corporate Credential Design Guide provides a vendor-neutral lifecycle, usability, physical badge, interoperability, mobile, biometric, and privacy framework. [SIA-CREDENTIAL-GUIDE]

## Migration strategy

1. Inventory credential populations, technologies, raw formats, issuer ranges, readers, panels, keys, mobile apps/wallets, and door criticality.
2. Eliminate duplicate namespace mappings and unknown-format auto-detection.
3. Choose the target cryptographic credential/profile and certified transport products.
4. Design issuer/key/trust, lifecycle, offline, help-desk, privacy, and reader-controller protection.
5. Pilot with synthetic/test identities and noncritical isolated openings under an approved, bounded acceptance plan.
6. Run old and new credentials only for a bounded overlap; mark old as accept-only, then revoke/disable.
7. Remove legacy reader inputs, default keys, converters, stale wallet credentials, and unused mobile app entitlements.
8. Retain an auditable mapping history without retaining unnecessary secrets/personal data.

## Review checklist

- [ ] Every identifier namespace and allocation authority recorded separately
- [ ] Exact bit format, card/mobile scheme, profile, transport, and certification pinned
- [ ] Identity proofing, issuance, activation, authentication, authorization, actuation, and confirmation separated
- [ ] Private keys non-exportable and trust/master keys protected under a documented ceremony
- [ ] Fresh challenge, reader identity, credential proof, range evidence, and target bound
- [ ] Mobile loss, restore, replacement, multi-device, sharing, suspension, revocation, and expiry handled
- [ ] Offline validity/revocation lag and clock failure bounded
- [ ] Reader-controller link preserves cryptographic assurance
- [ ] UID/static number/Wiegand output never misrepresented as strong authentication
- [ ] Privacy, badge display, logs, accessibility, and alternative credential paths reviewed
- [ ] Product certification, lifecycle, interoperability, failure, and physical acceptance evidence recorded

## Environment validation

Validate enrollment, issuance, presentation, sharing controls, suspension, revocation, restore, replacement, offline operation, and expiry across the selected wallet/card, reader, controller, and PACS versions. Record cryptographic-profile and certification evidence separately from UWB/radio, biometric, interoperability, and physical-door acceptance results.

## Sources

- **SIA-CREDENTIAL-GUIDE** — [Corporate Credential Design Guide][SIA-CREDENTIAL-GUIDE], Security Industry Association, March 2026.
- **SIA-WIEGAND** — [SIA AC-01-1996.10: 26-BIT Wiegand Reader Interface][SIA-WIEGAND], Security Industry Association, 1996.
- **SIA-OSDP** — [Open Supervised Device Protocol][SIA-OSDP], Security Industry Association, OSDP 2.2.2 status accessed 2026-08-25.
- **ALIRO** — [Introducing Aliro 1.0][ALIRO], Connectivity Standards Alliance, 26 February 2026.
- **ALIRO-SPEC** — [Alliance Specification Downloads: Aliro 1.0][ALIRO-SPEC], Connectivity Standards Alliance, accessed 2026-08-25.
- **PKOC** — [Secure Credential Interoperability and PKOC][PKOC], Physical Security Interoperability Alliance, Core/NFC/BLE 2.0.1 status dated 13 August 2026.
- **PKOC-OSDP** — [PKOC over OSDP 1.63][PKOC-OSDP], Physical Security Interoperability Alliance, approved 22 March 2024.
- **FIPS201** — [FIPS 201-3: Personal Identity Verification][FIPS201], NIST, January 2022.
- **PIV-INTERFACE** — [NIST SP 800-73-5 Part 1: PIV Card Application Namespace, Data Model and Representation][PIV-INTERFACE], NIST, final 15 July 2024.
- **PIV-PACS** — [NIST SP 800-116 Rev. 1: Guidelines for the Use of PIV Credentials in Facility Access][PIV-PACS], NIST, June 2018.
- **ISO7816-4** — [ISO/IEC 7816-4:2020][ISO7816-4], ISO, edition 4, confirmed 2025.

[SIA-CREDENTIAL-GUIDE]: https://www.securityindustry.org/wp-content/uploads/2026/03/SIA_CorporateCredentialDesignGuide.pdf
[SIA-WIEGAND]: https://www.securityindustry.org/industry-standards/sia-ac-01-1996-10/
[SIA-OSDP]: https://www.securityindustry.org/industry-standards/open-supervised-device-protocol/
[ALIRO]: https://csa-iot.org/newsroom/introducing-aliro-1-0-a-unified-standard-to-transform-the-access-control-ecosystem/
[ALIRO-SPEC]: https://csa-iot.org/developer-resource/specifications-download-request/
[PKOC]: https://psialliance.org/securecredentials/
[PKOC-OSDP]: https://psialliance.org/wp-content/uploads/2024/03/PKOC-OSDP-1.63-240325.pdf
[FIPS201]: https://csrc.nist.gov/pubs/fips/201-3/final
[PIV-INTERFACE]: https://csrc.nist.gov/pubs/sp/800/73/pt1/5/final
[PIV-PACS]: https://csrc.nist.gov/pubs/sp/800/116/r1/final
[ISO7816-4]: https://www.iso.org/standard/77180.html
