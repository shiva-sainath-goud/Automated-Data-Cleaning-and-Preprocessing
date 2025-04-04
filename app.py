# app.py (Main Streamlit App)
import streamlit as st
import pandas as pd
from data_cleaning import clean_data
from visualization import plot_raw_data, plot_cleaned_data

st.set_page_config(page_title="Data Cleaning Tool", page_icon="🧹", layout="wide")
st.title("🧹 Automated Data Cleaning & Preprocessing Tool")

st.sidebar.title("📁 Upload & Options")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    tab1, tab2 = st.tabs(["Raw Data", "Data Cleaning"])
    
    with tab1:
        st.subheader("📄 Raw Data Preview")
        st.dataframe(df.head())
        plot_raw_data(df)
    
    with tab2:
        st.subheader("🛠 Data Cleaning Options")
        if st.button("🚀 Clean My Data"):
            df = clean_data(df)
            st.success("✅ Data cleaned successfully!")
            st.dataframe(df.head())
            plot_cleaned_data(df)
            st.download_button("📥 Download Cleaned CSV", df.to_csv(index=False).encode('utf-8'), "cleaned_data.csv", "text/csv")
