---
title: "Legacy reader interfaces: Wiegand and Clock-and-Data"
summary: "Defensive developer reference for Wiegand electrical signaling, credential bit formats, parity, Clock-and-Data variants, weaknesses, compensating controls, and OSDP migration."
page_type: protocol
domains: [access-control]
tags:
  - wiegand
  - clock-and-data
  - legacy
scope: global
content_status: maintained
technology_status: legacy
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "SIA AC-01-1996.10: 26-BIT Wiegand Reader Interface"
coverage_limit: "Defensive format and migration guidance only; licensed electrical values, vendor Clock-and-Data variants, credential capture/replay, GPIO, reader, controller, and door behavior are not validated."
languages: [Python]
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Legacy reader interfaces: Wiegand and Clock-and-Data

[Access-control protocols](README.md) / Legacy reader interfaces

Legacy reader links usually convert a credential interaction into a static bit/character sequence sent from reader to controller. The **electrical interface** and the **credential bit format** are separate. “Wiegand” can mean the D0/D1 signaling interface, a specific 26-bit SIA format, or one of many unrelated vendor bit layouts; integration documents must say which. [SIA-WIEGAND]

## Status and risk posture

SIA AC-01-1996.10 defines the 26-bit Wiegand reader interface and was published in 1996. SIA describes Wiegand-style deployments as legacy, one-way, unsupervised, and cleartext compared with OSDP Secure Channel. Use OSDP Secure Channel for new designs and plan migration for existing high-value openings. [SIA-WIEGAND] [SIA-MIGRATE]

Legacy does not mean immediately removable: fire/life-safety constraints, panel capability, tenant disruption, wiring, power, and credential population can require a staged transition. Record and accept compensating risk explicitly.

## Wiegand D0/D1 signaling

Typical behavior uses two data lines:

- idle state is high through pull-ups;
- a pulse on Data 0 conveys a binary `0`;
- a pulse on Data 1 conveys a binary `1`;
- pulse width and inter-pulse timing delimit bits;
- a sufficiently long gap identifies the end of a bit string;
- data normally flows reader to controller; auxiliary LED/buzzer/hold lines are separate and vary.

Voltage, current, pull-up, timing, cable, power, grounding, and auxiliary-line requirements are installation-specific and normative in the applicable reader/panel documents and licensed SIA standard. Never connect general-purpose logic directly without correctly rated, isolated interface circuitry.

### Why it is weak

- No standard cryptographic confidentiality or message authentication on D0/D1.
- Static bit strings can be observed and replayed.
- Normal data flow is one-way, preventing cryptographic controller-to-reader challenges.
- Cable/device substitution is not inherently supervised.
- Format parity detects some transmission errors but is not an authenticity check.
- A strong smart-card interaction at the reader can be reduced to a replayable number on the panel link.

## Common 26-bit format

The standardized 26-bit layout is commonly represented as:

```text
bit:       1 | 2 ........ 9 | 10 ................ 25 | 26
meaning:  P1 | facility (8) | card/identifier (16)   | P2
```

`P1` provides even parity over the first half and `P2` provides odd parity over the second half under the SIA format. Parity proves only that the bit string satisfies that error-detection relation. It does not prevent copying or deliberate modification.

Not every 26-bit stream is necessarily provisioned under the same site allocation policy. Longer 32-, 34-, 35-, 36-, 37-, 40-, 48-, or other formats are not mutually interoperable merely because both endpoints accept that length. Record for every format:

- total bit length;
- parity bit positions and coverage;
- facility/company/site fields;
- credential/card fields;
- issue/region/type fields;
- bit order and numeric display convention;
- allocation authority, allowed ranges, and collision domain.

## Safe offline 26-bit decoder

**Target:** Offline parsing only—no GPIO, reader, card, panel, or capture interface.

**Inputs:** A caller-supplied synthetic 26-character `0`/`1` string.

**Side effects:** None.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Wiegand26:
    facility: int
    card: int
    even_parity_ok: bool
    odd_parity_ok: bool


def decode_sia_26(bits: str) -> Wiegand26:
    if len(bits) != 26 or set(bits) - {"0", "1"}:
        raise ValueError("expected exactly 26 binary characters")

    raw = [int(bit) for bit in bits]
    return Wiegand26(
        facility=int(bits[1:9], 2),
        card=int(bits[9:25], 2),
        even_parity_ok=sum(raw[0:13]) % 2 == 0,
        odd_parity_ok=sum(raw[13:26]) % 2 == 1,
    )
