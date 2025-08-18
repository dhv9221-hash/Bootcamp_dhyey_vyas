import numpy as np
import pandas as pd

def data_summary(df):
    df_temp=df.describe()
    print("from function",df_temp)
    return df_temp