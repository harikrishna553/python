import ollama

response = ollama.generate(
    model = "llama3.2",
    prompt = "Tell me a Joke"
)

print(response["response"])
