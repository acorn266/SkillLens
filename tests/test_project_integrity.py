from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def test_authoritative_career_database_is_valid():
    path = ROOT / "data" / "processed" / "career_intelligence.csv"
    df = pd.read_csv(path)

    expected = {
        "Career",
        "Career_Category",
        "Career_Description",
        "Skill",
        "Skill_Category",
        "Required_Level",
        "Importance",
    }

    assert expected.issubset(df.columns)
    assert len(df) == 168
    assert df["Career"].nunique() == 21
    assert df["Skill"].notna().all()
    assert df["Required_Level"].between(0, 10).all()
    assert set(df["Importance"].unique()) <= {"Critical", "Important"}
