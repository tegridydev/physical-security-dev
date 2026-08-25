---
title: Identity, Authentication, and Authorization
summary: Separating people, credentials, devices, workloads, tenants, roles, and policy decisions across physical-security systems.
page_type: foundation
domains: [cross-domain]
tags: [identity, authentication, authorization, rbac, oauth]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [NIST SP 800-63-4, RFC 9700, RFC 10027]
coverage_limit: General security architecture; assurance levels and legal identity-proofing requirements are context-specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Identity, authentication, and authorization

Identity names an entity; authentication provides evidence for a claimed identity; authorization decides whether that entity may perform a specific operation on a specific resource under current conditions. Keep all three explicit.

## Identity classes

| Class | Examples | Typical lifecycle owner |
|---|---|---|
| Person | employee, contractor, visitor, resident | HR/identity/visitor process |
| Credential/authenticator | card, mobile key, passkey, password, token | credential service/PACS/IdP |
| Device | camera, reader, controller, gateway | asset/enrollment/PKI process |
| Workload/client | integration service, VMS connector, automation | platform/IAM team |
| Operator session | signed-in user plus device and context | application/IdP |
| Tenant/site | organizational or location scope | service administration |

A credential ID is not a person, and possession does not prove rightful use. A device certificate is not an operator identity. An API token is not a safe place to encode permanent authorization.

## Authentication

Choose assurance based on consequence and threat. NIST [SP 800-63-4](https://csrc.nist.gov/pubs/sp/800/63/4/final) is an authoritative digital-identity reference for identity proofing, authentication, and federation, but its federal scope and assurance framework must be profiled to the use case.

For privileged or remote access, prefer phishing-resistant multi-factor authentication where the platform supports it. For services, prefer short-lived workload credentials, mTLS, or signed assertions over shared static passwords. Bootstrap credentials should be unique, limited, rotated during enrollment, and not recoverable from logs or backups in plaintext.

## Authorization model

Authorize at operation time using:

```text
subject + workload/device + action + resource + site/tenant
+ time/context + approval/safety state + policy version
```

Role-based access control (RBAC) is useful but broad roles such as `admin` or `operator` often combine viewing, export, credential management, firmware, and actuation. Add resource/site scope and operation-level permissions. For high-impact actions, require step-up authentication, dual authorization, a reason/ticket, and a bounded window where appropriate.

## OAuth and federated APIs

OAuth is an authorization framework, not a user-authentication protocol by itself. Follow [RFC 9700, OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700) for new deployments. Validate issuer, audience, signature/algorithm, time, client, scopes/claims, and token type. Prevent a token issued for one API, tenant, or environment from being accepted by another.

Keep access tokens short lived; protect refresh tokens; avoid tokens in URLs; do not log bearer tokens. For service-to-service access, bind credentials to a client where feasible and rotate keys without downtime.

SAML and OpenID Connect establish federated application identity under a configured trust relationship; SCIM provisions lifecycle state. Neither automatically grants local roles or physical access. See [enterprise federation with SAML and OpenID Connect](../02-protocols/infrastructure/enterprise-federation-saml-and-oidc.md) and [SCIM identity provisioning](../02-protocols/infrastructure/scim-identity-provisioning.md).

## Cross-device authentication and authorization

A cross-device flow starts an operation on one device and uses another device to authenticate or authorize it, often through a QR code, deep link, short code, proximity signal, or push. [RFC 10027](https://www.rfc-editor.org/info/rfc10027/) provides current IETF security guidance for these flows.

- Bind the secondary-device result to the exact initiating session, service, account, transaction, purpose, and short expiry.
- Show enough trusted context on the authorizing device for the person to detect a swapped session, wrong relying party, or different action.
- Use high-entropy, single-use initiation secrets; a displayed/scanned value must not become a reusable bearer credential.
- Treat QR, push, NFC, BLE, and apparent proximity as transport/discovery signals, not identity or consent by themselves.
- Prevent unsolicited prompts, cross-tenant session confusion, remote phishing, replay, and completion into an attacker-controlled browser.
- Give both devices an unambiguous completion/failure state and expire abandoned transactions.
- Keep the authenticated cross-device result separate from local authorization for site, resource, action, current safety state, and required approval.

WebAuthn/passkey cross-device use is covered in [WebAuthn, FIDO, and passkeys](../02-protocols/infrastructure/webauthn-fido-and-passkeys.md). A successful passkey ceremony can step up an operator session but is not a door credential or proof of physical presence.

## Physical-access identity

Distinguish:

```text
identity record -> credential assignment -> presentation
-> reader/device authentication -> controller/PACS decision
-> physical actuation -> sensed passage/door state -> audit event
```

Each stage has its own evidence. Anti-passback, occupancy, escort, schedule, area, risk, and offline rules can alter decisions. Do not reconstruct a person's location as fact from a single access-granted event.

## Lifecycle and break-glass

Automate joiner/mover/leaver changes with reconciliation and explicit ownership. Disable or rotate shared/service credentials when maintainers change. Break-glass access should be minimal, independently protected, tested through approved exercises, time bounded where possible, and always alerting/audited—without making emergency safety functions depend on unavailable enterprise identity.

## Audit

Record authenticated subject, acting workload/device, decision, policy/scopes, resource, tenant/site, source, time quality, correlation ID, result, and reason. Do not record authenticator secrets or unnecessary credential/personal data.

Apply this model through [identity, authentication, and authorization controls](../06-security-and-assurance/identity-authentication-and-authorization.md), and use [credentials and identity media](credentials-and-identity-media.md) for the physical credential path.

## Review checklist

- [ ] Person, credential, device, workload, session, and tenant identities are distinct
- [ ] Authentication assurance matches consequence and includes secure enrollment and recovery
- [ ] Authorization binds subject/workload, action, resource, tenant/site, context, and policy version
- [ ] OAuth token and federation issuer, audience, type, time, key, and scope/claim validation are explicit
- [ ] External groups/claims pass through scoped local role mapping rather than becoming permissions directly
- [ ] Cross-device flows bind both devices to the exact transaction and resist replay, swapping, and remote phishing
- [ ] Application identity and step-up remain separate from PACS/controller and physical-outcome decisions
- [ ] Joiner/mover/leaver, session revocation, break-glass, privacy, and audit ownership are defined
