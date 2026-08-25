---
title: "RTSP, RTP, RTCP, and SDP"
summary: "Developer reference for media session control, real-time transport, reception feedback, session description, version compatibility, and secure implementation."
page_type: protocol
domains: [video, intercom]
tags:
  - rtsp
  - rtp
  - rtcp
  - sdp
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "RFC 2326: RTSP 1.0 (obsolete but deployed)"
  - "RFC 7826: RTSP 2.0"
  - "RFC 3550 / STD 64: RTP and RTCP"
  - "RFC 8866: SDP"
coverage_limit: "Base IETF protocols and defensive parsing only; no vendor extension, authentication profile, camera, recorder, NAT, multicast, or stream interoperability is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# RTSP, RTP, RTCP, and SDP

[Video and media protocols](README.md) / RTSP, RTP, RTCP, and SDP

These protocols solve different problems:

- **RTSP** controls a media resource or session.
- **SDP** describes media, addresses, payload types, and codec parameters.
- **RTP** carries time-sensitive media packets.
- **RTCP** reports reception quality, identifies sources, and supports synchronization and session control.

None of them, by itself, establishes user authorization, reliable delivery, confidentiality, or a complete video-surveillance application.

## Revision and deployment status

| Protocol | Current base | Status and compatibility |
|---|---|---|
| RTSP 1.0 | RFC 2326 (1998) | Obsoleted by RFC 7826, but still prevalent in cameras and recorders |
| RTSP 2.0 | RFC 7826 (2016) | Standards Track; not backward compatible with 1.0 except for explicit version-negotiation behavior |
| RTP/RTCP | RFC 3550, STD 64 (2003) | Internet Standard base; payload formats and extensions are separate specifications |
| SDP | RFC 8866 (2021) | Standards Track revision that obsoletes RFC 4566; a description format, not a transport or negotiation protocol by itself |

RTSP 2.0 is not “RTSP 1.0 plus features.” A client must implement the selected version's message, connection, session, and request behavior rather than sending 1.0 assumptions with a `RTSP/2.0` version token. [RTSP1] [RTSP2]

## Typical on-demand session

```text
client                         media server
  |---- OPTIONS ------------------->|  discover methods/features
  |---- DESCRIBE ------------------>|  retrieve SDP
  |<--- 200 + application/sdp ------|
  |---- SETUP track 1 --------------|  negotiate RTP/RTCP transport
  |<--- 200 + Session/Transport -----|
  |---- SETUP track 2 --------------|
  |---- PLAY ----------------------->|
  |<==== RTP media / RTCP =========>|
  |---- PAUSE or TEARDOWN ---------->|
```

Common methods include `OPTIONS`, `DESCRIBE`, `SETUP`, `PLAY`, `PAUSE`, and `TEARDOWN`. Servers can implement additional methods and feature tags. Method support, aggregate versus per-track control, range units, seek behavior, and live-versus-recorded semantics must be discovered and documented.

## RTSP message and session rules

### Resource and control URLs

The presentation URL identifies the aggregate resource. SDP can provide per-media control attributes that resolve relative to the content base. Resolve URLs using the RTSP version's rules and reject cross-origin/cross-trust-boundary targets unless policy explicitly permits them.

### Request correlation and state

- RTSP 1.0 commonly correlates requests with `CSeq` and identifies established state with `Session`.
- Preserve the full session identifier but do not log sensitive parameters.
- A TCP connection and an RTSP session are not identical lifetimes.
- Model server timeout, keepalive behavior, reconnect, and restart; a stale session identifier is not recoverable state.
- Apply per-method retry rules. `OPTIONS` and `DESCRIBE` are easier to retry safely than `PLAY`, recording, parameter mutation, or vendor extensions.

### Transport negotiation

`SETUP` negotiates lower transport and delivery parameters. Common deployments use:

- RTP/RTCP over unicast UDP;
- RTP/RTCP over multicast UDP;
- RTP and RTCP interleaved over the RTSP TCP connection;
- protected variants where explicitly supported.

Do not assume the old adjacent UDP-port convention. Explicit RTCP ports, RTCP multiplexing, ICE, NAT traversal, and interleaving alter it. RFC 5761 defines RTP/RTCP multiplexing on one port. [RTCP-MUX]

## Safe RTSP transcript

**Target:** Synthetic RTSP 1.0 server at a documentation-only hostname.

**Inputs:** No credentials; no production address.

**Side effects:** None; this transcript is not a command script.

```http
DESCRIBE rtsp://camera.example/media/main RTSP/1.0
CSeq: 1
Accept: application/sdp
User-Agent: physical-security-dev-example/1.0

RTSP/1.0 200 OK
CSeq: 1
Content-Type: application/sdp
Content-Length: 214

...SDP body...
```

Implementations must read exactly the declared body length, enforce a configured maximum, handle partial reads, and keep RTSP parsing separate from interleaved binary-frame parsing.

## SDP anatomy

SDP is line-oriented. The single-letter field name and ordering rules matter. A session commonly contains:

```sdp
v=0
o=- 424242 2 IN IP4 192.0.2.10
s=Synthetic camera stream
t=0 0
a=control:*
m=video 0 RTP/AVP 96
c=IN IP4 192.0.2.10
a=rtpmap:96 H264/90000
a=fmtp:96 packetization-mode=1;profile-level-id=42e01f
a=control:trackID=1
```

**Target:** Parser/unit-fixture design.

**Inputs:** RFC 5737 documentation address.

**Side effects:** None.

Interpretation:

