---
title: Wireless and low-power links
summary: Wi-Fi, Bluetooth, Zigbee, Thread, Z-Wave, LoRaWAN, NFC, radio commissioning, key lifecycle, and coexistence guidance.
page_type: reference
domains: [networking, ot, cross-domain]
tags: [wifi, bluetooth, zigbee, thread, zwave, lorawan, nfc, wireless]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [IEEE 802.11-2024, Bluetooth Core 6.3, Thread 1.4.1, LoRaWAN 1.0.4, Zigbee R23.2]
coverage_limit: Family-level baseline; exact regional radio rules, profiles, commissioning method, security revision, certification, and product capabilities must be verified per deployment.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Wireless and low-power links

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / Wireless and low-power

Radio reach is variable and crosses walls, fences, vehicles, and tenancy boundaries. Signal strength is neither identity nor authorization. Design for eavesdropping, rogue transmitters, interference, replay/jamming symptoms, battery exhaustion, gateway compromise, and loss of the cloud or border router.

## Family map

| Family | Integration model | Security/configuration questions |
|---|---|---|
| Wi-Fi | 802.11 LAN carrying IP protocols | personal versus enterprise authentication, 802.1X method, protected management, client isolation, roaming, VLAN policy |
| Bluetooth LE | GAP discovery/connection, GATT services/characteristics, optional mesh/profile layers | exact Core/profile version, association method, bonding, MITM protection, privacy addresses, key storage, authorization per characteristic |
| Zigbee | coordinator/trust-centre, router/end-device mesh, clusters and profiles | install/link/network keys, joining policy, key update, device/cluster revision, group and binding scope |
| Thread | IPv6 mesh with border router; application layer is separate | network credentials, commissioning owner, border-router redundancy, partitioning, backbone exposure, application security |
| Z-Wave | controller-managed sub-GHz mesh and command classes | S2 class/DSK, inclusion/exclusion authority, command-class security, controller backup/replacement |
| LoRaWAN | end device, gateways, network/application servers | OTAA/ABP, root/session keys, frame counters, join/rejoin, regional parameters, confirmed-message limits |
| NFC | very-short-range reader/writer, card emulation, peer modes | tag/credential authenticity, relay risk, secure element/application protocol, anti-cloning and transaction freshness |

IEEE lists 802.11-2024 as the current base wireless LAN standard.[^wifi] Bluetooth SIG adopted Core 6.3 in May 2026, but deployed products may qualify against earlier supported editions; profile and security-feature support matter more than the marketing version alone.[^bt] Thread Group publishes Thread 1.4.1 resources.[^thread] CSA's download page is the authoritative place to check current Zigbee and Matter specifications.[^csa]

## Commissioning and keys

- Make join/inclusion windows short, local, operator-authorized, and auditable. A button press is not sufficient audit identity.
- Use unique install codes/DSKs/device credentials; never publish QR/setup codes or copy fleet keys into logs and tickets.
- Authenticate the network/controller/border router to the joining device where the protocol permits; otherwise rogue infrastructure may capture credentials.
- Record fabric/network ID, device immutable identity, radio address history, assigned role, profile/schema revision, security level, key epoch, commissioner, and evidence.
- Test removal, loss, controller replacement, key rotation, replay/counter persistence after reset, factory reset, and decommissioning on a bench.

Z-Wave Alliance states S2 has been mandatory for new certifications since 2017, but actual inclusion security still needs evidence from the controller/device transaction and certification record.[^zwave] LoRa Alliance publishes the LoRaWAN 1.0.4 package; select the exact regional parameters and backend interfaces separately.[^lora]

## Availability and semantics

Budget airtime, duty cycle, channel occupancy, retry, mesh depth, sleeping intervals, battery, gateway queueing, and backhaul outage. Avoid turning every loss into an immediate alarm storm. Conversely, do not show a cached battery device value as live without an age/quality indicator.

Wi-Fi/Bluetooth/802.15.4 coexistence in 2.4 GHz, metal enclosures, moving vehicles, weather, antenna placement, and deliberate interference can change performance after commissioning. Use site-approved spectrum/RF assessment and country-specific regulatory settings; never raise power or change channel plans outside local rules.

Wireless must not be the sole path for life-safety or safe egress unless the complete certified system explicitly supports it. Validate pairing/join policy, interference, range boundaries, coexistence, loss, recovery, and regional radio compliance in an authorized environment.

## Primary sources

[^wifi]: [IEEE Standards Association — IEEE 802.11-2024](https://standards.ieee.org/ieee/802.11/10548/)
[^bt]: [Bluetooth SIG — Bluetooth Core 6.3 release](https://www.bluetooth.com/blog/just-released-bluetooth-core-6-3/)
[^thread]: [Thread Group — specifications and technical resources](https://threadgroup.org/resources)
[^csa]: [Connectivity Standards Alliance — specification downloads](https://csa-iot.org/developer-resource/specifications-download-request/)
[^zwave]: [Z-Wave Alliance — S2/DSK certification guidance](https://marketcert.z-wavealliance.org/help/Step7-Security2DSKInformation.html)
[^lora]: [LoRa Alliance — LoRaWAN 1.0.4 specification package](https://lora-alliance.org/resource_hub/lorawan-104-specification-package/)
- [Z-Wave Alliance — developer specifications](https://z-wavealliance.org/development-resources-overview/specification-for-developers/)
- [NFC Forum — technical specifications](https://nfc-forum.org/build/specifications/)
