import re

pattern1 = r"ab*c"  # Matches "a" followed by zero or more "b"s and then "c"
pattern2 = r"(ab)*c"  # Matches zero or more repetitions of "ab" followed by "c"
pattern3 = r"(abc)*"  # Matches zero or more repetitions of "abc"

text1 = "abc"
text2 = "abbbc"
text3 = "abcabcdef"

print(f'({pattern1}, {text1}) : {re.match(pattern1, text1)}')
print(f'({pattern2}, {text1}) : {re.match(pattern2, text1)}')
print(f'({pattern3}, {text1}) : {re.match(pattern2, text1)}')

print(f'\n({pattern1}, {text2}) : {re.match(pattern1, text2)}')
print(f'({pattern2}, {text2}) : {re.match(pattern2, text2)}')
print(f'({pattern3}, {text2}) : {re.match(pattern2, text2)}')

print(f'\n({pattern1}, {text3}) : {re.match(pattern1, text3)}')
print(f'({pattern2}, {text3}) : {re.match(pattern2, text3)}')
print(f'({pattern3}, {text3}) : {re.match(pattern2, text3)}')
