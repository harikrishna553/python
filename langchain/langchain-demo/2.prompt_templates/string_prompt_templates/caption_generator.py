from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Step 1: Define the prompt template
prompt_template = PromptTemplate.from_template(
    "Write a creative Instagram caption for a {business_type} that wants to attract new customers in 20 words maximum."
)

# Step 2: Choose a business type
variables = {"business_type": "coffee shop"}

# Step 3: Format the prompt with the input
formatted_prompt = prompt_template.format(**variables)

# Optional: Print formatted prompt
print("Formatted Prompt:\n", formatted_prompt)

# Step 4: Use Ollama with the LLaMA 3.2 model
llm = ChatOllama(model="llama3.2")

# Step 5: Get LLM response
response = llm.invoke(formatted_prompt)

# Step 6: Output result
print("Generated Caption:\n", response.content)
