"""Compatibility facade for the authoritative career intelligence layer."""

from src.career_intelligence import (
    get_all_careers,
    get_career_metadata,
    get_career_profile,
    get_required_skills,
    get_skill_requirements,
    load_career_intelligence,
)


__all__ = [
    "load_career_intelligence",
    "get_all_careers",
    "get_career_profile",
    "get_career_metadata",
    "get_required_skills",
    "get_skill_requirements",
]
