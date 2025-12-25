# Neonatal ADR Prediction System

> A machine learning web application for predicting adverse drug reactions (ADR) in neonatal patients using CatBoost classifiers and SHAP-based explainability.

## Overview

Predicts two critical outcomes from patient and medication data:
- **Reaction Type** — Classifies the adverse reaction category
- **Outcome Severity** — Predicts reaction severity level

Uses SHAP visualizations to explain model predictions and highlight feature importance.

## Features

- Dual CatBoost classification models (reaction type + outcome prediction)
- Real-time Flask web interface with interactive prediction form
- SHAP-based explainability for model transparency
- Label encoding for categorical feature handling
- Responsive HTML frontend with results visualization

## Project Structure

| Directory | File | Purpose |
|-----------|------|---------|
| Root | `app.py` | Flask web server & prediction routes |
| | `train_model.py` | Model training & validation pipeline |
| | `utils.py` | Data preprocessing, inference, SHAP utilities |
| | `requirements.txt` | Python package dependencies |
| | `README.md` | Project documentation |
| `templates/` | `index.html` | Input form interface |
| | `result.html` | Results page with SHAP visualization |
| `models/` | (generated) | Trained CatBoost model artifacts |
| `data/` | (input) | Dataset directory - private/restricted access |
| `static/` | (generated) | SHAP feature importance plots |

## Installation

### Requirements
- Python 3.8+
- pip

### Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Dataset Access** ⚠️
   
   The training dataset is **proprietary clinical data** (not included in this repository).
   
   **To request dataset access, email:**
   - Md. Zehadul Islam: [gg.solve.zehadul999@gmail.com](mailto:gg.solve.zehadul999@gmail.com)
   - Md. Abdullah Al Moin: [midul7714@gmail.com](mailto:midul7714@gmail.com)

   
   **Include in request:** Your name, institution, and research purpose. Access granted for research/education only after approval.

## Usage

### Code Structure

The project follows a modular architecture:
Training Models

```bash
python train_model.py
```

Trains two CatBoost classifiers on the clinical dataset and saves models to `models/` directory.

*Requires dataset access (see Installation).*

### Running the Web Application

```bash
python app.py
```

Access the application at: `http://localhost:5000`

**Workflow:**
1. Select medication (active ingredient)
2. Choose indication (reason for use)
3. Enter patient details: sex, age, weight
4. Click "Predict"
5. View prediction results + SHAP explanation plot

### Application Screenshots

| Input Interface | Results Page |
|-----------------|-------------|
| ![Input Form](https://drive.google.com/uc?id=1yhqdjHCRrBMndkI7zVQz758FN8SShxfY) | ![Results Page](https://drive.google.com/uc?id=1SUwoAXsESxb8aAf33lnNczZ2GK0ds6WG)

**Input Features**: 5 (medication, reason, sex, age, weight)

**Architecture**:
- Label encoding for categorical features
- Two CatBoost classifiers (reaction & outcome)
- SHAP-based feature importance visualization

**Output**: Probability scores + feature importance plot

## Dependencies
Data**: This project uses sensitive clinical data from neonatal adverse drug reactions. All data handling must comply with healthcare regulations.

⚠️ **Clinical Use**: This system is a research tool and decision support aid, not a clinical decision maker. Professional clinical judgment is always required.
Architecture

**Input Features:** 5 (medication, indication, sex, age, weight)

**Pipeline:**
- Label encoding for categorical features
- Two CatBoost classifiers: reaction type + outcome prediction
- SHAP visualization for feature importance

**Output:** Probability scores + feature importance plot

## Dependencies

- Flask (web framework)
- pandas, scikit-learn (data processing)
- CatBoost (gradient boosting classifier)
- SHAP (model explainability)
- matplotlib (visualization)
- joblib (model serialization)
- openpyxl (Excel handling)

See `requirements.txt` for version specifications.

## Important Notes

⚠️ **Clinical Data** — Contains sensitive neonatal adverse reaction information. Strict privacy compliance required.

⚠️ **Research Use Only** — Decision support tool, not a clinical decision maker. Professional judgment always required.

⚠️ **Data Protection** — Dataset access restricted and non-redistributable. Individual requests reviewed on case-by-case basis.

⚠️ **Regulatory Compliance** — Ensure HIPAA, GDPR, and institutional requirements compliance before deployment.

## License & Disclaimer

Developed for educational and research purposes only. **Not intended for clinical decision-making without proper validation, oversight, and regulatory approval.**

---

**Last Updated:** December 2025 | **Status:** Active Development