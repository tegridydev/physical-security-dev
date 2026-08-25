---
title: "Safe HTTPS JSON read in Python"
summary: "A bounded, certificate-validating, read-only Python HTTPS request with explicit timeout and schema checks."
page_type: development
domains:
  - development
tags:
  - python
  - https
coverage_limit: "Read-only Python reference client using a reserved documentation domain; proxy, OAuth, certificate, endpoint authorization, and product behavior require an environment profile."
languages:
  - Python
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-executed
safety_level: safety-relevant
standards:
  - "Python 3.14.7"
  - "HTTP Semantics, RFC 9110"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Safe HTTPS JSON read in Python

[Home](../../README.md) / [Development](../README.md) / [Examples](README.md) / HTTPS JSON read

Target: Python 3.14.7, standard library only  
Target name: device.example, a reserved documentation domain  
Scope: reference implementation for an authorized read-only endpoint

## Complete example

~~~python
from __future__ import annotations

import http.client
import json
import os
import ssl
import urllib.error
import urllib.request

URL = "https://device.example/api/v1/health"
MAX_BODY = 64 * 1024
IO_TIMEOUT_SECONDS = 5.0


class DenyRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.HTTPError(
            req.full_url, code, "redirect denied", headers, fp
        )


def reject_duplicate_members(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    document: dict[str, object] = {}
    for key, value in pairs:
        if key in document:
            raise ValueError("duplicate JSON member")
        document[key] = value
    return document


def main() -> None:
    token = os.environ.get("PHYSICAL_SECURITY_DEV_READONLY_TOKEN")
    if not token:
        raise SystemExit("PHYSICAL_SECURITY_DEV_READONLY_TOKEN is required")

    context = ssl.create_default_context()
    request = urllib.request.Request(
        URL,
        method="GET",
        headers={
            "Accept": "application/json",
            "Authorization": "Bearer " + token,
            "User-Agent": "physical-security-dev-readonly-example/1",
        },
    )

    opener = urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=context),
        DenyRedirects(),
    )

    try:
        with opener.open(request, timeout=IO_TIMEOUT_SECONDS) as response:
            content_type = response.headers.get_content_type()
            if content_type != "application/json":
                raise ValueError("unexpected content type")
            body = response.read(MAX_BODY + 1)
            if len(body) > MAX_BODY:
                raise ValueError("response exceeds configured limit")
    except (
        urllib.error.URLError,
        http.client.HTTPException,
        TimeoutError,
        ssl.SSLError,
        ValueError,
    ) as error:
        raise SystemExit("request failed without retry: " + type(error).__name__) from error

    try:
        document = json.loads(
            body.decode("utf-8"),
            object_pairs_hook=reject_duplicate_members,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        raise SystemExit(
            "invalid JSON response: " + type(error).__name__
        ) from error
    if not isinstance(document, dict) or set(document) != {"status"}:
        raise SystemExit("unexpected response schema")
    status = document["status"]
    if not isinstance(status, str) or status not in {"healthy", "degraded"}:
        raise SystemExit("unknown health state")
    print("validated health state:", status)


if __name__ == "__main__":
    main()
~~~

## Security properties and limits

The default SSL context validates the server chain and hostname. The custom opener denies redirects so credentials are not silently forwarded to another location. The timeout bounds blocking I/O operations; it is **not** a total wall-clock deadline for the whole transaction. The response-size limit is an application bound, duplicate JSON members and unknown fields are rejected, no automatic retry is made, and neither token nor body is printed. The example does not demonstrate OAuth token acquisition, certificate pinning, explicit proxy policy, or product authorization.

## Validation checklist

For an authorized test environment, cover success, redirect denial, unknown CA, wrong hostname, stalled I/O, 401/403, oversized body, wrong content type, malformed JSON, duplicate/unknown members, and an end-to-end wall-clock deadline supplied by the calling application. Record the exact Python, OS, trust store, endpoint implementation, cases, observations, and limitations in a separate validation record.

## Sources

- [Python urllib.request](https://docs.python.org/3/library/urllib.request.html), accessed 2026-08-25.
- [Python ssl](https://docs.python.org/3/library/ssl.html), accessed 2026-08-25.
- [RFC 9110 HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110), accessed 2026-08-25.

## Related pages

- [HTTP and REST](../../02-protocols/web-and-messaging/http-and-rest.md)
- [Python guide](../language-guides/python.md)
