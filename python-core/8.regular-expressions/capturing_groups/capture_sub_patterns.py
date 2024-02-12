import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"(\w+) (\w+) jumps"  # Capture two word groups
match = re.search(pattern, text)

if match:
    matched_text = match.group()  # Access captured groups
    print(f"matched_text : {matched_text}")

    matched_text = match.group(0)  # Access captured groups
    print(f"matched_text : {matched_text}")

    color = match.group(1)
    animal = match.group(2)
    print(f"Color: {color}, Animal: {animal}")

    # To retrive all the groups
    color, animal = match.groups()
    print(f"Color: {color}, Animal: {animal}")
else:
    print('No match found')