import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def plot_visualizations(df, cleaned_df):
    num_cols = df.select_dtypes(include='number').columns
    
    if len(num_cols) > 0:
        first_num_col = num_cols[0]

        st.write("### 🔥 Correlation Heatmap Comparison")
        col1, col2 = st.columns(2)
        with col1:
            st.write("#### Before Cleaning")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
        with col2:
            st.write("#### After Cleaning")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(cleaned_df[num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)

        st.write("### 📊 Histogram Comparison")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"#### Before Cleaning ({first_num_col})")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.histplot(df[first_num_col], bins=20, kde=True, ax=ax)
            st.pyplot(fig)
        with col2:
            st.write(f"#### After Cleaning ({first_num_col})")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.histplot(cleaned_df[first_num_col], bins=20, kde=True, ax=ax)
            st.pyplot(fig)

        st.write("### 📦 Boxplot Comparison")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"#### Before Cleaning ({first_num_col})")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.boxplot(x=df[first_num_col], ax=ax)
            st.pyplot(fig)
        with col2:
            st.write(f"#### After Cleaning ({first_num_col})")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.boxplot(x=cleaned_df[first_num_col], ax=ax)
            st.pyplot(fig)
