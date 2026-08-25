---
title: "Video bandwidth and storage calculation"
summary: "Calculate design ranges while preserving bitrate variability, overhead, retention, failover, and uncertainty."
page_type: lab
domains:
  - video
tags:
  - bandwidth
  - storage
  - video
scope: global
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Video bandwidth and storage calculation

[Home](../README.md) / [Defensive labs](README.md) / Video capacity calculation

Lab class: **Offline calculation**

## Core calculation

For a constant average stream bitrate B in bits/second over duration T seconds:

~~~text
payload bytes = B × T ÷ 8
usable storage = payload bytes × overhead factor × resilience factor
~~~

Example inputs should be synthetic. A 4 Mbit/s average stream over one day produces about 43.2 GB decimal before container/filesystem/index overhead, retention headroom, replication, failures, exports and other streams.

## Required scenario variables

- codec/profile/level, resolution, frame rate and GOP;
- constant/variable bitrate controls and measured scene range;
- audio, metadata and secondary streams;
- continuous versus event recording and pre/post-event duration;
- transport/container/database/index overhead;
- camera count and synchronized peak behavior;
- edge catch-up/retrieval after outage;
- RAID/erasure coding, replication, hot spare and reserved free space;
- retention/deletion policy, evidence holds and export work area;
- network multicast/unicast fanout and client/analytics copies;
- failure/rebuild throughput and maintenance margin.

## Exercise

Build nominal, busy-scene peak, outage catch-up, and degraded-storage scenarios from synthetic low/nominal/high inputs. State whether units are decimal GB/TB or binary GiB/TiB and preserve the range rather than collapsing variability into one value. Comparison with field measurements belongs to separately governed environment validation after privacy review.

## Evidence checklist

- [ ] Synthetic input set, units, source assumptions, and calculation method recorded
- [ ] Nominal, busy-scene peak, outage catch-up, and degraded-storage scenarios calculated
- [ ] Video, audio, metadata, secondary streams, and synchronized peak behavior included
- [ ] Container, filesystem, index, reserved-space, replication, and resilience overhead included
- [ ] Retention, evidence holds, exports, rebuild throughput, and maintenance margin represented
- [ ] Network fanout and edge catch-up separated from storage consumption
- [ ] Decimal and binary units labelled and uncertainty/ranges preserved

## Related pages

- [Codecs and streaming](../02-protocols/video-and-media/codecs-and-streaming.md)
- [Recording and storage systems](../03-systems/video-surveillance/recording-storage-and-retention.md)
