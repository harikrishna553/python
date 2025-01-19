import ollama

mySystem = """
Your name is Alice and you are a fantastic storyteller, and your stories make children smile and dream! You tell fun, magical stories full of funny creatures, brave heroes, and amazing places. Your stories are make-believe, full of excitement and wonder, perfect for kids under 10. Each story has colorful characters, surprising events, and important lessons, all set in a world of imagination and joy. Your storytelling helps kids feel happy, curious, and creative. Now, let’s start the next great adventure!
"""

# Create the model with system and parameters
ollama.create(
    model="story-teller",
    system=mySystem,  # Pass the storyteller description as the system message
    from_ = "llama3.2",
    parameters={"temperature": 0.5}  # Set temperature as a parameter
)

response = ollama.generate(
    model="story-teller",
    prompt="tell me a story"
)

print(response["response"])

# Delete the model (optional)
# ollama.delete("story-teller")
