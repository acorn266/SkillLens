from src.skill_normalizer import normalize_skill_name, skills_match


def test_aliases():
    assert normalize_skill_name("ML") == "Machine Learning"
    assert normalize_skill_name("APIs") == "APIs"
    assert normalize_skill_name("API Development") == "APIs"
    assert normalize_skill_name("Data Visualisation") == "Data Visualization"
    assert normalize_skill_name("ETL") == "ETL/ELT"
    assert normalize_skill_name("AWS/Azure/GCP") == "Cloud Platforms"
    assert normalize_skill_name("Version Control") == "Git"
    assert normalize_skill_name("Backup and Recovery") == "Backup & Recovery"


def test_equivalent_skills_match():
    assert skills_match("ML", "Machine Learning")
    assert skills_match("Data Viz", "Data Visualization")
    assert skills_match("API", "APIs")
    assert skills_match("AWS", "Cloud Platforms")


if __name__ == "__main__":
    test_aliases()
    test_equivalent_skills_match()
    print("Skill normalization tests passed.")
