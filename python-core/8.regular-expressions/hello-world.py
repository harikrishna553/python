import re

yearRegex = re.compile(r'[1-9]\d{3}')
yearsMatched = yearRegex.search('Hi, My name is Krishna, and my birth year is 1989 and I graduated on 2009')

if yearsMatched:
    matched_year = yearsMatched.group()
    print("Matched year:", matched_year)
else:
    print("No match found.")
