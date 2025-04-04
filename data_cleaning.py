import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from scipy import stats

def remove_duplicates(df):
    return df.drop_duplicates()

def handle_missing(df):
    imputer = SimpleImputer(strategy='mean')
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = imputer.fit_transform(df[num_cols])
    return df

def handle_outliers(df):
    num_df = df.select_dtypes(include='number')
    z_scores = stats.zscore(num_df)
    return df[(np.abs(z_scores) < 3).all(axis=1)]

def normalize_formatting(df):
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip().str.lower()
    return df

def scale_features(df):
    scaler = StandardScaler()
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = scaler.fit_transform(df[num_cols])
    return df

def encode_categoricals(df):
    return pd.get_dummies(df)

def clean_data(df, options):
    if options["remove_dupes"]:
        df = remove_duplicates(df)
    if options["handle_missing_vals"]:
        df = handle_missing(df)
    if options["handle_outliers_flag"]:
        df = handle_outliers(df)
    if options["normalize_format"]:
        df = normalize_formatting(df)
    if options["scale_numeric"]:
        df = scale_features(df)
    if options["encode_cat"]:
        df = encode_categoricals(df)
    return df
