---
title: Gallagher Command Centre Integrations
summary: Officially evidenced Gallagher Command Centre REST API families, Cloud API Gateway, controller interfaces, and video/mobile SDK licensing and partner boundaries.
page_type: vendor-api
domains: [access-control, identity, integration]
tags: [gallagher, command-centre, rest-api, cloud-api-gateway, mobile-connect]
scope: global with server, product, region, licence, and partner differences
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: Public Gallagher product, integration-tool, and Technology Partner material; developer guides, sample code, endpoint contracts, authentication, tokens, API versions, licences, and exact Command Centre compatibility are partner/request gated.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Gallagher Command Centre integrations

[Vendor APIs](../README.md) / [Access and identity](README.md) / Gallagher

Gallagher exposes several separately licensed server and controller interfaces around Command Centre. The public Integration Tools data sheet is the authoritative catalogue-level source; detailed developer guides, samples, tokens, demo licences and endorsement workflow are supplied through the Technology Partner programme.

## Verified surface map

| Surface | Publicly documented capability | Access/licence boundary |
|---|---|---|
| REST API View Events & Alarms | Receives selected Command Centre event/alarm information | Server API/licence and partner guide required |
| REST API Create Events & Alarms | Creates external events/alarms in Command Centre | Licensed per server; Cloud API Gateway is offered for remote connectivity |
| REST API Cardholders | Cardholder/credential-oriented integration | Exact create/update/delete fields and authority require current guide/licence |
| REST API View Status | Obtains current state for supported Command Centre items | Remote access can use Cloud API Gateway; supported objects/version vary |
| REST API Overrides | Overrides doors, access/alarm/fence zones, macros and outputs | Licensed per server; high-impact command surface |
| Cloud API Gateway | Cloud connection to an on-premises Command Centre REST API | Subscription/connectivity, identity, tenant and API licence apply |
| Controller API and field interfaces | Controller-side integration plus documented ASCII, BACnet, OPC and other interfaces | Distinct trust plane and protocol/licence contract |
| Video Viewer SDK | Embeds third-party VMS video in Command Centre UI | Free for development according to product page; licensed per server for deployment |
| Mobile Connect SDK | Embeds Gallagher mobile credentials in iOS/Android applications | Technology Partner access; Cardholder REST API participates in provisioning |

## Partner and licence workflow

Gallagher’s Technology Partner page describes agreement, API selection, portal access, Command Centre environment, development, an integration licensing review, API-endpoint inventory, token/demo licence, technical review and endorsement. This is not an anonymous public-API onboarding model. Obtain written confirmation of:

- required REST/SDK/controller interface product codes;
- development and production server licences;
- Command Centre and independently upgradeable REST API versions;
- cloud-gateway subscription/region and network route;
- endpoint inventory approved for the integration;
- token/credential lifecycle and partner redistribution terms.

Command Centre v9.10 public material described its REST API as independently upgradeable from the Command Centre server. Treat that as a version-specific architecture fact, not proof that every older/current deployment has the same API module or compatibility.

## Authentication and authorization

Public catalogue pages do not establish the complete current auth contract, so this page does not invent one. Follow the partner guide for direct on-premises and Cloud API Gateway modes. Use unique integration identities/tokens, validated TLS, network allowlists where appropriate and least privilege by API family and object.

Cardholder synchronization, event ingestion, status reading and overrides should not share one all-powerful credential. Separate human approval from workload identity and record the Command Centre operator/role, partner token, site and object scope behind every command.

## State and event engineering

- Build an initial snapshot before applying event deltas.
- Persist stable Command Centre identifiers, source/ingest time and event identity.
- Detect server/API upgrade, reconnect, duplicates, gaps and changed object permissions.
- Reconcile cardholders, credentials and object status from authoritative reads.
- Do not equate access granted, door unlocked, door contact open and person passage.
- Bound page sizes, queues, webhook/gateway retries and client concurrency using the gated guide.

For inbound alarms, preserve source provenance and prevent external systems from spoofing native Gallagher events. For status exported to a BMS, minimize personal/security detail.

## High-impact command boundary

The Overrides API publicly names doors, zones, macros and outputs and gives lockdown and open-door examples. These commands can affect life safety and site response. Require explicit approved use cases, narrow target allowlists, command preconditions, reason codes, dual control where appropriate, and immutable audit. Never blind-retry after timeout; reconcile state and operator journal first.

## Primary sources

- [Gallagher Integration Tools data sheet](https://products.security.gallagher.com/security/medias/Integration-Tools-Datasheet?context=bWFzdGVyfGRvY3VtZW50c3wxOTE4ODkyfGFwcGxpY2F0aW9uL3BkZnxhRGcxTDJoaU5pOHhORFl5TnpVNU9EYzVORGM0TWk5SmJuUmxaM0poZEdsdmJsOVViMjlzYzE5RVlYUmhjMmhsWlhRfDMwNmFiZTA2MjRlOTJmZWM1MmU2MTY1MTJmZTk5M2FiNGJjNmM2NzQ3MGFjNWJkMWY1YzQxZDY4ZDBiZWUwNmY) — official surface catalogue.
- [Technology Partner programme](https://security.gallagher.com/en-CA/Our-Partners/Our-Technology-Partners) — gated resources, licence/token and endorsement workflow.
- [REST API Overrides](https://products.security.gallagher.com/security/us/en_US/products/software/rest-api-overrides/p/C12812) — supported high-impact object classes and per-server licence.
- [REST API Create Events and Alarms](https://products.security.gallagher.com/security/us/en_US/products/software/rest-api-create-events-%26-alarms/p/C12820) and [View Status](https://products.security.gallagher.com/security/us/en_US/products/software/interfaces/rest-api-view-status/p/C12810) — event/status and Cloud API Gateway evidence.
- [Video Viewer SDK](https://products.security.gallagher.com/security/us/en_US/products/integrations/video-viewer-sdk/p/C12732) — development/deployment licence distinction.
- [Mobile Connect SDK](https://products.security.gallagher.com/security/global/en/products/software/interfaces/mobile-connect-sdk/p/AAA105) — partner and credential-provisioning boundary.

## Related pages

- [PACS architecture](../../03-systems/access-control/pacs-architecture.md)
- [Alarm, event, and command security](../../06-security-and-assurance/api-and-event-security.md)
- [BACnet family](../../02-protocols/building-and-industrial/bacnet-family.md)
