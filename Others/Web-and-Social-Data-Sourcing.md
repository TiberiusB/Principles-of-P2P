## Web and Social Data Sourcing for P2P-ness Assessments

Purpose: propose practical, resilient ways to gather evidence for `template_data.md` and scoring in `template_compilation.md`, including sources that block generic AI traffic. This is a planning document only; no implementations are included.

### Categories of Tools and Sources

- **Web crawling frameworks**
  - **Scrapy**
    - **Capabilities**: High-performance Python crawling, async I/O, item pipelines, throttling, caching.
    - **Advantages**: Mature ecosystem, broad middleware support, strong reliability at scale.
    - **Functionality**: Custom spiders for org sites; feed exports to JSON/CSV/Parquet; robots.txt-aware.
  - **StormCrawler**
    - **Capabilities**: Distributed, low-latency crawling on Apache Storm; real-time fetch/parse/index.
    - **Advantages**: Horizontal scaling; elastic throughput; integrates with Elasticsearch/Solr.
    - **Functionality**: Durable frontier, URL dedup, content parsing, metadata enrichment.
  - **Crawlee (Apify SDK)**
    - **Capabilities**: Headless-browser and HTTP crawling with autoscaling, request queues.
    - **Advantages**: Built-in Playwright/Puppeteer orchestration; good anti-block defaults.
    - **Functionality**: Page handlers, link extraction, proxy rotation, storage adapters.
  - **Firecrawl API (cloud crawler)**
    - **Capabilities**: API-first crawling/ingestion of sites with JS rendering, sitemaps, and structured output.
    - **Advantages**: Fast to integrate; offloads headless browser ops and anti-bot tactics.
    - **Functionality**: Submit seeds/domains; receive normalized HTML, markdown, and extracted metadata.

- **Headless browsers & anti-bot resilience**
  - **Playwright / Puppeteer**
    - **Capabilities**: Reliable JS rendering, network interception, device emulation, Chromium/Firefox/WebKit.
    - **Advantages**: Scriptability for login flows, client-side routing, and SPA hydration.
    - **Functionality**: Navigate, wait-for selectors, extract DOM; export HAR/snapshots for evidence.
  - **Stealth/undetected drivers + session management**
    - **Capabilities**: Reduce detection; rotate user-agents, timezones, fingerprints, and cookies.
    - **Advantages**: Increases success against WAF/CDN challenges while respecting rate/robots.
    - **Functionality**: Session pooling, human-like delays, backoff on 429/403.
  - **Smart proxies (Zyte, Bright Data, Oxylabs, ScraperAPI)**
    - **Capabilities**: Residential/datacenter/mobile pools; country/ASN targeting; CAPTCHA solving options.
    - **Advantages**: Reliability under blocks; centralized rotation; compliance tooling.
    - **Functionality**: Per-request geotargeting, header injection, concurrency controls.

- **Social media data extraction**
  - **Apify actors (Reddit, X/Twitter, YouTube, Instagram, LinkedIn, TikTok)**
    - **Capabilities**: Ready-made, maintained scrapers with cloud execution and data stores.
    - **Advantages**: Rapid setup; scales without infra; webhooks/integrations.
    - **Functionality**: Extract posts, comments, profiles, engagement; schedule runs.
  - **TexAu / PhantomBuster (automation)**
    - **Capabilities**: No-/low-code social workflows for profiles, posts, and engagement metadata.
    - **Advantages**: Visual builders; many connectors; rate control baked in.
    - **Functionality**: Sequences that gather data and optionally trigger outreach (disabled for research-only).
  - **Official APIs (prefer when available/approved)**
    - **X (Academic/Enterprise), Reddit API, YouTube Data API, LinkedIn Partner APIs, Facebook/Instagram Graph API**
    - **Advantages**: Terms-compliant; higher stability; richer metadata; fewer block risks.
    - **Functionality**: Query posts, comments, channels/subreddits/spaces; paginate; filter; fetch insights (scope-dependent).
  - **Monitoring/Listening platforms (YouScan, Brandwatch, Meltwater)**
    - **Capabilities**: Cross-network monitoring with text/image analysis and alerting.
    - **Advantages**: Always-on ingestion; dashboards for sentiment/topics/volume.
    - **Functionality**: Query by brand/org/keyword; export mentions and analytics.

