# {{ORG_NAME}} — Evidence Repository (for P2P-ness Assessment)

Purpose: Collect verifiable data and links about {{ORG_NAME}}, organized by the evaluation framework in `Evaluation.md` (layers × dimensions × levels), with traceability to the fundamental principles in `Model.md`. Each item should include a short note, a status tag, a confidence tag, and source link(s).

## Variables (set these first)
- ORG_NAME: {{ORG_NAME}}
- ASSESSOR: {{ASSESSOR_NAME_OR_HANDLE}}
- ASSESSMENT_DATE: {{YYYY-MM-DD}}
- SCOPE_LEVELS: {{PROJECT / OPEN-ENTERPRISE / NETWORK / GLOBAL — mark which apply; others are N/A}}
- PRIMARY_URLS: {{PRIMARY_URLS}}
- MAIN_SITE: {{MAIN_SITE_URL}}
- FORUM_URL: {{FORUM_URL}}
- DOCS_OR_MANUAL_URL: {{DOCS_OR_MANUAL_URL}}
- BLOG_OR_NEWS_URL: {{BLOG_OR_NEWS_URL}}
- GITHUB_ORG_URL: {{GITHUB_ORG_URL}}
- GOVERNANCE_PORTALS: {{GOVERNANCE_PORTALS — e.g., Snapshot, Tally, Boardroom, DeepDAO, Discourse, custom governance UI}}
- SNAPSHOT_SPACE: {{SNAPSHOT_SPACE_OR_URL — optional}}
- TALLY_SPACE: {{TALLY_SPACE_OR_URL — optional}}
- REGISTRY_URL: {{REGISTRY_URL — optional; e.g., OpenCorporates entry}}
- WAYBACK_URLS: {{WAYBACK_URLS — optional; founding-era snapshots}}

---

## Evidence Conventions (apply to every finding)

- **Status** (required, one of):
  - `Evidenced` — claim supported by at least one primary source.
  - `Partially evidenced` — some support, but incomplete or indirect.
  - `Not evidenced` — looked for, not found. **This is not a negative finding.**
  - `Contradicted` — sources conflict, or official claims conflict with observed practice. Record both sides.
- **Confidence** (required): `High` | `Medium` | `Low`.
- **Citations**: 1–3 public URLs per finding; prefer primary sources. For volatile pages (roadmaps, governance rules, token allocations), also capture a Wayback Machine snapshot link.
- Absence of evidence is not evidence of absence: `Not evidenced` items become TODOs in the checklist, not zeros in scoring.

## Method: Web Search & Capture Protocol
- Run parallel searches across:
  - Official site, forum/governance, docs/handbook/manual, blog/newsroom
  - GitHub org (repos, LICENSE, CONTRIBUTING, governance files, contributor insights)
  - Governance portals (Snapshot/Tally/Boardroom/DeepDAO or equivalent), foundation filings, whitepapers
  - Registries and archives: OpenCorporates (legal entities, directors), trademark registries (USPTO/EUIPO), Wayback Machine (founding-era pages, earlier governance rules), GitHub contribution graphs
- Use a consistent citation style: include the public URL for every claim.
- Capture in this format under each dimension:
  - Findings: 1–3 bullets, concise, factual, each with Status + Confidence
  - Citations: 1–3 links (prefer primary sources)
- Capture complexity-upgrade evidence:
  - Founding history, early governance choices, initial asset/token/equity allocation, and persistent admin rights.
  - Reputation systems, contributor hierarchies, delegation patterns, and potential incumbent lock-in.
  - Transparency/privacy boundaries: what is public, what is private, and how peer verification avoids surveillance.
  - Capital influence: investor/donor/sponsor rights, treasury controls, exit pressures, and commons-governance constraints.
  - Scenario or simulation inputs for contribution accounting, governance thresholds, benefit distribution, and reputation.
- Assessor ethics: respect robots.txt and site terms of service; collect only public, organization-level content; do not collect personal data beyond what the organization itself publishes for accountability purposes; practice the same privacy-preserving transparency the framework demands. For tooling options at scale, see `Others/Web-and-Social-Data-Sourcing.md`.

