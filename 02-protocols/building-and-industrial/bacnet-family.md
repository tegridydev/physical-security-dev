---
title: BACnet family
summary: BACnet objects, services, discovery, routing, conformance, and safe physical-security integration patterns.
page_type: protocol
domains: [bms, cross-domain]
tags: [bacnet, bms, objects, services, discovery]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [ANSI/ASHRAE 135-2024, ANSI/ASHRAE 135.1-2023, ISO 16484-5]
coverage_limit: Architectural guidance only; normative encoding, service, profile, and conformance requirements are in the licensed standards.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# BACnet family

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / BACnet

BACnet is a building-automation protocol with a standard object model and application services. It can represent devices, analogue and binary values, schedules, trends, alarms/events, access-control objects, and other building functions. The current consolidated edition is ANSI/ASHRAE 135-2024; the BACnet Committee reports it as protocol revision 31.[^updates]

## Transport choices

| Data link | Typical role | Read next |
|---|---|---|
| BACnet/IP | UDP/IP with BACnet Virtual Link Layer (BVLL), broadcasts and routed subnets | [BACnet/IP](bacnet-ip.md) |
| BACnet MS/TP | Token-passing BACnet over an EIA-485 multidrop bus | [BACnet MS/TP](bacnet-ms-tp.md) |
| BACnet Secure Connect | WebSocket/TLS secure data link with hubs and nodes | [BACnet/SC](bacnet-secure-connect.md) |

BACnet routers join data-link networks while preserving BACnet network-layer addressing. A protocol gateway that maps BACnet to another model has a larger semantic responsibility than a BACnet router.

## Object and service contract

A durable integration identifies an object by device instance, object type and instance—not display name alone. Record property, array index if applicable, units, resolution, writable priority, update mechanism, expected status flags, and ownership.

BACnet commandable properties use a priority array. Writing a present value without an agreed priority and relinquish procedure can mask another controller indefinitely. Store the chosen priority, use `NULL`/relinquish only as specified by the product and project, and verify the resulting value and status. Never reserve emergency/life-safety priorities for ordinary physical-security automation.

Change of Value (COV) subscriptions reduce polling but introduce subscription lifetime, renewal, reboot, duplicate notification, and fallback behaviour. Persist neither a subscription nor a cached value as proof of current device state after loss of communication. ReadProperty/ReadPropertyMultiple limits vary by product; bound batches and degrade gracefully.

## Discovery and identity

Who-Is/I-Am and object discovery reveal protocol addresses and capabilities; they do not authenticate a device. Device instance uniqueness must be engineered across the routed BACnet internetwork. Maintain an approved inventory binding instance, certificate identity where applicable, network/address, vendor/product, firmware, and expected services.

## Conformance language

A Protocol Implementation Conformance Statement (PICS) declares supported BACnet Interoperability Building Blocks, object types, data links, character sets, and options. It is a selection and test input, not proof that two products implement the same project semantics. ANSI/ASHRAE 135.1 defines conformance tests; certification claims should link to the exact listing and version.[^about]

## Safety boundary

BACnet can command HVAC, lifts, door interfaces, and other consequential equipment. Make write paths opt-in, authorize by object/property/priority, enforce quality and stale-state rules, and keep certified fire/life-safety interfaces within their approved design. Discovery and broad ReadPropertyMultiple sweeps can overload small devices; use an isolated lab or an owner-approved query budget.

## Primary sources

[^updates]: [ASHRAE BACnet Committee — standard and addenda status](https://bacnet.org/updates/)
[^about]: [ASHRAE BACnet Committee — about the BACnet standard](https://bacnet.org/about-bacnet-standard/)
- [ASHRAE BACnet Committee — developer aids](https://bacnet.org/developer-aids/)
- [ASHRAE BACnet Committee — obtaining Standards 135 and 135.1](https://bacnet.org/buy/)
