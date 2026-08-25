---
title: "ONVIF discovery and media-flow reasoning"
summary: "A passive design exercise mapping ONVIF discovery, services, authentication, media, events, and profiles."
page_type: lab
domains:
  - video
tags:
  - onvif
  - discovery
  - media
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "ONVIF Network Interface Specifications 26.06"
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# ONVIF discovery and media-flow reasoning

[Home](../README.md) / [Defensive labs](README.md) / ONVIF flow reasoning

Lab class: **Offline specification and synthetic trace**

## Objectives

- Separate WS-Discovery from device/service operations.
- Map SOAP service endpoints, authentication and profile-dependent features.
- Follow media configuration to RTSP/RTP transport.
- Follow event subscription/delivery and optional MQTT handling.
- Tie conformance to exact product and firmware, not a generic ONVIF label.

## Procedure

1. Select an invented device/client combination and record the exact ONVIF 26.06 namespaces plus an example conformance-listing structure.
2. Draw discovery scope, multicast/broadcast boundary and post-commissioning need.
3. List service endpoints and whether HTTPS identity is validated.
4. Select one read-only capability/media-profile exchange and document synthetic request/response namespaces and bounds without sending it.
5. Map the returned media URI to RTSP control, RTP/RTCP transport, codec/payload and credential exposure risk.
6. Map an event subscription's lease, filters, delivery, renewal, gaps and authentication.
7. Compare every observed feature with the exact profile requirements and conditional/optional status.
8. Record unsupported, vendor-specific and ambiguous behavior separately.

## Safety boundaries

Scope is limited to specification review and synthetic response fragments. Network discovery, device contact, configuration, PTZ, I/O, media retrieval, and product acceptance belong to the separately authorized commissioning process.

## Evidence checklist

- [ ] ONVIF specification release, profile status, namespaces, and synthetic product roles pinned
- [ ] Discovery and post-discovery trust boundaries separated
- [ ] Media URI, RTSP, RTP/RTCP, codec, and credential-exposure path mapped
- [ ] Subscription lease, renewal, duplicate, gap, and authentication behaviour documented
- [ ] Conformance listing, implementation support, interoperability, and site acceptance treated as separate evidence

## Sources

- [ONVIF specifications](https://www.onvif.org/profiles/specifications/), accessed 2026-08-25.
- [ONVIF conformant products](https://www.onvif.org/conformant-products/), accessed 2026-08-25.

## Related pages

- [ONVIF](../02-protocols/video-and-media/onvif.md)
- [RTSP/RTP/SDP trace analysis](rtsp-rtp-sdp-trace-analysis.md)
