from src.career_data import get_all_careers, get_career_profile
from src.roadmap import generate_roadmap


def test_every_career_generates_a_complete_roadmap():
    careers = get_all_careers()
    assert len(careers) == 21

    for career in careers:
        profile = get_career_profile(career)
        assessed = [
            {
                "skill": item["Skill"],
                "current_level": 5,
                "required_level": int(item["Required_Level"]),
                "importance": item["Importance"],
            }
            for item in profile
        ]

        roadmap = generate_roadmap(assessed, career)

        assert len(roadmap) == 5
        assert roadmap[0]["title"]
        assert len(roadmap[2]["projects"]) == 3
        assert all(project["title"] for project in roadmap[2]["projects"])
