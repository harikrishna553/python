from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.documents import Document

# A simple prompt template
prompt = PromptTemplate.from_template(
    """
    Use the following documents to answer the question:
    
    {context}
    
    Question: {input}
    """
)

# Define the LLM
llm = ChatOllama(model="llama3.2")

# Create the document chain
chain = create_stuff_documents_chain(llm, prompt)

# Wrap your strings into Document objects
docs = [
    Document(page_content="ChronoCorp launched its first commercial time machine in 2042."),
    Document(page_content="It was founded by a group of quantum physicists in 2038.")
]

# Run the chain
result = chain.invoke({
    "input": "What is ChronoCorp?",
    "context": docs
})

print(result)
