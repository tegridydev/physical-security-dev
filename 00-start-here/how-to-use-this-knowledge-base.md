---
title: How to Use This Knowledge Base
summary: A practical method for finding, interpreting, and validating physical-security integration guidance.
page_type: guide
domains: [cross-domain]
tags: [navigation, workflow, evidence]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: Does not replace normative standards, product manuals, or site-specific engineering.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# How to use this knowledge base

Use the library to build a mental model and a verification checklist—not to copy a generic design into a live site.

## Begin with the integration question

Write the outcome before choosing technology. For example: “deliver a camera tamper observation to a case-management system within 15 seconds, without losing the source timestamp or creating a control path back to the camera.” That statement exposes the actors, data, timeliness, trust direction, failure tolerance, and safety boundary.

Then follow this sequence:

1. Identify the systems in [system architecture](../01-foundations/physical-security-system-architecture.md).
2. Mark every network, administrative, physical, and supplier [trust boundary](../01-foundations/trust-boundaries-and-segmentation.md).
3. Classify each interface using [architecture and layering](../01-foundations/architecture-and-layering.md).
4. Establish the canonical entity, state, event, command, and timestamp meanings using [events, state, commands, and time](../01-foundations/events-state-commands-and-time.md).
5. Read the relevant protocol page and its exact version/lifecycle notes.
6. Check the product's official documentation, supported firmware/software, conformance declaration, security advisories, and licensing terms.
7. Record assumptions and unresolved gaps before implementation.

## Read metadata before prose

The front matter describes the page's usable scope. Pay particular attention to:

- `content_status`: whether the page is maintained, draft, historical, or a pointer;
- `technology_status`: current, release-candidate, legacy, deprecated, historical, or mixed;
- `verification`: what evidence review occurred;
- `runtime_status`: execution-evidence state for executable material;
- `coverage_limit`: what the page deliberately does not claim;
- `last_verified` and `next_review`: whether mutable facts may be stale.

A high verification state cannot widen a narrow `coverage_limit`. A `V2` page about public documentation does not validate an undocumented endpoint or every device bearing a vendor name.

## Separate four kinds of statement

| Kind | How it should read |
|---|---|
| Normative | “RFC 9325 section … requires/recommends …” with exact source and version |
| Product fact | “Product family/version X documents …” with vendor source and date |
| Repository recommendation | “Prefer … because …” with rationale and constraints |
| Inference or observation | Explicitly labelled, with the evidence and uncertainty |

Words such as **must**, **shall**, **should**, and **may** are lowercase advisory prose unless a page attributes them to a normative source. Do not silently convert one source's recommendation into a protocol requirement.

## Use examples safely

Examples use reserved names, documentation networks, synthetic identifiers, and clearly marked secret placeholders. Runtime metadata uses these states:

- `conceptual`: illustrates a relationship, not executable syntax;
- `protocol-fragment`: intentionally incomplete wire or payload excerpt;
- `not-executed`: a complete code/protocol example without linked environment evidence;
- `partially-runtime-validated`: only the linked cases and environment have recorded evidence;
- `runtime-validated`: the exact stated claim has a complete linked validation record.

No example should be treated as production-ready merely because it parses. Validate authorization, version compatibility, timeouts, bounds, certificate handling, logging, rollback, and physical consequences.

For an authorized isolated check or deployment acceptance activity, use the [environment validation checklist](../10-sources-and-maintenance/manual-qa-checklist.md) and keep the evidence narrowly scoped.

## When sources disagree

Prefer the applicable normative edition, then official corrigenda/errata, conformance material, and current product documentation. Record the conflict rather than averaging it away. A deployed legacy device may correctly implement an older edition; “newer” and “applicable” are not always the same.

See the [source policy](../10-sources-and-maintenance/source-policy.md), [verification policy](../10-sources-and-maintenance/verification-policy.md), and [known gaps](../10-sources-and-maintenance/known-gaps.md).
