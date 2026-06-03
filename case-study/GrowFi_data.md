# GrowFi — Evidence Repository (for P2P-ness Assessment)

Purpose: Collect verifiable data and links about GrowFi, organized by the evaluation framework in `Evaluation.md` (layers x dimensions x levels). Each item includes a short note and source link(s).

## Variables (set these first)
- ORG_NAME: GrowFi
- PRIMARY_URLS: https://growfi.dev/ ; https://github.com/rifaisiciliadao/growfi ; https://x.com/RifaiSicilia
- FORUM_URL: https://x.com/RifaiSicilia
- MAIN_SITE: https://growfi.dev/
- GITHUB_ORG_URL: https://github.com/rifaisiciliadao/growfi
- DOCS_OR_MANUAL_URL: N/A (no dedicated handbook URL provided)
- BLOG_OR_NEWS_URL: N/A (no dedicated blog URL provided)
- SNAPSHOT_SPACE: N/A (not identified)
- TALLY_SPACE: N/A (not identified)

---

## Method: Web Search & Capture Protocol
- Primary sources reviewed: official website, repository landing page, repository root contents API, raw `README.md`, raw `LICENSE`.
- Forum/X source reviewed but content was not retrievable in this run.
- Evidence entries below use conservative interpretation when source coverage is incomplete.
- Complexity-upgrade evidence was assessed from the same public source set: founding conditions, owner/admin powers, privacy boundaries, capital influence, reputation capture, lock-in, and scenario inputs are marked incomplete where not publicly evidenced.

---

## Index of Primary Sources (live)
- Governance forum: https://x.com/RifaiSicilia
- Blog/News: N/A
- Organization GitHub: https://github.com/rifaisiciliadao/growfi
- Handbook / governance manual: N/A
- Main site: https://growfi.dev/
- Voting portals: Snapshot N/A, Tally N/A

---

## 1) Structural / Formal Layer

### 1.1 Membership & Entry/Exit
- Findings:
  - Website frames participation as open for both growers and investors ("Any grower launches a campaign, no permission").
  - Funding and participation are onchain and wallet-mediated, implying practical entry friction from crypto tooling.
  - No formal membership charter, onboarding policy, or explicit contributor rights policy was found.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 1.2 Role & Task Structure
- Findings:
  - Protocol roles are explicit in contracts and docs (`producer`, protocol owner/factory, investors, stakers, holders).
  - Smart-contract permissions are concretely role-gated.
  - Community organizational roles beyond protocol actors are not documented in available sources.
- Citations:
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md
  - https://github.com/rifaisiciliadao/growfi

### 1.3 Governance & Decision-Making
- Findings:
  - Public product logic states "No DAO votes, no committees — code is law" for campaign lifecycle behaviors.
  - Core protocol deployment/onboarding includes owner-gated flows (`CampaignFactory.createCampaign(...)`), indicating centralized protocol administration layer.
  - No public Snapshot/Tally governance space identified.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 1.4 Value Accounting & Rewards / Redistribution
- Findings:
  - Reward logic is specified: staking yields `$YIELD`; at harvest, holders can redeem product or USDC pro-rata.
  - Protocol fee is disclosed at 2% (activation and harvest).
  - No contributor reward/redistribution framework (for builders, maintainers, non-code work) is documented in reviewed sources.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 1.5 Legal / Liability / Financial Structures
- Findings:
  - Website references Rifai Sicilia DAO as host and describes it as a registered cultural association in Italy.
  - No full legal wrapper map (entity relationships, liabilities, signatory policies) found in reviewed sources.
  - README includes explicit non-guarantees and risk boundaries at protocol level, but not full legal governance details.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 1.6 Infrastructure & Commons
- Findings:
  - Code is presented as open-source and repository is public.
  - MIT license confirms permissive reuse posture.
  - Website claims deployed verified contracts on Base and a public subgraph.
- Citations:
  - https://growfi.dev/
  - https://github.com/rifaisiciliadao/growfi
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/LICENSE

---

## 2) Operational / Process Layer

### 2.1 Transparency & Access to Information
- Findings:
  - High protocol-level technical transparency through detailed README and security testing narratives.
  - Website discloses key mechanism rules (escrow, soft-cap refund, buyback windows, fees).
  - No periodic governance minutes, treasury reports, or budget disclosures found.
  - Privacy-preserving transparency boundaries are not documented; current transparency is mainly protocol/mechanism visibility rather than a stated policy for peer verification without personal exposure.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 2.2 Coordination of Tasks & Workflows
