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
│   └──dataset
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

| Screenshot | Description |
|-----------|-------------|
| ![Input Form](https://drive.google.com/uc?id=1yhqdjHCRrBMndkI7zVQz758FN8SShxfY) | **Input Form** - Main prediction input interface |
| ![Results Page](https://drive.google.com/uc?id=1SUwoAXsESxb8aAf33lnNczZ2GK0ds6WG) | **Results Page** - Prediction output with SHAP visualization |


## Model Details

**Input Features**: 5 (medication, reason, sex, age, weight)

**Architecture**:
- Label encoding for categorical features
- Two CatBoost classifiers (reaction & outcome)
- SHAP-based feature importance visualization

**Output**: Probability scores + feature importance plot

## Dependencies

See `requirements.txt` for details:
- Flask (web framework)
- pandas, scikit-learn (data processing)
- CatBoost (gradient boosting)
- SHAP (explainability)
- matplotlib (visualization)
- joblib, openpyxl (utilities)

## Data Format

Required Excel columns:
- `suspect_product_active_ingredients`: Medication name
- `reason_for_use`: Clinical indication
- `reactions`: Observed adverse reaction
- `outcomes`: Reaction outcome/severity
- `sex`: Patient gender (M/F)
- `patient_age`: Age (numeric)
- `patient_weight`: Weight in kg

## Configuration

Key settings (in code):
- `DATA_PATH = "data/neonatal_adr_top20_new.xlsx"`
- `MODEL_DIR = "models"`
- Flask debug mode enabled for development

## Important Notes

⚠️ **Clinical Use**: This is a decision support tool, not a clinical decision maker. Always consult healthcare professionals.

⚠️ **Data Privacy**: Ensure compliance with HIPAA, GDPR, and institutional regulations before deployment.

⚠️ **Dataset Access**: The dataset is proprietary and requires permission. Contact maintainers for access.

## License & Disclaimer

Developed for educational and research purposes. Not intended for clinical decision-making without proper validation and oversight.

---

**Last Updated**: December 2025 | **Status**: Active Development 