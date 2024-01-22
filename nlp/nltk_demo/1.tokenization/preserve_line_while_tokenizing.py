import nltk
from nltk import word_tokenize

# Specify the path to your custom data directory
custom_data_directory = '/Users/Shared/nltk_data'

# Set the NLTK data directory to your custom directory
nltk.data.path.append(custom_data_directory)

# Tokenize text with explicit newline characters
text = "Test sentence ä,ö,üaaa"
tokens = word_tokenize(text, language='english')
print(tokens)

tokens = word_tokenize(text, language='german')
print(tokens)