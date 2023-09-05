import pandas as pd

def categorical_columns(df, count_threashold):
    # Approach 1: Data Type Inspection
    categorical_columns_dtype = df.select_dtypes(include=['object', 'category']).columns

    categorical_columns_dtype_by_threshold = [col for col in categorical_columns_dtype if df[col].nunique() < count_threashold]

    # Approach 2: Unique Value Count
    categorical_columns_unique_by_threshold = [col for col in df.columns if df[col].nunique() < count_threashold]

    # Add elements to the list
    all_categorical_columns = []
    all_categorical_columns.extend(categorical_columns_dtype_by_threshold)

    for item in categorical_columns_unique_by_threshold:
        if item not in all_categorical_columns:
            all_categorical_columns.append(item)

    return all_categorical_columns

# Sample DataFrame
data = {
    'Name': ['Harika', 'Krishna', 'Joel', 'Gopi', 'Sailu', 'Raj', 'Ravi', 'Narasimha'],
    'Age': [25, 30, 22, 35, 36, 42, 23, 37],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male'],
    'City': ['Chennai', 'Bangalore', 'Chennai', 'Bangalore', 'Hyderabad', 'Bangalore', 'Hyderabad', 'Bangalore']
}

df = pd.DataFrame(data)
categorical_columns = categorical_columns(df, 5)
print(f'categorical_columns : {categorical_columns}')





