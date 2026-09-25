from src.career_recommender import recommend_careers


def test_recommendations_are_ranked_and_complete():
    current = {
        "Python": 8,
        "SQL": 5,
        "Statistics": 6,
        "Machine Learning": 7,
        "Data Visualization": 8,
    }

    recommendations = recommend_careers(current)

    assert len(recommendations) == 21
    assert all("match_percentage" in item for item in recommendations)
    assert all(0 <= item["match_percentage"] <= 100 for item in recommendations)
    assert all(
        recommendations[i]["match_percentage"]
        >= recommendations[i + 1]["match_percentage"]
        for i in range(len(recommendations) - 1)
    )
