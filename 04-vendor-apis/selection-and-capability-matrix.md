---
title: Vendor API Selection and Capability Matrix
summary: Cross-vendor comparison of deployment, integration surface, capability class, documentation access, and evidence limits.
page_type: reference
domains: [integration, cross-domain]
tags: [vendor-selection, capability-matrix, api, sdk]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: Capability-level comparison from official material reviewed on 2026-08-25; cells do not assert endpoint parity, licence inclusion, product compatibility, or availability in every region.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Vendor API selection and capability matrix

[Vendor APIs](README.md) / Selection and capability matrix

Use this matrix to shortlist a surface, then read its vendor page and current official contract. “Documented” means the vendor publicly establishes the capability class; it does not mean every operation is available to every product, account, licence, or role.

## Device and edge video

| Vendor family | Primary deployment | Documented native surfaces | Capability classes evidenced | Documentation/package access | Grade |
|---|---|---|---|---|---|
| [Axis](device-and-edge-video/axis-vapix-and-acap.md) | Device and on-device app | VAPIX; Device Configuration APIs; ACAP | Discovery, configuration, media/events/I/O by API family, application lifecycle, edge apps | Core docs public; SDK public; model/OS/API compatibility applies | V2 |
| [Hikvision](device-and-edge-video/hikvision-isapi-and-heop.md) | Device and on-device app | ISAPI; HEOP | Cross-product HTTP integration; embedded applications | TPP registration/login and restricted material for normative guides | V1 |
| [Dahua](device-and-edge-video/dahua-cgi-and-netsdk.md) | Device and native client SDK | CGI; NetSDK | Device integration, events/media/control by product/package | Public product/release evidence; current complete contracts are not consistently public | V1 |
| [Hanwha Vision](device-and-edge-video/hanwha-sunapi-and-open-platform.md) | Device and on-camera app | SUNAPI; SUNAPI SDK; Open Platform SDK | Device integration and edge applications; exact functions model-specific | Product pages public; SDK/guides commonly STEP account-gated | V1 |
| [Bosch / Keenfinity](device-and-edge-video/bosch-video-and-device-integration.md) | Device, VMS component, native SDK | Video SDK and integration tools | Video/device integration and plug-in tooling | Portals public at catalogue level; packages, licences, compatibility can be partner/download gated | V1 |
| [2N](device-and-edge-video/2n-http-and-platform-apis.md) | Intercom/access device and management server | 2N IP HTTP API; Access Commander API; selected platform APIs | Status, events, configuration and device functions; access/intercom actuation where enabled | Manuals and API references public; feature/licence/model gates apply | V2 |
| [Zenitel](device-and-edge-video/zenitel-apis-and-sdks.md) | Intercom server/client integration | VS-SDK; .NET libraries; recorder interface | ICX/AlphaCom state and control; recording integration | Official wiki public; binaries/features/licences and lifecycle vary | V1 |

## VMS and cloud video

| Vendor family | Primary deployment | Documented native surfaces | Capability classes evidenced | Documentation/package access | Grade |
|---|---|---|---|---|---|
| [Milestone](vms-and-cloud-video/milestone-mip-sdk-and-api-gateway.md) | On-premises VMS and gateway | MIP SDK; protocol APIs; API Gateway REST | Configuration, events/alarms, messaging, control, media/metadata, plug-ins | Documentation public; product/licence and installed environment required | V2 |
| [Genetec](vms-and-cloud-video/genetec-security-center-sdk-and-web-api.md) | On-premises Security Center | Security Center SDK; Web SDK; product-specific web APIs | Video, access, intrusion, ALPR, events, media and platform extensions | Overview public; DAP membership, package and licences for development/deployment | V2 |
| [Network Optix](vms-and-cloud-video/network-optix-nx-meta-apis-and-sdks.md) | Nx Meta/OEM VMS | Server REST API; C++ plug-in SDK; Cloud API; open-source client | Resource/user administration, media, events/rules, PTZ, server plug-ins | Core docs public; account/program, developer licences and build compatibility apply | V2 |
| [Motorola Solutions / Avigilon](vms-and-cloud-video/motorola-avigilon-integration-surfaces.md) | Unity, Alta and product-specific platforms | Developer-program and product-specific web/REST/SDK surfaces | Video, access, alarms, web endpoint and partner integration surfaces by product | Public catalogue is fragmented; detailed contracts and entitlements often partner/product gated | V1 |
| [Eagle Eye Networks](vms-and-cloud-video/eagle-eye-video-api.md) | Cloud VMS | Video API v3 | Cameras, live/recorded media, events, alerts, SSE/webhooks | Docs public; developer account, OAuth client and customer authorization required | V2 |
| [Verkada](vms-and-cloud-video/verkada-command-apis.md) | Multi-region cloud platform | Command APIs and webhooks | Camera, access and other product APIs; token, pagination and limit contract | Reference public; organization, region, permissions and product subscription required | V2 |

