---
title: "SIP and SRTP for intercom and real-time media"
summary: "Developer reference for SIP transactions/dialogs, SDP offer-answer, call flows, identity, signaling protection, SRTP profiles, key management, and physical-security controls."
page_type: protocol
domains: [intercom, video]
tags:
  - sip
  - sdp
  - srtp
  - dtls-srtp
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "RFC 3261: SIP"
  - "RFC 3264: SDP Offer/Answer"
  - "RFC 3711: SRTP"
  - "RFC 5764: DTLS-SRTP"
coverage_limit: "Core signaling and media-protection architecture only; no PBX, proxy, intercom, registration, call, SRTP exchange, DTMF action, or door-control behavior is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# SIP and SRTP for intercom and real-time media

[Video and media protocols](README.md) / SIP and SRTP

SIP establishes, modifies, and terminates multimedia sessions. SDP usually describes the media; RTP carries it; SRTP can protect it. SIP signaling protection and media protection are independent. A TLS-protected SIP hop does not automatically encrypt RTP, and SRTP does not authorize a caller to unlock a door. [SIP] [SRTP]

## Standards status and profiles

RFC 3261 remains the SIP core, with many updating RFCs. The IETF SIPCORE charter identifies the maintained core family including reliable provisional responses (RFC 3262), server location (RFC 3263), SDP offer/answer (RFC 3264), and event notification (RFC 6665). Implementations must state the extensions and option tags they support rather than claiming an unspecified “latest SIP.” [SIPCORE]

| Function | Reference | Notes |
|---|---|---|
| Core signaling | RFC 3261 plus applicable updates | Transactions, dialogs, routing, methods, responses |
| Media negotiation | RFC 3264 | Offer/answer rules over SDP |
| Digest authentication update | RFC 8760 | Modern algorithms and updates to SIP Digest behavior |
| Authenticated calling identity | RFC 8224 | PASSporT-based identity within an originating/terminating service model; not universal end-user identity |
| SRTP base | RFC 3711, updated by RFCs 5506, 6904, and 9335 | Media confidentiality, message authentication, and replay protection profiles |
| AEAD AES-GCM for SRTP | RFC 7714 | Modern authenticated-encryption transforms |
| DTLS-SRTP keying | RFC 5764 | Establishes SRTP keying material from DTLS |
| SDP security descriptions | RFC 4568 | Carries key parameters in SDP; the signaling path must protect them and deployment support varies |

## SIP concepts that must stay distinct

- **Transaction:** one request and its responses, with client/server transaction state.
- **Dialog:** peer relationship established by identifiers such as Call-ID and tags; multiple transactions can occur within it.
- **Registration:** binding an Address of Record to contacts; registration is not call authorization.
- **Route set:** proxies a dialog traverses; it is not necessarily the media path.
- **Session:** negotiated media state; it can outlive a transaction and can change through re-INVITE or UPDATE where supported.

Call-ID, tags, branches, contacts, display names, and asserted headers are protocol identifiers or claims, not independently verified identities.

## Basic intercom call flow

```text
door station             proxy/registrar              operator endpoint
     |--- REGISTER ---------->|                              |
     |<-- 401 challenge ------|                              |
     |--- REGISTER + auth --->|                              |
     |<-- 200 ----------------|                              |
     |--- INVITE + SDP ------>|--- INVITE + SDP ----------->|
     |<-- 100 / 180 ----------|<-- provisional -------------|
     |<-- 200 + SDP answer ---|<-- 200 + SDP answer --------|
     |--- ACK --------------->|--- ACK --------------------->|
     |<========= RTP/SRTP media, often on a separate path ===>|
     |--- BYE --------------->|--- BYE --------------------->|
     |<-- 200 ----------------|<-- 200 ----------------------|
```

`CANCEL` stops a pending request; it does not terminate an established dialog. `ACK` handling differs for 2xx and non-2xx final responses. Model retransmissions, provisional responses, forking, multiple final responses, glare, session timers, and endpoint restart.

## Safe message shape

**Target:** Parser and documentation fixture only.

**Inputs:** Reserved example domains, names, and no credentials.

**Side effects:** None.

```sip
OPTIONS sip:intercom-01@devices.example SIP/2.0
Via: SIP/2.0/TLS client.example;branch=z9hG4bK-doc-001
Max-Forwards: 20
From: <sip:monitoring@client.example>;tag=doc-from-001
To: <sip:intercom-01@devices.example>
Call-ID: doc-call-001@client.example
CSeq: 1 OPTIONS
Contact: <sips:monitoring@client.example>
Content-Length: 0
```

The example is intentionally unauthenticated and unsuitable for production. A real implementation must follow the selected transport, certificate, routing, authentication, authorization, and extension profile.

## Signaling protection

### TLS and SIPS

Use TLS with certificate validation between each managed hop. `sips:` expresses a requirement for secure SIP transport along the route defined by SIP; it does not mean that every intermediary is invisible, that headers are end-to-end encrypted, or that media is protected. RFC 5630 clarifies SIPS handling. [SIPS]

Protect UDP/TCP-only legacy segments with network isolation and a migration plan. Reject opportunistic downgrade after TLS failure. Do not disable name/certificate verification to accommodate IP-address provisioning without an explicit trust design.

### Digest and identity

- Use updated Digest algorithms/profile support and TLS; do not rely on legacy weak choices or reusable shared credentials.
- Use unique endpoint credentials, bounded nonce lifetime, replay detection, attempt throttling, and credential rotation.
- SIP Identity can authenticate an asserted telephone identity within its trust framework; it does not prove physical presence or entitlement to a door operation.
- Display name and `From` URI are untrusted presentation data.

