# Template Prompt — P2P-ness Assessment Orchestration

//Instructions for the user: set AI in Agent mode, add Browser and Web tools, and include OVNwiki and P2Pfoundation sources.

System/Instructional prompt for AI agents to run a repeatable assessment of GrowFi using `template_data.md` and `template_compilation.md`, grounded in `Model.md`, `Evaluation.md`, `Hybrid.md`, and `Ethos.md`.

## Context
- Objective: Assess the degree of P2P-ness of GrowFi with a multi-level, multi-dimensional model.
- Foundations: Use the four documents as the theoretical/methodological basis.
- Outputs: Filled `template_data.md` (evidence), `template_compilation.md` (dynamic profile, scores, stress tests, conclusion), optional executive summary.
- Interpretation rule: report a dynamic P2P profile first. Any overall score is a secondary index, not the main finding.

## Variables to set
- ORG_NAME: GrowFi
- MAIN_SITE: https://growfi.dev/
- FORUM_URL: https://x.com/RifaiSicilia
- DOCS_OR_MANUAL_URL: N/A
- BLOG_OR_NEWS_URL: N/A
- GITHUB_ORG_URL: https://github.com/rifaisiciliadao/growfi
- SNAPSHOT_SPACE: N/A
- TALLY_SPACE: N/A

## High-level steps
1) Read foundations: `Model.md`, `Evaluation.md`, `Hybrid.md`, `Ethos.md`.
2) Clone `template_data.md`; set variables; run the Web Search & Capture Protocol; populate findings/citations per dimension.
3) Clone `template_compilation.md`; fill per-dimension scores (0–5) at each level (including the Economic layer); compute layer averages and optional overall index.
4) Fill the dynamic profile, path-dependency analysis, complexity stress tests, scenario/simulation recommendations, Hybridization X-ray, and Ethos Assessment tables with concise rationales and citations.
5) Draft a profile-first conclusion and (optional) generate an executive summary slide. If desired, include a radar chart of layer averages.

## Evidence & search protocol (strict)
- Search parallel across the org’s primary properties (forum/docs/blog/site/GitHub), plus Snapshot/Tally.
- Prefer primary sources; include 1–3 citations for each finding; no uncited claims.
- Capture governance process (stages, timing), voting mechanisms, legal wrappers, repos/licenses, trademark policy, non-code attribution, identity/sybil controls, ecosystem partnerships.
- Capture Economic-layer evidence: property/licensing & trademark posture; contribution/value accounting & distributions; funding sources; revenue model & market interface; tokenomics (if any); cost structure & sustainability; economic openness & cost transparency (budgets, cost breakdowns, allocation criteria).
- Capture path-dependency evidence: founding choices, early allocations, persistent admin powers, early contributor authority, funding dependencies, and infrastructure lock-in.
- Capture reputation/meritocracy risks: incumbent advantage, role concentration, delegation concentration, decay/review/appeal mechanisms.
- Capture privacy-preserving transparency: what is public, what is private, and how peer verification avoids surveillance or exposure of sensitive personal data.
- Capture capital-governance evidence: whether capital providers, sponsors, donors, or token/equity holders can steer strategy outside commons governance.
- For every major mechanism or enterprise pattern, answer the complexity stress-test questions: feedback loop, visibility, hiddenness, lock-in, adaptive-capacity gain, agency loss.

## Scoring guidance (grounded in Principles from `Evaluation.md`)
- Structural/Formal: Membership openness; roles & task fluidity; governance distribution; value accounting; legal wrapper; commons infrastructure.
- Operational/Process: Transparency; coordination; contribution logging; conflict/forking; reputation & accountability.
- Economic: Property/licensing & commons orientation; contribution & value accounting; funding & capital sources; revenue model & market interface; tokenomics & incentives (if applicable); cost structure & sustainability; economic openness & cost transparency.
- Cultural/Ecosystem: Values & norms; learning/adaptation; mission/identity; phenomenological grounding; ecosystem relations.
- Use 0–5. When uncertain due to missing evidence, prefer conservative (lower) scores and add a TODO in data template.
- Do not collapse contradictions into an average. Explain tensions between openness/quality, transparency/privacy, meritocracy/capture, capital/commons governance, and formal decentralization/lived agency.

## Hybrid & Ethos mapping
- Use `Hybrid.md` X-ray dimensions to record centralized vs P2P features and explain scores.
- Use `Ethos.md` to rate ethos dimensions; align with evidence from forums, repos, and docs.
- Add explicit notes for privacy-preserving transparency, capital subordination to commons governance, and reputation/meritocracy capture risk.

## Deliverables
Create the following docs from template within the "case-study" folder
- `GrowFi_data.md` (from template): fully populated.
- `GrowFi_compilation.md` (from template): dynamic profile, scores, averages, path-dependency analysis, stress tests, scenario recommendations, X-ray, ethos, conclusion.
- `GrowFi_executive_summary.md` with top-line score,
- radar chart/profile, strengths/risks/recommendations.

## Quality checks
- Every assertion has a citation.
- Averages computed correctly; conclusion matches table values and does not overstate the optional overall index.
- TODOs for missing items (legal/trademark, Snapshot index, non-code attribution, etc.).
- Path-dependency, privacy, capital-governance, reputation-capture, and scenario sections are filled or explicitly marked "not evidenced".

## Hand-off
- Provide a short summary of key findings, a list of priority recommendations (2–5 items), and links to all created files.
