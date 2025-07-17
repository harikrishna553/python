from langgraph.graph import StateGraph, START, END
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from typing_extensions import TypedDict
from typing import List
import sys

class ChatState(TypedDict):
    messages: List[BaseMessage]
    choice: str

try:
    llm = ChatOllama(
        model="llama3.2",  # Updated to use llama3.2 (more common format)
        temperature=0.7,   # Add some creativity
        timeout=30         # Add timeout for better error handling
    )
except Exception as e:
    print(f"Error initializing ChatOllama: {e}")
    print("Please ensure Ollama is running and the model is available.")
    sys.exit(1)

def user_node(state: ChatState) -> ChatState:
    print("\n" + "="*60)
    print("AI Assistant - Type 'exit' to quit")
    print("="*60)
    
    user_input = input("You: ").strip()
    
    if not user_input:
        user_input = "Hello"  # Default message if empty input
    
    return {
        "messages": state["messages"] + [HumanMessage(content=user_input)],
        "choice": user_input.lower().strip()
    }

def llm_node(state: ChatState) -> ChatState:
    try:
        response = llm.invoke(state["messages"])
        print(f"AI: {response.content}")
        
        return {
            "messages": state["messages"] + [AIMessage(content=response.content)],
            "choice": state["choice"]
        }
    except Exception as e:
        error_message = f"Sorry, I encountered an error: {str(e)}"
        print(f"AI: {error_message}")
        
        return {
            "messages": state["messages"] + [AIMessage(content=error_message)],
            "choice": state["choice"]
        }

def take_decision(state: ChatState) -> str:
    if state.get("choice") == "exit":
        print("\nGoodbye!")
        return END
    return "llm_node"

def create_chatbot_graph() -> StateGraph:
    graph_builder = StateGraph(ChatState)
    
    # Add nodes
    graph_builder.add_node("user_node", user_node)
    graph_builder.add_node("llm_node", llm_node)
    
    # Set entry point
    graph_builder.set_entry_point("user_node")
    
    # Add edges
    graph_builder.add_conditional_edges("user_node", take_decision)
    graph_builder.add_edge("llm_node", "user_node")  # Loop back to user
    
    return graph_builder.compile()

def main():
    print("LangGraph Chatbot Demo")
    print("=" * 60)
    print("Welcome! You can start chatting with the AI assistant.")
    print("Type 'exit' when you want to end the conversation.")
    print("=" * 60)
    
    try:
        # Create the graph
        graph = create_chatbot_graph()
        
        # Start the conversation
        initial_state = {
            "messages": [],
            "choice": ""
        }
        
        graph.invoke(initial_state)
        
    except KeyboardInterrupt:
        print("\n\nConversation interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please check your Ollama installation and try again.")

if __name__ == "__main__":
    main()
