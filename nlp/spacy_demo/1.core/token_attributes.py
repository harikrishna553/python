from spacy_demo.utils import file_util
from spacy_demo.utils import spacy_util

text = file_util.read_file_content('../data/test_content.txt')
nlp = spacy_util.nlp_model()

doc = nlp(text)

# Print first 20 tokens
for token in doc[:5]:
    # Print token attributes
    print(f'\ntext : {token.text}')
    print(f'left_edge : {token.left_edge}')
    print(f'right_edge : {token.right_edge}')
    print(f'ent_type : {token.ent_type}')
    print(f'ent_type : {token.ent_type_}')
    print(f'ent_iob : {token.ent_iob_}')
    print(f'lemma : {token.lemma_}')
    print(f'morph : {token.morph}')
    print(f'pos_ : {token.pos_}')
    print(f'dep_ : {token.dep_}')
    print(f'lang_ : {token.lang_}')

