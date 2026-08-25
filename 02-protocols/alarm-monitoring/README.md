---
title: Alarm-monitoring protocols
summary: Index of SIA event reporting, receiver integration, Contact ID, and audio-verification protocols.
page_type: index
domains: [alarms]
tags: [sia, alarms, central-station, receivers]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [ANSI/SIA DC-09-2026, SIA DC-03-2017, SIA DC-05-2016, SIA DC-07, SIA AV-01-2014, IEC 60839-5 series]
coverage_limit: Family navigation and public-edition status; purchased SIA standards and receiver/product profiles remain required for implementation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Alarm-monitoring protocols

[Home](../../README.md) / [Protocols](../README.md) / Alarm monitoring

Alarm communication has several distinct interfaces. Confusing them produces brittle integrations:

```text
protected premises                  monitoring centre

panel / communicator  ── DC-09 ──> receiver ── DC-07 ──> automation
        │                 │            │
        └─ DC-03 or       │            └─ acknowledgement, receiver status
           Contact ID     └─ IP transport of event content

operator telephone ── DTMF / voice ──> premises audio-verification system
                         AV-01
```

| Reference | Interface | Status note |
|---|---|---|
| [SIA DC-09](sia-dc-09.md) | Premises equipment to central-station receiver over IP | Current ANSI/SIA edition is DC-09-2026 |
| [SIA DC-03](sia-dc-03.md) | SIA-format alarm communicator to receiver | Current public SIA listing is DC-03-2017 |
| [Contact ID / SIA DC-05](contact-id-sia-dc-05.md) | DTMF alarm communicator to receiver | Legacy but widely encountered; public listing is DC-05-2016 |
| [SIA DC-07](sia-dc-07.md) | Receiver to monitoring automation computer | SIA's public index and store expose conflicting edition labels; verify the purchased copy |
| [SIA AV-01](sia-av-01.md) | Monitoring operator to premises audio-verification equipment | Public listing is AV-01-2014; DTMF command-set standard |
| [IEC 60839 alarm transmission](iec-60839-alarm-transmission.md) | Alarm-transmission systems, equipment, and network requirements | IEC 60839-5-1/-5-2/-5-3 baselines plus separately labelled IEC TS 60839-7-8 IP message-protocol context |

## Shared engineering concerns

- Preserve account, receiver, line/channel, partition, zone/user, qualifier, event, and timestamp semantics without silently coercing unknown values.
- Treat transport acceptance, protocol acknowledgement, automation ingestion, operator presentation, and response as different milestones.
- Make duplicate detection and replay handling explicit. Alarm networks intentionally retry; duplicate delivery is normal, while duplicate operator action may not be.
- Record occurrence time, transmitter time, receiver time, and ingest time separately.
- Fail closed on malformed control messages, but do not discard the raw evidence required to diagnose a field incompatibility.
- Never infer restoration merely because a fault event stops arriving. Use an explicit restore event or authoritative state query when the protocol and product support one.

## Safety boundary

Monitoring-path work can suppress, delay, duplicate, or falsely generate dispatch-relevant events. Keep development on synthetic accounts and isolated receiver/automation paths. Never use real subscriber identifiers or exercise panic, duress, fire, medical, hold-up, lockdown, or dispatch workflows without the monitoring centre's written authorization and operational controls.

## Primary source

- Security Industry Association, [At-a-Glance Guide to SIA Standards](https://www.securityindustry.org/industry-standards/at-a-glance-guide-to-sia-standards/), reviewed 2026-08-25.
