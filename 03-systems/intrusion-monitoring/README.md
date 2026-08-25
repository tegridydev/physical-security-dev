---
title: Intrusion and Monitoring Systems
summary: Architecture and navigation for panels, zones, sensors, communication paths, receivers, supervision, verification, panic, duress, and fire boundaries.
page_type: index
domains: [alarms]
tags: [intrusion, alarms, monitoring, receivers]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [IEC 62642 series, ANSI/SIA DC-09-2026, ANSI/SIA CP-01-2019]
coverage_limit: System/integration model only; response policy, installation grades, emergency services, fire, and local alarm obligations are jurisdiction/site specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Intrusion and monitoring systems

An alarm system detects and reports conditions; a monitoring operation interprets, verifies, escalates, and records response. Protocol acknowledgement is not operator response or resolution.

## Pages

- [Panels, zones, and sensors](panels-zones-and-sensors.md)
- [Communicators, receivers, and monitoring](communicators-receivers-and-monitoring.md)
- [Path supervision and alarm verification](path-supervision-and-alarm-verification.md)
- [Duress, panic, and fire boundaries](duress-panic-and-fire-boundaries.md)

## Event lifecycle

```text
sensor condition -> panel zone state -> alarm/restore/trouble event
 -> communication path -> receiver acknowledgement -> automation case
 -> operator verification/dispatch -> closure and retained audit
```

Keep alarm, restore, cancel, acknowledgement, test, bypass, communication fault, operator action, and case closure distinct.

## Source baseline

[IEC 62642-1:2010](https://webstore.iec.ch/en/publication/7298) gives system-level scope for wired/wireless intrusion and hold-up alarms; its stability date is 2027, so edition status needs scheduled review. SIA's public [DC-09-2026](https://www.securityindustry.org/industry-standards/dc-09-2026/) scope covers IP event reporting from premises equipment to central stations. [ANSI/SIA CP-01-2019](https://www.securityindustry.org/industry-standards/cp-01-2019/) is current SIA-listed panel/receiver guidance aimed at false-alarm reduction. Normative texts are paid.

Return to [Systems](../README.md).
