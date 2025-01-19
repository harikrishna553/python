from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

import nltk
nltk.download('punkt_tab')
# print(nltk.data.path)

documentPath = "./data/timeTravel.pdf"
model = "llama3.2"

if documentPath:
    loader = UnstructuredPDFLoader(file_path=documentPath)
    data = loader.load()
    #print("Done loading the pdf file")
else:
    print("Upload a PDF file")

# Preview First few line of the pdf document
content = data[0].page_content
#print(content[:100])

# Extract the text from pdf file and split into small chunks
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Split Chunk
textSplitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=300)
chunks = textSplitter.split_documents(data)
#print("Done Splitting....")
#print(f"Total Chunks are {len(chunks)}")
#print(f"First Chunk {chunks[0]}")

# Add embedding model
import ollama
ollama.pull("nomic-embed-text")

vectorDb = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="simple-rag",
)
#print("done adding to vector database....")


from langchain_ollama import ChatOllama
llm = ChatOllama(model=model)

## Retrieval
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever

queryPrompt = PromptTemplate(
    input_variables=["question"],
    template = """
You are an AI language model assistant. Your task is to generate appropriate Answer
 to the question by retrieving relevant documents from a vector database.
 Original question: {question}
"""
)

retriever = MultiQueryRetriever.from_llm(
    vectorDb.as_retriever(), llm, prompt=queryPrompt
)

# RAG prompt
template = """Answer the question based ONLY on the following context:
{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


# res = chain.invoke(input=("what is the document about?",))
# res = chain.invoke(
#     input=("what are the main points as a business owner I should be aware of?",)
# )
#res = chain.invoke(input=("What is Yearly dividend for Doom industries?"))
res = chain.invoke(input=("Summarize about time machine and doom industries?"))
print(res)
