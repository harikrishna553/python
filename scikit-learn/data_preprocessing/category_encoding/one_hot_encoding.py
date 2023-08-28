import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Create a DataFrame with a categorical column
df = pd.DataFrame(
    {'color': ['red', 'green', 'blue', 'red']}
)

# Create a OneHotEncoder object
encoder = OneHotEncoder()

# Transform the DataFrame
encoded_sparse_matrix = encoder.fit_transform(df)

# The result is a sparse matrix, you can convert it to a dense array
one_hot_encoded_array = encoded_sparse_matrix.toarray()

print("Original categorical data:")
print(df)

print("\nencoded sparse matrix:")
print(type(encoded_sparse_matrix))

print("\nOne-hot encoded data:")
print(one_hot_encoded_array)
