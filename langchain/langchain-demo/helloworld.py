from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage

def main():
    # Use Ollama with the LLaMA 3.2 model
    chat = ChatOllama(model="llama3.2")

    # Ask a question using `.invoke()`
    response = chat.invoke([HumanMessage(content="Tell me a fun fact about space.")])

    # Print the response
    print("Ollama says:", response.content)

if __name__ == "__main__":
    main()

