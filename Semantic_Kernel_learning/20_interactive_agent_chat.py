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
            "You are a friendly Python tutor for beginners. "
            "Answer in simple English and use examples when helpful. "
            "Use the conversation history to understand follow-up questions."
        ),
    )

    thread: ChatHistoryAgentThread | None = None

    print("PythonTutor Agent")
    print("Ask a Python question. Type 'exit' to stop.")

    try:
        while True:
            question = input("\nYou: ").strip()

            if question.lower() == "exit":
                print("Chat ended.")
                break

            if not question:
                continue

            response = await agent.get_response(
                messages=question,
                thread=thread,
            )

            print(f"\nPythonTutor: {response.message.content}")

            thread = response.thread

    finally:
        if thread is not None:
            await thread.delete()


if __name__ == "__main__":
    asyncio.run(main())