### Query bank (replace {{ORG_NAME}})
- "site:{{MAIN_SITE_HOST}} governance"; "site:{{FORUM_HOST}} proposal governance process"; "site:{{DOCS_HOST}} governance overview"; "site:github.com {{ORG_NAME}} license"
- "{{ORG_NAME}} foundation legal wrapper jurisdiction"; "{{ORG_NAME}} Snapshot space"; "{{ORG_NAME}} Tally proposals"
- "{{ORG_NAME}} grants round recap"; "{{ORG_NAME}} maturity framework"; "{{ORG_NAME}} brand trademark policy"
- "site:opencorporates.com {{ORG_NAME}}"; "{{ORG_NAME}} annual report OR financial statements"; "{{ORG_NAME}} trademark site:uspto.gov OR site:euipo.europa.eu"
- "web.archive.org {{MAIN_SITE}}" (founding-era about/governance pages); "{{ORG_NAME}} contributors insights site:github.com"; "site:deepdao.io OR site:boardroom.info {{ORG_NAME}}"
- "{{ORG_NAME}} contributor survey OR retrospective OR postmortem"; "{{ORG_NAME}} fork OR split community"; "{{ORG_NAME}} energy OR ecological footprint"

---

## Index of Primary Sources (live)
- Main site: {{MAIN_SITE}}
- Governance forum: {{FORUM_URL}}
- Handbook / governance manual: {{DOCS_OR_MANUAL_URL}}
- Blog/News: {{BLOG_OR_NEWS_URL}}
- Organization GitHub: {{GITHUB_ORG_URL}}
- Governance portals: {{GOVERNANCE_PORTALS}} (Snapshot {{SNAPSHOT_SPACE}}, Tally {{TALLY_SPACE}})
- Legal registry entry: {{REGISTRY_URL — e.g., OpenCorporates}}
- Wayback Machine snapshots (founding era): {{WAYBACK_URLS}}

---

## 0) Organizational Snapshot & Enterprise Stack Positioning

Anchor: `new-collaborative-entrepreneurship.md` (Enterprise Stack as **heuristic map, not fixed ontology**). Record where the organization operates, and just as importantly, where it does not fit the map.

### 0.1 Snapshot
- One-paragraph description; founding date; founders; declared mission; current scale (contributors, users, budget/treasury).
- Findings:
  -
- Citations:
  -

### 0.2 Enterprise Stack layers in use
Mark each layer: `Active` | `Emerging` | `Absent`, with evidence.

| Stack layer | Code | Status | Evidence (what concretely exists at this layer) |
| ----- | ----- | ----- | ----- |
| Product | P |  |  |
| Service | S |  |  |
| Outcome | O |  |  |
| Value Chain | VC |  |  |
| Value Tree | VT |  |  |
| Platform | PL |  |  |
| Ecosystem | E |  |  |
| Cascading Market | CM |  |  |
| Mission Cascade | MC |  |  |

### 0.3 Business-model patterns present
From the pattern library in `new-collaborative-entrepreneurship.md` and its semantically richer source `Distributed business model patterns - Models.csv` (60 patterns + OVN additions), list the patterns the organization actually runs (e.g., Open Source, Crowdfunding, Revenue Sharing, Freemium, Lock-in, Orchestrator, Subscription).

| Pattern | Where observed | Evidence |
| ----- | ----- | ----- |
|  |  |  |

### 0.4 Where the map does not fit
- Aspects of {{ORG_NAME}} that the Enterprise Stack / pattern library cannot describe without distortion (record these; do not force the fit).
  -

---

## Evaluation Layers and Levels

Layers (per `Evaluation.md`):
- Structural/Formal
- Operational/Process
- Economic
- Cultural/Ecosystem/Superstructural

Levels of scale (per SCOPE_LEVELS; mark non-applicable levels N/A):
- Project level
- Open-Enterprise level
- Network level
- Global/inter-network level

For each dimension below, record: Findings (with Status + Confidence) + Citations.

---

## 1) Structural / Formal Layer

