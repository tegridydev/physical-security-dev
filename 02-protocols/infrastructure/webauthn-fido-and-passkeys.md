---
title: "WebAuthn, FIDO, and passkeys"
summary: "Standards-aware guidance for WebAuthn registration and authentication, FIDO authenticators, passkeys, cross-device flows, recovery, and physical-security administration."
page_type: protocol
domains: [identity, cross-domain]
tags:
  - webauthn
  - fido2
  - passkeys
  - phishing-resistant-authentication
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "Web Authentication: An API for accessing Public Key Credentials Level 2"
  - "Web Authentication: An API for accessing Public Key Credentials Level 3, Candidate Recommendation"
  - "FIDO CTAP 2.3 Proposed Standard"
  - "FIDO CTAP 2.3.1 Working Draft"
  - "RFC 10027 / BCP 247: Best Current Practice for Security of Cross-Device Flows"
coverage_limit: "WebAuthn/FIDO application authentication guidance; authenticator certification, enterprise attestation policy, identity proofing, account recovery, browser/platform behavior, and physical credential decisions require a deployment profile."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# WebAuthn, FIDO, and passkeys

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / WebAuthn, FIDO, and passkeys

Web Authentication (WebAuthn) lets a relying party authenticate users with origin-bound public-key credentials through a user agent and authenticator. FIDO Client to Authenticator Protocol (CTAP) defines communication between a platform/client and external or platform authenticators. “Passkey” commonly describes a discoverable FIDO credential that may be device-bound or available across a provider ecosystem. [WEBAUTHN-2] [FIDO-23]

These technologies can strongly protect administrative sign-in. They do not identify a person without an enrollment/proofing process, decide what the person may do, or act as a physical PACS credential merely because an authenticator uses biometrics, NFC, BLE, or a secure element.

## Standards status

Status labels matter when writing procurement requirements or compatibility claims.

| Document | Status used here | Engineering treatment |
|---|---|---|
| Web Authentication Level 2 | W3C Recommendation; final published baseline | Suitable normative baseline where required features are supported |
| Web Authentication Level 3 | W3C Candidate Recommendation Snapshot dated 2026-05-26, not a final Recommendation | Track and test selected features; do not claim final Level 3 conformance |
| CTAP 2.3 | FIDO Alliance Proposed Standard dated 2026-02-26 | Pin authenticator/client feature support and certification claims independently |
| CTAP 2.3.1 | FIDO Alliance Working Draft dated 2026-05-29, non-final | Do not make a production requirement without an explicit draft/adoption policy |
| RFC 10027 / BCP 247 | Published IETF Best Current Practice for cross-device-flow security | Apply to initiation, user context, phishing resistance, and transaction binding |

WebAuthn and CTAP revisions are related but have separate status, implementation, and certification lifecycles. A browser supporting a WebAuthn feature does not prove every authenticator/CTAP transport supports the corresponding capability. [WEBAUTHN-3] [FIDO-23] [FIDO-231]

## Architecture and trust boundaries

```text
relying-party server
  <-> HTTPS origin and user agent
       <-> platform WebAuthn implementation
            <-> platform or roaming authenticator via CTAP/platform API
```

- The **relying party (RP)** defines the RP ID, allowed origins, account binding, challenge, credential policy, and server-side verification.
- The **client/user agent** mediates the WebAuthn ceremony and reports client data including challenge, origin, and ceremony type.
- The **authenticator** creates and uses a credential scoped to the RP ID, performs user presence and possibly user verification, and returns authenticator data plus an attestation statement or assertion signature.
- The **identity/lifecycle system** determines who may enroll, how accounts are recovered, and when credentials and sessions are revoked.
- The **application authorization layer** decides which tenant, site, resource, and operation an authenticated account may access.

Authentication success means the presented credential satisfied the RP’s ceremony policy. It does not prove the operator’s current employment, physical location, intent, or authority for a specific unlock, lockdown, evidence export, credential issuance, or configuration change.

## Registration ceremony

The server should create registration options for an already authenticated, authorized enrollment context. Bind the ceremony to the intended account and session.

### Server-side registration checks

1. Generate an unpredictable, single-use challenge and retain its account/session/purpose/expiry binding.
2. Set the expected RP ID and user identity; keep the stable user handle opaque and free of unnecessary personal data.
3. Choose authenticator attachment, discoverable-credential, user-verification, attestation, and algorithm policy deliberately.
4. On response, parse with strict size/shape limits and reject duplicate security-critical members.
5. Verify client-data type, challenge, and exact allowed origin.
6. Verify RP ID hash, required user-presence/user-verification flags, and ceremony-specific authenticator data.
7. Validate the attestation statement only to the level required by policy; otherwise apply the selected privacy-preserving attestation conveyance policy.
8. Confirm the public-key algorithm is allowlisted and store the credential ID, public key, user handle/account, sign count where used, transports as hints, backup-related state where available, and policy evidence.
9. Prevent credential-ID collision/account confusion and audit enrollment without storing reusable ceremony secrets.

Do not allow a session authenticated only with a weak or recovered factor to silently enroll a stronger credential without step-up and notification appropriate to the account’s consequence.

