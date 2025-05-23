from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage, AIMessage

# Create the chat model using the latest Ollama version of LLaMA 3
chat = ChatOllama(model="llama3.2")

conversation = []

print("💬 Start chatting with LLaMA 3! Type 'exit' to quit.\n")

while True:
    user_input = input("🧑 You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Ending chat. Goodbye!")
        break

    # Add user's message to the conversation
    conversation.append(HumanMessage(content=user_input))

    # Use `invoke()` instead of `__call__()`
    response = chat.invoke(conversation)

    # Add AI's response
    conversation.append(AIMessage(content=response.content))

    # Print AI's response
    print(f"🤖 AI: {response.content}\n")
