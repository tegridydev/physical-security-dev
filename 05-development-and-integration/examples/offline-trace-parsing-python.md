---
title: "Offline trace parsing in Python"
summary: "A bounded Python parser for synthetic JSON-lines physical-security events."
page_type: development
domains:
  - development
tags:
  - python
  - events
  - offline
coverage_limit: "Synthetic JSON-lines parser; production schemas, streaming/storage limits, Python patch behavior, and source authorization require an environment profile."
languages:
  - Python
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-executed
safety_level: safety-relevant
standards:
  - "Python 3.14.7"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Offline trace parsing in Python

[Home](../../README.md) / [Development](../README.md) / [Examples](README.md) / Offline trace parsing

Target: Python 3.14.7, standard library only  
Inputs: embedded synthetic JSON-lines events  
Side effects: standard output only; no network, files, devices, or actuators

## Complete example

~~~python
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from typing import Final, Literal, cast

MAX_LINE_BYTES: Final = 2_048
ALLOWED_TYPES: Final = frozenset({"door.state", "camera.health"})
ALLOWED_STATES: Final = {
    "door.state": frozenset({"open", "closed", "unknown"}),
    "camera.health": frozenset({"healthy", "degraded", "offline"}),
}
EventType = Literal["door.state", "camera.health"]


@dataclass(frozen=True, slots=True)
class Event:
    event_id: str
    event_type: EventType
    source: str
    occurred_at: datetime
    state: str


def parse_timestamp(value: object) -> datetime:
    if not isinstance(value, str) or len(value) > 40:
        raise ValueError("occurred_at must be a bounded string")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("occurred_at must include an offset")
    return parsed


def reject_duplicate_members(pairs: list[tuple[str, object]]) -> dict[str, object]:
    document: dict[str, object] = {}
    for key, value in pairs:
        if key in document:
            raise ValueError(f"duplicate JSON member: {key}")
        document[key] = value
    return document


def require_bounded_string(value: object, name: str) -> str:
    if not isinstance(value, str) or not 1 <= len(value) <= 128:
        raise ValueError(f"invalid {name}")
    return value


def parse_event(line: bytes) -> Event:
    if not line or len(line) > MAX_LINE_BYTES:
        raise ValueError("line size outside allowed range")
    document = json.loads(
        line.decode("utf-8"), object_pairs_hook=reject_duplicate_members
    )
    if not isinstance(document, dict):
        raise ValueError("event must be an object")

    required = {"id", "type", "source", "occurred_at", "state"}
    if set(document) != required:
        raise ValueError("unexpected or missing fields")
    raw_type = document["type"]
    if not isinstance(raw_type, str) or raw_type not in ALLOWED_TYPES:
        raise ValueError("unsupported event type")

    event_id = require_bounded_string(document["id"], "id")
    source = require_bounded_string(document["source"], "source")
    state = require_bounded_string(document["state"], "state")
    if state not in ALLOWED_STATES[raw_type]:
        raise ValueError("state is invalid for event type")

    return Event(
        event_id=event_id,
        event_type=cast(EventType, raw_type),
        source=source,
        occurred_at=parse_timestamp(document["occurred_at"]),
        state=state,
    )


FIXTURES = (
    b'{"id":"evt-001","type":"door.state","source":"door.example/7",'
    b'"occurred_at":"2026-08-25T02:15:00Z","state":"closed"}',
    b'{"id":"evt-002","type":"unknown","source":"test",'
    b'"occurred_at":"2026-08-25T02:15:01Z","state":"x"}',
    b'{"id":"evt-001","type":"camera.health","source":"camera.example/2",'
    b'"occurred_at":"2026-08-25T02:15:02Z","state":"healthy"}',
    b'{"id":"evt-004","id":"evt-duplicate-member","type":"camera.health",'
    b'"source":"camera.example/4","occurred_at":"2026-08-25T02:15:03Z",'
    b'"state":"healthy"}',
)


def main() -> None:
    seen_ids: set[str] = set()
    for number, fixture in enumerate(FIXTURES, start=1):
        try:
            event = parse_event(fixture)
            if event.event_id in seen_ids:
                raise ValueError("duplicate event id across records")
            seen_ids.add(event.event_id)
            print(number, "accepted", event.event_id, event.event_type)
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
            print(number, "rejected", type(error).__name__)


if __name__ == "__main__":
    main()
~~~

## Expected behavior

The first fixture is accepted. The unknown event type, repeated event ID across records, and duplicate JSON member name are rejected without printing raw content. Duplicate member names are a JSON-object parsing problem; repeated event IDs are a stream/state problem. The example preserves a timezone-aware occurrence time, validates state against event type, and rejects extra fields to make schema drift visible.

## Validation checklist

Review with fixtures for empty and oversized records, invalid UTF-8, duplicate member names, repeated record IDs, non-string field types, invalid type/state combinations, offset-free timestamps, invalid calendar values, extra/missing fields, and bounded strings. Record the exact Python, OS, fixture digest, observations, and limitations separately.

## Sources

- [Python json documentation](https://docs.python.org/3/library/json.html), accessed 2026-08-25.

## Related pages

- [Python guide](../language-guides/python.md)
- [Event normalization](../patterns/event-normalization-and-schema-evolution.md)
