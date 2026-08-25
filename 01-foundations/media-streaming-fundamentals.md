---
title: Media Streaming Fundamentals
summary: Separating media encoding, session description/control, packet transport, timing, recording, and security.
page_type: foundation
domains: [video, intercom]
tags: [media, video, audio, rtp, rtcp, rtsp, sdp, webrtc]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: [RFC 3550, RFC 7826, RFC 8866, RFC 8834]
coverage_limit: Conceptual media pipeline; codec/profile/licensing and product-specific behavior require separate verification.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Media streaming fundamentals

“Video stream” hides several independent contracts:

```text
capture -> encode -> describe/negotiate -> control session
        -> packetize/transport -> receive/jitter/decode -> render/record
        -> index/export/verify
```

Authenticate and observe each relevant path. Protecting the management API does not necessarily protect media; supporting a codec does not imply the required profile, level, packetization, resolution, or recording behaviour.

## Components

| Concern | Common technologies | Key questions |
|---|---|---|
| Encoding | H.264/AVC, H.265/HEVC, JPEG, AAC, G.711, Opus | Profile/level, bitrate mode, keyframe cadence, licensing, decoder bounds |
| Description | SDP, ONVIF configuration, vendor JSON/XML | Codec parameters, media address/ports, direction, timing, security |
| Session control | RTSP, SIP, WebRTC signalling, vendor API | Authentication, setup state, teardown, keepalive, renegotiation |
| Media transport | RTP/RTCP, SRTP/SRTCP, interleaved RTP, WebRTC | Loss, jitter, sequence, timestamps, feedback, encryption |
| Recording | edge, NVR/VMS, cloud object storage | continuity, indexes, retention, encryption, evidence integrity |

[RFC 3550](https://www.rfc-editor.org/info/rfc3550) defines RTP and RTCP. RTP provides transport functions for real-time data but does not guarantee delivery or reserve resources. RTCP carries control and reception information; it does not itself prove content integrity.

[RFC 8866](https://www.rfc-editor.org/rfc/rfc8866) defines SDP as a description format. An SDP received over an unauthenticated/unprotected path must not be trusted to select safe media destinations or security parameters. [RFC 7826](https://www.rfc-editor.org/info/rfc7826) defines RTSP 2.0, while many deployed products also implement RTSP 1.0 or product-specific subsets; determine the actual version.

WebRTC is a suite, not one wire protocol. Its media uses protected RTP profiles; [RFC 8834](https://www.rfc-editor.org/info/rfc8834) requires WebRTC endpoints to use SRTP/SRTCP, and [RFC 8827](https://www.rfc-editor.org/rfc/rfc8827) describes the security architecture. Application signalling and authorization remain the product's responsibility.

## Timing and loss

RTP timestamps represent media sampling time, not necessarily UTC. Sequence numbers help detect loss/reordering but can wrap and are scoped to a synchronization source. Correlate media clocks to wall time using applicable RTCP or system metadata, preserving uncertainty.

Design receivers for bounded jitter buffers, packet loss, reorder, duplicate, source restart/identifier change, keyframe acquisition, codec reconfiguration, and silent stall. Backpressure and latency policy must be explicit: dropping old live frames can be preferable to growing an unbounded queue, while recording has different requirements.

## Security and privacy

- Authenticate control/signalling peers and authorize each stream/resource.
- Protect media and metadata in transit where the threat model requires; record where legacy cleartext remains.
- Validate SDP, codec parameters, dimensions, rates, packet sizes, and decoder input.
- Restrict destinations to prevent a device being induced to send media to an attacker-controlled address.
- Treat audio, analytics metadata, thumbnails, and exported clips as sensitive—not only primary video.
- Separate viewing, export, administration, and evidence-deletion permissions.

## Capacity

Plan peak rather than nameplate average: keyframe bursts, multiple profiles, multicast replication, live viewing, recording, playback, analytics, export, failover, and catch-up. Measure end-to-end latency and recording gaps in the authorized target environment, and record the exact stream profiles, topology, load, failover cases, observations, and limitations.
