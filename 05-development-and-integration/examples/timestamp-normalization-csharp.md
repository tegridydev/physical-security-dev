---
title: "Timestamp normalization in C#"
summary: "Preserve source time, ingestion time, offset, and sequence instead of flattening event chronology."
page_type: development
domains:
  - development
tags:
  - csharp
  - time
coverage_limit: "Synthetic timestamp-normalization reference; source clock quality, product formats, .NET patch behavior, and ordering guarantees are environment-specific."
languages:
  - "C#"
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-executed
safety_level: safety-relevant
standards:
  - ".NET 10 LTS"
  - "C# 14"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Timestamp normalization in C#

[Home](../../README.md) / [Development](../README.md) / [Examples](README.md) / Timestamp normalization

Target: .NET 10 LTS, C# 14, standard library only  
Inputs: embedded synthetic timestamps  
Side effects: standard output only

## Complete example

~~~csharp
#nullable enable

using System;
using System.Globalization;

internal sealed record SourceEvent(
    string EventId,
    string Source,
    string OccurredAt,
    long? Sequence);

internal sealed record NormalizedEvent(
    string EventId,
    string Source,
    DateTimeOffset OccurredAt,
    DateTimeOffset IngestedAt,
    long? Sequence);

internal static class Program
{
    private static NormalizedEvent Normalize(
        SourceEvent source,
        DateTimeOffset ingestedAt)
    {
        if (string.IsNullOrEmpty(source.EventId) ||
            source.EventId.Length > 128 ||
            string.IsNullOrEmpty(source.Source) ||
            source.Source.Length > 128)
        {
            throw new ArgumentException("Identifier outside configured bounds");
        }

        const DateTimeStyles Styles = DateTimeStyles.None;
        if (!DateTimeOffset.TryParseExact(
                source.OccurredAt,
                "O",
                CultureInfo.InvariantCulture,
                Styles,
                out DateTimeOffset occurredAt))
        {
            throw new ArgumentException("Timestamp must be round-trip ISO 8601");
        }

        if (source.Sequence is < 0)
        {
            throw new ArgumentException("Sequence must be non-negative");
        }

        return new NormalizedEvent(
            source.EventId,
            source.Source,
            occurredAt,
            ingestedAt,
            source.Sequence);
    }

    private static void Main()
    {
        var source = new SourceEvent(
            "evt-001",
            "camera.example/4",
            "2026-08-25T12:15:30.0000000+10:00",
            42);
        var normalized = Normalize(
            source,
            new DateTimeOffset(2026, 8, 25, 2, 15, 31, TimeSpan.Zero));

        Console.WriteLine("event: " + normalized.EventId);
        Console.WriteLine("occurred UTC: " + normalized.OccurredAt.UtcDateTime.ToString("O"));
        Console.WriteLine("ingested UTC: " + normalized.IngestedAt.UtcDateTime.ToString("O"));
        Console.WriteLine("sequence: " + normalized.Sequence);
    }
}
~~~

## Design note

The example retains DateTimeOffset and sequence rather than replacing source time with ingestion time. Exact-format parsing intentionally rejects ambiguous local timestamps. It preserves a supplied numeric offset but does not infer a named timezone or daylight-saving rule, establish clock trust, or prove causal order.

## Environment validation checklist

- [ ] Cover UTC and positive/negative offsets, daylight-saving boundaries, and sub-second precision required by the source contract.
- [ ] Reject offset-free or malformed timestamps, excessive identifiers, and negative sequences.
- [ ] Confirm occurrence time and ingestion time remain distinct and the source offset is preserved.
- [ ] Record the .NET SDK/OS versions, fixtures, observed output, clock assumptions, and limitations.

## Sources

- [DateTimeOffset documentation](https://learn.microsoft.com/dotnet/api/system.datetimeoffset), accessed 2026-08-25.

## Related pages

- [C# guide](../language-guides/csharp.md)
- [Logging, time, and evidence integrity](../../06-security-and-assurance/logging-time-and-evidence-integrity.md)
