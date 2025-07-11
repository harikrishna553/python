from fastapi import FastAPI
from langserve import add_routes

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the model
llm = ChatOllama(model="llama3.2")

# Create a prompt that takes a question
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Question: {question}")
])

# Output parser
parser = StrOutputParser()

# Build the chain
chain = prompt | llm | parser

# Create FastAPI app
app = FastAPI(
    title="Question Answering API",
    version="1.0",
    description="Ask any question, get a response using LLaMA 3.2"
)

# Add the chain as an API route
add_routes(app, chain, path="/ask-anything")

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=1234)
