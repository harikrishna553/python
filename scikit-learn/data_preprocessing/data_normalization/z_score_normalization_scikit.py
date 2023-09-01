import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create a sample pandas DataFrame
data = pd.DataFrame({
    'ratings': [27, 98, 123, 4, 6, 897, 643],
    'product_code': [123, 43, 91, 8, 98, 45, 3]
})
df = pd.DataFrame(data)

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the data using the scaler
normalized_data = scaler.fit_transform(data[['ratings']])
normalized_df = pd.DataFrame(normalized_data, columns=['ratings'])

print('actual_rating,normalized_rating')
for index, row in normalized_df.iterrows():
    print(data.iloc[index]['ratings'],',',row['ratings'])

print()