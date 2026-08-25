---
title: "CAP and EDXL emergency messaging"
summary: "Developer reference for CAP 1.2 alert semantics, EDXL distribution envelopes, CAP-AU profiling, XML security, and the boundary between message delivery and public warning."
page_type: protocol
domains: [alarms, cross-domain]
tags:
  - cap
  - edxl
  - emergency-messaging
  - public-warning
  - xml
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "OASIS Common Alerting Protocol Version 1.2"
  - "ITU-T X.1303 bis"
  - "OASIS EDXL Distribution Element Version 2.0"
  - "OASIS CAP Australia Profile Version 1.0"
coverage_limit: "Message semantics and defensive integration only; local warning authority, CAP profile, dissemination policy, geospatial practice, accessibility requirements, and operational approval govern every deployment."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# CAP and EDXL emergency messaging

[Web and messaging protocols](README.md) / CAP and EDXL

The Common Alerting Protocol (CAP) is an OASIS XML format for exchanging all-hazard alerts across warning systems. CAP 1.2 is also published by ITU-T as X.1303 bis. The Emergency Data Exchange Language Distribution Element (EDXL-DE) adds a distribution envelope that can route CAP or other emergency payloads. Neither format decides who is authorized to warn, whether a message should be disseminated, or whether a recipient actually perceived and acted on it.

## Standards and profiles

| Publication | Standing | Use |
|---|---|---|
| CAP 1.2 | OASIS Standard | Core alert document, lifecycle, information blocks, areas, resources, and references |
| ITU-T X.1303 bis | ITU-T publication of CAP 1.2 | International telecommunications reference for the same protocol family |
| EDXL-DE 2.0 | OASIS Committee Specification 02 | Distribution metadata and one or more embedded or referenced content objects |
| CAP Australia Profile 1.0 (CAP-AU) | Australian profile published through OASIS and supported by Australian government implementation material | Constrains CAP use for Australian public-warning interoperability |

CAP permits implementation profiles to impose tighter vocabulary, cardinality, identifier, language, geospatial, transport, signing, or governance requirements. Declare the exact profile and version. “CAP 1.2 XML” is not sufficient evidence of interoperability with a national warning system.

## Roles and trust boundaries

```text
authoring system -> approving / issuing authority -> CAP originator
       -> broker, hub, gateway, or EDXL distributor
       -> channel adapter -> recipient application or public channel
```

One organization or service can hold multiple roles. Keep them distinct in the security model:

- **author** creates proposed content;
- **approver/issuer** applies legal and operational authority;
- **originator/sender** assigns protocol identity and transmits;
- **distributor** routes, filters, aggregates, transforms, or relays;
- **channel adapter** maps content to siren, cellular, broadcast, web, app, signage, or another medium;
- **recipient** validates and presents or processes the alert.

Transport authentication establishes a connection or message source within its trust model. It does not establish warning authority unless that authenticated identity is explicitly bound to the relevant sender, jurisdiction, hazard, area, severity, and channel policy.

## CAP document model

A CAP `alert` has top-level lifecycle and routing fields and can contain one or more `info` blocks.

| Layer | Representative content | Important interpretation |
|---|---|---|
| Alert identity | `identifier`, `sender`, `sent` | The tuple is protocol identity context; validate uniqueness and sender ownership |
| Lifecycle | `status`, `msgType`, `scope`, `references` | Test/draft/actual state and alert/update/cancel relationships require policy-aware handling |
| Routing | restrictions, addresses, codes, notes | These constrain distribution; they are not display text |
| Information | language, category, event, urgency, severity, certainty, effective/onset/expiry, headline, description, instruction | Preserve the selected profile's vocabulary and language-specific block semantics |
| Area | area description, polygons, circles, geocodes, altitude/ceiling | Geometry and codes can overlap, conflict, or exceed channel capabilities |
| Resource | description, MIME type, size, URI, digest, embedded data | Treat every URI and payload as untrusted external content |

Do not flatten multiple `info` blocks into one lossy record. Language, audience, time, parameter, event code, area, and resource can differ by block. Preserve unknown extension data under a namespace-aware policy so it can be audited without becoming an implicit command.

## Lifecycle and correlation

CAP `msgType` distinguishes at least an initial alert, update, cancellation, acknowledgement, and error. Implement lifecycle as a graph tied to the cited prior message references, not as “same identifier means replacement.”

- Require the referenced sender, identifier, and sent-time tuple to resolve within the expected authority and tenant.
- Authenticate an update or cancellation to an authority permitted to modify the earlier alert.
- Retain prior versions and the raw canonical evidence needed by policy.
- Make out-of-order, duplicate, delayed, and missing-reference behavior explicit.
- Do not infer cancellation from expiry, transport silence, or a disconnected feed.
- Do not let a late update revive an expired or cancelled warning without profile-defined authority.

An acknowledgement says what the applicable profile or application defines it to say. It does not prove public receipt, comprehension, siren operation, broadcast completion, or response.

## Severity, certainty, urgency, and local policy

CAP's urgency, severity, and certainty values are separate dimensions. Never combine them into an undocumented numeric score or use one dimension as a substitute for another. Category and event text are also not universal actuation codes.

Channel selection, interruption level, siren behavior, accessibility presentation, multilingual content, area targeting, escalation, and expiry are operational policy decisions. They require a locally governed mapping from authenticated CAP fields to each channel's supported semantics. Unknown or unsupported values should route to a safe review/error path rather than silently selecting a default high-impact action.

## Areas and geospatial handling

