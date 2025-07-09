from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# Set user-agent for web scraping
os.environ['USER_AGENT'] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/134.0.0.0 Safari/537.36"
)

# Step 1: Load content from the website
url = "https://self-learning-java-tutorial.blogspot.com/2024/06/understanding-dual-write-and-effective.html"
loader = WebBaseLoader(url)
documents = loader.load()

# Step 2: Chunk the document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

# Step 3: Generate embeddings using Ollama
embedding = OllamaEmbeddings(model="mxbai-embed-large")
db = FAISS.from_documents(chunks, embedding)

# Step 4: Perform similarity search
# query = "What is the Capital of India"
query = "What is Transactional Outbox Pattern?"
results = db.similarity_search(query, k=5)

# Step 5: Prepare context and prompt
llm = ChatOllama(model="llama3.2")
retrieved_context = "\n\n".join([doc.page_content for doc in results])

system_persona = (
    "You are a helpful AI assistant. Answer only based on the content provided between "
    "the <context> and </context> tags. If the answer is not found in the context, say 'I don't know.'\n\n"
    f"<context>\n{retrieved_context}\n</context>"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_persona),
    ("user", "{input}")
])

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Step 6: Ask the question and get the response
response = chain.invoke({"input": query})

# Final Output
# print(f"\n***** System Persona *****\n{system_persona}")
print(f"\n***** Query *****\n{query}")
print(f"\n***** Response *****\n{response}")