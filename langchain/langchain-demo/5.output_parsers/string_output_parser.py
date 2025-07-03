from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableSequence
from langchain.agents import (
	create_react_agent,
	AgentExecutor
)

# 1. Define the prompt template
prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")

# 2. Initialize the LLM
llm = ChatOllama(model="llama3.2")

# 3. Initialize the output parser
output_parser = StrOutputParser()

# 4. Chain the components
chain: RunnableSequence = prompt | llm | output_parser

# 5. Run the chain with input
result = chain.invoke({"product": "electric bikes"})

# 6. Print the result
print(result)
