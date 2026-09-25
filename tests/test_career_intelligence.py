from src.career_data import (
    get_all_careers,
    get_career_metadata,
    get_career_profile,
    get_required_skills,
    get_skill_requirements,
)


def test_authoritative_database():
    careers = get_all_careers()

    assert len(careers) == 21
    assert "Data Scientist" in careers
    assert "Data Analyst" in careers


def test_career_profile_is_complete():
    profile = get_career_profile("Data Scientist")

    assert profile is not None
    assert len(profile) == 8
    assert profile[0]["Career"] == "Data Scientist"
    assert all("Importance" in item for item in profile)
    assert all("Skill_Category" in item for item in profile)


def test_career_metadata():
    metadata = get_career_metadata("Data Scientist")

    assert metadata["career"] == "Data Scientist"
    assert metadata["skill_count"] == 8
    assert metadata["critical_skill_count"] == 4
    assert metadata["description"]


def test_required_skills_use_authoritative_levels():
    required = get_required_skills("Data Scientist")

    assert required["Python"] == 9
    assert required["SQL"] == 8
    assert required["Statistics"] == 9
    assert required["Machine Learning"] == 9


def test_skill_requirements_include_intelligence_fields():
    requirements = get_skill_requirements("Data Scientist")

    python_skill = next(
        item for item in requirements if item["skill"] == "Python"
    )

    assert python_skill["required_level"] == 9
    assert python_skill["importance"] == "Critical"
    assert python_skill["skill_category"] == "Programming"


if __name__ == "__main__":
    test_authoritative_database()
    test_career_profile_is_complete()
    test_career_metadata()
    test_required_skills_use_authoritative_levels()
    test_skill_requirements_include_intelligence_fields()
    print("Career intelligence tests passed.")
