/* Search is deliberately small and independent of the DOM, so it is testable. */
(function (root) {
  "use strict";
  const normalise = value => String(value || "").normalize("NFKC").toLowerCase();
  function tokens(query) {
    return [...new Set((normalise(query).slice(0, 200).match(/[\p{L}\p{N}]+/gu) || []))].slice(0, 12);
  }
  function prepare(pages) {
    if (!Array.isArray(pages)) throw new Error("Invalid search index");
    return pages.filter(p => p && typeof p.title === "string" && typeof p.url === "string")
      .map(p => ({ ...p, _title: normalise(p.title), _summary: normalise(p.summary),
        _tags: normalise((Array.isArray(p.tags) ? p.tags : []).join(" ")),
        _headings: normalise(p.headings), _text: normalise(p.text) }));
  }
  function rank(pages, query, section = "") {
    const terms = tokens(query);
    if (!terms.length) return [];
    const phrase = normalise(query).trim().slice(0, 200);
    const scored = [];
    for (const page of pages) {
      if (section && page.section !== section) continue;
      let score = 0;
      let allFound = true;
      for (const term of terms) {
        const title = page._title.includes(term);
        const tags = page._tags.includes(term);
        const summary = page._summary.includes(term);
        const headings = page._headings.includes(term);
        const text = page._text.includes(term);
        if (!(title || tags || summary || headings || text)) { allFound = false; break; }
        score += (title ? 35 : 0) + (tags ? 22 : 0) + (summary ? 12 : 0) + (headings ? 7 : 0) + (text ? 1 : 0);
      }
      if (allFound) {
        if (page._title === phrase) score += 160;
        else if (page._title.startsWith(phrase)) score += 75;
        else if (page._title.includes(phrase)) score += 45;
        scored.push({ page, score });
      }
    }
    return scored.sort((a, b) => b.score - a.score || a.page.title.localeCompare(b.page.title));
  }
  const api = Object.freeze({ normalise, tokens, prepare, rank });
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.WikiSearch = api;
})(typeof globalThis !== "undefined" ? globalThis : this);
