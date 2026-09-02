#!/usr/bin/env python3
"""Probe a public GitHub user/org or repo for commons-footprint evidence stubs.

Uses the unauthenticated GitHub API (60 req/hr). Prefer the GitHub MCP when
authenticated; this script is a deterministic fallback for LICENSE / stewardship-concentration signals.

Example:
  python3 tools/github_footprint.py ChangePool
  python3 tools/github_footprint.py ChangePool/FamilyDAO --markdown
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from typing import Any

API = "https://api.github.com"


def get(url: str) -> Any:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "Principles-of-P2P-github-footprint",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def repo_footprint(full_name: str) -> dict[str, Any]:
    repo = get(f"{API}/repos/{full_name}")
    license_info = repo.get("license") or {}
    try:
        contents = get(f"{API}/repos/{full_name}/contents/")
        names = [c["name"] for c in contents] if isinstance(contents, list) else []
    except urllib.error.HTTPError:
        names = []
    try:
        contrib = get(f"{API}/repos/{full_name}/contributors?per_page=10")
        contributors = [
            {"login": c.get("login"), "contributions": c.get("contributions")}
            for c in (contrib or [])
        ]
    except urllib.error.HTTPError:
        contributors = []

    return {
        "full_name": full_name,
        "html_url": repo.get("html_url"),
        "description": repo.get("description"),
        "default_branch": repo.get("default_branch"),
        "license_spdx": license_info.get("spdx_id") or license_info.get("key") or "NOASSERTION/none",
        "license_name": license_info.get("name"),
        "fork": repo.get("fork"),
        "stargazers": repo.get("stargazers_count"),
        "forks": repo.get("forks_count"),
        "open_issues": repo.get("open_issues_count"),
        "has_issues": repo.get("has_issues"),
        "archived": repo.get("archived"),
        "pushed_at": repo.get("pushed_at"),
        "root_files": names,
        "has_license_file": any(
            n.lower() in {"license", "license.md", "license.txt", "copying"}
            or n.upper().startswith("LICENSE")
            for n in names
        ),
        "has_contributing": any(n.upper().startswith("CONTRIBUTING") for n in names),
        "has_codeowners": "CODEOWNERS" in names or ".github" in names,
        "contributors": contributors,
        "bus_factor_hint": 1
        if len(contributors) <= 1
        else (2 if len(contributors) == 2 else len(contributors)),
    }


def owner_footprint(owner: str) -> dict[str, Any]:
    try:
        user = get(f"{API}/users/{owner}")
    except urllib.error.HTTPError as e:
        raise SystemExit(f"GitHub API error for user/org {owner!r}: {e}") from e
    repos = get(f"{API}/users/{owner}/repos?per_page=100&type=owner&sort=updated")
    return {
        "owner": owner,
        "type": user.get("type"),
        "html_url": user.get("html_url"),
        "public_repos": user.get("public_repos"),
        "repos": [
            {
                "name": r["name"],
                "full_name": r["full_name"],
                "license": (r.get("license") or {}).get("spdx_id") or "none",
                "fork": r.get("fork"),
                "pushed_at": r.get("pushed_at"),
                "stargazers": r.get("stargazers_count"),
            }
            for r in repos
        ],
    }


def to_markdown(payload: dict[str, Any]) -> str:
    if "full_name" in payload:
        c = payload
        lines = [
            f"### GitHub footprint — `{c['full_name']}`",
            "",
            f"- URL: {c.get('html_url')}",
            f"- License (API): `{c.get('license_spdx')}` ({c.get('license_name')})",
            f"- LICENSE file at root: **{'yes' if c.get('has_license_file') else 'no'}**",
            f"- CONTRIBUTING present: **{'yes' if c.get('has_contributing') else 'no'}**",
            f"- Stars / forks / open issues: {c.get('stargazers')} / {c.get('forks')} / {c.get('open_issues')}",
            f"- Contributors (top): {c.get('contributors')}",
            f"- Stewardship-concentration hint: **{c.get('bus_factor_hint')}**",
            f"- Root files: {', '.join(c.get('root_files') or [])}",
            "",
            "*Paste into data §1.6 / §2.2 / §9; add Status + Confidence + your reading.*",
        ]
        return "\n".join(lines)
    lines = [
        f"### GitHub footprint — owner `{payload.get('owner')}` ({payload.get('type')})",
        "",
        f"- URL: {payload.get('html_url')}",
        f"- Public repos: {payload.get('public_repos')}",
        "",
        "| Repo | License | Fork | Stars | Pushed |",
        "| ----- | ----- | ----- | ----- | ----- |",
    ]
    for r in payload.get("repos") or []:
        lines.append(
            f"| {r['full_name']} | {r['license']} | {r['fork']} | {r['stargazers']} | {r['pushed_at']} |"
        )
    lines.append("")
    lines.append("*Re-run with `owner/repo` for a deep single-repo stub.*")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("target", help="owner or owner/repo")
    p.add_argument("--markdown", action="store_true", help="Emit markdown stub for _data.md")
    args = p.parse_args(argv)

    try:
        if "/" in args.target.strip("/"):
            payload = repo_footprint(args.target.strip("/"))
        else:
            payload = owner_footprint(args.target.strip("/"))
    except urllib.error.HTTPError as e:
        print(f"GitHub API error: {e}", file=sys.stderr)
        return 2

    if args.markdown:
        print(to_markdown(payload))
    else:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
