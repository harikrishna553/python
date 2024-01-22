from spacy_demo.utils import spacy_util
from spacy import displacy

text = 'Lahari enjoys playing Cricket...'
nlp = spacy_util.nlp_model()

doc = nlp(text)

# Print first 20 tokens
for token in doc[:]:
    print(f'{token.text}, {token.pos_}, {token.dep_}')

# Visualize the dependency parse tree using displacy.render
# displacy.render(doc, style="dep", options={'distance': 100})

# Visualize the dependency parse tree and save it as an image
output_path = "dependency_tree.svg"
svg = displacy.render(doc, style="dep", options={'distance': 100}, jupyter=False)

with open(output_path, "w", encoding="utf-8") as file:
    file.write(svg)

print(f"Dependency parse tree visualization saved to {output_path}")

# svg viewer
# https://www.svgviewer.dev/