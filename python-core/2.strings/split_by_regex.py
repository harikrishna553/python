import re

str = 'Hi there, 123 How are 456 you'
split_by_space = re.split(r"\s+", str)
split_by_digits = re.split(r"\d+", str)

print(f'split_by_space : {split_by_space}')
print(f'split_by_digits : {split_by_digits}')