from src.skill_intelligence import get_skill_intelligence
from src.project_intelligence import recommend_projects

"""
Personalized Career Roadmap Engine

This module converts a user's career skill assessment
into a practical, career-specific development roadmap.

The roadmap is based on:
    - Current skill level
    - Required skill level
    - Skill importance
    - Career selected by the user
    - Skill-specific learning intelligence
    - Gap-driven project recommendations

Learning stages:
    1. Beginner
    2. Intermediate
    3. Advanced

The learner's current self-assessed level determines
which learning stage is recommended.
"""


# ============================================================
# LEGACY SKILL LEARNING GUIDANCE
# ============================================================
#
# Kept here for compatibility/reference.
#
# The actual roadmap now uses the richer intelligence layer
# from src/skill_intelligence.py.
#
# ============================================================

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_skill_guidance(skill_name):
    """
    Return structured learning guidance for a skill.

    The roadmap uses the learner's current skill level
    to determine which learning stage should be emphasized.

    Returns:
        dict:
            description
            beginner
            intermediate
            advanced
            practice
    """

    intelligence = get_skill_intelligence(skill_name)

    return {
        "description": intelligence["description"],
        "beginner": intelligence["beginner"],
        "intermediate": intelligence["intermediate"],
        "advanced": intelligence["advanced"],
        "practice": intelligence["practice"]
    }


def get_learning_stage(current_level):
    """
    Determine the appropriate learning stage based on
    the learner's current self-assessed skill level.

    Levels:
        1-3  -> Beginner
        4-6  -> Intermediate
        7-10 -> Advanced

    Returns:
        str: beginner / intermediate / advanced
    """

    try:
        current_level = int(current_level)
    except (TypeError, ValueError):
        current_level = 0

    if current_level <= 3:
        return "beginner"

    if current_level <= 6:
        return "intermediate"

    return "advanced"


def create_learning_action(skill):
    """
    Create a personalized learning action for one skill.

    The learner's current level determines whether the roadmap
    recommends beginner, intermediate, or advanced learning content.
    """

    skill_name = skill["skill"]
    current_level = skill["current_level"]

    learning_stage = get_learning_stage(current_level)

    guidance = get_skill_guidance(skill_name)

    return {
        "skill": skill_name,
        "description": guidance["description"],
        "topics": guidance[learning_stage],
        "practice": guidance["practice"],
        "stage": learning_stage,
        "current_level": current_level,
        "required_level": skill["required_level"],
        "gap": skill["gap"],
        "importance": skill["importance"]
    }


def remove_duplicate_skills(skills):
    """
    Remove duplicate skills while preserving their original order.
    """

    seen = set()
    unique_skills = []

    for skill in skills:

        skill_name = skill["skill"]

        if skill_name not in seen:
            seen.add(skill_name)
            unique_skills.append(skill)

    return unique_skills


# ============================================================
# ROADMAP GENERATOR
# ============================================================

