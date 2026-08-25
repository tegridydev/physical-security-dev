---
title: Genetec Security Center SDK and Web API
summary: Publicly evidenced Genetec Security Center SDK, Web SDK, development programme, licence, media, and product-specific API boundaries.
page_type: vendor-api
domains: [video, access-control, integration]
tags: [genetec, security-center, web-sdk, platform-sdk, vms-sdk]
scope: global with product, programme, and licence differences
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public Genetec developer and technical documentation reviewed on 2026-08-25; full package contents, partner entitlements, exact SDK/product compatibility, API methods, licences, and deployment support require DAP and target-system confirmation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Genetec Security Center SDK and Web API

[Vendor APIs](../README.md) / [VMS and cloud video](README.md) / Genetec

Genetec documents a broad **Security Center SDK** for native platform integration and a separate **Web SDK** for HTTP-oriented applications. Product-specific web APIs, such as the Mission Control Web API, are separate contracts. Do not use “Genetec Web API” as if it names one universal endpoint set.

## Verified surface map

| Surface | Documented purpose | Access/licence boundary |
|---|---|---|
| Security Center SDK | Integrates video, access control, intrusion, ALPR and Security Center platform workflows | SDK package and development licence supplied through the Development Acceleration Program (DAP); deployment licences/features apply |
| Platform, Media, Workspace and Plugin samples | Illustrate distinct native integration areas | Public sample catalogue; full package and target compatibility remain DAP/product controlled |
| Security Center Web SDK | Platform/framework-neutral web access to many Security Center functions | Public overview; Web SDK option/licence and system configuration required |
| Web Player/media surfaces | Browser-oriented video/media integration | Separate media authorization, browser/codec and licence boundary |
| Mission Control Web API | Incident-management integration for Genetec Mission Control | Product-specific; not a synonym for Security Center Web SDK |

## Development programme and versions

The DAP description states that an SDK package includes documentation and samples and provides a one-year development licence. That development entitlement is not a production deployment licence and does not guarantee access to every product module.

The public sample catalogue includes .NET Framework 4.8 and .NET 8 sample sets. A public release page exists for the Security Center 5.13.1.0 SDK, while Genetec product documentation also contains later Security Center product lines. Therefore, do not call 5.13.1 “latest” or combine sample runtimes across releases. Pin the installed Security Center build, SDK package, target framework, architecture and applicable licence together.

## Capability and authority boundaries

Security Center unifies multiple physical-security domains, but authorization must remain domain- and action-specific:

- live view, playback, export, audio and camera/PTZ control;
- access-control identities, credentials, doors and commands;
- intrusion, alarms and acknowledgement;
- ALPR records and privacy-sensitive searches;
- configuration, federation and system administration;
- plug-in hosting and client workspace extension.

The Web SDK overview publicly describes high-impact capabilities including door operations. A web integration identity must not inherit broad operator rights merely for convenience. Require explicit site/entity scope, purpose and immutable command audit.

## Authentication and deployment

Use only identity modes documented for the exact Security Center/Web SDK release. Verify TLS and server identity, use unique non-human accounts where supported, store secrets in an approved vault and separate development from production credentials. Web browser clients should not receive a confidential client secret or unconstrained long-lived token.

For a native SDK application, follow the official connection, threading, object-lifetime and event-subscription contract. For an in-process plug-in, treat the host as a shared privileged process: bound work, fail closed, protect configuration and design uninstall/rollback. For Web SDK, enforce origin, session, CSRF and authorization controls in the application tier; the SDK does not replace application security.

## Events, media, and failure

Establish whether an event subscription is transient, resumable or replayable and how initial state is obtained. Preserve Genetec entity identity, source and ingest time, event ID/type and correlation. Reconcile after Directory failover, token expiry and connection loss.

Media viewing and evidence export are different workflows. Do not log or cache media session details indiscriminately, and do not present a convenience export as forensic evidence without the documented export/integrity path.

For a door, alarm or other high-impact command that times out, do not blindly retry. Query current state and audit history or require operator resolution; the first request may have succeeded.

## Lifecycle and compatibility

Review the SDK release notes, Security Center compatibility, licence options, known issues and DAP terms for each target. Public product guides are versioned; use the correct version selector rather than a search result from another release.

## Primary sources

- [Security Center SDK overview](https://developer.genetec.com/r/en-us/overview-of-the-security-center-sdk) — official platform scope.
- [Security Center SDK code samples](https://developer.genetec.com/r/en-us/security-center-sdk-code-samples) — integration areas and documented runtime sample sets.
- [What is included in the SDK package](https://developer.genetec.com/r/en-us/development-acceleration-program/what-is-included-in-the-sdk-package) — DAP package and development-licence boundary.
- [Web SDK overview](https://developer.genetec.com/r/en-us/overview-of-the-web-sdk) — web surface and capability scope.
- [Security Center SDK 5.13.1.0 release notes](https://developer.genetec.com/r/en-us/security-center-sdk-release-notes-5.13.1.0/what-s-new-in-the-security-center-5.13.1.0-sdk) — one fixed release, not a universal latest claim.
- [Security Center licence options](https://techdocs.genetec.com/r/en-US/Security-Center-Administrator-Guide-5.12/License-options-in-Security-Center) — versioned official evidence for Web SDK and Plugin SDK licence options.
- [Mission Control Web API overview](https://developer.genetec.com/r/en-us/overview-of-the-genetec-mission-controltm-web-api) — distinct product-specific surface.

## Related pages

- [PACS architecture](../../03-systems/access-control/pacs-architecture.md)
- [Evidence export and integrity](../../03-systems/video-surveillance/evidence-export-and-integrity.md)
- [API and event security](../../06-security-and-assurance/api-and-event-security.md)
