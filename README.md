# Neonatal ADR Prediction System

A machine learning-based web application for predicting adverse drug reactions (ADR) and outcomes in neonatal patients using CatBoost classifiers with SHAP-based explainability.

## Overview

The system predicts two outcomes from patient and medication data:
- **Reaction Type**: Classification of the adverse reaction
- **Outcome Severity**: Predicted severity level

It provides SHAP visualizations to help interpret prediction drivers.

## Features

- Dual CatBoost models for reaction type and outcome prediction
- Flask web interface with real-time predictions
- SHAP-based model explainability
- Label encoding for categorical features
- Responsive input form with dropdown selections

## Project Structure

```
.
├── app.py                          # Flask web application
├── train_model.py                  # Model training pipeline
├── utils.py                        # Utility functions (preprocessing, prediction, XAI)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── templates/
│   ├── index.html                 # Input form interface
│   └── result.html                # Prediction results page
├── models/                        # Trained model artifacts (generated)
├── data/
│   └── neonatal_adr_top20_new.xlsx # Training dataset
└── static/                        # XAI plots (generated)
```

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Dataset Access** ⚠️
   - The training dataset (`data/neonatal_adr_top20_new.xlsx`) is **not included** in this repository
   - **Permission required**: Contact the project maintainer to access the dataset
   - Once obtained, place it in the `data/` directory
   - Required columns: suspect_product_active_ingredients, reason_for_use, reactions, outcomes, sex, patient_age, patient_weight

## Usage

### Train Models
```bash
python train_model.py
```
Trains CatBoost classifiers and saves to `models/` directory.

### Run Web Application
```bash
python app.py
```
Access at `http://localhost:5000`

**Using the Web Interface:**

| Step | Action |
|------|--------|
| 1 | Select medication (active ingredient) |
| 2 | Choose reason for use |
| 3 | Enter patient details (sex, age, weight) |
| 4 | Click Predict |
| 5 | View results and SHAP explanation plot |

### Interface Screenshots

- **Input Form**: [See index.html page](screenshots/input_form.png) - Main prediction input interface
- **Results Page**: [See result.html page](screenshots/results_page.png) - Prediction output with SHAP visualization

## Model Architecture

### Classification Pipeline

- **Input Features**: 5 features (medication, reason, sex, age, weight)
- **PreprDetails

**Input Features**: 5 (medication, reason, sex, age, weight)

**Architecture**:
- Label encoding for categorical features
- Two CatBoost classifiers (reaction & outcome)
- SHAP-based feature importance visualization

**Output**: Probability scores + feature importance plot
| Flask | ≥2.1 | Web framework |
| pandas | ≥1.3 | Data manipulation |
See `requirements.txt` for details:
- Flask (web framework)
- pandas, scikit-learn (data processing)
- CatBoost (gradient boosting)
- SHAP (explainability)
- matplotlib (visualization)
- joblib, openpyxl (utilities)ng columns:

| Column | Type | Description |
|--------|------|-------------|
| suspect_product_active_ingredients | string | Medication name/ingredient |
Required Excel columns:
- `suspect_product_active_ingredients`: Medication name
- `reason_for_use`: Clinical indication
- `reactions`: Observed adverse reaction
- `outcomes`: Reaction outcome/severity
- `sex`: Patient gender (M/F)
- `patient_age`: Age (numeric)
- `patient_weight`: Weight in kg
- **Data Path**: `DATA_PATH = "data/neonatal_adr_top20_new.xlsx"`
- **settings (in code):
- `DATA_PATH = "data/neonatal_adr_top20_new.xlsx"`
- `MODEL_DIR = "models"`
- Flask debug mode enabled for development

## Important Notes

⚠️ **Clinical Use**: This is a decision support tool, not a clinical decision maker. Always consult healthcare professionals.

⚠️ **Data Privacy**: Ensure compliance with HIPAA, GDPR, and institutional regulations before deployment.

⚠️ **Dataset Access**: The dataset is proprietary and requires permission. Contact maintainers for access.
This project is developed for educational and research purposes. Ensure compliance with your institution's policies and healthcare regulations before clinical deployment.

## Support & Contact

For issues, questions, or collaborations:
- Review the code comments and docstrings
- Check the project structure and file descriptions
- Verify dataset format and file paths match expectations

## Disclaimer

This application is intended for research and educational purposes. It should not be used for clinical decision-making without proper validation, clinical oversight, and regulatory approval. Always consult qualified healthcare professionals for medical decisions.

---

**Last Updated**: December 2025  
**Status**: Active Development
 & Disclaimer

Developed for educational and research purposes. Not intended for clinical decision-making without proper validation and oversight.

---

**Last Updated**: December 2025 | 