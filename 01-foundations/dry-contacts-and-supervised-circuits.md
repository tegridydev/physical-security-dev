---
title: Dry Contacts and Supervised Circuits
summary: Relays, digital inputs, end-of-line supervision, state interpretation, and safety boundaries for universal field integration.
page_type: foundation
domains: [access-control, alarms, intercom, bms, ot, video]
tags: [dry-contact, relay, gpio, supervision, eol]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: No wiring values or actuation instructions; follow approved drawings, product manuals, and jurisdictional electrical/life-safety requirements.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Dry contacts and supervised circuits

A relay contact is one of the most interoperable physical-security interfaces, but it carries almost no semantics by itself. “Closed” can mean alarm, normal, energized, bypassed, unlock, fault, or nothing—depending on the approved design.

## Terms

- **Dry/volt-free contact:** switch contact that does not intentionally supply voltage. Verify ratings and isolation; never assume a terminal is dry from its label alone.
- **NO / NC / COM:** normally open, normally closed, and common relative to the relay's defined normal/de-energized state—not necessarily the system's normal condition.
- **Digital input:** senses an electrical state; it may supply a wetting voltage and have polarity or threshold requirements.
- **End-of-line (EOL) supervision:** components at the circuit end allow the receiver to distinguish more than open/closed states.

## Separate electrical and semantic state

Define a mapping table in the approved design:

| Electrical observation | Interpreted state | Quality/action |
|---|---|---|
| Expected normal range | normal | valid |
| Expected alarm range | active | valid alarm/event |
| Open-circuit range | trouble or state, per design | do not guess |
| Short-circuit range | trouble or state, per design | do not guess |
| Out of range/unstable | unknown/fault | raise health condition |

Single-EOL, double-EOL, and product-specific schemes differ. Resistor values, tolerances, topology, cable resistance, input thresholds, debounce, and tamper semantics must come from exact documentation and approved drawings.

## Relay is not confirmation

An output energizing does not prove the physical operation. Use a separate, appropriately designed monitor where the outcome matters:

```text
unlock request -> controller accepts -> lock output changes
               -> lock monitor changes (if present)
               -> door contact changes (if opened)
```

Each arrow has separate timing and failure modes. A door contact indicates leaf position, not lock security; a gate limit indicates position, not a clear path.

## Safety and isolation

Do not connect, bridge, force, meter, or actuate live fire, egress, lift, gate, lockdown, alarm, or emergency circuits based on generic guidance. Use qualified people, approved drawings, isolation boundaries, contact ratings, surge/fault protection, test windows, manual override, and independent observation.

Avoid driving an inductive load directly from an interface relay unless the product and electrical design explicitly support it. Suppression components and polarity can affect release timing and monitoring; this is an electrical engineering decision.

## Integration design

- Name signals by meaning and polarity, not `input1` or `relay2` alone.
- Record normal/degraded/unknown behaviour during power loss, controller restart, cable fault, and communication loss.
- Debounce without hiding rapid fault transitions; preserve raw transition count where useful.
- Rate-limit automated outputs and require operation-level authorization.
- Keep observation inputs physically/logically separate from actuation outputs.
- Audit request, controller result, output state, independent sensed state, and time quality separately.

Dry contacts are intentionally simple. Do not invent identity, encryption, message integrity, sequence, or supervision properties they do not provide.

## Source boundary

- [IEC 60839-11-1:2013](https://webstore.iec.ch/en/publication/3662) supplies the official catalogue scope for electronic access-control system and component requirements.
- [IEC 62642-1:2010](https://webstore.iec.ch/en/publication/7298) supplies the official catalogue scope for intrusion and hold-up alarm system requirements.
- [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) supplies the OT safety, reliability, segmentation, and operational framing used here.

Catalogue scope does not supply wiring values or product acceptance criteria. Resistor values, circuit classes, terminals, ratings, release behavior, and acceptance criteria must come from the applicable licensed normative text, approved design, and exact product documentation.
