---
title: Modbus Security
summary: TLS, certificate, authorization, migration, and operational guidance for the Modbus Security protocol.
page_type: protocol
domains: [bms, ot]
tags: [modbus-security, tls, x509, authorization, port-802]
scope: global
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: [Modbus Security Protocol]
coverage_limit: Public Modbus Organization material was reviewed; implementers must use the current downloadable security specification and product certificate profile.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Modbus Security

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / [Modbus](modbus-family.md) / Security

The Modbus Security protocol wraps Modbus in TLS and uses X.509 v3 certificates for client and server authentication and role-based authorization. The Modbus Organization assigns TCP port 802 to this protected form; classic Modbus TCP commonly uses 502.[^security]

Security is more than enabling a TLS listener. Interoperability depends on the supported Modbus Security specification edition, TLS versions and cipher suites, certificate profile, trust-anchor model, identity-to-role mapping, revocation/time policy, and whether both products implement the same authorization behaviour.

## Connection decision sequence

1. Resolve an approved endpoint from configuration—not unauthenticated discovery alone.
2. Establish TLS with current policy and validate the full server certificate path and expected identity.
3. Present the client certificate and prove possession of its private key.
4. Map the authenticated certificate identity to an explicit least-privilege Modbus role.
5. Authorize each requested function and address range; do not infer rights from network location.
6. Audit identity, decision, function, range, result, and correlation metadata without logging secrets.

## PKI operations

- Give devices unique identities. Do not clone one certificate/private key into a fleet image.
- Protect private keys with hardware-backed storage where supported; make export and replacement auditable.
- Stage trust-anchor and leaf rotation with overlap, verify clock quality, and define behaviour when revocation infrastructure is unavailable.
- Separate commissioning/bootstrap trust from steady-state trust. An installation default cannot remain an operational root of trust.
- Monitor certificate expiry, unexpected issuers, identity/role changes, failed handshakes, downgrade attempts, and authorization denials.

## Migration

Inventory both endpoints and intervening gateways. A gateway that terminates Security and emits classic RTU/TCP creates a new cleartext trust boundary; document where authentication ends and physically protect the downstream segment. Run 502 and 802 concurrently only under a time-bounded migration plan. Ensure firewall and monitoring policy distinguishes them.

TLS authenticates the endpoint and protects transport; it does not validate register semantics, make a write safe, prove physical completion, or repair a compromised authorized controller. Preserve the point contract and change-control gates in [Modbus family](modbus-family.md).

Validate certificate exchange, authorization, error handling, downgrade rejection, and conformance against the selected product versions in an isolated authorized environment.

## Primary sources

[^security]: [Modbus Organization — Modbus Security protocol announcement and specification link](https://www.modbus.org/news/modbus-security-new-protocol-to-improve-control-system-security)
- [Modbus Organization — specifications](https://www.modbus.org/modbus-specifications)
