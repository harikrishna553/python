# Step 1: Import the PDF loader
from langchain_community.document_loaders import PyPDFLoader

# Step 2: Provide the path to your PDF
pdf_path = "time_machine.pdf"  # This could be any PDF file

# Step 3: Initialize the loader
loader = PyPDFLoader(pdf_path)

# Step 4: Load the document
docs = loader.load()

# Step 5: Inspect the result
print(f"Total pages loaded: {len(docs)}")
print(f"Type of docs[0]: {type(docs[0])}")
print(f"First page content:\n{docs[0].page_content[:500]}")  # First 500 chars
print(f"Metadata:\n{docs[0].metadata}")
