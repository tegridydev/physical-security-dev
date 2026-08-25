---
title: "RTSP, RTP, RTCP, and SDP trace analysis"
summary: "Offline interpretation of synthetic session control, description, media, timing, and loss evidence."
page_type: lab
domains:
  - video
tags:
  - rtsp
  - rtp
  - sdp
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "RFC 7826"
  - "RFC 8866"
  - "RFC 2326"
  - "RFC 3550"
  - "RFC 4566"
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# RTSP, RTP, RTCP, and SDP trace analysis

[Home](../README.md) / [Defensive labs](README.md) / RTSP/RTP/SDP analysis

Lab class: **Offline synthetic trace**

RFC 7826 and RFC 8866 are the current RTSP 2.0 and SDP bases. RFC 2326 (RTSP 1.0) and RFC 4566 (older SDP) remain useful only when a captured or synthetic fixture explicitly uses those installed legacy versions.

## Procedure

1. Identify RTSP version; do not assume RTSP 1.0 and 2.0 are interchangeable.
2. Follow request/response pairs using CSeq and session identifiers; record authentication and URI exposure.
3. Parse SDP media, connection, payload type, rtpmap/fmtp, control URI, direction and timing fields.
4. Determine RTP over UDP, multicast, TCP interleaving or another negotiated path.
5. Track one SSRC's sequence and timestamp space; distinguish packet loss, reordering, duplication and capture loss.
6. Use RTCP sender/receiver reports to interpret timing and reported loss without treating them as authenticated truth in an unprotected session.
7. Map payload format to codec/framing and confirm receiver limits.
8. Identify whether control and media have confidentiality/integrity, and where credentials/tokens appear.

## Expected artifacts

- session-flow diagram;
- SDP field table and resolved control/media endpoints;
- transport and port/multicast map;
- sequence/loss/reordering note;
- authentication/encryption boundary;
- explicit capture and version limitations.

## Evidence checklist

- [ ] Fixture provenance, digest, protocol versions, and codec mapping recorded
- [ ] RTSP 1.0 and 2.0 semantics not mixed
- [ ] SDP version and resolved control/media endpoints recorded
- [ ] Capture gaps distinguished from protocol loss and reordering
- [ ] Authentication, confidentiality, integrity, and interpretation limits documented

## Sources

- [RFC 7826 RTSP 2.0](https://www.rfc-editor.org/rfc/rfc7826), current RTSP base, accessed 2026-08-25.
- [RFC 8866 SDP](https://www.rfc-editor.org/rfc/rfc8866), current SDP base, accessed 2026-08-25.
- [RFC 2326 RTSP 1.0](https://www.rfc-editor.org/rfc/rfc2326), accessed 2026-08-25.
- [RFC 3550 RTP](https://www.rfc-editor.org/rfc/rfc3550), accessed 2026-08-25.
- [RFC 4566 SDP](https://www.rfc-editor.org/rfc/rfc4566), obsolete legacy baseline, accessed 2026-08-25.

## Related pages

- [RTSP/RTP/RTCP/SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md)
- [Offline RTSP/SDP example](../05-development-and-integration/examples/rtsp-sdp-inspection-python.md)
