---
title: "WebRTC for physical-security media"
summary: "Developer reference for WebRTC signaling boundaries, ICE/STUN/TURN, DTLS-SRTP, media and data channels, browser APIs, security, and operations."
page_type: protocol
domains: [video, intercom]
tags:
  - webrtc
  - ice
  - turn
  - dtls-srtp
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "RFC 8825: Overview: Real-Time Protocols for Browser-Based Applications"
  - "RFC 8827: WebRTC Security Architecture"
  - "RFC 8835: Transports for WebRTC"
  - "W3C WebRTC Recommendation, 13 March 2025"
coverage_limit: "Protocol and browser-API architecture only; no browser, TURN, SFU, codec, gateway, firewall, NAT, media session, or compatibility matrix is validated."
languages: [JavaScript]
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# WebRTC for physical-security media

[Video and media protocols](README.md) / WebRTC

WebRTC is a suite of real-time media and data protocols plus APIs. In a physical-security system it can deliver low-latency live video, audio, intercom, and constrained data to browsers or native clients. It deliberately does **not** standardize the application's signaling transport or authorization model. [WEBRTC-OVERVIEW] [W3C-WEBRTC]

## Standards snapshot

| Layer | Base reference | Role |
|---|---|---|
| Architecture | RFC 8825 | Overall browser real-time protocol model |
| Security | RFC 8827 | Threat model and security architecture |
| Transports | RFC 8835 | ICE, TURN, DTLS-SRTP, SRTP/SRTCP, and data-channel transports |
| Browser API | W3C WebRTC Recommendation, 2025-03-13 | `RTCPeerConnection`, media/data APIs, state, statistics, and privacy behavior |
| ICE | RFC 8445 | Candidate gathering, connectivity checks, nomination, and consent |
| TURN | RFC 8656 | Relayed connectivity when direct paths fail or policy requires a relay |
| DTLS-SRTP | RFC 5764 | Derivation of SRTP/SRTCP keying material from DTLS |
| WebRTC media | RFC 8834 | RTP use, multiplexing, feedback, and media behavior |

The standards continue to be extended, but these are the stable protocol bases used by the current W3C API. [WEBRTC-TRANSPORT] [ICE] [TURN]

## Connection model

```text
browser/native client       application signaling       media endpoint/SFU
        |---- authenticated offer SDP ------------------------>|
        |<--- authenticated answer SDP ------------------------|
        |<==== ICE candidates via signaling ==================>|
        |...... STUN/TURN gathering and ICE checks ............|
        |<===== DTLS handshake; fingerprint bound via SDP =====>|
        |<===== SRTP/SRTCP media; SCTP/DTLS data channels =====>|
```

The signaling channel transports offers, answers, and ICE candidates, but its shape—HTTP, WebSocket, SIP, vendor API, or other mechanism—is application-defined. Signaling must authenticate both the user and the target resource, authorize requested media/direction, prevent cross-session substitution, and protect SDP fingerprints and candidates from tampering.

## ICE, STUN, and TURN

### Candidate types

- **Host:** local interface address.
- **Server-reflexive:** public mapping learned through STUN.
- **Peer-reflexive:** mapping discovered during checks.
- **Relayed:** address allocated by TURN.

Full ICE agents gather candidates, form candidate pairs, run authenticated connectivity checks, select a valid pair, and maintain consent. A reachable UDP port is not proof that the intended peer owns it. ICE credentials are short-lived session values, not application identity.

### Deployment policy

- Use authenticated, time-limited TURN credentials; do not embed a permanent shared secret in browser code.
- Bound allocations, bandwidth, lifetime, peer destinations, and protocols.
- Decide whether direct candidates are allowed. TURN-only policy can reduce topology disclosure and simplify egress at the cost of relay capacity and latency.
- Treat ICE candidates as sensitive network metadata and redact them from routine telemetry.
- Support both IPv4 and IPv6 deliberately; avoid policy gaps where only one family is filtered.
- Observe consent freshness and close media when consent or application authorization ends.

## SDP offer/answer and negotiation

WebRTC uses SDP offer/answer but imposes a WebRTC-specific profile. Applications should:

- serialize offer/answer changes and handle glare using a documented negotiation pattern;
- validate media kinds, directions (`sendrecv`, `sendonly`, `recvonly`, `inactive`), codecs, header extensions, payload types, fingerprints, and ICE credentials;
- reject unexpected data channels or media sections;
- cap SDP/candidate size and count;
- avoid rewriting security-critical SDP unless the intermediary is an intentional trusted endpoint;
- track transceivers and media identifiers rather than relying on array position.

## Media and data protection

WebRTC media is protected with SRTP/SRTCP; DTLS-SRTP derives keys after the DTLS peer presents a certificate whose fingerprint is carried in the authenticated signaling exchange. Data channels use SCTP over DTLS. This gives transport protection, but the application still owns user identity, endpoint authorization, recording notice, retention, and access revocation. [WEBRTC-SEC] [DTLS-SRTP]

Do not infer that “encrypted WebRTC” means end-to-end encryption across an SFU, gateway, or cloud media service. A component that terminates DTLS-SRTP can normally access media. If end-to-end media protection is required through an intermediary, specify and verify a separate E2EE design, key lifecycle, participant identity, recording policy, and recovery model.

## Safe browser configuration shape

**Target:** Browser `RTCPeerConnection` construction only.

**Inputs:** Documentation-only TURN hostname and placeholder ephemeral credential.

