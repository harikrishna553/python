# Import the pandas Library.
import pandas as pd

# Specify the file path to the CSV file relative to the project directory.
file_path = '../../data/csv/ipl_matches.csv'

# Set the maximum number of columns to display as unlimited
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

print(df.iloc[:5, :4] )