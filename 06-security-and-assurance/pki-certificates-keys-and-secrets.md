---
title: "PKI, certificates, keys, and secrets"
summary: "Lifecycle guidance for device identity, TLS trust, signing keys, shared keys, and application secrets."
page_type: security
domains:
  - cross-domain
tags:
  - pki
  - tls
  - secrets
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards:
  - "RFC 5280"
  - "RFC 8446"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# PKI, certificates, keys, and secrets

[Home](../README.md) / [Security and assurance](README.md) / PKI, certificates, keys, and secrets

PKI is an operating system for trust, not a certificate-generation task. A secure design defines issuance, identity proofing, trust distribution, storage, renewal, revocation, algorithm transition, backup, incident response, and decommissioning.

## Trust inventory

For every protected flow, record:

- certificate or key purpose: TLS server, TLS client, code signing, firmware signing, media/evidence signing, OSDP secure channel, API token signing, or data encryption;
- subject identity and uniqueness boundary;
- issuing authority and trust anchors;
- private-key generation and storage location;
- supported algorithms, protocol versions, key usage, and name constraints;
- enrollment and renewal mechanism;
- revocation or distrust mechanism and offline behavior;
- overlap window and rollback plan;
- evidence showing the active certificate/key on each endpoint.

## TLS endpoint validation

A client must validate the certificate chain, validity interval, intended key usage, and expected DNS/IP service identity. An encrypted session with an unverified peer protects only against passive observation; it does not establish whom the client reached. Never solve a deployment problem by installing a permanent accept-all callback or disabling hostname verification.

TLS 1.3 is specified by RFC 8446; exact protocol and cipher policy still depends on device support, ecosystem requirements, and current organizational cryptographic guidance [RFC-8446]. Record when a legacy device forces weaker choices and isolate it rather than silently lowering the whole system baseline.

## Key storage and handling

- Generate private keys at the strongest practical boundary and mark them non-exportable where supported.
- Use unique device and workload keys; shared fleet keys turn one compromise into systemic impersonation.
- Keep secrets out of source, Markdown, URLs, logs, screenshots, packet captures, support bundles, and command history.
- Give services access only to the specific secret version they require.
- Zero or release sensitive buffers according to the language/runtime and threat model.
- Separate encryption, signing, authentication, and key-encryption purposes.

## Renewal and failure

Track certificate expiry as an operational signal with enough lead time for approval, rollout, and rollback. Test overlap of old and new trust anchors before removing the old one. Define behavior when revocation information, enrollment services, or time sources are unavailable; insecure bypass must never be the automatic recovery mode.

## Legacy shared-key protocols

Where a protocol uses pre-shared keys, document provisioning, uniqueness, storage, rotation, loss, replacement, and downgrade behavior. A label such as secure channel is incomplete without knowing which base key is installed, whether an installation/default key remains accepted, and how the peer is authenticated.

## Sources

- **RFC-5280** — [RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL Profile][RFC-5280], accessed 2026-08-25.
- **RFC-8446** — [RFC 8446: The Transport Layer Security Protocol Version 1.3][RFC-8446], accessed 2026-08-25.
- **NIST-TLS** — [NIST SP 800-52 Rev. 2: Guidelines for TLS Implementations][NIST-TLS], accessed 2026-08-25.

[RFC-5280]: https://www.rfc-editor.org/rfc/rfc5280
[RFC-8446]: https://www.rfc-editor.org/rfc/rfc8446
[NIST-TLS]: https://csrc.nist.gov/pubs/sp/800/52/r2/final

## Related pages

- [Secure commissioning and onboarding](secure-commissioning-and-onboarding.md)
- [Remote access](remote-access.md)
- [Resilience, backup, and recovery](resilience-backup-and-recovery.md)
