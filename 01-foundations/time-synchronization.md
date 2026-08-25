---
title: Time Synchronization
summary: Clock sources, NTP, NTS, PTP, timestamp quality, monotonic time, and forensic correlation.
page_type: foundation
domains: [video, access-control, alarms, intercom, bms, ot]
tags: [time, ntp, nts, ptp, timestamps, forensics]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: [RFC 5905, RFC 8915, IEEE 1588-2019]
coverage_limit: General timing design; accuracy and profile requirements are use-case and product specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Time synchronization

Time is both an operational dependency and evidence. Incorrect clocks can break certificate validation, event ordering, recording search, access schedules, alarm correlation, token validity, and forensic reconstruction.

## Define the requirement

“Use NTP” is not a requirement. Specify:

- maximum offset and uncertainty at each device class;
- recovery time after boot or network outage;
- holdover behaviour and oscillator limits;
- authoritative source and upstream traceability;
- authentication and allowed servers;
- time zone/display policy versus UTC storage;
- leap-second and daylight-saving handling;
- monitoring, alarm threshold, and evidence retention;
- behaviour when time becomes untrusted.

Video frame alignment, intercom audio/video, access-event sequencing, and legal evidence may have different tolerance. Precision without authenticated provenance is not trustworthy time.

## NTP and NTS

NTP version 4 is specified by [RFC 5905](https://www.rfc-editor.org/info/rfc5905), with subsequent updates listed by the RFC Editor. Use multiple approved upstream sources and monitor offset, delay, stratum/source selection, reachability, and clock steps.

NTP is not automatically authenticated. [RFC 8915](https://www.rfc-editor.org/info/rfc8915) defines Network Time Security (NTS) for NTP client-server mode using TLS for key establishment and authenticated NTP extension fields. Product support varies; where unavailable, constrain time paths and protect the time infrastructure while recording the limitation.

## PTP

Precision Time Protocol (PTP) is specified by active [IEEE 1588-2019](https://sagroups.ieee.org/1588/public-documents/) (PTP v2.1) and amendments. It can achieve much tighter synchronization on a properly engineered network, but depends on the selected profile, grandmaster selection, boundary/transparent clock support, path asymmetry, multicast/unicast mode, and security architecture.

Do not mix PTP profiles or assume any switch carrying PTP is timing aware. Protect grandmaster selection and management, monitor identity changes, and document whether the source is traceable to UTC.

## Clock types

- **Wall clock:** calendar time; can step, slew, change zone representation, or be corrected.
- **Monotonic clock:** never intentionally goes backward during a boot; use for timeouts and durations.
- **Media clock:** codec/RTP sampling timeline; correlation to wall clock needs RTCP or protocol-specific mapping.
- **Source timestamp:** time asserted by the originating device/application.
- **Receipt timestamp:** time recorded by an intermediary; useful but not a substitute for occurrence time.

Keep these separate in schemas.

## Failure handling

When a clock jumps backward, do not reuse sequence/nonce/idempotency values derived only from time. When it jumps forward, guard against expiring all sessions, recordings, or certificates without a recovery route. A device without synchronized time should mark event time quality rather than emit apparently precise timestamps.

## Evidence record

For significant events preserve source timestamp and offset, receipt time, device/clock identity, sync status, estimated uncertainty, sequence/order evidence, timezone conversion rules, and any later correction. Do not “fix” historical raw timestamps in place; append a corrected interpretation with provenance.

