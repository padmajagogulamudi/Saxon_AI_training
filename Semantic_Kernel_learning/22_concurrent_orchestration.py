import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from semantic_kernel.agents import (
    ChatCompletionAgent,
    ConcurrentOrchestration,
)
from semantic_kernel.agents.runtime import InProcessRuntime
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion


load_dotenv(Path(__file__).resolve().parent / ".env")


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

    student_advisor = ChatCompletionAgent(
        service=service,
        name="StudentAdvisor",
        instructions=(
            "Evaluate the product from a student's perspective. "
            "Focus on affordability, portability, and usefulness. "
            "Give a concise assessment."
        ),
    )

    office_advisor = ChatCompletionAgent(
        service=service,
        name="OfficeAdvisor",
        instructions=(
            "Evaluate the product from an office worker's perspective. "
            "Focus on convenience, durability, and daily office use. "
            "Give a concise assessment."
        ),
    )

    orchestration = ConcurrentOrchestration(
        members=[student_advisor, office_advisor],
    )

    runtime = InProcessRuntime()
    runtime.start()

    try:
        result = await orchestration.invoke(
            task=(
                "Evaluate a reusable stainless steel water bottle that "
                "keeps drinks cold for 24 hours and is designed for "
                "students and office workers."
            ),
            runtime=runtime,
        )

        responses = await result.get(timeout=120)

        print("\n========== CONCURRENT RESULTS ==========")

        for response in responses:
            print(f"\n--- {response.name} ---")
            print(response.content)

    finally:
        await runtime.stop_when_idle()


if __name__ == "__main__":
    asyncio.run(main())