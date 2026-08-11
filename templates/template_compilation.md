# {{ORG_NAME}} — P2P-ness Compilation & Scoring

This document compiles quantitative scores and rationales derived from evidence in `{{ORG_NAME}}_data.md`, following `Evaluation.md` (layers × dimensions × levels), `Model.md` (fundamental principles), `Hybrid.md` (two-axis hybridization X-ray), `Ethos.md` (ethos dimensions), and `new-collaborative-entrepreneurship.md` (Enterprise Stack / pattern analysis).

- ORG_NAME: {{ORG_NAME}}
- ASSESSOR: {{ASSESSOR_NAME_OR_HANDLE}}
- ASSESSMENT_DATE: {{YYYY-MM-DD}}
- SCOPE_LEVELS: {{PROJECT / OPEN-ENTERPRISE / NETWORK / GLOBAL — which apply}}
- Evidence repository: `{{ORG_NAME}}_data.md`

## Scoring Scale (0–5) and Conventions

- 0 = Absent / contrary to P2P (**evidence of absence**: you looked and found the opposite)
- 1 = Weak / token
- 2 = Partial / significant gaps
- 3 = Moderate / functional
- 4 = Strong / high fidelity
- 5 = Exemplary / benchmark

Conventions:
- `NE` = not evidenced. Never average `NE` as 0; exclude the cell and flag it as a TODO in the data repository. Absence of evidence is not evidence of absence.
- `N/A` = level out of scope for this organization (per SCOPE_LEVELS). Exclude from averages.
- **Numeric source of truth:** `case-study/{{ORG_NAME}}_scores.yaml`. After editing cells, run `tools/compute_scores.py` to refresh this document's Score Summary and the radar chart. Mirror cell values into the layer tables below for human-readable rationales; do not hand-average.
- If using the 0–3 mapping from `Model.md`'s benchmark rubric, translate: 0→0, 1→1–2, 2→3–4, 3→5.
- When uncertain despite some evidence, prefer conservative (lower) scores and say why in the rationale.
- Do not collapse contradictions into an average. Explain tensions in the profile.

## Interpretation Rule: Profile Before Score

The main output is a **dynamic P2P profile**. Layer/level averages and any overall score are secondary summary signals only. A total score can hide exactly the contradictions that matter most in complex adaptive systems; the conclusion must explain tensions, path dependencies, capture risks, and trajectory.

---

## Dynamic Profile (fill after scoring; place first when reading)

- **Layer profile**: one line per layer (structural, operational, economic, cultural) — main strength, main gap.
  - Structural:
  - Operational:
  - Economic:
  - Cultural/Ecosystem:
- **Level profile**: which levels (project / open-enterprise / network / global) are strongest and weakest, and why.
- **Trajectory**: moving toward more P2P / stable hybrid / capture risk / insufficient evidence.
  - Disintermediation direction: is the organization systematically replacing centralized hubs (in its own structure and its market) with distributed, horizontal mechanisms over time? (per `Model.md`, "fundamental nature of the p2p movement")
- **Main tensions**:
  - Openness vs quality:
  - Transparency vs privacy:
  - Meritocracy/reputation vs incumbent capture:
  - Capital access vs commons governance:
  - Formal decentralization vs lived agency:

---

## Layer 1: Structural/Formal

| Dimension | Project | Open-Enterprise | Network | Global | Rationale (evidence refs + status) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Membership & Entry/Exit |  |  |  |  |  |
| Role & Task Structure |  |  |  |  |  |
| Governance & Decision-Making |  |  |  |  |  |
| Value Accounting & Rewards / Redistribution |  |  |  |  |  |
| Legal / Liability / Financial Structures |  |  |  |  |  |
| Infrastructure & Commons (incl. plural property-regime map) |  |  |  |  |  |
| **Layer average (excluding NE/N/A)** |  |  |  |  |  |

## Layer 2: Operational/Process

| Dimension | Project | Open-Enterprise | Network | Global | Rationale (evidence refs + status) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Transparency & Access to Information |  |  |  |  |  |
| Coordination of Tasks & Workflows (incl. stigmergy) |  |  |  |  |  |
| Contribution Logging & Attribution |  |  |  |  |  |
| Conflict Management & Forking |  |  |  |  |  |
| Reputation, Trust & Accountability |  |  |  |  |  |
| **Layer average (excluding NE/N/A)** |  |  |  |  |  |

## Layer 3: Economic

| Dimension | Project | Open-Enterprise | Network | Global | Rationale (evidence refs + status) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Property Regime & Licensing |  |  |  |  |  |
| Contribution & Value Accounting / Benefit Distribution |  |  |  |  |  |
| Funding & Capital Sources (incl. capital-vs-resources posture) |  |  |  |  |  |
| Revenue Model & Market Interface (incl. disintermediation) |  |  |  |  |  |
| Tokenomics & Incentives (if applicable) |  |  |  |  |  |
| Cost Structure & Sustainability |  |  |  |  |  |
| Economic Openness & Cost Transparency |  |  |  |  |  |
| **Layer average (excluding NE/N/A)** |  |  |  |  |  |

