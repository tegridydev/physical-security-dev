---
title: Panels, Readers, and Door I/O
summary: Controller/peripheral topology, OSDP and legacy reader paths, door-state semantics, supervision, power, tamper, and safe gateways.
page_type: system
domains: [access-control]
tags: [controllers, panels, readers, osdp, door-io]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 60839-11-5:2020", SIA OSDP 2.2.2]
coverage_limit: Architecture and semantics only; no live wiring values, key material, credential capture, relay actuation, or door commissioning procedure.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Panels, readers, and door I/O

The field controller enforces local access logic and drives/senses door hardware. Reader, lock output, door contact, request-to-exit (RTE), lock monitor, tamper, power, and emergency inputs are separate channels with distinct meaning.

## Typical door topology

```text
credential <-> reader/peripheral <-> controller/panel
                                      |- lock/output
                                      |- door-position input
                                      |- RTE input
                                      |- lock monitor/tamper
                                      `- emergency/fire interface (approved boundary)
```

The exact design may use intelligent locks/readers, distributed I/O, wireless gateways, elevator modules, or nested controllers. Inventory which component decides, caches policy, timestamps, and stores events.

## Reader channel

SIA's [OSDP page](https://www.securityindustry.org/industry-standards/open-supervised-device-protocol/) describes bidirectional supervised panel/peripheral communication, Secure Channel, smart-card/biometric support, current SIA edition 2.2.2, and OSDP Verified. [IEC 60839-11-5:2020](https://webstore.iec.ch/en/publication/33414) is the international OSDP publication.

For new supported designs prefer OSDP Secure Channel with per-deployment key management, device identity/installation process, correct RS-485 topology, supervision, and verified interoperability. “OSDP capable” does not prove secure mode is enabled, default keys were replaced, or all features interoperate.

Legacy Wiegand/Clock-and-Data typically transfers identifier bits without modern bidirectional supervision or cryptographic protection. Contain it physically, shorten exposure, monitor tamper, avoid using low-assurance identifiers for high-risk access, and plan migration. Do not capture or replay live credential traffic.

## Door-state semantics

Keep independent:

- access decision and reason;
- lock-output command/electrical state;
- lock-monitor state if installed;
- door-position contact;
- RTE/egress input;
- forced/held/open-too-long logic;
- passage/occupancy inference;
- tamper, power, battery, bus, and controller health.

Door open while output is secure may be forced, mechanically keyed, emergency-released, miswired, or stale; context is required. A “normal” contact cannot prove latch engagement.

## Timing and failure

Define unlock duration, door-open/held timers, RTE timing, debounce, reader feedback, re-lock conditions, and behavior on controller/bus/power loss using approved system design. Software integrations should request a named high-level operation, not toggle a raw relay.

After an ambiguous command timeout, query controller and independent input state before any retry. Bound unlock/relay commands and require site/resource authorization, reason, audit, and where appropriate dual control.

## Power and supervision

Readers, locks, panels, I/O, batteries, and PoE/DC supplies have different load and outage behavior. Monitor AC/DC/battery, bus faults, open/short/tamper where supported, enclosure, temperature, and clock. Do not infer electrical supervision from application heartbeats.

All live wiring/termination/contact values and emergency interfaces require exact manuals, approved drawings, qualified personnel, and local code review.

Return to [Access-control systems](README.md).
