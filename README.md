# Principles of P2P

A **multi-dimensional P2P-ness assessment framework** for organizations, networks, and projects — with foundation theory, reusable templates, deterministic scoring tools, and worked case studies.

The main output is a **dynamic P2P profile** (tensions, path dependencies, capture risks, trajectory). Layer averages and an optional overall index are secondary signals only. A single score must never replace the profile.

## What’s in this repo


| Path                         | Role                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- |
| `[Foundation/](Foundation/)` | Theory & method: Model, Evaluation, Hybrid, Ethos, Enterprise Stack, pattern library, plus Truth / Value / data-sourcing |
| `[templates/](templates/)`   | Blank assessment artifacts + orchestration prompt                                                  |
| `[tools/](tools/)`           | Scaffolding, score averages, radar charts, validation, GitHub/pattern helpers                      |
| `[case-study/](case-study/)` | Completed assessments (e.g. ChangePool / FamilyDAO, Holons)                                        |
| `[assets/](assets/)`         | Framework improvement notes and related assets                                                     |




## Foundations (read these)

1. `[Foundation/Model.md](Foundation/Model.md)` — P2P economy aspects and **8 fundamental principles**
2. `[Foundation/Evaluation.md](Foundation/Evaluation.md)` — layers × dimensions × levels, scoring conventions (`0–5` / `NE` / `N/A`)
3. `[Foundation/Hybrid.md](Foundation/Hybrid.md)` — two-axis hybridization X-ray (P2P vs traditional fidelity)
4. `[Foundation/Ethos.md](Foundation/Ethos.md)` — 14 ethos dimensions
5. `[Foundation/Enterprise-Stack-collaborative-entrepreneurship.md](Foundation/Enterprise-Stack-collaborative-entrepreneurship.md)` — Enterprise Stack (heuristic map). Formerly cited as `new-collaborative-entrepreneurship.md`.
6. `[Foundation/Distributed business model patterns - Models.csv](Foundation/Distributed%20business%20model%20patterns%20-%20Models.csv)` — pattern library
7. `[Foundation/Others/Truth.md](Foundation/Others/Truth.md)` — how organizations assess truth; computational models (required qualitative section)
8. `[Foundation/Others/Value.md](Foundation/Others/Value.md)` — how organizations define and redistribute value (required qualitative section)
9. `[Foundation/Others/Web-and-Social-Data-Sourcing.md](Foundation/Others/Web-and-Social-Data-Sourcing.md)` — assessor ethics and large-scale sourcing



## Quick start — run an assessment



### 1. Environment

```bash
python3 -m venv .venv
.venv/bin/pip install -r tools/requirements.txt
```



### 2. Scaffold a case study

```bash
.venv/bin/python tools/init_assessment.py \
  --org AcmeDAO \
  --title "Acme DAO" \
  --assessor YourName \
  --date 2026-08-11 \
  --scope project \
  --main-site https://example.org \
  --github https://github.com/acme/dao \
  --register assessment
```

`--register` is `assessment` (default, terse executive summary) or `collaborative` (Holons-style invitation report). Agents also select `collaborative` when the organization is Open Value Network (OVN)–adjacent.

This creates under `case-study/`:

- `AcmeDAO_data.md` — evidence repository
- `AcmeDAO_scores.yaml` — **numeric source of truth** (0–5 / `NE` / `N/A`)
- `AcmeDAO_compilation.md` — profile, rationales, hybrid, ethos, …
- `AcmeDAO_executive_summary.md` — short profile + radar + migration path
- `assets/` — radar images land here



### 3. Assess (judgment)

1. Fill evidence in `_data.md` (Status + Confidence + citations on every finding).
2. Optionally: `tools/github_footprint.py owner/repo --markdown` and `tools/patterns.py search "…"`.
3. Enter scores in `_scores.yaml`; write dimension **rationales** in `_compilation.md` tables.
4. Author Dynamic Profile, principles narrative, Hybrid X-ray, Ethos, **Truth assessment**, **Value theory**, stress tests, executive summary.

Use an agent with `[templates/template_prompt.md](templates/template_prompt.md)` (copy/adapt variables), or a filled prompt such as `[family_dao.md](family_dao.md)`. Recommended MCP context: GitHub, Context7, browser; also OVN Wiki and P2P Foundation.

### 4. Compute averages + radar (mechanical)

```bash
.venv/bin/python tools/compute_scores.py case-study/AcmeDAO_scores.yaml \
  --write-summary case-study/AcmeDAO_compilation.md \
  --radar --png-only-fail
```

Do **not** hand-average layer/level scores when the YAML exists. Do **not** use Mermaid for the radar chart.

### 5. Validate before hand-off

```bash
.venv/bin/python tools/validate_assessment.py AcmeDAO
```

Full tool reference: `[tools/README.md](tools/README.md)`.

## Scoring conventions


| Cell    | Meaning                                                        |
| ------- | -------------------------------------------------------------- |
| `0`–`5` | Rubric score (`0` = absent / contrary to P2P; `5` = exemplary) |
| `NE`    | Not evidenced — **excluded** from averages (not a zero)        |
| `N/A`   | Level out of scope — **excluded** from averages                |


Interpretation rule: **profile before score.** See `Foundation/Evaluation.md`.

## Templates


| Template                                                                             | Becomes                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------ |
| `[templates/template_prompt.md](templates/template_prompt.md)`                       | Org-specific agent prompt (e.g. `family_dao.md`) |
| `[templates/template_data.md](templates/template_data.md)`                           | `case-study/{ORG}_data.md`                       |
| `[templates/template_scores.yaml](templates/template_scores.yaml)`                   | `case-study/{ORG}_scores.yaml`                   |
| `[templates/template_compilation.md](templates/template_compilation.md)`             | `case-study/{ORG}_compilation.md`                |
| `[templates/template_executive_summary.md](templates/template_executive_summary.md)` | `case-study/{ORG}_executive_summary.md`          |




## Example case study

**ChangePool (FamilyDAO)** — proposal-stage Cardano-adjacent project:

- Evidence: `[case-study/ChangePool_data.md](case-study/ChangePool_data.md)`
- Scores: `[case-study/ChangePool_scores.yaml](case-study/ChangePool_scores.yaml)`
- Compilation: `[case-study/ChangePool_compilation.md](case-study/ChangePool_compilation.md)`
- Executive summary: `[case-study/ChangePool_executive_summary.md](case-study/ChangePool_executive_summary.md)`
- Radar: `[case-study/assets/ChangePool_layer_radar.png](case-study/assets/ChangePool_layer_radar.png)`
- Prompt used: `[family_dao.md](family_dao.md)`



## Cursor notes

- Prefer **Markdown: Open Preview to the Side** (`Ctrl+K` then `V`) to view local radar PNGs — the in-tab Preview toggle often fails to render images (known Cursor limitation).
- Assessment tooling is designed so the agent does judgment and narrative; scripts own averages, radar, scaffolding, and validation.



## License / contribution

This repository is a living methodology. Improve foundations carefully (see `[assets/improvements.md](assets/improvements.md)`); add case studies under `case-study/` without overwriting the current example unless intentional.