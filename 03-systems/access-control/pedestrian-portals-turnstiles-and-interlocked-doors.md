---
title: "Pedestrian portals, turnstiles, and interlocked doors"
summary: "System guidance for pedestrian access portals, passage-state integration, machinery safety, egress, accessibility, privacy, and defensible acceptance evidence."
page_type: system
domains: [access-control, building-industrial]
tags:
  - turnstiles
  - speed-lanes
  - security-vestibules
  - pedestrian-gates
  - passage-control
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "IEC 60839-11-1:2013"
  - "EN 17352:2022"
  - "ISO 12100:2010"
coverage_limit: "Architecture and risk boundaries only; equipment selection, guarding, force/speed values, safety functions, egress, accessibility, fire integration, and acceptance criteria require the exact product, site risk assessment, adopted law, and qualified approval."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Pedestrian portals, turnstiles, and interlocked doors

[Access-control systems](README.md) / Pedestrian portals

Pedestrian access-control equipment combines authorization, moving machinery, presence sensing, passage detection, building circulation, accessibility, and emergency egress. The access-control system can request a passage, but the portal's approved local control and safety functions must decide whether and how motion occurs.

Use **security vestibule** or **interlocked-door system** for the two-door arrangement when that is the intended design. **Mantrap** is retained only as a legacy search term: it is imprecise, can obscure egress and accessibility duties, and should not appear as the primary system or user-interface label.

## Equipment families

| Family | Typical purpose | Integration caveat |
|---|---|---|
| Tripod or waist-high turnstile | Metered pedestrian entry with a rotating barrier | Does not prevent climbing, bypass, or unsafe use; passage and rotation sensing vary |
| Full-height turnstile | Higher physical resistance and one-person sequencing | Egress, rescue access, entrapment, accessibility, and adjacent bypass routes require explicit design |
| Optical turnstile / speed lane | Sensor-based passage detection with moving leaves or an open lane | Tailgating algorithms are probabilistic and sensitive to bags, mobility aids, groups, and sensor conditions |
| Powered pedestrian gate | Wider accessible or service passage | Must not become a lower-assurance bypass; machinery and latch/lock states remain separate |
| Security revolving door | Controlled circulation through rotating compartments | Occupancy, anti-piggybacking, emergency opening, and machinery safety are product-specific |
| Security vestibule / interlocked doors | Sequentially controlled doors with an intermediate space | Presence or identity checks never remove required release, communication, rescue, and egress provisions |

These names are categories, not performance or conformity claims. Record the exact product type, intended users, throughput, operating modes, safety-rated functions, and approvals.

## Standards and authority boundary

