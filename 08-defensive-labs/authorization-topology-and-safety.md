---
title: "Lab authorization, topology, and safety"
summary: "Define fixture provenance, loopback confinement, hazards, stop conditions, and evidence before any defensive-lab exercise."
page_type: lab
domains:
  - defensive-labs
tags:
  - authorization
  - safety
scope: global
content_status: maintained
technology_status: not-applicable
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Lab authorization, topology, and safety

[Home](../README.md) / [Defensive labs](README.md) / Authorization and safety

Lab class: **Offline fixture, calculation, tabletop, simulated topology, or loopback simulation**

## Required record

Before beginning a lab, record:

- provenance, ownership, and authority for every fixture, capture, dataset, and licensed source;
- lab class from the permitted set in the [section policy](README.md);
- exact fixture names, digests, versions, synthetic identities, and tools;
- for loopback simulation, bindings and evidence that no external route, proxy, discovery path, or device contact exists;
- permitted processing and data-handling scope;
- prohibited operations, especially network contact, writes, actuation, availability tests, firmware changes, and credential use;
- content hazards, including personal data, secrets, live identifiers, malicious artefacts, and licensed material;
- time window, reviewer, evidence location, and disposal requirements;
- expected observations and stop conditions;
- cleanup, fixture disposal, and restoration of the local analysis environment.

## Stop conditions

Stop immediately if scope or provenance is uncertain; any non-loopback traffic appears; a fixture contains an unexpected secret, personal record, live credential, or operational identifier; loopback confinement fails; an action would require device, broker, receiver, endpoint, field-bus, or hardware contact; or cleanup cannot be guaranteed.

## Isolation principles

Prefer embedded fixtures and calculations. When a loopback simulation materially helps, bind every component exclusively to operating-system loopback, use synthetic identities, disable proxy/discovery behavior, and verify confinement before processing the fixture. Private address space, a dedicated switch, a VLAN, or a serial adapter is not loopback and does not make hardware eligible for this lab section.

## Evidence checklist

- [ ] Permitted lab class selected and scope recorded
- [ ] Fixture provenance, authority, digest, version, and sensitivity recorded
- [ ] Synthetic identities and non-operational data confirmed
- [ ] Loopback-only binding and absence of external routes confirmed where simulation is used
- [ ] Stop conditions, prohibited actions, and cleanup responsibilities assigned
- [ ] Evidence location, retention, sharing, and disposal rules recorded
- [ ] Physical or operational acceptance work routed to the separate environment-validation process

## Related pages

- [Secure system baselines](../06-security-and-assurance/secure-system-baselines.md)
- [Incident response and evidence](../07-operations-and-lifecycle/incident-response-and-evidence.md)
