# AI-Agent Workflow

Use this workflow when producing business-model consulting from a P2P-ness assessment.

## 0. Load required context

Read:

- `templates/template_prompt.md`
- `Foundation/Model.md`
- `Foundation/Evaluation.md`
- `Foundation/Hybrid.md`
- `Foundation/Ethos.md`
- `Foundation/Enterprise-Stack-collaborative-entrepreneurship.md`
- `Foundation/Distributed business model patterns - Models.csv`
- `Foundation/Others/Truth.md`
- `Foundation/Others/Value.md`
- relevant case-study files
- `business_models_consulting/methodology.md`
- `business_models_consulting/rules.md`

For OVN, P2P, Sensorica, nondominium, value, contribution accounting, or benefit redistribution claims, query Grounded Docs before asserting doctrine.

## 1. Determine work mode

Choose one:

- Full P2P-ness assessment plus consulting.
- Consulting extension to an existing assessment.
- Standalone opportunity map from a partial evidence base.

If evidence is thin, mark the output as provisional.

## 2. Build or reuse the evidence base

Use the existing assessment tooling when possible:

```bash
python tools/init_assessment.py ORG_NAME --register assessment
python tools/compute_scores.py case-study/ORG_NAME/ORG_NAME_scores.yaml --write-summary case-study/ORG_NAME/ORG_NAME_compilation.md --radar --png-only-fail
python tools/validate_assessment.py ORG_NAME
```

When not running a full assessment, maintain `templates/research_log.md` and `templates/claims_checklist.md`.

## 3. Diagnose the current model

Fill `templates/current_model.md`.

Minimum outputs:

- current product/service description;
- Enterprise Stack position;
- business-model patterns in use;
- monetization points;
- open/closed boundary;
- governance boundary;
- technical dependencies;
- risks that may block new opportunities.

## 4. Map technical capabilities

Fill `templates/technical_capability_map.md`.

For each capability:

1. Name the feature or architecture element.
2. Cite evidence.
3. Explain what it makes possible.
4. Link it to an economic pattern.
5. Identify what must still be developed.
6. Identify monetization or governance gates.

Use diagrams when they clarify the architecture.

## 5. Identify new value layers

Fill `templates/opportunity_map.md`.

Each value layer should answer:

- What current capability enables this?
- What is missing?
- Who benefits?
- Why a simple transactional model may block it?
- What sustainability path fits?
- What needs human review?

## 6. Design sustainability

Fill `templates/sustainability_models.md`.

Always distinguish:

- service cash flow;
- ecosystem services;
- benefit redistribution.

When relevant, include:

- infrastructure contribution rules;
- non-currency returns;
- regenerative infrastructure pool;
- protocol steward circle;
- outcome commons contracting;
- field finance.

## 7. Design migration

Fill `templates/migration_path.md`.

A good path:

- starts from current reality;
- preserves near-term cash flow;
- keeps user-sovereign basics accessible;
- defines the utility core;
- tests edge ventures before converting the whole organization;
- names path dependencies and robustness tests.

## 8. Write founder-facing suggestions

Fill `templates/founder_suggestions.md`.

Structure:

1. Why this note exists.
2. Where the organization stands now.
3. How to read the assessment.
4. Why the broader economic paradigm matters.
5. Core opportunity.
6. Ideal model or pattern.
7. New value dimensions.
8. Why a purely transactional model is too small.
9. Sustainability models.
10. Migration path.
11. Strategic message.

## 9. Human supervision checkpoint

Before finalizing, ask the human assessor to review:

- tone;
- strongest claims;
- weakest evidence;
- use of OVN/P2P language;
- possible unfairness to the organization;
- whether the advice is actionable.

Record input in `templates/human_supervision_log.md`.

## 10. Final verification

Check:

- every factual claim has evidence or is marked provisional;
- jargon is explained on first use;
- recommendations are invitational;
- current monetization is treated as legitimate unless evidence shows harm;
- no private or personal data is used;
- links are valid enough for handoff;
- the final output names both opportunities and constraints.
