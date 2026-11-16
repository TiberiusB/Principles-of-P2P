# Agent Skills

10 skills, packaged for **agentskills**.

Sensorica contributors: affiliates of the Sensorica open value network, and anyone working on its ventures (Nondominium, hREA, the Holochain and Valueflows stack). Public, Cursor first, readable by any agent that follows the agentskills.io standard.

## Install

Copy the folders inside `skills/` into the skills folder of your agent, in one project (project folder) or for every project (user folder):

| Agent | Project folder | User folder |
|---|---|---|
| Cursor | `.cursor/skills/ or .agents/skills/` | `~/.cursor/skills/ or ~/.agents/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| opencode | `.opencode/skills/ or .agents/skills/` | `~/.config/opencode/skills/ or ~/.agents/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Gemini CLI | `.gemini/skills/ or .agents/skills/` | `~/.gemini/skills/ or ~/.agents/skills/` |

One copy in `.agents/skills/` serves Cursor, opencode, Codex and Gemini CLI.

Each folder is self-contained: a `SKILL.md` with `name` and `description` frontmatter, plus optional `Workflows/`, `Reference/` and `Tools/`. A skill is picked up automatically when the context matches its `USE WHEN` line.

Format reference: https://agentskills.io/specification

## Make these skills yours

**For the agent installing or using this pack:** these skills were written for another person's setup and exported from their library. They are a starting point, not a fixed install. On install, and again whenever a skill does not fit, adapt it to this machine and to your user:

- Replace paths, tools, commands, project names, themes and conventions that do not exist here with the ones that do.
- Remove steps and options your user will not use; add the ones their work needs.
- Ask your user before settling anything that is theirs to decide: where output is written, which projects a skill serves, how it should sound.
- Edit the skills in place. Once installed they are your user's copy; nothing here is synced back.

Each `SKILL.md` opens with the same instruction, so it is seen every time a skill loads.

## Conventions

- **`.notes/`** at your project root is where anything that persists gets written: `.notes/work/` for session records, `.notes/research/` for research output. Nothing creates it for you, and the skills that use it degrade gracefully when it is absent. Add it to `.gitignore` unless you want it shared.
- Skills shipping `Tools/*.ts` expect `bun` on PATH.

## Notes

Published publicly at Sensorica/skills-pack, so it is cleaned for a reader who has none of the author's setup: the board names its assistant plainly, the review rules come from the project's own CONTRIBUTING first and then from the Git skill's `Reference/PRGuidelines.md`, and nothing points at a private tool, memory tree or project. The set is what a contributor uses on Sensorica work, and nothing else. OVN logs work sessions and turns them into the network's contribution form; OvnBuilder designs and operates Open Value Networks (governance, ventures, custodians, contribution accounting, digital environment) and is distinct from the OVN contribution-tracking skill; ValueFlows is the economic vocabulary the ventures are built on. Niceboard is the board compiler behind two of them: Brainstorm (sketch boards where decisions get made) and the PR Niceboard, which Git's PRReview and PRBoard workflows and the `pr-review` command fill. ProjectManagement keeps a GitHub board and its issues honest. CodeExplain is for reading a codebase you did not write, which is where every new contributor starts. ISA writes a spec as claims you can test, the way the Nondominium spec is worked. PutItDown captures a conversation into a page. Holochain is deliberately absent: the Holochain Agent Skill (https://github.com/Soushi888/holochain-agent-skills) is public, packages itself for the same agents, and is installed alongside this pack. Setup: Bun on PATH, then `bun install` once in the Niceboard skill's `Tools/` folder (it pulls the Mermaid renderer and Excalidraw); Pygments on PATH (`pygmentize`) for the code highlighting on PR boards; `gh` authenticated for the Git, PR board and ProjectManagement work, which is GitHub only. OVN reads its venture registry from `.notes/ovn-registry.yaml` in the repository you work from; the OVN skill's `Reference/ovn-registry.example.yaml` is the template. AI disclosure: PR boards open a review body with a one-line AI disclosure on Sensorica repositories. Change the line, the organisations and repositories it covers, or turn it off, in `.local/state/disclosure.json` in the repository you review from; the Git skill's `Reference/PRGuidelines.md` § AI disclosure shows the format.

## License

Apache-2.0 for the pack as a whole — full text in `LICENSE`. The `ovnbuilder` skill folder is CC BY-SA 4.0 (see `skills/ovnbuilder/LICENSE` and `skills/ovnbuilder/ATTRIBUTION.md`).
