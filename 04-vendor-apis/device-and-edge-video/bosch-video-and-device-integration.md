---
title: Bosch Video and Device Integration
summary: Evidence-bounded map of Bosch and Keenfinity video SDK, device integration, download, and partner tooling surfaces.
page_type: vendor-api
domains: [video, integration]
tags: [bosch, keenfinity, video-sdk, device-api, integration-tools]
scope: global with regional portal and product differences
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: Public Bosch Security and Keenfinity catalogue, download, release, and partner material; SDK packages, exact APIs, current version claims, licences, product/build compatibility, and partner-only content are excluded.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Bosch video and device integration

[Vendor APIs](../README.md) / [Device and edge video](README.md) / Bosch and Keenfinity

Bosch Security video integration material is distributed across the Bosch Download Store, product documentation and current **Keenfinity** integration-tools pages. The ownership/branding transition makes source identity and date especially important. Use the current portal linked from the target product and retain the exact package/release letter used for a build.

## Verified surface map

| Surface | Publicly evidenced purpose | Access boundary |
|---|---|---|
| Video SDK | Native video/device integration used by Bosch tools and partner solutions | SDK/version appears in product release artefacts; package, runtime, licence and compatibility require current download/partner material |
| Device/firmware integration support | Device configuration, firmware and plug-in support delivered with Bosch tooling | Product and Configuration Manager release letters govern exact support |
| BVMS/integration SDK surfaces | VMS extensions and integrations | Distinct from device Video SDK; verify BVMS edition/build and developer entitlement |
| Integration tools | Access, intrusion, video and partner APIs/SDKs catalogued by Keenfinity | Some packages and powerful command capabilities are partner-only or licensed |
| Bosch Security API portal | Public catalogue for selected web-service/API initiatives | Individual API maturity and product scope apply; landing text is not an endpoint contract |

## Version evidence

A Bosch Configuration Manager 7.76 release letter dated 2025-09-15 listed **Video SDK 6.3** within that release context. This page does not claim Video SDK 6.3 is current for every product on 2026-08-25. The proper compatibility unit is the target device firmware, Configuration Manager/BVMS build, SDK package, architecture/runtime and any device-support package named by their release notes.

## Integration decision

1. Start with a standards-based interface such as declared ONVIF support when it satisfies the workflow.
2. Select a native device or Video SDK only when the required function and compatibility are explicitly supported.
3. Use a BVMS-specific extension only for BVMS-hosted workflows; do not assume its object model is a general device API.
4. Use a web-service API only when its official page identifies the target product, maturity, identity flow and lifecycle.

Avoid coupling an integration directly to an internal database, private DLL, browser call or reverse-engineered protocol because an official tool happens to use it.

## Authentication and privilege

Obtain the exact current hardening and API/SDK guide. Use TLS with validated device/server identity, unique workload accounts and least privilege. Keep live/playback/export, configuration, firmware, user administration, PTZ/audio and physical-output permissions separate where the product allows.

Some Bosch/Keenfinity integration SDKs outside video expose intrusion arm/disarm, silence and output control. Their official data sheets describe them as integration-partner and licensed capabilities. This catalogue does not transplant those privileges into the Video SDK; it flags why a generic “Bosch SDK account” must never be broadly authorized.

## Native SDK handling

- Verify publisher/signature and package origin.
- Pin architecture, runtime, redistribution and codec dependencies.
- Follow the documented object ownership, threading and callback lifetime rules.
- Bound media buffers, connections, event queues and reconnect work.
- Isolate native SDK failure from the application’s durable event and command state where practical.
- Log package and target build identifiers without recording credentials or media URLs.
- Re-test static compatibility on every device firmware, SDK and BVMS/Configuration Manager change.

## Lifecycle and support

Do not interpret a file’s presence in the Download Store as active support. Read its release letter and lifecycle/support statement. During the Bosch-to-Keenfinity documentation transition, prefer the current link supplied by the target product and note redirects or superseded branding in the project source record.

## Primary sources

- [Keenfinity integration tools](https://www.keenfinity-group.com/gb/en/partners/technology-partners/integration-tools/) — current official partner-tool catalogue.
- [Bosch Security Download Store](https://downloadstore.boschsecurity.com/) and [firmware catalogue](https://downloadstore.boschsecurity.com/?type=FW) — package and release-document route.
- [Configuration Manager 7.76 release letter](https://downloadstore.boschsecurity.com/FILES/Bosch_Releaseletter_ConfigManager_7.76.0050-bugfix.pdf) — dated evidence for one tool/Video SDK relationship.
- [Bosch Security API portal](https://api-dev.boschsecurity.com/) — official selected-API catalogue; inspect each API’s maturity and scope.
- [Intrusion Integration SDK data sheet](https://media.boschsecurity.com/fs/media/pb/media/partners_1/integration_tools_1/developer/INT-SDK_Intrusion_Integration_SDK_Datasheet.pdf) — official evidence of partner/licence and high-impact privilege boundaries outside the video scope.

## Related pages

- [ONVIF](../../02-protocols/video-and-media/onvif.md)
- [Native-library security guidance](../../05-development-and-integration/language-guides/cpp.md)
- [Asset and configuration inventory](../../07-operations-and-lifecycle/asset-and-configuration-inventory.md)
