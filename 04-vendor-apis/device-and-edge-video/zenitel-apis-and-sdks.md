---
title: Zenitel APIs and SDKs
summary: Evidence-bounded map of Zenitel ICX and AlphaCom VS-SDK, .NET libraries, licences, and older recording integration surfaces.
page_type: vendor-api
domains: [intercom, integration]
tags: [zenitel, icx, alphacom, vs-sdk, intercom-sdk]
scope: global with product-generation and licence differences
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Official Zenitel wiki pages reviewed on 2026-08-25; package availability, current support status, exact SDK methods, licences, ICX/AlphaCom compatibility, recorder versions, and deployment behavior require vendor confirmation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Zenitel APIs and SDKs

[Vendor APIs](../README.md) / [Device and edge video](README.md) / Zenitel

Zenitel’s public wiki documents several integration generations. The principal server integration described for AlphaCom/ICX is **VS-SDK**, with vendor .NET libraries and sample applications. A separate **Recorder 2.0 API** is documented as a licensed recording surface. Their age, product scope, licence and support status differ; do not combine them into one generic Zenitel API.

## Verified surface map

| Surface | Product scope documented | Public evidence/access boundary |
|---|---|---|
| VS-SDK for AlphaCom | AlphaCom and compatible ICX-500/ICX-Core deployments | Official wiki; SDK package 2.1.3.1 or later named on page; feature licences differ between ICX and AlphaCom |
| Stentofon .NET libraries | Managed integration libraries used with supported Zenitel services | Official wiki lists .NET Framework 4.6.2; current runtime/support must be confirmed |
| Recorder 2.0 API | Licensed recording integration using DLLs and sample application | Official but older product-specific page; treat as legacy until vendor confirms support |
| Current product/application APIs | Potentially product-specific ICX/Connect Pro and endpoint surfaces | Not sufficiently established by the reviewed public SDK pages; obtain current product documentation |

## Product and licence boundaries

The VS-SDK page states compatibility with ICX-500 and ICX-Core and explains that state retrieval is licensed, with differences between ICX and AlphaCom licence handling. The package number on that page is a minimum identified relationship, not a statement that every later package is compatible with every system release.

Before implementation, pin:

- ICX/AlphaCom server product and exact release;
- VS-SDK package and any service-provider component;
- required state/control/recording licence;
- .NET runtime, process architecture and supported operating system;
- endpoint types, intercom stations and redundancy topology;
- protocol/service connection mode and certificate/account support;
- vendor support status for Recorder 2.0 or any older DLL.

## State, events, and control

Intercom APIs can initiate or terminate calls, route audio, change station state, activate outputs or interact with emergency workflows depending on the licensed surface. Model every operation as one of observation, communication control, configuration or physical actuation, and authorize them independently.

For server state feeds:

- establish initial snapshot before applying deltas;
- preserve system/node identity and event time;
- detect reconnect, failover and stale state;
- bound callbacks and marshal work off SDK threads according to the official contract;
- reconcile active calls and outputs after connection loss;
- avoid recording sensitive call content or identifiers in diagnostic logs.

Never assume that a library return proves audible delivery, human acknowledgement, relay operation or emergency response.

## Native-library safety

Verify package publisher and licence, pin assembly versions, and isolate the integration service from operator clients where practical. Follow documented threading and object-disposal rules. Protect credentials in the platform secret store, use a distinct service identity, and do not grant general system control to a recorder-only integration.

If the product supports a secure transport or certificate configuration, use the current hardening guide. Do not infer TLS behavior from a .NET wrapper or expose a legacy raw service outside a segmented management conduit.

## Lifecycle and compatibility

`technology_status: mixed` reflects current ICX/AlphaCom integration alongside older Recorder 2.0 and .NET Framework-era material. Verify current supported replacements directly with Zenitel before starting a new project, and retain the exact wiki revision/package documentation used.

## Primary sources

- [VS-SDK for AlphaCom](https://wiki.zenitel.com/wiki/VS-SDK_for_AlphaCom) — official product, package and licence overview.
- [Zenitel SDK category](https://wiki.zenitel.com/wiki/Category%3ASDK) — official SDK catalogue.
- [Stentofon .NET libraries](https://wiki.zenitel.com/wiki/Stentofon_DotNet_Libraries) — documented managed-library runtime context.
- [Recorder 2.0 API](https://wiki.zenitel.com/wiki/Recorder_2.0_-_API) — separate licensed legacy recording surface.
- [Zenitel licences](https://wiki.zenitel.com/wiki/Licenses) — official licence reference route.

## Related pages

- [Intercom and emergency communications](../../03-systems/intercom-and-emergency-communications/README.md)
- [Remote access security](../../06-security-and-assurance/remote-access.md)
- [Reconnect, backpressure, and queues](../../05-development-and-integration/patterns/reconnect-backpressure-and-queues.md)
