---
title: "Contactless and smart-card standards"
summary: "Developer reference for ISO/IEC 14443, 15693, and 7816 layers, current editions, APDUs, applications, secure messaging, identifiers, and defensive reader design."
page_type: protocol
domains: [access-control, identity]
tags:
  - iso-14443
  - iso-15693
  - iso-7816
  - apdu
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "ISO/IEC 14443-1:2018, -2:2020, -3:2018, -4:2018"
  - "ISO/IEC 15693-1:2018, -2:2019, -3:2026"
  - "ISO/IEC 7816-3:2006 and -4:2020"
coverage_limit: "Standards-layer and defensive APDU guidance only; licensed normative details, card applications, keys, RF/contact hardware, APDUs, secure messaging, relay controls, and conformance are not validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Contactless and smart-card standards

[Access-control protocols](README.md) / Contactless and smart-card standards

The ISO/IEC 14443 and 15693 series define contactless physical/link behavior. ISO/IEC 7816 defines contact-card electrical behavior and technology-independent application/command concepts used by both contact and contactless smart cards. A radio standard does not define a secure credential application; an APDU interface does not guarantee cryptographic authentication.

## Standards status snapshot

Status is verified as at **2026-08-25** from ISO's catalogue.

### ISO/IEC 14443 — contactless proximity objects

| Part | Current published base | Scope/status note |
|---|---|---|
| 1 | ISO/IEC 14443-1:2018, edition 4 | Physical characteristics |
| 2 | ISO/IEC 14443-2:2020, edition 4 | RF power and signal interface; Corrigenda 1:2021 and 2:2023 are published |
| 3 | ISO/IEC 14443-3:2018, edition 4 | Initialization and anticollision for Type A/Type B; revision is under development |
| 4 | ISO/IEC 14443-4:2018, edition 4 | Half-duplex block transmission (ISO-DEP); published amendments apply; Amendment 3 on relay-attack protection was **under publication**, not final, on the verification date |

Do not implement draft revision text as current ISO conformance. Track the ISO catalogue for final publication and product/profile adoption. [ISO14443-1] [ISO14443-2] [ISO14443-3] [ISO14443-4] [ISO14443-4-A3]

### ISO/IEC 15693 — contactless vicinity objects

| Part | Current published base | Scope/status note |
|---|---|---|
| 1 | ISO/IEC 15693-1:2018, edition 3 | Physical characteristics; confirmed current |
| 2 | ISO/IEC 15693-2:2019, edition 3 | Air interface and initialization; confirmed current in 2024 |
| 3 | **ISO/IEC 15693-3:2026, edition 4** | Anticollision and transmission protocol; published May 2026 and replaces 2019 edition |

Use the 2026 Part 3 for new requirements; a device claiming only the withdrawn 2019 edition needs an explicit compatibility assessment. [ISO15693-1] [ISO15693-2] [ISO15693-3]

### ISO/IEC 7816 — integrated-circuit cards

The series has many parts. Most PACS developer work starts with:

| Part | Current relevant base | Scope/status note |
|---|---|---|
| 3 | ISO/IEC 7816-3:2006, edition 3, with Amendment 1:2025 | Contact-card electrical interface and transmission protocols; current base is marked “to be revised” and a replacement is under development |
| 4 | ISO/IEC 7816-4:2020, edition 4, with Amendment 1:2023 | Organization, security, commands, applications, files, and secure messaging; confirmed current in 2025 |
| 6 | ISO/IEC 7816-6:2023, edition 4, with Amendment 1:2026 | Interindustry data elements; 2026 amendment adds quantum-safe cryptography data elements |

An ISO/IEC 7816-4 Amendment 2 concerning quantum-safe cryptography was a Final Draft Amendment on the verification date and is not represented here as published. [ISO7816-3] [ISO7816-4] [ISO7816-4-A1] [ISO7816-6]

## Layer mapping

```text
credential application and data model
  challenge-response, files/objects, keys, certificates, access rules
                         │
ISO/IEC 7816-4 command/response APDUs and secure messaging
                         │
          ┌──────────────┴──────────────┐
ISO/IEC 14443-4 ISO-DEP             ISO/IEC 7816-3 T=0/T=1
contactless Type A/B                contact electrical interface
          │
ISO/IEC 14443-2/-3 RF, activation, anticollision

ISO/IEC 15693 defines a separate vicinity RF/protocol family; an application
profile can add memory commands, security, or an APDU-like application model.
```

The same high-level credential application can appear across contact and contactless transports only when its profile defines the mapping and security behavior.

