import pandas as pd
import numpy as np
def outlier(arr):
    per1 = np.nanpercentile(arr,75)
    per2 = np.nanpercentile(arr,25)
    iqr = per1-per2
    upperbound = per1+(1.5*iqr)
    lowerbound = per2-(1.5*iqr)
    return[i for i in arr if (i>upperbound or i<lowerbound)]


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


def basic_exploration(titanic):
    print("rows:{},columns:{}".format(str(titanic.shape[0]),str(titanic.shape[1])))
    print(titanic.info())
    print(titanic.describe())
    print("Descriptive Statistics for all columns:")
    print(titanic.describe(include='object'))
    print("Non Null Columns and Counts:")
    null_titanic = pd.DataFrame(titanic.isnull().sum())
    null_titanic.columns = ['Count']
    print(null_titanic[null_titanic['Count'] > 0])
    titanic_numeric = titanic.select_dtypes(exclude='object')
    titanic_num_cols = titanic_numeric.columns
    for c in titanic_num_cols:
        print(c)
        print(iqr_outliers(titanic[c]))

