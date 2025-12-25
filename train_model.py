# train_model.py
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from catboost import CatBoostClassifier
import shap
import joblib

# Paths
DATA_PATH = "data/neonatal_adr_top20_new.xlsx"
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

# Load and prepare dataset
def load_and_prepare(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_excel(path)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    expected_cols = ["suspect_product_active_ingredients", "reason_for_use",
                     "reactions", "outcomes", "sex", "patient_age", "patient_weight"]
    for col in expected_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df = df.dropna(subset=expected_cols)
    X = df[["suspect_product_active_ingredients", "reason_for_use", "sex",
            "patient_age", "patient_weight"]]
    y_reaction = df["reactions"]
    y_outcome = df["outcomes"]

    # Convert numeric columns
    for col in ["patient_age", "patient_weight"]:
        X[col] = pd.to_numeric(X[col], errors='coerce')
    X = X.fillna(0)

    # Label encode categorical features
    le_dict = {}
    for col in X.columns:
        if X[col].dtype == 'object':
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))
            le_dict[col] = le

    # Encode targets
    le_y_reaction = LabelEncoder()
    le_y_outcome = LabelEncoder()
    y_reaction = le_y_reaction.fit_transform(y_reaction)
    y_outcome = le_y_outcome.fit_transform(y_outcome)

    return X, y_reaction, y_outcome, le_dict, le_y_reaction, le_y_outcome

# Train models
def train_and_save(X, y_reaction, y_outcome, le_dict, le_y_reaction, le_y_outcome):
    X_train, X_test, y_reaction_train, y_reaction_test = train_test_split(X, y_reaction, test_size=0.2, random_state=42)
    _, _, y_outcome_train, y_outcome_test = train_test_split(X, y_outcome, test_size=0.2, random_state=42)

    print("Training CatBoost Reaction model...")
    model_reaction = CatBoostClassifier(iterations=200, depth=8, learning_rate=0.1, loss_function='MultiClass', verbose=False)
    model_reaction.fit(X_train, y_reaction_train)
    print("Reaction model trained ✅")

    print("Training CatBoost Outcome model...")
    model_outcome = CatBoostClassifier(iterations=200, depth=8, learning_rate=0.1, loss_function='MultiClass', verbose=False)
    model_outcome.fit(X_train, y_outcome_train)
    print("Outcome model trained ✅")

    # Save models
    joblib.dump(model_reaction, os.path.join(MODEL_DIR, "reaction_model.pkl"))
    joblib.dump(model_outcome, os.path.join(MODEL_DIR, "outcome_model.pkl"))
    joblib.dump(le_dict, os.path.join(MODEL_DIR, "label_encoders.pkl"))
    joblib.dump(le_y_reaction, os.path.join(MODEL_DIR, "le_y_reaction.pkl"))
    joblib.dump(le_y_outcome, os.path.join(MODEL_DIR, "le_y_outcome.pkl"))
    print("Models and encoders saved ✅")

    # SHAP explainers
    explainer_reaction = shap.TreeExplainer(model_reaction)
    shap_values_reaction = explainer_reaction.shap_values(X)
    joblib.dump((explainer_reaction, shap_values_reaction), os.path.join(MODEL_DIR, "xai_reaction.pkl"))

    explainer_outcome = shap.TreeExplainer(model_outcome)
    shap_values_outcome = explainer_outcome.shap_values(X)
    joblib.dump((explainer_outcome, shap_values_outcome), os.path.join(MODEL_DIR, "xai_outcome.pkl"))
    print("SHAP explainers saved ✅")

if __name__ == "__main__":
    X, y_reaction, y_outcome, le_dict, le_y_reaction, le_y_outcome = load_and_prepare(DATA_PATH)
    train_and_save(X, y_reaction, y_outcome, le_dict, le_y_reaction, le_y_outcome)