**Side effects:** Construction is local; a real browser may contact configured ICE services only after subsequent gathering operations, which are not shown.

```javascript
const peer = new RTCPeerConnection({
  iceTransportPolicy: "relay",
  iceServers: [
    {
      urls: ["turns:turn.example:5349?transport=tcp"],
      username: "ephemeral-user",
      credential: "replace-with-short-lived-secret"
    }
  ],
  bundlePolicy: "max-bundle"
});
```

Never ship the placeholder or a long-lived TURN secret. Obtain scoped credentials from an authenticated application service immediately before session establishment.

## Physical-security integration patterns

### Camera or gateway to browser

An edge gateway commonly terminates RTSP/RTP from a camera and originates WebRTC. Document whether it transcodes or repacketizes, how it authenticates cameras, its failure behavior, and whether users can reach only authorized streams. Codec compatibility determines whether “no-transcode” operation is possible.

### Intercom

Negotiate audio direction explicitly, gate microphone capture behind user intent and browser permission, process echo cancellation carefully, and authorize door/relay actions outside the media channel. Never treat a spoken phrase, DTMF tone, or data-channel message as sufficient authorization for a high-impact action.

### Cloud uplink

ONVIF Profile V was a release candidate on the verification date and includes WebRTC-related cloud uplink behavior. It must be represented as release-candidate support, not final ONVIF conformance. [ONVIF-V]

## Operational telemetry

Useful `getStats()` dimensions include selected candidate pair, bitrate, packets/bytes, loss, jitter, round-trip time, frames encoded/decoded/dropped, keyframes, resolution, jitter-buffer delay, and quality-limitation reason. Treat statistics as untrusted remote-influenced telemetry and control cardinality. Do not log raw SDP, ICE passwords, TURN credentials, private candidates, or persistent device identifiers.

## Failure states to design

- Signaling authenticated but target stream no longer authorized
- ICE gathering slow, UDP blocked, TURN unavailable, or relay quota exhausted
- DTLS fingerprint mismatch or certificate rotation during reconnect
- Browser backgrounding, permission revocation, device change, or page lifecycle change
- Codec negotiated but unsupported by gateway hardware path
- Packet loss requiring picture-loss indication or a fresh keyframe
- ICE restart after network handover
- SFU/gateway restart and stale application session
- User revocation during an established peer connection

## Security checklist

- [ ] Signaling uses HTTPS/WSS, authenticated sessions, CSRF/origin defenses as applicable, and per-stream authorization
- [ ] SDP fingerprint and ICE credentials integrity-protected end to end across signaling
- [ ] TURN credentials short-lived, scoped, rate-limited, and never committed to client code
- [ ] Direct-versus-relay candidate policy intentional
- [ ] Candidate, SDP, track, transceiver, data-channel, and message sizes bounded
- [ ] Media directions and microphone/camera permission match user intent
- [ ] Authorization rechecked on reconnect, ICE restart, and long session renewal
- [ ] SFU/gateway media visibility and recording policy documented
- [ ] Stats and signaling logs redacted
- [ ] Door, relay, PTZ, and other control actions use a separately authorized API

## Environment validation

Validate browser compatibility, permission and privacy behaviour, TURN/SFU quota and failure modes, camera-gateway and codec negotiation, firewall/NAT paths, network handover, revocation, reconnect, and long-session renewal against the supported target versions.

## Sources

- **WEBRTC-OVERVIEW** — [RFC 8825: Overview: Real-Time Protocols for Browser-Based Applications][WEBRTC-OVERVIEW], IETF, January 2021.
- **WEBRTC-SEC** — [RFC 8827: WebRTC Security Architecture][WEBRTC-SEC], IETF, January 2021.
- **WEBRTC-TRANSPORT** — [RFC 8835: Transports for WebRTC][WEBRTC-TRANSPORT], IETF, January 2021.
- **WEBRTC-MEDIA** — [RFC 8834: Media Transport and Use of RTP in WebRTC][WEBRTC-MEDIA], IETF, January 2021.
- **W3C-WEBRTC** — [WebRTC: Real-Time Communication in Browsers][W3C-WEBRTC], W3C Recommendation, 13 March 2025.
- **ICE** — [RFC 8445: Interactive Connectivity Establishment (ICE)][ICE], IETF, July 2018.
- **TURN** — [RFC 8656: Traversal Using Relays around NAT (TURN)][TURN], IETF, February 2020.
- **DTLS-SRTP** — [RFC 5764: DTLS Extension to Establish Keys for SRTP][DTLS-SRTP], IETF, May 2010.
- **ONVIF-V** — [Profile V][ONVIF-V], ONVIF, release candidate dated 2026-07-09.

[WEBRTC-OVERVIEW]: https://datatracker.ietf.org/doc/rfc8825/
[WEBRTC-SEC]: https://datatracker.ietf.org/doc/rfc8827/
[WEBRTC-TRANSPORT]: https://datatracker.ietf.org/doc/rfc8835/
[WEBRTC-MEDIA]: https://datatracker.ietf.org/doc/rfc8834/
[W3C-WEBRTC]: https://www.w3.org/TR/webrtc/
[ICE]: https://datatracker.ietf.org/doc/rfc8445/
[TURN]: https://datatracker.ietf.org/doc/rfc8656/
[DTLS-SRTP]: https://datatracker.ietf.org/doc/rfc5764/
[ONVIF-V]: https://www.onvif.org/profiles/profile-v/
