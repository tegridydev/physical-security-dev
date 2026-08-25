---
title: "WebSocket event client in TypeScript"
summary: "A bounded TypeScript WSS event client with runtime validation and no physical-control capability."
page_type: development
domains:
  - development
tags:
  - typescript
  - websocket
coverage_limit: "Read-only WSS reference client using a reserved documentation domain; transport memory bounds, server authorization, dependency patches, and product behavior require an environment profile."
languages:
  - TypeScript
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-executed
safety_level: safety-relevant
standards:
  - "TypeScript 7.0"
  - "Node.js 24 LTS"
  - "RFC 6455"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# WebSocket event client in TypeScript

[Home](../../README.md) / [Development](../README.md) / [Examples](README.md) / WebSocket events

Target: TypeScript 7 and Node.js 24 LTS  
Dependencies: `typescript` and `@types/node` for development; no third-party runtime package  
Target name: events.example, reserved for documentation  
Scope: read-only synthetic event contract with no command operation

## Complete example

~~~typescript
type EventMessage = Readonly<{
  id: string;
  type: "camera.health" | "door.state";
  source: string;
  occurredAt: string;
  state: string;
}>;

const MAX_MESSAGE_CHARS = 16_384;
const ALLOWED_TYPES = new Set(["camera.health", "door.state"]);
const ALLOWED_STATES: Readonly<
  Record<EventMessage["type"], ReadonlySet<string>>
> = {
  "camera.health": new Set(["healthy", "degraded", "offline"]),
  "door.state": new Set(["open", "closed", "unknown"]),
};
const CANONICAL_UTC_TIMESTAMP =
  /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/;

function requireBoundedString(
  value: unknown,
  name: string,
  maxLength = 128,
): string {
  if (typeof value !== "string" || value.length < 1 || value.length > maxLength) {
    throw new Error("invalid " + name);
  }
  return value;
}

function parseEvent(raw: string): EventMessage {
  if (raw.length > MAX_MESSAGE_CHARS) throw new Error("message too large");
  const value: unknown = JSON.parse(raw);
  if (typeof value !== "object" || value === null || Array.isArray(value)) {
    throw new Error("event must be an object");
  }
  const record = value as Record<string, unknown>;
  const expected = ["id", "type", "source", "occurredAt", "state"].sort();
  if (Object.keys(record).sort().join(",") !== expected.join(",")) {
    throw new Error("unexpected schema");
  }
  const type = requireBoundedString(record.type, "type");
  if (!ALLOWED_TYPES.has(type)) throw new Error("unsupported event type");
  const occurredAt = requireBoundedString(record.occurredAt, "occurredAt", 40);
  const parsedTime = new Date(occurredAt);
  if (
    !CANONICAL_UTC_TIMESTAMP.test(occurredAt) ||
    Number.isNaN(parsedTime.getTime()) ||
    parsedTime.toISOString() !== occurredAt
  ) {
    throw new Error("timestamp must be canonical UTC with milliseconds");
  }
  const eventType = type as EventMessage["type"];
  const state = requireBoundedString(record.state, "state");
  if (!ALLOWED_STATES[eventType].has(state)) {
    throw new Error("state is invalid for event type");
  }
  return {
    id: requireBoundedString(record.id, "id"),
    type: eventType,
    source: requireBoundedString(record.source, "source"),
    occurredAt,
    state,
  };
}

const token = process.env.PHYSICAL_SECURITY_DEV_READONLY_TOKEN;
if (!token) throw new Error("PHYSICAL_SECURITY_DEV_READONLY_TOKEN is required");

const socket = new WebSocket("wss://events.example/v1/events", ["physical-security-dev.events.v1"]);
const stop = setTimeout(() => socket.close(1000, "session timeout"), 10_000);

socket.addEventListener("open", () => {
  socket.send(JSON.stringify({ action: "authenticate", token }));
});

socket.addEventListener("message", (message) => {
  if (typeof message.data !== "string") {
    socket.close(1003, "text events required");
    return;
  }
  try {
    const event = parseEvent(message.data);
    console.log("validated event", event.id, event.type);
  } catch (error) {
    console.error("event rejected", error instanceof Error ? error.message : "unknown");
    socket.close(1007, "invalid event");
  }
});

socket.addEventListener("close", () => clearTimeout(stop));
socket.addEventListener("error", () => console.error("WebSocket transport error"));
~~~

## Security properties and limits

The WSS URL uses platform certificate and hostname validation. The code validates text length, exact top-level fields, bounded strings, allowed event type/state combinations, and canonical UTC timestamps after Node has delivered a complete message, and exposes no command/actuation operation. `MAX_MESSAGE_CHARS` is therefore an application/schema rejection bound, **not** a transport-level memory limit: the WebSocket implementation may already have buffered or allocated the message. Enforce frame/message and connection limits at the server, gateway, or a runtime that exposes those controls. Standard `JSON.parse` does not expose duplicate member names; an integration whose producers or intermediaries may interpret duplicates differently must reject them at ingress with a duplicate-aware parser or gateway. Passing a bearer token in the first message is illustrative and must match the actual API; prefer an API-supported protected authentication method and never log that message.

## Validation checklist

In an authorized test environment, use strict TypeScript settings and cover unknown certificate/host, denied token, timeout, binary/oversized/malformed messages, duplicate-member policy, unsupported type/state combinations, invalid/non-canonical timestamps, server-side message limits, reconnect behaviour, and clean shutdown. Record the exact Node.js, TypeScript, `@types/node`, server, cases, observations, and limitations separately.

## Sources

- [RFC 6455 WebSocket](https://www.rfc-editor.org/rfc/rfc6455), accessed 2026-08-25.
- [Node.js globals: WebSocket](https://nodejs.org/api/globals.html#class-websocket), accessed 2026-08-25.

## Related pages

- [TypeScript guide](../language-guides/typescript.md)
- [WebSocket, SSE, and webhooks](../../02-protocols/web-and-messaging/websocket-sse-and-webhooks.md)
