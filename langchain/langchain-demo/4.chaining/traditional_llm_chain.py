from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain

# Step 1: Define a prompt template for startup ideas
summary_template = """
You are a startup consultant.

Given the description of a startup idea: {idea}

Please provide:
1. A compelling 2-3 sentence elevator pitch.
2. Two potential challenges this startup might face.
"""

prompt = PromptTemplate(
    input_variables=["idea"],
    template=summary_template
)

# Step 2: Initialize the local LLM (Ollama with LLaMA 3.2)
llm = ChatOllama(model="llama3.2")

# Step 3: Create the chain using LLMChain
chain = LLMChain(prompt=prompt, llm=llm)

# Step 4: User interaction and invocation
def main():
    print("Enter your startup idea:")
    user_input = input("> ")

    print("\nAnalyzing your startup idea...\n")
    result = chain.invoke({"idea": user_input})  # LLMChain uses .run()
    print(result)

if __name__ == "__main__":
    main()
