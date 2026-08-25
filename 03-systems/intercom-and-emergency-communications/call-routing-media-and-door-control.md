---
title: Intercom Call Routing, Media, and Door Control
summary: Call-leg, media-session, recording, and door-release boundaries for secure intercom integration and operations.
page_type: system
domains: [intercom, video, access-control, networking]
tags: [call-routing, sip, media, door-release, recording]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["IEC 62820-1-2:2026", "IEC 62820-2:2017"]
coverage_limit: Architecture and state semantics only; no dial plan, relay wiring, lock actuation, emergency routing, or legal conclusion on recording.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Intercom call routing, media, and door control

One user-visible call can contain multiple signalling legs, media sessions, transfers, forks, recordings, and an optional access-control transaction. Give each its own identity and lifecycle.

## Canonical call model

```text
call request -> routing decision -> destination leg(s) -> answer/timeout/failure
             -> audio/video negotiation -> active media -> hold/transfer/end
             -> optional access request -> PACS decision -> door telemetry
```

Useful identifiers include source station, native call ID, integration correlation ID, each destination leg, media session, recording object, operator/client, access request, door transaction, and case/incident. Preserve native cause codes and timestamps rather than reducing outcomes to answered/unanswered.

## Routing

Route by approved site, station type, time schedule, occupancy/staffing state, priority, language/accessibility need, and escalation policy. Treat directory and route changes as privileged configuration with version, actor, approval, and rollback.

Test and document:

- simultaneous ringing versus ordered escalation;
- busy, declined, unreachable, unanswered, and controller-unavailable states;
- transfer, consult, park/hold, queue, and abandoned-call behavior where supported;
- external PBX/PSTN or mobile/cloud boundary, caller identity, and return path;
- duplicate delivery after failover and recovery;
- priority interaction without allowing routine traffic to starve emergency calls.

Do not infer that push notification delivery means the mobile user received, opened, or answered the call.

## Media and recording

Signalling may describe media while RTP or another transport follows a different route. Record the negotiated codec, endpoints/relay, direction, encryption state, clock/time basis, packet-loss/jitter observations, and any transcoding. See [SIP and SRTP](../../02-protocols/video-and-media/sip-and-srtp.md), [RTSP/RTP/RTCP/SDP](../../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md), and [WebRTC](../../02-protocols/video-and-media/webrtc.md).

Recording requires a declared purpose, legal basis/policy, notification or consent where applicable, access control, retention, export, integrity, and deletion. A recording icon in one client does not prove every leg was captured or that media remained intelligible.

Measure end-to-end usability: speech intelligibility, echo, clipping, gain, delay, packet loss, camera framing, lip/event timing, and behavior during route transitions. Codec support alone is not evidence of acceptable communication.

## Door-control boundary

Preferred flow:

```text
identified operator + active call/context
 -> constrained unlock request with door and reason
 -> PACS policy/controller decision
 -> decision result
 -> lock-output/contact/door-state telemetry
 -> attributable audit across both systems
```

- The intercom must not possess broad controller credentials merely to request one action.
- Scope operator rights by site, door, time, call state, and action; require stronger confirmation where risk warrants.
- Avoid exposing raw relay toggles in general clients. Use a semantic, bounded request.
- Do not substitute video or voice recognition for approved credentialing without explicit policy and assessment.
- A successful API or relay write is not proof the lock changed or door opened/closed.
- Life-safety, egress, emergency release, lockdown, and fire interaction remain with the approved design and authority.

See [Locks, egress, and life safety](../access-control/locks-egress-and-life-safety.md).

## Failure-safe presentation

Show stale video, missing audio, failed route, unavailable recording, PACS timeout, access denial, unknown door state, and audit-delivery failure explicitly. Never replay a cached image as live without prominent timestamp and state. If an operator cannot verify the caller or door, the UI should support the approved alternate process rather than silently weakening authorization.

## Source baseline

[IEC 62820-1-2:2026](https://webstore.iec.ch/en/publication/68746) addresses IP building-intercom systems; [IEC 62820-2:2017](https://webstore.iec.ch/en/publication/32331) covers advanced security intercom used for danger/emergency recognition and instruction. Exact protocol, conditional functions, access integration, and conformity remain product-specific.

Return to [Intercom and emergency-communication systems](README.md).
