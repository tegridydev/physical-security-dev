---
title: "Incident response and evidence"
summary: "Contain cyber compromise while preserving physical safety, critical services, trustworthy evidence, and recovery options."
page_type: operations
domains:
  - operations
tags:
  - incident-response
  - evidence
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-61 Rev. 3"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Incident response and evidence

[Home](../README.md) / [Operations and lifecycle](README.md) / Incident response and evidence

Responders must account for both cyber compromise and the continuing physical-security mission. Unplugging a controller, recorder, alarm communicator, intercom, gateway or time service can destroy evidence, remove coverage, create unsafe states, or trigger failover and dispatch.

## First decisions

1. Is any person, emergency function, egress path, gate/elevator movement, alarm signaling or critical facility state at immediate risk?
2. Which local authority controls physical actions and safety decisions?
3. Which functions can continue safely and which require compensating guards or procedures?
4. Which evidence is volatile, which system is authoritative, and which clocks are trustworthy?
5. Can containment be applied at identity, route, API, broker, service or device scope without broad shutdown?
6. Is an attacker actively using vendor cloud, support access, certificates, service accounts or physical wiring?

## Evidence collection record

Record collector and authority, time and time-source quality, asset/model/firmware, interface and command used, original output location, hash where appropriate, access controls, transformations, gaps and limitations. Preserve original logs, exports and configuration before normalizing them.

Relevant sources include device/controller logs, VMS/PACS/alarm audit, video/audio and export verification, identity and authorization decisions, API/broker logs, DNS/DHCP/NTP, network/firewall/NAC, remote support, cloud audit, configuration history, update records and physical access/tamper evidence.

## Containment hierarchy

Prefer narrow revocation of a token, account, certificate, topic permission, API role, route or destination before broad isolation. If a whole device/zone must be isolated, coordinate the resulting coverage and safe-state consequence. Do not erase, factory-reset or update suspected systems until evidence and recovery decisions are made unless immediate safety requires it.

## Recovery

Re-establish trusted identity, firmware/software, configuration, certificates/keys, time, and network policy from known-good sources. Reconcile controller/server/cloud state and queued events. The system owner and responsible safety authority must approve validation of denied, normal, degraded, and recovery behavior before return to service.

## Sources

- **NIST-800-61** — [NIST SP 800-61 Rev. 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management][NIST-800-61], final April 2025, accessed 2026-08-25.
- **NIST-800-86** — [NIST SP 800-86: Integrating Forensic Techniques into Incident Response][NIST-800-86], accessed 2026-08-25.
- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], OT safety and response context, accessed 2026-08-25.

[NIST-800-61]: https://csrc.nist.gov/pubs/sp/800/61/r3/final
[NIST-800-86]: https://csrc.nist.gov/pubs/sp/800/86/final
[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## Related pages

- [Logging, time, and evidence integrity](../06-security-and-assurance/logging-time-and-evidence-integrity.md)
- [Resilience, backup, and recovery](../06-security-and-assurance/resilience-backup-and-recovery.md)
- [Operational runbooks](runbooks.md)
