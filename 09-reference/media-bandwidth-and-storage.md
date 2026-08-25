---
title: "Media bandwidth and storage"
summary: "A unit-safe capacity model for video, audio, metadata, retention, peaks, protection overhead, and operational headroom."
page_type: reference
domains:
  - video
  - infrastructure
tags:
  - bandwidth
  - storage
  - retention
  - capacity-planning
  - units
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "BIPM SI Brochure, 9th edition"
  - "IEC 80000-13:2025"
coverage_limit: "Deterministic formulas and a synthetic worksheet only; codec behavior, scene complexity, product overhead, storage protection efficiency, retention law, failure performance, and measured workloads are deployment-specific."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Media bandwidth and storage

[Home](../README.md) / [Reference](README.md) / Media bandwidth and storage

Capacity is a workload model, not a camera-count lookup. Measure representative streams and failure modes, preserve units, and keep payload, network, usable storage, raw media, and retained evidence as distinct quantities.

The worked scenario is a synthetic unit-checking worksheet, not a recommendation, field measurement, or product-capacity result.

## Unit discipline

| Symbol | Meaning |
|---|---|
| `bit`, `kbit`, `Mbit`, `Gbit` | bits; decimal prefixes mean powers of 1000 |
| `B`, `kB`, `MB`, `GB`, `TB` | bytes; `1 B = 8 bit`; decimal prefixes mean powers of 1000 |
| `KiB`, `MiB`, `GiB`, `TiB` | binary byte multiples, powers of 1024 |
| `s`, `h`, `d` | seconds, hours, days; define recording schedule explicitly |

Network tools often report bit/s while storage products report decimal bytes and operating systems may display binary units. Always write the unit, prefix basis, and whether a value is payload, wire, usable, or raw.

## Core model

For stream `i`:

```text
mean_payload_bps_i = mean_video_bps_i + mean_audio_bps_i + mean_metadata_bps_i

retained_payload_bytes =
  sum(mean_payload_bps_i × recorded_seconds_per_day_i × retention_days_i) / 8

planned_logical_bytes =
  retained_payload_bytes × container_index_filesystem_factor

required_raw_bytes =
  planned_logical_bytes × storage_protection_factor / target_fill_fraction
```

The factors are not universal constants:

- `container_index_filesystem_factor` must come from measurement or documented architecture and can include container, index, thumbnail, database, journal, filesystem, and metadata effects;
- `storage_protection_factor` must be calculated for the exact mirror/replica/erasure/parity layout, drive count/capacity, hot spares, and failure policy;
- `target_fill_fraction` is a design-selected operating limit below physical fullness, not a standards value.

Do not multiply an already vendor-reported “usable after protection” capacity by a protection factor again.

## Network model

| Quantity | Calculation or evidence |
|---|---|
| Mean ingest payload | Sum of measured mean video/audio/metadata bitrates for simultaneously recording streams |
| Peak ingest payload | Measured short-window peaks plus synchronized keyframe/restart behavior |
| Wire rate | Payload plus RTP/RTCP, UDP/TCP/IP, Ethernet, TLS/SRTP, tunneling, retransmission, and encapsulation overhead for actual packet sizes |
| Read/export load | Concurrent live views, playback, analytics, export, replication, scrubbing, thumbnails, and rebuild reads |
| Failover load | Streams reassigned during recorder/link/node failure plus reconnect/keyframe surge |
| Control-plane load | Discovery, authentication, events, health, time, and management—not normally large, but latency-sensitive |

Do not apply one fixed percentage for network overhead across all packet sizes and transports. Measure actual wire behavior. Average bitrate sizes retention; peak and burst behavior sizes interfaces, buffers, switching, uplinks, and recorder ingest.

## Workload variables

For each stream or policy class, record:

| Variable | Why it changes the result |
|---|---|
| Codec, profile, level, bit depth/chroma | Encoder/decoder compatibility and compression behavior |
| Resolution and frame rate | Source sample volume and operational requirement |
| Rate control and target/max bitrate | Mean versus peak behavior; “VBR” is not a measured distribution |
| GOP/keyframe interval | Seek/recovery behavior and synchronized bursts |
| Scene, lighting, noise, motion, weather | Real compression workload; day/night can differ materially |
| Audio tracks | Continuous extra bitrate and retention/privacy impact |
| Metadata/analytics | Event/object streams, indexes, thumbnails, model/version data |
| Recording mode | Continuous, schedule, event, pre/post-event, edge buffering |
| Retention class | Different cameras/evidence may have different policy and legal holds |
| Simultaneous consumers | Live, playback, export, analytics, federation, mobile clients |

Use [codecs and streaming](../02-protocols/video-and-media/codecs-and-streaming.md), [recording, storage, and retention](../03-systems/video-surveillance/recording-storage-and-retention.md), and the offline [defensive capacity lab](../08-defensive-labs/video-bandwidth-and-storage-calculation.md).

