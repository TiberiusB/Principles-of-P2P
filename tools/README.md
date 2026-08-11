# Assessment tools — offload deterministic work from the AI agent

Pipeline (judgment stays with the assessor/agent; math and scaffolding are mechanical):

```text
init_assessment → fill _data.md + _scores.yaml → compute_scores (--radar)
                 → write narratives in compilation / executive summary
                 → validate_assessment
```

Install once:

```bash
python3 -m venv .venv
.venv/bin/pip install -r tools/requirements.txt
```

Prefer `.venv/bin/python tools/...` so radar PNG generation works.

---

## Tools

| Script | Role |
| ----- | ----- |
| `init_assessment.py` | Scaffold `case-study/{ORG}_*.md` + `_scores.yaml` + `assets/` from templates |
| `compute_scores.py` | Averages from `_scores.yaml` (excludes `NE`/`N/A`); patch Score Summary; call radar |
| `radar_chart.py` | Layer-average radar PNG/SVG (do **not** use Mermaid) |
| `validate_assessment.py` | Quality gates before hand-off |
| `github_footprint.py` | Public GitHub LICENSE / contributors / bus-factor stub for data §§1.6–2.x / 9 |
| `patterns.py` | Search `Foundation/Distributed business model patterns - Models.csv` |
| `scorelib.py` | Shared YAML load + averaging (imported by compute/validate) |

---

## 1. `init_assessment.py`

```bash
.venv/bin/python tools/init_assessment.py \
  --org AcmeDAO \
  --title "Acme DAO" \
  --assessor Tibi \
  --date 2026-08-11 \
  --scope project \
  --main-site https://example.org \
  --github https://github.com/acme/dao
```

Creates (unless present; `--force` overwrites):

- `case-study/AcmeDAO_data.md`
- `case-study/AcmeDAO_compilation.md`
- `case-study/AcmeDAO_executive_summary.md`
- `case-study/AcmeDAO_scores.yaml`
- `case-study/assets/`

---

## 2. Score sheet + `compute_scores.py`

**Source of truth for numbers:** `case-study/{ORG}_scores.yaml` (from `templates/template_scores.yaml`).

Cell values: `0`–`5`, `NE`, or `N/A`. Never encode “not evidenced” as `0`.

```bash
.venv/bin/python tools/compute_scores.py case-study/ChangePool_scores.yaml \
  --write-summary case-study/ChangePool_compilation.md \
  --radar \
  --png-only-fail \
  --print-json
```

This:

1. Prints the Score Summary block (layer / level / overall + basis counts)
2. Patches `## Score Summary (secondary signals)` in the compilation
3. Runs `radar_chart.py` into `case-study/assets/{ORG}_layer_radar.{png,svg}`

Rationales, Dynamic Profile, Hybrid X-ray, Ethos, and Migration Path remain authored in markdown.

---

## 3. `radar_chart.py`

Used by `compute_scores.py --radar`, or standalone:

```bash
.venv/bin/python tools/radar_chart.py \
  --org ChangePool \
  --title "ChangePool FamilyDAO" \
  --structural 0.3 --operational 1.2 --economic 1.0 --cultural 3.0 \
  --overall 1.4 \
  --out case-study/assets/ \
  --png-only-fail
```

**Do not use Mermaid** for this chart. Cursor’s Markdown Mermaid build does not reliably render radar/quadrant diagrams.

Embed under `## Layer averages (radar)` in the executive summary:

```markdown
![Radar chart of ChangePool layer averages](./assets/ChangePool_layer_radar.png)
```

**Cursor preview tip:** the in-tab Preview toggle often fails to show local images (known Cursor bug). Use **Markdown: Open Preview to the Side** (`Ctrl+K` then `V`) instead. No plugin required.

---

## 4. `validate_assessment.py`

```bash
.venv/bin/python tools/validate_assessment.py ChangePool
.venv/bin/python tools/validate_assessment.py ChangePool --strict
```

Checks: required deliverable files/sections, scores YAML computable (no null cells), radar asset present and linked from executive summary, Economic Model & Migration Path section, rough consistency between YAML averages and compilation Score Summary. Exit `1` on errors (`--strict` also fails on warnings).

---

## 5. Evidence helpers

```bash
# GitHub commons footprint stub (paste into _data.md; add Status/Confidence)
.venv/bin/python tools/github_footprint.py ChangePool/FamilyDAO --markdown

# Pattern library shortlist for §0.3 / pattern risk table
.venv/bin/python tools/patterns.py search "open source|crowdfunding|revenue share"
.venv/bin/python tools/patterns.py show "Open Source"
```

Prefer the GitHub MCP when authenticated; `github_footprint.py` is the deterministic unauthenticated fallback.

---

## Agent loop (canonical)

1. `init_assessment` (or reuse existing case-study files)
2. Gather evidence into `_data.md` (optionally `github_footprint` / `patterns`)
3. Fill **scores only** in `_scores.yaml` + rationales in `_compilation.md` tables
4. `compute_scores … --write-summary … --radar`
5. Author Dynamic Profile, principles narrative, Hybrid, Ethos, executive summary + Migration Path
6. Embed radar PNG; `validate_assessment` must pass before hand-off
