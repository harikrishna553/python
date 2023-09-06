import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

# Adjust display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

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

    for col in categorical_columns:
        print(f'\nFrequency count of values for the column {col}\n')
        print(df[col].value_counts())

    # print null value count and unique values count of categorical columns
    # Create an empty DataFrame to store the counts
    null_and_unique_value_count = pd.DataFrame(index=categorical_columns)

    # Count of null values for each column
    null_and_unique_value_count['Null Count'] = df[categorical_columns].isnull().sum()

    # Count of unique values for each column
    null_and_unique_value_count['Unique Count'] = df[categorical_columns].nunique()

    # Display the combined DataFrame
    print(null_and_unique_value_count)


def preprocess(df, categorical_columns):
    df_copy = df.copy(deep=True)

    # Convert the type of Date from Object to date typee
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])

    df_copy['Year'] = df_copy['Date'].dt.year
    df_copy['Month'] = df_copy['Date'].dt.month
    df_copy['Day'] = df_copy['Date'].dt.day

    df_copy.drop('Date', axis=1, inplace=True)

    # Encode the categorical columns
    label_encoder = LabelEncoder()
    for col in categorical_columns:
        # Fill missing values with mode
        mode_value = df_copy[col].mode().iloc[0]
        df[col].fillna(mode_value, inplace=True)

        # Encode the data
        df_copy[col] = label_encoder.fit_transform(df_copy[col])

    #print('\nNull values count in categorical columns')
    #print(df_copy[categorical_columns].isnull().sum())

    #print('\nfirst five rows of categorical columns')
    #print(df_copy[categorical_columns].head())

    # Work with numerical columns
    numerical_columns = [var for var in df.columns if df[var].dtype != 'O']
    #print('The numerical variables are :', numerical_columns)
    #print('Total numeric columns are : ', len(numerical_columns))

    #null_values_count = df[numerical_columns].isnull().sum()
    # print(f'null_values_count : \n{null_values_count}')

    # print('Basic statistics on numerical columns\n')
    # print(round(df[numerical_columns].describe()))

    # Replace all the outliers using Winsorization approach
    # Winsorization involves replacing extreme values with less extreme
    outlier_columns = ['Rainfall', 'Evaporation', 'WindSpeed9am', 'WindSpeed9am']
    for col_name in outlier_columns:
        lower_limit = df_copy[col_name].quantile(0.1)
        upper_limit = df_copy[col_name].quantile(0.9)
        df_copy[col_name] = np.where(df[col_name] < lower_limit, lower_limit, df_copy[col_name])
        df_copy[col_name] = np.where(df_copy[col_name] > upper_limit, upper_limit, df_copy[col_name])

    #print('Basic statistics on numerical columns\n')
    # print(round(df_copy[outlier_columns].describe()))

    # let's replace all the missing values with median
    for col_name in numerical_columns:
        median = df_copy[col_name].median()
        df_copy[col_name].fillna(median, inplace=True)

    #print(df_copy)
    #print(df_copy[numerical_columns].isnull().sum())
    return df_copy

def train_and_test_model(df):
    # Divide the data into features and target variable
    target_column_name = 'RainTomorrow'
    X = df.drop([target_column_name], axis=1)

    #scaler = MinMaxScaler()
    #X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    y = df[target_column_name]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=47)
    #print(X_train.describe())

    # instantiate the model
    logreg = LogisticRegression(solver='liblinear', random_state=47)

    # fit the model
    logreg.fit(X_train, y_train)

    y_pred = logreg.predict(X_test)
    print('Model accuracy score : ',accuracy_score(y_test, y_pred))

df = pd.read_csv('weatherAUS.csv')
categorical_columns = ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow']

# basic_analysis(df, categorical_columns)
preprocessed_data = preprocess(df, categorical_columns)
# preprocessed_data.info()

train_and_test_model(preprocessed_data)
