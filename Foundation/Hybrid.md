# Hybrid organizations

Most organizations that are seen in the p2p space are actually hybrid. This is normal, as nothing appears from nothing, everything is context dependent and as p2p evolves new organizations will acquire more p2p characteristics and shed traditional characteristics. The world is in transition today, so all open and network-type organizations carry some level of legacy within them. When we assess the level of p2p-ness of an organization we don’t just want a score on various dimensions, we also want to understand why and what legacy structures pull this organization away from being genuine or pure p2p. In order to assess the hybrid makeup of current organizations we need

* a compact “X-ray” comparison (many dimensions) to spot P2P vs traditional characteristics;  
* a catalog of **hybridization dimensions** (concrete signals you can observe / scrape) so you can explain *why* a P2P score looks the way it does;  
* a set of **hybridization models / patterns** with real examples (what to look for in the wild); and  
* a short practical checklist for performing the X-ray on a real organization.

We are using some OVN documentation, as well as key web sources (Benkler on commons-based peer production, Red Hat / Mozilla examples, DAO wrappers, platform co-ops and open-core) to ground the patterns below. 

# X-ray: short comparative map (open networks vs traditional orgs — plus hybrid signals)

Use this as the visual “X-ray” you’ll fill when evaluating an organization. For each dimension below I give: (A) the *P2P signature*, (B) the *Traditional signature*, and (C) *Hybrid signals / what to scrape or ask for*.

Note: many of these are already in our Principles or p2p doc (layered approach, commons orientation, governance, contribution accounting) — we map those operationally here so a researcher/scraper can gather evidence.

### **Structural & legal**

**Legal existence / entity**

