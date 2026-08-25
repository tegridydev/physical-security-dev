---
title: "Retries, timeouts, and idempotency"
summary: "Bound unreliable operations without duplicating commands or hiding uncertain outcomes."
page_type: development
domains:
  - development
tags:
  - retry
  - timeout
  - idempotency
scope: global
content_status: maintained
technology_status: not-applicable
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: "Protocol-neutral reliability pattern; method safety, idempotency, transaction identity, replay windows, and recovery semantics come from the selected standard or product contract."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Retries, timeouts, and idempotency

[Home](../../README.md) / [Development](../README.md) / [Patterns](README.md) / Retries and idempotency

A timeout says the caller did not receive a usable result before its deadline. It does not prove that the server or physical device did nothing. This distinction is critical for outputs, doors, alarms, PTZ, credential changes, firmware and evidence deletion.

## Operation classes

| Class | Examples | Retry posture |
|---|---|---|
| Pure/read-only | Capability or health query | Usually safe with bounds and freshness rules |
| Idempotent set | Set a named configuration to an exact desired value | Retry only with version/precondition and audit |
| Create with key | Create subscription/event using caller idempotency key | Retry under the protocol's key retention rules |
| Edge-triggered command | Pulse output, unlock, acknowledge, trigger recording | Do not retry blindly; outcome may be uncertain |
| Destructive | Delete evidence/user/configuration, reset, update | Explicit workflow, approval, preconditions and reconciliation |

## Timeout budget

Use one end-to-end deadline divided among connection, TLS/authentication, request write, first response, body/stream and downstream device work. Avoid nested libraries each applying full independent timeouts. Carry cancellation through queues and adapters.

## Retry policy

- Retry only errors classified as transient for the exact operation.
- Use bounded attempts, exponential backoff and jitter.
- Respect server/broker retry guidance without allowing unbounded delay.
- Stop on authentication, authorization, validation, version or safety errors.
- Limit fleet concurrency and reconnect storms.
- Preserve a stable correlation/idempotency identifier across attempts.

## Reconciliation

When outcome is uncertain, query the authoritative state or operation record using a stable identifier. If the protocol cannot disambiguate, surface unknown outcome to the caller/operator; do not convert it to success or failure silently.

## Environment evidence

- [ ] Cite exact method safety/idempotency, transaction identifier, replay-window, timeout, cancellation, and retry semantics.
- [ ] Cover failure before send, partial send, downstream commit before lost response, duplicate request, late response, exhausted deadline, and reconciliation.
- [ ] Record protocol/product versions, retry budget, idempotency retention, cases, observations, uncertain outcomes, and limitations.

## Related pages

- [Polling, subscriptions, and state reconciliation](polling-subscriptions-and-state-reconciliation.md)
- [API and event security](../../06-security-and-assurance/api-and-event-security.md)
