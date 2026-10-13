import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from semantic_kernel.agents import (
    ChatCompletionAgent,
    ChatHistoryAgentThread,
)
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion


load_dotenv(Path(__file__).resolve().parent / ".env")


async def main():
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")

    if not all([endpoint, api_key, deployment, api_version]):
        raise ValueError(
            "Missing Azure OpenAI configuration. Check your .env file."
        )

    chat_service = AzureChatCompletion(
        deployment_name=deployment,
        endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
    )

    agent = ChatCompletionAgent(
        service=chat_service,
        name="PythonTutor",
        instructions=(
            "You are a friendly Python tutor. "
            "Remember the conversation and explain concepts "
            "clearly for beginners."
        ),
    )

    thread = None

    questions = [
        "My name is Padmaja. I am learning Python functions.",
        "What topic am I learning?",
        "Give me a simple example of that topic."
    ]

    for question in questions:
        print(f"\nUser: {question}")

        response = await agent.get_response(
            messages=question,
            thread=thread,
        )

        print(f"Agent: {response.message.content}")

        thread = response.thread

    if thread is not None:
        await thread.delete()


if __name__ == "__main__":
    asyncio.run(main())
    