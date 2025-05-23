from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# Step 1: Create ChatPromptTemplate
prompt_template = ChatPromptTemplate([
    ("system", "You are a friendly Telugu language tutor. Help the user learn by giving examples and simple explanations."),
    ("user", "Can you give me a short Telugu sentence about {topic}? Also, translate it to English.")
])

# Step 2: Set input variables
variables = {
    "topic": "the weather"
}

# Step 3: Format the messages
messages = prompt_template.invoke(variables)

# Step 4: Initialize the LLaMA model
llm = ChatOllama(model="llama3.2")

# Step 5: Send the messages to the LLM
response = llm.invoke(messages)

# Step 6: Output the response
print("\nGenerated Response:\n", response.content)
