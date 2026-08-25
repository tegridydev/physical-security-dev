---
title: "MQTT TLS and ACL review"
summary: "Review MQTT client identity, topic authorization, session state, retained data, queues, and TLS from offline fixtures."
page_type: lab
domains:
  - integration
tags:
  - mqtt
  - tls
  - acl
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "MQTT Version 5.0"
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# MQTT TLS and ACL review

[Home](../README.md) / [Defensive labs](README.md) / MQTT TLS and ACL review

Lab class: **Offline configuration/trace fixture or loopback protocol simulation**

## Procedure

1. Record the broker/product/version represented by the fixture, MQTT version, listener model, TLS policy, and client identity mechanism.
2. Map one publisher and subscriber to exact allowed topic filters, sites/tenants and operations.
3. Confirm publish and subscribe authorization are independent and wildcard behavior cannot cross scope.
4. Review retained messages, persistent sessions, session/message expiry, wills, shared subscriptions, queue limits and dead-letter storage.
5. Review TLS endpoint validation, client certificate or credential rotation and denial behavior.
6. Map synthetic cases for authorized publish/subscribe, denied cross-site topic, malformed/oversized payload, duplicate event, session expiry, and reconnect to expected state transitions. A purpose-built loopback simulator may model these transitions without implementing or contacting a broker.
7. Record what QoS acknowledgement guarantees and what it does not guarantee downstream.

## Stop conditions

Do not start or contact a broker, connect to a network endpoint, enumerate real topics, publish operational-looking alarms/commands, test resource exhaustion, or use real device credentials. Broker and product acceptance belongs to separately governed environment validation.

## Evidence checklist

- [ ] Fixture provenance and represented broker, MQTT, and configuration versions recorded
- [ ] Publisher and subscriber identities mapped to exact tenant/site/topic permissions
- [ ] Publish, subscribe, wildcard, retained-message, and shared-subscription authorization reviewed independently
- [ ] Session expiry, wills, retained state, queue limits, overflow, reconnect, and duplicate behavior mapped
- [ ] TLS identity, client-credential lifecycle, denial, and downgrade expectations recorded
- [ ] Synthetic positive, cross-scope denial, malformed, oversized, duplicate, expiry, and reconnect cases assessed
- [ ] QoS milestones kept distinct from downstream persistence or physical outcome

## Sources

- [OASIS MQTT Version 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html), accessed 2026-08-25.

## Related pages

- [MQTT](../02-protocols/web-and-messaging/mqtt.md)
- [MQTT event contract](../05-development-and-integration/examples/mqtt-event-contract.md)