- [IEC 60839-11-1:2013](https://webstore.iec.ch/en/publication/3662) provides electronic access-control system and component requirements.
- [EN 17352:2022](https://www.nen.nl/en/nen-en-17352-2022-en-294705) addresses safety in use for power-operated pedestrian entrance-control equipment. Its published scope excludes some vulnerable-user, special-needs, and unsupervised-young-child cases, so it is not a complete accessibility or inclusive-use basis.
- [ISO 12100:2010](https://www.iso.org/standard/51528.html) supplies general machinery risk-assessment and risk-reduction principles.

Those standards have different scope. Product standards, machinery rules, building/fire/egress/accessibility law, electrical requirements, workplace obligations, and the authority having jurisdiction may also apply. A PACS standards claim does not establish machinery safety or code-compliant egress, and a machinery conformity claim does not establish secure identity or access authorization.

## System boundaries

```text
credential / visitor / operator policy
                 │
                 ▼
PACS decision ── passage request ──> portal controller
                                       ├─ local motion sequence
                                       ├─ safety sensors and protective functions
                                       ├─ barrier/door/lock monitoring
                                       └─ approved emergency and egress behavior
                 ▲
passage and fault events ──────────────┘
```

Keep at least these controllers and authorities explicit:

- PACS identity, access decision, schedules, anti-passback, and audit;
- portal machinery sequence, motion control, and local safety functions;
- independent emergency/fire release where the approved design requires it;
- building management observation, which should not silently own safety or authorization;
- local staff, guards, facilities personnel, and emergency responders;
- vendor remote support and maintenance modes.

The interface should expose named, bounded operations such as an authorized entry cycle or approved mode change. Avoid integrations that directly toggle motors, brakes, raw relays, safety inputs, or sensor bypasses.

## Passage-state model

An access grant, a portal opening, and a person completing passage are different facts. A useful state model separates:

1. credential or identity presentation;
2. access decision and reason;
3. direction and lane selected;
4. passage request accepted or rejected by the portal controller;
5. barrier/door movement and safe-ready state;
6. entry into the detection/vestibule zone;
7. completed, reversed, timed-out, or ambiguous passage;
8. barrier/door returned to its secure and safe state;
9. independent evidence such as door/leaf position, lock monitor, occupancy, or rotation count;
10. tailgating, wrong-way, obstruction, tamper, forced movement, or equipment fault.

Use a correlation identifier that survives controller and PACS retries. Record occurrence and receive times separately. Do not invent a successful passage when only the access decision or command acknowledgement exists.

### Ambiguous outcomes

People can stop, reverse, pass belongings, accompany another person, use a mobility aid, or enter side by side. A sensor can be obscured or incorrectly classify a passage. After an ambiguous outcome:

- preserve the original sensor/portal event and confidence or reason;
- avoid automatic punitive identity action based on a single ambiguous classification;
- reconcile anti-passback and occupancy through an approved exception process;
- route safety, obstruction, or entrapment indications to the responsible local workflow;
- do not issue an automatic second movement request merely because an acknowledgement was lost.

## Safety and risk assessment

The site risk assessment should cover intended use and reasonably foreseeable misuse across normal, degraded, maintenance, emergency, and rescue modes. Relevant hazards can include impact, crushing, shearing, drawing-in, entanglement, falls, entrapment, panic, crowd pressure, electrical energy, unexpected restart, and unsafe security behavior.

Risk controls belong in an engineered hierarchy: inherently safer design, guards/protective measures, safety-related control functions, information, training, and operating procedure. Software logging or analytics does not replace a protective device or approved safety function.

At minimum, account for:

- children, older people, pregnancy, mobility aids, assistance animals, luggage, deliveries, and accompanied users;
- single and multiple persons, wrong-way approach, loitering, obstruction, and attempted bypass;
- sensor contamination, misalignment, blind zones, reflective clothing, lighting, and environmental conditions;
- loss and restoration of power, network, PACS, time, sensor, actuator, brake/lock, and controller;
- emergency release, evacuation flow, first-responder entry, manual override, and rescue from the intermediate space;
- maintenance access, stored energy, inhibit/bypass control, and return to service;
- adjacent accessible and emergency routes, including their equivalent security monitoring.

Exact force, speed, clearance, timing, safety performance level, and protective-device placement are product- and site-specific. Use the current product standard, manufacturer instructions, approved design, and competent machinery/fire/accessibility review.

## Egress and emergency modes

Normal access denial must never be treated as authority to block required egress. Document the priority and ownership of:

- normal entry and exit;
- free or controlled egress as legally approved;
- fire alarm or emergency release;
- evacuation and crowd mode;
- lockdown/security emergency mode;
- power failure and depleted backup power;
- manual key, mechanical, or local override;
- rescue and emergency-service access;
- return from emergency to normal service.

The effective behavior is the combination of portal mechanics, locks, release circuits, PACS logic, fire interfaces, power supplies, surrounding doors, barriers, and operating procedure. See [Locks, egress, and life-safety boundaries](locks-egress-and-life-safety.md).

## Accessibility and equitable use

Accessibility is a route and service outcome, not merely the presence of one wide gate. Review clear passage, approach/turning space, reach and presentation zones, operating force, timing, visual/audible/tactile feedback, contrast, signage, queuing, assistance, emergency use, and privacy.

The accessible lane should offer equivalent security, dignity, availability, and response time. Do not require a person to disclose disability to receive ordinary access, and do not treat slower movement, an assistant, a mobility aid, or an assistance animal as a security anomaly by default.

## Security and privacy

- Bind each request to authenticated identity, site, lane, direction, time, and permitted operation.
- Separate ordinary passage, visitor/escort, delivery, accessibility, maintenance, emergency, hold-open, and security override permissions.
- Protect controller management, firmware, safety configuration, sensor calibration, and remote support as privileged functions.
- Supervise communications and physical enclosures without allowing a network fault to defeat required local safety.
- Minimize and retain only the passage, image, biometric, occupancy, and exception data needed for an approved purpose.
- Inform users where camera or biometric classification is used and provide a lawful, accessible alternative.
- Measure tailgating performance across representative users and conditions; do not market an algorithm as proof of individual identity.
- Keep video/analytics correlation separate from PACS truth and preserve uncertainty.

For credential and controller boundaries, see [PACS architecture](pacs-architecture.md), [Panels, readers, and door I/O](panels-readers-and-door-io.md), and [Offline operation and anti-passback](offline-operation-and-anti-passback.md).

## Degraded and maintenance behavior

Define behavior for PACS unavailable, portal controller unavailable, network partition, stale authorization cache, sensor failure, barrier obstruction, safety-device trip, battery condition, emergency input fault, and unavailable staff response. Local required safety behavior must not depend on cloud or enterprise availability.

Maintenance mode needs named authorization, physical control of the work area, energy-isolation procedure where applicable, visible indication, time limit, event logging, and an independent return-to-service check. A remotely cleared fault should not automatically restart motion when a person may still be in the hazard zone.

## Acceptance evidence

The system record should include:

- adopted standards, local authority decisions, risk assessment, intended use, and approved operating modes;
- product declarations/listings, manuals, safety-function design, drawings, firmware, and configuration baseline;
- interface contract between PACS, portal controller, emergency/fire functions, and monitoring;
- complete passage-state mapping, timestamp/correlation behavior, and ambiguous-outcome handling;
- representative users, mobility aids, luggage, accompanied passage, wrong-way travel, obstruction, and bypass scenarios;
- power, network, controller, sensor, lock/brake, emergency input, manual override, and restart behavior;
- accessible route and equivalent-security evidence;
- emergency release, evacuation, rescue, responder access, and restoration approvals;
- privacy assessment, retention, operator permissions, maintenance access, and incident response;
- independent distinction among authorization, command acceptance, machinery state, and completed passage.

Physical acceptance testing requires the system owner, machinery-safety and building/fire/accessibility stakeholders, controlled occupancy, emergency stop/override arrangements, and a site-specific method approved before movement.

## Primary sources

- IEC, [IEC 60839-11-1:2013](https://webstore.iec.ch/en/publication/3662), electronic access-control system requirements.
- NEN, [EN 17352:2022 catalogue record](https://www.nen.nl/en/nen-en-17352-2022-en-294705), current status and public scope for power-operated pedestrian entrance-control equipment safety in use.
- ISO, [ISO 12100:2010](https://www.iso.org/standard/51528.html), machinery safety risk assessment and risk reduction.
