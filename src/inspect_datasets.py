from pathlib import Path
import ast
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

job_path = ROOT / "data/raw/job_skill_set/all_job_post.csv"
match_path = ROOT / "data/raw/vocational_skill_job/Skill_Job_Matching_Dataset.csv"

jobs = pd.read_csv(job_path)
match = pd.read_csv(match_path)

print("\n=== JOB SKILL SET ===")
print("Shape:", jobs.shape)
print("Columns:", jobs.columns.tolist())
print("\nCategories:")
print(jobs["category"].value_counts())
print("\nUnique job titles:", jobs["job_title"].nunique())
print("\nMissing values:")
print(jobs.isna().sum())

print("\n=== VOCATIONAL MATCHING ===")
print("Shape:", match.shape)
print("Columns:", match.columns.tolist())
print("\nPrograms:", match["Vocational_Program"].value_counts().to_dict())
print("\nJobs:", match["Job_Title"].value_counts().to_dict())
print("\nJob_Match distribution:")
print(match["Job_Match"].value_counts())

print("\nNote: Required_Skill_* and Skill_* are numeric IDs/scores in this dataset.")