## ISO/IEC 14443 fundamentals

### Type A and Type B

Type A and Type B use different RF coding, modulation, initialization, and anticollision procedures at the lower layers. ISO/IEC 14443-4 provides a common block-oriented transport after activation for compliant Type A or B objects.

Key integration states include:

1. field on and polling;
2. anticollision/select among multiple objects;
3. activation and parameter negotiation;
4. ISO-DEP block exchange;
5. deselect/removal/field off.

Bound every state, retry, waiting-time extension, chaining operation, and APDU size. Card removal or RF loss during a command leaves the application outcome uncertain.

### Identifier warning

An anticollision identifier/UID helps select one object in the field. It can be fixed, random, reused across product classes, exposed, or translated by platform/reader behavior. It is not a secret and must not be the sole proof of credential authenticity or authorization.

### Relay and proximity

Short nominal RF range expresses coupling characteristics and user experience; it is not cryptographic distance bounding. Relays can extend communication. Use an application/profile designed for relay resistance, freshness, reader authentication, timing/ranging where specified, and end-to-end risk controls. The 14443-4 relay-protection amendment was not yet final on the snapshot date.

## ISO/IEC 15693 fundamentals

ISO/IEC 15693 targets vicinity objects and commonly supports longer coupling distances than proximity-card designs, depending on antenna, field, tag, reader, and local radio rules. Part 3 defines inventory/anticollision and commands. NFC Forum Type 5 Tags use NFC-V based on ISO/IEC 15693.

Do not infer secure credential behavior from “15693.” Many implementations expose static identifiers or memory. Authentication, protected areas, passwords, cryptographic commands, privacy features, and lock bits are product/application-specific and must be assessed exactly.

## ISO/IEC 7816 command model

### APDU shape

A command APDU (C-APDU) has:

```text
CLA | INS | P1 | P2 | optional Lc | optional command data | optional Le
```

A response APDU (R-APDU) has:

```text
optional response data | SW1 | SW2
```

Short and extended-length cases have different length encodings. `CLA` can also carry logical-channel, chaining, and secure-messaging semantics according to the applicable profile. `SW1 SW2` is a structured status; do not reduce all non-`90 00` values to an undifferentiated error.

### Safe APDU fixture

**Target:** APDU encoder/parser unit design.

**Inputs:** Invented proprietary application identifier that is not a real credential AID.

**Side effects:** None. If adapted to a real target, SELECT can alter card session state; use only in an authorized lab.

```text
00 A4 04 00 07 F0 00 00 00 00 00 01 00
```

Interpretation:

```text
CLA=00 INS=A4 P1=04 P2=00 Lc=07
Data=F0 00 00 00 00 00 01
Le=00
```

The exact SELECT semantics, partial-AID rules, return data, and permitted status handling belong to the selected card application profile and ISO/IEC 7816-4 edition.

## Application selection, files, and objects

- Application Identifiers (AIDs) select applications; they are identifiers, not secrets.
- Files/data objects and BER-TLV structures have profile-specific tags, access conditions, and encodings.
- Enforce BER length/depth/tag limits and reject indefinite/oversized/duplicate structures when the profile does not permit them.
- Preserve distinction among absent, empty, zero, proprietary, and unknown values.
- Do not probe arbitrary applications on production credentials; select only authorized AIDs under the intended workflow.

## Authentication and secure messaging

A secure smart-credential flow commonly includes:

1. select a known application;
2. retrieve capability/version information under policy;
3. exchange fresh challenges/nonces;
4. authenticate card and optionally reader;
5. derive or select session keys;
6. protect subsequent commands with secure messaging;
7. validate counters/nonces/MACs and close/expire session state.

Security requires strong algorithms, diversified/unique keys, authentic randomness, correct key versioning, anti-replay counters, protected reader/SAM/HSM storage, and refusal to downgrade. A mutual-authentication command name is not enough—validate the entire profile and key ceremony.

### Shared-key credentials

- Never deploy a global default key.
- Prefer diversified per-credential/per-application keys derived within a controlled key hierarchy.
- Keep master keys in HSM/SAM/secure service boundaries and minimize reader key exposure.
- Define key versions, rotation, recovery, compromised batch handling, and credential replacement.

### Public-key credentials

- Validate trust anchor, chain or attestation profile, algorithm, parameters, key usage, validity/revocation status where applicable, credential identifier binding, reader challenge, and signature.
- Keep private keys non-exportable in the credential's security boundary.
- A valid cryptographic credential still requires current subject/resource authorization.

## Contact-card notes

