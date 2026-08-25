---
title: "NFC, Bluetooth Low Energy, and UWB for access control"
summary: "Developer reference for current NFC, Bluetooth LE, and UWB layers, discovery, data exchange, ranging, security properties, version status, and safe access-system composition."
page_type: protocol
domains: [access-control, identity, networking]
tags: [nfc, bluetooth-le, uwb, ranging, mobile-credentials]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NFC Forum Release 15 and Certification Release 15 (authorized May 2026)"
  - "Bluetooth Core Specification 6.3 (adopted May 2026)"
  - "IEEE 802.15.4-2024"
  - "FiRa Core and Certification Release 4.0 (December 2025)"
coverage_limit: "Radio/protocol architecture and defensive composition only; no antenna, spectrum compliance, mobile OS, wallet, credential, ranging, reader, lock, interoperability, certification, or physical actuation is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# NFC, Bluetooth Low Energy, and UWB for access control

[Access-control protocols](README.md) / NFC, BLE, and UWB

NFC, Bluetooth Low Energy (BLE), and Ultra-Wideband (UWB) are complementary transports and ranging technologies. They do not, by themselves, define who a user is or whether a door should open. A secure access profile must bind fresh credential proof, the intended reader, transport/session, proximity policy, authorization state, and audit result end to end.

## Current status snapshot

Status is verified as at **2026-08-25**.

| Family | Current public base | Important status distinction |
|---|---|---|
| NFC Forum | NFC Release 15 announced June 2025; CR15/TR15.0 launched October 2025; Certification Release 15 authorized for use in certification May 2026 | Technical specification, test-release launch, and authorization for certification are distinct milestones; product certification is feature/release-specific |
| Bluetooth | Core Specification **6.3**, adopted May 2026 | A Core revision contains optional/conditional features; describe qualified product capabilities, not “Bluetooth 6.3” as a feature set |
| IEEE UWB | **IEEE 802.15.4-2024**, active | Supersedes 802.15.4-2020 and incorporates the work previously published as the now-superseded 802.15.4z-2020 amendment |
| Enhanced UWB work | P802.15.4ab | Active draft project, not a published standard on the verification date |
| FiRa | Core Specifications and Certification Release **4.0**, December 2025 | Modular certification covers selected feature sets; a FiRa label does not imply every ranging/data/profile feature |
| Access credential profile | Aliro **1.0**, February 2026 | Current CSA mobile credential and communication standard across NFC, BLE, and BLE+UWB flows |

[NFC-R15] [NFC-CR15] [BT63] [IEEE154] [IEEE154Z] [FIRA4] [ALIRO]

## Compose layers explicitly

```text
credential application
  key, identity binding, challenge-response, lifecycle, privacy
                          │
transport/profile
  Aliro, PKOC, vendor profile, NFC tag/application, BLE GATT service,
  FiRa application/profile
                          │
radio/link
  NFC-A/B/F/V       Bluetooth LE       IEEE 802.15.4 UWB
                          │
reader/lock -> protected reader-controller/API path -> PACS policy
```

Certification at one layer does not certify the entire stack. Record every layer and the exact certified feature set.

## NFC

NFC Forum specifications harmonize and extend ISO/IEC 14443, ISO/IEC 18092, ISO/IEC 15693, and related technologies for reader/writer, card-emulation, peer, and wireless-charging use. Release 15 expands the certified operating volume for applicable new devices to as much as 20 mm under its test model; this is not a universal read-range claim for every antenna, tag, installed reader, or legacy device. [NFC-SPECS] [NFC-R15]

### Technology mapping

| NFC technology/tag type | Lower-layer relationship |
|---|---|
| NFC-A | ISO/IEC 14443 Type A family |
| NFC-B | ISO/IEC 14443 Type B family |
| NFC-F / Type 3 Tag | JIS X 6319-4 family |
| Type 4 Tag | ISO-DEP over ISO/IEC 14443 Type A or B |
| NFC-V / Type 5 Tag | ISO/IEC 15693 family |
| Type 2 Tag | NFC-A-based tag protocol |

NFC Forum removed Type 1 Tag features from its 2021 technical-specification release for future-device simplification; legacy Type 1 deployments still need explicit handling. The current public specification catalogue lists Digital Protocol 2.4, Analog 3.0, and tag/application specifications with their own versions. Pin individual documents, not only “NFC Release 15.” [NFC-SPECS]

