---
title: "OSDP reader-to-controller protocol"
summary: "Developer and deployment reference for SIA OSDP 2.2.2, ACU/PD communication, RS-485, Secure Channel, conformance, state machines, and migration."
page_type: protocol
domains: [access-control]
tags:
  - osdp
  - rs485
  - secure-channel
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "SIA OSDP Version 2.2.2 (October 2024)"
  - "IEC 60839-11-5:2020"
coverage_limit: "Protocol architecture and defensive commissioning guidance only; licensed wire details, product behavior, wiring values, keys, Secure Channel, ACU/PD, door, and conformance testing are not validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# OSDP reader-to-controller protocol

[Access-control protocols](README.md) / OSDP

The Open Supervised Device Protocol (OSDP) connects an Access Control Unit (ACU) to Peripheral Devices (PDs), such as readers, keypads, supervised I/O, and biometric devices. It is bidirectional, supports supervised communications and remote device functions, and defines Secure Channel for authenticated encrypted communication. [SIA-OSDP]

## Current revision and conformance

SIA released **OSDP 2.2.2 in October 2024**. The international base **IEC 60839-11-5:2020**, edition 1.0, specifies OSDP commands and replies for electronic access control and has an IEC stability date of 2029. SIA's newer revision and its certification profiles are the source to use for current SIA product work. [SIA-OSDP] [IEC-OSDP]

“Supports OSDP” is not the same as **SIA OSDP Verified**. Record:

- ACU or PD role;
- product and exact firmware/hardware version;
- OSDP version/profile and supported capabilities;
- Secure Channel support and production enforcement;
- multi-drop, file transfer, smart-card/biometric, and other required features;
- entry in SIA's Verified-products register.

SIA describes OSDP Verified as third-party conformance/interoperability testing. Verification is product-, role-, version-, and feature-specific. [OSDP-VERIFIED]

## Topology and roles

```text
                 two-wire, half-duplex RS-485 data pair
ACU / control panel ============================================
        | address A: reader/PD
        | address B: reader + keypad/PD
        ` address C: supervised I/O/PD
```

The ACU controls the poll/command sequence; a PD replies when addressed. This makes timeout, retry, address ownership, and fair polling explicit. OSDP commonly uses a multi-drop RS-485 bus, but electrical design—cable, topology, termination, bias, grounding, surge protection, power, distance, and baud rate—must follow the device and site engineering requirements.

The protocol uses a 7-bit address space; `0x7F` is the special broadcast address, leaving addresses `0x00`–`0x7E` for individual PDs. Do not use broadcast for security-sensitive production commands unless the applicable standard/profile explicitly requires it and the risk is understood. [LIBOSDP-API]

## Frame and exchange model

At a high level an OSDP frame contains:

```text
start marker | address/direction | length | control | optional security block
             | command or reply data | checksum or CRC
```

The control field carries sequence/check/security indications. The start marker on the wire is `0x53`. Exact bit/byte rules, maximum sizes, command payloads, timing, and retry behavior are normative in the licensed current standard; do not implement from this summary alone.

Common command/reply families cover:

- poll, acknowledgment, negative acknowledgment, busy, and communication setup;
- PD identity and capabilities;
- local, input, output, and reader status;
- credential/card data and keypad data;
- LED, buzzer, display/text, and output control;
- smart-card/transparent-content exchanges;
- file transfer and manufacturer-specific extensions;
- Secure Channel establishment and key management.

A PD capability report tells what the device claims to implement. It does not authorize the ACU to use a feature or prove the physical installation supports it.

## Secure Channel

OSDP Secure Channel uses AES-128-based mechanisms to authenticate and protect ACU–PD traffic. Production security depends on a unique Secure Channel Base Key (SCBK) per PD, correct establishment, protected key storage, strong randomness, and enforcement after provisioning. SIA says unsecured mode should exist only during initialization before Secure Channel is configured. [SIA-CHECKLIST]

### Provisioning state model

```text
factory / controlled install state
    -> identify exact device and address
    -> establish controlled communication
    -> provision a unique SCBK through the approved process
    -> verify Secure Channel succeeds
    -> disable install/default-key acceptance
    -> enforce encrypted/authenticated operational traffic
    -> monitor loss, reset, replacement, and key rotation
