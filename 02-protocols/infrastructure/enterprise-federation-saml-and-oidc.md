---
title: "Enterprise federation with SAML and OpenID Connect"
summary: "Secure operator and application federation using SAML 2.0 and OpenID Connect, with strict validation, lifecycle, role-mapping, outage, and physical-authorization boundaries."
page_type: protocol
domains: [identity, networking, cross-domain]
tags:
  - saml
  - oidc
  - oauth
  - federation
  - single-sign-on
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "OASIS SAML 2.0 with SAML Version 2.0 Errata 05"
  - "OpenID Connect Core 1.0 incorporating errata set 2"
  - "NIST SP 800-63C-4"
  - "RFC 9700 / BCP 240"
coverage_limit: "Enterprise application federation guidance; identity proofing, authenticator assurance, organization-specific entitlement policy, PACS credential issuance, and physical-access decisions require separate controls."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Enterprise federation with SAML and OpenID Connect

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / Enterprise federation

Federation lets one security domain rely on authenticated identity information from another. SAML 2.0 and OpenID Connect (OIDC) are widely used for operator sign-in and application session establishment. Apply the OASIS SAML Version 2.0 Errata 05 alongside the base SAML publications; its clarifications affect interoperability and security-sensitive processing. Neither federation family, by itself, provisions accounts, proves a requested physical action is safe, or grants access to doors, video, alarms, intercom, or evidence. [SAML] [SAML-ERRATA] [OIDC] [NIST-FED]

## Protocol and responsibility boundaries

| Concern | SAML 2.0 | OpenID Connect | Separate responsibility |
|---|---|---|---|
| Primary model | XML assertions and protocol messages between identity provider and service provider | Identity layer over OAuth 2.0 using ID Tokens, UserInfo, discovery, and OAuth endpoints | Local application session and authorization |
| Typical browser flow | Web Browser SSO profile using HTTP Redirect/POST bindings | Authorization Code flow; PKCE should be used according to the client profile | Browser security, session cookie, CSRF, and logout policy |
| Identity evidence | Signed assertion and its conditions/statements | Signed ID Token and protocol checks; optionally UserInfo | Identity proofing and authenticator assurance at the IdP |
| API authority | SAML bearer profiles exist but are not implied by browser SSO | OAuth access token, not an ID Token | Resource-server audience, scope, object, action, tenant, and safety policy |
| Lifecycle | May create a just-in-time local account | May create a just-in-time local account | SCIM/directory reconciliation, disablement, ownership, and deletion |
| Physical authorization | None | None | PACS/controller policy and operation-specific controls |

OAuth is an authorization framework. OIDC adds an authentication layer. A valid OAuth access token is not necessarily evidence of an interactive user login, and a valid OIDC ID Token is intended for its client—not as a general API bearer credential. Follow RFC 9700 for OAuth security decisions. [OAUTH-BCP]

## Trust model and onboarding

Federation trust is configuration, not merely successful signature verification. Establish through a controlled onboarding process:

- exact issuer/entity identifier and environment;
- allowed SAML endpoints/bindings or OIDC discovery issuer and endpoints;
- trusted signing and, where used, encryption keys and algorithms;
- service-provider entity ID or OIDC client ID and exact redirect URIs;
- subject identifier semantics and tenant/organization mapping;
- required authentication context or assurance information;
- approved attributes/claims and their authoritative source;
- clock-skew, assertion/token lifetime, nonce, replay, and session policy;
- key rollover, emergency revocation, metadata/discovery refresh, and rollback ownership.

Do not dynamically trust an issuer, metadata URL, discovery URL, or key set supplied by an untrusted login request. Discovery and metadata retrieval are privileged configuration inputs: constrain scheme, host, redirects, size, parser behavior, refresh, and change approval.

## Stable identity mapping

Use a protocol-stable, issuer-scoped subject key:

```text
federated identity key = trusted issuer + protocol subject identifier
```

For OIDC this is normally the `iss` and `sub` pair. For SAML, define the accepted issuer plus NameID format/value or another contractually immutable identifier. Email address, display name, username, group display name, employee number, or certificate common name may change or collide and should not be the sole durable key unless an authoritative contract guarantees its scope and lifecycle.

Pairwise subject identifiers reduce cross-service correlation but require explicit account-linking design. Never merge two local operator records solely because an email-like claim matches. Make account linking an authenticated, audited, reversible process with collision handling.

## SAML 2.0 validation profile

