from langchain.llms import Ollama
from langchain.agents import initialize_agent, Tool

####
# An agent typically functions as a loop that:

# Receives an Input Prompt: The user gives instructions or asks a question.
# Selects the Right Tool: Based on the prompt, the agent decides if it needs to use an external tool or answer directly.
# Executes an Action: If needed, the agent calls a tool with the appropriate inputs.
# Observes the Result: The agent reviews the tool's output.
# Generates a Response: It combines the tool output (if any) with its reasoning to provide the final response to the user.

#####
# Step 1: Initialize the Ollama LLM
llm = Ollama(model="llama3.2", verbose=True)

# Step 2: Define Tools
# Tool 1: A greeting tool
def hello_tool(input_text: str) -> str:
    """A tool that simply returns a hello message."""
    return f"Hello, {input_text}! Welcome to the Ollama-powered agent."

hello_tool_instance = Tool(
    name="HelloTool",
    func=hello_tool,
    description="Use this tool to greet someone by name or input text."
)

# Tool 2: A calculator tool for multiplication
def calc_tool(input_text: str) -> str:
    """A tool that multiplies two numbers provided as input."""
    try:
        # Parse the input for two numbers
        numbers = input_text.split()
        if len(numbers) != 2:
            return "Error: Please provide exactly two numbers separated by a space."
        num1, num2 = map(float, numbers)  # Convert inputs to floats
        result = num1 * num2
        return f"The result of multiplying {num1} and {num2} is {result}."
    except ValueError:
        return "Error: Ensure that both inputs are valid numbers."

calc_tool_instance = Tool(
    name="CalcTool",
    func=calc_tool,
    description="Use this tool to multiply two numbers. Provide the numbers separated by a space."
)

# Step 3: Create an Agent
tools = [hello_tool_instance, calc_tool_instance]
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Step 4: Use the Agent with Controlled Behavior
if __name__ == "__main__":
    print("Welcome to the Ollama-powered Multiplication Agent!")
    print("Type 'exit' to quit.")
    while True:
        print("\nOptions:")
        print("1. Type a name or greeting prompt for the HelloTool.")
        print("2. Enter two numbers separated by a space for the CalcTool.")
        user_input = input("Your input: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        try:
            response = agent.run(user_input)
            print("Agent Response:", response)
        except Exception as e:
            print("An error occurred:", e)
