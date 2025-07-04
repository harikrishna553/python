from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

# Load your text file
loader = TextLoader("demo.txt")
documents = loader.load()

# Initialize the CharacterTextSplitter
text_splitter = CharacterTextSplitter(
    separator="\n",        # You can also try " " or other separators
    chunk_size=100,
    chunk_overlap=20
)

# Split the document
split_docs = text_splitter.split_documents(documents)

print(f"Total Splits : {len(split_docs)}")
i=1
for doc in split_docs:
    print(f"Split {i}")
    print(f"{doc.page_content}")
    print(f"Total length : {len(doc.page_content)}\n")
    i = i + 1