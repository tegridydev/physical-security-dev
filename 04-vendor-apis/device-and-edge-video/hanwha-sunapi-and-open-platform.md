---
title: Hanwha Vision SUNAPI and Open Platform
summary: Evidence-bounded guide to Hanwha Vision SUNAPI device integration, partner SDK distribution, and supported on-camera Open Platform applications.
page_type: vendor-api
domains: [video, access-control, integration]
tags: [hanwha-vision, sunapi, open-platform, edge-applications, device-sdk]
scope: global with STEP regional portal differences
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public Hanwha Vision product and STEP pages establish the surfaces; current complete SUNAPI/Open Platform packages, universal version claims, model matrices, operations, authentication, and licences are excluded where login-gated.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Hanwha Vision SUNAPI and Open Platform

[Vendor APIs](../README.md) / [Device and edge video](README.md) / Hanwha Vision

Hanwha Vision documents **SUNAPI** as a native HTTP API family and distributes related SDK material through its STEP partner/support environment. **Open Platform** is the separate on-camera application framework for supported models. Public product pages often identify which of these are present; the exact guide and SDK package remain the implementation authority.

## Verified surface map

| Surface | Purpose | Access/evidence boundary |
|---|---|---|
| SUNAPI HTTP API | Native device integration for supported cameras, recorders and access products | Model pages and STEP catalogue public; exact operation and version guide can require STEP login |
| SUNAPI SDK | Vendor development package for supported integration workflows | Distributed through STEP download/support routes; package compatibility must be pinned |
| Open Platform SDK | Builds applications that execute on compatible Hanwha network cameras | Public overview; SDK, model/firmware/toolchain and resource contract through STEP |
| ONVIF profiles | Standards-based media/device interoperability on conformant models | Separate from SUNAPI and Open Platform; use exact declaration/model support |

## Version evidence

On 2026-08-25, the STEP technical-support page listed a **SUNAPI v2.6.8 access-control API guide** dated 2026-04-09. That is evidence for the named access-control document only. It must not be described as the universal latest SUNAPI for cameras, recorders or every region.

Public camera product pages reviewed for this catalogue listed combinations of ONVIF, SUNAPI HTTP API and Open Platform. Availability varies by model and firmware. Capture the product page, firmware release note, API guide revision and SDK package manifest in the project inventory.

## Choosing a surface

- Use declared ONVIF profiles when the required cross-vendor feature is standardized and conformant.
- Use SUNAPI when an officially documented native capability is required and the exact device exposes it.
- Use the SUNAPI SDK when the vendor package provides supported higher-level media/event/device behavior that a direct HTTP integration should not reproduce.
- Use Open Platform only for logic that genuinely must run at the edge and fits the device’s supported application and resource model.

Do not treat the legacy ActiveX route found in old examples as the preferred architecture. Hanwha’s official STEP FAQ directs developers toward the SUNAPI SDK instead of older ActiveX support.

## Authentication, events, and commands

Take authentication, HTTPS, certificate, role and session behavior from the exact current guide and firmware. Product pages advertising HTTPS or security properties are capability evidence, not a universal auth contract. Provision a unique least-privileged account and do not accept plaintext fallback or permanent certificate exceptions.

For events, document subscription/stream framing, heartbeat, reconnect, duplicate/gap behavior, source timestamps and schema version. For media, pin profile, codec, transport, session lifetime and concurrent-stream limits. For access-control, PTZ, audio, I/O, restart, firmware and configuration operations, require separate authorization and post-operation reconciliation.

## Open Platform boundary

An on-camera application can affect availability, privacy and evidence. Before deployment, verify:

- compatible camera models, firmware, architecture and SDK/toolchain;
- application signing/approval and distribution route;
- documented APIs and permissions;
- CPU, accelerator, memory, storage, process and network limits;
- start/restart behavior and coexistence with recording/analytics;
- secure secret storage, update, rollback and removal;
- support policy when multiple third-party applications share a device.

Never use an undocumented operating-system interface simply because it is visible inside an application environment.

## Lifecycle and compatibility

STEP has regional/localized portals and account-controlled downloads. Re-check the correct region, product family, document date, licence and firmware release before implementation. Keep restricted packages and documents under their portal terms.

## Primary sources

- [Hanwha Vision STEP technical support](https://step.hanwhavision.com/kr/tech-support) — official document catalogue and dated access-control SUNAPI guide evidence.
- [STEP Download Center](https://step.hanwhavision.com/kor_EN/HelpDesk/Download_center.aspx) — account/download route for SUNAPI and Open Platform SDK material.
- [STEP Open Platform](https://step.hanwhavision.com/kor_EN/OpenPlatform/OpenPlatform.aspx?2=) — official on-camera framework overview.
- [STEP FAQ](https://step.hanwhavision.com/fra_FR/HelpDesk/FAQ_List.aspx) — official SDK-download and ActiveX-support direction.
- [Example Hanwha camera product page](https://hanwhavisionamerica.com/product/qno-8020r/) — model-level API/profile declarations; do not generalize to other products.

## Related pages

- [ONVIF](../../02-protocols/video-and-media/onvif.md)
- [Secure system baselines](../../06-security-and-assurance/secure-system-baselines.md)
- [Firmware and supply chain](../../06-security-and-assurance/firmware-updates-and-supply-chain.md)
