from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

# Initialize LLM
llm = ChatOllama(model="llama3.2")

# Manual memory store for all chat sessions
memory_store = {}

def get_session_history(session_id):
    if session_id not in memory_store:
        memory_store[session_id] = []
    return memory_store[session_id]

def update_session_history(session_id, message):
    memory_store[session_id].append(message)

# ---------- Chat Session 1 ----------
session_id_1 = "chat_1"
history_1 = get_session_history(session_id_1)

# User 1 sends a message
user_msg_1 = HumanMessage(content="Hi, my name is Krishna.")
update_session_history(session_id_1, user_msg_1)

# Bot 1 responds
response_1 = llm.invoke(history_1)
update_session_history(session_id_1, AIMessage(content=response_1.content))
print(f"Bot1: {response_1.content}")

# Follow-up message from User 1
follow_up_1 = HumanMessage(content="What's my name?")
update_session_history(session_id_1, follow_up_1)

# Bot 1 responds again
response_1_followup = llm.invoke(history_1)
update_session_history(session_id_1, AIMessage(content=response_1_followup.content))
print(f"Bot1: {response_1_followup.content}")

# ---------- Chat Session 2 ----------
session_id_2 = "chat_2"
history_2 = get_session_history(session_id_2)

# User 2 sends a message
user_msg_2 = HumanMessage(content="Hey, I am Ram.")
update_session_history(session_id_2, user_msg_2)

# Bot 2 responds
response_2 = llm.invoke(history_2)
update_session_history(session_id_2, AIMessage(content=response_2.content))
print(f"Bot2: {response_2.content}")

# Follow-up message from User 2
follow_up_2 = HumanMessage(content="Do you remember my name?")
update_session_history(session_id_2, follow_up_2)

# Bot 2 responds again
response_2_followup = llm.invoke(history_2)
update_session_history(session_id_2, AIMessage(content=response_2_followup.content))
print(f"Bot2: {response_2_followup.content}")
