---
title: TLS, PKI, and secure transport
summary: TLS versions, endpoint identity, mutual TLS, X.509 validation, certificate lifecycle, revocation, and protocol-profile boundaries.
page_type: reference
domains: [networking, identity, cross-domain]
tags: [tls, mtls, x509, pki, certificates, revocation]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [RFC 8446, RFC 9325, RFC 5280, RFC 9525, RFC 6960]
coverage_limit: General PKI baseline; each application protocol's TLS profile and product certification override generic assumptions.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# TLS, PKI, and secure transport

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / TLS and PKI

TLS protects a transport connection against eavesdropping and modification and authenticates endpoints according to the selected credential/profile. TLS 1.3 is RFC 8446. The current TLS deployment BCP, RFC 9325, prohibits TLS 1.0/1.1 and gives guidance for TLS 1.2/1.3 and algorithm selection.[^tls13][^bcp]

“TLS enabled” is not enough. Record application protocol/profile, client/server roles, permitted TLS versions, cipher/signature/key-exchange algorithms, SNI/ALPN if applicable, expected peer identity, trust anchors, certificate profile, client authentication, revocation/time policy, and failure behaviour.

## Server and client identity

Path validation proves that a chain terminates at a trusted anchor under PKIX rules; service-identity verification proves the certificate represents the endpoint actually requested. Apply the protocol's defined identity rules, with RFC 9525 as the general service-identity baseline when applicable.[^pkix][^identity]

- Match the configured service name using the defined subjectAltName type; do not fall back to IP/source address or a user-approved warning.
- Do not disable validation for self-signed certificates. Trust a deliberately provisioned self-signed certificate or private CA anchor with explicit scope.
- Separate trust-anchor selection from intermediate certificates supplied by the peer.
- Enforce key usage, extended key usage, name constraints, validity, algorithm strength, and application/profile identifiers as applicable.
- Mutual TLS authenticates both TLS peers, but application authorization must still map the client identity to permitted resources and actions.

## Lifecycle

Inventory issuer, serial, subjectAltName/application identity, fingerprint, key location, owner, issuance method, validity, renewal window, trust path, revocation method, deployed endpoints, and replacement history. Generate unique private keys on-device or in protected provisioning, prefer non-exportable hardware-backed keys, and never clone keys in images/backups.

Rotate trust anchors with an overlap procedure: distribute new trust, issue/test new leaves, switch identities, remove old trust only after evidence, and preserve recovery. Clock failure can make valid certificates appear expired/not-yet-valid. Monitor expiry, unexpected issuers, chain/identity failure, algorithm downgrade, trust-store change, private-key export, and repeated handshakes.

OCSP is defined by RFC 6960, while CRLs are part of PKIX.[^ocsp] Decide hard/soft failure and caching from consequence, availability, privacy, and the application profile; an unreachable responder must not silently produce an undocumented forever-valid state. Short-lived certificates may reduce but do not erase compromise response requirements.

## Protocol boundary

Do not substitute a generic reverse proxy or VPN for protocol-specific secure modes such as BACnet/SC, Modbus Security, CIP Security, KNX IP Secure, or OPC UA SecureChannel. A proxy terminates identity and protection; document the downstream cleartext/reauthentication boundary. TLS does not validate payload semantics, prevent authorized dangerous commands, attest firmware, or prove physical completion.

Validate handshakes, chain construction, revocation behaviour, clock faults, algorithm policy, certificate rotation, and rollback against the target implementations.

## Primary sources

[^tls13]: [RFC Editor — RFC 8446, TLS 1.3](https://www.rfc-editor.org/info/rfc8446/)
[^bcp]: [RFC Editor — RFC 9325, recommendations for secure TLS and DTLS](https://www.rfc-editor.org/info/rfc9325/)
[^pkix]: [RFC Editor — RFC 5280, Internet X.509 PKI certificate and CRL profile](https://www.rfc-editor.org/info/rfc5280/)
[^identity]: [RFC Editor — RFC 9525, service identity in TLS](https://www.rfc-editor.org/info/rfc9525/)
[^ocsp]: [RFC Editor — RFC 6960, OCSP](https://www.rfc-editor.org/info/rfc6960/)
