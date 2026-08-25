---
title: "Reconnect, backpressure, and queues"
summary: "Keep integrations bounded and truthful through bursts, downstream failure, reconnect, and replay."
page_type: development
domains:
  - development
tags:
  - backpressure
  - queues
  - reconnect
scope: global
content_status: maintained
technology_status: not-applicable
verification: V1
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: "Protocol-neutral reliability pattern; acknowledgement, persistence, ordering, replay, and flow-control guarantees are protocol- and product-specific."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Reconnect, backpressure, and queues

[Home](../../README.md) / [Development](../README.md) / [Patterns](README.md) / Backpressure and queues

Unbounded queues convert downstream failure into memory exhaustion, disk exhaustion, stale alarms and a larger recovery burst. Every buffer needs capacity, priority, persistence, expiry, overflow, observability and recovery semantics.

## Queue contract

Define producer, consumer, item identity, ordering partition, maximum count/bytes/age, persistence and encryption, acknowledgement point, retry/dead-letter behavior, priority, overflow action, sensitive-data retention, and recovery reconciliation.

## Overload choices

- Backpressure: slow or stop producers when the protocol and physical function permit it.
- Coalesce: replace multiple state updates with the latest state while retaining transition/audit requirements.
- Drop: only for explicitly disposable data, with counters and visible degradation.
- Spill to disk: protect confidentiality/integrity and enforce capacity/expiry.
- Shed optional work: preserve alarms, health and command outcomes ahead of thumbnails or enrichment.
- Fail closed/open: never choose generically; document the physical and safety authority.

## Reconnect state machine

Use disconnected, connecting, authenticating, synchronizing, active, degraded and stopped states. Apply jittered bounded backoff, reset only after sustained health, and avoid parallel reconnect loops. On reconnect, renew identity/subscriptions, validate negotiated version, reconcile snapshot and events, and report any unrecoverable gap.

## Ordering and parallelism

Partition ordering by the smallest domain that requires it: device, door, alarm account, stream or credential. Global ordering is expensive and often false. Keep per-key work serialized only where state transitions require it, with bounded concurrency across independent keys.

## Environment evidence

- [ ] Cite broker/protocol acknowledgement, persistence, ordering, credit/flow-control, replay, and failover guarantees.
- [ ] Cover full queues, byte/age limits, priority starvation, spill exhaustion, consumer failure, reconnect storms, replay, and unrecoverable gaps.
- [ ] Record product versions, configuration, load shape, queue metrics, overflow decisions, observations, and limitations.

## Related pages

- [Polling, subscriptions, and state reconciliation](polling-subscriptions-and-state-reconciliation.md)
- [Monitoring and health](../../07-operations-and-lifecycle/monitoring-and-health.md)
