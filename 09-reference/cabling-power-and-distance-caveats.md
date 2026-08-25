---
title: "Cabling, power, and distance caveats"
summary: "A topology-first worksheet for cable, distance, signal integrity, power delivery, grounding, environment, and standards-bound physical-layer decisions."
page_type: reference
domains:
  - infrastructure
  - cross-domain
tags:
  - cabling
  - power
  - distance
  - poe
  - serial
  - physical-layer
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "IEEE 802.3-2022"
  - "TIA-485-A"
  - "SIA OSDP 2.2.2"
coverage_limit: "Engineering caveats and formulas only; no universal cable length, conductor size, PoE budget, termination, grounding, separation, fire rating, or electrical-code conclusion is supplied."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Cabling, power, and distance caveats

[Home](../README.md) / [Reference](README.md) / Cabling, power, and distance caveats

> There is no safe universal “maximum distance” table. Distance is a property of an exact PHY, cable and connector channel, data rate/timing, topology, transceivers, loading, environment, installation, power requirement, standard edition, and product limits.

This page does not approve electrical work. Follow the applicable standards, manufacturer instructions, qualified designer/installer, electrical and fire codes, accessibility rules, and authority having jurisdiction (AHJ). Life-safety, egress, fire, lift, gate, lock, and mains decisions require the responsible qualified parties.

## Required physical-layer record

| Category | Record before design or connection |
|---|---|
| Standard/profile | Exact PHY/electrical/cabling standard edition, application profile, product conformance |
| Endpoints | Models, firmware, port/transceiver types, isolation, termination/bias responsibility |
| Topology | Point-to-point, multidrop bus, star through active switch/hub, ring, spur/stub, redundant path |
| Channel | Installed cable type/category, conductor material/gauge, pair/twist, shield/drain, connectors, patching, joints |
| Lengths | Permanent link/channel, every segment and stub, elevation/riser, service loop—not an estimate alone |
| Signaling | Data rate, encoding, duplex, timing, common-mode range, impedance, loss/return loss/noise budget |
| Power | Source/PSE, load/PD min/max/peak, voltage range, class/negotiation, cable loss, conversion loss, UPS |
| Environment | Temperature, bundle size, enclosure, moisture, UV, lightning/surge, EMI, hazardous area, vibration |
| Grounding | Reference conductor, bonding, shield termination, isolation, earth-potential difference, surge path |
| Compliance | Cable fire rating, segregation, pathway/fill, penetrations, regional code, AHJ/engineer approval |
| Evidence | Design calculation, standard clause, product manual, test instrument/method, owner acceptance date |

## Technology caveats

| Technology | Familiar shorthand to avoid | Correct decision boundary |
|---|---|---|
| Balanced-copper Ethernet | “Ethernet is always 100 m” | Many common twisted-pair Ethernet PHY/cabling channels use a 100 m channel design, but supported length depends on exact PHY, category/channel construction, connectors, temperature, PoE, and product; some PHYs differ materially |
| Fiber Ethernet | “Fiber goes X km” | Fiber type, wavelength, launch/receive budget, connector/splice loss, dispersion, transceiver class, FEC, temperature, and regulatory laser requirements determine reach |
| PoE | “The switch says 30/60/90 W, so the device gets that” | IEEE type/class, PSE/PD negotiation, pair set, cable/channel loss, LLDP, temperature/bundle, switch total budget, conversion and failover determine available input power |
| Passive/proprietary power | “It uses an RJ45, so it is PoE” | Connector does not identify powering; passive voltage on data pairs can damage equipment. Require exact pinout/voltage/polarity and approved pairing |
| TIA-485 / RS-485 | “RS-485 is always 1200 m” | Standard defines an electrical interface, not one universal length; data rate, cable, loading, topology, termination, common mode, isolation, and application timing control reach |
| OSDP | “OSDP guarantees a long bus” | OSDP is an application/link profile over a suitable 2-wire RS-485 channel; exact ACU/PD count, baud, cable, power, topology and manufacturer constraints require design and bench/site validation |
| BACnet MS/TP | “Any RS-485 wiring works” | Token timing, MACs, baud, max master, router loading, cable/bias/termination and node electrical characteristics must all match |
| Modbus RTU | “Modbus defines the wire” | Modbus application/serial guide and chosen TIA-232/485 implementation are separate; product timing and framing matter |
| Wiegand / Clock-and-Data | “The format defines distance” | Bit format does not define electrical channel; reader/panel manuals, cable capacitance, supply loss, ground reference, pulse timing and environment own the limit |
| KNX TP | “Twisted pair is interchangeable” | Use KNX-certified/approved medium, topology, segment, power supply/choke and product rules; ordinary generic bus assumptions are insufficient |
| CAN/CANopen/J1939 | “CAN rate alone gives distance” | Bit timing, topology/stubs, cable, transceivers, termination, propagation and application profile define the network |
| USB | “The connector/version name gives cable reach and power” | USB data rate/generation, active/passive cable, cable assembly certification, Type-C current negotiation/PD, hubs and product role all matter |
| Dry contact / supervised input | “It is only open or closed” | Voltage/current, wet/dry source, EOL topology/value/tolerance, line monitoring, isolation and connected function define semantics and safety |
| Radio | “Range is a specification constant” | Region, antenna, orientation, body/building attenuation, interference, power, data rate, coexistence, certification and threat model govern observed range |

