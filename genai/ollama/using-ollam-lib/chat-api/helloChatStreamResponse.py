import ollama

response = ollama.chat(
    model = "llama3.2",
    messages = [
        {"role" : "user", "content" : "Tell me about Solar System"}
    ],
    stream = True
)

for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)