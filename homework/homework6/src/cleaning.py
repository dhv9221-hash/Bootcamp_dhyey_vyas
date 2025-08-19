import numpy as np 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def drop_missing(df):
    df_copy=df.copy()
    df_copy=df_copy.dropna()
    return df_copy
    

def fill_missing_median(df):
    df_copy=df.copy()
    df_copy['price_float_median']=df_copy['price_float'].fillna(df_copy['price_float'].median())
    df_copy=df_copy.reset_index(drop=True)
    return df_copy
    

def normalize_data(df1):
    df_copy=df1.copy()
    scaler = MinMaxScaler()
    df_copy['price_float_scaled']=scaler.fit_transform(df_copy[['price_float_median']])
    return df_copy
    