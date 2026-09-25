"""Career recommendation engine using the authoritative career database."""

from src.career_data import get_all_careers, get_required_skills
from src.skill_gap import (
    calculate_skill_gaps,
    calculate_skill_match_percentage,
)
from src.skill_normalizer import normalize_skill_name


def _normalize_current_skills(current: dict) -> dict:
    """Normalize learner skill names before comparing career profiles."""

    normalized = {}

    for skill, level in (current or {}).items():
        canonical = normalize_skill_name(skill)
        if not canonical:
            continue

        try:
            value = int(level)
        except (TypeError, ValueError):
            value = 0

        normalized[canonical] = max(0, min(value, 10))

    return normalized


def recommend_careers(current: dict) -> list[dict]:
    """Rank every supported career by transparent skill alignment."""

    current_normalized = _normalize_current_skills(current)
    recommendations = []

    for career in get_all_careers():
        required = get_required_skills(career)
        gaps = calculate_skill_gaps(current_normalized, required)
        match_percentage = calculate_skill_match_percentage(
            current_normalized,
            required,
        )

        recommendations.append({
            "career": career,
            "match_percentage": match_percentage,
            "total_gap": sum(gap["gap"] for gap in gaps),
            "skill_gaps": gaps,
        })

    recommendations.sort(
        key=lambda item: (
            item["match_percentage"],
            -item["total_gap"],
        ),
        reverse=True,
    )

    return recommendations
