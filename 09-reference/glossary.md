---
title: Glossary
summary: Concise definitions of recurring physical-security, protocol, integration, and assurance terms.
page_type: reference
domains: [cross-domain]
tags: [glossary, terminology, definitions]
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: Working definitions for this knowledge base; a governing standard or jurisdiction may define a term more narrowly.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Glossary

The [naming conventions](../00-start-here/glossary-and-conventions.md) explain how this library uses standards titles, requirement words, lifecycle labels, and device-neutral terms. This page supplies the compact domain vocabulary.

## A–C

**Access control unit (ACU)**  
A controller that evaluates or enforces access decisions and supervises connected doors, readers, inputs, and outputs. Product architectures vary between intelligent field controllers and host-dependent panels.

**Actuation**  
A command or output capable of changing physical state, such as unlocking a door, moving a gate, operating a relay, changing an alarm mode, or controlling equipment. Treat separately from observation.

**Adaptive streaming**  
HTTP delivery in which a manifest describes segmented media representations and a client selects among them. Manifest access, segment authorization, origin fetching, caching, DRM, and evidence provenance remain separate controls.

**Alarm**  
An asserted condition intended to trigger assessment or response. An event becomes an alarm through policy and context, not merely because a bit or message exists.

**Alert lifecycle**  
The relationship among an original public-warning alert and its updates, cancellation, expiry, references, audience, and geographic scope. Receipt is not proof that a downstream system activated a warning.

**Anti-passback**  
Rules intended to prevent credential reuse inconsistent with an entry/exit sequence. Controller partitions, degraded mode, occupancy errors, and emergency policy affect behavior.

**Authority having jurisdiction (AHJ)**  
The organization or official responsible for interpreting and enforcing applicable codes or requirements. The exact authority depends on location and system.

**Attestation**  
Evidence about an authenticator, device, software, or manufacturing identity evaluated under a stated trust policy. Attestation does not identify the current human user or grant an application or physical-access permission by itself.

**Capability**  
A supported function with defined limits. Discovery of a capability does not prove it is configured, licensed, authorized, safe, or interoperable.

**Central station**  
A monitoring facility that receives alarm communications and performs defined handling procedures. Regulatory and certification meanings are jurisdiction specific.

**Codec**  
An encoder/decoder and its bitstream format, such as H.264, H.265, or Opus. Codec name alone does not define profile, level, packetization, latency, or licensing.

**Commissioning**  
The controlled process of installing, configuring, checking, documenting, and accepting a system against approved requirements.

**Conformance**  
Evidence that an implementation satisfies a named specification, profile, role, and edition under the applicable scheme. It is not the same as interoperability, secure configuration, or fitness for purpose.

**Controller**  
A component that hosts logic and interfaces to field devices. Always qualify its domain and responsibility rather than relying on the word alone.

**Credential**  
Data or an object used as evidence in an authentication or access process. A credential identifier is not necessarily a secret, identity, or authorization decision.

**Credit and settlement**  
Messaging flow-control and delivery-state concepts used by protocols such as AMQP 1.0. Link credit bounds transfers; settlement resolves messaging responsibility. Neither proves that a business workflow or physical action completed.

## D–I

**Degraded mode**  
An intentional operating state used when a dependency is unavailable. Define allowed functions, cached decisions, time bounds, alerting, reconciliation, and recovery.

**Door forced open**  
A derived condition indicating that the monitored door opened without an expected authorized sequence. Sensor quality, request-to-exit, timing, and controller logic determine accuracy.

**Door held open**  
A derived condition indicating that a door remained open beyond an allowed interval. It is distinct from forced-open and from the raw contact state.

**Dry contact**  
A potential-free relay contact used as an electrical state boundary. It carries little semantic information unless supervision, polarity, timing, and ownership are documented.

**Edge device**  
A device near the sensing or actuation boundary, such as a camera, reader peripheral, intercom, gateway, or controller. “Edge” does not imply offline autonomy or trustworthiness.

**Event**  
An immutable statement that something was observed or asserted at a time, with source and provenance. Events may be delayed, duplicated, reordered, missing, or corrected.

**Fail-safe / fail-secure**  
Terms commonly describing a lock's behavior on loss of power. They do not by themselves determine compliant egress, fire behavior, emergency release, or whole-system failure policy; use qualified design records.

**Fabric**  
In Matter, an administrative trust domain containing operational identities, controllers, nodes, and policy. A device can belong to more than one fabric; commissioning and removal are security-lifecycle operations.

**Federation**  
A trust arrangement in which one security domain accepts identity assertions or authentication results from another. Federation does not automatically provision accounts, map safe roles, or delegate physical-access decisions.

**Gateway**  
A component that mediates between protocols, networks, trust zones, or semantic models. A secure gateway validates, minimizes, authorizes, rate-limits, observes, and fails predictably rather than transparently forwarding everything.

**Identity**  
An entity as represented within a defined authority and lifecycle. Person, credential, account, device, workload, and certificate identities are related but not interchangeable.

