---
title: "Polling, subscriptions, and state reconciliation"
summary: "Combine snapshots, events, heartbeats, cached state, and device truth predictably."
page_type: development
domains:
  - development
tags:
  - polling
  - subscriptions
  - reconciliation
scope: global
content_status: maintained
technology_status: not-applicable
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: "Protocol-neutral state-reconciliation pattern; snapshot consistency, sequence, subscription, replay, and retention guarantees are protocol- and product-specific."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Polling, subscriptions, and state reconciliation

[Home](../../README.md) / [Development](../README.md) / [Patterns](README.md) / Polling and state

Polling gives periodic snapshots; subscriptions give changes. Neither alone guarantees a complete current state. Events can be lost, duplicated or reordered, while snapshots can be stale, expensive or internally inconsistent.

## State record

Store value, source, source-native identifier, observation time, ingestion time, sequence/revision where supplied, quality/confidence, freshness deadline and the configuration/profile version used to interpret it. Unknown and stale must remain distinct from a legitimate false, closed, inactive or zero value.

## Bootstrap pattern

1. Establish authenticated session and capability/version context.
2. Start or prepare the event subscription without discarding early events.
3. Obtain a consistent snapshot or mark its consistency limitation.
4. Merge buffered events newer than the snapshot boundary.
5. Publish state only after provenance and freshness are known.
6. Periodically reconcile with authoritative snapshots and inventory.

When the protocol cannot provide a revision or atomic boundary, document the race and use conservative unknown/transitional state rather than claiming certainty.

## Polling discipline

- Add jitter to avoid synchronized fleets.
- Bound concurrency, response size and per-device work.
- Distinguish unsupported, denied, offline, timeout, invalid response and stale cache.
- Adapt cadence to operational need without hiding failures.
- Do not poll an actuation endpoint to infer whether a command was authorized or physically completed unless the returned state is explicitly authoritative.

## Subscription discipline

- Track subscription identity, lease/expiry, filters and negotiated schema.
- Renew before expiry with bounded retry and visible failure.
- Deduplicate by stable event identity or carefully scoped composite key.
- Reconcile after reconnect, peer restart, sequence gap or queue loss.
- Persist only the offset/token semantics the protocol guarantees.

## Environment evidence

- [ ] Cite the exact snapshot, sequence, subscription, lease, replay, and retention guarantees used by the implementation.
- [ ] Cover bootstrap races, duplicate/reordered events, sequence gaps, lease expiry, reconnect, peer restart, stale snapshots, and partial inventory.
- [ ] Record protocol/product versions, configuration, synthetic case set, observed state transitions, unresolved races, and reconciliation limits.

## Related pages

- [Reconnect, backpressure, and queues](reconnect-backpressure-and-queues.md)
- [Event normalization and schema evolution](event-normalization-and-schema-evolution.md)
- [Monitoring and health](../../07-operations-and-lifecycle/monitoring-and-health.md)