def generate_roadmap(skill_results, career):
    """
    Generate a personalized roadmap based on:

        - Current skill levels
        - Required skill levels
        - Skill importance
        - Selected career

    Returns:
        list of roadmap phases
    """

    # --------------------------------------------------------
    # Calculate skill gaps
    # --------------------------------------------------------

    skills = []

    for skill in skill_results:

        skill_copy = skill.copy()

        try:
            current_level = int(skill_copy["current_level"])
        except (TypeError, ValueError):
            current_level = 0

        try:
            required_level = int(skill_copy["required_level"])
        except (TypeError, ValueError):
            required_level = 0

        skill_copy["current_level"] = max(
            0,
            min(current_level, 10)
        )

        skill_copy["required_level"] = max(
            0,
            min(required_level, 10)
        )

        skill_copy["gap"] = max(
            skill_copy["required_level"]
            - skill_copy["current_level"],
            0
        )

        skills.append(skill_copy)

    # --------------------------------------------------------
    # Separate skills with gaps
    # --------------------------------------------------------

    gaps = [
        skill
        for skill in skills
        if skill["gap"] > 0
    ]

    # Critical skills first.
    # Within the same importance level, larger gaps first.

    gaps.sort(
        key=lambda x: (
            0 if x["importance"] == "Critical" else 1,
            -x["gap"]
        )
    )

    # --------------------------------------------------------
    # Critical and important gaps
    # --------------------------------------------------------

    critical_gaps = [
        skill
        for skill in gaps
        if skill["importance"] == "Critical"
    ]

    important_gaps = [
        skill
        for skill in gaps
        if skill["importance"] == "Important"
    ]

    # --------------------------------------------------------
    # Strong skills
    # --------------------------------------------------------

    strengths = [
        skill
        for skill in skills
        if skill["gap"] == 0
    ]

    # ========================================================
    # PHASE 1
    # ========================================================

    phase_1_skills = (
        critical_gaps[:3]
        if critical_gaps
        else important_gaps[:3]
    )

    phase_1 = {
        "phase": "Phase 1",
        "title": "Close Your Highest-Priority Skill Gaps",
        "description": (
            "Start with the skills that currently create the "
            "largest gap between your profile and the target "
            "career. Critical skills are prioritized first."
        ),
        "skills": phase_1_skills,
        "actions": []
    }

    for skill in phase_1_skills:

        action = create_learning_action(skill)

        phase_1["actions"].append(action)

    # ========================================================
    # PHASE 2
    # ========================================================

    phase_2_candidates = (
        critical_gaps[3:]
        + important_gaps
    )

    phase_2_candidates = remove_duplicate_skills(
        phase_2_candidates
    )

    phase_2_candidates.sort(
        key=lambda x: (
            0 if str(x.get("importance", "")).lower() == "critical" else 1,
            -x.get("gap", 0),
        )
    )

    phase_2_skills = phase_2_candidates[:4]

    phase_2 = {
        "phase": "Phase 2",
        "title": "Strengthen Your Career Foundation",
        "description": (
            "After addressing your biggest weaknesses, "
            "strengthen the supporting skills that help "
            "you perform effectively in your target role."
        ),
        "skills": phase_2_skills,
        "actions": []
    }

    for skill in phase_2_skills:

        action = create_learning_action(skill)

        phase_2["actions"].append(action)

    # ========================================================
    # PHASE 3 — INTELLIGENT PROJECT RECOMMENDATIONS
    # ========================================================

    projects = recommend_projects(
        career,
        skills,
        limit=3
    )

    phase_3 = {
        "phase": "Phase 3",
        "title": "Build Career-Ready Projects",
        "description": (
            f"These projects are selected for your {career} goal "
            "and ranked by how strongly they address the skill gaps "
            "found in your assessment."
        ),
        "skills": [],
        "projects": projects
    }

    # ========================================================
    # PHASE 4 — CAREER PREPARATION
    # ========================================================

    phase_4 = {
        "phase": "Phase 4",
        "title": "Build Your Professional Profile",
        "description": (
            "Turn your learning into evidence that employers "
            "can evaluate."
        ),
        "skills": [],
        "actions": [
            "Create a professional GitHub portfolio.",
            "Document your strongest projects clearly.",
            "Write a career-focused CV.",
            "Prepare a strong LinkedIn profile.",
            "Practice technical and behavioral interviews.",
            "Be prepared to explain the decisions behind your projects."
        ]
    }

    # ========================================================
    # PHASE 5 — FINAL READINESS
    # ========================================================

    remaining_gaps = gaps

    phase_5 = {
        "phase": "Phase 5",
        "title": "Become Career Ready",
        "description": (
            "Review your remaining skill gaps, strengthen "
            "your portfolio, and begin applying your skills "
            "to realistic career opportunities."
        ),
        "skills": remaining_gaps,
        "actions": [
            "Reassess your skills against the career profile.",
            "Close any remaining critical gaps.",
            "Build one polished capstone project.",
            "Practice realistic interview questions.",
            (
                "Start applying for relevant internships, "
                "freelance work, or entry-level opportunities."
            )
        ]
    }

    # ========================================================
    # RETURN COMPLETE ROADMAP
    # ========================================================

    return [
        phase_1,
        phase_2,
        phase_3,
        phase_4,
        phase_5
    ]