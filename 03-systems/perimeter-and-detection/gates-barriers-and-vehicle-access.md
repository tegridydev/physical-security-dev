---
title: Gates, Barriers, and Vehicle Access
summary: Separates vehicle entitlement, movement control, safety functions, position evidence, and operational recovery for powered access machinery.
page_type: system
domains: [access-control, ot, alarms, video]
tags: [gates, barriers, vehicle-access, machinery-safety]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: ["ISO 12100:2010", "ISO 14118:2017"]
coverage_limit: Safety-oriented architecture only; no wiring, force/speed/timing values, motion commands, safety-device placement, code selection, bypass, or commissioning procedure.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Gates, barriers, and vehicle access

Powered gates and barriers are machinery. Access control may request passage, but the approved gate controller and safety functions decide whether and how movement occurs. Never treat a generic relay, PACS grant, ANPR match, or API success as motion authority or proof of safe passage.

## Authority chain

```text
credential/plate/intercom/operator observation
 -> PACS or approved access-policy decision
 -> constrained open-cycle request
 -> gate controller evaluates mode, interlocks, and safety devices
 -> controlled movement
 -> position/presence/safety telemetry
 -> passage event and audit
```

Emergency stop, manual release, fire/emergency interaction, safety edges, presence detection, guarding, limits, drive control, and restart behavior belong to the assessed machinery design. Integration must not bypass them.

## Separate states

Model at least:

- access request, decision, reason, credential/vehicle context, and expiry;
- controller mode: automatic, manual, service, emergency, locked out, or unknown;
- requested cycle versus accepted/rejected command;
- physical position: open, closed, intermediate, moving, unknown, and sensor disagreement;
- safety-device active/fault, obstruction/presence, emergency stop, and interlock state;
- vehicle approach, authorized passage, tailgate/second passage, reverse, and abandoned transit where observed;
- power, network, controller, drive, communications, and clock fault;
- forced/manual movement, held-open/forced-open, and restoration.

Do not derive position solely from elapsed time after a command. Where several sensors disagree, report disagreement rather than selecting a convenient state.

## Vehicle authorization

Credentials, ANPR/LPR, mobile credentials, ticketing, intercom release, schedule, occupancy/capacity, and operator action can contribute to policy. A plate alone is not a person or entitlement. Define fallback for unreadable plates, lost connectivity, stale allowlists, multiple vehicles, trailers, motorcycles, visitors, and emergency response without weakening safety control.

Anti-passback and occupancy estimates can be wrong after tailgating, manual operation, sensor failure, or offline use. They are not safety-rated presence systems or evacuation truth.

## Machinery and life-safety boundary

Risk assessment must cover people, vehicles, cyclists, animals, crushing/shearing/drawing-in/impact hazards, trapping areas, public access, foreseeable misuse, environment, power loss/return, manual operation, maintenance, and unexpected startup. Use the applicable local gate/door product and installation standards and competent authorized practitioners.

[ISO 12100:2010](https://www.iso.org/standard/51528.html) provides general machinery risk-assessment and risk-reduction principles; ISO marks it as expected to be replaced, so check status before use. [ISO 14118:2017](https://www.iso.org/standard/66460.html) addresses prevention of unexpected machinery startup. Neither substitutes for the applicable gate-specific and local requirements.

## Security and integration

- Use a semantic, bounded passage request rather than unrestricted relay/register access.
- Separate PACS, gate-maintenance, safety-controller, intercom, and monitoring identities and privileges.
- Protect remote control and mobile clients with strong identity, constrained site/device scope, confirmation, and audit.
- Segment OT control from general user and cloud networks according to assessed dependencies.
- Validate command authentication, replay/duplicate behavior, queueing, timeout, failover, and recovery.
- Expose stale telemetry and lost safety/controller communication prominently.
- Prevent automated cross-domain rules from cycling a gate on an unverified alarm or analytics event.

## Acceptance boundary

Security integration evidence includes identity, policy, command scope, state correlation, failure visibility, and audit. Machinery safety validation, force/movement testing, emergency coordination, and live commissioning require the approved local process, competent specialists, manufacturer instructions, and applicable normative requirements.

See [ANPR and LPR systems](anpr-lpr-systems.md), [Offline operation and anti-passback](../access-control/offline-operation-and-anti-passback.md), and [BMS and SCADA integration](../integration-platforms/bms-and-scada-integration.md).

Return to [Perimeter and detection systems](README.md).
