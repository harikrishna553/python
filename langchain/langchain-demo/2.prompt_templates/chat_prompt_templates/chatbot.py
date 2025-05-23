from langchain_ollama import ChatOllama

# Initialize model
llm = ChatOllama(model="llama3.2")

# Start with system message to set behavior
chat_history = [
    {"role": "system", "content": "You are a friendly chatbot, that answer user questions"}
]

def chat_with_model(user_input):
    # Append user message to history
    chat_history.append({"role": "user", "content": user_input})

    # Format messages for the model
    # (Here we assume llm.invoke accepts list of dicts with role and content)
    response = llm.invoke(chat_history)

    # Append assistant response to history
    chat_history.append({"role": "assistant", "content": response.content})

    return response.content

# Example interactive loop
if __name__ == "__main__":
    print("Chatbot (type 'exit' to quit)")
    while True:
        print( "*" * 50,)
        user_text = input("You: ")
        if user_text.lower() == "exit":
            break
        reply = chat_with_model(user_text)
        print("Tutor:", reply)
