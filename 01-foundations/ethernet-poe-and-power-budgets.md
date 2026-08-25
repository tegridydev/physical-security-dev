---
title: Ethernet, PoE, and Power Budgets
summary: Ethernet links, standards-based Power over Ethernet, power sourcing, negotiation, thermal/load planning, and outage behaviour.
page_type: foundation
domains: [video, access-control, intercom, bms, ot]
tags: [ethernet, poe, power, switches, cabling]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [IEEE 802.3-2022]
coverage_limit: Conceptual planning only; cable, electrical, fire-rating, UPS, and installation requirements are jurisdiction and site specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Ethernet, PoE, and power budgets

Power over Ethernet (PoE) can simplify cameras, readers, intercoms, and edge devices, but “the switch has enough watts” is not a complete availability design.

## Roles and standards

- **Power sourcing equipment (PSE):** switch or midspan that supplies power.
- **Powered device (PD):** device that requests/uses power.
- **Endpoint versus midspan:** where power is injected.
- **Class/signature:** negotiation/classification information used to allocate power.

IEEE [802.3-2022](https://standards.ieee.org/ieee/802.3/10422/) is the active Ethernet base standard at this review date and incorporates power over selected twisted-pair PHYs, including earlier 802.3af/at/bt work. The Ethernet Alliance [PoE Certification Program](https://ethernetalliance.org/poecert/) distinguishes products tested against IEEE-based Gen 1 and Gen 2 plans. Marketing names such as “PoE+” or “PoE++” are not enough; verify the exact IEEE type/class, PSE mode, PD signature, and supported cabling.

## End-to-end power budget

For each PD record:

```text
minimum and maximum input power
negotiated class and fallback behaviour
heater, IR, PTZ, audio, relay, USB, or accessory peaks
cable length/gauge/category and bundle/ambient limits
switch per-port and total budget
power-supply and UPS capacity at normal and degraded temperature
redundancy/failover behaviour
boot surge and simultaneous restart policy
```

Distinguish PSE output from power available at the PD after cable loss. Do not mix proprietary passive power with standards-based PoE unless both endpoints and the approved design explicitly support it; incorrect powering can damage equipment.

## Availability traps

- All high-draw functions activate together at night or cold temperature.
- A redundant switch has ports but not equal PoE capacity.
- UPS runtime calculations omit switch/PSE losses and battery aging.
- Power restoration boots all devices simultaneously, causing surge and network/control-plane load.
- A camera link remains up while the heater, illuminator, or motor is power-limited.
- Link Layer Discovery Protocol (LLDP) power negotiation differs after firmware/configuration changes.
- Midspan or media-converter behaviour is absent from monitoring.

## Network and physical security

PoE restart is a remote actuation: it can interrupt recording, intercom, access readers, or sensors. Restrict switch power-cycle permissions and audit them. Do not use power cycling as a generic recovery loop without bounds and state awareness.

Switch port security, IEEE 802.1X, VLAN assignment, and certificate identity solve different problems. A powered and linked device is not authenticated. Protect accessible cable endpoints and cabinets from substitution or unauthorized bridging.

## Monitoring

Collect negotiated class, actual draw, budget remaining, overload/deny events, link flaps, temperature, PSU/UPS state, and restart cause. Correlate power loss with device gaps but retain uncertainty: a switch report is not proof of downstream function.
