# Physical Security Dev Notes

**Physical Security Dev Notes** is an open-source, plain-Markdown knowledge base for developers and integrators working across video surveillance, physical access control, alarm monitoring, intercom, building automation, OT, identity, and their supporting network services. It explains how systems fit together, what each protocol actually guarantees, where legacy risk remains, and how to build integrations that fail safely.

The canonical repository is [tegridydev/physical-security-dev](https://github.com/tegridydev/physical-security-dev). The library is designed to be cloned and used locally without a documentation server or build step.

The library is **protocol first**, global in scope, and evidence led. It is not a replacement for a standard, a product manual, an authority having jurisdiction, or a qualified fire, electrical, life-safety, locksmithing, privacy, or security professional.

## Start here

- [How to use this knowledge base](00-start-here/how-to-use-this-knowledge-base.md)
- [Scope and boundaries](00-start-here/scope-and-boundaries.md)
- [Learning paths](00-start-here/learning-paths.md)
- [Verification and safety](00-start-here/verification-and-safety.md)
- [Glossary and naming conventions](00-start-here/glossary-and-conventions.md)
- [Canonical protocol landscape](physical-security-protocol-landscape.md)

## Library map

| Section | Purpose |
|---|---|
| [00 Start here](00-start-here/README.md) | Orientation, learning paths, scope, terminology, and safe use |
| [01 Foundations](01-foundations/README.md) | Architecture, networking, media, identity, time, field wiring, reliability, and trust |
| [02 Protocols](02-protocols/README.md) | Protocol families, wire behaviour, security properties, and implementation concerns |
| [03 Systems](03-systems/README.md) | Cameras, VMS, PACS, alarms, intercoms, PSIM, BMS, SCADA, and identity systems |
| [04 Vendor APIs](04-vendor-apis/README.md) | Publicly documented vendor interfaces with explicit product/version limits |
| [05 Development and integration](05-development-and-integration/README.md) | Adapter design, event processing, schemas, resilience, and language guidance |
| [06 Security and assurance](06-security-and-assurance/README.md) | Threat modelling, hardening, certificates, API security, privacy, and assurance |
| [07 Operations and lifecycle](07-operations-and-lifecycle/README.md) | Commissioning, inventory, monitoring, backup, incident handling, and retirement |
| [08 Defensive labs](08-defensive-labs/README.md) | Synthetic, offline, tabletop, calculation, and loopback-simulation exercises |
| [09 Reference](09-reference/README.md) | Matrices, ports, statuses, glossary, and quick-reference material |

## Evidence model

Every substantive page carries YAML metadata and a verification state:

| State | Meaning |
|---|---|
| `V0` | Draft, incomplete, or containing unresolved material claims |
| `V1` | Material claims checked against primary sources for the stated coverage |
| `V2` | Primary-source checked, cross-checked where practical, and statically reviewed |
| `V3` | Environment validated for an exact claim in a recorded evidence set |

`V2` does **not** mean product conformance, interoperability, regulatory approval, or successful execution. `V3` requires a linked, narrowly scoped evidence record reviewed under the [verification policy](10-sources-and-maintenance/verification-policy.md).

## Safe-use rules

- Treat commands, payloads, and code as explanatory unless their page says otherwise.
- Never aim exploratory traffic at a system without written authorization and an agreed test window.
- Keep door, gate, lift, fire, alarm, relay, lockdown, and emergency-control work non-actuating until it has passed the site's engineering and safety process.
- Use synthetic identities, documentation address ranges, `.example` names, and secret placeholders.
- Prefer observation, vendor-supported diagnostics, and reversible changes. Preserve evidence and an independent recovery path.

## Current baseline

The source and status baseline was reviewed on **2026-08-25**. Time-sensitive highlights, including ONVIF Profile V's Release Candidate status and Profile S's scheduled support end, are dated and linked in the [landscape](physical-security-protocol-landscape.md). The [original dated landscape filename](<CCTV, Access Control & Physical Security Protocol Landscape — 2026.md>) remains as a navigation-only compatibility pointer. Consult the relevant standard, conformance database, product documentation, and advisories before making a deployment decision.

## License

open~knowledge 2026 tegridydev.

Unless otherwise noted, original repository prose, metadata, diagrams, tables, examples, and code snippets are available under the [MIT License](LICENSE.md). Vendor names, trademarks, standards, specifications, quotations, and linked third-party materials remain the property of their respective rights holders and are not relicensed by this repository.
