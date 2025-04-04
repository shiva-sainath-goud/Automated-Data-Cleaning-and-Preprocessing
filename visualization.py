import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_raw_data(df):
    st.subheader("📊 Raw Data Visualizations")
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    with col2:
        st.write("### Histogram of Numeric Columns")
        fig, ax = plt.subplots(figsize=(8, 6))
        df.select_dtypes(include='number').hist(figsize=(8, 6), bins=20)
        st.pyplot(fig)

def plot_cleaned_data(df):
    st.subheader("📊 Cleaned Data Visualizations")
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Correlation Heatmap (After Cleaning)")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    with col2:
        st.write("### Histogram of Numeric Columns (After Cleaning)")
        fig, ax = plt.subplots(figsize=(8, 6))
        df.select_dtypes(include='number').hist(figsize=(8, 6), bins=20)
        st.pyplot(fig)