- Findings:
  - Repository exposes engineering workflow artifacts (issues/pulls available, structured project files, tests).
  - Deployment and contract documents suggest internal coordination maturity.
  - Public coordination processes for broader community participation are not evident yet.
- Citations:
  - https://github.com/rifaisiciliadao/growfi
  - https://api.github.com/repos/rifaisiciliadao/growfi/contents/

### 2.3 Contribution Logging & Attribution
- Findings:
  - GitHub provides standard code attribution through commits/PRs.
  - No evidence of formal non-code contribution accounting in reviewed materials.
  - No explicit "how contributors are recognized/rewarded" policy found.
- Citations:
  - https://github.com/rifaisiciliadao/growfi
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 2.4 Conflict Management & Forking
- Findings:
  - MIT license supports forking and redistribution rights at code level.
  - No explicit trademark policy found, so practical fork/brand boundaries remain unclear.
  - No documented conflict mediation process found in reviewed sources.
- Citations:
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/LICENSE
  - https://github.com/rifaisiciliadao/growfi

### 2.5 Reputation, Trust & Accountability
- Findings:
  - Trust model emphasizes verifiable onchain state transitions, escrow logic, and constrained admin privileges.
  - README documents internal audit approach and test coverage with clear caveat that external audit is pending.
  - No social reputation system or sybil-resistance governance mechanism identified for human coordination.
  - No reputation decay, review, appeal, role-rotation, or anti-incumbency safeguards found in the reviewed public sources.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

---

## 3) Economic Layer

### 3.1 Property Regime & Licensing (Commons/Nondominium vs Proprietary)
- Findings:
  - MIT licensed code indicates permissive commons-aligned software posture.
  - No restrictive CLA or proprietary dual-license evidence found in reviewed sources.
  - Trademark/brand policy visibility remains unresolved.
- Citations:
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/LICENSE
  - https://github.com/rifaisiciliadao/growfi

### 3.2 Contribution & Value Accounting / Benefit Distribution
- Findings:
  - Protocol describes explicit economic distribution to campaign participants (holders/stakers/redeemers).
  - Benefit split includes disclosed protocol fee and holder allocation mechanics.
  - Contributor-side value accounting for protocol builders is not documented.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 3.3 Funding & Capital Sources
- Findings:
  - Website presents campaign crowdfunding structure (USDC deposits into campaign contracts).
  - No evidence found of grants/VC/corporate financing structure for the protocol organization itself.
  - Early-stage metric display (0 campaigns / 0 raised on captured snapshot) limits empirical funding analysis.
  - Capital-governance influence at the organization level is not evidenced: no public investor, donor, sponsor, treasury-control, or strategic-veto documentation found.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 3.4 Revenue Model & Market Interface
- Findings:
  - Revenue is protocol-fee based (2%) with onchain market interactions around campaign purchase, staking, and redemption.
  - Protocol markets tokenized claims on real agricultural harvests (physical or USDC redemption path).
  - Market model is clear at protocol level but organization-level operating revenue/cost disclosures are absent.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 3.5 Tokenomics & Incentives (if applicable)
- Findings:
  - Incentive design includes campaign token, yield token, dynamic reward rates, penalties for early unstake, and queue-based sell-back.
  - Incentive parameters and state transitions are documented in detail.
  - No broad governance-token power-distribution model identified in reviewed sources.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 3.6 Cost Structure & Sustainability
- Findings:
  - Protocol sustainability mechanism appears to rely on fee extraction and repeated campaign cycles.
  - No public operating budget, runway, or cost breakdown found.
  - No explicit eco-cost accounting framework found beyond regenerative mission narrative.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 3.7 Economic Openness & Cost Transparency
- Findings:
  - Fee rules and payout logic are transparent at product/protocol level.
  - Cost-side transparency (team costs, infra spend, allocation criteria) not evidenced.
  - Treasury openness remains unclear with current public materials.
  - The public materials do not distinguish aggregate economic transparency from contributor/user privacy concerns.
- Citations:
  - https://growfi.dev/
  - https://github.com/rifaisiciliadao/growfi

---

## 4) Cultural / Ecosystem / Superstructural Layer

### 4.1 Values, Norms & Culture
- Findings:
  - Mission language strongly emphasizes regeneration, transparency, and verification.
  - Cultural narrative aligns around "real harvests", anti-discretion escrow mechanics, and public verifiability.
  - No explicit community code of conduct or social norm handbook found.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 4.2 Learning, Adaptation & Innovation
- Findings:
  - Extensive internal testing and audit iteration indicates active engineering learning loops.
  - Multi-chain fork testing suggests adaptability to deployment contexts.
  - Governance/process retrospectives beyond code hardening were not identified.
