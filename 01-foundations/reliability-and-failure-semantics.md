---
title: Reliability and Failure Semantics
summary: Timeouts, retries, idempotency, backpressure, offline operation, reconciliation, and indeterminate physical outcomes.
page_type: foundation
domains: [cross-domain]
tags: [reliability, retries, idempotency, backpressure, failover]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: General distributed-systems guidance; product and safety behaviour require evidence from the authorized target environment and acceptance by the system owner.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Reliability and failure semantics

The safest default for a timed-out command is **indeterminate**, not failed. The request may have reached a controller and produced a physical effect before the response was lost.

## Failure categories

| Failure | Example | Required distinction |
|---|---|---|
| Omission | event or response never observed | never sent, lost, filtered, or expired |
| Delay | stale alarm arrives after restore | source time versus receipt/order |
| Duplication | reconnect replays retained events | duplicate versus repeated real condition |
| Reordering | restore arrives before alarm | source-local sequence and reconciliation |
| Partial success | batch updates some credentials | per-item outcome and rollback policy |
| Ambiguous actuation | unlock times out | query independent state; do not blind retry |
| Split brain | redundant nodes both act authoritative | fencing/epoch/ownership |
| Resource exhaustion | queue grows during outage | bounded buffer and explicit shedding |

## Delivery language

Avoid promising “exactly once” end to end. A transport, broker, database, and physical controller have different acknowledgement boundaries. Prefer:

- at-most-once attempt;
- at-least-once delivery with consumer deduplication;
- effect-once within a scoped idempotency store;
- ordered only within a named source/partition/session;
- reconciled current state plus immutable event history.

State the boundary and retention duration.

## Retry policy

Classify operations:

- safe read/poll: retry with deadline, jittered backoff, and bounds;
- idempotent write: retry only with the same idempotency key and documented server semantics;
- non-idempotent/actuating command: after ambiguity, reconcile before any retry;
- batch: require per-item result and a deliberate compensation plan.

Retries must respect rate limits, device capacity, alarm priority, maintenance windows, and cancellation. Use circuit breaking or admission control so an offline site cannot create a reconnect storm.

## Offline and restart

Define each component's behaviour when WAN, DNS, time, identity, certificate service, broker, database, or upstream controller is unavailable. Record:

- local cached policy and expiry;
- event buffer capacity and overflow order;
- command acceptance/rejection during isolation;
- sequence/session epoch after reboot;
- time quality and certificate bootstrap;
- catch-up ordering and duplicate policy;
- operator-visible degraded state.

Local controllers should preserve approved safety and access behaviour without depending unnecessarily on enterprise/cloud services. But cached authorization can become stale; set risk-based expiry and reconciliation.

## Backpressure

Bound every queue by count, bytes, and age. Decide what can be coalesced (health state), sampled (telemetry), dropped with a gap marker (low-priority observations), or never silently discarded (critical alarm lifecycle). Separate priority classes so bulk video/export or noisy health events do not starve alarms and control responses.

## Recovery and reconciliation

After reconnect:

1. establish a new authenticated session/epoch;
2. obtain authoritative capabilities and state;
3. compare sequence/checkpoint and identify gaps;
4. replay/catch up within retention and deduplicate;
5. surface unrecoverable gaps and stale mappings;
6. resume commands only after authority and time are valid.

Never hide uncertainty. An explicit `unknown`, `stale`, `gap`, or `indeterminate` is safer than a plausible but false normal state.

## Sources

- [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) supplies the OT availability, reliability, safety, redundancy, recovery, and change-management framing.
- [RFC 9110 section 9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) defines idempotent HTTP methods and cautions about automatic retry boundaries; application and physical effects still require their own semantics.
- [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) provides concrete session, acknowledgement, QoS, expiry, retained-message, and delivery behavior used by many event integrations.

These sources support the shared model, not an exactly-once or safe-retry claim for any product. The exact acknowledgement, persistence, deduplication, failover, and physical-outcome boundary must be verified per protocol and implementation.
