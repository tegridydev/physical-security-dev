---
title: KNX Secure
summary: KNX IP Secure and Data Secure scope, key lifecycle, commissioning, replay protection, migration, and operational controls.
page_type: protocol
domains: [bms, cross-domain]
tags: [knx-secure, data-secure, ip-secure, aes-ccm, keyring]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [KNX Secure, ISO 22510]
coverage_limit: Detailed algorithms, telegram formats, commissioning sequences, and certification requirements remain normative KNX specification material.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# KNX Secure

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / [KNX](knx.md) / Secure

KNX Secure has two complementary scopes. **KNX IP Secure** protects KNXnet/IP communication between IP endpoints. **KNX Data Secure** protects selected KNX group/object data across supported media so protection can survive routers. KNX Association describes AES-128 CCM-based confidentiality and integrity and identifies KNX IP Secure as standardized in ISO 22510.[^iso][^overview]

Using one does not imply the other. An IP-secured backbone can still carry unprotected application telegrams onto a field segment, while Data Secure does not automatically protect device web interfaces, ETS tunnelling, or unrelated management traffic.

## Commissioning trust

Secure commissioning depends on authentic device bootstrap information, the approved ETS project, and its generated keyring. Factory Device Setup Keys (FDSKs) and project keys are secrets—not asset labels. Capture them through an authorized process, restrict export, avoid screenshots/logging, and record which project/keyring version was deployed.

Operational design must cover:

- unique device enrolment and replacement rather than shared fleet secrets;
- group-security assignment and the impact of one group member compromise;
- sequence/freshness state across reboot, restore, cloning, and device replacement;
- keyring backup, recovery, rotation, revocation, and technician offboarding;
- mixed secure/unsecure devices and explicit downgrade prevention;
- audit of project changes, secure-mode changes, key export, and commissioning access.

Do not reset secure state or reprogram a live device simply to recover sequence synchronization. Follow the exact ETS and product recovery procedure under change control; incorrect recovery can make legitimate telegrams fail or reintroduce old trust material.

## Gateway design

A gateway decrypting secure KNX and publishing plaintext to another API terminates the security boundary. Authenticate and authorize the downstream consumer, protect cached values and keys, and label the export as derived—not end-to-end KNX Secure. Conversely, a generic VPN does not turn endpoints into KNX IP Secure devices or provide group-level Data Secure semantics.

## Verification boundary

Confirm the precise product certification, firmware, supported secure roles, ETS version, DPT/group configuration, keyring, time/sequence behaviour, and fallback settings. Test enrolment, rotation, replacement, rollback, outage, and mixed-mode rejection only in a controlled project environment.

## Primary sources

[^overview]: [KNX Association — KNX Security overview](https://support.knx.org/hc/en-us/articles/360012630199-KNX-Security-overview)
[^iso]: [KNX Association — ISO standard for KNX IP Secure](https://www.knx.org/news/new-iso-standard-knx-ip-secure-becomes-worlds-first-vendor-independent-security-standard)
- [KNX Association — KNX Data Secure](https://support.knx.org/hc/en-us/articles/360012689639-KNX-Data-Secure)
- [KNX Association — configuring KNX Secure with ETS](https://www.knx.org/news/security-configuring-knx-secure-systems-ets)
- [KNX Association — security checklist](https://www.knx.org/knx-en/for-professionals/benefits/knx-secure/KNX-Security-Checklist-en.pdf)
