---
title: 2N HTTP and Platform APIs
summary: Publicly documented 2N IP device HTTP API, Access Commander API, and selected platform-specific integration surfaces.
page_type: vendor-api
domains: [intercom, access-control, integration]
tags: [2n, http-api, access-commander, intercom, access-control]
scope: global with model, firmware, and licence differences
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public 2N manuals and API references reviewed on 2026-08-25; exact device services, firmware, account count, licences, Access Commander edition, authentication availability, and command behavior require target-product confirmation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# 2N HTTP and platform APIs

[Vendor APIs](../README.md) / [Device and edge video](README.md) / 2N

2N publishes a device-facing **2N IP HTTP API** and distinct APIs for management/application platforms such as **2N Access Commander** and selected indoor-device applications. Keep those authority planes separate: a device HTTP account is not an Access Commander API identity, and a platform integration does not prove direct device support.

## Verified scope and access

| Surface | Product plane | Public documentation | Boundary |
|---|---|---|---|
| 2N IP HTTP API | Supported IP intercoms, access units and related devices | Public latest manual plus versioned PDF | Service availability and licence vary by product/firmware |
| Access Commander HTTP API | 2N Access Commander management platform | Public versioned manual with v2/v3 sections | Server edition/version, tenant/site and permission model apply |
| Indoor Touch application HTTP API | Supported 2N Indoor Touch application/device | Public reference | Not interchangeable with the IP device API |

The public IP HTTP API manual enumerates supported product families. Use that list and the target device’s **Services → HTTP API** configuration page; do not infer support from a similar chassis or product name.

## Device service model

The device configuration manual groups HTTP API control by service, including system, access, switch, I/O, display, e-mail, logging and automation-related functions where supported. Each service can have its own enablement, transport and authentication choice. That granularity is a security boundary: enable only the services the integration requires.

The public manual describes HTTP/HTTPS and None/Basic/Digest choices on supported products. “None” is not appropriate for a production integration. Prefer HTTPS with a unique account and the strongest documented authentication that is compatible with the exact firmware. Validate the certificate under the deployment PKI policy and block plaintext fallback.

An Access Unit 2.50 configuration page describes up to five HTTP API accounts for that product/version. Do not generalize the count to every intercom, access unit or firmware.

## Capability and authorization design

Separate identities and privileges for:

- health and inventory reads;
- event/log retrieval;
- access/cardholder information;
- camera snapshot or media-related operations;
- switch, relay, I/O, display or automation control;
- system configuration and restart;
- Access Commander administration.

Switch and access operations can release a door or activate connected equipment. Require explicit user authorization, a bounded target, an auditable reason and post-command state reconciliation. The API result does not prove the lock, contact, person passage or downstream automation state.

## Events and state

Use the event/log mechanism documented for the exact API version. Preserve device event time, collector time, device identity, event identifier/type and any sequence information. On reconnect, assume duplicates and gaps are possible until the manual says otherwise; re-read relevant status and reconcile.

Do not use event text as a stable machine contract when the API supplies structured type or identifiers. Treat names, display strings, e-mail fields and uploaded content as untrusted input and minimize personal data in logs.

## Version and lifecycle

The public site exposed a versioned 2N IP HTTP API PDF numbered 2.49 and product configuration documentation numbered 2.50 during review. These are observations for those documents, not a universal “latest API version.” Record device firmware, manual revision and individual service support together.

For Access Commander, pin server release, API generation, authentication method and permission set. Do not silently migrate between v2/v3 sections or depend on an unversioned example.

## Primary sources

- [2N IP HTTP API manual](https://wiki.2n.com/hip/hapi/latest/en) — public device API reference and product scope.
- [2N IP HTTP API manual 2.49 PDF](https://wiki.2n.com/download/attachments/123498082/2N_IP_HTTP_API_manual_EN_2.49.pdf) — fixed versioned evidence.
- [2N Access Unit 2.50 HTTP API configuration](https://wiki.2n.com/acuc/latest/en/5-konfigurace-pomoci-weboveho-rozhrani/5-4-sluzby/5-4-5-http-api) — service/auth/account model for that documented product line.
- [2N Access Commander 2.7 HTTP API](https://wiki.2n.com/acc/2.7/en/6-http-api) — platform API reference route.
- [2N Indoor Touch application HTTP API](https://wiki.2n.com/hseita33/api/latest/en/2-http-api) — separate platform-specific surface.

## Related pages

- [SIP and SRTP](../../02-protocols/video-and-media/sip-and-srtp.md)
- [Locks, egress, and life safety](../../03-systems/access-control/locks-egress-and-life-safety.md)
- [API and event security](../../06-security-and-assurance/api-and-event-security.md)
