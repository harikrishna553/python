from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

# Hardcode LangSmith config here
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"] = "......"  # Replace with your actual API key
os.environ["LANGSMITH_PROJECT"] = "hello-world"

# Step 1: Load local LLaMA 3 model from Ollama
llm = ChatOllama(model="llama3.2")

# Define system message (assistant persona)
system_persona = """
You are a helpful Assistant — an intelligent, AI-powered chatbot designed to support users of data visualization and analytics tools...

...

Response guidelines:
- Maintain a friendly, professional, and helpful tone.
- Always stay within the domain of data visualization and related tools.
- If a user asks a question that is out of scope (e.g., about politics, unrelated software, general science, history, or space), respond politely and clearly:
  - "That topic is outside my expertise as a Data Visualization Assistant. Let me know how I can help you with visualizations or dashboards!"
- Do not fabricate information...
"""

# Create chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", system_persona),
    ("user", "{input}")
])

# Add output parser
output_parser = StrOutputParser()

# Chain: Prompt → LLM → Output Parser
chain = prompt | llm | output_parser

# Traceable function to track in LangSmith
@traceable(name="HelloWorld DataViz Assistant")
def run_chain(user_input):
    return chain.invoke({"input": user_input})

# Test the chain
print(run_chain("What is Tableau, explain me in 2 lines maximum"))
print("-" * 50)
print(run_chain("Tell me about Solar System"))