- **AI-powered extraction & enrichment**
  - **Diffbot**
    - **Capabilities**: ML/computer-vision extraction to structured objects; massive web knowledge graph.
    - **Advantages**: Minimal parser maintenance; entity resolution across the open web.
    - **Functionality**: Article/Product/Organization APIs; KG queries to enrich org profiles.
  - **NetOwl**
    - **Capabilities**: Entity/relation/event extraction, sentiment, geotagging across multilingual text.
    - **Advantages**: Enterprise-scale text analytics; integrates with big data stacks.
    - **Functionality**: Batch and stream NLP pipelines for documents and social data.

- **Aggregated datasets (to reduce crawling load)**
  - **GDELT, Media Cloud**: Global news/events monitoring; topic/time-series; source diversity.
  - **Common Crawl**: Historical web snapshots; WARC access; reduce live crawling.
  - **Wikidata/DBpedia/Wikipedia**: Organization entities, properties, references.
  - **OpenCorporates**: Corporate registry data; directors, filings (jurisdiction-dependent).
  - **OpenAlex**: Scholarly works/orgs; if research outputs inform ethos/mission.
  - **GitHub GraphQL / GitLab API / npm / PyPI**: Repos, licenses, contributions for OSS evidence.
  - **Web3 governance**: Snapshot API, Tally API, Boardroom, DeepDAO; decisions, turnout, delegates.
  - **Ecosystem/crypto**: CoinGecko, DeFiLlama, L2Beat (for economic/treasury signals where relevant).

- **Search & discovery accelerators**
  - **SerpAPI, Tavily API, SearXNG**
    - **Capabilities**: Programmatic search across engines or metasearch.
    - **Advantages**: Finds primary sources fast; supports site/domain scoping.
    - **Functionality**: Query org properties (site/forum/docs/blog/GitHub) in parallel; capture URLs for crawlers.

- **Model Context Protocol (MCP) servers and utilities**
  - **HTTP/Fetch MCP**
    - **Capabilities**: Standardized, tool-governed HTTP GET/POST for evidence capture.
    - **Advantages**: Auditable requests; policy controls; easy to compose in assistants.
    - **Functionality**: Retrieve pages, JSON APIs, and sitemaps directly from an AI workflow.
  - **Browser/Playwright MCP**
    - **Capabilities**: Headless browsing via MCP with navigation, DOM queries, snapshots.
    - **Advantages**: Works on JS-heavy sites; consistent with assistant guardrails.
    - **Functionality**: Login flows, screenshot proof, structured extraction.
  - **Search MCP (e.g., Tavily/SerpAPI)**
    - **Capabilities**: Search from within assistant; unify result ranking and filtering.
    - **Advantages**: Faster source discovery; reproducible logs.
    - **Functionality**: Site-scoped discovery against `MAIN_SITE`, `FORUM_URL`, etc.
  - **GitHub MCP**
    - **Capabilities**: GraphQL/REST queries to repos, PRs, issues.
    - **Advantages**: First-party OSS evidence with rate-limit-aware access.
    - **Functionality**: Pull license files, contribution stats, governance docs.
  - **Firecrawl MCP / Apify MCP (community/bridge)**
    - **Capabilities**: Delegate crawling/scraping to hosted services via MCP.
    - **Advantages**: Offloads anti-bot heavy lifting; single, auditable interface.
    - **Functionality**: Submit crawl jobs; retrieve structured datasets for evidence rows.

### How this maps to the templates

- `template_data.md` (evidence):
  - Use Search MCP + SerpAPI/Tavily to discover pages within `MAIN_SITE`, `FORUM_URL`, `DOCS_OR_MANUAL_URL`, `BLOG_OR_NEWS_URL`, `GITHUB_ORG_URL`, `SNAPSHOT_SPACE`, `TALLY_SPACE`.
  - Use Crawlee/Playwright or Firecrawl to capture page content and citations.
  - Use official/social APIs or Apify actors for posts, votes, proposals, maintainers.
  - Use Diffbot/Wikidata/OpenCorporates to enrich org metadata.
