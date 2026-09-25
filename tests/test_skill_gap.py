from src.skill_gap import analyze_career


def test_data_scientist_skill_gap_analysis():
    current = {
        "Python": 8,
        "SQL": 5,
        "Statistics": 6,
        "Machine Learning": 7,
        "Data Visualization": 8,
    }

    result = analyze_career("Data Scientist", current)

    assert result["career"] == "Data Scientist"
    assert result["skill_match_percentage"] > 0
    assert result["total_gap"] > 0
    assert len(result["skill_gaps"]) == 8
