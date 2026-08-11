#!/usr/bin/env python3
"""Compute layer/level/overall averages from a scores YAML; optionally update radar + docs.

Example:
  python3 tools/compute_scores.py case-study/ChangePool_scores.yaml \\
    --write-summary case-study/ChangePool_compilation.md \\
    --radar --png-only-fail \\
    --print-json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from scorelib import (  # noqa: E402
    ScoreError,
    compute_summary,
    format_summary_markdown,
    load_scores,
    patch_score_summary_section,
)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("scores_yaml", type=Path, help="Path to *_scores.yaml")
    p.add_argument(
        "--write-summary",
        type=Path,
        default=None,
        help="Patch ## Score Summary in this compilation markdown",
    )
    p.add_argument(
        "--radar",
        action="store_true",
        help="Generate radar chart via tools/radar_chart.py",
    )
    p.add_argument(
        "--radar-out",
        type=Path,
        default=ROOT / "case-study" / "assets",
        help="Radar output directory",
    )
    p.add_argument(
        "--png-only-fail",
        action="store_true",
        help="Fail if radar PNG cannot be written",
    )
    p.add_argument("--print-json", action="store_true", help="Print machine-readable summary")
    args = p.parse_args(argv)

    try:
        data = load_scores(args.scores_yaml)
        summary = compute_summary(data)
    except ScoreError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    if summary.total_unset and any(
        level in summary.scope_levels
        for level in summary.scope_levels
    ):
        # Warn only for unset cells inside scope — compute_summary already counted them.
        if summary.total_unset > 0:
            print(
                f"warning: {summary.total_unset} unset (null) cell(s) in score sheet — "
                "fill with 0–5, NE, or N/A before finalizing.",
                file=sys.stderr,
            )

    print(format_summary_markdown(summary))

    if args.print_json:
        payload = {
            "org_name": summary.org_name,
            "title": summary.title,
            "scope_levels": summary.scope_levels,
            "layer_averages": summary.layer_averages,
            "layer_basis": summary.layer_basis,
            "level_averages": summary.level_averages,
            "overall": summary.overall,
            "strongest_layer": summary.strongest_layer,
            "weakest_layer": summary.weakest_layer,
            "total_scored": summary.total_scored,
            "total_ne": summary.total_ne,
            "total_na": summary.total_na,
            "total_unset": summary.total_unset,
        }
        print(json.dumps(payload, indent=2))

    if args.write_summary:
        path = args.write_summary
        if not path.exists():
            print(f"error: compilation not found: {path}", file=sys.stderr)
            return 2
        text = path.read_text(encoding="utf-8")
        updated = patch_score_summary_section(text, format_summary_markdown(summary))
        path.write_text(updated, encoding="utf-8")
        print(f"updated Score Summary in {path}")

    if args.radar:
        if summary.overall is None or any(
            summary.layer_averages[k] is None for k in ("structural", "operational", "economic", "cultural")
        ):
            print("error: cannot build radar — missing layer average(s)", file=sys.stderr)
            return 2
        cmd = [
            sys.executable,
            str(ROOT / "tools" / "radar_chart.py"),
            "--org",
            summary.org_name,
            "--title",
            summary.title,
            "--structural",
            str(summary.layer_averages["structural"]),
            "--operational",
            str(summary.layer_averages["operational"]),
            "--economic",
            str(summary.layer_averages["economic"]),
            "--cultural",
            str(summary.layer_averages["cultural"]),
            "--overall",
            str(summary.overall),
            "--out",
            str(args.radar_out),
        ]
        if args.png_only_fail:
            cmd.append("--png-only-fail")
        print("running:", " ".join(cmd))
        proc = subprocess.run(cmd, cwd=str(ROOT))
        if proc.returncode != 0:
            return proc.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