- `template_compilation.md` (scoring):
  - Aggregate signals for Structural/Operational/Economic/Cultural layers with explicit citations.
  - Compute layer averages; capture Hybrid X-ray and Ethos rationales referencing evidence IDs.

### Proposed suite (integrated, practical stack)

- **Discovery**: Tavily or SerpAPI (and a Search MCP) for fast primary-source URL harvesting.
- **Site crawling**: Crawlee (Playwright) for JS-heavy org properties; Scrapy for static/sitemap coverage.
- **Social data**: Apify actors for Reddit/X/YouTube/LinkedIn/TikTok; prefer official APIs where approved.
- **Anti-bot & reliability**: Zyte Smart Proxy Manager (or Bright Data/Oxylabs) with geographic targeting.
- **Enrichment**: Diffbot for org/article structuring; Wikidata/OpenCorporates for cross-checking.
- **Web3 governance (if applicable)**: Snapshot + Tally APIs for proposals, participation, delegates.
- **MCP layer**: HTTP/Fetch MCP, Browser/Playwright MCP, Search MCP, GitHub MCP, and a Firecrawl/Apify bridge.
- **Storage & indexing**: Postgres/DuckDB for tabular evidence; OpenSearch/Elasticsearch for text search; object storage for snapshots.
- **Orchestration & QA**: Airflow/Prefect for pipelines; Great Expectations for data quality checks.

### Implementation plan (phased)

1) **Requirements & governance** (1–2 weeks)
   - Define evidence fields aligned to `template_data.md` (IDs, URLs, selectors, citation text, timestamps).
   - Approvals for official social APIs; review TOS/robots; document compliance posture.
   - Choose proxy vendor and MCP servers (Fetch, Browser, Search, GitHub; optional Firecrawl/Apify bridges).

2) **MVP collection** (2–3 weeks)
   - Implement Discovery via Search MCP for each org variable (site/forum/docs/blog/GitHub/Snapshot/Tally).
   - Build Crawlee + Playwright spider for org properties; add Scrapy for sitemap/static pages.
   - Integrate Apify actors for at least two social networks; store outputs to Postgres/DuckDB.
   - Add Snapshot/Tally API harvesters where relevant; basic Diffbot enrichment for org pages.

3) **Hardening & coverage** (2–4 weeks)
   - Add smart proxy rotation; session pools; exponential backoff on 429/403; retry policies.
   - Expand to additional socials/APIs; add GitHub GraphQL metrics (license, contributors, governance files).
   - Introduce Great Expectations tests; add OpenSearch index for full-text search of evidence.

4) **Scoring & reporting** (1–2 weeks)
   - Implement transformations that compute per-dimension signals for `template_compilation.md`.
   - Generate Hybrid X-ray and Ethos tables with linked evidence IDs; verify averages.
   - Optional: build a radar chart of layer averages and an executive summary export.

5) **Continuous monitoring** (ongoing)
   - Schedule crawls/social collections; watch deltas; refresh evidence and citations.
   - Add alerting for governance changes (new proposals/votes), license changes, or policy updates.
   - Maintain allowlist/denylist; update compliance notes and provenance logs.

### Compliance, ethics, and resilience notes

- Prefer official APIs and platform-approved access where available; respect robots.txt and site TOS.
- Avoid PII collection; focus on public, organization-level content; document provenance.
- Rate-limit conservatively; add backoff and circuit breakers; log request/response metadata for audits.
- Keep human-in-the-loop for ambiguous classifications; store raw snapshots for verification.

### Deliverables alignment

- A repeatable pipeline that populates `case-study/{{ORG_NAME}}_data.md` with cited evidence.
- A companion `case-study/{{ORG_NAME}}_compilation.md` with computed scores, X-ray, and ethos tables.
- Optional executive summary and charts, using stored aggregates.


