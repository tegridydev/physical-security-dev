---
title: AAA and network access
summary: 802.1X, EAP, RADIUS, LDAP, Active Directory, Kerberos, identity mapping, authorization, and accounting guidance.
page_type: reference
domains: [identity, networking, cross-domain]
tags: [aaa, 802-1x, eap, radius, ldap, active-directory, kerberos]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [IEEE 802.1X-2020, RFC 3748, RFC 2865, RFC 6614, RFC 4511, RFC 4120]
coverage_limit: General integration baseline; directory schema, EAP method, RADIUS attributes, authorization policy, and recovery design are deployment-specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# AAA and network access

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / AAA and network access

Authentication proves an identity to a defined assurance level. Authorization decides what that identity may do. Accounting records what was requested and decided. Keep network admission, device administration, operator login, API authorization, and physical-access decisions as separate policy layers even when they use the same directory.

## 802.1X, EAP, and RADIUS

IEEE 802.1X defines port-based network access control with a supplicant, authenticator (switch/access point), and authentication server.[^dot1x] EAP provides the authentication framework; an EAP method supplies actual credentials and security properties.[^eap] RADIUS commonly carries EAP and authorization attributes between authenticator and server.[^radius]

Design and test:

- machine/device identity, certificate issuance, private-key protection, trust roots, renewal, revocation, replacement, and clock dependency;
- authenticated server validation by the supplicant—without it, credentials may be offered to an impostor;
- exact EAP method and inner method; “supports 802.1X” is insufficient;
- VLAN/ACL/role result, reauthentication, session timeout, change of authorization, accounting, and failure/reject behaviour;
- boot sequencing when network, DNS, time, CRL/OCSP, directory, or RADIUS is unavailable;
- controlled critical/fallback VLANs that cannot become permanent bypasses.

MAC Authentication Bypass is possession of a spoofable address, not strong authentication. If unavoidable for legacy devices, isolate it to device-specific least privilege and pair it with switch-port/topology monitoring.

Classic RADIUS has legacy protection limitations. **RFC 6614 and RFC 9765 are both Experimental RFCs**, so publication alone is not a deployment recommendation. RFC 6614 encapsulates the existing RADIUS packet format in TLS and therefore retains MD5-based packet authenticators and attribute-obfuscation mechanisms inside the protected connection; validate TLS peer identity and never infer that the inner format was modernized.[^radsec] RADIUS/1.1 in RFC 9765 requires TLS 1.3, removes those MD5 packet mechanisms, and changes protocol behaviour, so it requires explicit client/server support and cannot be enabled as a transparent port change.[^radius11]

## LDAP, Active Directory, and Kerberos

LDAP v3 protocol operations are defined by RFC 4511; Kerberos V5 by RFC 4120.[^ldap][^kerberos] Active Directory combines LDAP directory access, Kerberos, DNS and Microsoft-specific protocols rather than being “just LDAP.”[^ad]

- Use TLS with full server identity validation or a product-supported signed/sealed bind. Do not send simple-bind passwords on plaintext LDAP.
- Use a dedicated service identity with minimum search base, attributes and operations; never bind an application as a domain administrator.
- Pin schema/attribute semantics and stable immutable identifiers. Display name, email, or DN can change and must not be the sole authorization key.
- Resolve nested groups, cycles, replication delay, disabled/deleted users, duplicate names, referral chasing, paging/size limits, and cache expiry explicitly.
- Fail closed for privileged commands while preserving an engineered local emergency/recovery path. Do not make door egress or certified life-safety behaviour depend on a live directory lookup.
- Prevent LDAP filters, DNs, log records, and UI labels from being constructed through unescaped user input.

Microsoft documents LDAP signing controls for Active Directory Domain Services; exact defaults and enforcement vary with supported Windows versions and configuration, so inspect the deployed policy rather than assuming.[^signing]

## Primary sources

[^dot1x]: [IEEE Standards Association — IEEE 802.1X-2020](https://standards.ieee.org/ieee/802.1X/7345/)
[^eap]: [RFC Editor — RFC 3748, EAP](https://www.rfc-editor.org/info/rfc3748/)
[^radius]: [RFC Editor — RFC 2865, RADIUS](https://www.rfc-editor.org/info/rfc2865/)
[^radsec]: [RFC Editor — RFC 6614, RADIUS over TLS](https://www.rfc-editor.org/info/rfc6614/)
[^radius11]: [RFC Editor — RFC 9765, RADIUS/1.1](https://www.rfc-editor.org/info/rfc9765/)
[^ldap]: [RFC Editor — RFC 4511, LDAP](https://www.rfc-editor.org/info/rfc4511/)
[^kerberos]: [RFC Editor — RFC 4120, Kerberos V5](https://www.rfc-editor.org/info/rfc4120/)
[^ad]: [Microsoft Open Specifications — Active Directory protocols overview](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adod/5ff67bf4-c145-48cb-89cd-4f5482d94664)
[^signing]: [Microsoft Learn — LDAP signing for Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-signing)
