---
title: Biometric Access-Control Systems
summary: Enrollment, template protection, matching modes, thresholds, presentation-attack detection, demographic performance, privacy, and fallback.
page_type: system
domains: [access-control, identity]
tags: [biometrics, face, fingerprint, iris, templates]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [ISO/IEC 19795 series, ONVIF Profile D]
coverage_limit: Architecture and assurance only; no biometric capture/template, threshold recommendation, identity claim, or product accuracy claim.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Biometric access-control systems

Biometric matching is probabilistic. A result depends on sensor, sample quality, algorithm/version, threshold, population, environment, presentation-attack controls, and workflow. A biometric characteristic is not secret and is difficult to replace after compromise.

## Lifecycle and roles

```text
notice/authority -> identity proof -> supervised enrollment/capture
 -> quality check/template creation -> protected storage/binding
 -> presentation + liveness/PAD -> comparison -> policy decision
 -> adjudication/fallback -> update/revoke/delete/audit
```

Distinguish 1:1 verification (claim then comparison) from 1:N identification/search. Their error rates, privacy, scale, and authorization consequences differ.

## Metrics and thresholds

Evaluate false match/non-match, failure to acquire/enrol, transaction time, quality rejection, presentation-attack outcomes, and operator fallback at the deployed threshold and population. Report confidence/score according to the product contract; scores from different algorithms/versions are not directly comparable.

ISO/IEC 19795 is the multi-part biometric performance-testing/reporting family in the [ISO catalogue](https://www.iso.org/committee/313770/x/catalogue/). NIST's ongoing/official biometric evaluations and [FRVT demographic-effects report](https://www.nist.gov/publications/face-recognition-vendor-test-part-3-demographic-effects) show why performance must be disaggregated across relevant demographics and conditions. A lab result is not site validation.

## Template/data protection

- Prefer matching/storage architectures that minimize centralized raw biometric data and use cancelable/protected templates where supported.
- Encrypt in transit/at rest, isolate keys, restrict enrollment/export/admin, and audit every access/change.
- Do not store raw captures or templates in generic PACS logs, SIEM, analytics, ordinary backups, tickets, or documentation repositories.
- Define retention, deletion (including replicas/backups/device caches), portability/non-reuse, breach response, and subject rights.
- Prevent cross-purpose correlation through scoped opaque subject/template IDs.

Legal consent/authority, workplace fairness, accessibility, children/vulnerable people, surveillance law, and biometric-specific regulation vary sharply by jurisdiction.

## Device and PACS boundary

ONVIF Profile D's public [access-control peripheral scope](https://www.onvif.org/blog/2021/08/04/do-you-know-your-onvif-profiles/) includes biometric readers. Verify where matching occurs, what traverses reader-controller/network links, template format/lock-in, reader/controller identity, secure channel, offline cache, and revocation.

The PACS should receive the minimum result needed, with provenance/quality, not unrestricted templates. A match is one authentication signal; authorization still applies schedules, areas, anti-passback, risk, and account state.

## Fallback and safety

Design accessible, non-discriminatory fallback and manual adjudication. Attackers often target fallback/recovery rather than the biometric algorithm. Rate-limit and review repeated failures without locking people into unsafe areas. Required egress/emergency behavior must not depend on successful biometrics.

## Change control

Model, firmware, sensor, threshold, camera/illumination, population, mask/PPE, enrollment process, or environment change requires re-evaluation. Preserve versioned score/decision evidence without retaining excessive biometric data.

Return to [Access-control systems](README.md).