## Authentication ceremony

For authentication, issue a new bounded challenge and verify the returned assertion at the server.

- Match the response to the intended RP, account/discoverable-login context, session, purpose, and expiry.
- Verify `type`, challenge, and exact origin in client data.
- Verify RP ID hash and required user-presence/user-verification flags.
- Select the stored public key by credential ID under the correct tenant/RP/account relationship.
- Verify the signature over the prescribed authenticator-data and client-data-hash construction.
- For discoverable credentials, validate the returned user handle under the RP’s account-mapping rules.
- Process signature-counter behavior according to authenticator capabilities; a non-incrementing counter is not by itself proof of cloning, and an unexpected regression needs risk handling rather than an unsafe universal response.
- Consume the challenge once, even when later authorization fails.

Create a new application session after success. Authentication does not remove the need for secure session cookies, CSRF protection, reauthentication, authorization, rate limits, and audit.

## RP ID, origin, and domain governance

WebAuthn phishing resistance depends heavily on browser enforcement plus correct RP/origin configuration.

- Maintain an exact allowlist of HTTPS origins; development and production origins are separate trust domains.
- Choose the RP ID at the narrowest domain scope that supports the intended applications. A broad registrable-domain RP ID can expand which compromised subdomains matter.
- Protect DNS, domain registration, TLS, reverse proxies, redirects, hosting, and all origins allowed to initiate ceremonies.
- Do not accept an origin because it ends with a trusted string; parse and compare scheme, host, and port under Web origin rules.
- Treat native-application and related-origin features as explicit profiles with platform/version testing and change control.
- Reassess credentials before domain migration, merger, tenant split, or relying-party rebranding; RP ID binding is intentional and cannot be wished away by redirect.

## User presence, user verification, and biometrics

**User presence (UP)** indicates that the authenticator performed a user-presence test, commonly through an explicit gesture. **User verification (UV)** indicates that the authenticator locally verified the user through a configured method such as a PIN or biometric. The RP must request and check the policy it requires.

WebAuthn normally receives a UV result, not a raw biometric. A platform biometric used to unlock a passkey is not the same system, template, assurance, liveness, retention regime, or legal purpose as a PACS biometric reader. Keep them in separate privacy, assurance, and lifecycle assessments.

UV does not identify which authorized person used a shared device unless enrollment and device/account policy establish that relationship. User presence alone does not prove informed approval of the application transaction.

## Passkeys and credential characteristics

A passkey may be:

- a discoverable credential usable in usernameless/identifier-first experiences;
- bound to one authenticator/device;
- backed up or synchronized within a platform/provider ecosystem;
- usable through cross-device/hybrid authentication without being copied into the initiating device.

Do not infer device-bound hardware assurance merely from the word “passkey.” If policy differentiates device-bound and backed-up credentials, use defined WebAuthn flags/metadata and product support; document what happens when the information is absent or changes.

Synchronization can improve recovery and multi-device usability but moves assurance into the provider account, device enrollment, sync encryption, recovery, and ecosystem controls. A hardware security key may offer different portability and recovery properties. Provide more than one approved authenticator for privileged accounts so loss does not force a weak emergency bypass.

## Attestation and authenticator policy

Attestation can provide evidence about an authenticator model or provenance under a selected format and trust policy. It is optional in many deployments and can create privacy/correlation and operational risks.

- Define whether no attestation, self/none, indirect, direct, or enterprise attestation is acceptable.
- Validate the complete attestation format and trust chain when a policy depends on it.
- Maintain metadata/trust-anchor update, revocation/status, model allow/deny, and rollback procedures.
- Do not treat attestation as proof of the person’s identity or current device health.
- Plan for model retirement and replacement without locking operators out.
- Minimize persistent authenticator identifiers; enterprise attestation needs explicit governance and user/workforce notice.

FIDO certification, authenticator metadata status, platform support, and an organization’s risk acceptance are separate facts. Record each rather than collapsing them into “FIDO compliant.”

## CTAP and authenticator management

CTAP covers client-to-authenticator operations and transports. It does not authorize the relying-party application.

- Establish an approved authenticator inventory and ownership/replacement process.
- Require appropriate authenticator PIN/UV and retry/lockout policy; protect against shoulder-surfing and help-desk social engineering.
- Bound resident/discoverable credential capacity and handle storage-full conditions safely.
- Control enterprise attestation, credential management, reset, and firmware/update capabilities.
- Treat USB, NFC, BLE, and hybrid transport availability as attack-surface and usability decisions; disable only with tested recovery alternatives.
- A factory reset can remove credentials but does not close application sessions or prove provider-synchronized copies are unavailable.

Transport presence—especially BLE or NFC proximity—is not sufficient transaction or operator authorization.

## Cross-device authentication

Cross-device flows let an operation initiated on one device be authorized or authenticated using another. RFC 10027 documents security guidance for these flows. [CROSS-DEVICE]

