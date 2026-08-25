---
title: Recording, Storage, and Retention
summary: Recording continuity, storage sizing, indexes, encryption, retention, deletion, legal hold, and recovery models.
page_type: system
domains: [video]
tags: [recording, storage, retention, edge-recording, backups]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [ONVIF Profile G, "IEC 62676-1-1:2013"]
coverage_limit: Architecture and sizing inputs only; retention, evidence, privacy, storage engineering, and legal-hold requirements are site/jurisdiction specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Recording, storage, and retention

Recording is a pipeline, not a disk allocation. A system can retain files yet fail to provide complete, correctly timed, decodable, searchable, authorized evidence.

## Recording lifecycle

```text
capture -> encode -> receive/buffer -> segment -> index -> replicate/protect
 -> search/playback -> export/hold -> expiry/deletion -> media retirement
```

Track media segment, recording track, camera/source, codec/configuration, start/end source and receive times, continuity/gaps, integrity/provenance, storage tier, retention class, hold state, and deletion outcome.

## Recording policy

Define per purpose/source:

- continuous, event-triggered, schedule, manual, or failover recording;
- pre/post event buffer and trigger source;
- primary/substream, audio, metadata, overlays, and privacy masking;
- frame rate, resolution, bitrate/quality, keyframe interval, and codec;
- edge, site, cloud, redundant copy, and failure behavior;
- retention start point and deletion semantics;
- user/role rights for view, export, protect/hold, and delete.

Event-triggered recording depends on detector availability, time, rule/configuration, prebuffer, and recovery; do not advertise its nominal retention as continuous coverage.

## Capacity model

Estimate from measured/contracted peak and distribution, not only average bitrate:

```text
ingest = sum(stream peak bitrate × duty cycle) + protocol/index overhead
usable capacity = retention × ingest × resilience/rebuild/headroom factors
```

Account for variable bitrate scene changes, keyframe bursts, audio/metadata, multiple profiles, failover/catch-up, filesystem/object overhead, replicas/erasure coding, snapshots, export staging, audit, rebuild load, and growth. Thermal, power, network, controller, IOPS, and object/API limits can fail before raw capacity.

## Edge and gap reconciliation

ONVIF [Profile G](https://www.onvif.org/profiles/profile-g/) provides a standardized scope for edge recording configuration/control/retrieval. Actual gap-fill sequencing, bandwidth throttling, retention competition, clock correction, duplicate segments, and device support require product verification.

After outage, preserve source sequence/time and mark unrecoverable intervals. Catch-up traffic must not starve live recording. A later recovered segment may overlap central recording; deduplicate without discarding provenance.

## Retention and deletion

Retention is a policy decision tied to purpose, risk, law, contract, investigation holds, and storage cost. “30 days” must define whether age is capture time, ingest time, or calendar policy; how unavailable cameras and daylight-saving transitions appear; and how protected incidents override expiry.

Deletion must cover primary, replicas, caches, exports, thumbnails, analytics indexes, backups, cloud lifecycle/versioning, and decommissioned disks—while preserving authorized holds. Record deletion request, authority, policy, target scope, completion/evidence, and failures. Cryptographic erasure only works when keys and copies are correctly scoped.

## Resilience and evidence

- Separate recording continuity from configuration/database backup.
- Test restore and search/playback, not merely backup job success.
- Monitor gap duration, late writes, corrupt/undecodable segments, time drift, index lag, capacity forecast, disk/object errors, replica state, and retention failures.
- Restrict direct storage access; use service identities and encryption with managed keys.
- Preserve native master evidence and transformation history for exports.

Return to [Video-surveillance systems](README.md).