SAML uses XML and supports multiple profiles and bindings. Pin the profile rather than accepting any syntactically valid SAML message. [SAML-CORE] [SAML-PROFILES]

For Web Browser SSO, validate at least:

1. expected response type, binding, destination, and service-provider endpoint;
2. trusted response/assertion issuer and signature according to the deployment profile;
3. signature algorithm, digest algorithm, certificate/key, and key rollover policy;
4. assertion audience restriction, recipient, subject-confirmation method, and `InResponseTo` when request correlation applies;
5. `NotBefore` and `NotOnOrAfter` under bounded clock skew;
6. replay of response/assertion identifiers for their useful lifetime;
7. required authentication context and attribute schema;
8. RelayState integrity and its binding to locally stored request state;
9. one unambiguous assertion/subject/attribute set after validation.

### XML and signature-wrapping safety

- Disable external entities, DTD processing, XInclude, and external resource retrieval.
- Bound document bytes, element depth/count, attributes, text, base64 values, and decompressed request size.
- Reject duplicate XML IDs and ambiguous duplicate protocol elements.
- Verify the signature reference and then consume the exact validated element; do not validate one assertion and read identity from another.
- Avoid permissive “find first assertion anywhere” logic.
- Apply schema/profile validation and business validation; a cryptographic signature alone does not make every claim acceptable.
- Keep encryption keys separate from signing trust and reject unsupported algorithm/key combinations.

Whether the SAML Response, Assertion, or both must be signed is a deployment-profile decision. State it explicitly; do not accept either opportunistically.

## OpenID Connect validation profile

OIDC Core defines authentication using OAuth 2.0 protocol elements. Prefer Authorization Code flow and apply the current OAuth security BCP. [OIDC] [OAUTH-BCP]

### Authorization request and response

- Use an exact preregistered redirect URI; never use substring, wildcard, or open-redirect matching for sensitive clients.
- Generate high-entropy `state` and bind it to the browser session and intended return context.
- Use PKCE with a strong challenge method for authorization-code interception protection; PKCE does not replace `state` or client authentication.
- Generate and validate a nonce for OIDC flows where required by the profile and bind it to the transaction.
- Prevent mix-up by binding the response to the expected issuer and authorization server.
- Keep authorization codes out of logs, referrers, browser history, and analytics where practicable; redeem once over protected transport.

### ID Token

Validate:

- exact `iss` match to the configured issuer;
- `aud` contains the client ID and `azp` is handled where required;
- signature against a trusted, refreshed issuer key set under an algorithm allowlist;
- `exp`, `iat`, and any required `nbf` with bounded clock tolerance;
- expected nonce and authentication context/age where required;
- token type/use so an access token or token from another environment cannot be substituted.

Do not select an arbitrary key solely by attacker-controlled header data. Bound JSON/token/header/key-set size, reject duplicate security-critical JSON members, and define behavior for an unknown key ID during controlled key refresh.

### Access tokens and UserInfo

An API validates access tokens according to the authorization-server profile: issuer, resource audience, signature or introspection result, token type, lifetime, client/subject, scopes, confirmation/sender constraint where used, and revocation/cache policy. It then authorizes the exact object and action.

The OIDC client must verify that UserInfo `sub` exactly matches the ID Token `sub`. Treat other claims as untrusted for authorization unless the federation contract makes them authoritative and current.

## Claims, groups, and role mapping

Federated claims are inputs to local policy, not automatically local permissions.

- Allowlist accepted claim names, types, cardinality, namespace, issuer, and maximum size.
- Distinguish absent, empty, false, unknown, and explicitly removed values.
- Map external groups to narrowly scoped local roles through reviewed configuration.
- Prevent a tenant administrator from minting a group name that collides with a privileged platform group.
- Define nested-group expansion, overage/truncation behavior, replication delay, and stale-session handling.
- Record mapping/policy version with every privileged authorization decision.
- Require local step-up, approval, reason, and safety prerequisites for high-impact operations where appropriate.

An IdP administrator able to alter claims can indirectly affect application access. Include federation configuration, claim rules, signing keys, and privileged group administration in the threat model and audit scope.

## Federation, provisioning, and deprovisioning

Just-in-time account creation helps onboarding but does not guarantee prompt disablement. A session or refresh token can outlive an upstream account change, and a user who never logs in again may never trigger cleanup.

Use [SCIM identity provisioning](scim-identity-provisioning.md), a directory connector, or another reconciled lifecycle channel for joiner/mover/leaver state. Define which system owns display data, employment status, role membership, credential assignment, site scope, and deletion. Reconcile periodically rather than assuming individual events are complete.

