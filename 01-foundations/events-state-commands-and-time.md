---
title: Events, State, Commands, and Time
summary: A rigorous model for observations, reconstructed state, requested actions, acknowledgements, ordering, and timestamps.
page_type: foundation
domains: [cross-domain]
tags: [events, state, commands, timestamps, ordering]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [RFC 3339]
coverage_limit: Generic semantic model; each protocol defines its own delivery and state machine.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Events, state, commands, and time

Treating an event as current state—or an acknowledgement as physical completion—is one of the most dangerous integration errors.

## Four distinct records

| Record | Meaning | Example |
|---|---|---|
| Observation/event | Something was reported at a point in time | Door contact changed to open |
| State estimate | Best current model assembled from evidence | Door is believed open as of sequence 884 |
| Command | Requested intent | Unlock door for five seconds |
| Outcome/confirmation | Evidence of acceptance or physical result | Controller accepted; lock monitor later reported unlocked |

An access-granted event says a decision was granted, not necessarily that the door opened. A relay-activated response says an output was driven, not that a lock moved. Confirmations should identify what was actually measured.

## Event envelope

A useful canonical event contains:

```yaml
event_id: source-or-derived-unique-id
event_type: access.door.contact.changed
entity_id: site-a/building-1/door-004
source_time: 2026-08-25T10:04:17.314+10:00
received_time: 2026-08-25T10:04:17.402+10:00
sequence: 884
value: open
quality: confirmed
source: controller-2
schema_version: 2
```

If the source does not provide a stable event ID, a derived ID is a local deduplication aid, not source truth. Hashing mutable serialization can produce different IDs for the same semantic event.

## Ordering and duplicates

Across reconnects, queues, gateways, and redundant paths, expect:

- duplicate delivery;
- events arriving out of source order;
- gaps in sequence;
- reset or wrap of counters;
- same timestamp for multiple events;
- clock stepping backward or forward;
- late delivery after a newer snapshot;
- replay of retained or cached messages.

Prefer source-local sequence when documented. Do not impose a false global order by receive time. Track an ordering key such as `(source, boot/session epoch, sequence)` and define what happens when one component is missing.

## Reconstructing state

Use snapshots to establish a baseline and events to advance it:

```text
subscribe/buffer -> fetch snapshot -> reconcile boundary -> apply later events
```

The exact safe ordering is protocol specific. If the API cannot provide a sequence-consistent boundary, mark the state uncertain during reconciliation. Periodic authoritative snapshots can detect silent event loss.

State should include quality:

- `confirmed`: direct recent authoritative evidence;
- `derived`: calculated from other fields;
- `stale`: age exceeds policy;
- `unknown`: insufficient or contradictory evidence;
- `unsupported`: source cannot express the property.

Unknown must not silently become a safe/normal value.

## Command lifecycle

Model at least:

```text
requested -> authorized -> accepted/rejected -> dispatched
          -> physically-confirmed | timed-out | indeterminate | compensated
```

Use an idempotency or command ID where the protocol supports one. After a timeout, query authoritative state before retrying an actuation. Automatic compensation is itself an actuation and may be unsafe when the first result is unknown.

## Time fields

Keep source occurrence time, device monotonic/order value, receipt time, normalization time, and storage time separate. Use an unambiguous offset or `Z` following the Internet timestamp profile in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339). Also retain clock uncertainty, synchronization status, or device-reported quality when available.

Wall-clock time is for correlation; monotonic time is for local durations and timeouts. Do not calculate a five-second unlock or retry interval from a clock that can step.

## Alarm lifecycle

An alarm, acknowledgement, restore, cancel, and operator closure are distinct events. “Restore” means the source condition cleared; it does not prove the alarm was handled. Preserve the original alarm and append lifecycle facts rather than overwriting history.

