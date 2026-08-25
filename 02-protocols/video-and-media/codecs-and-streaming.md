---
title: "Codecs, RTP payloads, and streaming design"
summary: "Developer reference for video/audio codec identification, RTP packetization, keyframes, rate control, loss recovery, latency, HLS and MPEG-DASH streaming, and compatibility."
page_type: protocol
domains: [video, intercom]
tags:
  - h264
  - h265
  - av1
  - opus
  - aac
  - streaming
  - mpeg-dash
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "RFC 6184: H.264 RTP payload"
  - "RFC 7798: H.265 RTP payload"
  - "RFC 9364: AV1 RTP payload"
  - "RFC 7587: Opus RTP payload"
  - "RFC 8216: HTTP Live Streaming"
  - "ISO/IEC 23009-1:2026: MPEG-DASH media presentation description and segment formats, sixth edition"
coverage_limit: "Codec, RTP payload, and streaming design only; product interoperability, encoder/decoder behavior, browser support, camera/recorder performance, licensing, and patent position require separate evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Codecs, RTP payloads, and streaming design

[Video and media protocols](README.md) / Codecs and streaming

A **codec** compresses media. A **payload format** maps codec units into RTP. A **container** stores or segments tracks. A **session/control protocol** describes or controls delivery. A **transport** moves bytes. Supporting H.264, for example, does not imply support for every H.264 profile/level, RTP packetization mode, container, transport, resolution, or bitrate.

## Common physical-security media formats

| Format | Typical use | Developer notes |
|---|---|---|
| H.264/AVC | Broad camera, recorder, browser/gateway compatibility | RTP payload is RFC 6184; negotiate profile-level and packetization mode |
| H.265/HEVC | Higher compression efficiency in modern cameras/recorders | RTP payload is RFC 7798; browser support is not universal; record VPS/SPS/PPS and decoder constraints |
| AV1 | Emerging browser/cloud and software media paths | RTP payload is RFC 9364; check encoder cost, hardware availability, latency, and decoder limits |
| Motion JPEG / JPEG | Simple independent images, snapshots, some low-frame-rate streams | RTP JPEG is RFC 2435; high bandwidth for continuous video but easy frame recovery |
| Opus | Interactive voice/intercom and WebRTC | RTP payload is RFC 7587; flexible rates, packet durations, FEC/DTX behavior |
| AAC | Recorded/streamed audio and MP4-family containers | Generic MPEG-4 RTP payload is RFC 3640; object type and configuration must match |
| G.711 | Legacy telephony/intercom | Static RTP payload types exist for common clock/channel forms; high bitrate but simple and low compute |

Codec licensing and patent obligations are jurisdiction-, use-, distribution-, and implementation-dependent. This page is not legal advice.

## ONVIF and WebRTC compatibility

ONVIF Profile T covers advanced video and includes H.264 and H.265 capabilities. ONVIF Profile V was still a release candidate on 2026-08-25 and requires H.264 for its WebRTC-oriented video capability. These statements do not mean every Profile T product exposes every encoder combination or that every browser decodes H.265. Query device and client capabilities and negotiate an intersection. [ONVIF-T] [ONVIF-V]

WebRTC's protocol profile and codec requirements are defined across RFCs 8834, 7742, and 7874. Browser implementations evolve, so a deployment must verify the exact client matrix rather than infer support from the WebRTC label. [WEBRTC-MEDIA] [WEBRTC-VIDEO] [WEBRTC-AUDIO]

## H.264 payload essentials

H.264 video is composed of Network Abstraction Layer (NAL) units. RFC 6184 defines transport forms including single NAL units, aggregation packets, and fragmentation units. Practical considerations:

- negotiate `packetization-mode`; mode 0 and mode 1 have different packetization capabilities;
- treat `profile-level-id` as a constraint, not decorative metadata;
- obtain and refresh sequence/picture parameter sets (SPS/PPS) according to the negotiated mechanism;
- request or wait for an independently decodable picture after join, loss, or decoder reset;
- do not assume RTP marker means “this packet is a keyframe”; its meaning is payload-format-specific and related to access-unit boundaries;
- bound reconstructed NAL and access-unit size before allocation.

## H.265 payload essentials

