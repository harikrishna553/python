
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # statistical data visualization

def basic_analysis(df):

    five_rows = df.head()
    print(f'five_rows : {five_rows}')

    shape = df.shape
    total_rows = shape[0]
    total_columns = shape[1]

    print(f'\ntotal_rows : {total_rows}')
    print(f'total_columns : {total_columns}')

    columns = df.columns
    print(f'\ncolumns : {columns}')

    print('\nDetailed information')
    df.info()

    print('\nColumn wise missing values')
    column_wise_missing_values = df.isnull().sum()
    print(f'column_wise_missing_values : {column_wise_missing_values}')

    # Check for duplicate rows based on all columns
    duplicate_count = df.duplicated().sum()
    print(f'duplicate_count : {duplicate_count}')

    # Print unique counts
    print(f'\nUnique counts, missing values count, data types column wise')
    unique_counts = df.nunique()
    missing_values = df.isnull().sum()
    result_df = pd.DataFrame({'Data Type': df.dtypes, 'Unique Count': unique_counts, 'missing_values' : missing_values})
    print(result_df)

def preprocess(df):
    preprocessed_df = df.copy(deep=True)

    return preprocessed_df

df = pd.read_csv('weatherAUS.csv')

categorical_columns = ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow']
for col in categorical_columns:
    print(f'\nFrequency count of values for the column {col}\n')
    print(df[col].value_counts())

# basic_analysis(df)
preprocessed_data = preprocess(df)