## SRTP and key management

SRTP adds encryption, integrity/authentication (depending on transform), and replay protection to RTP; SRTCP does the same for RTCP. Security depends on the negotiated transform and, critically, how keys and peer identity are established.

### DTLS-SRTP

DTLS-SRTP performs a DTLS handshake on the media path and exports SRTP keying material. Bind the certificate fingerprint from SDP to an authenticated signaling exchange. A fingerprint received over unauthenticated signaling can be replaced by an attacker.

### SDP security descriptions

RFC 4568 places SRTP key parameters in SDP. It is only acceptable when the complete signaling path and every component that can read the SDP are trusted for key exposure. Avoid logging or recording SDP that contains key material. Prefer a stronger key-management design where both endpoints support it.

### Transform selection

Inventory actual support. Older AES counter mode plus HMAC-SHA1 SRTP profiles remain deployed; AEAD AES-GCM profiles are defined by RFC 7714. Never negotiate “SRTP” without recording the exact protection profile, authentication-tag behavior, replay-window expectations, and rollover-counter handling. [SRTP-GCM]

## DTMF and physical control

DTMF can be in-band audio, RTP telephone events, or SIP INFO depending on the deployment. It can be replayed, generated by intermediaries, lost, duplicated, or exposed to media processors. A DTMF digit sequence must not be the sole authorization for unlock, relay, alarm suppression, or configuration. Route high-impact actions to a separately authenticated, authorized, freshness-protected control API and correlate the action to an operator identity.

## Parser and state-machine controls

- Bound start line, header count/length, body length, MIME nesting, SDP size, contacts, routes, and fork branches.
- Reject conflicting `Content-Length` values and parser differentials between proxy and endpoint.
- Validate URI schemes, hostnames, ports, and route targets before resolving or connecting.
- Use a real SIP grammar/state machine; do not parse security-relevant headers with ad-hoc string splitting.
- Keep transaction timers and dialog/session lifetimes bounded.
- Treat REFER, MESSAGE, SUBSCRIBE/NOTIFY, INFO, and vendor methods as separately authorized capabilities.
- Prevent automatic media or microphone activation except under documented operational policy.

## Deployment checklist

- [ ] Exact SIP transports, RFC extensions, option tags, codecs, and DTMF method documented
- [ ] Mutual endpoint/proxy trust and certificate lifecycle defined
- [ ] Unique endpoint credentials and modern Digest behavior configured
- [ ] Registration, call placement, media receive/send, and door-control permissions separated
- [ ] SDP offer/answer, early media, forking, re-INVITE, timeout, and restart behavior handled
- [ ] Exact SRTP profile and authenticated key-management method required
- [ ] Plain RTP fallback prohibited or explicitly isolated and accepted
- [ ] SIP/SDP/message sizes and state allocation bounded before authentication
- [ ] Identity headers and display text not treated as sufficient authorization
- [ ] DTMF/data-channel control mapped to an independently authorized service
- [ ] Call detail, SDP, addresses, and media metadata retained/redacted by policy

## Environment validation

SIP profiles differ materially across products. Validate registration, proxy routing, TLS identity, offer/answer, codec and DTMF negotiation, SRTP key management, retransmission/forking, intercom/PBX recovery, privacy, and the independently authorized door-control boundary in an approved lab.

## Sources

- **SIP** — [RFC 3261: SIP: Session Initiation Protocol][SIP], IETF, June 2002, including datatracker update status.
- **SIPCORE** — [SIPCORE Working Group Charter][SIPCORE], IETF, accessed 2026-08-25.
- **OFFER-ANSWER** — [RFC 3264: An Offer/Answer Model with SDP][OFFER-ANSWER], IETF, June 2002.
- **SIP-DIGEST** — [RFC 8760: The Session Initiation Protocol Digest Access Authentication Scheme][SIP-DIGEST], IETF, March 2020.
- **SIP-IDENTITY** — [RFC 8224: Authenticated Identity Management in SIP][SIP-IDENTITY], IETF, February 2018.
- **SIPS** — [RFC 5630: The Use of the SIPS URI Scheme in SIP][SIPS], IETF, October 2009.
- **SRTP** — [RFC 3711: The Secure Real-time Transport Protocol][SRTP], IETF, March 2004, including datatracker update status.
- **DTLS-SRTP** — [RFC 5764: DTLS Extension to Establish Keys for SRTP][DTLS-SRTP], IETF, May 2010.
- **SRTP-GCM** — [RFC 7714: AES-GCM Authenticated Encryption in SRTP][SRTP-GCM], IETF, December 2015.
- **SDES** — [RFC 4568: SDP Security Descriptions for Media Streams][SDES], IETF, July 2006.

[SIP]: https://datatracker.ietf.org/doc/rfc3261/
[SIPCORE]: https://datatracker.ietf.org/doc/charter-ietf-sipcore/
[OFFER-ANSWER]: https://datatracker.ietf.org/doc/rfc3264/
[SIP-DIGEST]: https://datatracker.ietf.org/doc/rfc8760/
[SIP-IDENTITY]: https://datatracker.ietf.org/doc/rfc8224/
[SIPS]: https://datatracker.ietf.org/doc/rfc5630/
[SRTP]: https://datatracker.ietf.org/doc/rfc3711/
[DTLS-SRTP]: https://datatracker.ietf.org/doc/rfc5764/
[SRTP-GCM]: https://datatracker.ietf.org/doc/rfc7714/
[SDES]: https://datatracker.ietf.org/doc/rfc4568/
