import pandas as pd
import numpy as np

def basic_exploration(df):
    print("rows:{},columns:{}".format(str(df.shape[0]),str(df.shape[1])))
    print(df.info())
    print(df.describe())
    print("Descriptive Statistics for all columns:")
    print(df.describe(include='object'))
    print("Non Null Columns and Counts:")
    null_df = pd.DataFrame(df.isnull().sum())
    null_df.columns = ['Count']
    print(null_df[null_df['Count'] > 0])
    df_numeric = df.select_dtypes(exclude='object')
    df_num_cols = df_numeric.columns
    for c in df_num_cols:
        print(c)
        print(iqr_outliers(df[c]))

def iqr_outliers(num_array):
    # Find 25th percentile / q1
    q1 = np.nanpercentile(num_array, 25)
    # Find 25th percentile / q1
    q3 = np.nanpercentile(num_array, 75)
    # Find IQR
    iqr = q3 - q1
    # Define upper and lower limits for outlier detection
    upper_limit = q3 + (1.5 * iqr)
    lower_limit = q1 - (1.5 * iqr)
    return [num for num in num_array if (num > upper_limit or num < lower_limit)]

def outlier(arr):
    per1 = np.nanpercentile(arr,75)
    per2 = np.nanpercentile(arr,25)
    iqr = per1-per2
    upperbound = per1+(1.5*iqr)
    lowerbound = per2-(1.5*iqr)
    return[i for i in arr if (i>upperbound or i<lowerbound)]