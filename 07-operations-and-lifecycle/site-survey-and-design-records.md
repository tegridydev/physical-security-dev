---
title: "Site survey and design records"
summary: "Information needed to design reliable protocol flows, capacity, trust boundaries, and recovery."
page_type: operations
domains:
  - operations
tags:
  - design
  - topology
  - survey
scope: global
content_status: maintained
technology_status: not-applicable
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Site survey and design records

[Home](../README.md) / [Operations and lifecycle](README.md) / Site survey and design records

The survey captures physical and logical facts that determine whether a protocol design will work. It is not a universal wiring or code prescription; qualified practitioners must assess electrical, radio, fire, egress, environmental and structural requirements locally.

## Record before design

### Assets and topology

- exact existing and proposed devices, firmware, interfaces and licences;
- controller, server, recorder, broker, gateway, directory, cloud and operator relationships;
- physical and logical network paths, VLANs/routes/firewalls, NAT, multicast and wireless/cellular paths;
- serial bus topology, cable type/length, termination, bias, grounding/isolation and addressing;
- power source, PoE class/budget, UPS, battery, surge/environment and reboot sequence;
- field inputs/outputs and safety interlocks, documented without assuming universal NO/NC behavior.

### Data and performance

- stream codecs, resolution, frame rate, bitrate mode, GOP, audio and metadata;
- event rates, burst patterns, queue capacity, alarm supervision and retry behavior;
- storage retention, export, replication and failure capacity;
- time-source path, required accuracy, drift tolerance and offline duration;
- directory/identity latency, controller offline cache and mobile credential dependencies.

### Trust and operations

- security zones and every intended conduit;
- administrative, operator, service, vendor and break-glass identities;
- certificates/keys and enrollment dependencies;
- Internet/cloud data flows and tenant/data-location assumptions;
- local maintenance, monitoring, backup and recovery access;
- privacy-sensitive fields/areas and evidence handling.

## Design outputs

Produce a versioned architecture, asset schedule, addressing plan, protocol/profile matrix, data-flow and firewall matrix, multicast/discovery plan, identity/role matrix, certificate plan, storage/bandwidth calculation, failure-state matrix, monitoring plan, acceptance cases and migration/rollback plan.

## Common omissions

- secondary network interfaces or undocumented vendor tunnels;
- dynamic media port ranges and connection direction;
- IPv6 when only IPv4 policy was designed;
- edge recording retrieval traffic and catch-up bandwidth;
- controller/cloud split-brain after outage;
- clock loss and certificate validation dependency;
- battery/PoE behavior during heater, IR, lock or PTZ peak load;
- life-safety authority and local certified functions.

## Applying the checklist

Tailor the checklist to the exact products, site conditions, and jurisdiction. Record responsible reviewers, unresolved assumptions, qualified-practitioner findings, and the environment-validation evidence used to approve the design.

## Related pages

- [Foundations](../01-foundations/README.md)
- [Segmentation and conduits](../06-security-and-assurance/segmentation-and-conduits.md)
- [Commissioning and acceptance](commissioning-and-acceptance.md)
