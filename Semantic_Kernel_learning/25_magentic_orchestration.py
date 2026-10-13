import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from semantic_kernel.agents import (
    ChatCompletionAgent,
    MagenticOrchestration,
    StandardMagenticManager,
)
from semantic_kernel.agents.runtime import InProcessRuntime
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents import ChatMessageContent


load_dotenv(Path(__file__).resolve().parent / ".env")


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

    research_agent = ChatCompletionAgent(
        service=service,
        name="ResearchAgent",
        description="Researches and proposes suitable AI internship projects.",
        instructions=(
            "You are an AI project researcher. Propose practical project "
            "ideas using Python, FastAPI, RAG, and Semantic Kernel. Explain "
            "the problem, target users, and useful features. Do not claim "
            "that you performed external research."
        ),
    )

    technical_agent = ChatCompletionAgent(
        service=service,
        name="TechnicalAgent",
        description="Evaluates project architecture and technical feasibility.",
        instructions=(
            "You are an AI engineer. Evaluate project proposals for "
            "technical feasibility, architecture, implementation steps, "
            "and technologies. Identify risks and practical improvements. "
            "Build on the existing task context."
        ),
    )

    manager = StandardMagenticManager(
        chat_completion_service=service,
    )

    orchestration = MagenticOrchestration(
        members=[research_agent, technical_agent],
        manager=manager,
        agent_response_callback=agent_response_callback,
    )
 
    runtime = InProcessRuntime()
    runtime.start()

    try:
        result = await orchestration.invoke(
            task=(
                "Develop a realistic mini-project plan for two AI interns "
                "who have studied Python, FastAPI, RAG, and Semantic Kernel. "
                "The project should stand out, be achievable by beginners, "
                "and include the problem statement, main features, "
                "architecture, technology stack, and implementation steps."
            ),
            runtime=runtime,
        )

        final_output = await result.get(timeout=300)

        print("\n========== FINAL RESULT ==========")
        print(final_output)

    finally:
        await runtime.stop_when_idle()


if __name__ == "__main__":
    asyncio.run(main())