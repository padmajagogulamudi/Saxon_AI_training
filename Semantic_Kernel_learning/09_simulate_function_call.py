from semantic_kernel.contents import (
    ChatHistory,
    ChatMessageContent,
    FunctionCallContent,
    FunctionResultContent
)
from semantic_kernel.contents.utils.author_role import AuthorRole


history = ChatHistory()

function_call = FunctionCallContent(
    name="get_employee_role-Employee",
    id="123",
    arguments='{"employee_id": "EMP101"}'
)

function_result = FunctionResultContent(
    name="get_employee_role-Employee",
    id="123",
    result="Software Engineer"
)

history.add_message(
    ChatMessageContent(
        role=AuthorRole.ASSISTANT,
        items=[function_call]
    )
)

history.add_message(
    ChatMessageContent(
        role=AuthorRole.TOOL,
        items=[function_result]
    )
)

print(history)