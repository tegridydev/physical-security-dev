---
title: Perimeter-Security Architecture
summary: Layered deterrence, delay, detection, assessment, response, and recovery architecture for site boundaries and approaches.
page_type: system
domains: [alarms, video, access-control, operations]
tags: [perimeter-security, detection, assessment, sensor-fusion]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 62676-4:2025", "IEC 62676-6:2026"]
coverage_limit: Architecture and assurance model only; no site layout, covert capability, civil design, detection settings, response tactics, or jurisdiction-specific requirement.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Perimeter-security architecture

A perimeter is a system of zones and response opportunities, not a fence line or a single sensor. Design each layer around a defined threat, operating context, detection objective, assessment path, response owner, and tolerated failure.

## Layered model

```text
approach awareness -> boundary definition/deterrence -> detection
 -> localization/tracking -> independent assessment -> response decision
 -> delay/access control -> intervention -> recovery and learning
```

Record the boundary of responsibility: public space, controlled approach, outer perimeter, sterile zone, vehicle/pedestrian portals, building line, and protected asset. A sensor alarm near a mapped line does not prove crossing, intent, identity, or compromise.

## Canonical zone and event model

Use stable identities for site, perimeter segment, detection zone, sensor, camera view, illumination, portal, response sector, and maintenance exclusion. Geospatial coordinates and drawings need version and datum/reference where applicable.

Preserve source observations before correlation:

- source-native event, object/track ID, location/zone, direction, time, confidence/quality, and classification;
- alarm, pre-alarm, tamper, masking, fault, degraded, maintenance, bypass, restore, and unknown states;
- correlated incident ID, association rule/version, contributing and contradictory sources;
- operator assessment, response action, outcome, and closure reason.

Correlation reduces workload but can amplify common errors. Do not overwrite an original radar, fence, analytic, access, or camera event with one fused verdict.

## Design dimensions

| Dimension | Questions |
|---|---|
| threat and objective | What action, object, path, speed, direction, and warning time matter? |
| environment | Terrain, vegetation, wildlife, weather, water, vibration, lighting, traffic, and RF conditions? |
| geometry | Coverage, gaps, occlusion, overlapping zones, dead ground, portal transitions? |
| assessment | Which camera/other source can actually view the alarm location within the required time? |
| response | Who receives it, with what context, and what safe action is possible? |
| resilience | Shared power/network/mounting, cut paths, flooding, fire, vandalism, maintenance? |
| privacy | Public/neighboring capture, plate/person tracking, audio, retention, disclosure? |

## Availability and health

Health must cover sensing performance as far as observable, not merely network reachability. Track enclosure/tamper, alignment, calibration age, obstruction/vegetation, signal/background/noise trends, power, battery, link/path, time, configuration drift, event flow, camera usability, recording, and operator destination.

Map common-mode dependencies. Two detectors on one pole, power supply, switch, fibre route, wireless backhaul, analytics server, clock, or operations client do not provide independent assurance.

Maintenance needs controlled zones, approved test targets/stimuli, environmental coverage, alarm-to-assessment correlation, and proof that bypasses expire. Do not publish sensitive detection thresholds, blind spots, response times, or defeat details in general documentation.

## Assessment and automation

An associated video pane must show its camera identity, live/recorded status, image timestamp, clock uncertainty, recording gaps, view/occlusion limits, and analytic status. A cached or stale image must never appear as live.

Automatic camera cueing or track handoff may improve assessment but should bound movement, respect privacy masks/priority, surface loss of track, and not displace evidential recording. Automatic barrier or gate actuation from uncertain sensor/analytic output needs a separately approved safety and authorization design.

## Acceptance evidence

- traceability from threat and zone objective to each sensor and assessment source;
- coverage/gap evidence across representative environmental and operating conditions;
- event location, timestamp, camera association, and response workflow;
- nuisance and missed-detection review without unsupported universal performance claims;
- power/network/time/server/camera/sensor failure and recovery behavior;
- bypass/maintenance controls and configuration/change audit;
- privacy boundaries, retention, export, and authorized disclosure.

## Source baseline

[IEC 62676-4:2025](https://webstore.iec.ch/en/publication/110108) gives current application guidance for video-surveillance systems. [IEC 62676-6:2026](https://webstore.iec.ch/en/publication/59704) defines methods to evaluate and grade real-time intelligent video analysis, including intrusion and complex scenarios under operational stress. Neither source establishes performance for an untested site or product.

See [Perimeter and detection systems](README.md) and [Radar, fence, and buried detection](radar-fence-and-buried-detection.md).
