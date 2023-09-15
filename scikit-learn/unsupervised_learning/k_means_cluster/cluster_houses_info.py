import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

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
    print(f'column_wise_missing_values : \n{column_wise_missing_values}')

    # Check for duplicate rows based on all columns
    duplicate_count = df.duplicated().sum()
    print(f'\nduplicate_count : \n{duplicate_count}')

    # Print unique counts
    print(f'\nUnique counts, missing values count, data types column wise')
    unique_counts = df.nunique()
    missing_values = df.isnull().sum()
    result_df = pd.DataFrame({'Data Type': df.dtypes, 'unique_count': unique_counts, 'missing_values' : missing_values})
    print(result_df)

    numerical_columns = [var for var in df.columns if df[var].dtype != 'O']
    print(round(df[numerical_columns].describe()))


def preprocess_data(df):
    # Encode ocean_proximity column
    label_encoder = LabelEncoder()
    df['ocean_proximity'] = label_encoder.fit_transform(df['ocean_proximity'])

    # Replace missing values in 'total_bedrooms' column with mode
    mode = df['total_bedrooms'].dropna().mode()
    print(f'total_bedrooms mode : {mode.iloc[0]}\n')
    df['total_bedrooms'].fillna(mode.iloc[0], inplace=True)


def cluster(df):
    no_of_clusters = 5
    kmeans = KMeans(n_clusters=no_of_clusters, random_state=47)

    # Fit the KMeans model to the data
    kmeans.fit(df)

    # Get cluster centroids and labels
    centroids = kmeans.cluster_centers_
    #print(f'centroids : {centroids}')
    labels = kmeans.labels_

    # Since visualizing high-dimensional data directly is challenging, we can only display a scatter plot of the first two dimensions
    plt.scatter(df['housing_median_age'], df['median_house_value'], c=labels, cmap='viridis', s=50)
    plt.title('K-Means Clustering (First Two Dimensions)')
    plt.xlabel('housing_median_age')
    plt.ylabel('median_house_value')
    plt.show()

df = pd.read_csv('housing.csv')
basic_analysis(df)
preprocess_data(df)
cluster(df)