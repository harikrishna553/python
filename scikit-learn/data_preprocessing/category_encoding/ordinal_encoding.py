from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

df = pd.DataFrame({'rating': ['poor', 'average', 'good', 'average', 'good', 'excellent']})

# Define the meaningful order of categories
meaningful_order = ['poor', 'average', 'good', 'excellent']

# Creating an instance of LabelEncoder
label_encoder = OrdinalEncoder(categories=[meaningful_order])

# Fitting the encoder on the categorical labels and transforming them
encoded_df = label_encoder.fit_transform(df)

# Print the encoded DataFrame
print(encoded_df)

index = 0
for rating in df['rating']:
    print(rating, ' -> ', encoded_df[index][0])
    index  = index + 1