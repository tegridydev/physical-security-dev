---
title: "Identity, authentication, and authorization controls"
summary: "Identity and permission design for people, devices, services, credentials, and high-impact commands."
page_type: security
domains:
  - cross-domain
tags:
  - identity
  - authentication
  - authorization
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-63-4"
  - "OAuth 2.0 Security Best Current Practice, RFC 9700"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Identity, authentication, and authorization controls

[Home](../README.md) / [Security and assurance](README.md) / Identity, authentication, and authorization controls

Physical-security systems contain several identity types that must not be collapsed into one account model: people, presented credentials, doors and devices, services, workloads, operators, administrators, installers, tenants, sites, and vendors.

The foundation page [Identity, authentication, and authorization](../01-foundations/identity-authentication-and-authorization.md) defines the canonical conceptual model. The assurance controls here cover identity classes, token/session handling, command permissions, broker/API policy, and audit.

## Separate the decisions

| Decision | Question | Common failure |
|---|---|---|
| Identification | Which subject or component is making the request? | Treating a card number, IP address, topic, or serial address as proof of identity |
| Authentication | What evidence binds the claimant to that identity now? | Shared defaults, unvalidated certificates, reusable bearer material |
| Authorization | May this identity perform this action on this object in this state? | Equating successful login or network reachability with permission |
| Accounting | Can the decision and outcome be reconstructed? | Shared accounts, missing correlation IDs, mutable or unsynchronized logs |

## Identity classes

- Human workforce identity: managed through an authoritative joiner-mover-leaver process.
- Physical credential: a token or mobile credential linked to a person or role; the identifier alone may not be secret or authentic.
- Device identity: preferably a unique key and certificate bound to a device lifecycle, not a shared fleet password.
- Workload identity: unique per service or integration instance, with narrowly scoped API/broker permissions.
- Administrative identity: separate from day-to-day operator identity, with stronger authentication and audit.
- Break-glass identity: controlled, monitored, periodically verified, and designed around safe loss of upstream identity services.

## Authorization model

Model an authorization as subject, action, resource, context, and policy version. Context may include site, tenant, door group, alarm partition, device class, time schedule, incident state, dual approval, and command origin. A transport session does not make subsequent actions safe automatically.

High-impact actions require explicit verbs and audit semantics. Avoid generic write or execute permissions that silently include unlock, disarm, relay activation, configuration reset, firmware change, evidence deletion, or credential issuance.

## Token and session guidance

- Validate issuer, audience, signature, time bounds, intended token type, and required claims.
- Use short-lived access tokens and narrowly scoped service credentials; rotate without service-wide outages.
- Prevent bearer tokens from entering URLs, logs, trace exports, crash reports, or browser history.
- Bind sessions to appropriate client/device evidence where the supported protocol permits it.
- Reject ambiguous subject or tenant identifiers and stale authorization caches.
- Define revocation and offline behavior before relying on cloud-issued credentials.

OAuth 2.0 is an authorization framework; it is not by itself user authentication. Use OpenID Connect when the application needs standardized identity assertions, and follow the current OAuth security best current practice for flow selection and token handling [RFC-9700].

## Service and broker permissions

For MQTT or event brokers, constrain publish and subscribe independently by exact topic hierarchy and tenant/site identity. For web APIs, authorize each object and command server-side; never trust a client-supplied site, role, or ownership field. For device APIs, distinguish media view, event subscription, health, configuration, firmware, user management, and output control.

## Sources

- **NIST-800-63** — [NIST SP 800-63-4 Digital Identity Guidelines][NIST-800-63], final July 2025, accessed 2026-08-25.
- **RFC-9700** — [RFC 9700: Best Current Practice for OAuth 2.0 Security][RFC-9700], January 2025, accessed 2026-08-25.
- **OIDC-CORE** — [OpenID Connect Core 1.0 incorporating errata set 2][OIDC-CORE], accessed 2026-08-25.

[NIST-800-63]: https://csrc.nist.gov/pubs/sp/800/63/4/final
[RFC-9700]: https://www.rfc-editor.org/rfc/rfc9700
[OIDC-CORE]: https://openid.net/specs/openid-connect-core-1_0.html

## Related pages

- [PKI, certificates, keys, and secrets](pki-certificates-keys-and-secrets.md)
- [API and event security](api-and-event-security.md)
- [Credential lifecycle](../03-systems/access-control/credential-lifecycle.md)
