---
title: SRT and RIST contribution streaming
summary: SRT and RIST recovery, latency, profiles, identity, encryption, failover, observability, and safe physical-security contribution-stream integration.
page_type: protocol
domains: [video, intercom]
tags: [srt, rist, contribution-streaming, udp, arq, media-transport]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "VSF TR-06-1:2020: RIST Simple Profile"
  - "VSF TR-06-2:2024: RIST Main Profile"
  - "VSF TR-06-3:2024: RIST Advanced Profile"
coverage_limit: Contribution-transport architecture and public specifications only; product feature subsets, interoperability, codecs/containers, performance, network behavior, cryptographic configuration, and evidentiary suitability require system-specific evidence.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# SRT and RIST contribution streaming

[Home](../../README.md) / [Protocols](../README.md) / [Video and media](README.md) / SRT and RIST contribution streaming

Secure Reliable Transport (SRT) and Reliable Internet Stream Transport (RIST) are UDP-based contribution-transport families designed to carry media across lossy or variable networks with retransmission and bounded playout delay. They can be useful between an authorized camera gateway, mobile unit, operations centre, cloud ingest, or recorder edge. They are not camera-management profiles and do not replace ONVIF, RTSP control, WebRTC signaling, recording policy, event semantics, or evidence management.

SRT and RIST are separate protocol families. Similar goals do not make their endpoints interoperable.

## Standards and status boundary

| Family | Published basis | Status to represent |
|---|---|---|
| SRT | SRT Alliance/open-source protocol and implementation material | Active technology, but not an IETF Standard |
| SRT IETF submission | `draft-sharabayko-srt` | Expired Internet-Draft; never published as an RFC |
| RIST Simple Profile | VSF TR-06-1:2020 | Published VSF Technical Recommendation |
| RIST Main Profile | VSF TR-06-2:2024 | Published VSF Technical Recommendation |
| RIST Advanced Profile | VSF TR-06-3:2024 | Published VSF Technical Recommendation |

The expired SRT Internet-Draft and the separate `srt-rfc` repository can help explain protocol design, but neither may be cited as an IETF standard. Pin the implementation/library release and supported feature set in addition to protocol documentation. [SRT-DRAFT] [SRT-RFC]

SRT library **1.5.6**, released on 20 July 2026, included security-relevant fixes. That release baseline does not prove a vendor appliance incorporates the same code, build options, patches, or behavior. Obtain the product software bill of materials or vendor release evidence and track later advisories. [SRT-RELEASES]

## Contribution path and system boundary

```text
camera / encoder
      |
      v
authorized contribution sender
  packetization + bounded recovery + optional protection
      |
      v
untrusted or variable IP path
      |
      v
authorized contribution receiver
  bounded reorder/recovery + payload validation
      |
      v
VMS / recorder / media gateway
```

The contribution sender and receiver are security endpoints. If a gateway terminates RTSP, SRT/RIST, MPEG transport, encryption, or tenancy, it can access and alter media and timing. Document every termination and do not describe the path as end-to-end protected across a component that decrypts or repacketizes it.

## What reliable means

SRT and RIST use sequence-aware packet recovery and retransmission to improve delivery over networks with loss, jitter, and reordering. Recovery is constrained by the configured latency/recovery window and available bandwidth. Packets that cannot be recovered before their usefulness deadline can still be dropped.

Reliable contribution does **not** mean:

- lossless delivery under unlimited loss or outage;
- exactly-once frame or event processing;
- authenticated media origin unless the selected security/profile design establishes it;
- guaranteed decoder recovery after missing codec dependencies;
- recorder commit, retention, or evidentiary integrity;
- physical camera health or live scene visibility.

A protocol-recovered packet can still contain malformed or malicious media. Validate the inner MPEG transport stream, RTP, elementary stream, codec, metadata, and container at their own trust boundaries.

## SRT model

SRT is built over UDP and commonly carries continuous live media such as MPEG transport streams. Implementations expose connection roles often described as **caller**, **listener**, and **rendezvous**. These are connection-establishment roles, not user or tenant authorization roles.

Core engineering dimensions include:

- socket/connection role and exact local/remote address policy;
- live/message/file mode supported by the product and the chosen payload contract;
- latency/recovery settings in both directions and their negotiation behavior;
- packet sequence, retransmission, late-drop, reordering, and timestamp-based delivery behavior;
- bandwidth overhead allowance and congestion response;
- stream-routing identifier syntax and trust treatment;
- encryption capability, key length/profile, key rotation, and authentication surrounding the session;
- reconnect, peer change, failover, and statistics reset behavior.

