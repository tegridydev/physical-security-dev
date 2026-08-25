---
title: "Time drift and event correlation"
summary: "Use synthetic timelines to distinguish occurrence, observation, ingestion, clock quality, and causal order."
page_type: lab
domains:
  - cross-domain
tags:
  - time
  - correlation
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "RFC 5905"
  - "RFC 8915"
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Time drift and event correlation

[Home](../README.md) / [Defensive labs](README.md) / Time drift and correlation

Lab class: **Offline synthetic timeline fixture**

## Fixture design

Create synthetic door, camera, alarm, API, broker and recorder events containing occurrence time, ingestion time, offset/timezone, source clock status, sequence and correlation ID. Include one clock 45 seconds fast, a device reboot/sequence reset, a duplicated delayed event and an ingestion backlog.

## Procedure

1. Preserve every original timestamp and offset; do not overwrite with UTC conversion.
2. Normalize display to UTC while retaining source values.
3. Calculate apparent offset between sources only where a common event/correlation makes comparison defensible.
4. Use sequence and causation to order events when clocks disagree.
5. Mark uncertainty caused by drift, reboot, capture delay, queueing and missing synchronization status.
6. Produce a timeline with separate occurred, observed/received and processed axes.
7. Explain which conclusions remain unsupported.

## Expected learning

Authenticated NTP protects aspects of time exchange but does not guarantee the upstream time is correct. Wall-clock order alone cannot prove causation. Video overlay time, file/container time and VMS event time may come from different clocks.

## Evidence checklist

- [ ] Fixture provenance, digest, source clocks, time zones/offsets, and sequence scopes recorded
- [ ] Original timestamps preserved alongside normalized UTC display values
- [ ] Occurrence, observation/receive, ingestion, and processing times kept separate
- [ ] Drift, reboot/reset, duplication, delay, backlog, and missing synchronization state represented
- [ ] Apparent offsets calculated only where a defensible common event exists
- [ ] Sequence and causal evidence used without treating wall-clock order as proof
- [ ] Timeline conclusions state uncertainty and unsupported inferences explicitly

## Sources

- [RFC 5905 NTPv4](https://www.rfc-editor.org/rfc/rfc5905), accessed 2026-08-25.
- [RFC 8915 Network Time Security](https://www.rfc-editor.org/rfc/rfc8915), accessed 2026-08-25.

## Related pages

- [Logging, time, and evidence integrity](../06-security-and-assurance/logging-time-and-evidence-integrity.md)
- [Timestamp normalization example](../05-development-and-integration/examples/timestamp-normalization-csharp.md)