* P2P: de-facto networks, loose federations, many contributors with no single legal owner; sometimes stewarded by a foundation or commons steward.  
* Traditional: incorporated company (LLC / C-corp / NGO) with clear legal owner(s).  
* Hybrid signals: presence of a foundation *and* a taxable subsidiary; presence of legal wrappers for DAOs; mixed legal filings (e.g., foundation \+ commercial spinoff). (Look: articles of incorporation, registry entries, trustee lists, foundation vs. corp filings.) ([Mozilla](https://www.mozilla.org/en-US/about/governance/organizations/?utm_source=chatgpt.com))

**Ownership of IP / outputs**

* P2P: outputs licensed to a commons (open licenses), nondominium regimes or public domain.  
* Traditional: IP assigned to the company; proprietary licenses.  
* Hybrid signals: dual-licensing, open core (core under OSS license, certain modules proprietary), contributor license agreements that assign IP to a central org. (Check LICENSE files, CLA/assignment docs, dual-license terms.) ([Wikipedia](https://en.wikipedia.org/wiki/Open-core_model?utm_source=chatgpt.com))

**Capital structure / funding**

* P2P: grants, donations, contributions, cooperative revenue-sharing, token models, service income to sustain commons.  
* Traditional: equity investors, VC, bank debt, retained earnings.  
* Hybrid signals: a mix — a public foundation raising donations \+ a for-profit arm selling services; token issuance plus institutional investors; subscription revenue for hosted services of an open project (open-core). (Look at annual reports, funding rounds, token capsheets, investor term sheets.) ([WIRED](https://www.wired.com/story/ibm-buying-open-source-specialist-red-hat-34-billion?utm_source=chatgpt.com))

### **Governance & decision-rights**

**Decision making**

* P2P: distributed, meritocratic or consensus-based (meritocracy via contribution), encoded governance processes or on-chain votes.  
* Traditional: top-down board \+ executive team; representative governance.  
* Hybrid: community decision making for technical/product matters but final legal/contractual decisions retained by a board (foundation or corp). (Look at bylaws, governance charters, recorded votes, GitHub / forum governance threads.) ([Institute of Network Cultures](https://networkcultures.org/cpov/resources/resources_in_english/wikimedia-evolution-in-terms-of-governance-and-the-creation-of-a-foundation/?utm_source=chatgpt.com))

**Formal authority vs emergent authority**

* P2P: authority emerges from contribution/reputation (social capital).  
* Traditional: authority flows from titles & contracts.  
* Hybrid: emergent technical authority (maintainers) \+ formal authority to sign contracts (a legal entity). Check whether maintainers have signing authority or whether only the corporate box signs. (Inspect role lists, signatories on contracts and invoices.)

### **Economic & value flows**

**Contribution accounting & reward mechanisms**

* P2P: explicit contribution accounting for diverse contributions (OVN-style accounting), reputation & redistribution mechanisms.  
* Traditional: salaries, profit distribution to shareholders.  
* Hybrid: open contribution logs \+ a corporate payroll for staff; token incentives for some contributors and salaries for others. (Scrape contribution ledgers, contribution accounting spreadsheets, payroll reports.) ([MDPI](https://www.mdpi.com/2078-2489/11/2/104?utm_source=chatgpt.com))

**Revenue model**

* P2P: commons provisioning, services around the commons (hosting, consultancy), grants, voluntary contributions, token mechanisms.  
* Traditional: product sales, subscriptions, licensing, investor exits.  
* Hybrid signals: “sell services around the commons” (support, hosted services) / open-core subscriptions / dual licensing. (Look at commercial offerings, pricing pages, support contracts.) ([Red Hat](https://www.redhat.com/en?utm_source=chatgpt.com))

**Distribution of surplus (who benefits)**

* P2P: redistribution to contributors, community funds, cooperative dividends.  
* Traditional: retained earnings to shareholders/founders.  
* Hybrid: part of tangible benefits are returned to commons/foundation, while shareholders get equity. (Check profit allocation clauses and grant programs.)

### **Technical & platform**

**Code/data openness**

* P2P: open repositories, open data, public auditability.  
* Traditional: private source, closed datasets.  
* Hybrid: core open codebase, proprietary hosted features (open-core), or private forks run by a corporate service. (Check GitHub/git history, published datasets, API access rules.) ([Wikipedia](https://en.wikipedia.org/wiki/Open-core_model?utm_source=chatgpt.com))

**Infrastructure control**

* P2P: many independent nodes, federation, nondominium.  
* Traditional: centralized servers, single vendor control.  
* Hybrid: federated network where a firm runs major hubs/instances (e.g., Mastodon instances run by companies) — concentration risk. (Look at who operates top instances, hosting contracts, infra ops logs.)

### **Operational & coordination**

**Coordination mode**

* P2P: stigmergy / asynchronous signals (issue trackers, RFCs, pull requests).  
* Traditional: planned top-down scheduling, hierarchical workflows.  
* Hybrid: open issue trackers for community but product roadmap controlled by paid product team. (Check issue assignment patterns, roadmap ownership.)

**Hiring / employment model**

* P2P: contributions from volunteers and paid freelancers; fluid affiliation.  
* Traditional: employees with contracts, benefits, payroll.  
* Hybrid: core paid staff (payroll) \+ broad volunteer contributor base. (Inspect payroll, contractor agreements, contributor onboarding.)

**Conflict & fork management**

* P2P: forking is accepted; disputes resolved in community channels.  
* Traditional: legal dispute resolution, board decisions, arbitration.  
* Hybrid: community can fork the commons but the corporation holds trademarks / brand and can block use — this creates tension. (Look at trademark policies, license terms, past forks and litigations.)

### **Culture, identity & social**

**Values & narrative**

* P2P: explicit commons, reciprocity, openness, reflexivity (your docs emphasize this strongly).  
* Traditional: profit / mission statements aligned to corporate goals.  
* Hybrid: public rhetoric of openness while internal metrics & incentives reward revenue growth. (Compare public mission statements vs internal KPIs, OKRs.)

**Reputation & crediting**

* P2P: fine-grained attribution and reputational records (commit history, contribution accounting).  
* Traditional: employer CVs, titles; contribution hidden behind corporate projects.  
* Hybrid: corporate PR packages for major contributors while community has separate reputation trails. (Check contributor graphs, authorship metadata.)

### **Ecosystem / external relations**

**Relationship to markets & incumbents**

* P2P: seeks to displace intermediaries, build commons; may cooperate with incumbents.  
* Traditional: market competition, B2B sales, strategic partnerships.  
* Hybrid: partnerships with incumbents (e.g., corporate sponsorship), sponsored devs inside community; capture risk. (Check sponsorship lists, corporate-funded developer programs.)

**Regulatory / compliance posture**

* P2P: may try to avoid centralized compliance models; uses legal hacks or new wrappers.  
* Traditional: compliance front & centre (tax, labor, data).  
* Hybrid: DAO with LLC wrapper; foundation handling compliance while network remains permissionless. (Look for legal wrappers, counsel memos, filings.) ([Paradigm](https://www.paradigm.xyz/2022/06/dao-strategy-and-legal-wrappers?utm_source=chatgpt.com))

# Exhaustive catalog of hybridization dimensions (what to flag — evidence and how it explains the P2P score)

Below we expand the X-ray into a longer checklist you can use during a P2P assessment. For each item I say *why it matters* and *concrete evidence to capture*.

**Legal & governance**

* *Single legal signatory vs distributed signatories* — matters because legal control often beats social norms. Evidence: contracts, authorized signatory lists, bank signers.  
* *Presence of a foundation / non-profit steward* — often means commons stewarding plus possible commercial arms. Evidence: foundation charter, relationship docs. ([Mozilla](https://www.mozilla.org/en-US/about/governance/organizations/?utm_source=chatgpt.com))  
* *Board composition* — if board drawn from corporate investors, expect traditional capture. Evidence: board minutes, director bios.  
* *Governance rules codified vs implicit* — formal bylaws show traditional structure; RFC-style procedures show P2P practice. Evidence: bylaws, governance RFCs.

**Financial & value**

* Who gets cash flows? — distribution clauses / payroll vs community grants. Evidence: financial statements, beneficiary lists; public budgets and allocation criteria links.  
* Investor agreements and liquidation preferences — indicate traditional exit incentives. Evidence: term sheets, cap table.  
* Tokenomics design & control — tokens can be P2P or investor capture tools. Evidence: token distribution schedules, vesting terms. ([makerdao.com](https://makerdao.com/en/whitepaper/?utm_source=chatgpt.com))  
   Open contribution accounting (OVN) presence — explicit sign of P2P economic modeling. Evidence: contribution logs, OVN ledger exports.

**Product & IP**

*  License type(s) — public/open license vs corporate assignment. Evidence: LICENSE, contributor licence agreements. ([Wikipedia](https://en.wikipedia.org/wiki/Open-core_model?utm_source=chatgpt.com))  
*  Dual licensing / open-core — explicit hybrid commercial strategy. Evidence: product comparisons, pricing pages. ([Wikipedia](https://en.wikipedia.org/wiki/Open-core_model?utm_source=chatgpt.com))

**Technical & infra**

* Instance operators & control of infrastructure — if a few operators run infra, expect centralization. Evidence: hosting contracts, server lists.  
* Data portability & federated standards — whether the network uses interoperable protocols. Evidence: protocol docs, API specs.

**Operations**

* Who sets the roadmap — community vs paid product managers. Evidence: roadmap owners, issue triage logs.  
* Hiring / payroll vs volunteer reliance — balance indicates hybridization. Evidence: payroll, contributor time logs.

**Culture & social**

* Public rhetoric vs internal KPIs — mismatch signals hybridization/mission drift. Evidence: internal OKRs vs public mission.  
* Credit / attribution practices — whether non-paid work is visible and rewarded. Evidence: commit logs, contributor dashboards.

**Risk & accountability**

* Legal risk absorbency — who takes responsibility for lawsuits? Evidence: indemnity clauses, insurance.  
* Forkability & portability of contributions — whether contributions survive forks. Evidence: license terms, migration docs.

**External dependencies**

* Sponsorship & corporate funding — corporate money can shape priorities. Evidence: sponsorship pages, funding lines.  
* Dependence on platform providers — if project hosted on single cloud vendor, it can be more traditional. Evidence: hosting invoices.

(You can turn this checklist into scraping rules: e.g., search for "foundation", "LLC", "Contributor License Agreement", "LICENSE", "Tokenomics", "term sheet", "board", "payroll", "roadmap owner", "contribution accounting export", "Git history".)

# Hybridization models (patterns you’ll see in the wild) — what they look like and examples

Below are common hybrid architectures, their logic, what to watch for and a real example.

**Foundation \+ For-profit subsidiary (dual box)**

* *Logic*: Foundation stewards commons & mission; for-profit sells services and returns some surplus.  
* *Pros/cons*: Governance separation, legal clarity for commercial deals; risk of capture if the for-profit dominates.  
* *Examples*: Mozilla Foundation \+ Mozilla Corporation. ([Mozilla](https://www.mozilla.org/en-US/about/governance/organizations/?utm_source=chatgpt.com))

**Open-core company**

* *Logic*: Core is open; advanced features or hosted services are paid.  
* *Pros/cons*: Enables sustainable revenue; controversy about whether it’s “true” open source.  
* *Examples*: GitLab (open-core subscriptions), many enterprise OSS firms; see open-core literature. ([The GitLab Handbook](https://handbook.gitlab.com/handbook/company/stewardship/?utm_source=chatgpt.com))

**Foundation (or non-profit) steward \+ commercial ecosystem**

* *Logic*: Foundation funds governance & standards; commercial firms provide implementation and services.  
* *Example*: Linux Foundation \+ corporate ecosystem (Red Hat historically built services around Linux). ([Red Hat](https://www.redhat.com/en?utm_source=chatgpt.com))

**DAO \+ legal wrapper (LLC / foundation / association)**

* *Logic*: On-chain governance \+ an entity that signs contracts, hires staff, or holds assets.  
* *Watch for*: who the legal wrapper is accountable to; whether token holders have real influence. ([Paradigm](https://www.paradigm.xyz/2022/06/dao-strategy-and-legal-wrappers?utm_source=chatgpt.com))

**Multi-stakeholder cooperative \+ token**

* *Logic*: Cooperative legal form for workers/users \+ token layer to coordinate micro-incentives.  
* *Example clue*: platform cooperatives such as CoopCycle or worker co-op platforms; see platform co-op literature. ([tripleC](https://www.triple-c.at/index.php/tripleC/article/view/1418/1504?utm_source=chatgpt.com))

**Commons steward \+ service company (two-tier)**

* *Logic*: Community maintains commons; a service company (for-profit) is contracted to provide recurring ops. Sensorica’s OVN often exhibits service and commons roles separated.

**Corporate sponsorship of community contributors**

* *Logic*: Corporations employ developers who contribute to commons (risk: vendor capture).  
* *Evidence*: corporate-funded projects, paid maintainers on GitHub. (E.g., corporate sponsorship on many OSS projects; Red Hat’s ecosystem being bought by IBM is a business example of this tension). ([WIRED](https://www.wired.com/story/ibm-buying-open-source-specialist-red-hat-34-billion?utm_source=chatgpt.com))

**Open-source core \+ private forks (semi-closed hybrid)**

* *Logic*: Project open but major actors run closed forks or proprietary versions — technically hybrid and can centralize. Evidence: proprietary forks, enterprise forks. ([Wikipedia](https://en.wikipedia.org/wiki/Open-core_model?utm_source=chatgpt.com))

**Federated network with corporate hubs**

* *Logic*: Protocol is federated (P2P), but a few commercial operators run large instances (centralization-by-scale). Example: Mastodon ecosystem (some large instances are run by companies). (Look for concentration of total activity on a handful of instances.)

**Spinout / corporate capture pattern**

* *Logic*: Community starts as commons, spinouts create companies that then capture revenue/attention. Evidence: spinout announcements, corporate acquisitions of open-source companies (Red Hat/IBM). ([WIRED](https://www.wired.com/story/ibm-buying-open-source-specialist-red-hat-34-billion?utm_source=chatgpt.com))

# Examples (where hybridization is visible)

* **Sensorica / OVN** — explicitly designed as an Open Value Network with open contribution accounting and commons orientation; good example of a high-P2P model you'll want to benchmark. ([wiki.p2pfoundation.net](https://wiki.p2pfoundation.net/Sensorica?utm_source=chatgpt.com))  
* **Mozilla Foundation \+ Mozilla Corporation** — classic foundation \+ commercial arm hybrid that tries to keep mission while scaling services / products. ([Mozilla](https://www.mozilla.org/en-US/about/governance/organizations/?utm_source=chatgpt.com))  
* **Red Hat → IBM** — Red Hat commercialized open source via services & subscriptions and was later acquired — a canonical path from community/open project to large corporate structure. Useful to illustrate capture/exits. ([Red Hat](https://www.redhat.com/en?utm_source=chatgpt.com))  
* **GitLab (open-core)** — open source core \+ paid tiers for customers; shows how open-core sustains product development while introducing hybrid incentives. ([The GitLab Handbook](https://handbook.gitlab.com/handbook/company/stewardship/?utm_source=chatgpt.com))  
* **MakerDAO / other DeFi DAOs** — show on-chain governance combined with foundations / legal entities to interact with off-chain world — a DAOs-with-wrappers strategy. ([makerdao.com](https://makerdao.com/en/whitepaper/?utm_source=chatgpt.com))  
* **Platform co-ops (CoopCycle, Resonate)** — examples of explicitly cooperative alternatives to platform capitalism (illustrate different hybrid mixes of membership, revenue, service). ([tripleC](https://www.triple-c.at/index.php/tripleC/article/view/1418/1504?utm_source=chatgpt.com))

# How to reveal hybrid features when you evaluate P2P-ness (data & scraping recipe)

When you run the P2P assessment, augment scores with a “hybridization profile” that records evidence for traditional features. For each dimension collect:

1. **Public legal & governance docs**: bylaws, articles, committees, board lists, minutes, charters. *Signal*: board with investor seats → traditional.  
2. **Financials**: audited reports, tax returns, sponsor lists, investor term sheets, payroll records. *Signal*: \>50% revenue from subscriptions / VC → traditional tilt.  
3. **Contribution logs & contribution accounting**: commits, pull requests, OVN ledgers. *Signal*: fine-grained public attribution → P2P tilt.  
4. **License & IP agreements**: LICENSE, CLAs, dual license statements. *Signal*: proprietary clause or CLA assigning IP to a corp → traditional. ([Wikipedia](https://en.wikipedia.org/wiki/Open-core_model?utm_source=chatgpt.com))  
5. **Token / equity distribution**: cap tables, token allocation/who holds tokens/vesting schedules. *Signal*: concentrated token holdings or long vesting to insiders → traditional capture. ([makerdao.com](https://makerdao.com/en/whitepaper/?utm_source=chatgpt.com))  
6. **Roadmap & issue ownership**: Who merges PRs, who sets roadmap; check product owner email domains. *Signal*: corporate email domain dominates commits/merges → traditional influence.  
7. **Infrastructure operation**: list of instance operators, major hosts, who pays infra costs. *Signal*: single provider bills → centralization.

8. **Contract signatories**: who signs contracts (foundation vs corp vs unknown) — tells you who has the legal power.  
9. **Media / PR / governance narratives**: compare public mission vs internal KPIs where possible. *Signal*: public commons rhetoric vs internal revenue KPIs → hybridity/mission drift.

Use the **two-axis** record per dimension: P2P fidelity (0–5) and Traditional fidelity (0–5). This produces a heatmap: areas where both scores are high \= *hybrid*; where Traditional \>\> P2P \= *captured/legacy*; where P2P \>\> Traditional \= *pure P2P*.

# Practical checklist you can run now (quick scoring & flags)

When you evaluate a candidate org, fetch these items first (fast wins to reveal hybridization):

* “About / Governance” page (who sits on the board?). ([Wikimedia Foundation](https://wikimediafoundation.org/what-we-do/?utm_source=chatgpt.com))  
* LICENSE, CONTRIBUTING.md, CLA or IP assignment files. ([Wikipedia](https://en.wikipedia.org/wiki/Open-core_model?utm_source=chatgpt.com))  
* Financials / annual report or fundraising announcements. ([WIRED](https://www.wired.com/story/ibm-buying-open-source-specialist-red-hat-34-billion?utm_source=chatgpt.com))  
* Git history (top committers, top PR mergers).  
* Meeting minutes or governance proposals (e.g., GitHub/EIP/DAO governance forum). ([makerdao.com](https://makerdao.com/en/whitepaper/?utm_source=chatgpt.com))  
* Contribution logs (OVN ledgers if present).  
* Token/ equity distribution (if present). ([makerdao.com](https://makerdao.com/en/whitepaper/?utm_source=chatgpt.com))  
* Any “foundation \+ corp” relationships (press, charter). ([Mozilla](https://www.mozilla.org/en-US/about/governance/organizations/?utm_source=chatgpt.com))

**Red flags** to surface automatically in your report:

* CLA that assigns all contributor IP to a central company. ([Wikipedia](https://en.wikipedia.org/wiki/Open-core_model?utm_source=chatgpt.com))  
* Large fraction of revenue from a single corporate sponsor.  
* Token allocation concentrated with founders / investors \> 40%. ([makerdao.com](https://makerdao.com/en/whitepaper/?utm_source=chatgpt.com))  
* Roadmap and merges dominated by employees of a single company.  
* Trademark or brand held by a company that can block forks.

# Short summary & suggested next steps

* We already have a clear layered P2P rubric in our doc; the next step is to operationalize hybrid detection by adding the X-ray checklist above to each dimension and collecting the 9 document types I list.  
* We can store per-dimension two numeric axes (P2P, Traditional) \+ a short evidence note and links to source documents. That gives you both a score and an explainable X-ray of *why* the score looks like it does (where the organization is hybrid).  
* We can:  
  1. produce a **spreadsheet template** (dimensions × levels × P2P/traditional axes \+ evidence links) that you can drop into a scraper; or  
  2. take a real organization you pick and run one example X-ray to show the method in practice.

# Others

They are also transitional models such as sociocracy, S3, O2, Holocracy, etc.