### NDEF

NFC Data Exchange Format (NDEF) is an application data container for records such as URI, text, MIME, and external types. It does not authenticate a tag or make its content safe. In March 2026 the NFC Forum announced NDEF's adoption as **IEC 63652-2:2026** (and NFC wireless charging as IEC 63652-1:2026). [NFC-IEC]

For NDEF consumers:

- cap message, record, type, ID, payload, nested/handover, and decompressed sizes;
- treat URIs, application links, Bluetooth handover data, and MIME payloads as untrusted;
- require user intent before opening links or changing configuration;
- allowlist schemes and destinations; do not pass records to a shell or unrestricted intent handler;
- do not use the tag UID or an unsigned NDEF identifier as credential authentication.

### NFC access flow

A strong tap flow selects a known credential application, exchanges fresh challenges, performs mutual or credential authentication, binds the transcript to reader and policy context, and closes session state after removal. The short-range user gesture helps intent but does not prevent relay by itself. See [Contactless and smart-card standards](contactless-and-smart-card-standards.md).

## Bluetooth Low Energy

BLE separates discovery/connection behavior (GAP), link security, attribute transport (ATT), and service/characteristic modeling (GATT). A mobile access profile defines the required roles, services, characteristics, procedures, security levels, and application cryptography.

### Discovery and connection

- Advertising data is observable, spoofable input until authenticated.
- Device names, addresses, service UUIDs, manufacturer data, and RSSI are discovery hints—not credential proof.
- Use privacy-address features according to the selected profile and mobile OS; avoid stable identifiers in clear advertising payloads.
- Bound scan duration, advertisements parsed, connections, GATT procedures, MTU, characteristic length, notifications, and reconnect attempts.
- Bind a connected peer to authenticated application state; BLE address equality is not sufficient.

### Pairing and bonding

Pairing negotiates link keys/security; bonding stores keys for later use. “Just Works” does not provide man-in-the-middle protection. Authenticated pairing methods depend on device I/O and user verification, and LE Secure Connections must be required under the deployment profile when supported. Even an encrypted/authenticated BLE link needs application-level credential proof and authorization.

Protect long-term keys in platform/secure hardware where available, handle OS restore and device replacement, expire stale bonds, cap failed pairing, and never let an unauthenticated client reach control characteristics.

### GATT design

- Allocate/profile UUIDs correctly; a UUID is a type identifier, not a secret.
- Give each characteristic exact read/write/notify and security permissions.
- Put command ID, version, length, freshness, target, and integrity inside the application protocol.
- Define fragmentation/reassembly independent of ATT MTU and bound total message size.
- Make write-without-response use explicit sequence/ack behavior at the application layer when delivery matters.
- Remove debug and unauthenticated provisioning services in production.

### RSSI, direction finding, and Channel Sounding

RSSI is a noisy path-loss observation and is readily influenced by body position, antenna, environment, and transmit power. It is not secure distance proof.

Bluetooth Channel Sounding was introduced in Core 6.0 and combines phase-based ranging and round-trip timing mechanisms with protocol security features. Core 6.3 adds refinements including PHY-specific RTT accuracy reporting and inline phase-coherent-tone transfer. The Bluetooth SIG says the feature provides ranging measurements used by an application algorithm; it does not define that final distance algorithm. [BT-CS] [BT63-OVERVIEW]

Use Channel Sounding only under an authenticated encrypted connection and a use-case profile. Validate attack-detection indicators, measurement quality, calibrated policy thresholds, hardware/firmware capability, and failure behavior. Do not map a single range estimate directly to unlock.

## Ultra-Wideband

IEEE 802.15.4-2024 defines low-rate wireless PHY/MAC behavior including precision-ranging modes and is the active base. The earlier 802.15.4z-2020 amendment enhanced UWB PHYs, ranging integrity/accuracy, and MAC ranging control but is now listed by IEEE as superseded because its work is incorporated into later base revisions. P802.15.4ab remains a draft project for enhanced UWB PHY/MAC/ranging, sensing, discovery, density, power, and data-rate features. [IEEE154] [IEEE154Z] [IEEE154AB]

### Ranging forms

