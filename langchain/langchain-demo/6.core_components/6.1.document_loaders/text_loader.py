# Step 1: Import the text loader
from langchain_community.document_loaders import TextLoader

# Step 2: Create the loader
loader = TextLoader("text.txt")

# Step 3: Load the document
documents = loader.load()

# Step 4: View the result
print(documents[0].page_content)   # Text content
print(documents[0].metadata)       # Metadata like file name