```

Do not publish, log, inventory in plaintext, reuse, or copy a default installation key into documentation or configuration examples.

### Key management requirements

- Generate keys with an approved cryptographic random source or managed KDF under a root-key/HSM design.
- Keep each PD's key distinct; bind it to device identity, address/bus, site, firmware, and lifecycle record.
- Protect keys at rest and while provisioned; restrict read/export and audit use.
- Define replacement and factory-reset behavior. A replacement device at the same address is not the same cryptographic peer.
- Define rotation, escrow/recovery if allowed, loss, compromise, and secure destruction.
- Fail closed on unexpected fallback from Secure Channel, while preserving life-safety egress and an authorized recovery procedure.
- Monitor repeated authentication failures, address identity changes, CRC/noise bursts, unexpected reset, and capability changes.

## ACU implementation model

Maintain per-PD state, not just per serial port:

```text
configured -> discovering/identifying -> capability exchange
           -> secure-channel setup -> online/operational
           -> degraded/retrying -> offline/recovering
```

Per-PD state should include address, expected identity, capabilities, sequence, negotiated check mode, secure-channel state, outstanding command, retry/deadline, last authenticated response, counters, and firmware/configuration metadata.

### Parser rules

- Accumulate partial serial reads and locate a valid start only under bounded resynchronization rules.
- Validate address, declared length, control bits, security-block consistency, sequence, and checksum/CRC before dispatch.
- Enforce the current standard's frame maximum before allocation.
- Authenticate/decrypt before interpreting protected application data.
- Do not deliver duplicate credential/keypad events on a retransmitted reply.
- Rate-limit NAK/BUSY/retry loops and avoid letting one PD starve the bus.
- Treat manufacturer-specific payloads as separately bounded schemas.
- Zeroize ephemeral key material and never emit keys or plaintext credentials in diagnostics.

## Safe offline frame-validation shape

**Target:** Authorized implementation review, not a wire tool.

**Inputs:** A frame already supplied by a controlled unit test.

**Side effects:** None.

```text
validate(frame):
  require minimum_header <= frame.length <= configured_max
  require frame.start_marker == 0x53
  require declared_length == frame.length
  require address_is_expected(frame.address)
  require control_bits_are_consistent(frame.control)
  require checksum_or_crc_is_valid(frame)
  if security_block_present(frame):
      plaintext = authenticate_then_decrypt(frame, peer_session)
      require sequence_is_expected(peer_session, frame)
      dispatch_bounded_reply(plaintext)
  else:
      require peer_is_in_explicit_install_or_allowed_clear_state
      dispatch_bounded_reply(frame.payload)
