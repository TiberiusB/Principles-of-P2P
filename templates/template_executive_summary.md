# {{ORG_NAME}} — Executive Summary

**Assessor:** {{ASSESSOR_NAME_OR_HANDLE}}  
**Date:** {{YYYY-MM-DD}}  
**Scope:** {{SCOPE_LEVELS}}  
**Register:** {{assessment | collaborative}}  
**Evidence:** [`{{ORG_NAME}}_data.md`](./{{ORG_NAME}}_data.md) · **Compilation:** [`{{ORG_NAME}}_compilation.md`](./{{ORG_NAME}}_compilation.md)

{{collaborative only: short opening letter — a map and an invitation, not a verdict. Spell acronyms on first use.}}

---

## Top-line profile

{{2–4 sentences: dynamic P2P profile first — strongest/weakest layers, decisive tension or design choice, trajectory. Do not lead with the overall index.}}

| Signal | Value |
| ----- | ----- |
| Overall index (secondary) | **{{X.X}} / 5** |
| Strongest layer | {{layer}} — **{{score}}** |
| Weakest layer | {{layer}} — **{{score}}** |
| Decisive tension / design choice | {{one line}} |
| Trajectory | {{toward more P2P / stable hybrid / capture risk / insufficient evidence}} |

---

## Layer averages (radar)

Numeric table first (must match `{{ORG_NAME}}_compilation.md` Score Summary):

| Layer | Score (0–5; NE = not evidenced) | Basis |
| ----- | ----- | ----- |
| Structural / Formal |  |  |
| Operational / Process |  |  |
| Economic |  |  |
| Cultural / Ecosystem |  |  |

{{collaborative: a paragraph that walks the table — peak, floor, what the spread means. assessment: one line is enough.}}

Optional ASCII bar strip (preview-safe, no tooling):

```
P2P-ness profile (0–5)

Cultural     ...
Operational  ...
Economic     ...
Structural   ...
             0    1    2    3    4    5
```

### Radar chart (required — produce with `tools/compute_scores.py --radar`)

**Do not use Mermaid.** Numbers come from `case-study/{{ORG_NAME}}_scores.yaml`. After filling scores:

```bash
python3 -m venv .venv
.venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/compute_scores.py case-study/{{ORG_NAME}}_scores.yaml \
  --write-summary case-study/{{ORG_NAME}}_compilation.md \
  --radar --png-only-fail
```

Embed the PNG **here** (under the table):

![Radar chart of {{ORG_NAME}} layer averages](./assets/{{ORG_NAME}}_layer_radar.png)

*Radar of the four layer averages (0–5). Note peak and floor; overall index is secondary only.*

Cursor tip: in-tab Preview often fails on local images — use **Markdown: Open Preview to the Side**. See `tools/README.md`.

---

## Fundamental principles (cross-check)

| Principle | Score (0–5; NE = not evidenced) |
| ----- | ----- |
| 1. Commons Orientation |  |
| 2. Open Participation |  |
| 3. Peer Governance |  |
| 4. Recognition & Distribution of Benefits |  |
| 5. Generativity & Adaptivity |  |
| 6. Contextual Embeddedness |  |
| 7. Reflexivity & Transparency |  |
| 8. Phenomenological Grounding |  |

{{collaborative: a paragraph on which principles are strong, which are floors, and any strong-average / weak-principle discrepancy. assessment: optional one line.}}

---

## Strengths

{{assessment: numbered one-liners. collaborative: short paragraphs — tensions you can work with.}}

1.
2.
3.

## Risks

{{assessment: numbered one-liners. collaborative: short paragraphs.}}

1.
2.
3.

## Priority recommendations

In `collaborative` register, write invitations (“you might consider,” “a pattern that has worked for us”), not command verbs. Keep 2–5 items total.

### Near-term conversations

{{assessment alias: Quick wins}}

1.
2.

### Structural patterns to consider

{{assessment alias: Structural changes}}

1.
2.

---

## Economic Model & Migration Path

### 1. Current economic model(s) / patterns

| Pattern in use | OVN fit | Capture / lock-in / mission-drift risk | Capital subordinate to commons? |
| ----- | ----- | ----- | ----- |
|  |  |  |  |

{{collaborative: a paragraph that walks the table in plain language.}}

### 2. Ideal model / pattern suggestion

{{Target pattern(s) from `Foundation/Enterprise-Stack-collaborative-entrepreneurship.md` and `Foundation/Distributed business model patterns - Models.csv` + why they fit this org's layer profile, ethos, mission, and ecosystem position. Treat the library as a heuristic map, not a recipe.}}

### 3. Migration path

| Stage | Actions | Path dependencies to navigate | Robustness tests the stage must survive | Adaptation rules to keep intact |
| ----- | ----- | ----- | ----- | ----- |
| 0 → 1 (near-term / quick wins) |  |  |  |  |
| 1 → 2 (structural) |  |  |  |  |
| 2 → 3 (scale / capital) |  |  |  |  |

{{collaborative: a paragraph that explains the stages as invitations.}}

---

## Hybridization snapshot

{{2–4 sentences from the two-axis X-ray + model match + red flags.}}

{{collaborative: expand into a short paragraph on what the hybrid actually is (copyfair two-path, foundation+subsidiary, open-core, etc.).}}

## Ethos snapshot

{{Short ethos average / standouts / floors. Scores are 0–5; NE = not evidenced.}}

{{collaborative: name the high and the floor in one paragraph.}}

---

## Glossary

{{Optional in `assessment`. Required in `collaborative`: expand every acronym used in this summary on first use, and list them here — e.g. Open Value Network (OVN); GNU Affero General Public License (AGPL); Contributor License Agreement (CLA); Resources, Events, Agents (REA).}}

---

## Hand-off links

| Deliverable | Path |
| ----- | ----- |
| Evidence repository | [`{{ORG_NAME}}_data.md`](./{{ORG_NAME}}_data.md) |
| Compilation & scoring | [`{{ORG_NAME}}_compilation.md`](./{{ORG_NAME}}_compilation.md) |
| This summary | [`{{ORG_NAME}}_executive_summary.md`](./{{ORG_NAME}}_executive_summary.md) |
| Layer radar (PNG) | [`assets/{{ORG_NAME}}_layer_radar.png`](./assets/{{ORG_NAME}}_layer_radar.png) |

---

## If you want a report like this

This write-up is a case of Sensorica’s P2P-ness assessment help. If you are reading as a visitor — another project, network, lab, or commons — and you want the same kind of map for your organization, request an assessment on [Sensorica’s P2P-ness assessment page](https://www.sensorica.co/ventures/p2p-ness-assesment).

You get a profile, not a badge. Sensorica would rather walk with you than grade you.
