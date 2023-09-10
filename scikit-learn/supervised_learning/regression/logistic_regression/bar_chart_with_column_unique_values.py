import pandas as pd
import matplotlib.pyplot as plt

def categorical_columns(df, count_threshold):
    # Approach 1: Data Type Inspection
    categorical_columns_dtype = df.select_dtypes(include=['object', 'category']).columns

    categorical_columns_dtype_by_threshold = [col for col in categorical_columns_dtype if
                                              df[col].nunique() < count_threshold]

    # Approach 2: Unique Value Count
    categorical_columns_unique_by_threshold = [col for col in df.columns if df[col].nunique() < count_threshold]

    # Add elements to the list
    all_categorical_columns = []
    all_categorical_columns.extend(categorical_columns_dtype_by_threshold)

    for item in categorical_columns_unique_by_threshold:
        if item not in all_categorical_columns:
            all_categorical_columns.append(item)

    return all_categorical_columns


df = pd.read_csv('weatherAUS.csv')
df.info()

threshold = 50
columns = categorical_columns(df, threshold)
columns_to_remove = ['WindSpeed9am', 'WindSpeed3pm', 'Cloud9am', 'Cloud3pm']
columns = [item for item in columns if item not in columns_to_remove]

unique_values = []

# Set display options to prevent column trimming
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.expand_frame_repr', False)  # Prevent line wrapping

print(df[columns].head())

for column in columns:
    unique_values.append(df[column].nunique())

total_columns = len(df.columns)
categorical_columns = len(columns)

plt.bar(columns, unique_values, label=f'total rows : {len(df)}\n '
                                      f'total_columns : {total_columns}\n '
                                      f'categorical_columns : {categorical_columns}\n'
                                      f'threshold_used = {threshold}')
plt.legend()

plt.show()