Keep identity federation separate from physical credential lifecycle:

```text
enterprise identity status
  -> application account and operator roles
  -> approved PACS identity/credential workflow
  -> controller policy distribution
  -> presentation and physical-access decision
```

Disabling application SSO does not prove cards, mobile credentials, PINs, cached controller rights, or existing sessions were revoked.

## Sessions, logout, and token lifetime

- Set absolute and idle application-session limits according to consequence.
- Regenerate session identifiers after authentication and privilege change.
- Use secure, HttpOnly, appropriately scoped cookies and a deliberate SameSite/CSRF policy.
- Reauthenticate or step up before sensitive exports, role changes, credential administration, overrides, and physical commands.
- Recheck authorization for long-running jobs and streams.
- Treat front-channel/back-channel/single logout as a profile with partial-failure states; local logout, IdP logout, token revocation, and all relying-party sessions are different outcomes.
- Never make emergency egress or certified life-safety operation depend on a browser session or live IdP.

## Availability and break-glass

Define behavior when DNS, time, metadata, key discovery, the IdP, token endpoint, directory, or upstream MFA is unavailable. Avoid both silent fail-open and total loss of safely required local administration.

A break-glass identity should be local only where necessary, minimally privileged, independently protected, monitored, tested through an approved exercise, and followed by credential rotation and review. It must not become the routine answer to federation outages.

## Audit and privacy

Record trusted issuer, subject key, client/service provider, authentication context, session ID in non-reusable form, claim-mapping version, local role/policy decision, target tenant/resource/action, correlation ID, outcome, and administrative configuration changes. Do not log assertions, ID Tokens, access tokens, authorization codes, private keys, or unnecessary identity attributes.

Federation logs can reveal employment, role, location, access, and incident-response information. Minimize collection, restrict access/export, define retention, and preserve source and receive time separately.

## Review checklist

- [ ] SAML profile/bindings or OIDC flow and exact issuer/client/service-provider identifiers pinned
- [ ] Metadata/discovery/key retrieval constrained and key rollover/revocation rehearsed
- [ ] Stable issuer-scoped subject key used; account linking handles collision and recovery
- [ ] SAML destination, audience, recipient, time, correlation, replay, signature, and exact signed object validated
- [ ] XML parser and signature-wrapping defenses enforced
- [ ] OIDC state, PKCE, nonce, issuer, audience/authorized party, time, algorithm, and token type validated
- [ ] ID Tokens rejected as general API access tokens; UserInfo subject matched
- [ ] External claims/groups mapped through typed, scoped, versioned local policy
- [ ] Provisioning/deprovisioning and active-session revocation reconciled separately
- [ ] Federation success kept separate from application, PACS, and physical authorization
- [ ] Outage, break-glass, logout, privacy, and audit behavior documented

## Sources

- **SAML** — [SAML 2.0 standard documents][SAML], OASIS.
- **SAML-ERRATA** — [SAML Version 2.0 Errata 05][SAML-ERRATA], OASIS Approved Errata, 1 May 2012.
- **SAML-CORE** — [Assertions and Protocols for SAML V2.0][SAML-CORE], OASIS Standard.
- **SAML-PROFILES** — [Profiles for SAML V2.0][SAML-PROFILES], OASIS Standard.
- **OIDC** — [OpenID Connect Core 1.0 incorporating errata set 2][OIDC], OpenID Foundation, December 2023.
- **OAUTH-BCP** — [RFC 9700 / BCP 240: Best Current Practice for OAuth 2.0 Security][OAUTH-BCP], IETF, January 2025.
- **NIST-FED** — [NIST SP 800-63C-4: Federation and Assertions][NIST-FED], NIST, July 2025.

[SAML]: https://docs.oasis-open.org/security/saml/v2.0/
[SAML-ERRATA]: https://docs.oasis-open.org/security/saml/v2.0/sstc-saml-approved-errata-2.0.html
[SAML-CORE]: https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf
[SAML-PROFILES]: https://docs.oasis-open.org/security/saml/v2.0/saml-profiles-2.0-os.pdf
[OIDC]: https://openid.net/specs/openid-connect-core-1_0.html
[OAUTH-BCP]: https://www.rfc-editor.org/info/rfc9700/
[NIST-FED]: https://csrc.nist.gov/pubs/sp/800/63/C/4/final
