/* Progressive enhancement: articles, links and the directory work without JS. */
(() => {
  "use strict";
  const root = document.documentElement;
  const theme = document.getElementById("theme-toggle");
  const systemDark = window.matchMedia("(prefers-color-scheme: dark)");
  const currentTheme = () => root.dataset.theme || (systemDark.matches ? "dark" : "light");
  const labelTheme = () => {
    const next = currentTheme() === "dark" ? "light" : "dark";
    theme.textContent = next === "dark" ? "Dark" : "Light";
    theme.setAttribute("aria-label", `Switch to ${next} theme`);
  };
  if (theme) {
    theme.hidden = false;
    labelTheme();
    theme.addEventListener("click", () => {
      const value = currentTheme() === "dark" ? "light" : "dark";
      root.dataset.theme = value;
      try { localStorage.setItem("securitytechnician.theme", value); } catch (_) { /* Theme for this session. */ }
      labelTheme();
    });
    systemDark.addEventListener("change", labelTheme);
  }

  const navigation = document.getElementById("site-navigation");
  const desktop = window.matchMedia("(min-width: 801px)");
  const updateNavigation = () => { if (navigation) navigation.open = desktop.matches; };
  updateNavigation();
  desktop.addEventListener("change", updateNavigation);
  document.addEventListener("keydown", event => {
    const target = event.target;
    const editing = target instanceof HTMLElement && (target.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(target.tagName));
    if ((event.key.toLowerCase() === "k" && (event.ctrlKey || event.metaKey)) || (event.key === "/" && !editing && !event.ctrlKey && !event.metaKey && !event.altKey)) {
      const field = document.getElementById("search-query") || document.getElementById("site-search");
      if (field) { event.preventDefault(); field.focus(); field.select(); }
    }
    if (event.key === "Escape" && navigation && !desktop.matches && navigation.open) {
      navigation.open = false;
      navigation.querySelector("summary").focus();
    }
  });

  const copyStatus = document.getElementById("copy-status");
  document.querySelectorAll("button[data-copy]").forEach(button => {
    button.hidden = false;
    button.addEventListener("click", async () => {
      const code = document.getElementById(button.dataset.copy);
      if (!code) return;
      try {
        if (!navigator.clipboard) throw new Error("Clipboard unavailable");
        await navigator.clipboard.writeText(code.textContent);
        button.textContent = "Copied";
        copyStatus.textContent = "Code copied to clipboard.";
      } catch (_) {
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(code);
        if (selection) { selection.removeAllRanges(); selection.addRange(range); }
        button.textContent = "Selected";
        copyStatus.textContent = "Automatic copying was unavailable. Code is selected; use your browser's copy command.";
      }
      setTimeout(() => { button.textContent = "Copy"; }, 2000);
    });
  });

  if ("IntersectionObserver" in window) {
    const tocLinks = [...document.querySelectorAll(".toc a")];
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        const anchor = `#${entry.target.id}`;
        tocLinks.forEach(link => link.classList.toggle("is-current", link.getAttribute("href") === anchor));
      }
    }, { rootMargin: "-15% 0px -65% 0px", threshold: 0 });
    document.querySelectorAll(".prose h2[id], .prose h3[id]").forEach(h => observer.observe(h));
  }

  const form = document.getElementById("search-form");
  if (!form || !window.WikiSearch) return;
  const queryInput = document.getElementById("search-query");
  const sectionInput = document.getElementById("search-section");
  const status = document.getElementById("search-status");
  const results = document.getElementById("search-results");
  const more = document.getElementById("search-more");
  const retry = document.getElementById("search-retry");
  const siteRoot = new URL(document.body.dataset.root || "../", window.location.href);
  const params = new URLSearchParams(window.location.search);
  queryInput.value = (params.get("q") || "").slice(0, 200);
  const selectedSection = params.get("section") || "";
  if ([...sectionInput.options].some(o => o.value === selectedSection)) sectionInput.value = selectedSection;
  let pages = null;
  let loading = null;
  let generation = 0;
  let matches = [];
  let shown = 0;
  let timer;
  let activeTerms = [];

  function saveQuery(query, section) {
    const url = new URL(window.location.href);
    query ? url.searchParams.set("q", query) : url.searchParams.delete("q");
    section ? url.searchParams.set("section", section) : url.searchParams.delete("section");
    try { history.replaceState(null, "", url); } catch (_) { /* Search still works. */ }
  }

  async function loadIndex() {
    if (pages) return pages;
    if (loading) return loading;
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 15000);
    loading = (async () => {
      const response = await fetch(new URL("search-index.json", siteRoot), { signal: controller.signal, credentials: "omit" });
      if (!response.ok) throw new Error(`Index request failed: ${response.status}`);
      const data = await response.json();
      if (data.version !== 1 || !Array.isArray(data.pages)) throw new Error("Unsupported search index");
      pages = window.WikiSearch.prepare(data.pages);
      return pages;
    })();
    try { return await loading; }
    finally { clearTimeout(timeout); loading = null; }
  }

  // Match highlighting uses text nodes only. A query never becomes HTML.
  function appendMarked(element, text, terms) {
    const lower = text.toLowerCase();
    let cursor = 0;
    let pieces = 0;
    while (cursor < text.length && pieces < 50) {
      let at = -1;
      let length = 0;
      for (const term of terms) {
        const found = lower.indexOf(term, cursor);
        if (found !== -1 && (at === -1 || found < at || (found === at && term.length > length))) {
          at = found; length = term.length;
        }
      }
      if (at === -1) break;
      element.append(document.createTextNode(text.slice(cursor, at)));
      const mark = document.createElement("mark");
      mark.textContent = text.slice(at, at + length);
      element.append(mark);
      cursor = at + length;
      pieces += 1;
    }
    element.append(document.createTextNode(text.slice(cursor)));
  }

  function safeResultURL(path) {
    const url = new URL(path, siteRoot);
    if (url.origin !== siteRoot.origin || !url.pathname.startsWith(siteRoot.pathname)) return null;
    return url;
  }

  function appendResults() {
    const batch = matches.slice(shown, shown + 25);
    for (const { page } of batch) {
      const url = safeResultURL(page.url);
      if (!url) continue;
      const article = document.createElement("article");
      article.className = "search-result";
      const category = document.createElement("div");
      category.className = "result-section";
      category.textContent = page.sectionLabel;
      const heading = document.createElement("h2");
      const link = document.createElement("a");
      link.href = url.href;
      appendMarked(link, page.title, activeTerms);
      heading.append(link);
      const summary = document.createElement("p");
      appendMarked(summary, page.summary || "", activeTerms);
      article.append(category, heading, summary);
      if (activeTerms.some(term => !(page._title + " " + page._summary).includes(term))) {
        const text = page.text || "";
        const first = Math.min(...activeTerms.map(term => page._text.indexOf(term)).filter(index => index >= 0));
        const start = Math.max(0, (Number.isFinite(first) ? first : 0) - 65);
        const snippet = document.createElement("p");
        snippet.className = "result-snippet";
        appendMarked(snippet, `${start ? "…" : ""}${text.slice(start, start + 220)}${text.length > start + 220 ? "…" : ""}`, activeTerms);
        article.append(snippet);
      }
      results.append(article);
    }
    shown += batch.length;
    more.hidden = shown >= matches.length;
    if (!more.hidden) more.textContent = `Show more results (${shown} of ${matches.length})`;
  }

  async function search() {
    const request = ++generation;
    const query = queryInput.value.trim().slice(0, 200);
    const section = sectionInput.value;
    activeTerms = window.WikiSearch.tokens(query);
    saveQuery(query, section);
    retry.hidden = true;
    more.hidden = true;
    results.replaceChildren();
    if (!activeTerms.length) {
      status.textContent = "Enter a term to search the full wiki. Nothing is sent to an external search service.";
      return;
    }
    status.textContent = pages ? "Searching…" : "Loading the local search index…";
    try {
      await loadIndex();
      if (request !== generation) return;
      matches = window.WikiSearch.rank(pages, query, section);
      shown = 0;
      status.textContent = matches.length ? `${matches.length} ${matches.length === 1 ? "page" : "pages"} found for “${query}”.` : `No pages matched “${query}”. Try fewer words or a broader section.`;
      appendResults();
    } catch (_) {
      if (request !== generation) return;
      status.textContent = "The search index could not be loaded. Check your connection, retry, or use the complete page directory below.";
      retry.hidden = false;
    }
  }
  form.addEventListener("submit", event => { event.preventDefault(); clearTimeout(timer); search(); });
  queryInput.addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(search, 160); });
  sectionInput.addEventListener("change", search);
  more.addEventListener("click", appendResults);
  retry.addEventListener("click", search);
  if (queryInput.value) search();
})();
