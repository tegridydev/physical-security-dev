---
title: Dahua CGI and NetSDK
summary: Bounded catalogue of Dahua device CGI integration and native NetSDK surfaces using public product and release evidence.
page_type: vendor-api
domains: [video, access-control, integration]
tags: [dahua, cgi, netsdk, device-api, native-sdk]
scope: global with product and regional documentation differences
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public Dahua product, integration, and release artefacts establish CGI and NetSDK but do not provide a single current public normative contract; endpoints, authentication details, package compatibility, versions, and product support are intentionally excluded.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Dahua CGI and NetSDK

[Vendor APIs](../README.md) / [Device and edge video](README.md) / Dahua

Dahua product material identifies two native integration routes: a device **CGI** surface and the native **NetSDK**. Public release notes and integration documents confirm their use, but a single current, global, publicly accessible normative specification and compatibility catalogue was not verified. This page therefore maps decisions and evidence gaps without reconstructing endpoints from old mirrors or third-party examples.

## Surface map

| Surface | Appropriate use | Evidence boundary |
|---|---|---|
| CGI | HTTP-oriented device configuration, query, events or control where the exact product guide declares support | Confirmed by product/release artefacts; operation/auth/version details require the current vendor package |
| NetSDK | Native client integration for supported device media, events, discovery, configuration or control | Release artefacts identify package versions for particular products; compatibility is not universal |
| Product-specific API/SDK | Access-control and other vertical-product integration | Regional file-host material exists, but the provenance of `files.dahua.support` was not independently verified as an official Dahua-controlled host |
| ONVIF and other standard protocols | Standards-based interoperability on declared models | Separate from CGI/NetSDK and subject to exact model conformance/support |

## Required procurement evidence

Obtain from Dahua or the authorized channel before coding:

- current CGI guide and/or NetSDK package under its applicable terms;
- target model, hardware revision, firmware train and region;
- package version, operating system, architecture, runtime and compiler support;
- feature licence, account role and product capability list;
- security hardening and certificate-management guide;
- release notes that explicitly name the tested SDK/API and target product;
- support and vulnerability-reporting route.

A release note that names one NetSDK version proves only that relationship for the listed product/release. It is not evidence that the package is current for another camera, recorder, intercom or access controller.

## Authentication and transport boundary

Do not derive authentication from historic web snippets or cached CGI examples. Confirm the current firmware’s HTTPS, certificate, digest/session/token, user-role, lockout and password-rotation contract. Reject plaintext fallback, default credentials and certificate validation bypasses.

Keep a unique integration account per workload and site. Separate read-only health/media/event access from configuration, PTZ, audio, credential, door, relay, alarm, reboot and firmware rights. Native SDK callbacks and credentials must never be logged verbatim.

## Data and failure handling

CGI command names and NetSDK structures can evolve independently. Treat every response, callback and device-supplied length/count as untrusted. Pin headers, structure packing, calling convention, character encoding and ownership rules from the exact SDK manual; copy callback data before returning only when the manual requires it.

For long-lived events and media:

- detect disconnect and device reboot;
- bound reconnect backoff, queues, payloads, media buffers and callback work;
- preserve device time and collector time;
- identify duplicates and gaps;
- re-read authoritative configuration after reconnect;
- isolate native SDK loading and crash impact from the main application where practical.

For high-impact commands, never repeat blindly after timeout. Determine whether the API defines idempotency, then query state or require operator reconciliation. An SDK “success” is not proof that a relay, lock, alarm or credential operation completed physically.

## Lifecycle and documentation hygiene

Regional file stores and release artefacts can preserve obsolete manuals alongside current ones. The `files.dahua.support` hostname used by two linked artefacts below has not been independently established as an official Dahua-controlled property, so treat those documents as provenance-unverified leads rather than vendor authority. Record source URL, publication/revision, product list and retrieval date, and obtain the same contract through Dahua or an authorized channel before implementation. Do not copy a guide from an unrelated model family merely because command naming looks similar.

The `technology_status: mixed` value reflects active products and interfaces alongside old public documents and discontinued-product pages, not a claim that CGI or NetSDK as families are deprecated.

## Primary sources

- [Dahua software release note for a named product release](https://materialfile.dahuasecurity.com/uploads/cpq/SWR/3125267/General_Faraday_V3.140.0000000.40.R.250325_Release_Notes.pdf) — official example tying testing to CGI tooling and a specific NetSDK package; not a universal compatibility statement.
- [Access-control integration document directory](https://files.dahua.support/Solutions/Access%20Control%20Solution/Integration/) — provenance-unverified regional file host; use for discovery only.
- [Access-control products integration instruction](https://files.dahua.support/Solutions/Access%20Control%20Solution/Integration/DAHUA%20ACCESS%20CONTROL%20PRODUCTS%20INTEGRATION%20INSTRUCTION%20Ver1.0.pdf) — provenance-unverified product-specific document; not sufficient authority for implementation.
- [Dahua product catalogue](https://www.dahuasecurity.com/products) — exact model and regional product status starting point.

## Related pages

- [Secure protocol parsing](../../06-security-and-assurance/secure-protocol-parsing.md)
- [Adapters and gateways](../../05-development-and-integration/patterns/adapters-gateways-and-translation.md)
- [Change, firmware, and patching](../../07-operations-and-lifecycle/change-firmware-and-patching.md)
