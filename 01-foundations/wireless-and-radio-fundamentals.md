---
title: Wireless and Radio Fundamentals
summary: Threats, ranging limits, coexistence, power, privacy, and lifecycle considerations for Wi-Fi, cellular, BLE, NFC, UWB, and low-power radio.
page_type: foundation
domains: [video, access-control, alarms, intercom, bms, ot]
tags: [wireless, radio, wifi, cellular, ble, nfc, uwb]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [Bluetooth Core Specification, NFC Forum Specifications]
coverage_limit: Technology overview only; spectrum rules, certification, profiles, and product implementations vary by region and version.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Wireless and radio fundamentals

Radio replaces a cable with a shared, observable, interference-prone medium. Short nominal range is not an access-control boundary; directional antennas, relays, obstructions, reflections, and receiver sensitivity change what is reachable.

## Technology roles

| Family | Common security use | Core design concern |
|---|---|---|
| Wi-Fi | cameras, intercoms, gateways, management | WLAN identity, roaming, airtime, interference, power |
| Cellular | remote alarms, temporary/mobile video, backup paths | carrier/APN, coverage, SIM/eSIM lifecycle, data limits, outage |
| Bluetooth Low Energy | mobile credentials, configuration, presence | pairing/bonding, application crypto, privacy addresses, relay/ranging assumptions |
| NFC/contactless | cards, mobile credentials, provisioning | application/card security, reader trust, key management—not distance alone |
| Ultra-wideband | precise ranging/presence/vehicle access | secure ranging implementation, fallback paths, device support |
| LoRaWAN/low-power sub-GHz | sparse sensors and remote telemetry | low bandwidth/duty cycle, join/key lifecycle, gateway dependency |
| Zigbee/Thread/Z-Wave | residential/light-commercial sensors | ecosystem version, commissioning trust, mesh routing, key rotation |

The Bluetooth SIG publishes [adopted specifications](https://www.bluetooth.com/specifications/specs/); a core-version claim alone does not say which Generic Attribute Profile (GATT), security, direction-finding, or channel-sounding features a product implements. The NFC Forum [specification architecture](https://nfc-forum.org/build/specifications/) spans analog/digital, modes, data formats, and test specifications; “NFC” likewise does not identify credential security.

## Threat model

Consider passive observation, traffic analysis, spoofing, replay, relay, downgrade, rogue enrollment, lost/stolen phones, cloned application data, tracking, interference/jamming, battery exhaustion, malicious advertisements, and compromised gateway/cloud accounts.

Radio-layer encryption may terminate before the application. Use application/device authentication and freshness/replay controls appropriate to the operation. For mobile access, bind the credential to secure device storage and a revocable lifecycle; do not base an unlock decision only on signal strength or “device nearby.”

## Ranging and presence

Received signal strength is affected by body position, walls, antennas, multipath, transmit power, and attackers; it is not a reliable distance measurement. Time-of-flight/channel-sounding technologies can improve ranging but only provide security when the complete protocol, hardware, key establishment, fallback, and decision policy resist manipulation.

Distinguish:

- device detected;
- credential authenticated;
- distance estimate with uncertainty;
- user intent/presence policy;
- access authorization;
- physical passage.

## Availability

Survey normal and degraded RF conditions, co-channel use, roaming, coverage holes, shielding, antenna placement, and interference sources. Define what local controllers do during radio, gateway, WAN, carrier, cloud, GPS/time, or battery loss. Jamming cannot be made impossible; detect degraded service and retain an approved alternative path.

## Privacy and lifecycle

Wireless identifiers and probe/advertisement patterns can track people or devices. Minimize stable broadcast identifiers, rotate privacy addresses where the protocol supports it, restrict scan/telemetry retention, and document purpose and consent/legal basis.

Inventory radio module, firmware, protocol/profile versions, regional configuration, certificates/keys, carrier/subscription, and update/end-of-support dates. Verify local radio and installation rules before deployment.