- Parse latitude/longitude in the order and range required by CAP; do not swap axes based on a GIS library default.
- Validate polygon closure, point count, circle radius, numeric bounds, altitude/ceiling relationship, and total geometry complexity.
- Define boundary inclusion, coordinate reference assumptions, antimeridian handling, and precision before spatial filtering.
- Treat geocodes and geometry as complementary profile-defined inputs, not automatically equivalent.
- Record the original area and any channel-specific simplification or clipping.
- Never broaden an invalid area silently to an entire jurisdiction.

Geospatial match means only that the configured algorithm matched a recipient or channel location. It does not prove the person is present, safe, at risk, or reachable.

## EDXL-DE distribution envelope

EDXL-DE 2.0 can carry distribution information and multiple content objects. It is not a newer CAP version and does not change CAP's internal lifecycle semantics.

Keep these layers separate:

```text
EDXL-DE envelope: distributor identity, distribution ID, time, audience/area,
                  distribution status/type, content objects
CAP payload:      alert identity, authority, lifecycle, hazard information,
                  alert area and resources
transport:        HTTP, message broker, file exchange, or governed service contract
```

Validate and authorize both envelope and payload. If their audiences, areas, status, identifiers, or policy labels conflict, do not guess which wins. Apply the declared profile and route unresolved conflicts to controlled handling. A distributor must not rewrite CAP sender identity, lifecycle references, or warning meaning without an auditable transformation contract.

## CAP-AU considerations

Australian integrations should follow the declared CAP-AU profile and the current Bureau of Meteorology implementation material, not generic CAP examples. The Bureau of Meteorology states that CAP-AU documentation contains inconsistencies and that some details are outdated. Treat that as an active interoperability risk:

- record which OASIS profile document, Bureau guidance, data.gov.au record, code list, and endpoint contract were used;
- resolve conflicting cardinality, vocabulary, identifier, area, and transport interpretations with the responsible Australian authority;
- preserve fixtures from each authorized provider and document provider-specific deviations;
- do not make a nationwide/public-warning compatibility claim from schema validation alone.

The inconsistency warning is not permission to choose whichever interpretation is easiest. Capture an owned decision and revisit it when the government material changes.

## XML, resource, and transport security

- Use a hardened XML parser with external entities, external DTDs, XInclude, and network resolution disabled.
- Bound document bytes, element depth/count, attributes, text length, `info`/area/resource counts, embedded data, and decoded size.
- Match namespace URI and local name; reject ambiguous duplicate security-relevant structures.
- Apply schema and profile validation before workflow mapping, but treat both as syntax/contract checks rather than authorization.
- Validate digital signatures, certificates, trust anchors, algorithms, reference targets, and wrapping resistance where the deployment profile requires signing.
- Authenticate feeds and bind each sender to permitted scope, hazard, geography, status, and message types.
- Fetch resource URIs only through an allowlisted, size- and type-bounded retrieval service; prevent server-side request forgery and redirect escape.
- Deduplicate at the application layer and make retry/idempotency rules explicit.
- Keep test and exercise feeds technically and operationally isolated from production dissemination.

CAP may contain personal, health, infrastructure, shelter, responder, and sensitive location information. Apply minimization, audience controls, encryption, logging redaction, retention, and incident handling appropriate to the content and jurisdiction.

## Delivery-to-outcome model

Record these milestones separately:

1. message bytes received;
2. transport and sender authenticated;
3. XML/profile validation completed;
4. sender and alert action authorized;
5. lifecycle and area resolved;
6. channel adapter accepted the message;
7. channel generated its own delivery evidence;
8. recipient exposure, comprehension, or action, if independently measurable and lawful.

No early milestone proves a later one. In particular, HTTP success, broker acknowledgement, valid XML, a CAP acknowledgement, or channel acceptance must not be represented as successful public warning.

## Verification evidence

Maintain evidence for:

- exact CAP, EDXL-DE, national/local profile, code-list, and transport versions;
- sender identity, warning authority, jurisdiction, hazard, area, status, and channel authorization;
- alert/update/cancel/ack/error correlation, duplicates, ordering, expiry, and missing references;
- multiple languages, multiple areas, geocodes, complex geometry, resources, and unsupported values;
- XML hardening, schema/profile validation, signature verification, and resource-fetch controls;
- transformations between CAP, EDXL-DE, internal schemas, and channel formats;
- independent distinction between ingestion, dissemination, channel evidence, and operational outcome;
- isolated test/exercise handling and controls preventing production activation.

Operational testing of public-warning paths requires the issuing authority, channel owners, emergency-management governance, affected-party coordination, and a plan that cannot be mistaken for a real alert.

## Primary sources

- OASIS, [Common Alerting Protocol standards page](https://www.oasis-open.org/standard/cap/), accessed 2026-08-25.
- OASIS, [Common Alerting Protocol Version 1.2](https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.html), OASIS Standard.
- ITU-T, [Recommendation X.1303 bis](https://www.itu.int/rec/T-REC-X.1303bis/en), CAP 1.2 publication.
- OASIS, [Emergency Data Exchange Language Distribution Element Version 2.0](https://docs.oasis-open.org/emergency/edxl-de/v2.0/edxl-de-v2.0.html), Committee Specification 02.
- OASIS, [Common Alerting Protocol Australia Profile Version 1.0](https://docs.oasis-open.org/emergency/edxl-cap1.2-au/v1.0/edxl-cap1.2-au-v1.0.html).
- Australian Bureau of Meteorology, [CAP-AU specification and implementation information](https://www.bom.gov.au/metadata/CAP-AU/Spec.shtml), reviewed 2026-08-25.
- Australian Government, [Common Alerting Protocol Australia Profile dataset record](https://data.gov.au/data/dataset/cap-au-std), reviewed 2026-08-25.
