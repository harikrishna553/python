from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load text file
loader = TextLoader("multiverse.txt")
docs = loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

embeddings = OllamaEmbeddings(model="mxbai-embed-large")
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever()

prompt = PromptTemplate.from_template("""
You are an expert assistant. Use the following context to answer the question.
If you don't know the answer, say you don't know.

Context:
{context}

Question: {input}
""")

llm = ChatOllama(model="llama3.2")

# Create a chain using function composition
retrieval_chain = (
    {"context": retriever, "input": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Invoke the chain with just the question (no dictionary needed)
response = retrieval_chain.invoke("Tell me about Multiverse Voyagers Inc")
print(response)