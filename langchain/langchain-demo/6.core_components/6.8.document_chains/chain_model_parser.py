from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage

# Define the LLM
llm = ChatOllama(model="llama3.2")

parser = StrOutputParser()

# Create the document chain
chain = llm | parser

messages = [
    SystemMessage(content="You are Alice, a helpful Robot to assist Humans...."),
    HumanMessage(content="Who are you? Explain me in single line")
]

result = chain.invoke(messages)

print(result)
