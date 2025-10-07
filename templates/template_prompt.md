# Template Prompt — P2P-ness Assessment Orchestration

System/Instructional prompt for AI agents to run a repeatable assessment of {{ORG_NAME}} using `template_data.md` and `template_compilation.md`, grounded in `Assessment model.md`, `Principles of p2p.md`, `Hybrid models.md`, and `Ethos.md`.

## Context
- Objective: Assess the degree of P2P-ness of {{ORG_NAME}} with a multi-level, multi-dimensional model.
- Foundations: Use the four documents as the theoretical/methodological basis.
- Outputs: Filled `template_data.md` (evidence), `template_compilation.md` (scores & conclusion), optional executive summary.

## Variables to set
- ORG_NAME: {{ORG_NAME}}
- MAIN_SITE: {{MAIN_SITE}}
- FORUM_URL: {{FORUM_URL}}
- DOCS_OR_MANUAL_URL: {{DOCS_OR_MANUAL_URL}}
- BLOG_OR_NEWS_URL: {{BLOG_OR_NEWS_URL}}
- GITHUB_ORG_URL: {{GITHUB_ORG_URL}}
- SNAPSHOT_SPACE: {{SNAPSHOT_SPACE_OR_URL}}
- TALLY_SPACE: {{TALLY_SPACE_OR_URL}}

## High-level steps
1) Read foundations: `Assessment model.md`, `Principles of p2p.md`, `Hybrid models.md`, `Ethos.md`.
2) Clone `template_data.md`; set variables; run the Web Search & Capture Protocol; populate findings/citations per dimension.
3) Clone `template_compilation.md`; fill per-dimension scores (0–5) at each level (including the Economic layer); compute layer and overall averages.
4) Fill Hybridization X-ray and Ethos Assessment tables with concise rationales and citations.
5) Draft a 3–6 sentence conclusion and (optional) generate an executive summary slide. If desired, include a radar chart of layer averages.

## Evidence & search protocol (strict)
- Search parallel across the org’s primary properties (forum/docs/blog/site/GitHub), plus Snapshot/Tally.
- Prefer primary sources; include 1–3 citations for each finding; no uncited claims.
- Capture governance process (stages, timing), voting mechanisms, legal wrappers, repos/licenses, trademark policy, non-code attribution, identity/sybil controls, ecosystem partnerships.
- Capture Economic-layer evidence: property/licensing & trademark posture; contribution/value accounting & distributions; funding sources; revenue model & market interface; tokenomics (if any); cost structure & sustainability; economic openness & cost transparency (budgets, cost breakdowns, allocation criteria).

## Scoring guidance (grounded in Principles)
- Structural/Formal: Membership openness; roles & task fluidity; governance distribution; value accounting; legal wrapper; commons infrastructure.
- Operational/Process: Transparency; coordination; contribution logging; conflict/forking; reputation & accountability.
- Economic: Property/licensing & commons orientation; contribution & value accounting; funding & capital sources; revenue model & market interface; tokenomics & incentives (if applicable); cost structure & sustainability; economic openness & cost transparency.
- Cultural/Ecosystem: Values & norms; learning/adaptation; mission/identity; ecosystem relations.
- Use 0–5. When uncertain due to missing evidence, prefer conservative (lower) scores and add a TODO in data template.

## Hybrid & Ethos mapping
- Use `Hybrid models.md` X-ray dimensions to record centralized vs P2P features and explain scores.
- Use `Ethos.md` to rate ethos dimensions; align with evidence from forums, repos, and docs.

## Deliverables
- `{{ORG_NAME}}_data.md` (from template): fully populated.
- `{{ORG_NAME}}_compilation.md` (from template): scores, averages, X-ray, ethos, conclusion.
- Optional: `{{ORG_NAME}}_executive_summary.md` with top-line score, radar chart link, strengths/risks/recommendations.

## Quality checks
- Every assertion has a citation.
- Averages computed correctly; conclusion matches table values.
- TODOs for missing items (legal/trademark, Snapshot index, non-code attribution, etc.).

## Hand-off
- Provide a short summary of key findings, a list of priority recommendations (2–5 items), and links to all created files.
