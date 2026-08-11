#!/usr/bin/env python3
"""Validate a P2P-ness assessment case study against quality gates.

Example:
  python3 tools/validate_assessment.py ChangePool
  python3 tools/validate_assessment.py ChangePool --strict
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from scorelib import ScoreError, compute_summary, load_scores  # noqa: E402

STATUS_RE = re.compile(
    r"`(Evidenced|Partially evidenced|Not evidenced|Contradicted|Not applicable)`"
)
CONF_RE = re.compile(r"`(High|Medium|Low|Medium-High|Low-Medium)`")


def check_file(path: Path, errors: list[str], warnings: list[str], label: str) -> None:
    if not path.exists():
        errors.append(f"missing {label}: {path}")
        return
    if path.stat().st_size < 200:
        warnings.append(f"{label} looks empty/stub: {path}")


def check_sections(path: Path, required: list[str], errors: list[str]) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    for heading in required:
        if heading not in text:
            errors.append(f"{path.name}: missing section {heading!r}")
    return text


def check_data_findings(text: str, warnings: list[str]) -> None:
    # Heuristic: findings bullets near Status tags
    findings_blocks = len(re.findall(r"- Findings:", text))
    status_hits = len(STATUS_RE.findall(text))
    if findings_blocks and status_hits < max(3, findings_blocks // 2):
        warnings.append(
            f"data: few Status tags ({status_hits}) relative to Findings headings ({findings_blocks})"
        )
    if "Phenomenological Grounding" in text and "not collected" not in text.lower():
        if re.search(r"Phenomenological Grounding[\s\S]{0,800}`Not evidenced`", text):
            pass
        elif "Participant Narratives" in text and "not collected" in text.lower():
            pass


def check_scores_vs_radar(
    org: str,
    summary,
    errors: list[str],
    warnings: list[str],
) -> None:
    png = ROOT / "case-study" / "assets" / f"{org}_layer_radar.png"
    svg = ROOT / "case-study" / "assets" / f"{org}_layer_radar.svg"
    if not png.exists() and not svg.exists():
        errors.append(
            f"missing radar image: expected case-study/assets/{org}_layer_radar.png "
            "(or .svg). Run compute_scores.py --radar"
        )
    elif not png.exists():
        warnings.append(
            f"radar PNG missing ({svg.name} present). Cursor preview prefers PNG."
        )

    exec_path = ROOT / "case-study" / f"{org}_executive_summary.md"
    if exec_path.exists():
        et = exec_path.read_text(encoding="utf-8")
        if f"{org}_layer_radar.png" not in et and f"{org}_layer_radar.svg" not in et:
            errors.append(
                f"{exec_path.name}: does not embed radar image under Layer averages"
            )
        if "## Layer averages (radar)" not in et and "## Layer averages" not in et:
            errors.append(f"{exec_path.name}: missing Layer averages (radar) section")
        if "## Economic Model & Migration Path" not in et:
            errors.append(f"{exec_path.name}: missing Economic Model & Migration Path")

    # Compilation score summary consistency (approximate)
    comp = ROOT / "case-study" / f"{org}_compilation.md"
    if comp.exists() and summary.overall is not None:
        ct = comp.read_text(encoding="utf-8")
        for key, label in [
            ("structural", "Structural average"),
            ("operational", "Operational average"),
            ("economic", "Economic average"),
            ("cultural", "Cultural"),
        ]:
            avg = summary.layer_averages[key]
            if avg is None:
                continue
            # Look for **X.X** near the label
            if label.split()[0] not in ct:
                warnings.append(f"compilation: could not find {label} line to cross-check")
                continue
            m = re.search(
                rf"{re.escape(label.split()[0])}[^\n]*\*\*([0-9]+(?:\.[0-9]+)?)\*\*",
                ct,
            )
            if m:
                doc_v = float(m.group(1))
                if abs(doc_v - avg) > 0.05:
                    errors.append(
                        f"compilation {label}: doc has {doc_v}, scores YAML has {avg}"
                    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("org", help="Org slug (case-study/{org}_*)")
    p.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors (exit 1)",
    )
    args = p.parse_args(argv)
    org = args.org
    errors: list[str] = []
    warnings: list[str] = []

    data_p = ROOT / "case-study" / f"{org}_data.md"
    comp_p = ROOT / "case-study" / f"{org}_compilation.md"
    exec_p = ROOT / "case-study" / f"{org}_executive_summary.md"
    scores_p = ROOT / "case-study" / f"{org}_scores.yaml"

    for path, label in [
        (data_p, "data"),
        (comp_p, "compilation"),
        (exec_p, "executive summary"),
        (scores_p, "scores YAML"),
    ]:
        check_file(path, errors, warnings, label)

    data_text = check_sections(
        data_p,
        [
            "## 0) Organizational Snapshot",
            "## 1) Structural / Formal Layer",
            "## 7) Participant Narratives Module",
            "## 9) Path Dependency",
            "## 10) Complexity Stress Tests",
        ],
        errors,
    )
    if data_text:
        check_data_findings(data_text, warnings)
        if "not collected" not in data_text.lower() and "`Not evidenced`" not in (
            re.search(
                r"### 4\.4 Phenomenological[\s\S]{0,1200}",
                data_text,
            )
            or [""]
        )[0]:
            # soft check
            if "### 4.4" in data_text and "Not evidenced" not in data_text[
                data_text.find("### 4.4") : data_text.find("### 4.4") + 800
            ]:
                warnings.append(
                    "data §4.4: if narratives were not collected, mark Not evidenced"
                )

    check_sections(
        comp_p,
        [
            "## Dynamic Profile",
            "## Score Summary",
            "## Fundamental Principles Coverage",
            "## Hybridization X-ray",
            "## Ethos Assessment",
            "## Conclusion",
        ],
        errors,
    )

    summary = None
    if scores_p.exists():
        try:
            summary = compute_summary(load_scores(scores_p))
            if summary.total_unset:
                errors.append(
                    f"scores YAML: {summary.total_unset} unset null cell(s) — "
                    "fill with 0–5, NE, or N/A"
                )
            if summary.overall is None:
                errors.append("scores YAML: no computable overall index (all NE/N/A?)")
        except ScoreError as e:
            errors.append(f"scores YAML: {e}")

    if summary:
        check_scores_vs_radar(org, summary, errors, warnings)

    print(f"validate_assessment: {org}")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠ {w}")
    if not errors and not warnings:
        print("  ✓ all checks passed")

    if errors:
        return 1
    if warnings and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
