from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load local model
llm = ChatOllama(model="llama3.2")

# Initial messages
messages = [
    SystemMessage(content="You are a friendly assistant who answers in a polite way.")
]

# Loop for ongoing chat
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("AI: It was a pleasure chatting with you. Goodbye!")
        break

    # Add new human message
    messages.append(HumanMessage(content=user_input))

    # Get model's response
    response = llm.invoke(messages)

    # Print and store the response
    print("AI:", response.content)
    messages.append(AIMessage(content=response.content))