- Clearly identify the initiating service, target account, and action on the authorizing device.
- Bind the secondary-device result cryptographically and temporally to the exact initiating transaction.
- Use high-entropy, short-lived, single-use secrets; never encode bearer authorization into a reusable QR code.
- Prevent session swapping, remote phishing, unsolicited prompts, and acceptance into the wrong browser/session.
- Treat QR, BLE/proximity, deep links, and push notifications as transport/discovery signals—not standalone identity proof.
- Avoid exposing QR codes or recovery artifacts on monitored displays, support captures, recordings, or screen-sharing sessions.
- Expire abandoned initiations and show both devices an unambiguous completion/failure state.

For a high-impact physical-security action, cross-device authentication can be a step-up factor but must still bind the local authorization decision to tenant, resource, operation, prerequisites, reason, and expiry.

## Account recovery and lifecycle

The weakest recovery path often controls the effective assurance of the account.

- Enroll at least two approved authenticators or a governed recovery method for privileged operators.
- Require strong verification and independent notification before adding or replacing authenticators.
- Rate-limit and delay high-risk recovery where operationally acceptable; protect against help-desk impersonation.
- Let users and administrators view credential creation/last-use/type information without exposing tracking-sensitive details.
- Revoke lost credentials, active sessions, refresh tokens, application passwords, and recovery artifacts as separate actions.
- Define joiner/mover/leaver and role-change propagation from the authoritative identity source.
- Retain security audit evidence according to policy after credential deletion without retaining unnecessary personal data.

If the identity provider or passkey ecosystem is unavailable, preserve an engineered local recovery path for authorized administration. Never make certified egress or life-safety operation depend on WebAuthn availability.

## Physical-security application profile

Recommended uses include operator sign-in, privileged administration, evidence export approval, credential-management step-up, and access to cloud management consoles. Keep application authentication separate from physical credential presentation:

```text
WebAuthn assertion -> operator application session
  -> application authorization for a scoped operation
  -> separately governed PACS/VMS/alarm request
  -> downstream acknowledgement and observed outcome
```

A WebAuthn authenticator is not automatically an OSDP smart-card credential, mobile access key, door token, or proof that a person passed through a portal. Likewise, WebAuthn success must not directly trigger a relay or unlock without the application’s high-impact command controls.

## Privacy, logging, and monitoring

Log account/tenant, credential record ID in an internal non-public form, ceremony type, RP/origin decision, UP/UV policy result, attestation policy outcome, authenticator metadata/policy revision where relevant, recovery/admin actor, session/correlation ID, and authorization outcome. Do not log challenges before expiry, client data wholesale, assertion signatures, credential public-key material unnecessarily, PINs, biometric data, QR contents, or session tokens.

Monitor enrollment and deletion, repeated challenge failures, origin/RP mismatch, signature failure, unknown credential IDs, abnormal recovery, metadata-status changes, privileged step-up failure, and credentials used after reported loss.

## Review checklist

- [ ] Normative baseline identifies WebAuthn Level 2 versus non-final Level 3 and exact CTAP status
- [ ] RP ID and allowed origins are minimal, exact, governed, and protected with DNS/TLS/hosting controls
- [ ] Registration challenge, account/session binding, algorithm, attestation, UP/UV, and credential storage policy defined
- [ ] Authentication verifies type, challenge, origin, RP ID hash, flags, user handle, signature, and replay
- [ ] Discoverable, device-bound, backed-up/synchronized, and cross-device credential behavior distinguished
- [ ] Attestation, metadata, certification, revocation/status, privacy, and model retirement governed
- [ ] Recovery is no weaker than intended assurance; multiple authenticators and session/token revocation are addressed
- [ ] Cross-device flow binds the authorizing device to the exact initiating context and resists phishing/session swapping
- [ ] WebAuthn authentication kept separate from local role, object/action, PACS, and physical-outcome authorization
- [ ] Logs exclude ceremony secrets, tokens, biometric data, and tracking-sensitive authenticator details

## Sources

- **WEBAUTHN-2** — [Web Authentication: An API for accessing Public Key Credentials Level 2][WEBAUTHN-2], W3C Recommendation.
- **WEBAUTHN-3** — [Web Authentication: An API for accessing Public Key Credentials Level 3][WEBAUTHN-3], W3C Candidate Recommendation Snapshot, 26 May 2026; non-final.
- **FIDO-23** — [FIDO Alliance specifications: CTAP 2.3 Proposed Standard][FIDO-23], FIDO Alliance, 2026-02-26.
- **FIDO-231** — [Client to Authenticator Protocol 2.3.1 Working Draft][FIDO-231], FIDO Alliance, 2026-05-29; non-final.
- **CROSS-DEVICE** — [RFC 10027 / BCP 247: Best Current Practice for Security of Cross-Device Flows][CROSS-DEVICE], IETF, August 2026.

[WEBAUTHN-2]: https://www.w3.org/TR/webauthn-2/
[WEBAUTHN-3]: https://www.w3.org/TR/webauthn-3/
[FIDO-23]: https://fidoalliance.org/specs/fido-v2.3-ps-20260226/
[FIDO-231]: https://fidoalliance.org/specs/fido-v2.3.1-wd-20260529/fido-client-to-authenticator-protocol-v2.3.1-wd-20260529.html
[CROSS-DEVICE]: https://www.rfc-editor.org/info/rfc10027/
