---
title: "Offline packet and trace reading"
summary: "Interpret synthetic or sanitized packet captures with documented provenance and no network or device interaction."
page_type: lab
domains:
  - defensive-labs
tags:
  - packet-analysis
  - offline
scope: global
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Offline packet and trace reading

[Home](../README.md) / [Defensive labs](README.md) / Offline packet reading

Lab class: **Offline fixture**

## Purpose

Build a layered interpretation without assuming a dissector's label proves semantics, security or conformance.

## Procedure

1. Use a synthetic fixture or a sanitized capture with documented ownership, authority, provenance, and digest.
2. Record capture source, topology, timestamp/timezone, interface, filter, truncation and packet-loss limitations.
3. Identify physical/link, network, transport, security/session, application and domain layers.
4. Reconstruct endpoints, connection direction, DNS/discovery, multicast groups and negotiated ports.
5. Identify plaintext versus protected portions; do not import real private keys into general analysis tooling.
6. Follow one transaction/event/stream using sequence, transaction, session and correlation identifiers.
7. Mark retransmission, duplicate, gap, out-of-order, reset, timeout and reconnect evidence.
8. Compare observed fields with the exact standard/profile/vendor revision.
9. Redact addresses, credentials, media, card values, identities and facility details before sharing notes.

## Questions

- Which endpoint initiated the connection and who authenticated whom?
- Are discovery and operational traffic scoped to intended zones?
- Does encryption cover only credentials, the whole control session, media, or nothing?
- Which delivery acknowledgement exists, and what does it actually prove?
- Are timestamps source, transport or capture timestamps?
- Could the trace be incomplete because of switching, offload, multicast or asymmetric routing?

## Evidence checklist

- [ ] Fixture provenance, authority, digest, sensitivity, capture point, and topology recorded
- [ ] Capture time basis, filter, snap length, offload, asymmetry, loss, and truncation limitations documented
- [ ] Link, network, transport, security/session, application, and domain layers separated
- [ ] One transaction, event, or stream followed through identifiers and timing
- [ ] Retransmission, duplication, gaps, reordering, resets, timeout, and reconnect evidence distinguished
- [ ] Protection, authentication, acknowledgement, and conformance claims bounded to observed evidence
- [ ] Addresses, identities, credentials, media, and facility details sanitized before sharing

## Related pages

- [Protocol catalogue](../02-protocols/README.md)
- [Offline trace parsing example](../05-development-and-integration/examples/offline-trace-parsing-python.md)
