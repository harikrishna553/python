from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

def main():
    # Load environment variables
    load_dotenv()

    # Use Ollama with the LLaMA 3.2 model
    chat = ChatOllama(model=os.environ.get("MODEL_TO_USE"))

    # Ask a question using `.invoke()`
    response = chat.invoke([HumanMessage(content="Tell me a fun fact about space.")])

    # Print the response
    print("Ollama says:", response.content)

if __name__ == "__main__":
    main()