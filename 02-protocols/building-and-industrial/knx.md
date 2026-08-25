---
title: KNX
summary: KNX topology, group communication, datapoint types, commissioning artefacts, transport choices, and safe integration guidance.
page_type: protocol
domains: [bms, cross-domain]
tags: [knx, group-address, datapoint-type, ets, building-control]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [KNX Standard V3 public set, KNX Standard V3.0.4 certification baseline, ISO/IEC 14543-3, EN 50090]
coverage_limit: Public KNX material was reviewed; complete quarterly specifications, ETS project data, device profiles, and certified product records are needed for implementation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# KNX

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / KNX

KNX is a distributed building-control system standardized through KNX specifications and international/regional standards. Two publication views must be kept distinct: the association's public V3 specification set was published in February 2025, while KNX Standard **3.0.4** was released on 22 August 2025 for member access and became the certification reference at the end of that month.[^specs][^v304] Implementation and certification work must use the exact member document, amendment, certification date, and product record rather than treating the public V3 download as a complete quarterly baseline. Media include twisted pair, power line, RF, KNXnet/IP, and the KNX IoT family; supported media and profiles are product-specific.

## Addressing and meaning

An individual address locates a device in the KNX topology. A group address identifies a shared communication function to which multiple communication objects may be linked. Neither address alone defines value encoding. The datapoint type (DPT) defines encoding and semantics such as boolean switching, percentage, temperature, scene, or time.

For each integration point preserve:

- individual and group addresses exactly as exported from the approved ETS project;
- main/sub DPT and any product-specific interpretation;
- direction, transmit/read/write/update flags, feedback group, and response behaviour;
- unit, valid range, default/unknown rules, and expected update interval;
- whether it is protected by [KNX Secure](knx-secure.md), including the keyring version;
- ownership and authorization for commands.

Do not infer a DPT from payload length. Several meanings share the same encoded width, and wrong scaling can create plausible but unsafe values. A write telegram being accepted does not prove actuator motion or final state; use an authoritative feedback object and explicit timeout.

## KNXnet/IP boundaries

KNXnet/IP supports routing and tunnelling roles. Confirm device discovery, tunnelling-slot capacity, individual-address allocation, multicast/routing configuration, filter tables, line/backbone coupling, NAT limitations, and reconnect behaviour. Avoid fleet-wide auto-discovery or unconstrained group monitoring on production networks.

Classic KNXnet/IP must not be treated as secure merely because it is on an IP VLAN or inside a generic tunnel. Use the applicable KNX Secure profile end to end where supported, and protect legacy TP/RF/PL segments and IP routers as trust boundaries.

## Commissioning and change control

ETS project exports, keyrings, device certificates/FDSKs, and product databases are sensitive configuration artefacts. Version, encrypt, access-control, and back up them according to site policy. Reconcile running devices with the approved project before changing addresses or application programs. Never learn group meanings by exploratory writes.

KNX can control doors, blinds, lifts, lighting, HVAC, and occupancy-dependent workflows. Use a bench or owner-approved commissioning window, retain manual recovery, and keep certified fire/life-safety functions outside an ordinary KNX integration unless the complete approved system design explicitly includes them.

## Primary sources

[^specs]: [KNX Association — KNX specifications](https://support.knx.org/hc/en-us/articles/360000040999-KNX-Specifications)
[^v304]: [KNX Association — KNX Standard Version 3.0.4](https://www.knx.org/news/knx-launches-knx-standard-version-304)
- [KNX Association — KNX Standard v3.0 introduction](https://www.knx.org/news/knx-standard-v30-bringing-internet-things-knx-specifications)
- [KNX Association — KNX IoT downloads](https://support.knx.org/hc/en-us/articles/10386532582930-Downloads)
