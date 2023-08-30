import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load log data from CSV file
data = pd.read_csv('log_data_binary.csv')

# Split data into features (log messages) and labels (severity)
X = data['log_message']
y = data['severity']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Transform text data to TF-IDF features
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Create a Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Train the classifier on the training data
clf.fit(X_train_tfidf, y_train)

# Predict severities for the test data
y_pred = clf.predict(X_test_tfidf)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# print("Predicted severities:", y_pred)
# print("True severities:", y_test)
print("Accuracy:", accuracy)

# Loop through the Series and print each element
index = 0;
for label, value in y_test.items():
    print(X_test[label], ',', value, ',',  y_pred[index])
    index = index + 1
    # print(f"Label: {label}, Value: ")