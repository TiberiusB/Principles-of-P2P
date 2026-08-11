# Prompt — ChangePool (FamilyDAO) P2P-ness Assessment

*Instructions for the user: set the AI to Agent mode, enable Browser and Web tools, and include OVNwiki (https://ovn.world/index.php?title=Main_Page) and P2P Foundation (https://wiki.p2pfoundation.net/index.php/Main_Page) sources.*

System/Instructional prompt for AI agents to run a repeatable assessment of ChangePool using `templates/template_data.md` and `templates/template_compilation.md`, grounded in `Model.md`, `Evaluation.md`, `Hybrid.md`, `Ethos.md`, `new-collaborative-entrepreneurship.md`, and `Distributed business model patterns - Models.csv`.

## Context

- Objective: Assess the degree of P2P-ness of ChangePool with a multi-level, multi-dimensional model.
- Foundations: Use the five foundation documents as the theoretical/methodological basis.
- Outputs: Filled `ChangePool_data.md` (status-tagged evidence), `ChangePool_compilation.md` (dynamic profile, scores, principles coverage, two-axis hybrid X-ray, Enterprise Stack & pattern analysis, stress tests, conclusion), optional executive summary.
- Interpretation rule: report a dynamic P2P profile first. Any overall score is a secondary index, not the main finding.

## Variables to set

- ORG_NAME: ChangePool
- ASSESSOR: {{Tibi}}
- ASSESSMENT_DATE: {{2026-08-11}}
- SCOPE_LEVELS: {{PROJECT}}
- PRIMARY_URLS: {{PRIMARY_URLS}}
- MAIN_SITE: [https://coincashew.io/Content/Home.html](https://coincashew.io/Content/Home.html)
- FORUM_URL: {{FORUM_URL}}
- DOCS_OR_MANUAL_URL: {{DOCS_OR_MANUAL_URL}}
- BLOG_OR_NEWS_URL: {{BLOG_OR_NEWS_URL}}
- GITHUB_ORG_URL: [https://github.com/ChangePool/FamilyDAO](https://github.com/ChangePool/FamilyDAO)
- GOVERNANCE_PORTALS: {{GOVERNANCE_PORTALS — e.g., Snapshot, Tally, Boardroom, DeepDAO, Discourse}}
- SNAPSHOT_SPACE: {{SNAPSHOT_SPACE_OR_URL — optional}}
- TALLY_SPACE: {{TALLY_SPACE_OR_URL — optional}}
- REGISTRY_URL: {{REGISTRY_URL — optional; e.g., OpenCorporates entry}}
- WAYBACK_URLS: {{WAYBACK_URLS — optional; founding-era snapshots}}
- SECONDARY_RESOURCES: see Resources section below.

## High-level steps

1. Read foundations: `Model.md`, `Evaluation.md`, `Hybrid.md`, `Ethos.md`, `new-collaborative-entrepreneurship.md`, and `Distributed business model patterns - Models.csv`.
2. Clone `templates/template_data.md` as `case-study/ChangePool_data.md`; set variables (including SCOPE_LEVELS); run the Web Search & Capture Protocol; fill Section 0 (organizational snapshot, Enterprise Stack positioning, business-model patterns, map misfits).
3. Populate findings per dimension with Status (`Evidenced` / `Partially evidenced` / `Not evidenced` / `Contradicted`) + Confidence + citations. Fill the plural property-regime map (1.6), path-dependency evidence (incl. 9.5 governance defaults/sunset clauses), and the stress-test inputs.
4. Where permitted, run the Participant Narratives Module (data Sec. 7): interviews or anonymous survey on agency, recognition, fairness, trust, belonging, care work. If not collected, mark 4.4 `Not evidenced` — never infer lived experience from documents.
5. Clone `templates/template_compilation.md` as `case-study/ChangePool_compilation.md`; fill per-dimension scores (0–5, or `NE`/`N/A`) at each in-scope level, including the Economic layer and Contextual & Ecological Embeddedness; compute layer averages **and** level averages (excluding NE/N/A, noting the basis).
6. Complete the Fundamental Principles Coverage cross-check (8 principles from `Model.md`); explain any strong-average/weak-principle discrepancy.
7. Complete the two-axis Hybridization X-ray (P2P fidelity + Traditional fidelity per dimension), the hybridization-model match, and red flags.
8. Complete the Enterprise Stack & pattern analysis: pattern risk table (OVN fit, P2P risks, adaptation rule, capital governance test) and the orchestrator-drift check.
9. Complete the complexity stress tests **and** the robustness scenario results (participation ×10, funding −50%, founder/keystone exit, contentious fork), then the scenario/simulation recommendations.
10. Complete the Ethos Assessment with traditional-baseline contrasts.
11. Draft a profile-first conclusion (quick wins vs structural changes; reduction-risk check) and (optional) generate the executive summary — with a radar chart of layer averages and the required Economic Model & Migration Path section described under Deliverables.

## Evidence & search protocol (strict)

- Use your **browser tool** (e.g., `browser_navigate`, `browser_click`, `browser_snapshot`) or Search MCP to perform live searches and verify information when needed, particularly against the OVN Wiki (https://ovn.world/) and P2P Foundation Wiki (https://wiki.p2pfoundation.net/).
- Search in parallel across the org's primary properties (site/GitHub above; discover forum/docs/blog if they exist) plus its governance portals.
- Prefer primary sources; include 1–3 citations for each finding (up to 10 for complex claims); no uncited claims. For volatile pages (roadmaps, governance rules, token allocations), capture a Wayback Machine snapshot as well.
- Beyond the org's own properties, check: legal registries (OpenCorporates or national equivalents), trademark registries (USPTO/EUIPO), Wayback Machine founding-era pages, GitHub contributor insights (top committers/mergers, email domains), and governance aggregators (DeepDAO, Boardroom) where applicable.
- Capture governance process (stages, timing), voting mechanisms, legal wrappers, repos/licenses, trademark policy, non-code attribution, identity/sybil controls, ecosystem partnerships.
- Capture Economic-layer evidence: property/licensing & trademark posture; contribution/value accounting & distributions; funding sources and attached control rights; revenue model & market interface (incl. disintermediation evidence); tokenomics (if any); cost structure & sustainability (incl. ecological costs); economic openness & cost transparency.
- Capture path-dependency evidence: founding choices, early allocations, persistent admin powers, early contributor authority, funding dependencies, infrastructure lock-in, and governance defaults with/without sunset clauses.
- Capture reputation/meritocracy risks: incumbent advantage, role concentration, delegation concentration, decay/review/appeal mechanisms.
- Capture privacy-preserving transparency: what is public, what is private, and how peer verification avoids surveillance or exposure of sensitive personal data. Note: a family-oriented system handles especially sensitive personal data — treat privacy boundaries as a first-class dimension of the assessment.
- Capture capital-governance evidence: whether capital providers, sponsors, donors, or token/equity holders can steer strategy outside commons governance.
- For every major mechanism or enterprise pattern, answer the complexity stress-test questions: feedback loop, visibility, hiddenness, lock-in, adaptive-capacity gain, agency loss — plus the four robustness scenarios.
- Assessor ethics: respect robots.txt and site terms; collect only public, organization-level content; avoid personal data beyond what the org itself publishes for accountability; obtain informed consent and anonymize all participant narratives. For large-scale tooling options, see `Others/Web-and-Social-Data-Sourcing.md`.

## Resources (SECONDARY_RESOURCES)

- **OVN Wiki**: [https://ovn.world/index.php?title=Main_Page](https://ovn.world/index.php?title=Main_Page) (Source for Open Value Network models, economic structures, and contribution accounting)
- **P2P Foundation Wiki**: [https://wiki.p2pfoundation.net/index.php/Main_Page](https://wiki.p2pfoundation.net/index.php/Main_Page) (Source for peer-to-peer history, culture, commons-based peer production)
- Ancestry. (2026). Retrieved August 2, 2026, from [https://www.ancestry.com/](https://www.ancestry.com/)

Bowen Center for the Study of the Family. (1975). Retrieved July 7, 2026, from [https://www.thebowencenter.org/](https://www.thebowencenter.org/)

Chainlink. (2026). What Is a 51% Attack? Retrieved July 7, 2026, from [https://chain.link/article/what-is-a-51-attack](https://chain.link/article/what-is-a-51-attack)

Comforting Loss, Celebrating Life. (2026). Retrieved July 26, 2026, from [https://www.bcfunerals.com/](https://www.bcfunerals.com/)

Lent, J. (2026). *Ecocivilization: Making a World That Works For All*. Brooklyn: Melville House.

Memorygram. (2026). On a Mission To Preserve Precious Memories and Legacy. Retrieved August 10, 2026, from [https://memoirs.memorygram.com/](https://memoirs.memorygram.com/)

Multicultural Family Institute. (2023). Standard Symbols for Genograms. Retrieved July 7, 2026, from [https://multiculturalfamily.org/product/genogram-how-to-downloadable-pdf/](https://multiculturalfamily.org/product/genogram-how-to-downloadable-pdf/)

NOĒMA. (2026). We May Be Entering A Second Axial Age. Retrieved July 9, 2026, from [https://www.noemamag.com/we-may-be-entering-a-second-axial-age/](https://www.noemamag.com/we-may-be-entering-a-second-axial-age/)

Remento. A Keepsake Book That Lets You Hear Their Voice Forever. Retrieved August 10, 2026, from [https://www.remento.co/](https://www.remento.co/)

Royal Bank of Canada Wealth Management. (2026). When Should I Consider a Family Office? Retrieved July 7, 2026, from [https://www.rbcwealthmanagement.com/en-ca/insights/when-should-i-consider-a-family-office](https://www.rbcwealthmanagement.com/en-ca/insights/when-should-i-consider-a-family-office)

Storyworth. (2026). Help Them See Their Life in a Whole New Light. Retrieved August 10, 2026, from [https://welcome.storyworth.com/](https://welcome.storyworth.com/)

## Scoring guidance (grounded in `Evaluation.md`)

- Structural/Formal: Membership openness; roles & task fluidity; governance distribution; value accounting; legal wrapper; commons infrastructure (incl. plural property regimes).
- Operational/Process: Transparency (privacy-preserving); coordination & stigmergy; contribution logging; conflict/forking; reputation, trust & accountability.
- Economic: Property/licensing & commons orientation; contribution & value accounting; funding & capital sources (capital-vs-resources posture); revenue model & market interface (disintermediation); tokenomics & incentives (if applicable); cost structure & sustainability; economic openness & cost transparency.
- Cultural/Ecosystem: Values & norms; learning/adaptation (incl. reflexivity); mission/identity; phenomenological grounding; ecosystem relations; contextual & ecological embeddedness.
- Use 0–5. Distinguish `NE` (not evidenced — excluded from averages, becomes a TODO) from `0` (evidence of absence) and from `N/A` (level out of scope). When evidence is thin but real, prefer conservative (lower) scores and add a TODO in the data repository.
- Compute layer averages and level averages, always excluding NE/N/A and stating how many cells were scored.
- Do not collapse contradictions into an average. Explain tensions between openness/quality, transparency/privacy, meritocracy/capture, capital/commons governance, and formal decentralization/lived agency.
- Cross-check scores against the 8 fundamental principles from `Model.md`; a high layer average that masks a weak principle must be surfaced, not averaged away.

## Hybrid & Ethos mapping

- Use `Hybrid.md`'s X-ray with **two-axis scoring**: P2P fidelity (0–5) and Traditional fidelity (0–5) per dimension, with evidence notes; interpret per Hybrid.md (both high = hybrid; Traditional ≫ P2P = captured/legacy).
- Match the organization against `Hybrid.md`'s hybridization-model catalog (foundation+subsidiary, open-core, DAO+wrapper, federated-with-corporate-hubs, formal-decentralization/experiential-alienation, etc.) and surface red flags.
- Use `Ethos.md` to rate the 14 ethos dimensions; contrast each with the traditional-org baseline; align with evidence from forums, repos, docs, and participant narratives.
- Add explicit notes for privacy-preserving transparency, capital subordination to commons governance, and reputation/meritocracy capture risk.

## Enterprise Stack & pattern analysis

- Treat the Enterprise Stack as a heuristic map, not an ontology. Record the organization's active stack layers and business-model patterns, and explicitly record where the map does **not** fit.
- For each pattern present, fill the pattern risk table: OVN fit; P2P risks (capture, lock-in, mission drift, governance complexity); adaptation rule; capital governance test.
- Run the orchestrator-drift check: does any orchestration role become a privileged coordinating center?

## Deliverables

Create the following docs from template within the "case-study" folder:

- `ChangePool_data.md` (from `templates/template_data.md`): fully populated, with status/confidence tags and citations.
- `ChangePool_compilation.md` (from `templates/template_compilation.md`): dynamic profile, layer and level scores, fundamental principles coverage, two-axis hybrid X-ray, Enterprise Stack & pattern analysis, path-dependency analysis, stress tests + robustness scenarios, scenario recommendations, ethos assessment, conclusion.
- `ChangePool_executive_summary.md`: top-line profile, layer/level averages and optional secondary overall index, radar chart/profile, strengths/risks/recommendations, and the Economic Model & Migration Path section specified below.

### Economic Model & Migration Path (required section in the executive summary)

Synthesize from the compilation's Enterprise Stack & pattern analysis, path-dependency table, and stress tests:

1. **Current economic model(s)/patterns** — assess the business-model patterns the organization actually runs today (from the pattern risk table): OVN fit, capture/lock-in/mission-drift risks, and whether capital remains subordinate to commons governance.
2. **Ideal model/pattern suggestion** — recommend target pattern(s) from the pattern library in `new-collaborative-entrepreneurship.md` and its semantically richer source `Distributed business model patterns - Models.csv` (including its OVN additions), justified by the organization's layer profile, ethos assessment, mission, and ecosystem position. Treat the pattern library as a heuristic map, not a recipe; state why the suggested pattern fits this organization's context.
3. **Migration path** — a staged path from the current model to the suggested one: quick wins first (project-level pilots, per `Evaluation.md`'s improvement pathways), then structural changes. Name the path dependencies and lock-ins the migration must navigate (from the path-dependency table), the robustness scenarios the transition must survive (funding −50%, founder/keystone exit, contentious fork), and the adaptation rules that keep openness, transparency, and fair benefit redistribution intact throughout.

## Quality checks

- Every assertion has a citation and a status tag; `NE` cells are never averaged as 0.
- Layer **and** level averages computed correctly (excluding NE/N/A, basis stated); conclusion matches table values and does not overstate the optional overall index.
- TODOs for missing items (legal/trademark, governance-portal index, non-code attribution, etc.).
- Fundamental Principles Coverage table complete; strong-average/weak-principle discrepancies explained.
- Two-axis hybrid X-ray filled (both axes per dimension); hybridization model(s) identified; red flags answered explicitly (yes/no + evidence).
- Enterprise Stack positioning, pattern risk table, misfit notes, and orchestrator-drift check completed.
- Path-dependency (incl. governance defaults/sunset clauses), privacy, capital-governance, reputation-capture, and scenario sections filled or explicitly marked "not evidenced".
- Robustness scenarios (10x participation, 50% funding drop, founder exit, fork) answered for governance, treasury, contribution accounting, and infrastructure.
- Participant narratives collected with consent/anonymity, or 4.4 explicitly marked "not evidenced".
- If an executive summary is produced, it contains the Economic Model & Migration Path section: current patterns assessed, ideal pattern(s) suggested and justified, and a staged migration path referencing path dependencies, robustness scenarios, and adaptation rules.

## Hand-off

- Provide a short summary of key findings, a list of priority recommendations (2–5 items, split into quick wins vs structural changes), and links to all created files.