- **Two-Way Ranging (TWR):** peers exchange timed frames to estimate time of flight.
- **TDoA:** infrastructure or tags use time differences across synchronized observations.
- **Angle of Arrival (AoA):** antenna-array measurements estimate direction.
- **Secure Timestamp Sequence (STS):** cryptographically generated sequence mechanisms improve ranging integrity under the selected profile/key context.

Ranging yields a measurement with uncertainty, quality, and threat assumptions. It does not establish user identity, device entitlement, line of sight, or safe door conditions.

### FiRa

FiRa Core 4.0, released December 2025, aligns its use-case features with IEEE 802.15.4-2024 and adds/extends UL-TDoA, suspend-ranging, and Aliro UWB support in UCI. Certification Release 4.0 is modular and can certify TWR, TDoA, AoA, scheduling, data transfer, CCC Digital Key UWB, Aliro UWB, and selected security/configuration features depending on the claim. Verify the device's exact certified feature set. [FIRA4] [FIRA-CERT]

FiRa also publishes a Physical Access Control System Profile and BLE out-of-band channel specification in its catalogue. Profile implementation and profile certification are separate from Core subsystem certification. [FIRA-SPECS]

## Multi-radio mobile access

Aliro 1.0 defines asymmetric-cryptography-based mobile access using:

- NFC for tap-to-access;
- BLE for user-initiated longer-range interaction;
- BLE plus UWB for hands-free authenticated/ranging interaction.

The BLE discovery/session can establish an authenticated context and configure UWB; UWB can then provide proximity evidence. The access decision must cryptographically bind both transcripts to the same credential, reader, session, and freshness context. Otherwise a system can authenticate one peer and range another. [ALIRO]

## Safe conceptual state machine

```text
IDLE
  -> DISCOVERED (untrusted NFC/BLE/UWB observation)
  -> SESSION_AUTHENTICATED (credential and reader proof bound)
  -> PROXIMITY_EVALUATED (optional UWB/Channel Sounding quality + policy)
  -> AUTHORIZATION_CHECKED (subject, door, time, lifecycle, anti-passback)
  -> COMMAND_ACCEPTED (unique command ID, expiry, audit)
  -> PHYSICALLY_CONFIRMED or FAILED (door/lock sensor, not radio assumption)
  -> CLOSED (keys/session/caches expired)
```

Never skip from `DISCOVERED` or a raw distance result to actuation.

## Cross-radio threat model

| Threat | Design response |
|---|---|
| Advertising/tag spoofing | Authenticate at application layer; discovery is untrusted |
| Relay | Fresh challenges, reader/credential authentication, secure ranging profile, transcript binding, timing/quality policy |
| Replay | Nonces/counters/session IDs, short validity, durable replay state as needed |
| Tracking | Rotating/private discovery identifiers, minimal clear metadata, bounded logs |
| Downgrade | Pin required transport/profile/algorithm; reject fallback to UID/RSSI/static number |
| Peer mix-up | Bind credential proof, reader identity, transport, range exchange, and target opening |
| Reader compromise | Secure boot/update, protected keys, tamper controls, attestation where profile-defined, protected reader-controller link |
| Phone compromise/loss | Non-exportable keys, user verification, rapid suspension/revocation, device-replacement workflow |
| Offline revocation lag | Short credential/policy validity, signed offline state, bounded grace, reconciliation and audit |
| RF denial/interference | Safe denied/degraded state, accessible fallback, life-safety egress independent of radio |

## Global radio and privacy constraints

UWB and BLE/NFC power, channels, duty cycle, emissions, coexistence, privacy, accessibility, and product approvals vary by jurisdiction. A globally standardized protocol does not remove local regulatory work. Maintain a country/region deployment matrix outside this global protocol page and do not enable unsupported radio modes through configuration alone.

## Review checklist

- [ ] Exact NFC documents, Bluetooth capabilities, IEEE base, FiRa feature set, and access profile pinned
- [ ] Certification claims verified at product/firmware/feature/profile level
- [ ] Discovery identifiers, UID, address, service UUID, RSSI, and raw range never treated as authentication
- [ ] Credential and reader mutually bound to session, target, freshness, and optional range transcript
- [ ] Pairing/bonding, keys, secure element, rotation, loss, restore, and revocation designed
- [ ] Radio/parser/message/connections/ranging resource limits enforced
- [ ] Replay, relay, downgrade, peer mix-up, tracking, interference, and offline policy tested by the system owner
- [ ] Reader-controller hop uses protected authenticated transport
- [ ] Physical completion is sensor/controller evidence, not radio success
- [ ] Regional radio, privacy, accessibility, and product approval reviewed

