import ollama

response = ollama.chat(
    model = "llama3.2",
    messages = [
        {"role" : "user", "content" : "Tell me about Solar System"}
    ]
)

print(response["message"]["content"])