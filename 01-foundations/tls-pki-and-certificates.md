---
title: TLS, PKI, and Certificates
summary: Transport protection, peer identity, certificate lifecycle, mutual TLS, and common embedded-device failure modes.
page_type: foundation
domains: [cross-domain]
tags: [tls, pki, certificates, mtls, cryptography]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: [RFC 8446, RFC 9325, RFC 5280]
coverage_limit: Baseline architecture, not a cipher-suite mandate or jurisdiction-specific cryptographic policy.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# TLS, PKI, and certificates

Transport Layer Security (TLS) can provide confidentiality, integrity, and endpoint authentication for a connection. It does not decide whether the authenticated peer may view a camera, issue a door command, change configuration, or access another tenant.

## Baseline

- Follow the current [BCP 195 / RFC 9325](https://www.rfc-editor.org/info/rfc9325) and its updates rather than freezing cipher advice in application code. It prohibits SSLv2/v3 and TLS 1.0/1.1 and promotes TLS 1.3; exact compatibility policy must account for the deployed product set.
- TLS 1.3 is defined by [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446). Do not enable early data (0-RTT) for state-changing operations unless the application specification explicitly makes replay safe.
- X.509 path validation is defined by [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280). A successful cryptographic handshake is insufficient if hostname/service identity, validity, usage, constraints, revocation policy, and trust anchor are not validated.

## Server and mutual authentication

With server-authenticated TLS, the client authenticates the service; the server usually authenticates the client at the application layer. Mutual TLS (mTLS) also presents a client certificate and can strongly identify a device or workload, but still needs mapping to an account/tenant/role and certificate lifecycle.

Keep these identities separate:

- DNS/service name in the certificate;
- product device ID/serial;
- application client or workload;
- human operator;
- tenant/site;
- authorization role.

## Private PKI lifecycle

Plan the whole lifecycle before enabling certificate-only access:

```text
key generation -> enrollment -> approval -> issuance -> distribution
-> validation -> inventory -> renewal/rotation -> revocation/distrust -> retirement
```

Prefer keys generated and retained in hardware-backed storage where available. Use separate issuing CAs/policies for device, workload, and user certificates. Keep offline/restricted root material and test recovery from an expired or lost intermediate. Do not ship the same private key or default certificate across devices.

## Embedded and appliance pitfalls

- self-signed certificates silently accepted or “trust on first use” without an authenticated ceremony;
- hostname validation disabled because devices use IP addresses;
- no usable enrollment/renewal interface;
- clock not yet valid, causing certificate failures during bootstrap;
- hard-coded trust stores that cannot be updated;
- weak legacy protocols retained for compatibility;
- management UI protected while RTSP, events, or SDK traffic remains cleartext;
- certificate replacement resetting on firmware upgrade or factory reset;
- client certificates mapped to a shared administrator role.

If a legacy device cannot meet policy, place a managed TLS gateway close to it and constrain the cleartext segment physically and logically. Document that this is compensating containment, not end-to-end protection.

## Validation checklist

- correct peer identity and full chain, including name and intended usage;
- rejection of unknown CA, wrong name, expired/not-yet-valid, revoked/distrusted, and malformed certificates according to policy;
- no downgrade to cleartext or obsolete versions;
- certificate/CA rotation without unsafe outage;
- distinct client identities and least-privilege mapping;
- protected private keys, sanitized TLS logs, and observable expiry;
- session resumption and load balancer behaviour understood;
- trust-store and time-source recovery documented.

Do not paste private keys or live certificate bundles into this knowledge base.

