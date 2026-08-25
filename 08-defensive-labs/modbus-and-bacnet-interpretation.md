---
title: "Modbus and BACnet interpretation"
summary: "Offline, read-only reasoning about register/object semantics, transactions, secure variants, and safety boundaries."
page_type: lab
domains:
  - building-industrial
tags:
  - modbus
  - bacnet
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "MODBUS Application Protocol V1.1b3"
  - "BACnet/SC Addendum 135-2016 bj"
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Modbus and BACnet interpretation

[Home](../README.md) / [Defensive labs](README.md) / Modbus and BACnet

Lab class: **Offline synthetic frame and object-listing fixtures**

## Modbus exercise

Use the [synthetic read response](../05-development-and-integration/examples/modbus-read-response.md) to identify MBAP fields, unit/function, byte count and registers. Then apply a synthetic vendor register map to discuss signedness, scaling, word order, freshness and limits. Do not send reads or writes to a PLC, gate, barrier, power system or controller.

## BACnet exercise

Use a synthetic object inventory to map device/object identifiers, object types, properties, services and represented network path. Separate BACnet/IP, MS/TP and BACnet/SC transports, and identify BBMD/foreign-device or hub/connector trust boundaries where applicable. Represent discovery and property-write behavior conceptually; the fixture contains object metadata only.

## Security comparison

- Classic Modbus/TCP and BACnet/IP do not inherently provide the endpoint identity and protected transport expected from modern secure variants.
- Modbus Security uses TLS and X.509 on assigned port 802 according to Modbus Organization materials.
- BACnet/SC uses TLS-secured WebSockets and certificates; certificate/hub operation remains a deployment responsibility.
- Secure transport does not authorize a physical write or establish safe register/object semantics.

## Evidence checklist

- [ ] Fixture provenance, digest, protocol/version, and synthetic topology recorded
- [ ] Modbus MBAP, unit, function, byte count, register, signedness, scaling, and word-order interpretation documented
- [ ] BACnet device/object identifiers, properties, services, and transport family mapped
- [ ] Unknown register/object semantics and vendor-map dependencies identified rather than guessed
- [ ] Classic and secure transport identity, confidentiality, integrity, and certificate boundaries compared
- [ ] Read, write, acknowledgement, and physical-outcome semantics kept distinct
- [ ] Network discovery, field-bus access, devices, controllers, and physical writes excluded

## Sources

- [Modbus specifications](https://www.modbus.org/modbus-specifications), accessed 2026-08-25.
- [BACnet Secure Connect](https://bacnetinternational.org/bacnetsc/), accessed 2026-08-25.

## Related pages

- [Building and industrial protocols](../02-protocols/building-and-industrial/README.md)
- [BMS and SCADA integration](../03-systems/integration-platforms/bms-and-scada-integration.md)
