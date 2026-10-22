# Methodology

## Purpose

This methodology helps an AI agent and a human assessor turn a P2P-ness assessment into practical business-model consulting. It is designed for unsolicited or early-stage advisory work, where the recipient has not necessarily asked for help and the tone must be respectful, useful, and non-dogmatic.

The method is not a replacement for the repository's formal assessment process. It depends on that process for evidence, scoring, and grounding. The consulting layer begins after there is enough evidence to say something responsible about the organization's current economic and organizational position.

## Source pattern

The method is distilled from two case studies:

- Flowsta: user-owned identity, signatures, Holochain integration, and a transition opportunity from paid service wrapper to shared trust infrastructure.
- YourOwnAI: local-first AI, signed records, open-source desktop app, and a transition opportunity from individual AI sovereignty to group intelligence and ecosystem utility.

Both cases moved through the same arc:

1. Assess what exists now.
2. Identify the decisive tension.
3. Show how current technical capabilities enable larger value layers.
4. Explain why the present economic model may block those layers.
5. Propose a transition that improves opportunity while preserving values.

## Method principles

### Evidence before imagination

Every consulting claim must trace back to public evidence, repository files, sourced doctrine, or explicit human input. When evidence is absent, say so.

### Transition, not condemnation

Describe the organization as it stands now, then show a better adjacent possibility. Avoid framing the organization as hypocritical or defective.

### Opportunity before ideology

Use P2P, Open Value Network (OVN), nondominium, contribution accounting, and benefit redistribution only when they solve an economic, organizational, or technical problem visible in the case.

### Technology enables economics

Do not jump from values to recommendations. Show how concrete features, architecture, licenses, governance interfaces, APIs, or data flows make specific economic patterns possible.

### Value is plural

Assess value beyond price: trust, consent, authorship, contribution memory, governance legitimacy, portability, field intelligence, reputation, learning, public utility, and ecosystem capacity.

### Human supervision is part of the method

The AI agent drafts and structures; the human assessor supplies judgment, selects framing, corrects tone, and decides what advice is appropriate to offer.

## Phase 1: Intake and scope

Establish:

- organization name and URLs;
- intended audience;
- register: assessment, collaborative, or unsolicited consulting note;
- whether there is already a case-study folder;
- known primary sources;
- sensitive areas to avoid;
- human assessor and date.

Deliverable: `templates/intake.md`.

## Phase 2: Evidence base

Use the existing P2P-ness assessment workflow:

- scaffold or reuse case-study files;
- read every relevant folder under `case-study/` before searching the web;
- collect public sources;
- inspect repositories and technical docs;
- use Grounded Docs for OVN, P2P, Sensorica, nondominium, and related doctrine;
- separate evidence from inference;
- record missing evidence as gaps, not accusations.

### The case-study folder is gitignored

`case-study/` is in `.gitignore`. Default searches that honour ignore files will return nothing from it, which can make a rich evidence base look empty. Open the folders directly, or search with `rg --no-ignore`. Never treat a missed search as evidence of absence.

This matters in both directions. The folder holds the evidence base for organizations already assessed (`Flowsta`, `YourOwnAI`, `Nondominium`, `Holons`, `REPAIRE`), and it holds worked examples of the output register. When a case touches an organization already in there, prior work is the starting point rather than something to rediscover. `case-study/Nondominium/nondominium-economic model.md` in particular carries the pattern composition, OVN license floors, and custodian and sponsor distinctions that recur across cases.

Deliverables: case-study `_data.md`, `_compilation.md`, `_scores.yaml`, `_executive_summary.md`, plus `templates/research_log.md` if the consulting work is outside a full assessment.

## Phase 3: Current model diagnosis

Describe the organization as it is today.

Look for:

- product/service/platform/ecosystem/mission layers;
- business-model patterns in use;
- monetization gates;
- governance boundaries;
- technical dependencies;
- property/licensing posture;
- user and developer lock-in risks;
- capital-governance relationships;
- what is open, closed, hosted, self-hostable, forkable, or brand-controlled.

Deliverable: `templates/current_model.md`.

## Phase 4: Technical capability map

Connect technical features to economic possibilities.

For each important feature or architecture element, ask:

- What can this capability verify, coordinate, protect, remember, or distribute?
- What value layer does it enable?
- What is missing for it to become socio-economic infrastructure?
- What governance or monetization boundary could block adoption?

Deliverable: `templates/technical_capability_map.md`.

## Phase 5: Opportunity and value-layer map

Identify new value layers that are adjacent to the organization's current capabilities.

Examples from Flowsta:

- identity continuity;
- consent memory;
- contribution receipts;
- rights and authorship;
- group legitimacy;
- data portability;
- ecosystem intelligence;
- trust as shared infrastructure.

Examples from YourOwnAI:

- local AI sovereignty;
- signed cognitive records;
- group memory;
- contribution-aware AI workflows;
- OurOwnAI as collective intelligence;
- epistemic evolution;
- nondominium-compatible AI utility.

Deliverable: `templates/opportunity_map.md`.

## Phase 6: Sustainability and transition design

Separate three sustainability layers:

1. Service cash flow: subscriptions, support, hosted convenience, enterprise integration.
2. Ecosystem services: custom development, education, onboarding, governance templates, migration, audits, self-hosting.
3. Benefit redistribution: revenue shares, infrastructure pools, non-currency returns, governance rights, field intelligence, service credits, node hosting, documentation, and reputation.

For OVN-compatible cases, map the organization as a possible infrastructure contributor to ventures. The OVN wiki describes a venture as a context where resources and benefits are produced, and the benefit redistribution algorithm applies at venture level while contribution accounting applies at resource level.

Deliverable: `templates/sustainability_models.md`.

## Phase 7: Migration path

Design a staged path. Avoid abrupt conversion narratives.

Common stages:

1. current hybrid;
2. make the transition legible;
3. package for adjacent ecosystems;
4. pilot socio-economic use cases;
5. define the utility core;
6. create a steward circle or protocol commons;
7. launch OVN-compatible edge ventures;
8. add field finance without enclosure.

Deliverable: `templates/migration_path.md`.

## Phase 8: Founder-facing suggestions

Write as a map and invitation.

Use:

- "you might consider";
- "the opportunity is";
- "the risk is not bad intent, but structural drift";
- "this can start at the edge";
- "the company does not have to become an OVN all at once."

Avoid:

- "must";
- "should" when it sounds like command;
- accusations of extraction unless evidenced and necessary;
- P2P purity tests;
- jargon without explanation.

Deliverable: `templates/founder_suggestions.md`.

## Phase 9: Review and validation

The human assessor reviews:

- evidence traceability;
- tone and fairness;
- strategic usefulness;
- missing citations;
- speculative claims;
- whether the advice respects the organization's own values and constraints.

Use `templates/human_supervision_log.md` and `templates/claims_checklist.md`.
