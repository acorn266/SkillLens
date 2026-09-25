"""
Central Skill Normalization Engine

Keeps equivalent skill names consistent across:
    - Career profiles
    - Project intelligence
    - Roadmap learning intelligence
    - User skill assessments

The displayed skill name is never changed by this module.  It only creates
an internal canonical representation so that equivalent names can be matched.
"""

import re


# ---------------------------------------------------------------------------
# Canonical aliases
# ---------------------------------------------------------------------------
# Keys are normalized text forms; values are the canonical skill names used
# internally by the application.

SKILL_ALIASES = {
    # Python / programming
    "python 3": "Python",
    "python programming": "Python",

    # Machine learning / AI
    "ml": "Machine Learning",
    "machine-learning": "Machine Learning",
    "machine learning": "Machine Learning",
    "ai": "Artificial Intelligence",
    "artificial intelligence": "Artificial Intelligence",
    "dl": "Deep Learning",
    "deep-learning": "Deep Learning",

    # APIs
    "api": "APIs",
    "apis": "APIs",
    "api development": "APIs",
    "api development and integration": "APIs",
    "rest api": "APIs",
    "rest apis": "APIs",
    "restful api": "APIs",
    "restful apis": "APIs",

    # Data visualization
    "data viz": "Data Visualization",
    "data visualisation": "Data Visualization",
    "data visualizations": "Data Visualization",
    "data visualisations": "Data Visualization",
    "data visualization": "Data Visualization",

    # Data manipulation
    "pandas dataframe": "Pandas",
    "pandas dataframes": "Pandas",
    "numpy/pandas": "Pandas",

    # ETL
    "etl": "ETL/ELT",
    "elt": "ETL/ELT",
    "etl/elt": "ETL/ELT",
    "etl & elt": "ETL/ELT",
    "etl and elt": "ETL/ELT",

    # Cloud platforms
    "aws": "Cloud Platforms",
    "amazon web services": "Cloud Platforms",
    "aws cloud": "Cloud Platforms",
    "azure": "Cloud Platforms",
    "microsoft azure": "Cloud Platforms",
    "gcp": "Cloud Platforms",
    "google cloud": "Cloud Platforms",
    "google cloud platform": "Cloud Platforms",
    "aws/azure/gcp": "Cloud Platforms",
    "aws azure gcp": "Cloud Platforms",
    "aws, azure, gcp": "Cloud Platforms",
    "cloud platform": "Cloud Platforms",
    "cloud platforms": "Cloud Platforms",

    # Cloud / deployment
    "cloud": "Cloud Computing",
    "cloud computing": "Cloud Computing",
    "cloud deployment": "Cloud Deployment",
    "model deployment": "Model Deployment",
    "model serving": "Model Deployment",
    "deployment": "Deployment",

    # Version control
    "version control": "Git",
    "git version control": "Git",
    "github/git": "Git",

    # Databases
    "database": "Databases",
    "databases": "Databases",
    "database design": "Database Design",
    "database management": "Database Management",

    # Backup / recovery
    "backup and recovery": "Backup & Recovery",
    "backup/recovery": "Backup & Recovery",
    "backup recovery": "Backup & Recovery",

    # Testing
    "software test": "Software Testing",
    "software tests": "Software Testing",
    "software testing": "Software Testing",
    "automated testing": "Test Automation",
    "test automation": "Test Automation",
    "api test": "API Testing",
    "api tests": "API Testing",
    "api testing": "API Testing",

    # UI/UX
    "ui": "UI Design",
    "ui design": "UI Design",
    "ux": "UX Design",
    "ux design": "UX Design",
    "ui ux": "UI/UX Fundamentals",
    "ui/ux": "UI/UX Fundamentals",
    "ui ux fundamentals": "UI/UX Fundamentals",
    "ui/ux fundamentals": "UI/UX Fundamentals",

    # HTML/CSS
    "html css": "HTML/CSS",
    "html/css": "HTML/CSS",
    "html & css": "HTML/CSS",
    "html and css": "HTML/CSS",

    # TensorFlow / PyTorch
    "tensorflow": "TensorFlow/PyTorch",
    "pytorch": "TensorFlow/PyTorch",
    "tensorflow pytorch": "TensorFlow/PyTorch",
    "tensorflow/pytorch": "TensorFlow/PyTorch",

    # Common abbreviations
    "oop": "Object-Oriented Programming",
    "object oriented programming": "Object-Oriented Programming",
    "object-oriented programming": "Object-Oriented Programming",
}


def _clean_skill_name(skill_name):
    """Create a stable comparison form without changing the meaning."""

    if skill_name is None:
        return ""

    value = str(skill_name).strip().lower()

    # Normalize common separators while preserving slash-separated concepts
    # long enough for explicit aliases such as HTML/CSS and AWS/Azure/GCP.
    value = value.replace("–", "-").replace("—", "-")
    value = value.replace("&", " and ")
    value = re.sub(r"\s+", " ", value)
    value = re.sub(r"\s*/\s*", "/", value)
    value = re.sub(r"\s*-\s*", "-", value)
    return value.strip()


def normalize_skill_name(skill_name):
    """Return the canonical internal name for a skill."""

    cleaned = _clean_skill_name(skill_name)

    if not cleaned:
        return ""

    if cleaned in SKILL_ALIASES:
        return SKILL_ALIASES[cleaned]

    # Handle punctuation-insensitive variants after the direct alias lookup.
    compact = re.sub(r"[^a-z0-9]+", " ", cleaned).strip()
    compact_aliases = {
        re.sub(r"[^a-z0-9]+", " ", key).strip(): value
        for key, value in SKILL_ALIASES.items()
    }

    if compact in compact_aliases:
        return compact_aliases[compact]

    return str(skill_name).strip()


def skills_match(first_skill, second_skill):
    """Return True when two skill names represent the same canonical skill."""

    first = normalize_skill_name(first_skill)
    second = normalize_skill_name(second_skill)

    if not first or not second:
        return False

    return first.casefold() == second.casefold()


def normalize_skill_list(skills):
    """Normalize a list of skill names and remove canonical duplicates."""

    result = []
    seen = set()

    for skill in skills or []:
        canonical = normalize_skill_name(skill)
        key = canonical.casefold()

        if canonical and key not in seen:
            seen.add(key)
            result.append(canonical)

    return result


# Useful for debugging/tests and for showing the normalization logic clearly.
def get_skill_aliases():
    """Return a copy of the configured alias mapping."""

    return dict(SKILL_ALIASES)
