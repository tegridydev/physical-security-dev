---
title: Power, USB, and GPIO
summary: PoE, USB device trust, GPIO electrical contracts, relays, dry contacts, supervised circuits, and safe hardware integration.
page_type: reference
domains: [ot, networking, cross-domain]
tags: [poe, usb, gpio, relay, dry-contact, supervised-circuit]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [IEEE 802.3-2022, USB 2.0 Specification]
coverage_limit: Conceptual interface guidance only; electrical ratings, wiring, supervision values, safety certification, and pinouts must come from current product and site documentation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Power, USB, and GPIO

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / Power, USB, and GPIO

Power and discrete wiring are operational interfaces, not incidental plumbing. A software-controlled PoE port, USB peripheral, GPIO, or relay can reboot devices, suppress supervision, energize a lock, or damage hardware.

## Power over Ethernet

IEEE 802.3 includes PoE power-sourcing equipment (PSE) and powered-device (PD) behaviour.[^poe] Record PSE/PD standard support, negotiated/class power, cable pairs and topology, switch/port budget, inrush/startup, LLDP power negotiation if used, UPS/generator domain, environmental derating, midspans, redundant feeds, and downstream accessories.

Do not use a headline wattage as an available-load guarantee. Budget worst-case device, heater/IR/illuminator, USB/accessory load, cable loss, simultaneous restart, and switch total. Monitor negotiated versus drawn power, denial/overload, short/ground fault, port cycle, and UPS state.

Treat remote PoE cycling as a high-impact administrative command: authorize the exact port/device, warn about dependent services, serialize fleet operations, confirm recovery from application health, and audit reason/operator/result. Never “fix” an unknown camera or controller by repeatedly cycling it.

## USB

USB is a host-controlled bus with descriptors, configurations, interfaces, endpoints, classes, and potentially alternate modes—not a trusted cable. USB-IF publishes the USB 2.0 specification and current documents.[^usb]

- Allowlist required class, vendor/product identity, serial and interface where the platform supports it; descriptors are attacker-controlled and identifiers can be cloned.
- Disable unused mass-storage, HID, network, debug, firmware-update, and serial classes. A device presenting several functions expands trust.
- Separate power-only charging from data with purpose-built approved hardware; do not assume an untrusted “charge” port lacks data.
- Validate all lengths, endpoint sizes, transfers, timeouts, disconnect/reconnect, and descriptor nesting in host software.
- Protect update/import files by signature/hash/schema and an authorization workflow. Successful copying is not safe application.

## GPIO

GPIO has no universal wire protocol. A complete contract specifies voltage domain, absolute maximum, input thresholds, output current, source/sink direction, push-pull/open-drain/open-collector, pull-up/down, active level, boot/reset/high-impedance state, debounce/filter, edge/level semantics, isolation, transient protection, ground/reference, connector/pinout, and failure state.

Never connect a nominal “3.3 V” GPIO to a panel input or relay coil without interface design. Use rated opto-isolation, transistor/driver, flyback protection, level shifting, and fusing as required. Safe defaults must exist in hardware where software boot delay/crash could energize an output.

## Relays, dry contacts, and supervised circuits

`NO`, `NC`, and `COM` describe contact state relative to an unenergized relay, not the security meaning. Record energized/de-energized truth table, fail-safe/fail-secure behaviour, contact rating and load type, wet/dry expectation, latching, pulse duration, feedback, and fire/egress interface approval.

A supervised input may distinguish normal, alarm, open, short, and tamper using one or more end-of-line resistors. Values and topology are panel-specific; software must preserve all states rather than reduce them to a boolean. Place end-of-line components where the design detects cable tamper, not conveniently at the controller unless specified.

Relay operation is not proof that a door moved or became secure. Correlate independent position/bolt/lock-power sensors under a defined state machine. Do not bypass supervised, fire-release, request-to-exit, anti-passback, or safe-egress circuits.

Validate PoE cycling, USB insertion/removal, GPIO levels, supervision states, relay interlocks, loss of power, and recovery on an electrically safe isolated bench.

## Primary sources

[^poe]: [IEEE Standards Association — IEEE 802.3-2022](https://standards.ieee.org/ieee/802.3/10422/)
[^usb]: [USB-IF — USB 2.0 specification](https://www.usb.org/document-library/usb-20-specification)
- [USB-IF — document library](https://www.usb.org/documents)
