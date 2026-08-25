---
title: SIA DC-07 receiver-to-automation interface
summary: Developer reference for alarm receiver to monitoring-automation communication and its edition ambiguity.
page_type: protocol
domains: [alarms]
tags: [sia, dc-07, receiver, automation, central-station]
scope: global
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: [SIA DC-07]
coverage_limit: SIA's public page lists DC-07-2001.04 while its store describes DC-07-2012; the exact purchased edition and vendor implementation must be reconciled before development.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# SIA DC-07 receiver-to-automation interface

[Home](../../README.md) / [Protocols](../README.md) / [Alarm monitoring](README.md) / DC-07

SIA DC-07 defines a common interface between alarm signal receivers and monitoring automation computers. It is the **inside-the-monitoring-centre** handoff, not the protected-premises-to-receiver transport.[^sia-dc07]

```text
premises ── alarm transport ──> receiver ── DC-07 ──> automation
                                  │                      │
                                  │ protocol status      ├─ event persistence
                                  │ line/receiver fault  ├─ operator workflow
                                  └ event normalization  └─ dispatch policy
```

## Edition warning

SIA's public standards page labels the available page **DC-07-2001.04**.[^sia-dc07] SIA's store separately describes a **SIA DC-07-2012 Standard**.[^sia-dc07-store] Because those official sources disagree, record the title page, revision date, addenda, interpretations, and receiver vendor's claimed edition from the actual purchased document. Do not silently call either one “the current DC-07” in an implementation contract.

## What the interface carries

The public scope says DC-07 covers a common receiver/computer format, codes identifying dialer protocols, and receiver conditions requiring technical attention. A developer-facing canonical model should therefore separate:

- received subscriber event and its original dialer/protocol identity;
- receiver, line/channel, and account routing identifiers;
- receiver-generated state, fault, and technician-attention conditions;
- source timestamp, receiver timestamp, and automation ingest timestamp;
- protocol acknowledgement and automation persistence status;
- standard code versus vendor extension.

Do not discard receiver-health messages as “not alarm events.” A receiver path failure or backlog may be more operationally important than a single subscriber event.

## Adapter design

- Implement the exact purchased edition's frame, code, continuation, acknowledgement, and retry rules.
- Bound message length and queued/unacknowledged records; backpressure must not silently drop high-priority events.
- Commit accepted events durably before acknowledging if the protocol/product contract defines acknowledgement as acceptance.
- Use an idempotency key derived from stable receiver identity and the protocol's own correlation/sequence data, not only event text and wall-clock time.
- Preserve unknown standard codes and manufacturer extensions with namespaces.
- Keep receiver connectivity state independent from individual account state.
- Reconcile state after reconnect; a live socket does not prove the backlog is complete.
- Sanitize raw fields before logs and UIs while retaining protected evidence for diagnosis.

SIA's public scope says independent code extensions make a device noncompliant and directs additions through SIA.[^sia-dc07] In practice, isolate vendor extensions instead of passing them off as standard DC-07.

## Security model

The public description does not claim modern cryptographic protection. Treat the receiver-to-automation network as a high-trust conduit: segment it, mutually authenticate endpoints using a supported secure wrapper or network control, restrict receiver and automation management, encrypt across shared infrastructure, and monitor for reconnect storms, sequence gaps, unexpected receiver IDs, and code-volume anomalies.

Never authorize dispatch solely because a syntactically valid DC-07 message arrived. Automation must bind it to a configured receiver/channel/account relationship and apply site policy.

## Safety boundary

Use a synthetic receiver feed and non-dispatch automation tenant. A receiver test mode is not sufficient unless its downstream route is independently proven unable to call, notify, unlock, silence, or dispatch.

## Primary sources

[^sia-dc07]: Security Industry Association, [DC-07-2001.04 — Receiver-to-Computer Interface Protocol](https://www.securityindustry.org/industry-standards/dc-07-2001-04/), reviewed 2026-08-25.
[^sia-dc07-store]: Security Industry Association store, [SIA DC-07-2012 Standard](https://mysia.securityindustry.org/ProductCatalog/Product.aspx?ID=17094), reviewed 2026-08-25.
