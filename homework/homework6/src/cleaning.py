import numpy as np 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def drop_missing(df):
    df_copy=df.copy()
    df_copy=df_copy.dropna()
    return df_copy
    

def fill_missing_median(df,col_name):
    df_copy=df.copy()
    df_copy[f'{col_name}_missing']=df_copy[col_name].fillna(df_copy[col_name].median())
    df_copy=df_copy.reset_index(drop=True)
    return df_copy
    

def normalize_data(df1,col_name):
    df_copy=df1.copy()
    scaler = MinMaxScaler()
    df_copy[f'{col_name}_scaled']=scaler.fit_transform(df_copy[[col_name]])
    return df_copy
    