```

This does not decide whether a credential is authentic or authorized. Do not adapt it to capture, emulate, or replay real credentials without explicit authorization and a legitimate defensive purpose.

## Number and bit-order traps

- Printed decimal numbers may represent only one field, a concatenation, a vendor conversion, or a database ID unrelated to raw bits.
- Hexadecimal dumps can reverse byte order without reversing bit order, or vice versa.
- Leading zeroes are significant to a fixed-length format but disappear in integer conversion.
- A panel can truncate or pad unsupported lengths.
- Signed integer/database types can corrupt high-bit identifiers.
- Two facilities can issue the same card number; uniqueness usually requires a compound namespace.

Store raw format name/version, bit length, field values, and normalized credential mapping separately. Avoid using a display string as the canonical credential key.

## Keypads and auxiliary data

Keypads can emit individual digits or buffered codes in several Wiegand encodings, including vendor-specific formats. Define length, terminator, timeout, backspace/cancel, duress behavior, invalid digit handling, duplicate suppression, and whether a PIN is combined with a credential at the reader or controller. Never log plaintext PIN digits. Wiegand does not protect them in transit.

## Clock-and-Data

Clock-and-Data is a family of simplex reader interfaces in which one line marks clock transitions and another carries data state. Access-control products often refer to magnetic-stripe/ABA-style data, but the reader-to-controller electrical signaling, character framing, sentinel/LRC behavior, and magnetic-stripe recording standard are distinct layers. Vendor timing and voltage profiles vary.

ISO/IEC 7811-2:2018 is the current confirmed standard for low-coercivity magnetic-stripe recording and coded character sets. It does not, by itself, standardize every reader-controller Clock-and-Data implementation. [ISO7811-2]

Clock-and-Data has the same fundamental PACS concerns as Wiegand: cleartext, one-way delivery, static/replayable data, weak supervision, and format ambiguity. Treat magnetic data as untrusted and never store sensitive track content beyond documented need.

## Defensive controls when migration is delayed

- Protect reader cable in conduit/secure zones; inspect and tamper-monitor reader and junction points.
- Place door decision/control hardware on the secure side; a reader must not directly energize a lock merely from credential data.
- Use panel input/tamper monitoring and anomaly alerts, acknowledging it is not cryptographic link supervision.
- Limit facility/card ranges and reject unknown lengths/formats rather than auto-detecting broadly.
- Detect impossible travel, unusual repeated reads, reader offline/restart, sequence anomalies, and use outside assigned schedule—without treating analytics as proof.
- Combine with a second factor at higher-risk openings when policy and accessibility allow.
- Segment controller networks and secure upstream APIs/databases.
- Maintain a dated OSDP Secure Channel migration plan.

## Migration checklist

1. Inventory every reader, panel input, format, keypad, LED/buzzer/hold line, cable, distance, power, grounding, door mode, and life-safety dependency.
2. Identify shared facility/card collision domains and clean the credential database before conversion.
3. Select OSDP Verified ACU/PD products supporting required profile/features and unique-key Secure Channel.
4. Bench-test actual reader, credential types, panel firmware, long/poor cable conditions, keypad, feedback, tamper, restart, and failover.
5. Stage unique PD address and key inventory without storing keys in ordinary worksheets.
6. Cut over in phases; verify cleartext legacy inputs are disabled when no longer needed.
7. Remove converters after transition. A converter provides compatibility, not end-to-end Secure Channel.

## Review checklist

- [ ] Interface type separated from credential format
- [ ] Exact format length, fields, parity, bit order, numeric conversion, and collision scope documented
- [ ] Electrical/timing/power requirements taken from licensed standard and product docs
- [ ] Unsupported lengths/formats rejected; no broad auto-detection
- [ ] PIN/keypad data never logged and protected by compensating controls
- [ ] Static identifier never treated as cryptographic authentication
- [ ] Cable, reader, junction, panel, and secure-side lock control physically protected
- [ ] OSDP Secure Channel migration has owner, scope, and date
- [ ] Synthetic parity, boundary, invalid-character, leading-zero, and collision fixtures pass

## Sources

- **SIA-WIEGAND** — [SIA AC-01-1996.10: Access Control Standard Protocol for the 26-BIT Wiegand Reader Interface][SIA-WIEGAND], Security Industry Association, 1996.
- **SIA-MIGRATE** — [There Is a Hole in the Boat: Why Access Control Professionals Need to Move From Wiegand to OSDP][SIA-MIGRATE], Security Industry Association, 9 November 2021.
- **SIA-OSDP** — [Open Supervised Device Protocol][SIA-OSDP], Security Industry Association, accessed 2026-08-25.
- **SIA-CREDENTIAL-GUIDE** — [Corporate Credential Design Guide][SIA-CREDENTIAL-GUIDE], Security Industry Association, March 2026.
- **ISO7811-2** — [ISO/IEC 7811-2:2018: Magnetic stripe — Low coercivity][ISO7811-2], ISO, edition 5; confirmed 2024.

[SIA-WIEGAND]: https://www.securityindustry.org/industry-standards/sia-ac-01-1996-10/
[SIA-MIGRATE]: https://www.securityindustry.org/2021/11/09/there-is-a-hole-in-the-boat-why-access-control-professionals-need-to-move-from-wiegand-to-osdp/
[SIA-OSDP]: https://www.securityindustry.org/industry-standards/open-supervised-device-protocol/
[SIA-CREDENTIAL-GUIDE]: https://www.securityindustry.org/wp-content/uploads/2026/03/SIA_CorporateCredentialDesignGuide.pdf
[ISO7811-2]: https://www.iso.org/standard/73638.html
