---
title: "Monitoring and health"
summary: "Observe whether physical-security functions, protocol trust, time, storage, and integrations remain effective."
page_type: operations
domains:
  - operations
tags:
  - monitoring
  - health
  - observability
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards:
  - "NIST SP 800-137"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Monitoring and health

[Home](../README.md) / [Operations and lifecycle](README.md) / Monitoring and health

Service reachability is not the same as security function. A camera may answer ping while video is frozen; a controller may be online while its reader bus is degraded; a broker may be healthy while authorization rejects every publisher.

## Health layers

| Layer | Signals |
|---|---|
| Physical/power | Power source, PoE/battery/UPS state, enclosure/tamper, temperature, link, serial errors |
| Device | Boot/reboot, firmware, CPU/memory, clock, storage, sensor/reader/stream state |
| Protocol | Authentication, certificate, sequence/CRC, timeout, retry, reconnect, queue, subscription, multicast |
| Application | Recording continuity, door decisions, alarm delivery, intercom call, analytics/event pipeline |
| Security | Account/role/config change, failed login, legacy mode, trust-anchor change, update failure |
| Data/evidence | Gaps, drift, corruption, retention, export verification, duplicate or out-of-order events |
| Dependency | DNS, DHCP, time, IdP, CA, broker, database, vendor cloud, cellular, storage and backup |

## Monitor expected absence

Some failures appear as silence. Define expected heartbeats, stream samples, event rates, sequence continuity, polling interval, certificate renewal, backup completion and configuration checkpoints. Alert on missing expected evidence, not only explicit errors.

## Alert design

- State the affected function and scope, not merely the component name.
- Preserve first occurrence, duration, flapping and recovery.
- Correlate downstream symptoms to upstream dependency failure.
- Suppress duplicate noise without hiding persistent security degradation.
- Route high-impact safety/availability conditions through the approved operational process.
- Avoid sensitive faces, credentials, tokens and facility details in broad alert channels.

## Environment validation cases

Verify expected alerts for controlled loss and restoration scenarios involving a non-production stream, reader/controller link, time source, certificate trust, storage capacity, broker subscription, authentication path, and vendor dependency. Record alert latency, recovery indication, missing evidence, false positives, and unexpected side effects in the environment-validation record.

## Sources

- **NIST-800-137** — [NIST SP 800-137: Information Security Continuous Monitoring][NIST-800-137], accessed 2026-08-25.
- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], OT monitoring guidance, accessed 2026-08-25.

[NIST-800-137]: https://csrc.nist.gov/pubs/sp/800/137/final
[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## Related pages

- [Logging, time, and evidence integrity](../06-security-and-assurance/logging-time-and-evidence-integrity.md)
- [Operational runbooks](runbooks.md)
- [Infrastructure protocols](../02-protocols/infrastructure/README.md)
