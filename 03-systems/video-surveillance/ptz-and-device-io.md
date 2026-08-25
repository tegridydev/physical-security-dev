---
title: PTZ and Camera Device I/O
summary: Safe control, arbitration, presets, tours, position uncertainty, privacy, relays, and physical confirmation for camera actuation.
page_type: system
domains: [video]
tags: [ptz, camera-io, relays, presets, actuation]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 62676-2-31:2019", ONVIF Profile T]
coverage_limit: Non-actuating architecture guidance; no live PTZ, relay, alarm, door, gate, or safety-output procedure.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# PTZ and camera device I/O

Pan/tilt/zoom (PTZ), focus, wipers, illuminators, audio, and relay outputs are actuation. They can expose private views, damage mechanisms, distract operators, interrupt analytics, or affect doors/gates/alarms wired to camera I/O.

## Control model

```text
operator/rule -> authorization -> arbitration/lease -> command
 -> device acceptance -> motion/output -> independent state/scene evidence
```

Distinguish absolute/relative/continuous movement, stop, home, preset, tour/patrol, auxiliary command, and configuration. A protocol response usually confirms command handling, not achieved position or physical relay outcome.

## Arbitration

Multiple clients—operator keyboard, VMS, analytics auto-tracking, guard tour, integration, maintenance—can conflict. Define priority, exclusive lease duration, preemption, idle timeout, stop behavior, and visible ownership. Emergency/safety use must not depend on an informal “last command wins” rule.

Audit subject/workload, target camera/site, operation, requested/actual position if reported, preset/tour version, reason/case, time, result, and preemption. Do not expose unrestricted generic auxiliary commands to low-privilege integrations.

## Presets, tours, and privacy

Preset numbers/names are mutable configuration, not universal coordinates. Store logical purpose plus device-specific mapping/version. Revalidate after camera replacement, mount service, firmware, calibration, or privacy-mask change.

Moving a camera can reveal excluded private areas or leave a protected scene unobserved. Define allowable mechanical zones, privacy masks at source, return-home policy, dwell limits, and operator indication. Verify masks across live, recorded, analytics, snapshots, and exports.

## Device I/O

Camera digital inputs may report alarms/tamper; outputs may drive indicators or interface relays. Follow [dry contacts and supervised circuits](../../01-foundations/dry-contacts-and-supervised-circuits.md). Name polarity/meaning and separate electrical output state from sensed physical outcome. Camera relays must not become an unreviewed shortcut around PACS, fire, gate, or lift control logic.

## Protocol scope

[IEC 62676-2-31:2019](https://webstore.iec.ch/en/publication/61227) includes PTZ control in its network-video web-service scope. ONVIF [Profile T](https://www.onvif.org/profiles/profile-t/) includes PTZ-related client/device features and conditional I/O capabilities. Exact movement ranges, coordinate spaces, speeds, focus/auxiliary functions, and conformance need product verification.

Legacy Pelco-D/P and vendor serial/IP dialects may expose fewer identity/security controls. Contain them behind a least-privilege authenticated gateway and serialize commands.

## Safe failure

- Issue explicit stop/cancel and define behavior on lost client/session/network.
- Bound speed, duration, command rate, queue, and tours.
- After timeout, query state/scene before retry; repeated continuous commands can be harmful.
- Detect stalled/moved/obstructed mechanisms without assuming position telemetry is correct.
- Preserve manual/local override and maintenance lockout.
- Keep all examples simulation-only; user site testing requires the high-impact safety gate.

Return to [Video-surveillance systems](README.md).
