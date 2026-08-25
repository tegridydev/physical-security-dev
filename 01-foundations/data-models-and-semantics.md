---
title: Data Models and Semantics
summary: Designing canonical entities, identifiers, schemas, units, provenance, and mappings across heterogeneous security systems.
page_type: foundation
domains: [cross-domain]
tags: [data-model, semantics, schemas, normalization]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: [RFC 8259, XML 1.0]
coverage_limit: Technology-neutral guidance; protocol-specific schemas remain authoritative.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Data models and semantics

Most cross-system defects are not byte-level problems. They are disagreements about identity, state, time, units, or authority hidden behind syntactically valid XML or JSON.

## Model the source before normalizing it

Preserve three representations where feasible:

1. **Raw source:** immutable message or a privacy-safe hash/reference plus transport metadata.
2. **Parsed source model:** fields retaining the publisher's names and types.
3. **Canonical model:** intentionally mapped entities and meanings used by consumers.

This makes lossy mappings visible and allows reprocessing when the canonical schema evolves. Never discard unknown fields merely because the current consumer ignores them; retain them within bounded, privacy-controlled storage when policy permits.

## Stable identity

Do not use a display name, IP address, array index, or mutable location as the primary identity. A robust identifier record can include:

```yaml
source_system: pacs-a
source_entity_type: door
source_entity_id: "8c18..."
canonical_entity_id: site-a/building-1/door-004
observed_name: East Lobby
mapping_version: 3
```

Distinguish person, identity record, credential, token instance, reader, access point, door, lock, input, controller, camera, stream, recording track, zone, and site. Their relationships change independently.

## Types and units

- Define integer width/sign and overflow behaviour for binary protocols.
- Treat identifiers that happen to contain digits as strings unless arithmetic is intended.
- Record unit, scale, precision, and valid range with numeric telemetry.
- Preserve `null`, absent, empty, zero, false, unknown, and unsupported as distinct where the source does.
- Define enum behaviour for new/unknown values; do not route an unknown alarm priority into the lowest class.
- Identify text encoding and normalization; cap lengths before logging or rendering.

JSON's grammar is standardized by [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259), but it does not define application semantics, duplicate-name handling across all implementations, numeric precision, or a schema. XML likewise needs the applicable namespace/schema and application rules; the W3C publishes the [XML specifications](https://www.w3.org/TR/xml/).

## Provenance envelope

For an observation, retain:

- source system and entity;
- source event/message identifier and sequence where available;
- source, receive, normalize, and publish times separately;
- source clock quality or uncertainty if known;
- protocol/profile/schema and product version;
- mapping version;
- authenticated peer/workload identity;
- trace/correlation identifiers;
- raw-evidence reference and integrity metadata;
- privacy/security classification.

## Canonical schemas

Keep canonical fields small and stable; put source-specific detail under a namespaced extension. Version the schema and mapping independently. Compatibility rules should state:

- whether consumers ignore unknown fields;
- which fields may become required;
- default versus absent behaviour;
- enum extension handling;
- timestamp and identifier format;
- retention and redaction requirements;
- how mapping corrections are replayed.

## Semantic mapping record

Every non-trivial mapping should document source value, target value, conditions, information loss, authority, and fallback. For example, do not map all of `forced-open`, `held-open`, `contact-open`, and `unlock-commanded` to `door_open` without preserving the distinction.

## Validation boundary

Validate structure before allocating large objects; validate semantics before changing state; validate authorization immediately before actuation. A schema-valid command can still refer to the wrong site, stale entity, unsupported unit, or unauthorized operation.