## Layer 4: Cultural/Ecosystem/Superstructural

| Dimension | Project | Open-Enterprise | Network | Global | Rationale (evidence refs + status) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Values, Norms & Culture |  |  |  |  |  |
| Learning, Adaptation & Innovation (incl. reflexivity) |  |  |  |  |  |
| Meaning, Purpose & Identity |  |  |  |  |  |
| Phenomenological Grounding (Lived Experience) |  |  |  |  |  |
| Ecosystem Relations & External Engagement |  |  |  |  |  |
| Contextual & Ecological Embeddedness |  |  |  |  |  |
| **Layer average (excluding NE/N/A)** |  |  |  |  |  |

## Score Summary (secondary signals)

> **Do not hand-edit averages.** Fill `case-study/{{ORG_NAME}}_scores.yaml`, then run:
> `python3 tools/compute_scores.py case-study/{{ORG_NAME}}_scores.yaml --write-summary case-study/{{ORG_NAME}}_compilation.md --radar`
> That command replaces this section and writes the radar asset.

- Structural average:
- Operational average:
- Economic average:
- Cultural/Ecosystem average:
- **Level averages** (average across layers, excluding NE/N/A):
  - Project:
  - Open-Enterprise:
  - Network:
  - Global / inter-network:
- Overall P2P-ness index (optional, simple avg of layer avgs; secondary only):
- Strongest layer(s) / level(s):
- Weakest layer(s) / level(s):
- For every average, note the basis (how many cells scored vs NE/N/A).

---

## Fundamental Principles Coverage (cross-check per `Model.md`)

Synthesize a score per principle from the contributing dimensions. If a layer average is strong but a principle is weak (or vice versa), explain the discrepancy in the conclusion. Layer averages above come from `tools/compute_scores.py` over `{{ORG_NAME}}_scores.yaml`.

| Fundamental principle | Contributing dimensions (this document) | Score (0–5 / NE) | Evidence summary & gaps |
| ----- | ----- | ----- | ----- |
| 1. Commons Orientation | 1.6, 3.1, Ethos: Stewardship |  |  |
| 2. Open Participation & Voluntary Contribution | 1.1, 1.2, Ethos: Openness |  |  |
| 3. Peer Governance | 1.3, 2.2, Ethos: Decentralization / Self-organization |  |  |
| 4. Recognition & Distribution of Benefits | 1.4, 2.3, 3.2, Ethos: Contribution & Recognition / Fairness |  |  |
| 5. Generativity & Adaptivity | 2.4, 4.2, forking evidence |  |  |
| 6. Contextual Embeddedness | 4.6, 3.6 (ecological costs) |  |  |
| 7. Reflexivity & Transparency | 2.1, 4.2, Ethos: Transparency |  |  |
| 8. Phenomenological Grounding | 4.4, narratives module, Ethos: Phenomenological Grounding |  |  |

---

## Hybridization X-ray (per `Hybrid.md`)

Two-axis scoring: rate **both** P2P fidelity (0–5) and Traditional fidelity (0–5) per dimension, with an evidence note. Interpretation: both high = genuinely hybrid; Traditional ≫ P2P = captured/legacy; P2P ≫ Traditional = pure P2P.

| X-ray dimension | P2P fidelity (0–5) | Traditional fidelity (0–5) | Hybrid signal / evidence note |
| ----- | ----- | ----- | ----- |
| Legal existence / entity |  |  |  |
| Ownership of IP / outputs |  |  |  |
| Capital structure / funding |  |  |  |
| Decision-making |  |  |  |
| Formal vs emergent authority |  |  |  |
| Contribution accounting & rewards |  |  |  |
| Revenue model |  |  |  |
| Distribution of surplus |  |  |  |
| Code / data openness |  |  |  |
| Infrastructure control |  |  |  |
| Coordination mode |  |  |  |
| Hiring / employment model |  |  |  |
| Conflict & fork management |  |  |  |
| Values & narrative |  |  |  |
| Reputation & crediting |  |  |  |
| Phenomenological grounding |  |  |  |
| Relationship to markets & incumbents |  |  |  |
| Regulatory / compliance posture |  |  |  |

**Hybridization model match** (check all that apply; add evidence): foundation + for-profit subsidiary / open-core company / foundation steward + commercial ecosystem / DAO + legal wrapper / multi-stakeholder cooperative + token / commons steward + service company / corporate sponsorship of contributors / open core + private forks / federated network with corporate hubs / spinout capture / formal decentralization with experiential alienation / other:

**Red flags to check** (surface any that apply):
- CLA assigning IP centrally; token/equity concentration; roadmap capture by single employer; trademark constraints on forks; permanent admin powers without review; reputation systems with no decay/appeal; transparency practices that expose people without improving peer verification; capital providers with strategic vetoes; high formal openness with low reported trust/recognition/belonging.

---

