# Template Prompt — P2P-ness Assessment Orchestration

*Instructions for the user: set the AI to Agent mode, ensure you have enabled and authenticated all necessary MCP servers (Context7, GitHub, Sourcegraph), and include OVNwiki ([https://ovn.world/index.php?title=Main_Page](https://ovn.world/index.php?title=Main_Page)) and P2P Foundation ([https://wiki.p2pfoundation.net/index.php/Main_Page](https://wiki.p2pfoundation.net/index.php/Main_Page)) sources.*

System/Instructional prompt for AI agents to run a repeatable assessment of {{ORG_NAME}} using `templates/template_data.md`, `templates/template_compilation.md`, `templates/template_executive_summary.md`, and `templates/template_scores.yaml`, grounded in `Model.md`, `Evaluation.md`, `Hybrid.md`, `Ethos.md`, `new-collaborative-entrepreneurship.md`, and `Distributed business model patterns - Models.csv`. Deterministic scoring, radar, scaffolding, and validation are offloaded to `tools/` (see `tools/README.md`).

## Context

- Objective: Assess the degree of P2P-ness of {{ORG_NAME}} with a multi-level, multi-dimensional model.
- Foundations: Use the five foundation documents as the theoretical/methodological basis.
- Outputs: Filled `{{ORG_NAME}}_data.md` (status-tagged evidence), `{{ORG_NAME}}_scores.yaml` (machine-readable scores), `{{ORG_NAME}}_compilation.md` (dynamic profile, rationales, principles, hybrid X-ray, stack, stress tests, ethos), and `{{ORG_NAME}}_executive_summary.md` (including radar chart from `tools/compute_scores.py --radar`).
- Interpretation rule: report a dynamic P2P profile first. Any overall score is a secondary index, not the main finding.



## Variables to set

- ORG_NAME: {{ORG_NAME}}
- ASSESSOR: {{ASSESSOR_NAME_OR_HANDLE}}
- ASSESSMENT_DATE: {{YYYY-MM-DD}}
- SCOPE_LEVELS: {{PROJECT / OPEN-ENTERPRISE / NETWORK / GLOBAL — mark which apply}}
- PRIMARY_URLS: {{PRIMARY_URLS}}
- MAIN_SITE: {{MAIN_SITE_URL}}
- FORUM_URL: {{FORUM_URL}}
- DOCS_OR_MANUAL_URL: {{DOCS_OR_MANUAL_URL}}
- BLOG_OR_NEWS_URL: {{BLOG_OR_NEWS_URL}}
- GITHUB_ORG_URL: {{GITHUB_ORG_URL}}
- GOVERNANCE_PORTALS: {{GOVERNANCE_PORTALS — e.g., Snapshot, Tally, Boardroom, DeepDAO, Discourse}}
- SNAPSHOT_SPACE: {{SNAPSHOT_SPACE_OR_URL — optional}}
- TALLY_SPACE: {{TALLY_SPACE_OR_URL — optional}}
- REGISTRY_URL: {{REGISTRY_URL — optional; e.g., OpenCorporates entry}}
- WAYBACK_URLS: {{WAYBACK_URLS — optional; founding-era snapshots}}
- SECONDARY_RESOURCES: {{SECONDARY_RESOURCES — optional bibliography/URLs specific to this assessment}}



## Tooling & Execution Harness (Strict Enforcement)

To execute this assessment thoroughly, the agent MUST utilize the following tools dynamically:

1. **Context7 MCP**: Invoke the `context7` MCP server whenever encountering technical infrastructure, libraries, SDKs, or APIs to fetch up-to-date documentation and ensure architectural conclusions are not based on stale training data.
2. **WebSearch & Browser Automation**: Invoke built-in WebSearch or the `cursor-ide-browser` MCP to perform live searches, visually verify information, interact with complex governance portals (e.g., Snapshot, Tally), and scrape public wiki data (OVN Wiki, P2P Foundation).
3. **GitHub & Sourcegraph MCPs**: Invoke the `user-github` or `plugin-sourcegraph-cursor-plugin-sourcegraph` MCP servers to dive deep into repository structures, analyze commit history, read smart contracts, and assess the technical implementation of governance/economic models. Optionally supplement with `tools/github_footprint.py` for a deterministic LICENSE/contributor stub.
4. **Assessment tooling (`tools/`, see `tools/README.md`)** — **required** for scaffolding, averages, radar, and hand-off validation:
   - `init_assessment.py` — scaffold case-study files from templates (do not hand-clone when this can run).
   - `{{ORG_NAME}}_scores.yaml` + `compute_scores.py` — **source of truth for numeric scores**; compute layer/level/overall averages excluding `NE`/`N/A`; patch compilation Score Summary; generate radar (`--radar`). **Do not hand-average** when the score sheet is available.
   - `radar_chart.py` — called via `compute_scores.py --radar`; do **not** use Mermaid for the radar.
   - `patterns.py` — search the business-model pattern CSV for §0.3 / pattern risk table shortlists.
   - `validate_assessment.py` — must pass before hand-off.

*Agent Directive*: Do not ask for permission to use these tools if they are available in your catalog. Proactively invoke `GetMcpTools` to discover the schema, then `CallMcpTool` to execute. If a tool fails due to missing authentication, explicitly inform the user to check their MCP configuration. Run `tools/*.py` via the Shell tool (prefer `.venv/bin/python` after `pip install -r tools/requirements.txt`).

## High-level steps

1. Read foundations: `Model.md`, `Evaluation.md`, `Hybrid.md`, `Ethos.md`, `new-collaborative-entrepreneurship.md`, and `Distributed business model patterns - Models.csv`.
2. Scaffold with `tools/init_assessment.py` (or reuse existing case-study files). Set variables (including SCOPE_LEVELS). Run the Web Search & Capture Protocol; fill Section 0 in `_data.md` (snapshot, Enterprise Stack, patterns via `tools/patterns.py` as needed, map misfits). Optionally run `tools/github_footprint.py owner/repo --markdown` into §§1.6/2.x/9.
3. Populate findings per dimension with Status (`Evidenced` / `Partially evidenced` / `Not evidenced` / `Contradicted`) + Confidence + citations. Fill the plural property-regime map (1.6), path-dependency evidence (incl. 9.5), and stress-test inputs.
4. Where permitted, run the Participant Narratives Module (data Sec. 7). If not collected, mark 4.4 `Not evidenced` — never infer lived experience from documents.
5. Fill **numeric cells** in `case-study/{{ORG_NAME}}_scores.yaml` (0–5 / `NE` / `N/A`). Fill per-dimension **rationales** in `{{ORG_NAME}}_compilation.md` tables. Then run:

```bash
.venv/bin/python tools/compute_scores.py case-study/{{ORG_NAME}}_scores.yaml \
  --write-summary case-study/{{ORG_NAME}}_compilation.md \
  --radar --png-only-fail
```

Do **not** hand-compute layer/level/overall averages.
6. Complete the Fundamental Principles Coverage cross-check (8 principles from `Model.md`); explain any strong-average/weak-principle discrepancy.
7. Complete the two-axis Hybridization X-ray, hybridization-model match, and red flags.
8. Complete the Enterprise Stack & pattern analysis (pattern risk table + orchestrator-drift check).
9. Complete complexity stress tests, robustness scenarios, and scenario/simulation recommendations.
10. Complete the Ethos Assessment with traditional-baseline contrasts.
11. Draft a profile-first conclusion; generate/fill `{{ORG_NAME}}_executive_summary.md` from `templates/template_executive_summary.md` (embed radar PNG; Economic Model & Migration Path required).
12. Run `tools/validate_assessment.py {{ORG_NAME}}` and fix any errors before hand-off.



## Evidence & search protocol (strict)

- Use your **browser tool** (e.g., `browser_navigate`, `browser_click`, `browser_snapshot`) or WebSearch tool to perform live searches and verify information when needed, particularly against the OVN Wiki ([https://ovn.world/](https://ovn.world/)) and P2P Foundation Wiki ([https://wiki.p2pfoundation.net/](https://wiki.p2pfoundation.net/)).
- Use the **GitHub MCP** (`user-github`) and **Sourcegraph MCP** to deeply inspect source code, pull requests, and organizational repositories directly. Use **Context7 MCP** to clarify any technical dependencies.
- Search in parallel across the org's primary properties (site/forum/docs/blog/GitHub) plus its governance portals.
- Prefer primary sources; include 1–3 citations for each finding (up to 10 for complex claims); no uncited claims. For volatile pages (roadmaps, governance rules, token allocations), capture a Wayback Machine snapshot as well.
- Beyond the org's own properties, check: legal registries (OpenCorporates or national equivalents), trademark registries (USPTO/EUIPO), Wayback Machine founding-era pages, GitHub contributor insights (top committers/mergers, email domains), and governance aggregators (DeepDAO, Boardroom) where applicable.
- Capture governance process (stages, timing), voting mechanisms, legal wrappers, repos/licenses, trademark policy, non-code attribution, identity/sybil controls, ecosystem partnerships.
- Capture Economic-layer evidence: property/licensing & trademark posture; contribution/value accounting & distributions; funding sources and attached control rights; revenue model & market interface (incl. disintermediation evidence); tokenomics (if any); cost structure & sustainability (incl. ecological costs); economic openness & cost transparency.
- Capture path-dependency evidence: founding choices, early allocations, persistent admin powers, early contributor authority, funding dependencies, infrastructure lock-in, and governance defaults with/without sunset clauses.
- Capture reputation/meritocracy risks: incumbent advantage, role concentration, delegation concentration, decay/review/appeal mechanisms.
- Capture privacy-preserving transparency: what is public, what is private, and how peer verification avoids surveillance or exposure of sensitive personal data.
- Capture capital-governance evidence: whether capital providers, sponsors, donors, or token/equity holders can steer strategy outside commons governance.
- For every major mechanism or enterprise pattern, answer the complexity stress-test questions: feedback loop, visibility, hiddenness, lock-in, adaptive-capacity gain, agency loss — plus the four robustness scenarios.
- Assessor ethics: respect robots.txt and site terms; collect only public, organization-level content; avoid personal data beyond what the org itself publishes for accountability; obtain informed consent and anonymize all participant narratives. For large-scale tooling options, see `Others/Web-and-Social-Data-Sourcing.md`.



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

Create the following docs from template within the "case-study" folder (prefer `tools/init_assessment.py`):

- `{{ORG_NAME}}_data.md` (from `templates/template_data.md`): fully populated, with status/confidence tags and citations.
- `{{ORG_NAME}}_scores.yaml` (from `templates/template_scores.yaml`): **source of truth** for 0–5 / NE / N/A cells.
- `{{ORG_NAME}}_compilation.md` (from `templates/template_compilation.md`): dynamic profile, dimension rationales, Score Summary **written by `compute_scores.py`**, principles, hybrid X-ray, stack, path-dependency, stress tests, ethos, conclusion.
- `{{ORG_NAME}}_executive_summary.md` (from `templates/template_executive_summary.md`): top-line profile, layer averages + **radar**, strengths/risks/recommendations, Economic Model & Migration Path.
- `case-study/assets/{{ORG_NAME}}_layer_radar.png` (+ `.svg`): from `compute_scores.py --radar`.



### Scores YAML + averages + radar (required)

**Numbers live in** `case-study/{{ORG_NAME}}_scores.yaml`. After filling cells, run:

```bash
python3 -m venv .venv
.venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/compute_scores.py case-study/{{ORG_NAME}}_scores.yaml \
  --write-summary case-study/{{ORG_NAME}}_compilation.md \
  --radar --png-only-fail
```

**Radar location:** `{{ORG_NAME}}_executive_summary.md` → `## Layer averages (radar)`, immediately under the numeric table. Embed:

```markdown
![Radar chart of {{ORG_NAME}} layer averages](./assets/{{ORG_NAME}}_layer_radar.png)
```

**Do not use Mermaid** for the radar. Keep the numeric table (and optional ASCII bars) above the image. Full docs: `tools/README.md`.

**Cursor preview tip:** in-tab Preview often fails to show local images (known Cursor bug). Use **Markdown: Open Preview to the Side** (`Ctrl+K` then `V`).



### Economic Model & Migration Path (required section in the executive summary)

Synthesize from the compilation's Enterprise Stack & pattern analysis, path-dependency table, and stress tests:

1. **Current economic model(s)/patterns** — assess the business-model patterns the organization actually runs today (from the pattern risk table): OVN fit, capture/lock-in/mission-drift risks, and whether capital remains subordinate to commons governance.
2. **Ideal model/pattern suggestion** — recommend target pattern(s) from the pattern library in `new-collaborative-entrepreneurship.md` and its semantically richer source `Distributed business model patterns - Models.csv` (including its OVN additions), justified by the organization's layer profile, ethos assessment, mission, and ecosystem position. Treat the pattern library as a heuristic map, not a recipe; state why the suggested pattern fits this organization's context.
3. **Migration path** — a staged path from the current model to the suggested one: quick wins first (project-level pilots, per `Evaluation.md`'s improvement pathways), then structural changes. Name the path dependencies and lock-ins the migration must navigate (from the path-dependency table), the robustness scenarios the transition must survive (funding −50%, founder/keystone exit, contentious fork), and the adaptation rules that keep openness, transparency, and fair benefit redistribution intact throughout.



## Quality checks

- Every assertion has a citation and a status tag; `NE` cells are never averaged as 0.
- Layer **and** level averages come from `tools/compute_scores.py` over `{{ORG_NAME}}_scores.yaml` (excluding NE/N/A, basis stated); conclusion matches those values and does not overstate the optional overall index.
- TODOs for missing items (legal/trademark, governance-portal index, non-code attribution, etc.).
- Fundamental Principles Coverage table complete; strong-average/weak-principle discrepancies explained.
- Two-axis hybrid X-ray filled (both axes per dimension); hybridization model(s) identified; red flags answered explicitly (yes/no + evidence).
- Enterprise Stack positioning, pattern risk table, misfit notes, and orchestrator-drift check completed.
- Path-dependency (incl. governance defaults/sunset clauses), privacy, capital-governance, reputation-capture, and scenario sections filled or explicitly marked "not evidenced".
- Robustness scenarios (10x participation, 50% funding drop, founder exit, fork) answered for governance, treasury, contribution accounting, and infrastructure.
- Participant narratives collected with consent/anonymity, or 4.4 explicitly marked "not evidenced".
- Executive summary contains Economic Model & Migration Path and a **radar chart image** at `## Layer averages (radar)` (Mermaid not accepted).
- **`tools/validate_assessment.py {{ORG_NAME}}` exits 0** before hand-off.



## Hand-off

- Provide a short summary of key findings, a list of priority recommendations (2–5 items, split into quick wins vs structural changes), and links to all created files (including `_scores.yaml` and the radar PNG).

