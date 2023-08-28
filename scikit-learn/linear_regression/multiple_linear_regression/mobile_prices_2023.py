import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from datetime import datetime

csv_file = os.getcwd() + '/../../data/csvs/mobile_prices_2023.csv'

input_data_set = pd.read_csv(csv_file)
df = input_data_set

def clean_and_transform_data(df):
    # Drop missing values
    df = df.dropna()

    # Drop duplicates
    df = df.drop_duplicates()

    # Use LabelEncoder to convert categories to numerical labels
    label_encoder = LabelEncoder()

    # Extract brand names and convert the names to numerical labels
    df['Brand Label'] = df['Phone Name'].apply(lambda x: x.split()[0])
    df['Brand Label'] = label_encoder.fit_transform(df['Brand Label'])

    # Normalize ratings
    df['Number of Ratings'] = df['Number of Ratings'].str.replace(',', '').astype(float)
    scaler = MinMaxScaler()
    df['Number of Ratings'] = scaler.fit_transform(df[['Number of Ratings']])

    # Convert the column 'Price in INR' to float
    df['Price in INR'] = df['Price in INR'] \
        .str.replace(',', '') \
        .str.replace('₹', '') \
        .astype(float)

    df['RAM'] = df['RAM'].str.extract('(\d+)').astype(float)
    df['ROM/Storage'] = df['ROM/Storage'].str.extract('(\d+)').astype(float)

    # Convert 'Date' to Unix timestamps
    df['Date of Scraping'] = df['Date of Scraping'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d').timestamp())

    # Extract battery capacity
    df['Battery Capacity'] = df['Battery'].str.extract(r'(\d+) mAh')

    # Convert 'Battery Capacity' to numerical
    df['Battery Capacity'] = pd.to_numeric(df['Battery Capacity'], errors='coerce')

    # Extract back camera details
    df['Back Camera MP'] = df['Back/Rare Camera'].str.extract(r'(\d+)MP')
    df['Back Camera MP'] = pd.to_numeric(df['Back Camera MP'], errors='coerce')

    # Extract front camera detail
    df['Front Camera MP'] = df['Front Camera'].str.extract(r'(\d+)MP')
    df['Front Camera MP'] = pd.to_numeric(df['Front Camera MP'], errors='coerce')

    df = df.dropna()
    df = df.drop(['Phone Name', 'Battery', 'Back/Rare Camera', 'Front Camera'], axis=1)

    columns_to_encode = ["Brand Label", "Processor"]
    label_encoder = LabelEncoder()
    for i in columns_to_encode:
        df[i] = label_encoder.fit_transform(df[i])

    return df


df = clean_and_transform_data(df)

# Split the data into features (X) and target (y)
X = df.drop(['Price in INR'], axis=1)
y = df[['Price in INR']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# Print the coefficients and MSE
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)


# Test
test_samples = input_data_set.loc[[20, 35, 320, 345]]
new_rows_to_test = test_samples
new_rows_to_test = clean_and_transform_data(new_rows_to_test)
new_rows_to_test = new_rows_to_test.drop(['Price in INR'], axis=1)
predictions = model.predict(new_rows_to_test)

count = 0
print('\nActual Price \t predicted price')
for index, row in test_samples.iterrows():
    print(row['Price in INR'], '\t', predictions[count])
    count = count+1
