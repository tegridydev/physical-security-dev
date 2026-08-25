---
title: Building and industrial protocols
summary: Index to field, building-automation, utility, and industrial Ethernet protocols encountered in physical-security integrations.
page_type: index
domains: [bms, ot, cross-domain]
tags: [ot, fieldbus, building-automation, industrial-ethernet, protocol-index]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [IEC 61158, IEC 61784, IEC 62541, IEC 61850, IEC 60870-5, ISO 16484-5, IEEE 1815, Matter 1.6]
coverage_limit: Architectural and developer integration guidance; licensed standards and device profiles remain authoritative for implementation and conformance.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Building and industrial protocols

[Home](../../README.md) / [Protocols](../README.md) / Building and industrial

Physical-security systems frequently exchange occupancy, door, lift, HVAC, power, fire-interface, and equipment-health state with operational technology. A shared cable or Ethernet network does not imply a shared object model, safety classification, timing contract, or trust boundary.

## References

| Family | Pages | Integration centre of gravity |
|---|---|---|
| Modbus | [Family](modbus-family.md), [RTU](modbus-rtu.md), [TCP](modbus-tcp.md), [Security](modbus-security.md) | Register/coils, simple request-response, serial and TCP gateways |
| BACnet | [Family](bacnet-family.md), [BACnet/IP](bacnet-ip.md), [MS/TP](bacnet-ms-tp.md), [BACnet/SC](bacnet-secure-connect.md) | Building-automation objects, services, discovery, routing |
| KNX | [KNX](knx.md), [KNX Secure](knx-secure.md) | Distributed building controls and group communication |
| OPC UA | [OPC UA](opc-ua.md) | Rich typed information models, client/server and PubSub |
| DNP3 | [DNP3](dnp3.md) | Telecontrol and utility event reporting |
| IEC telecontrol | [IEC 60870-5-101 and -104](iec-60870-5-101-and-104.md) | Telecontrol ASDUs over serial and TCP profiles, with IEC 62351 security context |
| Power utility automation | [IEC 61850](iec-61850.md) | Logical nodes, ACSI, SCL, MMS, GOOSE, Sampled Values, and IEC 62351 boundaries |
| Matter | [Matter](matter.md) | IP-based smart-building/home device fabrics, commissioning, ACLs, attestation, and multi-ecosystem control |
| CAN ecosystems | [CAN, CANopen, and J1939](can-canopen-j1939.md) | Embedded controllers, vehicles, gates, lifts, machinery |
| Industrial Ethernet | [PROFINET](profinet.md), [EtherNet/IP and CIP](ethernet-ip-and-cip.md) | Cyclic I/O, controller/device data, diagnostics, safety profiles |

## Integration rule

Treat every cross-domain point as a contract containing: authoritative source, engineering unit, valid range, update model, stale threshold, quality, command authority, safe fallback, ownership, and audit requirements. A protocol bridge must never silently turn `unknown`, `bad quality`, timeout, or stale state into `false`, `closed`, `secure`, or `normal`.

## Safety boundary

Do not write to live controllers, simulate field devices on an operational network, change routing, clear alarms, or operate connected equipment from examples or discovery tools. Use offline fixtures and simulation for research; hardware acceptance belongs under site change control, manufacturer procedures, independent observation, and the asset owner's recovery plan. Life-safety, process-safety, and machinery-safety functions require their own certified path.

## Primary sources

- [Modbus Organization — specifications](https://www.modbus.org/modbus-specifications)
- [ASHRAE BACnet Committee — standard status](https://bacnet.org/updates/)
- [KNX Association — public specifications](https://support.knx.org/hc/en-us/articles/360000040999-KNX-Specifications)
- [OPC Foundation — online reference](https://reference.opcfoundation.org/)
- [DNP Users Group — protocol overview](https://www.dnp.org/About/Overview-of-DNP3-Protocol)
- [CAN in Automation — technical documents](https://www.can-cia.org/cia-groups/technical-documents)
- [PI — PROFINET specifications](https://www.profibus.com/download/profinet-specification)
- [ODVA — specifications](https://www.odva.org/subscriptions-services/specifications/)