- Citations:
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md
  - https://github.com/rifaisiciliadao/growfi

### 4.3 Meaning, Purpose & Identity
- Findings:
  - Identity is coherent: regenerative finance for agricultural production with commodity-agnostic framing.
  - Strong purpose integration between website narrative and protocol mechanics.
  - Limited evidence of broad contributor/community identity structures at this stage.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 4.4 Phenomenological Grounding (Lived Experience)
- Findings:
  - Website narrative is user-centered around growers launching campaigns and holders redeeming harvest-linked value.
  - No participant interviews, contributor surveys, onboarding retrospectives, exit narratives, or lived-experience evidence found in reviewed materials.
  - Alignment between formal protocol rules and participant experience remains unverified beyond public product claims.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 4.5 Ecosystem Relations & External Engagement
- Findings:
  - Named ecosystem partners include Rifai Sicilia and Silvi (dMRV).
  - Website references Chainlink oracle dependency and Base deployment context.
  - Evidence of broader inter-network governance alliances is limited in reviewed set.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

---

## 5) Product/Protocol Notes (Context for Commons Orientation)

### 5.1 Core Protocols/Products
- Findings:
  - Core protocol stack includes campaign factory, token sale/escrow, staking vault, yield token, and harvest manager.
  - Security posture is explicitly documented with adversarial tests, fuzzing, and invariants.
  - External audit is pending.
- Citations:
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md
  - https://github.com/rifaisiciliadao/growfi

### 5.2 Additional Tooling/Stacks
- Findings:
  - Foundry-based smart-contract toolchain indicated (`forge`, `foundry.toml`, tests, scripts).
  - Repository structure suggests dedicated docs/deploy artifacts.
  - No separate app/backend architecture docs were reviewed in this assessment pass.
- Citations:
  - https://api.github.com/repos/rifaisiciliadao/growfi/contents/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

---

## 6) Level-specific Observations (to be expanded)

### Project level
- Strong technical transparency and clear protocol-level rule encoding.
- Participation/access framing is open for users/growers.

### Open-Enterprise level
- Centralized protocol owner/factory gate some high-impact operations.
- Legal and financial wrapper details are partially visible only.

### Network level
- Emerging partner and infrastructure dependencies (Base, Chainlink, Silvi, Rifai Sicilia).
- No robust evidence yet of distributed multi-org governance.

### Global / inter-network level
- Commodity-agnostic and chain-agnostic ambitions are stated.
- Practical inter-network standards participation not yet evidenced in collected sources.

---

## 7) Quick Checklist & TODOs
- Legal wrapper docs published? -> PARTIAL (Rifai Sicilia mention only). TODO: identify entity docs and signatory model.
- Snapshot/Tally index linked? -> NO. TODO: confirm whether governance is intentionally off-voting-portal.
- Repo licenses audited? Trademark/brand policy published? -> LICENSE YES (MIT), trademark policy NOT FOUND.
- Non-code contribution accounting documented? -> NOT FOUND.
- Identity/sybil and accountability linkages documented? -> NOT FOUND for social governance; protocol trust logic documented.
- Dynamic profile captured instead of relying only on a total score? -> UPDATED in compilation.
- Path-dependency evidence found? -> PARTIAL: owner/factory powers and host association visible; founding history, early allocations, and admin succession not documented.
- Reputation/meritocracy capture risks assessed? -> PARTIAL: no human reputation system found; protocol owner/admin concentration remains a governance capture question.
- Privacy-preserving transparency boundaries documented? -> NOT FOUND.
- Capital subordinated to commons governance? -> NOT EVIDENCED at organization level; campaign mechanics are transparent, capital influence over protocol governance is unclear.

---

## 8) Path Dependency & Capture Evidence

### 8.1 Founding Choices and Initial Conditions
- Findings:
  - GrowFi is publicly associated with Rifai Sicilia DAO / Rifai Sicilia as host.
  - Reviewed sources do not document founding governance, initial contributors, initial treasury, or initial rule-making process.
  - Campaign creation includes owner/factory-gated flows, creating a visible initial-control question for future governance.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 8.2 Early Contributions, Reputation, and Authority
- Findings:
  - Code contribution history is available through GitHub, but a full contributor-authority map was not captured in this assessment pass.
  - No public non-code contribution accounting, maintainer rotation, reputation decay, or role-review process found.
  - Early technical contributors or owners may hold practical authority if admin keys, maintainership, deployment knowledge, or roadmap control remain concentrated.