## Access and identity

| Vendor family | Primary deployment | Documented native surfaces | Capability classes evidenced | Documentation/package access | Grade |
|---|---|---|---|---|---|
| [HID Origo](access-and-identity/hid-origo-and-mobile-access.md) | Cloud identity and mobile credentials | Mobile Identities; User/Credential Management; Events; mobile SDK ecosystem | User and digital-credential lifecycle, callbacks, wallet/app provisioning | API docs public but intended for enrolled technology partners; credentials from HID | V2 |
| [Gallagher](access-and-identity/gallagher-command-centre-integrations.md) | On-premises Command Centre, optional cloud gateway | REST API families; controller interfaces; Video Viewer and Mobile Connect SDKs | Cardholders, events/alarms, status, overrides, inbound events, mobile credentials | Product summaries public; guides, token, demo licence and endorsement workflow partner-gated | V1 |
| [LenelS2](access-and-identity/lenels2-onguard-openaccess-and-elements.md) | OnGuard on-prem/cloud; Elements SaaS | OpenAccess Web Services and partner interfaces | OnGuard data, event and command integrations; Elements connector evidenced separately | Detailed docs/packages through LenelS2 Connect; Elements developer API not publicly established here | V1 |
| [Johnson Controls C•CURE](access-and-identity/johnson-controls-ccure-integrations.md) | On-premises C•CURE 9000/victor | Product SDK/web-service and licensed integration surfaces | Personnel, devices, alarms, command and platform integrations by package | Public product/integration docs are partial; developer packages/licensing require vendor channel | V1 |
| [SALTO](access-and-identity/salto-apis.md) | KS cloud, Nebula cloud, Space on-premises | KS Connect/Core; Nebula; Space Hospitality; SHIP | Identity/access lifecycle, locks, events and credentials by platform | Cloud API references public; client credentials from SALTO; SHIP licensed and NDA-gated | V2 |
| [Brivo](access-and-identity/brivo-api.md) | Cloud access platform | Brivo Access API | Sites, users, credentials, doors, events and high-impact commands | Documentation public; developer portal and customer-specific app credentials required | V2 |
| [Suprema](access-and-identity/suprema-biostar-2-api.md) | On-premises BioStar 2 | New Local API; separate Device SDK and TA API | Users, credentials, doors, devices, events, biometrics and administration | API collection/support docs public; exact server/API version and licence determine availability | V2 |
| [Kisi](access-and-identity/kisi-api.md) | Cloud access platform and mobile SDK | JSON API; webhooks; iOS/Android SDKs | Users, access rights, locks, unlocks, events and embedded mobile access | API reference public; sandbox/partner ID and SDK access require vendor onboarding | V2 |

## Selection tests

Before selecting a surface, answer all of these:

| Test | Required evidence |
|---|---|
| Authority | Which installed product or cloud tenant is authoritative for identities, configuration, events, media, and physical state? |
| Direction | Is the integration observing, provisioning, subscribing, embedding media, hosting a plug-in, or commanding a device? |
| Entitlement | Which account, partner agreement, licence, subscription, role, scope, and site/tenant permission enables it? |
| Compatibility | Which exact product build, API/SDK version, firmware, model, architecture, runtime, and region are supported together? |
| Security | How are clients enrolled, secrets/certificates rotated, privileges bounded, callbacks authenticated, and audit records correlated? |
| Failure | What happens on timeout, token expiry, reconnect, duplicate event, lost callback, server failover, cloud outage, and uncertain command outcome? |
| Lifecycle | Where are release notes, deprecation notices, security advisories, and support windows published? |
| Safety | Can the surface unlock, override, activate output, issue/revoke a credential, alter alarm behavior, expose audio/video, or process biometrics? |

## What cannot be compared safely in one cell

Endpoint counts, “RESTful” labels, nominal API versions, and SDK download availability are poor proxies for integration quality. Compare the exact workflow: authorization depth, event durability, media transport, reconciliation, offline behavior, audit quality, compatibility policy, and vendor support. See [retries and idempotency](../05-development-and-integration/patterns/retries-timeouts-and-idempotency.md) and [polling, subscriptions, and reconciliation](../05-development-and-integration/patterns/polling-subscriptions-and-state-reconciliation.md).