Use [serial and field interfaces](../01-foundations/serial-and-field-interfaces.md), [Ethernet, PoE, and power budgets](../01-foundations/ethernet-poe-and-power-budgets.md), [dry contacts and supervised circuits](../01-foundations/dry-contacts-and-supervised-circuits.md), and [wireless and radio fundamentals](../01-foundations/wireless-and-radio-fundamentals.md).

## DC voltage-drop model

For a simple two-conductor DC circuit:

```text
R_loop = resistance_outbound + resistance_return
V_drop = I_load × R_loop
V_at_load = V_source_min - V_drop - other_series_losses
P_at_load = V_at_load × I_load
```

This is an orientation formula, not a complete design. Account for:

- conductor resistance at maximum operating temperature and actual conductor material/gauge;
- connector, fuse, protection, distribution, and contact resistance;
- steady, boot, heater, IR illuminator, motor, audio, relay, lock and accessory peaks;
- shared-return/common conductors and simultaneous loads;
- source tolerance, battery discharge, UPS/converter efficiency, and low-temperature behavior;
- device minimum input voltage at the required load and transient behavior;
- code-required overcurrent protection, voltage class, separation, derating, and fire performance.

Never increase voltage, bypass protection, parallel outputs, or change conductor arrangements from a desk calculation. A qualified electrical design and approved product instructions own those decisions.

## PoE budget chain

```text
utility / generator / UPS
        ↓
switch PSU capacity and redundancy
        ↓
PSE total budget and per-port negotiated state
        ↓
cable/channel loss and temperature
        ↓
PD input and conversion
        ↓
camera/reader/intercom plus heater, IR, motor, relay, USB
```

Record both normal and degraded/failover budgets. Common failure cases include:

- all heaters/illuminators/motors starting together;
- a redundant switch or PSU lacking equivalent PoE capacity;
- LLDP/class negotiation changing after firmware/configuration;
- a link remaining up while a high-draw function browns out;
- simultaneous restoration causing boot surge and network/authentication load;
- UPS runtime based on nameplate load rather than measured full path and aged battery;
- a midspan, extender, surge protector, media converter, or patching element absent from the channel record.

Remote PoE cycle is actuation: it can interrupt recording, door readers, intercom, sensors, or alarms. Gate it through the [safety impact checklist](safety-impact-checklist.md).

## Serial multidrop design questions

