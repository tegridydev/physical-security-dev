---
title: "ONVIF SOAP request anatomy"
summary: "A synthetic SOAP envelope illustrating namespaces and bounded developer responsibilities."
page_type: development
domains:
  - video
  - development
tags:
  - onvif
  - soap
  - xml
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-executed
safety_level: safety-relevant
standards:
  - "ONVIF Core Specification"
coverage_limit: "SOAP/ONVIF envelope anatomy only; transport, discovery, authentication, authorization, product profiles, and response handling are outside this fragment."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# ONVIF SOAP request anatomy

[Home](../../README.md) / [Development](../README.md) / [Examples](README.md) / ONVIF SOAP

Target: synthetic device service  
Side effects: none; this page contains no network client or credentials

## Envelope fragment

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope
    xmlns:s="http://www.w3.org/2003/05/soap-envelope"
    xmlns:tds="http://www.onvif.org/ver10/device/wsdl">
  <s:Header/>
  <s:Body>
    <tds:GetDeviceInformation/>
  </s:Body>
</s:Envelope>
~~~

The fragment illustrates the SOAP 1.2 envelope and ONVIF device-service namespace. It deliberately omits transport, endpoint discovery, authentication, WS-Security, message addressing, HTTP headers, version negotiation, response limits, XML parser configuration and authorization. Adding those correctly requires the exact ONVIF specification/profile and product behavior.

## Developer checklist

- Use HTTPS with validated device identity where the device/profile supports it.
- Obtain the correct service endpoint through supported discovery/capability mechanisms.
- Generate namespace-aware XML; never concatenate untrusted values into markup.
- Disable external entity and network/file resolution in the response parser.
- Bound request/response bytes, nesting, arrays and time.
- Distinguish SOAP fault, HTTP error, TLS/authentication failure, unsupported action and invalid response.
- Do not log credentials or full sensitive device responses.

## Sources

- [ONVIF Network Interface Specifications](https://www.onvif.org/profiles/specifications/), official specification index, accessed 2026-08-25.
- [SOAP Version 1.2 Part 1](https://www.w3.org/TR/soap12-part1/), W3C Recommendation, accessed 2026-08-25.

## Related pages

- [ONVIF](../../02-protocols/video-and-media/onvif.md)
- [SOAP and XML](../../02-protocols/web-and-messaging/soap-and-xml.md)
