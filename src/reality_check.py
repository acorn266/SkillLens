def calculate_skill_score(current_level, required_level):
    """Calculate how closely the current skill matches its required level."""
    try:
        current_level = float(current_level)
    except (TypeError, ValueError):
        current_level = 0
    try:
        required_level = float(required_level)
    except (TypeError, ValueError):
        required_level = 0
    if required_level <= 0:
        return 100
    score = (current_level / required_level) * 100
    return min(max(score, 0), 100)


def calculate_readiness(skill_results):
    """Calculate weighted overall skill readiness."""
    total_weight = 0
    weighted_score = 0
    for skill in skill_results:
        score = calculate_skill_score(skill.get("current_level", 0), skill.get("required_level", 0))
        weight = 1.5 if str(skill.get("importance", "")).lower() == "critical" else 1.0
        weighted_score += score * weight
        total_weight += weight
    if total_weight == 0:
        return 0
    return round(weighted_score / total_weight, 1)


def calculate_critical_alignment(skill_results):
    """Calculate average alignment across Critical skills only."""
    critical_skills = [s for s in skill_results if str(s.get("importance", "")).lower() == "critical"]
    if not critical_skills:
        return 100.0
    scores = [calculate_skill_score(s.get("current_level", 0), s.get("required_level", 0)) for s in critical_skills]
    return round(sum(scores) / len(scores), 1)


def get_critical_gaps(skill_results):
    """Return Critical skills that are below their required level."""
    return sorted(
        [s for s in skill_results if str(s.get("importance", "")).lower() == "critical" and s.get("gap", 0) > 0],
        key=lambda s: -s.get("gap", 0),
    )


def get_severe_critical_gaps(skill_results):
    """Return Critical skills with a substantial readiness deficit."""
    severe = []
    for skill in skill_results:
        if str(skill.get("importance", "")).lower() != "critical":
            continue
        score = calculate_skill_score(skill.get("current_level", 0), skill.get("required_level", 0))
        gap = max(float(skill.get("required_level", 0)) - float(skill.get("current_level", 0)), 0)
        if gap >= 4 or score < 50:
            severe.append(skill)
    return sorted(severe, key=lambda s: -s.get("gap", 0))


def get_readiness_label(score, critical_alignment=None, severe_critical_count=0):
    """Return readiness label using overall and Critical-skill evidence."""
    score = float(score or 0)
    critical_alignment = 100.0 if critical_alignment is None else float(critical_alignment)
    if severe_critical_count > 0 or critical_alignment < 50:
        if score < 40:
            return "Major Gap"
        if score < 60:
            return "Early Foundation"
        return "Critical Gaps"
    if score < 40:
        return "Major Gap"
    if score < 60:
        return "Early Foundation"
    if score < 75:
        return "Developing"
    if score < 90:
        return "Near Ready"
    return "Strong Alignment"


def get_reality_message(score, critical_alignment=None, critical_gaps=None, severe_critical_gaps=None):
    """Generate an evidence-based explanation of the readiness result."""
    score = float(score or 0)
    critical_alignment = 100.0 if critical_alignment is None else float(critical_alignment)
    critical_gaps = critical_gaps or []
    severe_critical_gaps = severe_critical_gaps or []

    if severe_critical_gaps:
        names = ", ".join(s.get("skill", "Critical skill") for s in severe_critical_gaps[:2])
        if len(severe_critical_gaps) > 2:
            names += " and more"
        return (f"Your overall alignment is {score:.1f}%, but {names} still represent substantial Critical gaps. "
                "Strengthen these skills before treating yourself as career-ready.")
    if critical_gaps and critical_alignment < 75:
        names = ", ".join(s.get("skill", "Critical skill") for s in critical_gaps[:2])
        if len(critical_gaps) > 2:
            names += " and more"
        return (f"Your overall alignment is {score:.1f}%, while Critical-skill alignment is {critical_alignment:.1f}%. "
                f"Prioritize {names} before focusing heavily on lower-priority skills.")
    if score < 40:
        return ("You currently have significant gaps between your skills and the defined requirements for this career. "
                "Focus on the fundamentals and the largest Critical gaps first.")
    if score < 60:
        return ("You have started building relevant skills, but several areas still need substantial improvement. "
                "Follow the roadmap in priority order rather than trying to learn everything at once.")
    if score < 75:
        return ("You have a developing foundation. Your next step is to close the highest-priority gaps and turn "
                "those skills into practical project experience.")
    if score < 90:
        return ("You are relatively close to the defined skill profile. Target your remaining gaps, especially any "
                "Critical ones, and strengthen your practical experience.")
    return ("Your self-assessed skills strongly align with the defined skill profile. Focus next on substantial "
            "projects, portfolio quality, interview preparation, and validating your skills with real work.")


def classify_skill_gap(current_level, required_level, importance):
    """Classify the severity of an individual skill gap."""
    gap = max(required_level - current_level, 0)
    if gap == 0:
        return "Strong"
    if str(importance).lower() == "critical":
        if gap >= 4:
            return "Critical Gap"
        if gap >= 2:
            return "High Priority"
        return "Development Area"
    if gap >= 4:
        return "High Priority"
    return "Development Area"


def analyze_skills(skill_results):
    """Add gap, alignment score, and status to every skill."""
    analyzed = []
    for skill in skill_results:
        current = skill.get("current_level", 0)
        required = skill.get("required_level", 0)
        importance = skill.get("importance", "Important")
        gap = max(required - current, 0)
        score = calculate_skill_score(current, required)
        analyzed_skill = skill.copy()
        analyzed_skill["gap"] = gap
        analyzed_skill["score"] = round(score, 1)
        analyzed_skill["status"] = classify_skill_gap(current, required, importance)
        analyzed.append(analyzed_skill)
    return analyzed


def get_priority_skills(skill_results):
    """Return skills ordered by importance and gap size."""
    return sorted(skill_results, key=lambda s: (0 if str(s.get("importance", "")).lower() == "critical" else 1, -s.get("gap", 0)))


def get_strengths(skill_results):
    """Return skills where the learner meets or exceeds the requirement."""
    return sorted([s for s in skill_results if s.get("current_level", 0) >= s.get("required_level", 0)], key=lambda s: s.get("score", 0), reverse=True)


def get_gaps(skill_results):
    """Return all unmet skills, prioritizing Critical gaps."""
    return sorted([s for s in skill_results if s.get("gap", 0) > 0], key=lambda s: (0 if str(s.get("importance", "")).lower() == "critical" else 1, -s.get("gap", 0)))
