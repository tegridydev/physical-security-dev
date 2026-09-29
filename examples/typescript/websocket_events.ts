/** Read up to ten events over WSS. No subscription or command messages are sent. */
declare const process: { argv: string[]; env: Record<string, string | undefined>; exitCode: number; exit(code: number): never };
type DoorEvent = { event_id: string; device_id: string; state: "open" | "closed" | "unknown" };
const MAX_BYTES = 16_384;

export function parseEvent(text: string): DoorEvent {
  if (new TextEncoder().encode(text).byteLength > MAX_BYTES) throw new Error("Event exceeds 16 KiB");
  const value: unknown = JSON.parse(text);
  if (value === null || typeof value !== "object" || Array.isArray(value)) throw new Error("Expected an event object");
  const object = value as Record<string, unknown>;
  if (Object.keys(object).sort().join(",") !== "device_id,event_id,state") throw new Error("Missing or unknown fields");
  for (const field of ["event_id", "device_id"]) {
    if (typeof object[field] !== "string" || !/^[A-Za-z0-9_]{1,64}(?![\s\S])/.test(object[field])) throw new Error("Invalid event identity");
  }
  if (!["open", "closed", "unknown"].includes(String(object.state)) || typeof object.state !== "string") throw new Error("Unknown state");
  return { event_id: object.event_id as string, device_id: object.device_id as string, state: object.state as DoorEvent["state"] };
}

function run(): void {
  const args = process.argv.slice(2);
  if (args.length === 1 && args[0] === "--demo") {
    console.log(JSON.stringify(parseEvent('{"event_id":"evt001","device_id":"door01","state":"closed"}')));
    return;
  }
  if (args.length !== 2 || args[0] !== "--url") throw new Error("Use --demo or --url wss://host/events");
  if (process.env.NODE_TLS_REJECT_UNAUTHORIZED === "0") throw new Error("Certificate validation must remain enabled");
  if (/[\x00-\x20\x7f]/.test(args[1])) throw new Error("URL contains whitespace or control characters");
  const url = new URL(args[1]);
  if (url.protocol !== "wss:" || !url.hostname || url.username || url.password || url.hash || url.search) {
    throw new Error("Use a WSS URL without credentials, query parameters or a fragment");
  }
  const socket = new WebSocket(url);
  let count = 0;
  let closing = false;
  let failed = false;
  let closeDeadline: ReturnType<typeof setTimeout> | undefined;
  const stop = (failure: boolean): void => {
    failed ||= failure;
    if (failed) process.exitCode = 1;
    if (closing) return;
    closing = true;
    clearTimeout(deadline);
    socket.close(failure ? 1008 : 1000, failure ? "Invalid event or connection" : "Sample complete");
    // The native API has no terminate operation. Bound the CLI shutdown wait.
    closeDeadline = setTimeout(() => process.exit(failed ? 1 : 0), 2000);
  };
  const deadline = setTimeout(() => stop(true), 15_000);
  socket.addEventListener("message", (event: MessageEvent<unknown>) => {
    if (closing) return;
    try {
      if (typeof event.data !== "string") throw new Error("Only text messages are accepted");
      console.log(JSON.stringify(parseEvent(event.data)));
      count += 1;
      if (count >= 10) stop(false);
    } catch {
      console.error("Error: the event does not match the example contract");
      stop(true);
    }
  });
  socket.addEventListener("error", () => {
    console.error("Error: WebSocket connection failed");
    stop(true);
  });
  socket.addEventListener("close", (event: CloseEvent) => {
    clearTimeout(deadline);
    if (closeDeadline !== undefined) clearTimeout(closeDeadline);
    if (!closing && (!event.wasClean || count === 0)) process.exitCode = 1;
  });
}

try { run(); } catch (error: unknown) {
  console.error(error instanceof Error ? `Error: ${error.message}` : "Error: invalid input");
  process.exitCode = 1;
}
