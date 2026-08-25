---
title: "Logging, time, and evidence integrity"
summary: "Design trustworthy event, audit, media, and time records across distributed physical-security systems."
page_type: security
domains:
  - cross-domain
tags:
  - logging
  - time
  - evidence
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards:
  - "RFC 5424"
  - "RFC 8915"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Logging, time, and evidence integrity

[Home](../README.md) / [Security and assurance](README.md) / Logging, time, and evidence integrity

An incident timeline may join door events, video, alarms, operator actions, API requests, broker delivery, controller logs, identity-provider decisions and network telemetry. Their timestamps and identifiers are not automatically comparable or trustworthy.

## Event record minimum

- stable event type and schema version;
- event/source identity and site/tenant scope;
- occurrence, device, ingestion and processing times kept distinct;
- clock quality, uncertainty or synchronization state where available;
- actor/workload identity and authentication context;
- requested action, target, authorization decision and outcome;
- correlation and causation identifiers;
- sequence/counter and duplicate/replay disposition where meaningful;
- configuration/firmware/policy version needed to interpret the event;
- redaction/data-classification marker.

## Time model

Use UTC for interchange and store the original offset when operational context needs it. Do not infer event order solely from wall-clock timestamps. Prefer protocol sequence, monotonic duration and ingestion evidence for causal analysis. Handle leap seconds, clock steps, daylight-saving display, device reboot, oscillator drift, NTP source change and loss of synchronization explicitly.

NTPv4 is defined by RFC 5905, while Network Time Security adds cryptographic protection for NTP client/server time synchronization in RFC 8915 [RFC-5905] [RFC-8915]. Product support and deployment configuration must be checked per model; authenticated time does not guarantee the upstream time source itself is correct.

## Integrity and custody

- Send security-relevant records off-device promptly to a separately administered store.
- Restrict append, modification, deletion and export; log those operations too.
- Preserve original exports and hashes alongside derived/transcoded working copies.
- Record exporter, source system, exact time range, timezone, device/stream identifiers, software version and transformation steps.
- Use product-supported signing/verification when available, but document what it covers and how trust is established.
- Protect encryption/signing keys independently from stored evidence.
- Validate in a representative environment that retention, rollover, storage pressure, and failover do not silently discard critical logs.

## Privacy and utility

Logging everything can create a second surveillance database. Do not log raw credentials, authentication tokens, biometric templates, passwords, full private URLs, unnecessary faces/audio, or unrestricted operator screen content. Preserve enough identifiers for investigation through controlled lookup and access.

## Sources

- **RFC-5424** — [RFC 5424: The Syslog Protocol][RFC-5424], accessed 2026-08-25.
- **RFC-5905** — [RFC 5905: Network Time Protocol Version 4][RFC-5905], accessed 2026-08-25.
- **RFC-8915** — [RFC 8915: Network Time Security for NTP][RFC-8915], accessed 2026-08-25.
- **NIST-800-92** — [NIST SP 800-92: Guide to Computer Security Log Management][NIST-800-92], accessed 2026-08-25.

[RFC-5424]: https://www.rfc-editor.org/rfc/rfc5424
[RFC-5905]: https://www.rfc-editor.org/rfc/rfc5905
[RFC-8915]: https://www.rfc-editor.org/rfc/rfc8915
[NIST-800-92]: https://csrc.nist.gov/pubs/sp/800/92/final

## Related pages

- [Privacy and sensitive data](privacy-and-sensitive-data.md)
- [Resilience, backup, and recovery](resilience-backup-and-recovery.md)
- [Time protocols](../02-protocols/infrastructure/time-synchronisation.md)