### Latency and recovery

The receiver needs enough buffering for path round-trip time, jitter, reordering, retransmission, and processing. Too little latency turns recoverable loss into late loss. Excessive latency delays operator awareness and can increase memory use. Measure the complete path under expected and adverse conditions, including asymmetric routes and congestion; do not copy one vendor's latency value into a different topology.

Bound socket buffers, recovery queues, maximum bitrate, packet size, retransmission overhead, connection count, and CPU. A loss burst can increase both retransmissions and inner-decoder work at the worst moment.

### Stream identifier

SRT's stream identifier can convey application routing or admission metadata under deployment-defined conventions. It is untrusted client input until the receiving application authenticates and authorizes it. Do not place permanent credentials, personal data, internal topology, or access decisions in a stream identifier; it can appear in diagnostics and intermediary logs. Define length, character/encoding, duplicate key, normalization, tenancy, and unknown-field rules.

### Encryption and identity

SRT implementations can provide payload encryption based on a shared secret/passphrase configuration. Encryption support and a matching passphrase do not establish a named user, device inventory record, tenant, purpose, or stream authorization. Define peer admission separately, use unique scoped secrets, protect them at rest, rotate them, and decide fail-closed behavior. Reject empty, default, or downgraded protection when encryption is required.

## RIST profiles

RIST is standardized through Video Services Forum TR-06 Technical Recommendations. The profiles establish interoperable subsets and add capabilities in stages. Do not infer Main or Advanced support from “RIST,” and do not infer that an implementation supports every optional feature in a profile.

### Simple Profile

The Simple Profile defines the baseline interoperable media transport and packet-recovery behavior. Record payload/RTP expectations, recovery timing, feedback path, addressing, multicast/unicast use, and any redundancy feature actually supported. Its simplicity does not supply application identity, recording semantics, or a universal security policy.

### Main and Advanced Profiles

The Main and Advanced Profiles add standardized capabilities for more complex contribution systems. Security, tunneling, stream multiplexing, link behavior, and management expectations must be taken from the selected TR-06 edition and product conformance statement; they should not be back-projected onto a Simple Profile endpoint. Where the selected profile uses DTLS, pre-shared material, certificates, or another protection mechanism, record the exact role, identity, trust, algorithm, renewal, and failure behavior.

Profile names are not performance tiers. A later profile does not remove the need to agree payload, bitrate, latency, retransmission window, protection, network path, failover, and monitoring.

## Addressing and ports

Neither family has one universal deployment port that safely identifies every SRT or RIST stream. Products, orchestration systems, examples, unicast paths, multicast groups, and multiplexed/tunneled profiles vary. Even where a service-name registration or vendor default exists, a port number is not proof of protocol, encryption, peer identity, or authorized content.

Maintain an explicit flow inventory containing source/destination identities, address families, UDP ports, direction, expected bitrate/packet rate, payload, profile, protection, and owner. Allowlist those flows; avoid wide inbound UDP ranges or Internet-exposed listeners without a designed admission and denial-of-service boundary.

## Payload and codec contract

Agree the complete inner contract:

- MPEG transport stream, RTP, or other supported payload;
- program, PID, stream, SSRC, payload type, codec, profile/level, resolution, rate, and audio layout as applicable;
- continuity counters, PCR/timestamp/clock basis, jitter and discontinuity behavior;
- codec parameter sets and keyframe/random-access strategy;
- metadata, captions, ancillary data, encryption, and unsupported-stream policy;
- maximum aggregate bitrate, burst, packet, elementary unit, frame, and decoded dimensions.

The contribution protocol cannot compensate for a missing keyframe, invalid continuity, incompatible codec, clock discontinuity, or decoder resource exhaustion. Treat payload metadata and declared dimensions/rates as untrusted until bounded.

## Failover and path diversity

Multi-path, bonding, redundant senders, or receiver failover can improve availability, but they also change duplicate, reordering, identity, and cost behavior. Verify whether paths are truly diverse or share power, carrier, NAT, firewall, or cloud-region dependencies.

Define:

- active/active versus active/standby behavior;
- packet/stream deduplication scope and sequence continuity;
- acceptable skew and payload identity between redundant senders;
- authorization when source address, receiver, or orchestration owner changes;
- whether failback is automatic and how flapping is suppressed;
- how gaps, duplicates, codec reset, timestamps, and recording continuity are surfaced.

A reconnected stream with the same label is not automatically the same authenticated source or continuous evidence record.

