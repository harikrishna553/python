from spacy_demo.utils import file_util
from spacy_demo.utils import spacy_util

text = file_util.read_file_content('../data/test_content.txt')
#print(text)
nlp = spacy_util.nlp_model()

doc = nlp(text)

print(f'length of actual text is {len(text)}')
print(f'length of actual doc is {len(doc)}')

for token in doc[:20]:
    print(token)
