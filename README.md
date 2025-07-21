# 📈 AI Options Predictor Tool

This repository contains the complete source code, configuration, and data for an AI-powered tool that predicts options trading signals (CALL, PUT, or NO ACTION) for **NIFTY** and **BANKNIFTY** using frame-wise machine learning models.

---

## 🗂️ Contents

- `backend.ipynb` – Jupyter Notebook for data scraping, feature engineering, labeling, model training, and prediction.
- `app.py` – Streamlit app to visualize and select predictions for either NIFTY or BANKNIFTY.
- `OptionsTrade_EDA.ipynb` – Jupyter Notebook for EDA of the losses that were occuring previously can be considered a A (Control) group in A/B testing.
- `nifty_banknifty_../` – All the csv files are saved in each folders separately as every time the app is executed the data updates .
- `final_models/` – Trained model files saved for each timeframe and symbol.
- `requirements.txt` – All required dependencies.
- `.gitignore` – Ignores local files like `venv/` and cache folders.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jimit177/AI_PREDICTOR.git
cd AI_PREDICTOR
```

### 2. Set Up Virtual Environment
## Pythone version 3.10
```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 How to Execute the EDA, Statistical Tests & Hypothesis Evaluation

1. Open `backend.ipynb` in Jupyter Notebook or VS Code.
2. Run all cells sequentially to:
   - Scrape and load data
   - Perform exploratory data analysis (EDA)
   - Run statistical comparisons between options signals
   - Label data based on logic
   - Train models on labeled data
   - Generate predictions

3. Model outputs and statistical test results are displayed at the end of the notebook.

---

## 📚 Jupyter Notebook Language Model (LM) Log

A detailed log of maintained in the Notebook LM source.

🔗 **Notebook LM Log**: [Click here to view the LM log](https://notebooklm.google.com/notebook/9f33373d-66f7-48b1-9c21-56bd24cd8bff?_gl=1*ds9k0u*_up*MQ..*_ga*MTI5NTUyODE1OC4xNzUzMDY3NDMx*_ga_W0LDH41ZCB*czE3NTMwNjc0MzAkbzEkZzAkdDE3NTMwNjc0MzAkajYwJGwwJGgw)

---

## 📦 Included Data Sources

All CSV files used for EDA, training, and prediction are stored in the respective folder 

---

## 🚀 Running the Streamlit App

To launch the prediction tool UI:

```bash
streamlit run app.py
```

- The backend logic will automatically execute first.
- Then, select **NIFTY** or **BANKNIFTY** from the dropdown.
- View predictions frame-wise (5min, 15min, 30min, 60min.).