## Enterprise Stack & Pattern Analysis (per `new-collaborative-entrepreneurship.md` and `Distributed business model patterns - Models.csv`)

The Enterprise Stack is a heuristic map, not a fixed ontology. Record misfits rather than forcing them.

- **Stack positioning summary** (from data Sec. 0.2): which layers (P/S/O/VC/VT/PL/E/CM/MC) the organization actually operates at, and the deepest shared-consequence layer reached.
- **Misfit notes** (from data Sec. 0.4): where the map distorts the case.
- **Orchestrator-drift check**: does any "orchestration" role function as a privileged coordinating center (roadmap control, treasury discretion, gatekeeping), or does coordination remain distributed field stewardship? Evidence:

### Pattern risk table

For each business-model pattern identified in data Sec. 0.3:

| Pattern | Stack level(s) | OVN fit (high/med/low) | P2P risks (capture / lock-in / mission drift / governance complexity) | Adaptation rule (how to run it without violating openness, transparency, fair redistribution) | Capital governance test (does finance stay subordinate to commons governance?) |
| ----- | ----- | ----- | ----- | ----- | ----- |
|  |  |  |  |  |  |

The completed pattern analysis, together with the path-dependency table and stress tests below, feeds the Economic Model & Migration Path section of `{{ORG_NAME}}_executive_summary.md` (see `templates/template_prompt.md` → Deliverables). The compilation Score Summary is generated from `{{ORG_NAME}}_scores.yaml` via `tools/compute_scores.py`, which also feeds `tools/radar_chart.py` for the executive summary radar image.

---

## Path Dependency and Capture Analysis

| Area | Evidence summary | Productive path dependence | Capture-producing risk | Mitigation / next evidence |
| ----- | ----- | ----- | ----- | ----- |
| Founding choices and initial rules |  |  |  |  |
| Early contribution/reputation history |  |  |  |  |
| Funding/capital structure |  |  |  |  |
| Infrastructure/platform dependencies |  |  |  |  |
| Governance defaults and admin powers (incl. sunset clauses) |  |  |  |  |

---

## Complexity Stress Tests

### Mechanism analysis

| Mechanism / Pattern | Feedback loop created | What becomes visible | What becomes hidden | Lock-in risk | Who gains adaptive capacity | Who loses agency | Assessment |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|  |  |  |  |  |  |  |  |

### Robustness scenario results

For each scenario, state whether the organization adapts or reverts to hierarchy, enclosure, surveillance, or capital capture.

| Structure / mechanism | Participation grows 10x | Funding drops 50% | Founding/keystone actor exits | Conflict produces a fork | Verdict (adapts / reverts to …) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Governance process |  |  |  |  |  |
| Treasury / funding |  |  |  |  |  |
| Contribution accounting |  |  |  |  |  |
| Infrastructure / platforms |  |  |  |  |  |

---

## Scenario / Simulation Recommendations

- Contribution accounting scenarios (test whether the value equation over-rewards visible, early, technical, or capital contributions while under-recognizing care, coordination, translation, maintenance, and contextual work):
- Governance scenarios (quorum failure, voter fatigue, collusion, delegate concentration, founder exit, emergency powers, low-participation decisions):
- Benefit redistribution scenarios (revenue shocks, delayed payouts, unequal information access, disputes over weights):
- Reputation scenarios (incumbent lock-in, decay, appeal paths, portability, recovery after failure):
- Highest-priority simulation/backtest:

---

## Ethos Assessment (per `Ethos.md`)

| Ethos Dimension | Score (0–5 / NE) | Short rationale (citations) | Traditional baseline contrast |
| ----- | ----- | ----- | ----- |
| Openness / Access |  |  |  |
| Transparency |  |  |  |
| Contribution & Recognition |  |  |  |
| Stewardship of Commons |  |  |  |
| Decentralization / Distributed Influence |  |  |  |
| Self-organization / Initiative |  |  |  |
| Fairness / Equity |  |  |  |
| Resilience / Adaptability |  |  |  |
| Reliability / Trustworthiness |  |  |  |
| Economic Openness & Cost Transparency |  |  |  |
| Mission / Shared Purpose |  |  |  |
| Non-domination / Anti-hierarchy |  |  |  |
| Phenomenological Grounding |  |  |  |
| Quality of Peer Interactions |  |  |  |

---

## Conclusion

- 4–8 sentences summarizing the **profile**, not just the score: strongest P2P dimensions, weakest/capture-prone dimensions, main feedback loops, privacy/capital/reputation risks, trajectory (including disintermediation direction), and the priority pathway for improvement.
- Explain any discrepancy between strong layer averages and weak fundamental-principle coverage.
- Split improvement pathways into **quick wins** (project-level, low-stakes pilots) vs **structural changes** (governance defaults, capital accountability, property regimes).
- Reduction-risk check (per `improvements.md`): confirm the assessment did not collapse multidimensional contribution into a scalar, did not treat the Enterprise Stack as an ontology, and did not mistake orchestration language for distributed coordination.
