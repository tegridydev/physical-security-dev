---
title: Intrusion Panels, Zones, and Sensors
summary: State, authority, supervision, enrollment, and failure models for intrusion and hold-up alarm field systems.
page_type: system
domains: [alarms]
tags: [alarm-panels, zones, sensors, tamper, partitions]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 62642-1:2010", "IEC TS 62642-7:2011"]
coverage_limit: Architecture and state semantics only; no live wiring, detector placement, grade selection, commissioning values, or jurisdiction-specific response procedure.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Intrusion panels, zones, and sensors

The control and indicating equipment is the field authority for enrolled points, set/unset state, local timing, tamper and fault state, and the event sequence it actually observed. A head-end can present or enrich that state, but must not silently reinterpret it.

## Logical model

```text
site/account
 -> panel/control equipment
    -> area/partition
       -> zone/input/point
          -> detector/contact/hold-up device
    -> output/sounder/indicator
    -> communicator/path
```

Vendor terms vary. Preserve both the native identifier and a normalized class. Do not collapse an area into a building, or a zone into a single sensor: one zone may aggregate devices and one physical space may span multiple areas.

Minimum inventory attributes include panel and module identity, firmware, area, zone, sensor class, location, supervision method, normal-state semantics, tamper path, power source, dependencies, communication paths, and current lifecycle state. Names such as `Zone 17` are not durable asset identity.

## State is multi-dimensional

Model at least these dimensions separately:

- set/unset, entry/exit transition, and inhibited setting;
- normal, active, alarm, restore, and latched alarm;
- tamper, enclosure open, masking, and substitution where supported;
- fault/trouble, low battery, mains loss, device missing, and communication loss;
- bypass/inhibit/isolate/test state, including actor, reason, start, and expiry;
- acknowledged, reset, cancelled, and operator-closed workflow states.

A restore means the initiating condition returned to its defined normal state. It does not prove the incident ended, the premises are safe, or an operator reviewed the alarm. Reset clears only the states the product defines as resettable.

## Sensor classes and assumptions

Opening contacts, glass-break, vibration/seismic, passive infrared, microwave, dual-technology, beam, pressure, water/environmental, and hold-up devices fail differently. Record the sensing purpose and expected environment rather than treating every point as a Boolean.

For each sensor class, document:

- detection objective and excluded conditions;
- coverage, obstruction, masking, environmental, and mounting assumptions;
- warm-up, stabilization, pulse/count, or dwell semantics where applicable;
- local indication and tamper behavior;
- wired, bus, or radio dependency and power source;
- maintenance stimulus and evidence expected without exposing defeat instructions.

Wireless reachability, battery, and radio interference are distinct. A recent check-in does not prove sensing performance. Wired continuity does not prove correct placement or detector response.

## Enrollment and change control

Enrollment binds a physical device or circuit to an identity and security function. Capture installer-approved identity evidence; require authorization for replacement, relocation, zone-type change, radio re-enrollment, or tamper-disable changes. Compare panel-native configuration with the maintained design record and retain an attributable change event.

Treat service modes as privileged, time-bounded states. A bypass that persists beyond approved work creates an exposure even if the panel reports healthy.

## Power, expansion, and failure domains

Map control equipment, expanders, buses, radio receivers, power supplies, batteries, sounders, communicators, and upstream network equipment. An expander or shared supply can create a larger correlated loss than one zone. Identify which components retain local decisions or event queues during upstream failure and how they reconcile after recovery.

Avoid derived health that says only `online`. A useful view distinguishes point active, tamper, device missing, panel fault, bus fault, radio fault, power fault, clock fault, configuration mismatch, path failure, and monitoring suspension.

## Verification questions

- Does each point have a stable identity, location, purpose, owner, and expected state?
- Can alarm, tamper, fault, bypass, test, and restore coexist without loss of meaning?
- Are area transitions and entry/exit behavior validated against the approved operating concept?
- Are shared power, bus, receiver, and communicator failure domains visible?
- Is every bypass or test mode attributable, bounded, and reviewed?
- Does loss-and-recovery testing prove event queuing and ordering rather than only reconnection?

## Source baseline

[IEC 62642-1:2010](https://webstore.iec.ch/en/publication/7298) defines system requirements for wired, wire-free, and hybrid intrusion and hold-up alarm systems and is listed with a 2027 stability date. [IEC TS 62642-7:2011](https://webstore.iec.ch/en/publication/7308) supplies application guidance for planning, installation, commissioning, operation, and maintenance. The normative documents are not reproduced here, and grade or site design remains a competent-person decision.

See [Intrusion and monitoring systems](README.md) and [Communicators, receivers, and monitoring](communicators-receivers-and-monitoring.md).
