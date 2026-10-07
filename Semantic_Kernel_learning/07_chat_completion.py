import asyncio
import os

from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.open_ai import AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory


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

    chat_completion = kernel.get_service(
        type=ChatCompletionClientBase
    )

    execution_settings = AzureChatPromptExecutionSettings()

    history = ChatHistory()

    history.add_system_message(
        "You are a helpful assistant."
    )

    history.add_user_message(
        "What is Semantic Kernel?"
    )

    response = await chat_completion.get_chat_message_content(
        chat_history=history,
        settings=execution_settings
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())