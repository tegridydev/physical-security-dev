---
title: Verification and Safety
summary: Explains evidence levels, runtime claims, and safety gates for cyber-physical integrations.
page_type: guide
domains: [cross-domain]
tags: [verification, safety, evidence, testing]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [NIST SP 800-82 Rev. 3]
coverage_limit: General process only; site safety and regulatory approval remain local responsibilities.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Verification and safety

Physical-security software can observe people, grant access, suppress or generate alarms, move equipment, and change emergency response. Verification must therefore cover both information behaviour and physical consequence.

## Evidence levels

| Level | Evidence available | What may be claimed |
|---|---|---|
| `V0` | Draft notes, secondary material, or unresolved contradictions | Nothing beyond clearly marked work in progress |
| `V1` | Applicable primary sources reviewed and scope stated | Source-verified description within that scope |
| `V2` | V1 plus practical cross-check and static consistency review | Reviewed guidance; still no runtime or interoperability claim |
| `V3` | Authorized test with exact environment, procedure, expected/actual results, and evidence | Only the behaviour actually observed in that environment |

Source review is not execution. Execution is not conformance. A successful test of one firmware build is not proof for a product family, and conformance to a profile is not proof that two optional feature sets meet a project's use case.

## Verification layers

Verify independently:

1. **Syntax:** encoding, frame, schema, and message parsing.
2. **Protocol state:** sequencing, correlation, timeout, retry, reconnect, and error handling.
3. **Semantics:** identities, units, state transitions, timestamps, priorities, and authority.
4. **Security:** peer identity, authorization, certificate/path validation, replay resistance, secrets, and audit.
5. **Interoperability:** exact client/server/device versions and negotiated options.
6. **Operations:** upgrades, restart, clock loss, partial outage, certificate rotation, and recovery.
7. **Physical outcome:** independent observation of intended and unintended effects.

## Safety gate for actuation

Do not perform an actuation test merely because the protocol call is understood. Before any live test, the system owner and validation lead should establish:

- written authorization and named site/safety owners;
- an exact target and excluded systems;
- a maintenance window and notification plan;
- an isolated test device or proven non-actuating mode where possible;
- independent state observation, not only the requesting application's response;
- abort conditions, rollback, manual override, and recovery personnel;
- preservation of egress, fire, emergency communication, and other independent safeguards;
- data-handling rules for images, audio, credentials, biometrics, and logs.

NIST's [Guide to Operational Technology Security, SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) explicitly includes physical access control and building automation within OT and emphasizes performance, reliability, and safety constraints. The knowledge base adopts that conservative framing wherever software can affect the physical environment.

## Recording environment validation

Only upgrade an exact page claim or example to `V3` when a reviewer accepts a [runtime validation record](../10-sources-and-maintenance/templates/runtime-validation-record-template.md) containing:

- date, operator, authorization reference, and environment isolation;
- exact hardware, firmware, software, library, configuration, and network path;
- sanitized inputs and expected results;
- actual results, timestamps, logs or trace identifiers, and deviations;
- negative/degraded cases attempted;
- cleanup/recovery confirmation;
- the narrow claim supported by the evidence.

Never store live passwords, tokens, private keys, biometric templates, card secrets, access codes, resident data, or unredacted surveillance evidence in this library.

See the detailed [verification policy](../10-sources-and-maintenance/verification-policy.md) and [environment validation checklist](../10-sources-and-maintenance/manual-qa-checklist.md).
