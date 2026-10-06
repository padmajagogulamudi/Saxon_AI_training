
import asyncio
import os

from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.open_ai import AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory

from plugins.employee_plugin import EmployeePlugin


async def main():

    load_dotenv()

    kernel = Kernel()

    kernel.add_service(
       AzureChatCompletion(
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    endpoint=os.getenv("AZURE_OPENAI_BASE_URL"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)
    )

    kernel.add_plugin(
        EmployeePlugin(),
        plugin_name="Employee"
    )

    execution_settings = AzureChatPromptExecutionSettings()

    execution_settings.function_choice_behavior = (
        FunctionChoiceBehavior.Auto()
    )

    history = ChatHistory()

    history.add_user_message(
        "What is the role of employee EMP101?"
    )

    chat_completion = kernel.get_service(
        type=ChatCompletionClientBase
    )

    response = await chat_completion.get_chat_message_content(
        chat_history=history,
        settings=execution_settings,
        kernel=kernel
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())
