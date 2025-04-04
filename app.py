import streamlit as st
import pandas as pd
import time
from data_cleaning import clean_data
from visualization import plot_visualizations

st.set_page_config(page_title="Data Cleaning Tool", page_icon="🧹", layout="wide")

st.title("🧹 Automated Data Cleaning Tool")

st.sidebar.title("📁 Upload & Options")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        cleaned_df = df.copy()
        
        tab1, tab2, tab3 = st.tabs(["📄 Raw Data", "🛠 Data Cleaning", "📊 Cleaned Data & Comparisons"])
        
        with tab1:
            st.subheader("📊 Raw Data Preview")
            st.dataframe(df.head(10))
            st.info("After previewing raw data, move to Data Cleaning for processing.")

        with tab2:
            st.subheader("🔧 Cleaning Options")
            remove_dupes = st.checkbox("Remove Duplicates")
            handle_missing_vals = st.checkbox("Handle Missing Values")
            handle_outliers_flag = st.checkbox("Handle Outliers")
            normalize_format = st.checkbox("Normalize Text Formatting")
            scale_numeric = st.checkbox("Scale Numeric Features")
            encode_cat = st.checkbox("One-Hot Encode Categorical Variables")
            
            if st.button("🚀 Clean My Data"):
                with st.spinner("Processing..."):
                    options = {
                        "remove_dupes": remove_dupes,
                        "handle_missing_vals": handle_missing_vals,
                        "handle_outliers_flag": handle_outliers_flag,
                        "normalize_format": normalize_format,
                        "scale_numeric": scale_numeric,
                        "encode_cat": encode_cat,
                    }
                    cleaned_df = clean_data(cleaned_df, options)
                    st.success("✅ Data cleaned successfully!")

        with tab3:
            st.subheader("🔍 Cleaned Data Preview")
            st.dataframe(cleaned_df.head(10))
            st.download_button("📥 Download Cleaned CSV", cleaned_df.to_csv(index=False).encode('utf-8'), "cleaned_data.csv", "text/csv")
            st.subheader("📊 Before & After Cleaning Comparisons")
            plot_visualizations(df, cleaned_df)

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