### 1.1 Membership & Entry/Exit
- Findings:
  - Formal criteria, fees, statuses (observer/contributor/core); exit/removal policy; whether participation feels permissionless in lived experience
  -
- Citations:
  -

### 1.2 Role & Task Structure
- Findings:
  - Role definitions; permanent vs emergent roles; self-assignment vs assignment; ability of peers to create/fork roles
  -
- Citations:
  -

### 1.3 Governance & Decision-Making
- Findings:
  - Governance process (discussion → proposal → vote types → ratification), timing (min days), who approves what
  - Voting mechanisms (token voting, 1T1V, QV, consensus, councils/committees), on- vs off-chain
  -
- Citations:
  -

### 1.4 Value Accounting & Rewards / Redistribution
- Findings:
  - How value/funds are allocated (grants, retro, revenue sharing), transparency of totals; whether accounting collapses heterogeneous contributions into a single scalar too early
  -
- Citations:
  -

### 1.5 Legal / Liability / Financial Structures
- Findings:
  - Legal entities (foundation/association/co-op/LLC wrapper), jurisdiction, responsibilities (compliance, banking); signatories
  -
- Citations:
  -

### 1.6 Infrastructure & Commons + Plural Property-Regime Mapping
- Findings:
  - OSS footprint (repos), license posture, shared infra/standards, maintenance burden
  -
- Citations:
  -

Property-regime map (per `Model.md`: P2P economies combine *plural* property regimes — map each layer of the stack; do not assume one regime):

| Asset / artifact | Regime (private / commons / nondominium / public domain / proprietary) | Steward or controller | Evidence |
| ----- | ----- | ----- | ----- |
| Code |  |  |  |
| Data / ledger / contribution history |  |  |  |
| Brand / trademark |  |  |  |
| Infrastructure (servers, hardware, spaces) |  |  |  |
| Tokens / credits (if any) |  |  |  |
| Documentation / content |  |  |  |
| Physical / natural assets (if any) |  |  |  |

---

## 2) Operational / Process Layer

### 2.1 Transparency & Access to Information
- Findings:
  - Publication of minutes/decisions/budgets; cadence of updates
  - Privacy-preserving transparency: what can be verified without exposing sensitive personal or deliberative data
  -
- Citations:
  -

### 2.2 Coordination of Tasks & Workflows (incl. Stigmergy)
- Findings:
  - OSS workflows (issues/PRs), roadmap ownership, org structures (pods, collectives), decision matrices (DACI)
  - Stigmergy signals: what visible traces (open tasks, needs lists, commit history, dashboards, notifications) prompt peers to act without central assignment
  -
- Citations:
  -

### 2.3 Contribution Logging & Attribution
- Findings:
  - Code and non-code attribution; contribution accounting systems; granularity; preservation across forks/reorgs
  -
- Citations:
  -

### 2.4 Conflict Management & Forking
- Findings:
  - Conflict-resolution policies, mediation; repo license types, trademark/brand policy for forks/naming; notable forks and what was preserved across them
  -
- Citations:
  -

### 2.5 Reputation, Trust & Accountability
- Findings:
  - Identity/sybil tools, reputation systems, accountability practices
  - Trust model: where trust is displaced from agents onto protocols/processes (trustlessness), and where it still rests on identity/reputation of persons
  - Reputation capture safeguards: decay/review, appeals, role rotation, contextual reputation, anti-incumbency mechanisms
  -
- Citations:
  -

---

## 3) Economic Layer

### 3.1 Property Regime & Licensing (Commons/Nondominium vs Proprietary)
- Findings:
  - Cross-reference the property-regime map in 1.6; CLAs, dual licensing, open-core boundaries
  -
- Citations:
  -

### 3.2 Contribution & Value Accounting / Benefit Distribution
- Findings:
  -
- Citations:
  -

### 3.3 Funding & Capital Sources
- Findings:
  - Control rights attached to capital, grants, sponsorships, tokens, or revenue dependencies
  - Capital-vs-resources posture: how much of the economy is transactional/capital-based vs contribution/resource-based (non-monetary flows, in-kind, shared assets)
  -
- Citations:
  -

