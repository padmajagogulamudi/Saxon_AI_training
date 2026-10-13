import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from semantic_kernel.agents import (
    ChatCompletionAgent,
    SequentialOrchestration,
)
from semantic_kernel.agents.runtime import InProcessRuntime
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents import ChatMessageContent


load_dotenv(Path(__file__).resolve().parent / ".env")


def create_agent(service, name, instructions):
    return ChatCompletionAgent(
        service=service,
        name=name,
        instructions=instructions,
    )


def agent_response_callback(message: ChatMessageContent) -> None:
    print(f"\n--- {message.name} ---")
    print(message.content)


async def main():
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")

    if not all([endpoint, api_key, deployment, api_version]):
        raise ValueError("Check your Azure OpenAI settings in .env")

    service = AzureChatCompletion(
        deployment_name=deployment,
        endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
    )

    analyst = create_agent(
        service,
        "Analyst",
        (
            "You are a marketing analyst. Identify the product's key "
            "features, target audience, and unique selling points. "
            "Present your analysis clearly."
        ),
    )

    writer = create_agent(
        service,
        "Copywriter",
        (
            "You are a marketing copywriter. Use the analysis you receive "
            "to write a short, attractive product description. "
            "Do not invent unsupported product features."
        ),
    )

    editor = create_agent(
        service,
        "Editor",
        (
            "You are a professional editor. Improve the draft's grammar, "
            "clarity, and readability. Return only the polished description."
        ),
    )

    orchestration = SequentialOrchestration(
        members=[analyst, writer, editor],
        agent_response_callback=agent_response_callback,
    )

    runtime = InProcessRuntime()
    runtime.start()

    try:
        result = await orchestration.invoke(
            task=(
                "Create a product description for a reusable stainless "
                "steel water bottle that keeps drinks cold for 24 hours "
                "and is designed for students and office workers."
            ),
            runtime=runtime,
        )

        final_output = await result.get(timeout=120)

        print("\n========== FINAL RESULT ==========")
        print(final_output)

    finally:
        await runtime.stop_when_idle()


if __name__ == "__main__":
    asyncio.run(main())