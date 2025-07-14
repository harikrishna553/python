from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from typing import List

# Step 1: Define the enhanced state
class State(TypedDict):
    messages: List[str]

# Step 2: Define nodes (functions)
def create_document(state: State) -> State:
    # print("Document created")
    return {"messages": state["messages"] + ["Document Created"]}

def review_document(state: State) -> State:
    # print("Document reviewed")
    return {"messages": state["messages"] + ["Document Reviewed"]}

def approve_document(state: State) -> State:
    # print("Document approved")
    return {"messages": state["messages"] + ["Document Approved"]}

# Step 3: Build the graph
graph = StateGraph(State)
graph.add_node("create", create_document)
graph.add_node("review", review_document)
graph.add_node("approve", approve_document)

graph.add_edge(START, "create")
graph.add_edge("create", "review")
graph.add_edge("review", "approve")
graph.add_edge("approve", END)

# Step 4: Compile the graph
builder = graph.compile()

# Step 5: Run the graph
if __name__ == "__main__":
    input_state = {"messages": ["START"]}
    final_state = builder.invoke(input_state)
    
    print("\nWorkflow Steps:")
    for step in final_state["messages"]:
        print("•", step)