HEVC adds Video Parameter Sets (VPS) and different NAL/aggregation/fragmentation rules. RFC 7798 also supports temporal scalability concepts. Record the exact profile, tier, level, bit depth, chroma format, VPS/SPS/PPS strategy, and decoder maximums. A gateway that merely forwards RTP still needs to validate packetization and size; a transcoder must also handle codec state and timestamps safely. [H265-RTP]

## Audio payload essentials

Opus uses a 48 kHz RTP timestamp clock even when internal audio bandwidth differs. Packet duration, in-band FEC, discontinuous transmission, stereo/channel mapping, and maximum playback rate affect intercom quality and latency. [OPUS-RTP]

AAC/RTP has multiple modes and configuration data. Do not derive decoder setup from the codec name alone. For telephony codecs, distinguish sample rate, RTP clock rate, channels, packetization interval, and DTMF transport.

## Keyframes and group-of-pictures design

Longer GOPs reduce bitrate but increase random-access and recovery delay. Shorter GOPs increase bitrate/storage and encoder work but improve join, seek, failover, and loss recovery. Document:

- keyframe/IDR or random-access interval;
- whether scene-change keyframes are enabled;
- B-frame/reordering depth and decoder delay;
- what feedback requests a recovery picture;
- rate limit for picture-loss/full-intra requests;
- recorder segment boundaries and whether each segment begins with a usable random-access point.

Do not let unauthenticated or unbounded keyframe requests amplify encoder load or bandwidth.

## Bitrate and rate control

| Mode | Useful property | Risk to model |
|---|---|---|
| Constant bitrate target | Predictable network/storage planning | Quality varies; short-term bursts can still exceed target |
| Variable bitrate | Better quality/efficiency allocation by scene | Peaks can overflow constrained links or buffers |
| Constrained VBR | Balances average efficiency and peak budget | Vendor definitions and enforcement differ |

Plan using measured peak bitrate, audio, RTP/transport/container overhead, retransmission/FEC, metadata, TLS/QUIC overhead, concurrency, and failover—not the configured average video number alone.

## RTP packetization, MTU, and loss

- Keep packet size below the effective path MTU after IP, UDP, RTP, SRTP, and tunnel overhead.
- Avoid IP fragmentation; loss of one fragment discards the complete IP packet.
- One lost fragmented-NAL packet can invalidate a large access unit.
- Reordering and jitter buffers must be bounded by time and memory.
- Retransmission, forward error correction, and feedback are profile-negotiated; do not assume they exist.
- Apply decoder and parser limits before reassembly and decompression.
- Treat codec dimensions, cropping, stride, color format, and frame rate as untrusted until checked against resource limits.

## Streaming families

| Family | Latency shape | Strengths | Costs |
|---|---|---|---|
| RTSP/RTP | Low to moderate | Direct camera/recorder control; multicast possible | NAT/firewall complexity; security varies; broad legacy behavior |
| WebRTC | Low | Encrypted interactive media, NAT traversal, feedback, browser API | Signaling/SFU/TURN operations and codec intersection |
| HLS | Segment-oriented; conventional deployments add multiple seconds, though low-latency extensions can reduce it | HTTP/CDN/cache friendliness, adaptive variants | Segment/playlist delay, authorization and cache controls |
| MPEG-DASH | Segment-oriented; latency depends on segment/chunk/profile and player behavior | Standards-based adaptive presentations, multiple representations, HTTP/CDN distribution | MPD/segment complexity, client/profile intersection, authorization and cache controls |
| File/export | Not live | Evidence integrity, deterministic review, offline transfer | Export format, signing, provenance, and player compatibility |

RFC 8216 defines the published IETF HLS base. Apple continues work on a second-edition Internet-Draft; an Internet-Draft must not be represented as a final RFC. Pin the exact HLS feature set used by a product. [HLS] [HLS-BIS]

## HLS implementation contract

- Authenticate both playlists and segments; use short-lived, scoped URLs where appropriate.
- Prevent cache sharing across tenants/users by setting correct cache keys and response controls.
- Validate every URI obtained from a playlist before server-side retrieval.
- Bound playlist size, variant count, segment duration, discontinuities, and live-window history.
- Define behavior for key rotation, expired authorization, sequence wrap, discontinuity, missing segment, and clock shift.
- Do not place long-lived secrets in playlist URLs or logs.
- Treat encryption-key delivery and DRM as separate security designs; TLS alone protects only in transit to its endpoint.

## MPEG-DASH implementation contract

