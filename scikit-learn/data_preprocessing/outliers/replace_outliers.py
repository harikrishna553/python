import pandas as pd
import numpy as np

def find_and_replace_outlier_columns(df, threshold=1.5):
    outlier_columns = []
    for column in df.columns:
        if df[column].dtype in [np.int64, np.float64]:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
            if not outliers.empty:
                print(f'\nOutliers exists in the column {column}')
                df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
                df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])


df = pd.DataFrame({
    'a': [1, 2, 3, 4, 5, 6, 7, 32, 64, 128, 256, 1024],
    'b': [1024, 2058, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})

print(df.describe())

print('\nReplacing outliers with lower and upper bounds')
find_and_replace_outlier_columns(df, 3)
print(df.describe())