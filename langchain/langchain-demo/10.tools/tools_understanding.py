from langchain_ollama import ChatOllama
from langchain.agents import Tool
from pprint import pprint

# -------------------------------
# Weather and Cricket tools (mocked)
# -------------------------------
def get_weather(input: str) -> str:
    city = input.strip()
    # Mock response
    return f"The weather in {city} is 28°C, partly cloudy."

def get_live_cricket_news(input: str) -> str:
    # Mock response
    return "India vs Australia: India scores 245/3 in 35 overs. Kohli on 87*, Pandya on 45*."

# -------------------------------
# Tool registration
# -------------------------------
tools = [
    Tool(
        name="getWeather",
        func=get_weather,
        description="Get weather for a city. Input format: city name (e.g., 'Delhi')"
    ),
    Tool(
        name="liveCricketNews",
        func=get_live_cricket_news,
        description="Get current live cricket match news. Input: empty string or any string"
    )
]

# -------------------------------
# LLM with tools
# -------------------------------
llm = ChatOllama(model="llama3.2")
llm = llm.bind_tools(tools)

# -------------------------------
# Example prompt
# -------------------------------
response = llm.invoke("Give me the weather report for Bangalore.")
pprint(response)


# -------------------------------
# Tool call execution if any
# -------------------------------
tool_function_map = {tool.name: tool.func for tool in tools}
if hasattr(response, "tool_calls") and response.tool_calls:
    print("\n🔧 Executing tool calls:")
    for call in response.tool_calls:
        tool_name = call["name"]
        args = call["args"]
        arg_value = args.get("__arg1", "")  # Default to empty string

        if tool_name in tool_function_map:
            result = tool_function_map[tool_name](arg_value)
            print(f"{tool_name}({arg_value}) = {result}")
        else:
            print(f"Unknown tool: {tool_name}")
else:
    print("ℹ No tools were called by the LLM.")
