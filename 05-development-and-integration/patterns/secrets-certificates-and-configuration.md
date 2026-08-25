---
title: "Secrets, certificates, and configuration"
summary: "Separate deploy-time configuration and trust material from code while preserving validation and safe change."
page_type: development
domains:
  - development
tags:
  - configuration
  - secrets
  - certificates
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards:
  - "NIST SP 800-57 Part 1 Rev. 5"
coverage_limit: "Configuration and trust-material lifecycle pattern; storage technology, cryptographic policy, deployment platform, product behavior, and recovery controls are environment-specific."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Secrets, certificates, and configuration

[Home](../../README.md) / [Development](../README.md) / [Patterns](README.md) / Secrets and configuration

Configuration is untrusted input with operational side effects. Parse it into a typed validated model, fail clearly on invalid or ambiguous values, and make the effective configuration observable without revealing secrets.

## Configuration classes

- static application behavior and feature policy;
- deployment topology, addresses and protocol roles;
- tenant/site/resource mappings;
- credentials, private keys, tokens and trust anchors;
- runtime tuning such as timeouts, queue limits and retry budgets;
- high-impact authorization and actuation policy.

Do not treat all classes as interchangeable environment strings. Secret values require protected retrieval and redaction; trust anchors require controlled distribution; high-impact policy requires authorization and audit; tunables require bounds.

## Loading pipeline

1. Load from named sources with documented precedence.
2. Reject unknown critical keys and duplicate/conflicting definitions.
3. Parse exact types, units and durations; avoid implicit coercion.
4. Validate ranges, cross-field invariants, URL schemes, paths, identities and secure modes.
5. Resolve secret references without copying values into the configuration model or logs.
6. Produce a redacted effective-configuration fingerprint/version.
7. Apply changes atomically or retain the last known-good state.

## Secret handling

- Use references to an approved secret service/store, not values in Markdown or source.
- Grant access per workload and purpose, with short lifetime where possible.
- Avoid secrets in URLs, command arguments, process listings and error messages.
- Rotate with overlap/reconciliation and revoke the old material.
- Prevent crash reports, tracing and support bundles from capturing values.

## Certificate configuration

Configure expected peer identity and trust anchors, not merely a switch named TLS. Make certificate/hostname validation mandatory, expose expiry and issuer/serial for operations, and keep client key material separate from server trust.

## Sources

- **NIST-800-57** — [NIST SP 800-57 Part 1 Rev. 5][NIST-800-57], key-management guidance, accessed 2026-08-25.
- **NIST-SSDF** — [NIST SP 800-218 Version 1.1][NIST-SSDF], secure development practices, accessed 2026-08-25.

[NIST-800-57]: https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final
[NIST-SSDF]: https://csrc.nist.gov/pubs/sp/800/218/final

## Related pages

- [PKI, certificates, keys, and secrets](../../06-security-and-assurance/pki-certificates-keys-and-secrets.md)
- [Certificate and account lifecycle](../../07-operations-and-lifecycle/certificate-and-account-lifecycle.md)
