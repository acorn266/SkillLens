import pandas as pd
from pathlib import Path


# ---------------------------------------
# 1. Define file paths
# ---------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "raw"
    / "vocational_skill_job"
    / "Skill_Job_Matching_Dataset.csv"
)

OUTPUT_DIR = BASE_DIR / "data" / "processed"

OUTPUT_FILE = OUTPUT_DIR / "skill_job_cleaned.csv"


# ---------------------------------------
# 2. Load dataset
# ---------------------------------------

print("Loading dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Original dataset shape: {df.shape}")


# ---------------------------------------
# 3. Check missing values
# ---------------------------------------

print("\nMissing values:")

print(df.isnull().sum())


# ---------------------------------------
# 4. Remove duplicate rows
# ---------------------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate rows: {duplicates}")

df = df.drop_duplicates()

print(f"Shape after removing duplicates: {df.shape}")


# ---------------------------------------
# 5. Select useful columns
# ---------------------------------------

selected_columns = [
    "Age",
    "Gender",
    "Vocational_Program",
    "Academic_Performance",
    "Certifications_Count",
    "Internship_Experience",

    "Skill_1",
    "Skill_2",
    "Skill_3",
    "Skill_4",
    "Skill_5",

    "Job_Title",

    "Required_Skill_1",
    "Required_Skill_2",
    "Required_Skill_3",
    "Required_Skill_4",
    "Required_Skill_5",

    "Min_Experience_Months",
    "Location",

    "Job_Match"
]

df = df[selected_columns]


# ---------------------------------------
# 6. Convert categorical columns
# ---------------------------------------

categorical_columns = [
    "Gender",
    "Vocational_Program",
    "Job_Title",
    "Location"
]

for column in categorical_columns:
    df[column] = df[column].astype(str).str.strip()


# ---------------------------------------
# 7. Make sure numeric columns are numeric
# ---------------------------------------

numeric_columns = [
    "Age",
    "Academic_Performance",
    "Certifications_Count",
    "Internship_Experience",

    "Skill_1",
    "Skill_2",
    "Skill_3",
    "Skill_4",
    "Skill_5",

    "Required_Skill_1",
    "Required_Skill_2",
    "Required_Skill_3",
    "Required_Skill_4",
    "Required_Skill_5",

    "Min_Experience_Months",
    "Job_Match"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# ---------------------------------------
# 8. Remove rows with missing values
# ---------------------------------------

before_missing_removal = len(df)

df = df.dropna()

after_missing_removal = len(df)

print(
    f"\nRows removed because of missing values: "
    f"{before_missing_removal - after_missing_removal}"
)


# ---------------------------------------
# 9. Create processed directory
# ---------------------------------------

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------
# 10. Save cleaned dataset
# ---------------------------------------

df.to_csv(OUTPUT_FILE, index=False)

print("\nPreprocessing complete!")

print(f"Final dataset shape: {df.shape}")

print(f"Saved cleaned dataset to:")

print(OUTPUT_FILE)