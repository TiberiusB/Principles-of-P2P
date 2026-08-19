# Prompt — ChangePool (FamilyDAO) P2P-ness Assessment

*Instructions for the user: set the AI to Agent mode, ensure you have enabled and authenticated all necessary MCP servers (Context7, GitHub, Sourcegraph), and include OVNwiki (https://ovn.world/index.php?title=Main_Page) and P2P Foundation (https://wiki.p2pfoundation.net/index.php/Main_Page) sources.*

System/Instructional prompt for AI agents to run a repeatable assessment of ChangePool using `templates/template_data.md`, `templates/template_compilation.md`, `templates/template_executive_summary.md`, and `templates/template_scores.yaml`, grounded in `Model.md`, `Evaluation.md`, `Hybrid.md`, `Ethos.md`, `new-collaborative-entrepreneurship.md`, and `Distributed business model patterns - Models.csv`. Deterministic scoring, radar, scaffolding, and validation are offloaded to `tools/` (see `tools/README.md`).

## Context

- Objective: Assess the degree of P2P-ness of ChangePool with a multi-level, multi-dimensional model.
- Foundations: Use the five foundation documents as the theoretical/methodological basis.
- Outputs: Filled `ChangePool_data.md`, `ChangePool_scores.yaml`, `ChangePool_compilation.md`, and `ChangePool_executive_summary.md` (radar via `tools/compute_scores.py --radar`).
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

## Tooling & Execution Harness (Strict Enforcement)

To execute this assessment thoroughly, the agent MUST utilize the following tools dynamically:

1. **Context7 MCP**: Invoke the `context7` MCP server whenever encountering technical infrastructure, libraries, SDKs, or APIs.
2. **WebSearch & Browser Automation**: Invoke built-in WebSearch or the `cursor-ide-browser` MCP for live verification (OVN Wiki, P2P Foundation, org properties).
3. **GitHub & Sourcegraph MCPs**: Deep repo inspection; optionally `tools/github_footprint.py ChangePool/FamilyDAO --markdown` for LICENSE/contributor stubs.
4. **Assessment tooling (`tools/`, see `tools/README.md`)** — **required**:
   - `init_assessment.py` — scaffold when starting fresh.
   - `ChangePool_scores.yaml` + `compute_scores.py` — **source of truth for numbers**; patch Score Summary; `--radar`. Do **not** hand-average.
   - `patterns.py` — pattern CSV shortlists for §0.3 / pattern risk table.
   - `validate_assessment.py` — must pass before hand-off.

*Agent Directive*: Do not ask for permission to use these tools if available. Run `tools/*.py` via Shell (prefer `.venv/bin/python` after `pip install -r tools/requirements.txt`).

## High-level steps

1. Read foundations (Model, Evaluation, Hybrid, Ethos, NCE, patterns CSV).
2. Use existing `case-study/ChangePool_*` files (or `init_assessment.py`). Fill `_data.md` Section 0+; use `patterns.py` / `github_footprint.py` as needed.
3. Populate findings with Status + Confidence + citations; property-regime map; path dependency; stress-test inputs.
4. Narratives module or mark 4.4 `Not evidenced`.
5. Fill `case-study/ChangePool_scores.yaml` cells; rationales in compilation tables; then:

```bash
.venv/bin/python tools/compute_scores.py case-study/ChangePool_scores.yaml \
  --write-summary case-study/ChangePool_compilation.md \
  --radar --png-only-fail
```

6. Principles coverage; Hybrid X-ray; Enterprise Stack & patterns; stress tests; Ethos.
7. Executive summary from template (embed radar; Economic Model & Migration Path).
8. `tools/validate_assessment.py ChangePool` must exit 0.

## Evidence & search protocol (strict)

- Use your **browser tool** (e.g., `browser_navigate`, `browser_click`, `browser_snapshot`) or WebSearch tool to perform live searches and verify information when needed, particularly against the OVN Wiki (https://ovn.world/) and P2P Foundation Wiki (https://wiki.p2pfoundation.net/).
- Use the **GitHub MCP** (`user-github`) and **Sourcegraph MCP** to deeply inspect source code, pull requests, and organizational repositories directly. Use **Context7 MCP** to clarify any technical dependencies.
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

Create / maintain in `case-study/`:

- `ChangePool_data.md`, `ChangePool_scores.yaml` (**numeric source of truth**), `ChangePool_compilation.md`, `ChangePool_executive_summary.md`
- `assets/ChangePool_layer_radar.png` (+ `.svg`) via `compute_scores.py --radar`

### Scores YAML + averages + radar (required)

```bash
python3 -m venv .venv
.venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/compute_scores.py case-study/ChangePool_scores.yaml \
  --write-summary case-study/ChangePool_compilation.md \
  --radar --png-only-fail
```

Embed under `## Layer averages (radar)`:

```markdown
![Radar chart of ChangePool layer averages](./assets/ChangePool_layer_radar.png)
```

Do **not** use Mermaid. Cursor tip: use **Open Preview to the Side** to see the PNG. Docs: `tools/README.md`.

### Economic Model & Migration Path (required section in the executive summary)

Synthesize from the compilation's Enterprise Stack & pattern analysis, path-dependency table, and stress tests:

1. **Current economic model(s)/patterns** — assess the business-model patterns the organization actually runs today (from the pattern risk table): OVN fit, capture/lock-in/mission-drift risks, and whether capital remains subordinate to commons governance.
2. **Ideal model/pattern suggestion** — recommend target pattern(s) from the pattern library in `new-collaborative-entrepreneurship.md` and its semantically richer source `Distributed business model patterns - Models.csv` (including its OVN additions), justified by the organization's layer profile, ethos assessment, mission, and ecosystem position. Treat the pattern library as a heuristic map, not a recipe; state why the suggested pattern fits this organization's context.
3. **Migration path** — a staged path from the current model to the suggested one: quick wins first (project-level pilots, per `Evaluation.md`'s improvement pathways), then structural changes. Name the path dependencies and lock-ins the migration must navigate (from the path-dependency table), the robustness scenarios the transition must survive (funding −50%, founder/keystone exit, contentious fork), and the adaptation rules that keep openness, transparency, and fair benefit redistribution intact throughout.

## Quality checks

- Status tags + citations; `NE` never averaged as 0.
- Averages from `compute_scores.py` over `ChangePool_scores.yaml`; conclusion matches.
- Principles, Hybrid X-ray, stack/patterns, path-dependency, stress tests, ethos complete.
- Narratives collected or 4.4 `Not evidenced`.
- Executive summary has Migration Path + radar image.
- **`tools/validate_assessment.py ChangePool` exits 0** before hand-off.

## Hand-off

- Short key findings, 2–5 recommendations (quick wins vs structural), links to all created files (including `_scores.yaml` and radar PNG).
