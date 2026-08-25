---
title: Cloud, Mobile, and Multi-Tenant Security Platforms
summary: Shared-responsibility, tenant-isolation, edge-dependency, mobile-client, privacy, resilience, and exit architecture for hosted physical security.
page_type: system
domains: [integration, infrastructure, operations, identity]
tags: [cloud-platforms, mobile-clients, multi-tenancy, shared-responsibility, edge]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [NIST SP 800-207, NIST SP 800-207A]
coverage_limit: Vendor-neutral architecture only; no service availability, data-residency, certification, mobile-platform, offline, or product security claim without current provider and deployment evidence.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Cloud, mobile, and multi-tenant security platforms

Hosted platforms move management, identity, media, events, analytics, notifications, and support across provider and customer boundaries. They do not move all responsibility to the provider. Document which functions remain at the edge, which require the service, and which physical operations must remain safe during loss.

## Deployment model

```text
field devices/controllers
 -> edge gateway/recorder/cache and local authority
 -> outbound service connection/API
 -> regional/global control, data, media, analytics, notification planes
 -> browser/mobile clients and third-party integrations
```

Map every plane independently: identity, management, configuration, events/state, video/audio, analytics, commands, firmware/update, support, telemetry, backup/export, billing/licensing, and push notification. Region or tenant selection in one plane may not determine storage or processing in every other plane.

## Shared-responsibility record

For each control state provider, customer, integrator, device/vendor, carrier, and application-store responsibilities. Cover:

- workforce and workload identity, federation, MFA/passkeys where supported, recovery, and offboarding;
- endpoint/controller enrollment, keys/certificates, firmware, hardening, replacement, and physical protection;
- tenant/site/role configuration, privileged support, API clients, secrets, and integrations;
- networking, egress, DNS/time, proxies, edge availability, and bandwidth;
- logging, detection, incident communication, evidence access, and regulatory requests;
- data location, sub-processors, retention/deletion, backup, export, and service termination.

Provider certification or a secure architecture does not prove the customer's tenant configuration or every connected device is secure.

## Tenant and site isolation

Isolation must cover identifiers, authorization decisions, search indexes, media URLs, caches, exports, analytics jobs/models, notifications, maps, rules, reports, audit, support tooling, API rate limits, backups, and deletion—not only database rows.

Use non-guessable identifiers as defense in depth, never as authorization. Enforce identity and resource authorization on every service request. Test delegated administration, cross-site roles, integrator/MSP access, user moves between tenants, support impersonation, share links, exports, and deprovisioning under an authorized process.

NIST [SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) frames zero trust as removing implicit trust based on network location. [SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final) applies zero-trust access-control concepts to cloud-native applications across on-premises and multiple cloud environments. These publications guide architecture; they do not certify a service.

## Edge and offline operation

Define local operation for WAN/service/DNS/identity/licensing failure: door decisions and cached entitlements, alarm generation/transmission, recording, intercom calls, gate safety, configuration changes, event queueing, local users, and emergency/native controls. State capacity, expiry, clock dependency, security trade-offs, and reconciliation.

Avoid designs where loss of cloud silently disables essential local security or life-safety-related operation. Conversely, long-lived offline credentials or stale allowlists can preserve access after revocation. Make the chosen risk explicit and expose offline age.

Recovery must handle duplicate/out-of-order events, conflicting configuration, revoked identities, certificate expiry, queued commands, daylight/time changes, and storage exhaustion. A reconnected icon does not prove complete reconciliation.

## Mobile clients

Mobile devices add screen capture, local caches, biometric/PIN unlock, OS backup, push service, deep links, malicious overlays, device compromise, shared devices, SIM/number changes, roaming, and app-store update dependencies.

- Keep server-side authorization authoritative; do not trust hidden UI controls.
- Bind enrollment to a named user and managed recovery/revocation process.
- Minimize and protect cached video, audio, credentials, visitor and location data.
- Define session lifetime, reauthentication for high-impact actions, device/app integrity signals, and lost-device response.
- Treat a push notification as best-effort signalling, not alarm delivery, acknowledgement, or response.
- Show source, tenant/site, live/recorded/stale state, time, and requested-versus-observed physical outcome.
- Constrain remote unlock, gate, PTZ, alarm, audio, export, and administration rights separately.

## Data governance and provider operations

Document purpose and legal basis, capture boundary, region/location, transfers, sub-processors, support access, encryption and key responsibility, retention per data class, legal hold, export, deletion verification, and breach/incident notification. Video, biometrics, plates, access events, voice, device location, and identity graphs can require different controls.

Review provider release/change practices, status/incident channels, vulnerability handling, dependency/SBOM evidence where available, administrator notifications, API/profile lifecycle, mobile minimum OS, device end-of-support, and emergency change process. “Evergreen” does not remove change management.

## Resilience and exit evidence

- provider and customer dependency graph with documented native edge behavior;
- regional/service/identity/push/WAN failure, degradation, and recovery semantics;
- tenant/site isolation and privileged support audit;
- event/media/configuration queue limits and gap visibility;
- backups and export in documented usable formats, including identities and audit;
- certificate/key rotation, device transfer, ownership change, and provider termination;
- a tested migration/exit plan that does not rely on a discontinued service remaining available.

Record deployment-specific provider evidence for tenant isolation, regional processing, identity and key lifecycle, backup/restore, outage handling, export, deletion, and exit portability.

See [Integration platforms](README.md), [Offline operation and anti-passback](../access-control/offline-operation-and-anti-passback.md), and [VMS, NVR, and VSaaS](../video-surveillance/vms-nvr-and-vsaas.md).
