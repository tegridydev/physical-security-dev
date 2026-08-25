---
title: Trust Boundaries and Segmentation
summary: Designing zones, conduits, identities, and one-way/minimum-authority flows for cyber-physical security systems.
page_type: foundation
domains: [cross-domain]
tags: [trust-boundaries, segmentation, zero-trust, zones]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [NIST SP 800-82 Rev. 3, NIST SP 800-207]
coverage_limit: Architecture guidance; exact controls depend on risk, product capabilities, and site safety requirements.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Trust boundaries and segmentation

A trust boundary exists whenever administration, identity, exposure, physical access, assurance, tenancy, safety impact, or data sensitivity changes. VLANs and firewalls can enforce part of a boundary, but the boundary is an architectural fact, not a network feature.

## Common boundaries

- field wiring or radio to controller;
- device/edge network to site platform;
- video, access, alarm, intercom, BMS, and OT domains;
- control plane to observation/analytics plane;
- tenant/site to shared service;
- on-premises to supplier or cloud service;
- production to commissioning/support tooling;
- human operator to automation/workload;
- supplier-managed appliance to customer-managed identity and logging.

## Zone by consequence and authority

Group assets with compatible trust and failure requirements, not just ownership labels. Useful separations include:

```text
field devices
local controllers
recording and event services
integration/broker boundary
management and update services
operator clients
enterprise identity/SIEM
external/cloud/vendor support
```

A camera analytics service that only needs events should not share the same path/account as firmware administration. A BMS dashboard that consumes door occupancy should not automatically inherit door-control authority.

## Conduit record

For every permitted flow, record source/destination roles and zones, initiator, protocol/version, service identity, authentication, authorization, data classification, rate, availability, logging, owner, and expiry/review date. Default deny everything not represented.

When a legacy protocol lacks authentication or encryption:

- keep it within the smallest physical/network zone;
- restrict endpoints and direction at a protocol-aware or tightly scoped gateway;
- prevent direct enterprise/cloud reachability;
- monitor expected operations and rates;
- protect commissioning ports and wiring;
- plan migration instead of describing isolation as equivalent security.

## Identity plus segmentation

NIST [SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) states that network location or ownership must not create implicit trust. Apply user, device, and workload identity and operation-level authorization even inside a zone. Segmentation remains valuable for reducing reachability, containing failures, and supporting simpler policy; it does not replace identity.

## Cross-domain gateway

A gateway should:

- terminate and authenticate both sides independently;
- expose only required operations and fields;
- normalize identities and enforce site/tenant scope;
- validate size, schema, semantic range, freshness, and authorization;
- bound queues and rates;
- make loss, staleness, and partial failure visible;
- separate observation and actuation paths;
- produce tamper-resistant audit with correlation IDs;
- fail to an explicitly designed state.

Avoid transparent bidirectional bridges between security and OT/BMS networks. Prefer a narrow exported data product or broker namespace, with any reverse command path separately justified and approved.

## Availability and recovery

Segmentation controls can fail closed, fail open, or fail ambiguously. Define local autonomy, redundant dependencies, maintenance bypass governance, certificate/identity outage behaviour, and out-of-band recovery. NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) emphasizes that OT safeguards must respect availability, reliability, and safety.

## Validation questions

- Can a compromised viewing client reach device management?
- Can an analytics tenant publish a control message?
- Can a vendor-support identity operate outside its window/site?
- Does DNS, time, certificate, or identity outage break local control?
- Can the gateway distinguish stale replay from a new alarm?
- Are denied and unexpected cross-zone attempts observable?