- `v=` is the SDP protocol version, currently `0`.
- `o=` identifies the origin and session version; it is not an authenticated identity.
- `t=` describes session time.
- `m=` starts a media description and maps a dynamic payload type (`96`) to attributes.
- `c=` supplies connection data.
- `a=rtpmap` maps payload type to encoding and RTP clock rate.
- `a=fmtp` carries codec-format parameters whose grammar is payload-format-specific.
- `a=control` is an RTSP convention and can be session- or media-level.

Reject malformed lines, conflicting duplicate singleton fields, impossible payload mappings, control URLs outside policy, and unbounded attribute values. SDP does not safely carry secret key material unless the enclosing channel is private, authenticated, and the specific key-management mechanism defines that use. RFC 8866 explicitly calls for care with sensitive session descriptions. [SDP]

## RTP data model

The fixed RTP header supplies:

| Field | Purpose | Common trap |
|---|---|---|
| Version | RTP version, normally 2 | Confusing unrelated UDP with RTP |
| Marker | Profile/payload-defined boundary hint | Assuming it always means “keyframe” |
| Payload type | Mapping to a codec format in signaling | Treating dynamic numbers as globally assigned |
| Sequence number | Packet order/loss detection, modulo 2^16 | Treating wraparound as reset |
| Timestamp | Sampling/encoding clock position | Treating it as wall-clock UTC |
| SSRC | Synchronization-source identifier | Treating it as durable device identity |
| CSRC list | Contributing sources | Ignoring bounds and count validation |
| Extension | Profile-negotiated extension data | Parsing an unnegotiated extension as trusted metadata |

RTP offers sequence and timing information but does not guarantee delivery, ordering, latency, or quality of service. Receivers need a bounded jitter buffer, codec-aware loss handling, sequence wrap/restart logic, SSRC collision handling, and resource limits. [RTP]

## RTCP behavior

RTCP typically carries:

- Sender Reports (SR): sender counters plus RTP-to-NTP clock correlation;
- Receiver Reports (RR): loss, highest sequence, jitter, and timing feedback;
- Source Description (SDES), including canonical-name data;
- BYE: source departure;
- profile-specific feedback and extensions defined elsewhere.

RTCP statistics are measurements, not proof of delivery or user experience. Validate report blocks and counts, cap compound-packet processing, and regard CNAME or SDES text as untrusted. Avoid exposing personally identifying host/user information in CNAME construction.

## Timing and synchronization

- Each RTP stream has its own codec clock rate.
- Sequence numbers establish packet ordering; timestamps establish sampling time.
- RTCP SR pairs an RTP timestamp with an NTP-format reference to align streams.
- Wall-clock changes, unsynchronized devices, reboot, source switching, timestamp wrap, and capture-pipeline discontinuity must be handled.
- Audio and video sync should use the negotiated timing model, not packet-arrival time.

## Security and privacy

- Use RTSP over TLS or another explicitly protected control path where supported; authenticate the server and authorize each media resource.
- Keep passwords and bearer tokens out of RTSP URLs. URI user-info leaks through logs, telemetry, history, and diagnostics.
- Plain RTP/RTCP provides no confidentiality, integrity, or replay protection; use SRTP/SRTCP or an equivalently protected transport where required.
- Constrain multicast by network design. A joinable multicast group is not an authorization boundary.
- Validate SDP-derived addresses and ports to prevent SSRF, traffic reflection, or egress-policy bypass.
- Rate-limit session creation and cap concurrent sessions, tracks, UDP flows, interleaved channels, body sizes, and parser memory.
- Redact session IDs, authorization data, URLs containing tokens, private addresses, and SDP fields that reveal topology.

## Implementation checklist

- [ ] RTSP 1.0 and 2.0 support represented as separate capabilities
- [ ] TLS, server identity, authentication, and per-resource authorization specified
- [ ] URL resolution and cross-host redirects/control targets constrained
- [ ] `Content-Length`, header count/length, interleaved-frame length, and SDP size bounded
- [ ] Partial I/O, pipelining/version behavior, timeout, and reconnect modeled
- [ ] Per-track and aggregate-control behaviour validated against target versions
- [ ] RTP payload type and `fmtp` parsed only after negotiation
- [ ] Sequence, timestamp, and SSRC wrap/restart/collision handled
- [ ] Jitter, loss, reordering, MTU, and keyframe recovery bounded
- [ ] RTCP reports consumed as telemetry, not delivery guarantees
- [ ] Plain-media risks and multicast scope explicitly accepted or removed

## Environment validation

Validate parser limits, authentication, vendor extensions, camera/recorder interoperability, NAT and multicast behaviour, loss/reordering, codec recovery, reconnect, clock discontinuity, and resource cleanup against exact target versions. Treat vendor documentation and captured acceptance evidence as implementation-specific supplements to the RFC baseline.

## Sources

- **RTSP1** — [RFC 2326: Real Time Streaming Protocol (RTSP)][RTSP1], IETF, April 1998; obsoleted by RFC 7826.
- **RTSP2** — [RFC 7826: Real-Time Streaming Protocol Version 2.0][RTSP2], IETF, December 2016.
- **RTP** — [RFC 3550 / STD 64: RTP: A Transport Protocol for Real-Time Applications][RTP], IETF, July 2003.
- **SDP** — [RFC 8866: SDP: Session Description Protocol][SDP], IETF, January 2021.
- **RTCP-MUX** — [RFC 5761: Multiplexing RTP Data and Control Packets on a Single Port][RTCP-MUX], IETF, April 2010.

[RTSP1]: https://datatracker.ietf.org/doc/rfc2326/
[RTSP2]: https://datatracker.ietf.org/doc/rfc7826/
[RTP]: https://datatracker.ietf.org/doc/rfc3550/
[SDP]: https://datatracker.ietf.org/doc/rfc8866/
[RTCP-MUX]: https://datatracker.ietf.org/doc/rfc5761/
