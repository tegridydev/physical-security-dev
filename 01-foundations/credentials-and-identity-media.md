---
title: Credentials and Identity Media
summary: A security model for cards, smart cards, mobile credentials, biometrics, PINs, identifiers, readers, and lifecycle.
page_type: foundation
domains: [access-control]
tags: [credentials, smart-card, nfc, ble, biometrics, mobile-access]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [ISO/IEC 14443, ISO/IEC 15693, ISO/IEC 7816]
coverage_limit: Conceptual taxonomy; no cloning, key-extraction, bypass, live credential, or biometric-template procedures.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Credentials and identity media

A credential is evidence presented during authentication. It is not inherently unique, secret, person-bound, revocable, or resistant to copying. Security comes from the complete lifecycle and protocol, not the card shape or radio frequency.

## Separate layers

```text
person/subject
  -> identity proofing and account
  -> credential issuance and binding
  -> physical/mobile authenticator
  -> radio/contact interface
  -> application and cryptographic protocol
  -> reader authentication and controller channel
  -> PACS/controller authorization decision
  -> physical output and audit
```

ISO/IEC 14443 defines proximity contactless cards/interfaces, ISO/IEC 15693 covers vicinity cards, and ISO/IEC 7816 covers contact integrated-circuit cards. These are multi-part standards accessible through the [ISO catalogue](https://www.iso.org/standards.html). They do not, by their names alone, state which application, keys, mutual authentication, or credential lifecycle a deployment uses.

## Credential classes

- **Identifier-only legacy media:** emits a number used as an index. If replay/copy resistance is absent, treat the number as public identifier data, not a secret.
- **Cryptographic smart credential:** performs authenticated operations using protected keys. Security depends on product/application, diversified keys, algorithms, reader validation, and backend policy.
- **Mobile credential:** provisioned to a phone/wearable and presented over NFC, BLE, UWB, or combinations. Review secure storage, device binding, app/account recovery, offline use, platform attestation, and revocation.
- **Knowledge factor:** PIN/passcode. Protect against observation, online/offline guessing, shared codes, and unsafe fallback.
- **Biometric:** probabilistic matching of a physiological/behavioural characteristic. Templates are sensitive, hard to revoke, and subject to presentation-attack, bias, privacy, accessibility, and jurisdictional requirements.

## Identifiers are contextual

Card serial/UID, facility code, card number, application identifier, account ID, mobile token ID, and PACS credential ID are different namespaces. Preserve leading zeros and bit length; never guess a credential format solely from a decimal value. Global uniqueness is not guaranteed.

Avoid exposing raw credential numbers in event topics, URLs, logs, analytics, or user interfaces. Use scoped opaque identifiers and access-controlled resolution where business use requires identity.

## Reader-to-controller boundary

Even a strong card transaction can be reduced to replayable identifier bits over a legacy reader interface. Preserve authenticated transaction meaning over a supervised, protected channel such as an appropriately configured secure protocol. Reader configuration, keys, firmware, tamper state, and controller identity need lifecycle controls.

## Issuance and recovery

Record issuer, subject binding, credential type/application, unique inventory identifier, issue/activation/expiry/revocation times, assurance, allowed fallback, and key/version identifiers without storing secret key material here. Use two-person control or equivalent governance for high-impact key operations.

Lost-phone/card, replacement, re-enrollment, backup/restore, shared-device, visitor, contractor, and emergency processes are part of the security design. Recovery must not become the easiest impersonation path.

## Defensive boundary

This library may compare security properties and explain authorized offline/synthetic analysis. It does not provide instructions to clone credentials, extract production keys, capture live presentations, defeat readers, or bypass access decisions.
