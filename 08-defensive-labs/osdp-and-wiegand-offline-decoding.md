---
title: "OSDP and Wiegand offline decoding"
summary: "Compare supervised secure-channel-capable reader communications with legacy bit signaling using synthetic fixtures."
page_type: lab
domains:
  - access-control
tags:
  - osdp
  - wiegand
scope: global
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "SIA OSDP 2.2.2"
  - "IEC 60839-11-5:2020"
coverage_limit: "Offline synthetic comparison only; detailed OSDP content requires the licensed standard, and field acceptance is outside lab scope."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# OSDP and Wiegand offline decoding

[Home](../README.md) / [Defensive labs](README.md) / OSDP and Wiegand decoding

Lab class: **Offline synthetic fixture**

## Purpose

Understand that physical signaling, frame error detection, supervision and authenticated encryption are different properties. IEC 60839-11-5 and the full OSDP specification are licensed; normative frames and keys are excluded from the fixture.

## Wiegand exercise

Using an invented bit string whose format is explicitly supplied with the fixture, identify parity positions, facility/site field, credential-number field, total width, and ambiguity. Document that parity detects limited transmission errors but does not authenticate a reader or credential and that bit-field formats vary.

Do not capture a real credential, infer a site's card format, clone/replay a card, or connect to operational reader wiring.

## OSDP review exercise

From official SIA overview material and a licensed standard where lawful access is available, map controller/peripheral roles, multidrop addressing, supervision, capabilities, secure-channel purpose, key provisioning/rotation, installation/default-key risk, downgrade/fallback policy, and conformance testing. Use only synthetic metadata, never live keys or frames.

## Comparison record

| Property | Wiegand-style signaling | OSDP design question |
|---|---|---|
| Direction | Commonly reader to controller | Which bidirectional commands/replies are required? |
| Supervision | Limited by implementation | How is loss/tamper detected and alerted? |
| Confidentiality/authentication | Not inherent | Is Secure Channel required and correctly provisioned? |
| Addressing/topology | Often dedicated conductors | How are multidrop address and bus constraints managed? |
| Migration | Existing panels/readers/format | Is fallback disabled and key lifecycle operational? |

## Evidence checklist

- [ ] Synthetic bit string, declared format, provenance, and digest recorded
- [ ] Bit width, field boundaries, parity positions, and ambiguity identified without inferring a real site format
- [ ] Signaling, error detection, supervision, confidentiality, and authentication kept distinct
- [ ] OSDP controller/peripheral roles, addressing, capabilities, and supervision mapped from lawful sources
- [ ] Secure Channel provisioning, rotation, default-key, downgrade, and fallback questions documented
- [ ] Migration assumptions and conformance evidence requirements recorded
- [ ] Real credential data, keys, frames, cards, readers, panels, and field wiring excluded

## Sources

- [SIA OSDP](https://www.securityindustry.org/industry-standards/open-supervised-device-protocol/), version/status overview, accessed 2026-08-25.
- [IEC 60839-11-5:2020](https://webstore.iec.ch/en/publication/33414), catalogue entry, accessed 2026-08-25.

## Related pages

- [OSDP](../02-protocols/access-control/osdp.md)
- [Legacy reader interfaces](../02-protocols/access-control/legacy-reader-interfaces.md)
