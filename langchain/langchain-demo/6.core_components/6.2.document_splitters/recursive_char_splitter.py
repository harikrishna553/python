from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step 1: Load the document
loader = PyPDFLoader("time_machine.pdf")
docs = loader.load()  # This gives you a list of Document objects

# Step 2: Initialize the splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

# Step 3: Split the document into chunks
final_documents = text_splitter.split_documents(docs)

# Step 4: Inspect the result
print(f"Total Chunks: {len(final_documents)}")
print(final_documents[0].metadata)
print(final_documents[0].page_content)
