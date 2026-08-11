#!/usr/bin/env python3
"""Shared score-sheet loading and averaging for P2P-ness assessments.

Cell values: number 0–5, "NE", "N/A", or null (treated as unset / error if left null
in a scoped level). NE and N/A are excluded from averages — never treated as 0.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

LEVELS = ("project", "open_enterprise", "network", "global")
LAYER_KEYS = ("structural", "operational", "economic", "cultural")

LAYER_LABELS = {
    "structural": "Structural",
    "operational": "Operational",
    "economic": "Economic",
    "cultural": "Cultural",
}


class ScoreError(ValueError):
    pass


def _require_yaml():
    try:
        import yaml  # type: ignore
    except ImportError as e:
        raise ScoreError(
            "PyYAML is required. Install with:\n"
            "  python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt"
        ) from e
    return yaml


def load_scores(path: Path) -> dict[str, Any]:
    yaml = _require_yaml()
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ScoreError(f"{path}: expected a YAML mapping at root")
    if "org_name" not in data or "layers" not in data:
        raise ScoreError(f"{path}: missing required keys org_name / layers")
    return data


def normalize_cell(value: Any) -> float | str | None:
    """Return float, 'NE', 'N/A', or None (unset)."""
    if value is None:
        return None
    if isinstance(value, bool):
        raise ScoreError(f"invalid boolean score cell: {value!r}")
    if isinstance(value, (int, float)):
        v = float(value)
        if not (0.0 <= v <= 5.0):
            raise ScoreError(f"score {v} out of range 0–5")
        return v
    if isinstance(value, str):
        s = value.strip()
        upper = s.upper().replace(" ", "")
        if upper in {"NE", "N/A", "NA", "NULL", "~"}:
            if upper == "NE":
                return "NE"
            return "N/A"
        try:
            v = float(s)
        except ValueError as e:
            raise ScoreError(f"unrecognized score cell: {value!r}") from e
        if not (0.0 <= v <= 5.0):
            raise ScoreError(f"score {v} out of range 0–5")
        return v
    raise ScoreError(f"unrecognized score cell type: {value!r}")


def is_numeric(cell: float | str | None) -> bool:
    return isinstance(cell, float)


def mean(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)


def round1(v: float) -> float:
    return round(v + 1e-12, 1)


@dataclass
class LayerLevelStats:
    average: float | None
    n_scored: int
    n_ne: int
    n_na: int
    n_unset: int
    values: list[float] = field(default_factory=list)


@dataclass
class ScoreSummary:
    org_name: str
    title: str
    scope_levels: list[str]
    # layer -> level -> stats
    layer_level: dict[str, dict[str, LayerLevelStats]]
    # layer -> average across in-scope levels that have scored cells
    # (for single-level assessments this equals that level's layer average)
    layer_averages: dict[str, float | None]
    layer_basis: dict[str, str]
    level_averages: dict[str, float | None]
    overall: float | None
    strongest_layer: tuple[str, float] | None
    weakest_layer: tuple[str, float] | None
    total_scored: int
    total_ne: int
    total_na: int
    total_unset: int


def compute_summary(data: dict[str, Any]) -> ScoreSummary:
    scope = [s.replace("-", "_") for s in data.get("scope_levels") or ["project"]]
    for s in scope:
        if s not in LEVELS:
            raise ScoreError(f"unknown scope level: {s}")

    layers = data["layers"]
    layer_level: dict[str, dict[str, LayerLevelStats]] = {}
    total_scored = total_ne = total_na = total_unset = 0

    for layer_key in LAYER_KEYS:
        if layer_key not in layers:
            raise ScoreError(f"missing layer: {layer_key}")
        layer = layers[layer_key]
        dims = layer.get("dimensions") or {}
        layer_level[layer_key] = {}
        for level in LEVELS:
            values: list[float] = []
            n_ne = n_na = n_unset = 0
            for dim_key, dim in dims.items():
                scores = (dim or {}).get("scores") or {}
                if level not in scores:
                    cell = None
                else:
                    cell = normalize_cell(scores[level])
                if cell is None:
                    n_unset += 1
                    if level in scope:
                        total_unset += 1
                elif cell == "NE":
                    n_ne += 1
                    if level in scope:
                        total_ne += 1
                elif cell == "N/A":
                    n_na += 1
                    if level in scope:
                        total_na += 1
                else:
                    values.append(cell)
                    if level in scope:
                        total_scored += 1
            layer_level[layer_key][level] = LayerLevelStats(
                average=round1(mean(values)) if values else None,
                n_scored=len(values),
                n_ne=n_ne,
                n_na=n_na,
                n_unset=n_unset,
                values=values,
            )

    # Primary layer average: for each layer, average of numeric cells across
    # in-scope levels (ChangePool-style: one level → that level's layer mean).
    layer_averages: dict[str, float | None] = {}
    layer_basis: dict[str, str] = {}
    for layer_key in LAYER_KEYS:
        vals: list[float] = []
        n_scored = n_ne = n_na = 0
        for level in scope:
            st = layer_level[layer_key][level]
            vals.extend(st.values)
            n_scored += st.n_scored
            n_ne += st.n_ne
            n_na += st.n_na
        avg = round1(mean(vals)) if vals else None
        layer_averages[layer_key] = avg
        parts = [f"{n_scored} scored"]
        if n_ne:
            parts.append(f"{n_ne} NE")
        if n_na:
            parts.append(f"{n_na} N/A")
        layer_basis[layer_key] = ", ".join(parts)

    # Level averages: mean of layer averages that exist for that level
    level_averages: dict[str, float | None] = {}
    for level in LEVELS:
        layer_avgs = [
            layer_level[lk][level].average
            for lk in LAYER_KEYS
            if layer_level[lk][level].average is not None
        ]
        level_averages[level] = round1(mean(layer_avgs)) if layer_avgs else None

    present = [(k, v) for k, v in layer_averages.items() if v is not None]
    overall = round1(mean([v for _, v in present])) if present else None
    strongest = max(present, key=lambda x: x[1]) if present else None
    weakest = min(present, key=lambda x: x[1]) if present else None

    return ScoreSummary(
        org_name=str(data["org_name"]),
        title=str(data.get("title") or data["org_name"]),
        scope_levels=scope,
        layer_level=layer_level,
        layer_averages=layer_averages,
        layer_basis=layer_basis,
        level_averages=level_averages,
        overall=overall,
        strongest_layer=strongest,
        weakest_layer=weakest,
        total_scored=total_scored,
        total_ne=total_ne,
        total_na=total_na,
        total_unset=total_unset,
    )


def format_summary_markdown(summary: ScoreSummary) -> str:
    lines = [
        "## Score Summary (secondary signals)",
        "",
        f"- Structural average: **{_fmt(summary.layer_averages['structural'])}** ({summary.layer_basis['structural']})",
        f"- Operational average: **{_fmt(summary.layer_averages['operational'])}** ({summary.layer_basis['operational']})",
        f"- Economic average: **{_fmt(summary.layer_averages['economic'])}** ({summary.layer_basis['economic']})",
        f"- Cultural/Ecosystem average: **{_fmt(summary.layer_averages['cultural'])}** ({summary.layer_basis['cultural']})",
        "- **Level averages** (average across layers, excluding NE/N/A):",
    ]
    for level, label in [
        ("project", "Project"),
        ("open_enterprise", "Open-Enterprise"),
        ("network", "Network"),
        ("global", "Global / inter-network"),
    ]:
        v = summary.level_averages[level]
        lines.append(f"  - {label}: {_fmt(v) if v is not None else 'N/A'}")
    lines.append(
        f"- Overall P2P-ness index (optional, secondary only): **{_fmt(summary.overall)} / 5**"
        if summary.overall is not None
        else "- Overall P2P-ness index (optional, secondary only): N/A"
    )
    if summary.strongest_layer:
        k, v = summary.strongest_layer
        lines.append(f"- Strongest layer(s) / level(s): **{LAYER_LABELS[k]}** ({v})")
    if summary.weakest_layer:
        k, v = summary.weakest_layer
        lines.append(f"- Weakest layer(s) / level(s): **{LAYER_LABELS[k]}** ({v})")
    lines.append(
        f"- Basis note: {summary.total_scored} cells scored, "
        f"{summary.total_ne} NE, {summary.total_na} N/A"
        + (f", {summary.total_unset} unset" if summary.total_unset else "")
        + "."
    )
    lines.append("")
    return "\n".join(lines)


def _fmt(v: float | None) -> str:
    if v is None:
        return "N/A"
    return f"{v:.1f}"


def patch_score_summary_section(markdown: str, new_block: str) -> str:
    """Replace an existing '## Score Summary...' section, or append it."""
    import re

    pattern = re.compile(
        r"## Score Summary \(secondary signals\).*?(?=\n---\n|\n## |\Z)",
        re.DOTALL,
    )
    if pattern.search(markdown):
        return pattern.sub(new_block.rstrip() + "\n\n", markdown, count=1)
    return markdown.rstrip() + "\n\n" + new_block + "\n"
