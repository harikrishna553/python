from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Step 1: Define a more complex prompt template with multiple placeholders
template = """
Write a persuasive product description for an e-commerce store.

Product Name: {product_name}
Category: {category}
Target Audience: {audience}
Tone: {tone}
Key Features: {features}
Style Guide: {style_guide}

Instructions:
- Keep it under 60 words
- Use the specified tone and follow the style guide
- Make it compelling for {audience}
- Emphasize unique features

Respond only with the product description text, no labels.
"""

# Step 2: Create the PromptTemplate
prompt_template = PromptTemplate.from_template(template)

# Step 3: Define input variables
variables = {
    "product_name": "AuroraGlow Smart Lamp",
    "category": "Home & Living",
    "audience": "tech-savvy millennials",
    "tone": "trendy and upbeat",
    "features": "voice control, customizable RGB lighting, sunrise alarm",
    "style_guide": "Use playful language, emojis allowed, avoid formal tone"
}

# Step 4: Format the prompt
formatted_prompt = prompt_template.format(**variables)
print("Formatted Prompt:\n", formatted_prompt)

# Step 5: Initialize the LLM
llm = ChatOllama(model="llama3.2")

# Step 6: Get response from LLM
response = llm.invoke(formatted_prompt)

# Step 7: Output result
print("\nGenerated Product Description:\n", response.content)