ISO/IEC 23009-1:2026 is the sixth edition of MPEG-DASH Part 1, covering the Media Presentation Description (MPD) and segment formats. An MPD can organize a presentation into periods, adaptation sets, representations, initialization information, and media segments. It can describe multiple codecs, bitrates, languages, resolutions, roles, timelines, and URL derivation rules; it does not guarantee that a particular player supports the resulting profile or media combination. [MPEG-DASH]

Pin the applicable DASH profile and the exact interpretation of:

- static versus dynamic MPD behavior and its update cadence;
- Period, AdaptationSet, Representation, and dependency relationships;
- `BaseURL`, `SegmentTemplate`, `SegmentTimeline`, `SegmentList`, and `SegmentBase` use;
- initialization segments, indexes, media segment numbering/time, discontinuities, and end-of-presentation behavior;
- `UTCTiming`, availability windows, suggested delay, clock source, and uncertainty for live content;
- codec strings, MIME types, dimensions, frame/audio rates, bandwidth declarations, and decoder limits;
- EventStream/InbandEventStream or other timed metadata used by the application;
- ContentProtection descriptors and the separately selected key/licence system.

### Manifest and segment security

An authorized MPD response does not authorize every URL that it references. Apply authorization to the MPD, initialization segments, indexes, media segments, keys/licences, timed metadata, thumbnails, and alternate representations. Bind entitlement to tenant, user/workload, camera/resource, purpose, time window, and representation policy.

- Resolve `BaseURL` and every enabled external reference under an approved scheme/host/path allowlist.
- For server-side retrieval, revalidate DNS results and every permitted redirect; reject loopback, link-local, metadata-service, management, and unexpected private-network destinations.
- Cap MPD bytes, XML depth, Period/AdaptationSet/Representation counts, timeline entries, URL length/expansion, segment duration/count, and update rate before allocation or fan-out.
- Use secure XML processing with external entity resolution disabled and no implicit network retrieval.
- Prevent one tenant's MPD or segment from satisfying another tenant's cache request. Include authenticated resource/tenant/entitlement dimensions in cache design or use correctly scoped unguessable URLs with bounded lifetime.
- Keep bearer tokens, signatures, licence challenges, device identifiers, and personal data out of cache keys, analytics URLs, referrers, and ordinary logs where possible.
- Define behavior when MPD authorization remains valid but a segment or licence expires, and when revoked viewers retain cached bytes.

`ContentProtection` and DRM descriptors signal protection-system information; they are not proof that media is encrypted correctly, that a licence was issued to the intended principal, or that screen/output controls meet policy. Review media encryption, key derivation/rotation, licence authorization, client robustness, offline use, revocation, and failure behavior as a separate design.

### HLS, DASH, and shared media

HLS and DASH can reuse related fragmented-MP4/CMAF media assets in some deployments, but shared segments do not make playlist and MPD semantics interchangeable. Authentication, sequence/timeline interpretation, codec/profile signaling, low-latency behavior, encryption metadata, and player feature support remain manifest-family specific.

For recordings or evidence derived from adaptive streaming, preserve the exact manifest snapshot and response metadata, selected representation, initialization and media segment identities/hashes, gaps and discontinuities, clock evidence, decryption/licence context where policy permits, and every remux/transcode transformation. A mutable live MPD or CDN cache is not a chain-of-custody record.

## Metadata, privacy, and evidence

Video/audio can contain faces, voices, locations, access events, and behavioral data. Codec metadata may reveal device models, timestamps, encoder configuration, or topology. Define minimization, retention, export authorization, watermark/signature verification, chain of custody, and redaction independently of stream delivery.

For evidentiary export, preserve original bytes where policy requires, record hashes and provenance, use a documented time source, and retain the decoder/player requirements. Transcoding changes the bitstream and can remove metadata; record that transformation explicitly.

## Safe negotiation fixture

The following synthetic SDP fragment is suitable as an offline parser/negotiation fixture. It contains no endpoint or credential:

```sdp
m=video 0 RTP/AVP 96 97
a=rtpmap:96 H264/90000
a=fmtp:96 packetization-mode=1;profile-level-id=42e01f
a=rtpmap:97 JPEG/90000
a=sendonly
```

A parser must not choose the first payload blindly. Intersect the offered payload, direction, format parameters, decoder limits, security profile, and application policy.

