---
title: "Privacy and sensitive data"
summary: "Engineering controls for video, audio, biometrics, credentials, location, occupancy, and identity data."
page_type: security
domains:
  - cross-domain
tags:
  - privacy
  - biometrics
  - data-minimization
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST Privacy Framework 1.0"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Privacy and sensitive data

[Home](../README.md) / [Security and assurance](README.md) / Privacy and sensitive data

Physical-security data can reveal identity, movement, associations, schedules, facility layout, access rights, behavior, health-related inferences, and response capability. Global technical guidance cannot determine whether collection or use is lawful in a particular jurisdiction; obtain local legal and governance review.

## Data classes

| Class | Examples | Special risk |
|---|---|---|
| Media | Live/recorded video, audio, intercom calls | Captures bystanders and sensitive spaces; secondary use is easy |
| Biometric | Face, fingerprint, iris, voice template and quality data | Difficult to replace; matching and demographic performance concerns |
| Credential | Card/mobile identifiers, keys, access rights, revocation state | Enables tracking, impersonation or access-policy inference |
| Location and behavior | ANPR/LPR, UWB/BLE position, occupancy, access history | Creates detailed movement and association records |
| Identity | Names, photos, directory identifiers, visitor records | Links system events to people and organizations |
| Security telemetry | Alarms, camera health, blind spots, topology, response | Can expose facility weaknesses and operational patterns |

## Data-flow questions

For every field ask: why is it needed, who is the subject, where is it collected, which systems receive it, which identifiers join it, how long is it retained, who can query/export it, which vendors/subprocessors handle it, what leaves the site/region, how is deletion propagated, and what happens if the purpose ends.

## Engineering controls

- Collect the least resolution, duration, area, audio, biometric feature set, and metadata required for the declared purpose.
- Apply privacy masks and exclusion zones at the earliest reliable stage, while documenting whether raw data exists upstream.
- Separate operational viewing, investigation, export, analytics training, administration and bulk search permissions.
- Default APIs to narrow time/site/object ranges; rate-limit bulk enumeration and export.
- Encrypt data in transit and at rest with separately managed keys and auditable access.
- Redact logs and support bundles; use synthetic data in documentation and development.
- Make retention and deletion explicit across edge storage, VMS, cloud replicas, caches, analytics stores, backups and exports.
- Record model/version and evaluation limits for biometric or analytic decisions; keep human review where consequences warrant it.
- Design for subject correction, revocation, deletion and account closure without corrupting audit integrity.

## Developer anti-patterns

- using a stable card number as a cross-system analytics identifier without necessity;
- placing faces, plate numbers or raw credential values in broker topic names or URLs;
- returning unrestricted historical search results to a broad operator role;
- retaining debug media or full API bodies indefinitely;
- silently repurposing security footage to train analytics;
- claiming anonymization while stable device, location and time fields permit re-identification.

## Sources

- **NIST-PRIVACY** — [NIST Privacy Framework 1.0][NIST-PRIVACY], risk-management framework, accessed 2026-08-25.
- **NIST-FACE** — [NIST Face Technology Evaluation][NIST-FACE], official evaluation programme and reports, accessed 2026-08-25.
- **OECD-PRIVACY** — [OECD Privacy Guidelines][OECD-PRIVACY], globally recognized principles, accessed 2026-08-25.

[NIST-PRIVACY]: https://www.nist.gov/privacy-framework/privacy-framework
[NIST-FACE]: https://www.nist.gov/programs-projects/face-technology-evaluations-ftef
[OECD-PRIVACY]: https://www.oecd.org/en/topics/sub-issues/privacy-principles.html

## Related pages

- [Logging, time, and evidence integrity](logging-time-and-evidence-integrity.md)
- [Biometric systems](../03-systems/access-control/biometrics.md)
- [ANPR/LPR systems](../03-systems/perimeter-and-detection/anpr-lpr-systems.md)
