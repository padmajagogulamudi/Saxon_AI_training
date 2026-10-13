import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from semantic_kernel.agents import ChatCompletionAgent
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
            "Explain concepts in simple English and give a short example "
            "when useful."
        ),
    )

    question = "What is a Python function? Explain with a simple example."

    async for response in agent.invoke(messages=question):
        print("Agent:", response.content)


if __name__ == "__main__":
    asyncio.run(main())