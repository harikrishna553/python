from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Define the LLM
llm = ChatOllama(model="llama3.2")

# Define the output parser
parser = StrOutputParser()

# Create a dynamic prompt template
template = ChatPromptTemplate.from_messages([
    ("system", "You are Alice, a helpful robot."),
    ("human", "{text}")
])

# Combine components using LCEL
chain = template | llm | parser

# Invoke the chain with runtime variables
input_data = {
    "text": "What is the Capital Of India?"
}

result = chain.invoke(input_data)

# Display the output
print(result)