### 3.4 Revenue Model & Market Interface
- Findings:
  - Services around commons, open-core tiers, subscriptions, marketplaces; whether monetization re-centralizes power
  - Disintermediation evidence: does the organization systematically replace centralized intermediaries with distributed mechanisms (in its own structure and in its market)?
  -
- Citations:
  -

### 3.5 Tokenomics & Incentives (if applicable)
- Findings:
  -
- Citations:
  -

### 3.6 Cost Structure & Sustainability
- Findings:
  - Opex/infra costs, runway; ecological/resource costs (energy, hosting, travel) and whether they are disclosed
  -
- Citations:
  -

### 3.7 Economic Openness & Cost Transparency
- Findings:
  - Whether cost transparency supports peer verification without turning into individual surveillance
  -
- Citations:
  -

---

## 4) Cultural / Ecosystem / Superstructural Layer

### 4.1 Values, Norms & Culture
- Findings:
  - Declared values/mission; evidence of alignment in actions; how norm violations are handled
  -
- Citations:
  -

### 4.2 Learning, Adaptation & Innovation
- Findings:
  - Evidence of iteration, retrospectives/postmortems/maturity frameworks; changes over time; reflexivity (does the org openly discuss its own governance limits and risks?)
  -
- Citations:
  -

### 4.3 Meaning, Purpose & Identity
- Findings:
  - Mission coherence across properties; sense of belonging/community identity
  -
- Citations:
  -

### 4.4 Phenomenological Grounding (Lived Experience)
- Findings:
  - Participant narratives about agency, recognition, fairness, trust, meaning, belonging, and care work (use the Participant Narratives Module below where possible)
  - Mismatches between formal openness and lived experience
  -
- Citations:
  -

### 4.5 Ecosystem Relations & External Engagement
- Findings:
  - Partnerships, federations, interoperability/standards participation; relations with incumbents and sponsors
  -
- Citations:
  -

### 4.6 Contextual & Ecological Embeddedness
Anchors: `Model.md`, principle of Contextual Embeddedness; `Evaluation.md`, Cultural layer (Contextual & Ecological Embeddedness dimension).
- Findings:
  - Cosmo-local practice: knowledge/design shared globally, production instantiated locally
  - Ecological limits: awareness/disclosure of footprint; reduction of duplication; biophysical constraints acknowledged in design
  -
- Citations:
  -

---

## 5) Product/Protocol Notes (Context for Commons Orientation)

### 5.1 Core Protocols/Products (e.g., Grants protocol, Identity, etc.)
- Findings:
  - Purpose, openness, governance, repos/docs
- Citations:
  -

### 5.2 Additional Tooling/Stacks
- Findings:
  -
- Citations:
  -

---

## 6) Level-specific Observations

For each in-scope level (per SCOPE_LEVELS), note how the dimensions manifest differently at that level. Mark out-of-scope levels N/A.

### Project level
-

### Open-Enterprise level
-

### Network level
-

### Global / inter-network level
-

---

## 7) Participant Narratives Module (feeds 4.4; optional but strongly recommended)

Web sources cannot capture lived experience. Where permitted, collect first-person evidence:

- **Method**: 3–8 semi-structured interviews or an anonymous survey; include a mix of core contributors, peripheral contributors, newcomers, and (if reachable) departed contributors.
- **Consent & anonymity**: informed consent; publish only anonymized quotes; no PII; aggregate sensitive themes. The assessor must practice the privacy-preserving transparency the framework requires of the assessed organization.
- **Prompts**: sense of agency ("can you start things without permission?"); recognition ("is your work seen, including care/maintenance work?"); fairness ("are benefits distributed fairly relative to contribution?"); trust ("do peers keep commitments? what happens when they don't?"); meaning/belonging ("why do you stay?"); metric friction ("where do you feel reduced to a score or token?").
- **Record as**: anonymized quote or theme + dimension tag(s) + date + collection method.

| Theme / quote (anonymized) | Dimension tag(s) | Method | Date |
| ----- | ----- | ----- | ----- |
|  |  |  |  |

If narratives were not collected, mark 4.4 as `Not evidenced` (do not infer lived experience from documents).

---

