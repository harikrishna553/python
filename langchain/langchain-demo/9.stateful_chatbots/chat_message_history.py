from langchain_core.messages import AIMessage, HumanMessage
from langchain.memory import ChatMessageHistory

# Create a new message history for a session
history = ChatMessageHistory()

# Add some conversation messages
history.add_user_message("Hi")
history.add_ai_message("Hi, How can I help you")
history.add_user_message("My Name is Krishna")
history.add_ai_message("Hi Krishna, it is nice meeting you")

# View the stored history
for message in history.messages:
    print(message.type, "->", message.content)
