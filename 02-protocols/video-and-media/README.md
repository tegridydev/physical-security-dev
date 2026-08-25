---
title: "Video and media protocols"
summary: "Index for discovery, control, signaling, transport, security, and codec behavior in physical-security media systems."
page_type: index
domains: [video, intercom]
tags:
  - onvif
  - rtsp
  - rtp
  - webrtc
  - sip
scope: global
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: safety-relevant
standards: [ONVIF Network Interface Specifications 26.06, ONVIF Profile V Release Candidate]
coverage_limit: "Navigation and layer boundaries only; no device, codec, network, or conformance behavior is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Video and media protocols

[Knowledge base](../../README.md) / Video and media protocols

Use this section when implementing or reviewing camera, recorder, video-management, intercom, or browser-media integrations. It separates device/service control from session signaling, media transport, codec payloads, and application policy. Supporting one layer never implies support for the others.

## Reading map

| Module | Primary question | Status covered |
|---|---|---|
| [ONVIF](onvif.md) | How are conformant physical-security devices discovered, configured, and controlled? | Network Interface Specifications 26.06; active, release-candidate, deprecated, and deprecating profiles as at 2026-08-25 |
| [GB/T 28181](gbt-28181.md) | How do Chinese public-security video systems register, catalogue, signal, stream, and report events? | GB/T 28181-2022 with related GB 35114-2017 security and GB/T 43026-2023 test context |
| [RTSP, RTP, RTCP, and SDP](rtsp-rtp-rtcp-sdp.md) | How are stored/live sessions described, controlled, transported, and measured? | RTSP 1.0 and 2.0; current RTP and SDP bases |
| [WebRTC](webrtc.md) | How is low-latency encrypted browser/native real-time media established? | IETF WebRTC protocol suite and W3C WebRTC Recommendation |
| [SIP and SRTP](sip-and-srtp.md) | How do intercom and voice/video endpoints signal calls and protect media? | SIP core, SRTP, and DTLS-SRTP |
| [Codecs and streaming](codecs-and-streaming.md) | How do codecs, packetization, keyframes, bitrate, loss, latency, and adaptive delivery interact? | H.264, H.265, AV1, JPEG, AAC, Opus, HLS, and MPEG-DASH |
| [SRT and RIST](srt-and-rist.md) | How do contribution links carry live media across impaired IP paths? | SRT project protocol—the expired Internet-Draft is not an IETF standard—and current VSF RIST profiles; neither is an ONVIF or evidence-export replacement |

## Layer model

1. **Discovery and management:** ONVIF device/service APIs and product profiles.
2. **Session description and signaling:** SDP, RTSP, SIP, or an application-defined WebRTC signaling channel.
3. **Transport and feedback:** RTP/RTCP, SRTP/SRTCP, WebRTC transports, or container/file transfer.
4. **Encoding:** video and audio codecs plus their payload formats.
5. **Application policy:** identity, authorization, audit, retention, privacy, rate limits, and failure handling.

Treat every boundary as independently authenticated and authorized. A valid media URL, session identifier, ICE candidate, or SIP dialog identifier is not an authorization decision.

## Integration defaults

- Prefer encrypted transports and authenticated discovery/control on managed networks.
- Negotiate an explicit profile, codec, packetization mode, clock rate, and transport; do not infer them from a file extension.
- Bound parsers, jitter buffers, frame sizes, metadata, and session lifetime.
- Keep credentials out of URLs, SDP, logs, packet captures, and example files.
- Model reconnect, keyframe recovery, clock discontinuity, packet loss, duplicate control requests, and device restart.
- Confirm claimed ONVIF conformance in ONVIF's registered-product database; implementing a WSDL or endpoint alone is not conformance.

## Example and verification policy

Examples in this section are documentation artefacts using synthetic addresses and identifiers. `V1` on this index means its links and terminology were reviewed manually. Protocol pages use `V2` where technical claims were checked against primary standards and a second official source. Environment-specific compatibility or conformance requires its own evidence record.

## Scope boundaries

This section does not replace licensed standards, an ONVIF conformance test, codec patent/licensing advice, radio or privacy regulation, safety engineering, or vendor deployment guidance. General HTTP and messaging transports are in [Web and messaging protocols](../web-and-messaging/README.md).
