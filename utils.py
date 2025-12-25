# utils.py
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load all models
def load_all_models():
    model_files = ["reaction_model.pkl", "outcome_model.pkl",
                   "label_encoders.pkl", "le_y_reaction.pkl",
                   "le_y_outcome.pkl", "xai_reaction.pkl", "xai_outcome.pkl"]
    for f in model_files:
        if not os.path.exists(f"models/{f}"):
            raise FileNotFoundError(f"Missing model file: models/{f}")

    return {
        "reaction_model": joblib.load("models/reaction_model.pkl"),
        "outcome_model": joblib.load("models/outcome_model.pkl"),
        "le_dict": joblib.load("models/label_encoders.pkl"),
        "le_y_reaction": joblib.load("models/le_y_reaction.pkl"),
        "le_y_outcome": joblib.load("models/le_y_outcome.pkl"),
        "xai_reaction": joblib.load("models/xai_reaction.pkl"),
        "xai_outcome": joblib.load("models/xai_outcome.pkl"),
    }

# Preprocess input
def preprocess_input(form_data, le_dict):
    df = pd.DataFrame([form_data], columns=[
        "suspect_product_active_ingredients",
        "reason_for_use",
        "sex",
        "patient_age",
        "patient_weight"
    ])
    for col in df.columns:
        if col in le_dict:
            le = le_dict[col]
            val = str(df[col][0])
            if val not in le.classes_:
                le.classes_ = np.append(le.classes_, val)
            df[col] = le.transform(df[col])
        else:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    return df

# Predict reaction and outcome
def predict_reaction_outcome(df, models):
    reaction_pred = models["reaction_model"].predict(df)[0]
    outcome_pred = models["outcome_model"].predict(df)[0]
    reaction_prob = np.max(models["reaction_model"].predict_proba(df)) * 100
    outcome_prob = np.max(models["outcome_model"].predict_proba(df)) * 100

    reaction_label = models["le_y_reaction"].inverse_transform([int(reaction_pred)])[0]
    outcome_label = models["le_y_outcome"].inverse_transform([int(outcome_pred)])[0]

    return reaction_label, outcome_label, reaction_prob, outcome_prob

# Generate SHAP plot
def generate_xai_plot(df, models, save_path="static/xai_plot.png"):
    explainer, shap_values = models["xai_reaction"]
    shap_vals = shap_values[0] if isinstance(shap_values, list) else shap_values
    if shap_vals.ndim == 3:
        shap_vals = shap_vals[0, :, :]
    if shap_vals.shape[1] > df.shape[1]:
        shap_vals = shap_vals[:, :df.shape[1]]
    shap_single = shap_vals[0, :] if shap_vals.ndim == 2 else shap_vals
    plt.figure(figsize=(8,5))
    pd.Series(shap_single, index=df.columns).sort_values(key=abs, ascending=True).plot(kind="barh", color="skyblue")
    plt.title("Feature Contribution (SHAP Values)")
    plt.xlabel("SHAP value")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    return save_path