## 8) Quick Checklist & TODOs
- Legal wrapper docs published?
- Governance portals indexed and linked?
- Repo licenses audited? Trademark/brand policy published? CLA terms checked for central IP assignment?
- Plural property-regime map filled (1.6)?
- Non-code contribution accounting documented?
- Identity/sybil and accountability linkages documented?
- Trust model characterized (protocol-based vs identity-based, 2.5)?
- Enterprise Stack positioning and business-model patterns recorded, including misfits (0.2–0.4)?
- Participant narratives collected, or 4.4 explicitly marked "not collected / not evidenced"?
- Dynamic profile captured instead of relying only on a total score?
- Path-dependency evidence found (founding choices, early allocations, admin rights, funding dependencies, governance defaults/sunset clauses)?
- Reputation/meritocracy capture risks assessed?
- Privacy-preserving transparency boundaries documented?
- Capital subordinated to commons governance, or capital influence still unclear?
- Contextual & ecological embeddedness evidenced (4.6)?
- Robustness scenarios answered (10x participation, 50% funding drop, founder exit, fork)?

---

## 9) Path Dependency & Capture Evidence

### 9.1 Founding Choices and Initial Conditions
- Findings:
  - Founders, initial rule-set, first repositories/assets, first legal entity, first governance defaults (use Wayback Machine for founding-era pages)
- Citations:
  -

### 9.2 Early Contributions, Reputation, and Authority
- Findings:
  - Whether early contributors gained persistent admin rights, social authority, reputation advantages, tokens, equity, or maintainership
- Citations:
  -

### 9.3 Funding, Capital, and Strategic Influence
- Findings:
  - Whether funders, investors, donors, sponsors, or treasury controllers can steer strategic priorities (control rights, veto rights, liquidity preferences, exit pressures)
- Citations:
  -

### 9.4 Infrastructure and Platform Lock-in
- Findings:
  - Dependencies on hosting, wallets, identity systems, repositories, legal wrappers, trademarks, data, or proprietary platforms
- Citations:
  -

### 9.5 Governance Defaults and Sunset Clauses
- Findings:
  - Emergency powers, owner/admin keys, committees, councils, maintainers: do they have sunset clauses, review processes, or renewal requirements? Have they ever been reviewed or revoked?
- Citations:
  -

---

## 10) Complexity Stress Tests

Anchor: `Evaluation.md`. For each major governance, economic, infrastructure, or enterprise-pattern choice, answer briefly.

### 10.1 Mechanism analysis

| Mechanism / Pattern | Feedback loop created | What becomes visible | What becomes hidden | Lock-in risk | Who gains adaptive capacity | Who loses agency | Evidence refs |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|  |  |  |  |  |  |  |  |

### 10.2 Robustness scenarios

Apply each scenario to the organization's key structures (governance process, treasury/funding, contribution accounting, infrastructure). Note what happens and whether the system adapts without reverting to hierarchy, enclosure, surveillance, or capital capture.

| Structure / mechanism | Participation grows 10x | Funding drops 50% | Founding/keystone actor exits | Conflict produces a fork |
| ----- | ----- | ----- | ----- | ----- |
| Governance process |  |  |  |  |
| Treasury / funding |  |  |  |  |
| Contribution accounting |  |  |  |  |
| Infrastructure / platforms |  |  |  |  |

---

## 11) Scenario / Simulation Inputs

### 11.1 Contribution Accounting Scenarios
- Inputs to collect:
  - Contribution categories, weights, formulas, review cycles, appeal mechanisms, invisible/care work treatment
- Evidence:
  -

### 11.2 Governance Scenarios
- Inputs to collect:
  - Quorum rules, delegation, owner/admin powers, emergency powers, fork procedures, founder exit paths
- Evidence:
  -

### 11.3 Benefit Redistribution Scenarios
- Inputs to collect:
  - Revenue shocks, surplus rules, payout schedules, dispute paths, treasury reserves
- Evidence:
  -

### 11.4 Reputation Scenarios
- Inputs to collect:
  - Reputation dimensions, decay/review, portability, sanctions, appeals, recovery after failure
- Evidence:
  -
