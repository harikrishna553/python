import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Krishna', 'Sailu', 'Joel', 'Chamu', 'Jitendra', "Krishna"],
        'Age': [34, 35, 234, 35, 52, 34],
        'City': ['Bangalore', 'Hyderabad', 'Hyderabad', 'Chennai', 'Bangalore', 'Chennai'],
        'Hobbies': ['Football,Cricket', 'Tennis, cricket', 'Trekking, reading books', 'Chess', 'Read Books', 'Cricket']}
df = pd.DataFrame(data)

print('Original DataFrame')
print(df)

# Convert the column values to lower case to perform the case insensitive search
book_in_hobbies = df['Hobbies'].str.lower().str.contains('book')
persons_hobby_contain_book = df[book_in_hobbies]

print('\nBoolean series to find the people whose hobby contain the string "book"\n', book_in_hobbies)
print('\nPeople whose hobby contains the string "book"\n',persons_hobby_contain_book)

book_in_hobbies = df['Hobbies'].str.contains('book', case=False)
persons_hobby_contain_book = df[book_in_hobbies]
print('\nBoolean series to find the people whose hobby contain the string "book"\n', book_in_hobbies)
print('\nPeople whose hobby contains the string "book"\n',persons_hobby_contain_book)

# Check for substring in multiple columns
contains_c = df[['Name', 'City', 'Hobbies']].apply(lambda x: x.str.contains('c', case=False))
print('\nRow that contains the character "c" case insensitive : \n', contains_c)