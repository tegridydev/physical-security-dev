---
title: Protocol infrastructure
summary: Shared transport, discovery, time, identity, secure administration, serial, wireless, power, and physical-I/O foundations.
page_type: index
domains: [cross-domain, networking, ot]
tags: [networking, infrastructure, transport, identity, physical-io]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [IEEE 802, IETF RFCs, TIA-232, TIA-485, USB specifications]
coverage_limit: Cross-protocol engineering baseline; local electrical, radio, safety, network, and product requirements remain authoritative.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Protocol infrastructure

[Home](../../README.md) / [Protocols](../README.md) / Infrastructure

These pages cover the foundations reused by cameras, controllers, intercoms, alarms, building systems, and gateways. “Uses IP,” “uses TLS,” or “has an RS-485 port” is only a layer statement; the application protocol and operational contract still have to be identified.

| Concern | Reference |
|---|---|
| Ethernet, IPv4/IPv6, TCP/UDP, multicast, VLANs, NAT, segmentation | [IP transport and segmentation](ip-transport-and-segmentation.md) |
| DHCP, DNS, mDNS/DNS-SD, WS-Discovery, LLDP | [Discovery and addressing](discovery-and-addressing.md) |
| NTP/NTS, PTP, monotonic and event time | [Time synchronisation](time-synchronisation.md) |
| SNMP, syslog, SSH/SFTP, secure management | [Monitoring and secure administration](monitoring-and-secure-administration.md) |
| 802.1X/EAP/RADIUS, LDAP, Active Directory, Kerberos | [AAA and network access](aaa-and-network-access.md) |
| SAML 2.0, OpenID Connect, OAuth security, enterprise SSO | [Enterprise federation with SAML and OIDC](enterprise-federation-saml-and-oidc.md) |
| SCIM provisioning, joiner/mover/leaver, reconciliation, asynchronous signals | [SCIM identity provisioning](scim-identity-provisioning.md) |
| WebAuthn, FIDO2, CTAP, passkeys, cross-device authentication | [WebAuthn, FIDO, and passkeys](webauthn-fido-and-passkeys.md) |
| TLS, mutual TLS, X.509 and certificate operations | [TLS, PKI, and secure transport](tls-pki-and-secure-transport.md) |
| UART, TIA-232/422/485 and serial gateways | [Serial transports](serial-transports.md) |
| Wi-Fi, Bluetooth, Zigbee, Thread, Z-Wave, LoRaWAN, NFC | [Wireless and low-power links](wireless-and-low-power.md) |
| PoE, USB, GPIO, relay and supervised circuits | [Power, USB, and GPIO](power-usb-and-gpio.md) |

## Shared rule

For each dependency record protocol/version, endpoint and authenticated identity, addresses, ports/media, direction, expected rates, timeout/retry, maximum sizes, trust roots or keys, authorization, clock dependency, monitoring, owner, safe failure, and recovery. Discovery output and source addresses populate candidates; they do not establish identity or authorization.

## Safety boundary

Network scans, multicast discovery, time changes, AAA changes, serial attachment, radio commissioning, PoE cycling, USB insertion, GPIO drive, and relay operation can interrupt or actuate physical-security systems. These references grant no authority for those actions. Use offline configuration review for research and the asset owner's approved commissioning process for environment acceptance.

## Primary source directories

- [RFC Editor](https://www.rfc-editor.org/)
- [IEEE 802 standards](https://standards.ieee.org/standard/802_1X-2020.html)
- [USB-IF document library](https://www.usb.org/documents)
- [TIA standards store](https://tiaonline.org/products-and-services/buy-standards/)