**Idempotency**  
A property allowing a repeated operation to have the same intended effect as one application. It must be defined at the business operation level, not inferred solely from an HTTP verb.

**Interoperability**  
The ability of exact implementations to exchange information and produce the intended result under stated conditions. Standards conformance improves the prospects but does not guarantee it.

## L–R

**Least privilege**  
Granting only the operations, resources, sites, tenants, and duration required for a role or workload.

**Life safety**  
Functions whose failure may contribute to injury or loss of life, including relevant fire, emergency communication, egress, and safety-control functions. Applicability is determined by design and jurisdiction.

**Logical node**  
An IEC 61850 model component that groups standardized data and behavior for a function. Its name and data objects carry engineering meaning; they are not interchangeable with raw point addresses.

**Manifest**  
A document describing media presentations, representations, segments, timing, and related metadata in an adaptive-streaming system. Treat every URI and declared property as untrusted input.

**Mobile credential**  
A credential presented by a mobile device, commonly using BLE, NFC, or UWB plus a vendor application and cloud/provisioning system. The radio is only one layer of the trust model.

**Monitoring**  
Collection and interpretation of health, state, performance, security, and audit signals. A reachable endpoint is not proof that the end-to-end service is healthy.

**Normalization**  
Mapping source-specific observations into a stable internal model while preserving the original meaning, provenance, uncertainty, and raw reference.

**Profile**  
A constrained selection of requirements and options from one or more specifications for a defined role or use case. Name the exact profile and version.

**Passage confirmation**  
Evidence that a person or object traversed a controlled portal in a declared direction. It is distinct from credential authentication, access grant, actuator command, and barrier-open state.

**Passkey**  
A discoverable FIDO/WebAuthn credential intended for user authentication, often synchronized or device-bound depending on the provider and policy. It is not a mobile physical-access credential merely because both may reside on a phone.

**Protocol**  
A set of rules for communication. A protocol may describe only one layer and may leave data semantics, transport, security, discovery, or lifecycle to other specifications.

**Provenance**  
Information about where data came from and how it was transformed, including source system, device, original identifier, receive time, mapping version, and integrity evidence.

**Reader**  
A credential-interaction device. Some readers only forward identifiers; others perform cryptography, biometric processing, PIN entry, mobile communication, or decision support.

**Reconciliation**  
Comparison of event-derived or cached state with an authoritative snapshot after gaps, reconnects, restarts, or uncertainty.

**Restore**  
An event indicating that a previously asserted condition is no longer asserted. It does not necessarily mean an incident was resolved, acknowledged, or closed.

## S–Z

**Secure mode**  
A protocol- or product-specific protected mode. The phrase is incomplete without authentication, encryption, key lifecycle, downgrade behavior, and exact configuration.

**Security vestibule**  
An access-controlled passage space using two or more coordinated doors or barriers. Use this neutral term in new material; “mantrap” remains a legacy search term. Egress, entrapment, accessibility, occupancy sensing, and emergency release need qualified design.

**Security Configuration Language (SCL)**  
The IEC 61850 engineering representation for system, device, communication, and data-model configuration. SCL files are sensitive, versioned inputs whose integrity and deployment state require change control.

**Sensor**  
A component that observes a physical or environmental condition. Its output may be raw, filtered, inferred, stale, tampered with, or unavailable.

**State**  
A condition believed to hold over an interval, usually reconstructed from snapshots and events. Include freshness, confidence, and source.

**Supervision**  
Mechanisms intended to detect faults, substitution, communication loss, wiring conditions, or missed check-ins. Exact detection and timing depend on the interface and configuration.

**System of record**  
The authority designated to own a class of data or decisions. There may be different systems of record for identity, credentials, access rules, video retention, incidents, and assets.

**Tailgating**  
Passage by an additional person or object through a controlled boundary without the intended independent authorization. Detection and prevention technologies have privacy, accuracy, and safety implications.

**Tenant**  
An administrative security boundary in a shared service. Every identity, resource, event, query, token, and audit record should carry and enforce tenant scope where multi-tenancy exists.

**Trust boundary**  
A boundary across which identity, authority, data quality, ownership, or consequence assumptions change. Validate and authorize at the boundary.

**Unknown / indeterminate**  
An explicit state used when the system lacks sufficient trustworthy evidence. It is safer than guessing `false`, `closed`, `healthy`, or `denied`.

**Verification**  
Evidence that a statement, document, design, or implementation meets its stated review level. In this library, `V3` requires a linked record for an exact claim and environment.

**WebAuthn ceremony**  
The challenge/response sequence by which a relying party registers or authenticates a public-key credential through a browser/client and authenticator. Origin, relying-party ID, challenge, user verification, credential policy, and server-side validation all matter.

**Video management system (VMS)**  
A system that manages cameras, live/recorded media, users, events, exports, health, and related integrations. Product and deployment boundaries vary.

**Zone**  
A named grouping used for alarm, access, detection, or network policy. Always qualify the owning system; similarly named zones need not share semantics.