- Which node owns termination at each physical end, and are there exactly the intended terminations?
- Which device/network owns bias/failsafe state?
- What is the maximum stub length under the exact rate/topology/product—not a generic rule?
- Is a reference conductor required, and what common-mode range applies?
- Where is galvanic isolation and surge protection required?
- Does any adapter or gateway transmit during boot, discovery, driver installation, reconnect, or configuration?
- How are duplicate addresses, simultaneous transmitters, token loss, turnaround, and retries detected?
- Does bus power share conductors or reference with signaling, and what is its worst-case drop?
- How will passive observation avoid changing termination/bias/loading?

See [serial transports](../02-protocols/infrastructure/serial-transports.md), [OSDP](../02-protocols/access-control/osdp.md), and [BACnet MS/TP](../02-protocols/building-and-industrial/bacnet-ms-tp.md).

## Acceptance evidence

| Stage | Evidence—not assumption |
|---|---|
| Design | Standard/profile and product manual clauses; topology; signal/power/loss/thermal calculations; qualified approval |
| Installation | Cable/connector IDs, route, measured length, labeling, termination/bias/shield/ground record, inspection |
| Certification | Appropriate cable/optical/electrical test report for the specified channel and limits |
| Functional environment validation | Normal/peak/failure behavior, errors, negotiated power/link state, restart and recovery |
| Operations | Baseline counters/telemetry, change record, spare compatibility, periodic inspection/test plan |

A continuity test alone does not certify a data channel. Link-up does not prove error margin. A protocol reply does not prove power headroom or safe physical behavior.

## Mandatory deferral and stop conditions

Stop and defer to the manufacturer, qualified engineer/installer, AHJ, and responsible system owner when:

- voltage, pinout, polarity, wet/dry contact, signal standard, or power source is unknown;
- mains, batteries, fire-rated pathways, lightning/surge, hazardous locations, or building penetrations are involved;
- work can interrupt egress, locks, gates, lifts, fire/emergency systems, alarms, dispatch, or recording obligations;
- grounding/bonding/earth-potential difference is unresolved;
- the proposed distance exceeds an exact standard/product channel or depends on undocumented extenders;
- two products claim the same connector but not the same electrical/power profile;
- approval, rollback, isolation, and witnessed acceptance are absent.

This reference supplies planning boundaries; connection, measurement, certification, and functional acceptance require qualified site procedures and retained environment evidence.

## Sources

- **IEEE8023** — [IEEE 802.3-2022 Ethernet Standard][IEEE8023], IEEE Standards Association; amendments and current project status must be checked at use time.
- **IEEE-POE** — [IEEE 802.3 Power over Ethernet information][IEEE-POE], IEEE 802.3 working group, accessed 2026-08-25.
- **TIA** — [TIA standards catalogue and purchase path][TIA], Telecommunications Industry Association, accessed 2026-08-25.
- **SIA-OSDP** — [Open Supervised Device Protocol][SIA-OSDP], Security Industry Association, accessed 2026-08-25.
- **SIA-OSDP-CHECK** — [Implementing OSDP Access Control? Follow This Simple Checklist][SIA-OSDP-CHECK], Security Industry Association, 10 February 2026.
- **BACNET-MSTP** — [BACnet MS/TP technical bulletin][BACNET-MSTP], ASHRAE BACnet Committee.
- **MODBUS-SERIAL** — [Modbus over Serial Line Specification and Implementation Guide V1.02][MODBUS-SERIAL], Modbus Organization.
- **USB** — [USB-IF specifications and compliance resources][USB], USB Implementers Forum, accessed 2026-08-25.

[IEEE8023]: https://standards.ieee.org/ieee/802.3/10422/
[IEEE-POE]: https://www.ieee802.org/3/bt/
[TIA]: https://tiaonline.org/products-and-services/buy-standards/
[SIA-OSDP]: https://www.securityindustry.org/industry-standards/open-supervised-device-protocol/
[SIA-OSDP-CHECK]: https://www.securityindustry.org/2026/02/10/implementing-osdp-access-control-follow-this-simple-checklist/
[BACNET-MSTP]: https://bacnet.org/wp-content/uploads/sites/4/2022/06/STB-08-93.pdf
[MODBUS-SERIAL]: https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf
[USB]: https://www.usb.org/documents
