---
title: Interoperability, Conformance, and Profiles
summary: How to interpret standards support, conformance claims, profiles, optional features, and product compatibility.
page_type: foundation
domains: [cross-domain]
tags: [interoperability, conformance, profiles, procurement]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: General method; each standards body defines its own marks, testing, and policy.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Interoperability, conformance, and profiles

“Supports X” is not a sufficient integration requirement. It may mean a marketing claim, a library exists in the product, one role is implemented, an older edition is supported, or a tested profile is available only on certain firmware.

## Distinct claims

| Claim | What it demonstrates | What it does not demonstrate |
|---|---|---|
| Specification compliance | Implementation follows stated requirements | Independent testing or compatibility with a use case |
| Conformance certification/declaration | Named product/version passed the publisher's defined process | Every optional feature or production suitability |
| Profile conformance | Selected roles/features meet that profile | Native API behaviour or features outside the profile |
| Interoperability test | Exact implementations completed defined exchanges | All configurations, loads, failures, or future versions |
| User acceptance | Agreed site outcomes were observed | General protocol conformance |

## Minimum capability record

For both endpoints record:

```text
manufacturer and exact product
hardware revision
firmware/software version
protocol edition
client/server or controller/peripheral role
profile and add-ons
mandatory and selected optional features
authentication and secure transport modes
codec/encoding/schema constraints
known errata and vendor advisories
conformance declaration or database entry
```

Compare the **intersection** of supported behaviour, not the union. If a client requires H.265, an event topic, mutual TLS, and edge-recording retrieval, “both are ONVIF conformant” is not enough; the exact profiles, services, optional capabilities, and authentication paths must align.

## Profiles freeze choices

Profiles improve predictable interoperability by selecting requirements from broader specifications. They also preserve compatibility, which can prevent security mechanisms from being changed in place. ONVIF explains this explicitly in its [Profile S deprecation Q&A](https://www.onvif.org/profiles/profile-s/profile-s-deprecation-qna/): profiles are not modified in ways that would break conformance interoperability, so Profile T is the replacement path rather than retrofitting Profile S.

Profile lifecycle is therefore separate from protocol lifecycle. Track:

- release candidate versus final;
- first and last conformance-submission dates;
- replacement guidance;
- whether deployed conformant products continue to operate;
- test-tool and declaration version;
- security add-ons that are separate from the base profile.

## Optionality traps

- Discovery may be optional or administratively disabled.
- A device can stream a codec but not expose it through the selected profile.
- TLS can be supported while certificate validation or client authentication varies.
- Event support can omit the topic/data needed by the use case.
- A server can accept a command but implement different physical timing or confirmation.
- Vendor extensions can be valid yet destroy cross-vendor portability.

## Evidence and procurement

Use public conformance databases where offered, download the declaration, and preserve its date and version. Require a capability matrix and a small acceptance set that includes authentication, negative authorization, reconnect, clock error, certificate rotation, upgrade, partial outage, and exact semantic mappings.

Do not call a compatibility matrix “verified” until the exact combinations have evidence. Mark unknown cells unknown; absence of a documented feature is not proof that it is unsupported, and an undocumented observed feature is not a stable contract.

## Primary examples

- [ONVIF conformant products database](https://www.onvif.org/conformant-products/)
- [ONVIF profile policy](https://www.onvif.org/wp-content/uploads/2024/04/onvif-profile-policy-v3-4.pdf)
- [OPC UA profiles](https://reference.opcfoundation.org/profiles/)
- [BACnet Testing Laboratories product listing](https://bacnetinternational.net/btl/)

