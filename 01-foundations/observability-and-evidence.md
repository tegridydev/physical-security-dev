---
title: Observability and Evidence
summary: Logs, metrics, traces, audit, health, provenance, privacy, and defensible incident evidence for security integrations.
page_type: foundation
domains: [cross-domain]
tags: [observability, logging, audit, evidence, provenance]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: General engineering guidance; evidence admissibility, retention, and privacy duties are jurisdiction specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Observability and evidence

Observability should answer: what happened, according to which component, under whose authority, when, with what confidence, and what was the physical outcome? One application log cannot answer all of those.

## Signals

- **Metrics:** rates, latency distributions, queue depth/age, reconnects, sequence gaps, clock offset, certificate expiry, disk/power/link health.
- **Logs:** structured state transitions, decisions, errors, configuration changes, and lifecycle operations.
- **Traces/correlation:** request through gateway/broker/controller and independent confirmation.
- **Audit:** security-relevant actions and policy decisions protected from unauthorized modification.
- **Evidence objects:** recordings, snapshots, exports, raw messages, access/alarm histories, and their provenance/integrity metadata.

## Event correlation

Carry a bounded correlation ID across protocol boundaries where possible, but preserve the source's original event/transaction ID. A gateway-generated ID must not masquerade as a device ID. Record source, tenant/site, entity, session/boot epoch, sequence, and each timestamp type.

For commands, log requested intent, authenticated human/workload, authorization/policy, target, idempotency ID, protocol dispatch, response, independent sensed outcome, and uncertainty. Do not log credential secrets or full bearer tokens.

## Health is layered

```text
power -> link -> network reachability -> authenticated session
      -> protocol/application response -> data freshness
      -> sensor/actuator physical function
```

A TCP connection or heartbeat proves only its layer. Define freshness and quality for each critical signal. Alarm on sustained or consequential degradation, while retaining the raw transitions needed to diagnose flapping.

## Privacy and minimization

Video, audio, faces, vehicle plates, badge events, mobile identifiers, biometrics, location estimates, occupancy, and operator actions can be personal or sensitive. Log the minimum required fields, restrict access by purpose, redact at collection where feasible, and set retention/deletion holds deliberately.

Do not put secrets, private keys, card data, biometric templates, or unnecessary person names in generic telemetry. Use opaque references to a more restricted system.

## Evidence integrity

Maintain chain of custody appropriate to the context:

- immutable source and acquisition method;
- source/device/system identity and version;
- original and receipt times plus clock quality;
- cryptographic hash and algorithm where used;
- transformations, exports, transcoding, redaction, and operator actions;
- storage/access history and retention/legal-hold state;
- mapping/schema versions and known gaps.

A hash proves later bytes match the hashed bytes; it does not prove the source was trustworthy or the clock correct. Digital signatures likewise require verified key ownership, validity, and protected signing process.

## Operational dashboards

Prioritize actionable conditions: lost event sequence, recording gap, stale door state, controller offline, certificate nearing expiry, time offset, queue overflow, denied high-impact operation, unexpected cross-zone client, or power budget fault. Avoid a single green “system healthy” status that masks degraded layers.

## Diagnostic safety

Diagnostic logging can increase CPU, I/O, storage, network traffic, or privacy exposure. Enable it for a bounded authorized window, preserve pre-change settings, set size/rotation limits, and confirm cleanup. Packet capture is sensitive surveillance evidence and may include credentials; authorize, scope, protect, and delete it under policy.

## Sources

- [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) is the final NIST log-management publication at this baseline; the [Rev. 1 Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd) is tracked as draft, not final.
- [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) supplies OT monitoring, audit, incident, availability, reliability, and safety context.
- [RFC 3339](https://www.rfc-editor.org/info/rfc3339) defines the Internet date/time representation commonly used at integration boundaries; representation alone does not establish clock accuracy or trust.

Evidence admissibility, chain-of-custody procedure, privacy duties, and retention remain jurisdiction- and organization-specific.