## Security and privacy

- Authenticate the sender/receiver or surrounding orchestration with device/workload identities, not a stream label alone.
- Authorize tenant, site, camera, purpose, destination, time window, and payload profile.
- Use supported confidentiality and integrity protection appropriate to the selected SRT implementation or RIST profile; prohibit silent downgrade.
- Segment contribution ingress from camera management, VMS administration, storage, and general corporate networks.
- Rate-limit handshakes, invalid packets, retransmission feedback, stream-ID parsing, and connection attempts before expensive allocation.
- Protect management APIs, metrics, debug dumps, packet captures, orchestration tokens, shared secrets, and certificates.
- Minimize topology, credential, camera identity, and personal information in stream identifiers and logs.
- Patch protocol libraries and appliances using vendor/SBOM evidence; the SRT 1.5.6 fixes illustrate why the embedded library baseline matters.

Network encryption does not decide whether a user may view, record, export, or retain the media. Apply privacy, recording notice, retention, redaction, and evidence policy at the application and recorder layers.

## Observability and evidence

Useful per-direction metrics include connection state, authenticated peer, uptime, bitrate/packet rate, round-trip time, configured/effective latency, packets lost/recovered/retransmitted/late/dropped, reorder depth, send/receive buffer occupancy, payload continuity errors, decoder health, reconnects, and failover path.

Keep metric labels bounded. A client-controlled stream identifier should not become an unrestricted high-cardinality or log-injection field. Correlate transport health with source encoder, network path, receiver, decoder, and recorder commit; green contribution transport alone can coexist with a frozen camera image or failed recording.

SRT/RIST delivery does not create evidentiary authenticity. For evidence, preserve source provenance, original bitstream where required, hashes/signatures, trusted time and uncertainty, transformations, gap/discontinuity records, authorization, chain of custody, and player/decoder requirements.

## Safe review and acceptance model

Documentation review can establish a proposed compatibility contract without contacting an endpoint. Use vendor capability statements, selected SRT release or RIST TR-06 profile, sanitized configuration exports, network-flow design, payload samples approved for offline review, and security/evidence controls. Operational packet-loss, jitter, failover, codec, encryption, interoperability, and performance acceptance belongs in an owner-controlled environment under a separate validation record.

## Design and evidence checklist

- [ ] SRT implementation/library release or RIST TR-06 profile/edition and product subset pinned
- [ ] SRT never represented as an IETF Standard; expired draft status recorded where cited
- [ ] Connection roles, endpoint identity, flow direction, address/port, admission, and tenancy explicit
- [ ] Payload/container/RTP, codec, timing, metadata, bitrate, packet, frame, and decoder limits defined
- [ ] Latency/recovery window derived from measured path budget and operator requirement
- [ ] Retransmission overhead, buffers, connection count, CPU, and denial-of-service limits bounded
- [ ] Encryption/integrity mode, authenticated identity, secret/certificate lifecycle, and downgrade policy defined
- [ ] Stream identifiers treated as untrusted routing metadata, not credentials
- [ ] Redundant path, deduplication, failover/failback, sequence, clock, and recording-continuity behavior documented
- [ ] Contribution termination and every plaintext/media trust boundary shown
- [ ] Transport statistics correlated with encoder, payload/decoder, and recorder health
- [ ] Privacy, view/record authorization, retention, export, and evidentiary controls applied independently

## Sources

- **SRT-ALLIANCE** — [SRT Alliance][SRT-ALLIANCE], protocol ecosystem and public resources, accessed 2026-08-25.
- **SRT-RELEASES** — [Haivision SRT releases][SRT-RELEASES], including SRT 1.5.6 released 20 July 2026.
- **SRT-DRAFT** — [Expired IETF Internet-Draft: The Secure Reliable Transport Protocol][SRT-DRAFT], IETF Datatracker; never published as an RFC.
- **SRT-RFC** — [SRT protocol specification repository][SRT-RFC], Haivision, work maintained outside the IETF standards stream.
- **VSF-TR** — [VSF Technical Recommendations][VSF-TR], including RIST TR-06-1:2020, TR-06-2:2024, and TR-06-3:2024.

[SRT-ALLIANCE]: https://srtalliance.org/
[SRT-RELEASES]: https://github.com/Haivision/srt/releases
[SRT-DRAFT]: https://datatracker.ietf.org/doc/draft-sharabayko-srt/
[SRT-RFC]: https://github.com/haivision/srt-rfc
[VSF-TR]: https://vsf.tv/technical-recommendations/
