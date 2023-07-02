# Import the pandas Library.
import pandas as pd

# Specify the file path to the CSV file relative to the project directory.
file_path = '../../../data/csv/ipl_matches.csv'

# Set options to display all columns and increase the maximum width to print the columns in same row
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

first_five_rows = df.head()
print("First five rows\n", first_five_rows)

first_two_rows = df.head(2)
print("\nFirst two rows\n", first_two_rows)

# Get the total number of rows using the len() function
total_rows = len(df)
total_rows_minus_three = total_rows-3
first_three_rows = df.head(-total_rows_minus_three)
print("\nFirst three rows\n", first_three_rows)