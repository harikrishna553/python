from spacy_demo.utils import file_util
from spacy_demo.utils import spacy_util

text = file_util.read_file_content('../data/test_content.txt')
nlp = spacy_util.nlp_model()

doc = nlp(text)

for sentence in doc.sents:
    print(sentence)