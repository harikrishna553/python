from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

# Initialize the embedding model
embedding = OllamaEmbeddings(model="mxbai-embed-large")

# Sample documents for a fictional Time Machine company
documents = [
    Document(page_content="ChronoCorp launched its first commercial time machine in 2042."),
    Document(page_content="ChronoCorp's time portal can transport humans to any year between 1900 and 2200."),
    Document(page_content="The ChronoX Model 3 uses quantum tachyons to stabilize time loops."),
    Document(page_content="Time travel is restricted to government-approved missions due to paradox risks."),
    Document(page_content="ChronoCorp's latest upgrade includes a failsafe to prevent timeline corruption."),
]

# Embed and store in FAISS
db = FAISS.from_documents(documents, embedding)

# Run a semantic query
query = "Which model of time machine uses quantum particles?"
results = db.similarity_search(query, k=2)

# Display the results
print("Query:", query)
print("\nTop Matching Documents:")
for i, res in enumerate(results, 1):
    print(f"{i}. {res.page_content}")