## Engineering checklist

- [ ] Codec, profile/tier/level, bit depth, chroma, resolution, frame rate, and payload format explicit
- [ ] Parameter-set/configuration delivery and changes handled
- [ ] Keyframe interval and post-loss/join recovery measured in the target environment
- [ ] Peak bitrate, overhead, concurrency, and failover capacity budgeted
- [ ] MTU, fragmentation, reordering, jitter, feedback, and packet-loss behavior bounded
- [ ] Decoder dimensions, allocation, CPU/GPU, queue depth, and decompression limits enforced
- [ ] Client/browser/hardware codec matrix verified for the supported deployment baseline
- [ ] Transcoding latency, quality loss, failure, and trust boundary documented
- [ ] HLS playlist or DASH MPD profile, limits, URL resolution, authorization, and update behavior explicit where used
- [ ] Manifest, initialization, segment, key/licence, CDN cache, redirect, SSRF, and tenant boundaries reviewed
- [ ] Privacy, retention, evidence export, and redaction requirements mapped

## Sources

- **H264-RTP** — [RFC 6184: RTP Payload Format for H.264 Video][H264-RTP], IETF, May 2011.
- **H265-RTP** — [RFC 7798: RTP Payload Format for High Efficiency Video Coding][H265-RTP], IETF, March 2016.
- **AV1-RTP** — [RFC 9364: RTP Payload Format for AV1][AV1-RTP], IETF, March 2023.
- **JPEG-RTP** — [RFC 2435: RTP Payload Format for JPEG-compressed Video][JPEG-RTP], IETF, October 1998.
- **OPUS-RTP** — [RFC 7587: RTP Payload Format for the Opus Codec][OPUS-RTP], IETF, June 2015.
- **MPEG4-RTP** — [RFC 3640: RTP Payload Format for Transport of MPEG-4 Elementary Streams][MPEG4-RTP], IETF, November 2003.
- **WEBRTC-MEDIA** — [RFC 8834: Media Transport and Use of RTP in WebRTC][WEBRTC-MEDIA], IETF, January 2021.
- **WEBRTC-VIDEO** — [RFC 7742: WebRTC Video Processing and Codec Requirements][WEBRTC-VIDEO], IETF, March 2016.
- **WEBRTC-AUDIO** — [RFC 7874: WebRTC Audio Codec and Processing Requirements][WEBRTC-AUDIO], IETF, May 2016.
- **HLS** — [RFC 8216: HTTP Live Streaming][HLS], IETF, August 2017.
- **HLS-BIS** — [HTTP Live Streaming 2nd Edition Internet-Draft][HLS-BIS], IETF Datatracker, work in progress, accessed 2026-08-25.
- **MPEG-DASH** — [ISO/IEC 23009-1:2026, sixth edition][MPEG-DASH], ISO/IEC, Dynamic adaptive streaming over HTTP (DASH) — Part 1: Media presentation description and segment formats.
- **ONVIF-T** — [Profile T][ONVIF-T], ONVIF, accessed 2026-08-25.
- **ONVIF-V** — [Profile V][ONVIF-V], ONVIF, release candidate dated 2026-07-09.

[H264-RTP]: https://datatracker.ietf.org/doc/rfc6184/
[H265-RTP]: https://datatracker.ietf.org/doc/rfc7798/
[AV1-RTP]: https://datatracker.ietf.org/doc/rfc9364/
[JPEG-RTP]: https://datatracker.ietf.org/doc/rfc2435/
[OPUS-RTP]: https://datatracker.ietf.org/doc/rfc7587/
[MPEG4-RTP]: https://datatracker.ietf.org/doc/rfc3640/
[WEBRTC-MEDIA]: https://datatracker.ietf.org/doc/rfc8834/
[WEBRTC-VIDEO]: https://datatracker.ietf.org/doc/rfc7742/
[WEBRTC-AUDIO]: https://datatracker.ietf.org/doc/rfc7874/
[HLS]: https://datatracker.ietf.org/doc/rfc8216/
[HLS-BIS]: https://datatracker.ietf.org/doc/draft-pantos-hls-rfc8216bis/
[MPEG-DASH]: https://www.iso.org/standard/23009-1
[ONVIF-T]: https://www.onvif.org/profiles/profile-t/
[ONVIF-V]: https://www.onvif.org/profiles/profile-v/
