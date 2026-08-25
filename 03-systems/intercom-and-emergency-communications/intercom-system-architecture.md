---
title: Intercom System Architecture
summary: Component, trust, media, identity, availability, and privacy architecture for IP and mixed-technology building intercom systems.
page_type: system
domains: [intercom, networking, access-control, video]
tags: [intercom, call-stations, master-stations, gateways, ip-intercom]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 62820-1-1:2026", "IEC 62820-1-2:2026", "IEC 62820-2:2017"]
coverage_limit: Architecture only; no live relay control, emergency call procedure, acoustic design, accessibility determination, or jurisdiction-specific approval.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Intercom system architecture

An intercom is an identity, call-control, real-time-media, notification, and sometimes physical-control system. Treat those planes separately even when a single appliance or cloud service implements all of them.

## Component model

```text
door/room/help-point station
  -> discovery, registration, and call controller
  -> routing/queue/presence
  -> master station, attendant client, mobile client, or PBX/SIP peer
  -> media path: audio, video, data, recording
  -> optional PACS/door-control request through a separate authority
```

Inventory stations, call controllers, directories, master stations, gateways, media relays, recorders, mobile/cloud services, physical I/O, PoE/power, switches, time, certificates, and external telephony. Record physical location and purpose separately from mutable address, extension, or display name.

## Authorities

| Concern | Normal authority | Integration rule |
|---|---|---|
| device identity/configuration | intercom management system | synchronize deliberately; do not infer from IP address |
| call state and routing | call controller/native system | retain native call and leg identifiers |
| media | negotiated endpoints/relay | report negotiated protection and actual path |
| door authorization | PACS/controller and approved life-safety design | intercom requests; PACS decides and door reports state |
| emergency response | approved operational/safety system | common UI must not replace native authority silently |

A client showing `door released` after sending a relay command is unsafe. Represent request accepted, authorization decision, output state, contact state, and held/forced conditions separately.

## Functional planes

- **Identity and enrollment:** device credentials, directory entries, trusted administrators, certificates, replacement and revocation.
- **Call signalling:** registration, initiation, ringing, queueing, answer, transfer, escalation, termination, failure reason, and presence.
- **Media:** codecs, packet path, jitter/loss handling, echo control, camera source, encryption, recording, and retention.
- **Management:** provisioning, firmware, diagnostics, logs, time, configuration backup, and service access.
- **Physical I/O:** call buttons, tamper, local inputs, amplifiers/speakers, and separately governed control requests.

Protection on one plane does not prove protection on another. For example, an authenticated management session says nothing about signalling trust, media confidentiality, external call routing, or relay authorization.

## Availability and degraded operation

Document behavior for loss of controller, directory, DNS, time, WAN/cloud, mobile push service, PBX gateway, PoE, one network segment, media relay, recorder, and PACS link. State which calls remain local, how queued calls are shown, whether alternate destinations work, and how recovery reconciles duplicate or abandoned calls.

An endpoint heartbeat does not prove microphone, loudspeaker, call button, camera view, intelligibility, or the staffed availability of a destination. Health monitoring should expose each observable function and the age of evidence.

## Security and privacy

- use unique device and administrator identity; remove default/shared credentials;
- segment management, signalling, media, and unrelated tenant/site traffic according to risk;
- restrict remote support, mobile enrolment, directory export, live listening, recording, playback, and control;
- verify negotiated signalling and media protection rather than relying on feature support;
- make recording and live-monitoring indication/consent comply with applicable law and policy;
- minimize retained audio, images, call metadata, phone numbers, and visitor details;
- audit configuration, directory, routing, recording, export, and door-request actions.

## Acceptance evidence

- exact endpoints, controller/gateway versions, roles, identities, and trust anchors;
- call matrix for normal, busy, unanswered, transfer, escalation, and failure paths;
- usable audio/video in representative noise, lighting, bandwidth, and accessibility conditions;
- clock alignment and call/media/audit correlation;
- controller, WAN, PoE, destination, gateway, and PACS-link failure behavior;
- role and tenant isolation, recording behavior, retention, and export;
- native door-state feedback rather than command-success inference.

## Source baseline

[IEC 62820-1-1:2026](https://webstore.iec.ch/en/publication/68745) provides general building-intercom requirements and [IEC 62820-1-2:2026](https://webstore.iec.ch/en/publication/68746) covers systems using IP. [IEC 62820-2:2017](https://webstore.iec.ch/en/publication/32331) adds advanced security building-intercom requirements. Normative content and product conformity must be obtained separately.

See [Intercom and emergency-communication systems](README.md) and [Call routing, media, and door control](call-routing-media-and-door-control.md).
