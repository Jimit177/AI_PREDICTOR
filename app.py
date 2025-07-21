import streamlit as st
import subprocess
import pandas as pd
import joblib
import os

# Constants
symbols = ["NIFTY", "BANKNIFTY"]
intervals = ["5m", "15m", "30m", "60m"]
model_dir = "final_models"

st.set_page_config(page_title="Option Signal App", layout="centered")
st.title("📊 Option Signal Predictor")

# Step 1: Run backend.ipynb using nbconvert once per session
@st.cache_resource
def run_backend_once():
    try:
        subprocess.run([
            "jupyter", "nbconvert", "--to", "notebook",
            "--execute", "--inplace", "backend.ipynb"
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        st.error(f"❌ Failed to execute backend notebook.\n\n{e}")
        return False

# Automatically run the backend at app startup (once per session)
if run_backend_once():
    st.success("✅ Backend preprocessing complete for this session.")

# Step 2: Let user select symbol
selected_symbol = st.selectbox("Select Index for Prediction", symbols)

# Step 3: Predict for selected symbol
if st.button("🚀 Get Prediction"):
    st.subheader(f"📌 Frame-wise Decision for {selected_symbol}:")

    for interval in intervals:
        model_path = f"{model_dir}/{selected_symbol}_model_{interval}.pkl"
        data_path = f"nifty_banknifty_labeled/{selected_symbol}_{interval}_labeled.csv"

        if not os.path.exists(model_path) or not os.path.exists(data_path):
            st.write(f"⏱ {interval}: ❌ Missing model or data")
            continue

        try:
            model = joblib.load(model_path)
            df = pd.read_csv(data_path, index_col=0)
            df.drop(columns=['target', 'future_close', 'return_pct'], errors='ignore', inplace=True)
            df = df.select_dtypes(include='number').fillna(0)

            if df.empty:
                st.write(f"⏱ {interval}: ⚠️ No valid input data")
                continue

            pred = model.predict(df.iloc[[-1]])[0]
            signal = {0: "📉 PUT", 1: "⏸️ NO ACTION", 2: "📈 CALL"}.get(pred, "❓ Unknown")

            st.write(f"⏱ {interval}: {signal}")
        except Exception as e:
            st.write(f"⏱ {interval}: ⚠️ Prediction failed — {e}")
