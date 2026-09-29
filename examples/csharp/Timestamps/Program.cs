using System.Globalization;
using System.Text.Json;
using System.Text.RegularExpressions;

// Keep occurrence and receipt timestamps separate. Do not infer a time zone.
static DateTimeOffset ParseTimestamp(string value)
{
    const string pattern = @"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,7})?(?:Z|[+-]\d{2}:\d{2})$";
    if (value.Length > 40 || value.EndsWith("-00:00", StringComparison.Ordinal) ||
        !Regex.IsMatch(value, pattern, RegexOptions.CultureInvariant | RegexOptions.NonBacktracking,
            TimeSpan.FromMilliseconds(100)))
        throw new FormatException("Use a timestamp with a known UTC offset or Z");
    string normalised = value.EndsWith('Z') ? value[..^1] + "+00:00" : value;
    string[] formats = ["yyyy-MM-dd'T'HH:mm:sszzz", "yyyy-MM-dd'T'HH:mm:ss.FFFFFFFzzz"];
    if (!DateTimeOffset.TryParseExact(normalised, formats, CultureInfo.InvariantCulture,
        DateTimeStyles.None, out DateTimeOffset result))
        throw new FormatException("Invalid timestamp");
    return result.ToUniversalTime();
}

try
{
    if (args.Length == 1 && args[0] == "--self-test")
    {
        if (ParseTimestamp("2026-09-10T09:00:00+10:00") != ParseTimestamp("2026-09-09T23:00:00Z"))
            throw new InvalidOperationException("UTC conversion failed");
        foreach (string invalid in new[] { "2026-09-10T09:00:00", "2026-09-10T09:00:00-00:00", "2026-02-30T00:00:00Z" })
        {
            bool rejected = false;
            try { ParseTimestamp(invalid); } catch (FormatException) { rejected = true; }
            if (!rejected) throw new InvalidOperationException("Invalid timestamp was accepted");
        }
        Console.WriteLine("Timestamp tests passed");
        return 0;
    }
    bool demo = args.Length == 1 && args[0] == "--demo";
    if (!demo && (args.Length != 4 || args[0] != "--occurred" || args[2] != "--received"))
    {
        Console.Error.WriteLine("Use --demo, --self-test or --occurred TIMESTAMP --received TIMESTAMP");
        return 2;
    }
    DateTimeOffset occurred = ParseTimestamp(demo ? "2026-09-10T09:00:00+10:00" : args[1]);
    DateTimeOffset received = ParseTimestamp(demo ? "2026-09-09T23:00:02Z" : args[3]);
    Console.WriteLine(JsonSerializer.Serialize(new {
        occurred_at = occurred.ToString("O", CultureInfo.InvariantCulture),
        received_at = received.ToString("O", CultureInfo.InvariantCulture),
        observed_delay_seconds = (received - occurred).TotalSeconds
    }));
    return 0;
}
catch (Exception error) when (error is FormatException or InvalidOperationException or RegexMatchTimeoutException)
{
    Console.Error.WriteLine($"Error: {error.Message}");
    return 1;
}
