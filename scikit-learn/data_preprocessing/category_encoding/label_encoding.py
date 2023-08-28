from sklearn.preprocessing import LabelEncoder

# Sample categorical labels
categorical_labels = ['poor', 'average', 'good', 'average', 'good', 'excellent']

# Creating an instance of LabelEncoder
label_encoder = LabelEncoder()

# Fitting the encoder on the categorical labels and transforming them
encoded_labels = label_encoder.fit_transform(categorical_labels)

print(encoded_labels)
