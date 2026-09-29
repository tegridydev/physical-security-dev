/* Run before CSS to avoid a theme flash. Storage may be disabled by the browser. */
(() => {
  "use strict";
  try {
    const stored = localStorage.getItem("securitytechnician.theme");
    if (stored === "light" || stored === "dark") {
      document.documentElement.dataset.theme = stored;
    }
  } catch (_) { /* The system preference remains usable without storage. */ }
})();
