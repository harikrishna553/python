from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from typing import List
import random

# Step 1: Define the enhanced state
class State(TypedDict):
    messages: List[str]

# Step 2: Define nodes (functions)
def create_document(state: State) -> State:
    return {**state, "messages": state["messages"] + ["Document Created"]}

def review_document(state: State) -> State:
    return {**state, "messages": state["messages"] + ["Document Reviewed"]}

def approve_document(state: State) -> State:
    return {**state, "messages": state["messages"] + ["Document Approved"]}

def fix_comments(state: State) -> State:
    return {**state, "messages": state["messages"] + ["Fix Comments Made"]}

# Step 3: Conditional edge with random logic
def route_review(state: State) -> str:
    choice = random.choice(["approve", "fix_comments"])
    return choice

# Step 4: Build the graph
graph = StateGraph(State)

graph.add_node("create", create_document)
graph.add_node("review", review_document)
graph.add_node("approve", approve_document)
graph.add_node("fix_comments", fix_comments)

graph.add_edge(START, "create")
graph.add_edge("create", "review")

# Conditional transition from review
graph.add_conditional_edges("review", route_review)

# Loop back from fix_comments to review
graph.add_edge("fix_comments", "review")

# Final step
graph.add_edge("approve", END)

# Step 5: Compile the graph
builder = graph.compile()

# Step 6: Run the graph
if __name__ == "__main__":
    input_state = {"messages": ["START"]}

    print("=== Randomized Workflow ===")
    final_state = builder.invoke(input_state)

    for step in final_state["messages"]:
        print("•", step)