ISO/IEC 7816-3 defines contact activation, reset and transport protocols such as T=0 and T=1. The Answer to Reset (ATR) advertises interface/protocol information, not trusted subject identity. Apply electrical sequencing exactly to avoid card damage or undefined state and use an approved smart-card interface device.

For contactless ISO-DEP, analogous activation parameters such as ATS data describe communication capabilities. They are not authentication.

## Defensive reader architecture

- Put parsing and radio/contact drivers in a least-privileged process with strict time/memory bounds.
- Allowlist applications, commands, data sizes, algorithms, and versions.
- Authenticate the reader and protect its firmware, debug ports, keys, configuration, and reader-controller link.
- Ensure the PACS receives a cryptographically verified result or protected credential proof—not merely an unprotected UID converted to Wiegand.
- Rate-limit failed authentication without enabling simple denial of service against legitimate users.
- Separate card protocol errors, reader health, policy denial, and door actuation status.
- Redact APDUs because they can contain credential identifiers, certificates, personal data, PIN state, and cryptographic material.

## Test dimensions for the system owner

- Multiple objects in field, rapid removal/re-presentation, collision, RF noise, and field reset
- Short/extended APDUs, chaining, waiting-time extensions, status continuations, and maximum response
- Unknown AID, tag, algorithm, key version, and application version
- Stale/replayed challenge, wrong MAC/signature, counter rollback, interrupted secure messaging, and attempted downgrade
- Reader/controller restart and credential revocation while offline
- Malformed TLV lengths/depth, huge certificate/data object, duplicate critical fields, and allocation limits
- Contactless relay-resistance profile and timing under the actual certified implementation

## Environment validation

Implement against the full ISO standards and selected application profile. Validate exact card/tag/phone and reader versions, RF and contact behaviour, APDU state transitions, key lifecycle, secure messaging, malformed-input limits, relay-resistance claims, conformance results, and controller-bound authorization in an approved environment.

## Sources

- **ISO14443-1** — [ISO/IEC 14443-1:2018][ISO14443-1], ISO, edition 4.
- **ISO14443-2** — [ISO/IEC 14443-2:2020][ISO14443-2], ISO, edition 4.
- **ISO14443-3** — [ISO/IEC 14443-3:2018][ISO14443-3], ISO, edition 4 and lifecycle status.
- **ISO14443-4** — [ISO/IEC 14443-4:2018][ISO14443-4], ISO, edition 4.
- **ISO14443-4-A3** — [ISO/IEC 14443-4:2018/Amd 3: Relay attack protection mechanisms][ISO14443-4-A3], ISO, under publication as at 2026-08-25.
- **ISO15693-1** — [ISO/IEC 15693-1:2018][ISO15693-1], ISO, edition 3.
- **ISO15693-2** — [ISO/IEC 15693-2:2019][ISO15693-2], ISO, edition 3.
- **ISO15693-3** — [ISO/IEC 15693-3:2026][ISO15693-3], ISO, edition 4, May 2026.
- **ISO7816-3** — [ISO/IEC 7816-3:2006][ISO7816-3], ISO, edition 3 and lifecycle status.
- **ISO7816-4** — [ISO/IEC 7816-4:2020][ISO7816-4], ISO, edition 4, confirmed 2025.
- **ISO7816-4-A1** — [ISO/IEC 7816-4:2020/Amd 1:2023][ISO7816-4-A1], ISO.
- **ISO7816-6** — [ISO/IEC 7816-6:2023][ISO7816-6], ISO, edition 4 and Amendment 1:2026 listing.
- **NFC-SPECS** — [NFC Forum Specifications][NFC-SPECS], NFC Forum, accessed 2026-08-25.

[ISO14443-1]: https://www.iso.org/standard/73596.html
[ISO14443-2]: https://www.iso.org/standard/73597.html
[ISO14443-3]: https://www.iso.org/standard/73598.html
[ISO14443-4]: https://www.iso.org/standard/73599.html
[ISO14443-4-A3]: https://www.iso.org/standard/86711.html
[ISO15693-1]: https://www.iso.org/standard/70837.html
[ISO15693-2]: https://www.iso.org/standard/73601.html
[ISO15693-3]: https://www.iso.org/standard/90286.html
[ISO7816-3]: https://www.iso.org/standard/38770.html
[ISO7816-4]: https://www.iso.org/standard/77180.html
[ISO7816-4-A1]: https://www.iso.org/standard/84943.html
[ISO7816-6]: https://www.iso.org/standard/77181.html
[NFC-SPECS]: https://nfc-forum.org/build/specifications