```

Real processing order and retransmission rules must follow SIA OSDP 2.2.2.

## Bus scheduling and supervision

- Poll frequently enough to meet status/alarm latency while reserving time for commands and slow devices.
- Use per-command deadlines based on standard/device behavior; file transfer is not a normal poll latency.
- Mark a PD degraded/offline only under a defined missed-response policy.
- Separate communication health from door/reader physical state.
- Measure collision/noise/retry rates and response latency by address.
- After reconnect, reidentify the device and reestablish Secure Channel before accepting credential or keypad data.
- Do not silently continue cleartext because secure establishment failed.

## High-impact functions

LED/text/buzzer commands are low physical impact but can deceive users. Output/relay control, firmware/file transfer, configuration, key changes, and address/baud changes can cause denial of access or unsafe operation. Apply separate roles, maintenance windows, signed firmware/provenance checks, rollback, audit, and local safety controls.

## Wiring and commissioning

SIA's 2026 implementation checklist calls for OSDP Verified PDs and ACUs, Secure Channel, suitable two-wire RS-485 cabling, unique documented addresses, bench staging, and post-install performance validation. It also recommends cataloging address, speed, firmware, location, cable, interface, and keys. Store only a key reference/fingerprint in ordinary documentation—not the secret itself. [SIA-CHECKLIST]

Environment acceptance should cover:

- minimum/maximum supported baud and bus loading;
- every installed PD model/firmware and required feature;
- power-up, brownout, cable open/short, termination error, duplicate address, noise, and device replacement;
- Secure Channel success, prohibited fallback, wrong-key behavior, and factory reset/reprovision;
- credential/keypad duplicate suppression under lost reply/retry;
- controller restart, PD restart, long outage, file-transfer interruption, and upgrade rollback;
- tamper, status, LED, buzzer, display, input/output, and event latency.

## Migration from legacy interfaces

1. Inventory reader, credential technology/format, panel, wiring, power, door behavior, and life-safety dependencies.
2. Confirm exact OSDP Verified roles/firmware and Secure Channel support.
3. Bench-stage reader plus actual ACU with production-like bus length/load.
4. Assign and document unique PD addresses and cryptographic identities.
5. Install in phases with rollback and outage communication.
6. Verify Secure Channel is active—not merely configured—and cleartext fallback is blocked.
7. Retire converters/legacy input where possible; a Wiegand bridge preserves the legacy weak link on one side.

## Review checklist

- [ ] SIA OSDP 2.2.2 and exact Verified product/firmware/profile recorded
- [ ] RS-485 topology, cable, termination, bias, grounding, surge, power, and baud engineered
- [ ] Unique PD address and expected device identity bound in inventory
- [ ] Unique per-PD SCBK generated, protected, rotated, and never logged
- [ ] Install/default-key state disabled after controlled provisioning
- [ ] Cleartext operational fallback prohibited
- [ ] Per-PD sequence, timeout, retry, duplicate, offline, and fairness state bounded
- [ ] Parser length/control/check/security validation occurs before dispatch/allocation
- [ ] Credential/keypad data, relay/output, file transfer, configuration, and key changes separately authorized/audited
- [ ] Acceptance evidence covers physical behaviour, Secure Channel, failure recovery, and safe-state handling

## Environment validation

Purchase and implement against SIA OSDP 2.2.2 and applicable conformance documents. Record OSDP Test Tool results, exact PD/ACU firmware and Verified profiles, bus measurements, key-ceremony evidence, Secure Channel establishment and prohibited-fallback results, fault recovery, and physical safe-state acceptance.

## Sources

- **SIA-OSDP** — [Open Supervised Device Protocol][SIA-OSDP], Security Industry Association, revision/status accessed 2026-08-25.
- **IEC-OSDP** — [IEC 60839-11-5:2020][IEC-OSDP], IEC, edition 1.0, published 8 July 2020.
- **OSDP-VERIFIED** — [SIA OSDP Verified Products][OSDP-VERIFIED], Security Industry Association, accessed 2026-08-25.
- **SIA-CHECKLIST** — [Implementing OSDP Access Control? Follow This Simple Checklist][SIA-CHECKLIST], Security Industry Association, 10 February 2026.
- **SIA-CREDENTIAL-GUIDE** — [Corporate Credential Design Guide][SIA-CREDENTIAL-GUIDE], Security Industry Association, March 2026.
- **LIBOSDP-API** — [LibOSDP public API and address model][LIBOSDP-API], open-source implementation documentation, accessed 2026-08-25; informative, not the normative standard.

[SIA-OSDP]: https://www.securityindustry.org/industry-standards/open-supervised-device-protocol/
[IEC-OSDP]: https://webstore.iec.ch/en/publication/33414
[OSDP-VERIFIED]: https://www.securityindustry.org/industry-standards/open-supervised-device-protocol/sia-osdp-verified/sia-osdp-verified-products/
[SIA-CHECKLIST]: https://www.securityindustry.org/2026/02/10/implementing-osdp-access-control-follow-this-simple-checklist/
[SIA-CREDENTIAL-GUIDE]: https://www.securityindustry.org/wp-content/uploads/2026/03/SIA_CorporateCredentialDesignGuide.pdf
[LIBOSDP-API]: https://github.com/osdp-dev/libosdp/blob/master/include/osdp.h
