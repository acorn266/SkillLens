"""Reusable skill-gap calculations backed by the career intelligence layer."""

from typing import Dict, List

from src.career_data import get_required_skills
from src.skill_normalizer import normalize_skill_name


def _normalize_skill_levels(skills: Dict[str, int]) -> Dict[str, int]:
    """Normalize skill names and clamp levels to the 0-10 assessment scale."""

    normalized = {}

    for skill, level in (skills or {}).items():
        canonical = normalize_skill_name(skill)
        if not canonical:
            continue

        try:
            value = int(level)
        except (TypeError, ValueError):
            value = 0

        normalized[canonical] = max(0, min(value, 10))

    return normalized


def load_career_skills(
    csv_path: str | None = None,
    career: str | None = None,
) -> Dict[str, int]:
    """Load required skills from the authoritative career database.

    ``csv_path`` is retained for backward compatibility but is intentionally
    ignored. Career requirements must come from one source of truth.
    """

    # Support the historical positional call: load_career_skills(path, career)
    # while making the career argument the only value that affects the result.
    if career is None and isinstance(csv_path, str):
        # If a caller passes only a career name, treat it as the career.
        if not csv_path.lower().endswith(".csv"):
            career = csv_path

    if not career:
        raise ValueError("A career name is required.")

    return get_required_skills(career)


def calculate_skill_gaps(
    current: Dict[str, int],
    required: Dict[str, int],
) -> List[dict]:
    """Calculate transparent gaps between current and required skill levels."""

    current_normalized = _normalize_skill_levels(current)
    required_normalized = _normalize_skill_levels(required)
    rows = []

    for skill, req in required_normalized.items():
        cur = int(current_normalized.get(skill, 0))
        gap = max(req - cur, 0)

        if gap == 0:
            severity = "None"
        elif gap <= 2:
            severity = "Small"
        elif gap <= 4:
            severity = "Medium"
        else:
            severity = "Large"

        rows.append({
            "skill": skill,
            "current": cur,
            "required": req,
            "gap": gap,
            "severity": severity,
        })

    return sorted(rows, key=lambda x: x["gap"], reverse=True)


def calculate_total_gap(gaps: List[dict]) -> int:
    """Calculate the total skill gap."""

    return sum(item["gap"] for item in gaps)


def calculate_average_gap(gaps: List[dict]) -> float:
    """Calculate the average skill gap."""

    if not gaps:
        return 0.0

    return round(
        sum(item["gap"] for item in gaps) / len(gaps),
        2,
    )


def calculate_skill_match_percentage(
    current: Dict[str, int],
    required: Dict[str, int],
) -> float:
    """Calculate the average transparent skill-match percentage."""

    required_normalized = _normalize_skill_levels(required)
    current_normalized = _normalize_skill_levels(current)

    if not required_normalized:
        return 0.0

    scores = []

    for skill, req in required_normalized.items():
        cur = int(current_normalized.get(skill, 0))

        if req <= 0:
            score = 100.0
        else:
            score = min(cur / req, 1.0) * 100

        scores.append(score)

    return round(sum(scores) / len(scores), 2)


def analyze_career(
    career: str,
    current: Dict[str, int],
    csv_path: str | None = None,
) -> dict:
    """Perform a complete skill-gap analysis for a career."""

    required = load_career_skills(csv_path, career)
    gaps = calculate_skill_gaps(current, required)

    return {
        "career": career,
        "required_skills": required,
        "skill_gaps": gaps,
        "total_gap": calculate_total_gap(gaps),
        "average_gap": calculate_average_gap(gaps),
        "skill_match_percentage": calculate_skill_match_percentage(
            current, required
        ),
    }
