"""Flask web application for the Skill Gap Predictor."""

import logging
import os
import re

from flask import Flask, redirect, render_template, request, url_for

from src.career_data import get_all_careers, get_career_metadata, get_career_profile
from src.reality_check import (
    analyze_skills,
    calculate_critical_alignment,
    calculate_readiness,
    get_critical_gaps,
    get_gaps,
    get_readiness_label,
    get_reality_message,
    get_severe_critical_gaps,
    get_strengths,
)
from src.roadmap import generate_roadmap


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 64 * 1024

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def skill_field_name(skill_name: str) -> str:
    """Convert a skill name into a safe, deterministic form-field suffix."""
    normalized = re.sub(r"[^a-z0-9]+", "_", str(skill_name).lower()).strip("_")
    return normalized or "skill"


def _parse_skill_level(value) -> int:
    """Parse and clamp a submitted skill level to the 0-10 range."""
    try:
        return max(0, min(int(value), 10))
    except (TypeError, ValueError):
        return 0


@app.context_processor
def inject_template_helpers():
    """Expose small presentation helpers to Jinja templates."""
    return {"skill_field_name": skill_field_name}


@app.route("/")
def index():
    return render_template("index.html", careers=get_all_careers())


@app.route("/assessment")
def assessment():
    career = request.args.get("career", "").strip()
    if not career:
        return redirect(url_for("index"))

    skills = get_career_profile(career)
    career_metadata = get_career_metadata(career)

    if not skills or not career_metadata:
        return redirect(url_for("index"))

    return render_template(
        "assessment.html",
        career=career,
        skills=skills,
        career_metadata=career_metadata,
    )


@app.route("/results", methods=["POST"])
def results():
    career = request.form.get("career", "").strip()
    if not career:
        return redirect(url_for("index"))

    career_profile = get_career_profile(career)
    if not career_profile:
        return redirect(url_for("index"))

    skill_results = []
    for skill in career_profile:
        skill_name = skill["Skill"]
        field_name = f"skill_{skill_field_name(skill_name)}"
        skill_results.append(
            {
                "skill": skill_name,
                "current_level": _parse_skill_level(request.form.get(field_name)),
                "required_level": int(skill["Required_Level"]),
                "importance": skill["Importance"],
            }
        )

    analyzed = analyze_skills(skill_results)
    readiness = calculate_readiness(analyzed)
    critical_alignment = calculate_critical_alignment(analyzed)
    critical_gaps = get_critical_gaps(analyzed)
    severe_critical_gaps = get_severe_critical_gaps(analyzed)

    return render_template(
        "results.html",
        career=career,
        readiness=readiness,
        readiness_label=get_readiness_label(
            readiness, critical_alignment, len(severe_critical_gaps)
        ),
        reality_message=get_reality_message(
            readiness, critical_alignment, critical_gaps, severe_critical_gaps
        ),
        critical_alignment=critical_alignment,
        critical_gaps=critical_gaps,
        severe_critical_gaps=severe_critical_gaps,
        skill_results=analyzed,
        strengths=get_strengths(analyzed),
        gaps=get_gaps(analyzed),
        roadmap=generate_roadmap(analyzed, career),
    )


@app.errorhandler(404)
def not_found(error):
    return render_template(
        "error.html",
        code=404,
        message="The page you requested was not found.",
    ), 404


@app.errorhandler(413)
def request_too_large(error):
    return render_template(
        "error.html",
        code=413,
        message="The submitted request is too large.",
    ), 413


@app.errorhandler(500)
def internal_error(error):
    logger.exception("Unhandled application error")
    return render_template(
        "error.html",
        code=500,
        message="Something went wrong while generating your career report. Please try again.",
    ), 500


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug)
