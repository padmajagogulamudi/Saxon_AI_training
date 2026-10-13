from semantic_kernel import Kernel
from semantic_kernel.contents import ChatHistory, ChatMessageContent
from semantic_kernel.contents.utils.author_role import AuthorRole


kernel = Kernel()

history = ChatHistory()

message = ChatMessageContent(
    role=AuthorRole.USER,
    name="Padmaja",
    content="What is Semantic Kernel?"
)

history.add_message(message)

print(history)