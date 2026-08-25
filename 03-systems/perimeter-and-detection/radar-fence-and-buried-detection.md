---
title: Radar, Fence, and Buried Perimeter Detection
summary: Detection-zone, track, environmental, supervision, fusion, and lifecycle models for non-video perimeter sensors.
page_type: system
domains: [alarms, networking, infrastructure]
tags: [radar, fence-detection, buried-sensors, perimeter-sensors]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: ["IEC 62642-1:2010", "IEC 62676-6:2026"]
coverage_limit: Architecture and assurance only; no frequencies, detection thresholds, blind-zone mapping, civil installation, radio licensing, tuning, or defeat detail.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Radar, fence, and buried perimeter detection

Radar, fence-mounted, buried, beam, and related perimeter sensors observe different physical effects. Their events are uncertain measurements shaped by geometry, installation, environment, calibration, and processing. Preserve those conditions rather than flattening every result into `intrusion`.

## Technology roles

| Family | Typical observation | Important uncertainty |
|---|---|---|
| radar | range/angle/velocity tracks or zone occupancy | terrain, clutter, multipath, occlusion, target cross-section, RF conditions |
| fence-mounted | vibration/strain/disturbance along a section | wind, vegetation, loose fabric, corrosion, maintenance, nearby activity |
| buried/field sensor | ground disturbance or field change | soil/water, trench/install consistency, surface traffic, seasonal change |
| active beam | interrupted transmission path | alignment, fog/rain/snow, vegetation, wildlife, contamination |

This table is a design prompt, not performance guidance. Exact technologies and products require vendor evidence and representative site validation.

## Entity and state model

Use stable IDs for device, processor, cable/channel, physical segment, logical zone, track, alarm, camera preset/view, power source, network path, and maintenance exclusion. Store configuration/calibration version and geospatial reference.

Separate raw observation, track/zone state, classification, alarm rule, correlated incident, and operator decision. Preserve confidence/quality and contradictions. Track `normal`, `pre-alarm`, `alarm`, `tamper`, `masking`, `fault`, `degraded`, `maintenance`, `bypass`, `restore`, and `unknown` independently where the product supports them.

For tracks, retain source track ID, creation/update/end time, position and uncertainty, speed/direction, class candidates, merge/split/handoff, and loss reason. A track ID is temporary and must not become a person identity.

## Environmental baseline and change

Commission against an approved operating envelope covering terrain, vegetation, fences/structures, weather, water/soil, wildlife, vehicles, radio environment, and legitimate activity. Record baseline and seasonal/physical changes. Civil works, fence repairs, landscaping, drainage, new structures, lighting, and software changes can invalidate earlier performance evidence.

Avoid fixed universal thresholds copied between sites. Configuration is security-sensitive; changes need named authorization, before/after evidence, versioning, and rollback.

## Fusion and assessment

Associate detections with cameras or other sensors using explicit geometry, time tolerance, and rule versions. A camera cue should show whether it is live, at the expected preset/view, recording, time-aligned, and unobstructed. Loss of video assessment must remain visible even if the detector is healthy.

Fusion may use concurrence, sequence, direction, dwell, or track continuity, but must preserve source events and missed/contradictory evidence. Do not let a second unavailable sensor count as negative confirmation.

## Supervision and resilience

Monitor power, enclosure/tamper, cable/channel continuity where available, alignment, signal/noise/background trends, calibration age, event flow, processor resources, network, clock, configuration, storage, and destination receipt. A reachable processor does not prove its field sensor or detection performance.

Map shared poles, trenches, cable routes, power supplies, switches, radio links, processors, analytics services, and operations clients. Protect maintenance and test modes with expiry and alerting. Radio-emitting equipment requires applicable spectrum authorization and competent design.

## Acceptance evidence

- traceable zone objectives and authorized test scenarios;
- representative object, route, direction, speed, environment, and legitimate-activity coverage;
- localization and camera-association accuracy with time uncertainty;
- nuisance/missed event review and preserved raw evidence;
- tamper, masking, cut/link/power/processor failure and recovery;
- seasonal/change-management plan and bounded maintenance exclusions.

## Source baseline

[IEC 62642-1:2010](https://webstore.iec.ch/en/publication/7298) provides a system context for wired, wire-free, and hybrid intrusion/hold-up alarms. [IEC 62676-6:2026](https://webstore.iec.ch/en/publication/59704) covers repeatable testing and grading for real-time intelligent video analytics; use its stress-aware testing principle only for video analytics, not as a claim of radar or fence conformity.

Return to [Perimeter and detection systems](README.md).
