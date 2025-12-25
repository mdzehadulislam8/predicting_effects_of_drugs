# app.py
from flask import Flask, render_template, request
from utils import load_all_models, preprocess_input, predict_reaction_outcome, generate_xai_plot
import pandas as pd

app = Flask(__name__)
models = load_all_models()

DATA_PATH = "data/neonatal_adr_top20_new.xlsx"
df = pd.read_excel(DATA_PATH)
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
unique_products = sorted(df["suspect_product_active_ingredients"].dropna().unique())
unique_reasons = sorted(df["reason_for_use"].dropna().unique())

@app.route("/")
def index():
    return render_template("index.html", products=unique_products, reasons=unique_reasons)

@app.route("/predict", methods=["POST"])
def predict():
    form_data = [
        request.form["product"],
        request.form["reason"],
        request.form["sex"],
        request.form["age"],
        request.form["weight"]
    ]
    df_input = preprocess_input(form_data, models["le_dict"])
    reaction_label, outcome_label, reaction_prob, outcome_prob = predict_reaction_outcome(df_input, models)
    xai_path = generate_xai_plot(df_input, models)
    return render_template("result.html",
                           reaction=reaction_label,
                           outcome=outcome_label,
                           reaction_prob=round(reaction_prob,2),
                           outcome_prob=round(outcome_prob,2),
                           xai_image=xai_path)

if __name__ == "__main__":
    app.run(debug=True)
