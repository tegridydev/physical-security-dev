---
title: Monitoring and secure administration
summary: SNMP, syslog, SSH, SFTP, management-plane isolation, telemetry quality, and safe administrative operations.
page_type: reference
domains: [networking, cross-domain]
tags: [snmpv3, syslog, ssh, sftp, monitoring, management-plane]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [RFC 3411, RFC 3414, RFC 3826, RFC 7860, RFC 5424, RFC 5425, RFC 4251, RFC 8332, RFC 9142]
coverage_limit: Protocol and operational baseline; product MIBs, command sets, SSH algorithms, log schemas, and retention policy remain system-specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Monitoring and secure administration

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / Monitoring and administration

Monitoring observes a system; administration changes it. Keep those identities, network paths, credentials, authorization, and audit streams separate. Do not expose management services merely because a device's operational protocol must be reachable.

## SNMP

SNMP uses managers, agents, MIB modules and object identifiers. Polling, notifications, and SET operations have different failure and consequence models. The SNMP architecture is defined by RFC 3411; SNMPv3 User-based Security Model (USM) is RFC 3414.[^snmp][^usm]

- Prefer SNMPv3 with authentication and privacy (`authPriv`) when the product supports it. RFC 7860 defines SHA-2 authentication protocols for USM, and RFC 3826 defines AES privacy; verify the exact product combinations and key-localization lifecycle rather than treating `SNMPv3` as one fixed suite.[^usmsha2][^usmaes] SNMPv1/v2c community strings are reusable cleartext-equivalent secrets, not modern identities.
- Give each manager a least-privilege view. Disable SET or use a separate tightly controlled identity unless a documented operational need exists.
- Preserve OID, syntax, units, scale, counter width/wrap, source, poll time, response status, and quality. Vendor MIB revision is part of the schema.
- Treat a trap as unacknowledged delivery; an inform has protocol acknowledgement, not proof that the incident system processed it.
- Protect authoritative engine ID and engine boots/time state. Cloned/replaced SNMP engines and counter resets require explicit handling.
- Bound walks and table sizes. Broad GETBULK requests can overload small embedded agents.

## Syslog

RFC 5424 defines a structured syslog message with facility, severity, timestamp, host/application/process/message identifiers, structured data, and message. RFC 5425 maps syslog over TLS.[^syslog][^syslogtls] Preserve raw bounded records or tamper-evident references plus parsed fields. Vendor severity is not automatically incident severity.

Define transport/framing, TLS identity, maximum message, queue/disk limits, reconnect/backoff, loss counters, clock-quality handling, parsing version, retention, privacy/redaction, and backpressure. UDP syslog can lose/reorder/duplicate; TCP delivery can still be lost before durable ingestion; TLS protects a hop, not downstream storage integrity.

## SSH and SFTP

SSH architecture is RFC 4251.[^ssh] Pin or validate host keys through an approved provisioning channel; never accept a changed host key silently. Use named service accounts, public-key or hardware-backed authentication, algorithms consistent with the current RFC 9142 recommendations, and RSA/SHA-2 signatures from RFC 8332 where RSA remains necessary.[^sshalg][^sshrsa] Restrict commands/subsystems and sources, keep sessions short, and retain complete administrative audit. Disable password/default accounts where operational recovery permits.

SFTP is the SSH File Transfer Protocol subsystem, not FTP over SSH and not necessarily SCP. Its later protocol versions remained IETF Internet-Drafts rather than an RFC; confirm the implemented SFTP version and extensions for both products.[^sftp] Upload configuration atomically where supported, validate size/hash/schema, protect permissions, and retain rollback. A successful file transfer is not proof the device safely applied the configuration.

## Management plane

Place operator/admin clients, jump hosts, update repositories, AAA, time, logging, and device management endpoints in explicit management conduits. Record emergency access, credential escrow, offline recovery, certificate/key rotation, configuration backup, four-eyes approval for high-impact commands, session recording policy, and vendor-support expiry. Never test restart, reset, firmware upload, configuration import, SNMP SET, or log-flood behaviour on live physical-security devices.

## Primary sources

[^snmp]: [RFC Editor — RFC 3411, SNMP management architecture](https://www.rfc-editor.org/info/rfc3411/)
[^usm]: [RFC Editor — RFC 3414, SNMPv3 USM](https://www.rfc-editor.org/info/rfc3414/)
[^usmsha2]: [RFC Editor — RFC 7860, HMAC-SHA-2 authentication protocols in USM](https://www.rfc-editor.org/info/rfc7860/)
[^usmaes]: [RFC Editor — RFC 3826, AES privacy protocol in USM](https://www.rfc-editor.org/info/rfc3826/)
[^syslog]: [RFC Editor — RFC 5424, syslog protocol](https://www.rfc-editor.org/info/rfc5424/)
[^syslogtls]: [RFC Editor — RFC 5425, TLS transport mapping for syslog](https://www.rfc-editor.org/info/rfc5425/)
[^ssh]: [RFC Editor — RFC 4251, SSH architecture](https://www.rfc-editor.org/info/rfc4251/)
[^sshalg]: [RFC Editor — RFC 9142, SSH key-exchange method recommendations](https://www.rfc-editor.org/info/rfc9142/)
[^sshrsa]: [RFC Editor — RFC 8332, RSA keys with SHA-2 signatures in SSH](https://www.rfc-editor.org/info/rfc8332/)
[^sftp]: [IETF Datatracker — SSH File Transfer Protocol draft 13](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13)
