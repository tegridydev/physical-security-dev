---
title: Time synchronisation
summary: NTP, Network Time Security, PTP, clock quality, event ordering, monotonic timers, and safe time operations.
page_type: reference
domains: [networking, cross-domain]
tags: [ntp, nts, ptp, ieee-1588, clock, timestamp]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [RFC 5905, RFC 8915, IEEE 1588-2019]
coverage_limit: Architecture and software semantics only; no site accuracy budget, grandmaster profile, holdover, or hardware timestamping validation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Time synchronisation

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / Time synchronisation

Time affects alarm ordering, video correlation, credential validity, certificate validation, audit, retry, and forensic evidence. Define an accuracy and availability budget per use case; “NTP configured” is not an evidence-quality claim.

NTPv4 is specified by RFC 5905. Network Time Security (NTS), RFC 8915, adds cryptographic protection to NTP using a key-establishment exchange plus authenticated time packets.[^ntp][^nts] Precision Time Protocol is standardized by IEEE 1588-2019 and uses selectable profiles, roles, and often hardware timestamping for tighter synchronization.[^ptp]

## Four time concepts

- **Wall clock:** UTC-referenced time displayed and persisted for audit.
- **Monotonic clock:** never stepped backwards; use for timeouts, retry and duration.
- **Source timestamp:** when the originating device says the event occurred.
- **Receive/persist timestamps:** when each trusted processing boundary observed or stored it.

Persist timezone/offset only as presentation context; normalize evidence to an unambiguous instant while retaining the original timestamp and clock-quality metadata. Define leap-second, daylight-saving, epoch, precision, wraparound, and invalid/zero timestamp handling for each protocol.

## Source and failure policy

Inventory server/grandmaster identity, authenticated mechanism, stratum/profile/domain, path, polling, maximum acceptable offset/jitter, holdover, boot behaviour, and monitoring. Configure several approved independent sources where the protocol/profile allows, but prevent unauthenticated or lower-quality sources from silently becoming authoritative.

Choose step versus slew policy by consequence. Large clock steps can reorder events, invalidate certificates/tokens, trigger schedules, or distort recordings. Never force-set time on a live controller or camera as a diagnostic shortcut. Quarantine or label data whose source clock is outside policy rather than silently rewriting its event time.

Monitor offset, frequency/drift, source change, reachability, stratum/class, leap indicators, PTP grandmaster identity, NTS authentication, holdover age, reboot, manual time change, and divergence between subsystems. A synchronized server does not prove an endpoint is synchronized.

## Security

Unauthenticated NTP and PTP can be manipulated where an attacker reaches the timing path. Prefer NTS for supported NTP clients/servers, an approved authenticated PTP profile where available, constrained network paths, source allowlists, protected management, and monitoring. Security and accuracy are separate: a correctly authenticated bad clock remains bad, and an accurate unauthenticated sample is not trustworthy evidence.

Validate source selection, holdover, monotonic application behaviour, step/slew policy, authentication failure, and recovery against the target clock stack.

## Primary sources

[^ntp]: [RFC Editor — RFC 5905, NTPv4](https://www.rfc-editor.org/info/rfc5905/)
[^nts]: [RFC Editor — RFC 8915, Network Time Security for NTP](https://www.rfc-editor.org/info/rfc8915/)
[^ptp]: [IEEE Standards Association — IEEE 1588-2019](https://standards.ieee.org/ieee/1588/6825/)
