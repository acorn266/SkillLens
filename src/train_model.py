from pathlib import Path

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)
import joblib


# ============================================================
# 1. LOAD CLEANED DATASET
# ============================================================

print("Loading cleaned dataset...")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "skill_job_cleaned.csv"

df = pd.read_csv(DATA_PATH)

print(f"Dataset shape: {df.shape}")


# ============================================================
# 2. CREATE SKILL GAP FEATURES
# ============================================================

print("\nCreating skill gap features...")

skill_columns = [
    "Skill_1",
    "Skill_2",
    "Skill_3",
    "Skill_4",
    "Skill_5"
]

required_skill_columns = [
    "Required_Skill_1",
    "Required_Skill_2",
    "Required_Skill_3",
    "Required_Skill_4",
    "Required_Skill_5"
]

gap_columns = []

for skill, required in zip(skill_columns, required_skill_columns):
    gap_name = skill.replace("Skill_", "Skill_Gap_")
    df[gap_name] = (df[required] - df[skill]).clip(lower=0)

    gap_columns.append(gap_name)


# Total and average skill gap

df["Total_Skill_Gap"] = df[gap_columns].sum(axis=1)

df["Average_Skill_Gap"] = df[gap_columns].mean(axis=1)


print("Created:")
print(gap_columns)
print("Total_Skill_Gap")
print("Average_Skill_Gap")


# ============================================================
# 3. SELECT FEATURES
# ============================================================

features = [
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

    "Required_Skill_1",
    "Required_Skill_2",
    "Required_Skill_3",
    "Required_Skill_4",
    "Required_Skill_5",

    "Min_Experience_Months",
    "Location",

    "Skill_Gap_1",
    "Skill_Gap_2",
    "Skill_Gap_3",
    "Skill_Gap_4",
    "Skill_Gap_5",

    "Total_Skill_Gap",
    "Average_Skill_Gap"
]

target = "Job_Match"


X = df[features]

y = df[target]


print("\nFeature matrix shape:", X.shape)
print("Target shape:", y.shape)


# ============================================================
# 4. IDENTIFY FEATURE TYPES
# ============================================================

categorical_features = [
    "Gender",
    "Vocational_Program",
    "Location"
]

numeric_features = [
    feature
    for feature in features
    if feature not in categorical_features
]


# ============================================================
# 5. PREPROCESSING
# ============================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numeric",
            "passthrough",
            numeric_features
        )
    ]
)


# ============================================================
# 6. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ============================================================
# 7. CREATE RANDOM FOREST MODEL
# ============================================================

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced",
    max_depth=None,
    min_samples_split=2,
    n_jobs=-1
)


# ============================================================
# 8. CREATE COMPLETE ML PIPELINE
# ============================================================

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# ============================================================
# 9. TRAIN MODEL
# ============================================================

print("\nTraining Random Forest model...")

pipeline.fit(X_train, y_train)

print("Model training completed!")


# ============================================================
# 10. MAKE PREDICTIONS
# ============================================================

y_pred = pipeline.predict(X_test)

y_probability = pipeline.predict_proba(X_test)[:, 1]


# ============================================================
# 11. MODEL EVALUATION
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

roc_auc = roc_auc_score(
    y_test,
    y_probability
)

print("\n===================================")
print("MODEL PERFORMANCE")
print("===================================")

print(f"Accuracy: {accuracy:.4f}")

print(f"ROC-AUC: {roc_auc:.4f}")


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)


print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


# ============================================================
# 12. SAVE TRAINED MODEL
# ============================================================

MODEL_PATH = BASE_DIR / "models" / "skill_gap_model.joblib"

MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

joblib.dump(
    pipeline,
    MODEL_PATH
)

print("\n===================================")
print("MODEL SAVED")
print("===================================")

print(f"Saved model to: {MODEL_PATH}")