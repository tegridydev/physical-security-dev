---
title: Glossary and Conventions
summary: Core terminology and writing conventions used consistently across the library.
page_type: reference
domains: [cross-domain]
tags: [glossary, terminology, conventions]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: Core cross-domain terms only; protocol-specific glossaries remain on protocol pages.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Glossary and conventions

## Core terms

| Term | Meaning in this library |
|---|---|
| Actuation | A request or signal capable of changing a physical or security-relevant state. |
| API | A defined software interface. “REST API” does not by itself specify authentication, schema, or delivery semantics. |
| Command | An expression of requested intent; not proof of acceptance or physical completion. |
| Conformance | Evidence that an implementation satisfied a named test/claim for a specific standard edition, profile, role, and version. |
| Controller | A component that evaluates logic and/or drives field outputs. Context must say camera, access, industrial, or other controller. |
| Credential | Data or an artefact presented in an authentication process; not automatically a person or authorization. |
| Device identity | Identity of hardware/software in a protocol or trust system. It is distinct from operator, user, credential, and workload identity. |
| Event | An immutable report that something was observed or decided at a time; delivery may be repeated, delayed, reordered, or lost. |
| Fail safe | Failure leads toward the defined safer condition. This is a hazard decision, not synonymous with electrically unlocked. |
| Fail secure | Failure preserves the defined security condition. It does not override life-safety and egress requirements. |
| Gateway | A boundary component translating transport, protocol, data model, trust, or policy. State what it translates. |
| Integration | A designed exchange between systems, including ownership, semantics, security, failure, and lifecycle—not merely connectivity. |
| Interoperability | Two implementations perform the intended use case together. It is narrower than “both support protocol X.” |
| Metadata | Data describing or accompanying other data, such as video analytics objects or provenance. It can itself be sensitive. |
| Observation | Data received without an intended control effect. Subscription setup or acknowledgement may still create a control path. |
| Profile | A selected, testable set of requirements from one or more specifications. Profile names are not protocol versions. |
| Restore | A report that a previously active condition is no longer active; not deletion or negation of the original event. |
| State | The current model of a property, usually reconstructed from snapshots, events, polling, and local assumptions. |
| Supervision | Detection of path/device/circuit conditions such as open, short, substitution, loss, or timeout. |
| Trust boundary | A point where identity, administration, exposure, or assurance changes and policy must be enforced. |
| VMS / VSaaS | Video management system / video surveillance as a service. Deployment model does not determine interface openness. |

## Protocol and layer conventions

- **Ethernet, RS-485, RS-232, radio, and dry contacts** are media/electrical or physical interfaces, not interchangeable application protocols.
- **TCP, UDP, TLS, HTTP, RTP, MQTT, OSDP, and ONVIF** occupy different layers or define different sets of behaviour. Avoid “runs over IP” as a complete architecture description.
- A registered port is a default or service convention, not evidence that traffic is present, authentic, or safe.
- “Secure” is qualified: confidentiality, integrity, peer authentication, user authorization, replay resistance, key management, secure update, and audit are separate properties.

## Naming and files

- Files and folders use lowercase ASCII `kebab-case`.
- Acronyms are expanded on first use in prose unless universally clear in the immediate context.
- Dates use ISO `YYYY-MM-DD`; times should include an offset or `Z` and identify source clock.
- Byte and bit positions start at zero only when the source convention is stated.
- Network examples use RFC 5737 IPv4, RFC 3849 IPv6, `.example`, or loopback space.
- Secrets use descriptive placeholders such as `${DEVICE_TOKEN}`; never plausible sample secrets.

## Requirement language

Uppercase **MUST**, **SHOULD**, **MAY**, and related terms are used only in attributed summaries of a normative document that defines those terms. Knowledge-base advice uses “require,” “prefer,” “consider,” and “avoid,” with rationale.

## Status language

| Label | Meaning |
|---|---|
| current | Final and supported in the stated ecosystem |
| release-candidate | Not final; details and conformance availability may change |
| legacy | Deployed and relevant, but generally not preferred for new design |
| deprecated | Publisher has announced withdrawal/end of support or replacement |
| historical | Retained to understand installed systems, not current implementation guidance |
| mixed | Depends materially on edition, profile, product, or deployment mode |

See the [metadata schema](../10-sources-and-maintenance/metadata-schema.md) for controlled values.

