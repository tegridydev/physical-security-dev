---
title: Video Analytics and Metadata Systems
summary: Model lifecycle, detection semantics, confidence, drift, privacy, event automation, and standardized metadata integration.
page_type: system
domains: [video]
tags: [analytics, metadata, ai, detection, onvif-profile-m]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: ["IEC 62676-6:2026", ONVIF Profile M]
coverage_limit: Architecture and assurance principles; no accuracy claim for any model, demographic, scene, product, or deployment.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Video analytics and metadata systems

Analytics output is an observation produced by a model under particular scene and configuration conditions—not ground truth. Preserve input/model/context and uncertainty so a downstream rule cannot turn a probabilistic label into an unqualified fact.

## Pipeline

```text
video/sensor input -> preprocessing/ROI -> model/inference -> tracking
 -> rule/threshold -> metadata/event -> review/workflow/automation
```

Canonical records should identify camera/source and media time, object/track/event IDs, class/attributes, confidence/quality where defined, region/rule, model/product/version, configuration/calibration, source frame/clip reference, processing time/location, and transformation/mapping version.

## Standards and interoperability

ONVIF [Profile M](https://www.onvif.org/profiles/profile-m/) standardizes analytics metadata/event interfaces including generic objects and conditional vehicle, plate, face/body, geolocation, rules, and MQTT event handling. Conditional support must be checked per conformant product; Profile M is not a promise of a specific model's accuracy.

[IEC 62676-6:2026](https://webstore.iec.ch/en/publication/59704) establishes performance-testing and grading scope for real-time intelligent video analytics, including core/complex capabilities and operating stress. The normative test methods are paid; public catalogue scope does not validate a site.

## Evaluation

Define target population, scene, weather/illumination, camera/view, object sizes/speeds/occlusion, threshold, dwell/rule, and consequence. Measure at the operational decision level:

- true/false positive and negative outcomes;
- precision/recall or detection probability and nuisance-alarm rate;
- latency, duplicate/split/merged tracks, missed transitions;
- performance by relevant environmental and demographic groups;
- operator workload and escalation outcome;
- unavailable/uncertain periods, not only scored frames.

Aggregate accuracy can conceal a harmful subgroup or rare-condition failure. NIST's [Face Recognition Vendor Test demographic report](https://www.nist.gov/publications/face-recognition-vendor-test-part-3-demographic-effects) demonstrates why demographic effects must be evaluated for facial recognition; it does not evaluate a local deployment automatically.

## Model/configuration lifecycle

Inventory model and runtime versions, training/provenance information available from supplier, camera/input contract, thresholds/regions, license, firmware/hardware acceleration, and rollback. Rebaseline after camera move, lens/illumination change, scene change, model/update, codec/profile change, or seasonal conditions.

Monitor input quality, inference availability, event rate distribution, confidence drift, operator disposition, ground-truth sample process, and configuration changes. Avoid self-reinforcing labels in which prior model output becomes unreviewed training truth.

## Security, privacy, and automation

- Minimize faces, plates, biometric embeddings, trajectories, demographics, occupancy, and cross-camera tracking; define purpose, access, retention, and subject processes.
- Authenticate metadata source and preserve media linkage; reject stale/replayed events and tenant/site confusion.
- Bound images/metadata and untrusted model/plugin inputs.
- Separate analytics administration from video viewing and actuation.
- Require human or separately assured policy for high-consequence action. Never unlock, dispatch, deny service, or declare identity solely from an unvalidated generic detection.

## Failure semantics

Represent `not-detected`, `no-object`, `analytics-unavailable`, `input-unusable`, `rule-disabled`, and `unknown` separately. Silence from an analytics service is not a normal scene.

Return to [Video-surveillance systems](README.md).