- Citations:
  - https://github.com/rifaisiciliadao/growfi
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 8.3 Funding, Capital, and Strategic Influence
- Findings:
  - Campaign-level capital flows are transparent in product logic: USDC deposits, soft-cap refund paths, protocol fees, harvest redemption.
  - Organization-level funding, treasury, investor/donor influence, sponsorship rights, and strategic vetoes were not evidenced.
  - This means capital capture cannot be confirmed, but also cannot be ruled out from reviewed public materials.
- Citations:
  - https://growfi.dev/
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md

### 8.4 Infrastructure and Platform Lock-in
- Findings:
  - Current infrastructure dependencies include Base deployment context, Chainlink oracle dependency, public GitHub hosting, and dMRV partner dependency via Silvi.
  - MIT licensing reduces code-level lock-in, but trademark/brand, deployment/admin, oracle, subgraph, and host-association dependencies remain unclear.
  - No documented migration or fork-governance process found.
- Citations:
  - https://growfi.dev/
  - https://github.com/rifaisiciliadao/growfi
  - https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/LICENSE

---

## 9) Complexity Stress Tests

| Mechanism / Pattern | Feedback loop created | What becomes visible | What becomes hidden | Lock-in risk | Who gains adaptive capacity | Who loses agency | Evidence refs |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Permissionless campaign launching | More growers can launch campaigns, increasing market/protocol activity and social proof | Campaign terms, escrow state, funding status | Quality control, grower support burden, offchain verification capacity | If factory/admin onboarding remains gated, permissionlessness may be partial | Growers and investors gain direct access | Participants may depend on protocol/admin/oracle choices | https://growfi.dev/ ; https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md |
| Owner/factory-gated campaign creation | Admin control can protect protocol quality but can also centralize access | Authorized campaign setup path | Criteria for approval, admin succession, appeal paths | Persistent owner role may become governance chokepoint | Protocol stewards gain risk-control capacity | Growers/users lose agency if criteria are opaque | https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md |
| Protocol fee model | More campaign volume funds protocol sustainability | Fee percentage and redemption logic | Operating costs, treasury allocation, maintainer compensation | Fee governance can centralize if not peer-governed | Protocol maintainers gain sustainability path | Contributors/users may lack voice over fee use | https://growfi.dev/ ; https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md |
| Tokenized harvest claims and staking | Participation can deepen through yield/redeem loops | Holder/staker logic, penalties, redemption paths | User comprehension, offchain delivery risks, lived fairness | Incentive mechanics may privilege sophisticated crypto users | Investors/holders gain programmable access | Less technical growers/users may face tooling barriers | https://growfi.dev/ ; https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/README.md |
| MIT-licensed public code | Forkability and review improve technical commons | Code, license, reuse rights | Brand/trademark rights, deployment keys, operational know-how | Brand/admin/oracle dependencies may limit practical forkability | Developers and peer reviewers gain reuse capacity | Non-technical contributors remain less visible | https://github.com/rifaisiciliadao/growfi ; https://raw.githubusercontent.com/rifaisiciliadao/growfi/main/LICENSE |

---

## 10) Scenario / Simulation Inputs

### 10.1 Contribution Accounting Scenarios
- Inputs to collect:
  - Code, protocol design, grower onboarding, dMRV work, community support, legal/admin, and care/coordination contribution categories.
  - Whether any future reward formula values non-code work and allows peer review or appeals.
- Evidence:
  - No contributor-side value equation found in reviewed materials.

### 10.2 Governance Scenarios
- Inputs to collect:
  - Owner/factory powers, transfer/sunset rules, campaign approval criteria, emergency powers, fork procedure, host-association accountability.
  - Founder/owner exit scenario and multi-steward governance transition path.
- Evidence:
  - Owner/factory powers appear in README; no full governance charter found.

### 10.3 Benefit Redistribution Scenarios
- Inputs to collect:
  - Effects of failed campaigns, delayed harvests, low liquidity, high redemption demand, revenue shock, and fee allocation disputes.
  - Rules for protocol fee use, treasury reserves, and community/grant redistribution.
- Evidence:
  - Campaign-level fee, refund, staking, and redemption mechanics are documented; organization-level fee allocation is not.

### 10.4 Reputation Scenarios
- Inputs to collect:
  - Grower reliability history, campaign performance, dispute outcomes, contributor reputation, recovery after failure, reputation portability.
  - Whether reputation is contextual and appealable rather than a permanent hierarchy.
- Evidence:
  - No social reputation or contributor reputation system found in reviewed materials.