## Synthetic worked worksheet

The worksheet is conceptual arithmetic using synthetic assumptions.

Assume solely for demonstrating units:

- 48 continuously recorded streams;
- 4 Mbit/s measured-mean payload per stream;
- 30 days retention;
- an assumed logical overhead factor of `1.12`;
- an assumed target fill fraction of `0.75`;
- calculate one logical copy first; do not assume a protection factor.

```text
per stream per day
= 4,000,000 bit/s × 86,400 s / 8
= 43,200,000,000 B
= 43.2 GB (decimal)

48 streams × 30 days
= 43.2 GB × 48 × 30
= 62,208 GB
= 62.208 TB retained payload

logical data including the synthetic 1.12 factor
= 62.208 TB × 1.12
= 69.67296 TB

raw capacity before any protection-layout factor,
at the synthetic 0.75 target fill
= 69.67296 TB / 0.75
= 92.89728 TB
```

This result is deliberately incomplete. If the exact design needs mirroring, parity, erasure coding, replicas, hot spares, or cloud copies, calculate the real physical/raw effect from that design. Do not simply double it unless the storage architecture truly stores two full physical copies and no other effects apply.

The corresponding assumed mean video payload is `48 × 4 Mbit/s = 192 Mbit/s`. That is not peak wire rate. A synthetic peak multiplier would be only a scenario input, never a codec fact.

## Retention is not only capacity

- Define whether “30 days” means 30 × 24 hours, calendar-day boundaries, or local-time policy through daylight-saving transitions.
- Treat legal hold, incident bookmark, export, and evidence copy as separate retention states.
- Define deletion authority, propagation, tombstone/audit evidence, failed deletion, backup/replica behavior, and clock source.
- Record gaps explicitly; do not extend an older image and call it continuous retention.
- Preserve source stream/configuration changes so bitrate shifts and evidence interpretation are explainable.
- Separate storage occupancy from searchable/indexed/decodable evidence availability.

Jurisdiction, regulator, contract, labor/privacy, evidence, and litigation requirements require qualified review. This page provides no universal retention period.

## Failure and recovery capacity

Normal steady-state utilization can conceal failure bottlenecks. Model at least:

- one recorder/node/link/PSU/drive/failure-domain unavailable;
- rebuild or re-protection reads/writes while recording continues;
- simultaneous device restart and keyframe burst after power/network restoration;
- edge-recording backlog upload plus live ingest;
- export/playback during an incident;
- replication site or cloud path unavailable and later catching up;
- metadata/index rebuild and database recovery;
- depleted free space, retention deletion lag, and backpressure behavior.

Availability claims need measured sustained performance at the intended fill level and failure state—not disk/interface headline throughput.

## Acceptance worksheet

- [ ] Decimal/binary and bit/byte units explicit
- [ ] Every stream class has measured mean, peak window, and variability evidence
- [ ] Video, audio, metadata, container/index/filesystem effects separated
- [ ] Continuous/event/schedule/pre/post recording seconds defined
- [ ] Logical, usable, raw, protected, spare, reserve, and target-fill capacities separated
- [ ] Live/playback/export/analytics/replication/rebuild concurrency modeled
- [ ] Day/night, motion, weather, firmware, codec, and configuration changes sampled
- [ ] Network payload, wire rate, packet rate, loss/retransmission, and uplink oversubscription supported by environment evidence
- [ ] Failure, restoration surge, edge backlog, and degraded protection modeled
- [ ] Retention/legal hold/deletion/privacy rules approved by qualified owners
- [ ] Result recorded as assumption, calculation, vendor claim, or environment measurement—not mixed

## Sources

- **BIPM-SI** — [The International System of Units (SI Brochure), 9th edition][BIPM-SI], BIPM, current online edition accessed 2026-08-25.
- **IEC-INFO** — [IEC 80000-13:2025, quantities and units for information science and technology][IEC-INFO], IEC, 2025.
- **RTP** — [RFC 3550: RTP][RTP], IETF, July 2003.
- **H264-RTP** — [RFC 6184: RTP Payload Format for H.264 Video][H264-RTP], IETF, May 2011.
- **H265-RTP** — [RFC 7798: RTP Payload Format for HEVC][H265-RTP], IETF, March 2016.
- **AV1-RTP** — [RFC 9364: RTP Payload Format for AV1][AV1-RTP], IETF, March 2023.

[BIPM-SI]: https://www.bipm.org/en/publications/si-brochure
[IEC-INFO]: https://webstore.iec.ch/en/publication/87379
[RTP]: https://datatracker.ietf.org/doc/rfc3550/
[H264-RTP]: https://datatracker.ietf.org/doc/rfc6184/
[H265-RTP]: https://datatracker.ietf.org/doc/rfc7798/
[AV1-RTP]: https://datatracker.ietf.org/doc/rfc9364/