## Environment validation

Validate the selected phone, wallet, card/tag, reader, antenna, firmware, and credential profile together. Record BLE session and downgrade behaviour, NFC/APDU state transitions, UWB ranging accuracy and attack-resistance limits, radio certification, privacy, interoperability, controller authorization, and physical lock/door acceptance as separate evidence.

## Sources

- **NFC-R15** — [NFC Release 15][NFC-R15], NFC Forum, June 2025.
- **NFC-CR15-LAUNCH** — [NFC Forum launches CR15/TR15.0][NFC-CR15-LAUNCH], NFC Forum, 22 October 2025.
- **NFC-CR15** — [Certification Release 15][NFC-CR15], authorized for use in certification May 2026.
- **NFC-SPECS** — [NFC Forum Specifications][NFC-SPECS], NFC Forum, accessed 2026-08-25.
- **NFC-IEC** — [Two NFC Forum Specifications Adopted as IEC Standards][NFC-IEC], NFC Forum, 5 March 2026.
- **BT63** — [Core Specification 6.3 Adopted][BT63], Bluetooth SIG, May 2026.
- **BT63-OVERVIEW** — [Bluetooth Core 6.3 technical overview][BT63-OVERVIEW], Bluetooth SIG, 2026.
- **BT-CS** — [Bluetooth Channel Sounding][BT-CS], Bluetooth SIG, accessed 2026-08-25.
- **IEEE154** — [IEEE 802.15.4-2024][IEEE154], IEEE Standards Association, active standard published 12 December 2024.
- **IEEE154Z** — [IEEE 802.15.4z-2020][IEEE154Z], IEEE Standards Association, superseded standard.
- **IEEE154AB** — [IEEE P802.15.4ab][IEEE154AB], IEEE Standards Association, active project status accessed 2026-08-25.
- **FIRA4** — [FiRa Consortium Unveils Core 4.0 Specifications and Certification][FIRA4], FiRa Consortium, 3 December 2025.
- **FIRA-CERT** — [FiRa Certification Program][FIRA-CERT], FiRa Consortium, Release 4.0 feature scope accessed 2026-08-25.
- **FIRA-SPECS** — [FiRa UWB Specifications][FIRA-SPECS], FiRa Consortium, accessed 2026-08-25.
- **ALIRO** — [Introducing Aliro 1.0][ALIRO], Connectivity Standards Alliance, 26 February 2026.

[NFC-R15]: https://nfc-forum.org/nfc-release-15
[NFC-CR15-LAUNCH]: https://nfc-forum.org/news/2025-10-nfc-forum-launches-certification-to-support-extended-range-of-contactless-connections/
[NFC-CR15]: https://nfc-forum.org/certification_releases/certification-release-15/
[NFC-SPECS]: https://nfc-forum.org/build/specifications
[NFC-IEC]: https://nfc-forum.org/news/2026-03-two-nfc-forum-specifications-adopted-as-iec-standards/
[BT63]: https://www.bluetooth.com/specifications/specs/core-specification-6-3/
[BT63-OVERVIEW]: https://www.bluetooth.com/bluetooth-core-6-3-technical-overview/
[BT-CS]: https://www.bluetooth.com/learn-about-bluetooth/feature-enhancements/channel-sounding/
[IEEE154]: https://standards.ieee.org/ieee/802.15.4/11041/
[IEEE154Z]: https://standards.ieee.org/ieee/802.15.4z/10230/
[IEEE154AB]: https://standards.ieee.org/ieee/802.15.4ab/10694/
[FIRA4]: https://firaconsortium.org/news/press-releases/2025/12/fira-consortium-unveils-fira-core-4-0-specifications-and-certification
[FIRA-CERT]: https://www.firaconsortium.org/certifications/certification-program
[FIRA-SPECS]: https://www.firaconsortium.org/resource-hub/specifications
[ALIRO]: https://csa-iot.org/newsroom/introducing-aliro-1-0-a-unified-standard-to-transform-the-access-control-ecosystem/
