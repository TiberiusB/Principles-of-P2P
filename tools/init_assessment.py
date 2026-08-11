#!/usr/bin/env python3
"""Scaffold a new P2P-ness assessment case study from templates.

Example:
  python3 tools/init_assessment.py \\
    --org ChangePool \\
    --title "ChangePool FamilyDAO" \\
    --assessor Tibi \\
    --date 2026-08-11 \\
    --scope project \\
    --main-site https://coincashew.io/Content/Home.html \\
    --github https://github.com/ChangePool/FamilyDAO
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
CASE = ROOT / "case-study"

FILES = [
    ("template_data.md", "{org}_data.md"),
    ("template_compilation.md", "{org}_compilation.md"),
    ("template_executive_summary.md", "{org}_executive_summary.md"),
    ("template_scores.yaml", "{org}_scores.yaml"),
]


def replace_vars(text: str, mapping: dict[str, str]) -> str:
    out = text
    for key, value in mapping.items():
        out = out.replace("{{" + key + "}}", value)
    # Collapse any remaining empty optional placeholders carefully — leave unknowns.
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--org", required=True, help="Org slug (used in filenames)")
    p.add_argument("--title", default=None, help="Display title (defaults to --org)")
    p.add_argument("--assessor", required=True)
    p.add_argument("--date", required=True, help="YYYY-MM-DD")
    p.add_argument(
        "--scope",
        action="append",
        default=[],
        choices=["project", "open_enterprise", "network", "global"],
        help="Repeatable. Default: project",
    )
    p.add_argument("--main-site", default="")
    p.add_argument("--github", default="")
    p.add_argument("--forum", default="")
    p.add_argument("--docs", default="")
    p.add_argument("--blog", default="")
    p.add_argument("--force", action="store_true", help="Overwrite existing case-study files")
    args = p.parse_args(argv)

    org = args.org
    title = args.title or org
    scopes = args.scope or ["project"]
    scope_display = " / ".join(
        {
            "project": "PROJECT",
            "open_enterprise": "OPEN-ENTERPRISE",
            "network": "NETWORK",
            "global": "GLOBAL",
        }[s]
        for s in scopes
    )

    mapping = {
        "ORG_NAME": org,
        "ASSESSOR_NAME_OR_HANDLE": args.assessor,
        "YYYY-MM-DD": args.date,
        "SCOPE_LEVELS": scope_display,
        "PRIMARY_URLS": " ; ".join(x for x in [args.main_site, args.github] if x),
        "MAIN_SITE_URL": args.main_site or "{{MAIN_SITE_URL}}",
        "MAIN_SITE": args.main_site or "{{MAIN_SITE}}",
        "FORUM_URL": args.forum or "{{FORUM_URL}}",
        "DOCS_OR_MANUAL_URL": args.docs or "{{DOCS_OR_MANUAL_URL}}",
        "BLOG_OR_NEWS_URL": args.blog or "{{BLOG_OR_NEWS_URL}}",
        "GITHUB_ORG_URL": args.github or "{{GITHUB_ORG_URL}}",
        "GOVERNANCE_PORTALS — e.g., Snapshot, Tally, Boardroom, DeepDAO, Discourse": "{{GOVERNANCE_PORTALS}}",
        "GOVERNANCE_PORTALS": "{{GOVERNANCE_PORTALS}}",
        "SNAPSHOT_SPACE_OR_URL — optional": "{{SNAPSHOT_SPACE}}",
        "TALLY_SPACE_OR_URL — optional": "{{TALLY_SPACE}}",
        "REGISTRY_URL — optional; e.g., OpenCorporates entry": "{{REGISTRY_URL}}",
        "WAYBACK_URLS — optional; founding-era snapshots": "{{WAYBACK_URLS}}",
        "SECONDARY_RESOURCES — optional bibliography/URLs specific to this assessment": "{{SECONDARY_RESOURCES}}",
    }

    CASE.mkdir(parents=True, exist_ok=True)
    (CASE / "assets").mkdir(parents=True, exist_ok=True)

    written = []
    for src_name, dst_pattern in FILES:
        src = TEMPLATES / src_name
        if not src.exists():
            print(f"error: missing template {src}", file=sys.stderr)
            return 2
        dst = CASE / dst_pattern.format(org=org)
        if dst.exists() and not args.force:
            print(f"skip (exists): {dst}  (use --force to overwrite)")
            continue
        text = src.read_text(encoding="utf-8")
        text = replace_vars(text, mapping)
        if src_name == "template_scores.yaml":
            # Rewrite scope_levels block from --scope
            scope_block = "scope_levels:\n" + "\n".join(f"  - {s}" for s in scopes) + "\n"
            text = re.sub(
                r"scope_levels:\n(?:  #[^\n]*\n|  - [^\n]+\n)+",
                scope_block,
                text,
                count=1,
            )
            text = text.replace(f'title: "{org}"', f'title: "{title}"')
            text = text.replace(f'title: "{org}"', f'title: "{title}"')  # idempotent
            if f'title: "{org}"' in text or f"title: '{org}'" in text:
                pass
            text = re.sub(
                r'^title:\s*".*"',
                f'title: "{title}"',
                text,
                count=1,
                flags=re.MULTILINE,
            )
        dst.write_text(text, encoding="utf-8")
        written.append(dst)

    print("Scaffolded:")
    for path in written:
        print(f"  {path.relative_to(ROOT)}")
    print(f"  { (CASE / 'assets').relative_to(ROOT) }/")
    print(
        "\nNext:\n"
        f"  1. Fill evidence in case-study/{org}_data.md\n"
        f"  2. Fill numeric cells in case-study/{org}_scores.yaml (0–5 / NE / N/A)\n"
        f"  3. python3 tools/compute_scores.py case-study/{org}_scores.yaml "
        f"--write-summary case-study/{org}_compilation.md --radar\n"
        f"  4. Write narratives in compilation + executive summary\n"
        f"  5. python3 tools/validate_assessment.py {org}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
