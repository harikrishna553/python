import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# Adjust display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def find_outlier_columns(df, threshold=1.5):
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
                outlier_columns.append(column)
    return outlier_columns

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
                df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
                df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])

def basic_analysis(df):
    shape = df.shape
    total_rows = shape[0]
    total_columns = shape[1]

    print(f'\ntotal_rows : {total_rows}')
    print(f'total_columns : {total_columns}')

    columns = df.columns
    print(f'\ncolumns : {columns}')

    print('\nDetailed information')
    df.info()

    five_rows = df.head()
    print(f'five_rows : \n{five_rows}')

    print('\nColumn wise missing values')
    column_wise_missing_values = df.isnull().sum()
    print(f'column_wise_missing_values : {column_wise_missing_values}')

    # Check for duplicate rows based on all columns
    duplicate_count = df.duplicated().sum()
    print(f'\nduplicate_count : {duplicate_count}')

    # Print unique counts
    print(f'\nUnique counts, missing values count, data types column wise')
    unique_counts = df.nunique()
    missing_values = df.isnull().sum()
    result_df = pd.DataFrame({'Data Type': df.dtypes, 'unique_count': unique_counts, 'missing_values' : missing_values})
    print(result_df)

    numerical_columns = [var for var in df.columns if df[var].dtype != 'O']
    print(round(df[numerical_columns].describe()))

    outlier_columns = find_outlier_columns(df, 3)
    print(f'Total outlier_columns : {len(outlier_columns)}')
    print(f'outlier_columns : \n{outlier_columns}')

def preprocess_data(df):
    df.drop('Unnamed: 32', axis=1, inplace=True)
    df.drop('id', axis=1, inplace=True)

    label_encoder = LabelEncoder()
    df['diagnosis'] = label_encoder.fit_transform(df['diagnosis'])

    find_and_replace_outlier_columns(df, 3)

    #print(round(df.describe()))

def train_test_model(df):
    #df.info()

    # Split the data into features (X) and target (y)
    X = df.drop(['diagnosis'], axis=1)
    y = df['diagnosis']

    sc = StandardScaler()
    X = sc.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=47)

    # Initialize the K-NN classifier (Let's choose k=3)
    knn_classifier = KNeighborsClassifier(n_neighbors=3)

    # Fit the classifier to the training data
    knn_classifier.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = knn_classifier.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)


df = pd.read_csv('KNNAlgorithmDataset.csv')
# basic_analysis(df)
preprocess_data(df)
train_test_model(df)