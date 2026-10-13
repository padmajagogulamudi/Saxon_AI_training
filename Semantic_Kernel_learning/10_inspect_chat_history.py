from semantic_kernel.contents import ChatHistory

history = ChatHistory()

history.add_system_message(
    "You are a helpful assistant."
)

history.add_user_message(
    "What is Semantic Kernel?"
)

history.add_assistant_message(
    "Semantic Kernel is an SDK for integrating AI into applications."
)

print("Number of messages:", len(history))

for message in history:
    print("Role:", message.role)
    print("Content:", message.content)
    print()