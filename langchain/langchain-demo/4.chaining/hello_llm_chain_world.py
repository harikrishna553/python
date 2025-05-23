from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Step 1: Define a new prompt template for startup ideas
prompt = PromptTemplate.from_template("""
You are a startup consultant.

Given the description of a startup idea: {idea}

Please provide:
1. A compelling 2-3 sentence elevator pitch.
2. Two potential challenges this startup might face.
""")

# Step 2: Initialize the local LLM (Ollama with LLaMA 3.2)
llm = ChatOllama(model="llama3.2")

# Step 3: Create the chain using the pipe operator
chain = prompt | llm

# Step 4: User interaction and invocation
def main():
    print("🚀 Enter your startup idea:")
    user_input = input("> ")

    print("\n💡 Analyzing your startup idea...\n")
    result = chain.invoke({"idea": user_input})
    print(result.content)

if __name__ == "__main__":
    main()
